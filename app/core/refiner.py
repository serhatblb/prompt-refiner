import chromadb
import os
import certifi
import google.generativeai as genai
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

# 1. SSL Sertifika Fix (Şirket ağı için şart)
os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv()

# 2. Google Gemini Ayarları (Bedava LLM)
# .env dosyasında GEMINI_API_KEY olduğundan emin ol
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Model seçimi: 'gemini-1.5-flash' hızlı ve ücretsizdir.
# Listendeki en güvenli ve ücretsiz model bu
model = genai.GenerativeModel('gemini-flash-latest')

# 3. ChromaDB ve Embedding Ayarları (Local & Bedava)
# ingest_memory.py dosyasındaki model ile AYNI olmak zorunda!
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="./local_model"  # <--- Burayı da klasör yolu yapıyoruz
)
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="my_prompt_style", embedding_function=ef)


def refine_prompt(user_input: str):
    try:
        # A. Benzer örnekleri bul (RAG)
        results = collection.query(query_texts=[user_input], n_results=3)

        examples = ""
        # Eğer sonuç varsa formatla, yoksa boş geç
        if results['documents'] and len(results['documents'][0]) > 0:
            for i, doc in enumerate(results['documents'][0]):
                refined_version = results['metadatas'][0][i]['refined']
                examples += f"ÖRNEK {i + 1}:\nGirdi: {doc}\nÇıktı: {refined_version}\n---\n"
        else:
            examples = "Henüz yeterli örnek yok, genel en iyi pratikleri kullan."

        # B. Prompt Hazırla
        system_instruction = f"""
        Sen 'PromptRefiner' adında kişisel bir asistansın.
        Görevin: Kullanıcının girdiği ham (raw) fikri, onun geçmişteki kaliteli prompt stiline uygun hale getirmek.

        KULLANICININ STİL ÖRNEKLERİ:
        {examples}

        TALİMAT:
        1. Kullanıcının niyetini anla.
        2. Eğer örnekler varsa, o örneklerdeki yapı, ton ve detay seviyesini taklit et.
        3. Sadece refine edilmiş promptu yaz. Başka açıklama, giriş veya 'işte promptunuz' gibi yazılar yazma.
        4. Promptu doğrudan kullanıma hazır ver.
        """

        # C. Gemini'ye Gönder
        response = model.generate_content(
            f"{system_instruction}\n\nHAM GİRDİ: {user_input}"
        )

        return response.text.strip()

    except Exception as e:
        return f"Hata oluştu: {str(e)}"