import json
import chromadb
import os
import certifi
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

# SSL Sertifika sorunu için (Şirket ağı önlemi)
os.environ["SSL_CERT_FILE"] = certifi.where()

load_dotenv()

# 1. ChromaDB İstemcisi
client = chromadb.PersistentClient(path="./chroma_db")

# --- DEĞİŞİKLİK BURADA BAŞLIYOR (BEDAVA MODEL) ---
# OpenAI yerine 'all-MiniLM-L6-v2' adında meşhur, hızlı ve ücretsiz bir model kullanıyoruz.
# İlk çalıştırmada bu modeli internetten indirecek (yaklaşık 80-100MB).
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="./local_model"  # <--- DİKKAT: Artık internet adresi değil, klasör yolu
)
# -------------------------------------------------

# 2. Koleksiyonu Oluştur
collection = client.get_or_create_collection(
    name="my_prompt_style",
    embedding_function=ef
)


# 3. Veriyi Oku ve Yükle
def load_data():
    try:
        with open("data/my_prompts.json", "r", encoding="utf-8") as f:
            prompts = json.load(f)

        ids = [p["id"] for p in prompts]
        documents = [p["raw"] for p in prompts]
        metadatas = [{"refined": p["refined"], "category": p["category"]} for p in prompts]

        print("⏳ Model indiriliyor ve embeddingler oluşturuluyor, lütfen bekle...")
        collection.upsert(ids=ids, documents=documents, metadatas=metadatas)
        print(f"✅ {len(prompts)} adet prompt BEDAVA yöntemle hafızaya yüklendi!")

    except Exception as e:
        print(f"❌ Hata oluştu: {e}")


if __name__ == "__main__":
    load_data()