import os
import requests
import shutil

# Model Bilgileri
MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
DEST_FOLDER = "./local_model"

# Klasör yapısını temizle (Sıfırdan kurulum)
if os.path.exists(DEST_FOLDER):
    print("🗑️ Eski model klasörü temizleniyor...")
    shutil.rmtree(DEST_FOLDER)
os.makedirs(DEST_FOLDER)
os.makedirs(os.path.join(DEST_FOLDER, "1_Pooling"))  # <-- İşte eksik olan klasör!

# İndirilecek Dosyalar Listesi (Eksik parça eklendi)
FILES = {
    "config.json": "",
    "model.safetensors": "",
    "tokenizer.json": "",
    "tokenizer_config.json": "",
    "vocab.txt": "",
    "special_tokens_map.json": "",
    "modules.json": "",
    "sentence_bert_config.json": "",
    "1_Pooling/config.json": "1_Pooling"  # <-- Kritik dosya burası
}

print(f"🚀 Model dosyaları '{DEST_FOLDER}' klasörüne indiriliyor...")

for file_name, subfolder in FILES.items():
    # HuggingFace URL'si
    url = f"https://huggingface.co/{MODEL_ID}/resolve/main/{file_name}"

    # Kaydedilecek Yer
    if subfolder:
        save_path = os.path.join(DEST_FOLDER, subfolder, "config.json")  # Dosya adı path içinde
    else:
        save_path = os.path.join(DEST_FOLDER, file_name)

    print(f"⬇️ İndiriliyor: {file_name}")

    try:
        # verify=False ile Şirket Güvenlik Duvarını (SSL) atlıyoruz
        response = requests.get(url, stream=True, verify=False)

        if response.status_code == 200:
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f"  ✅ Tamamlandı")
        else:
            print(f"  ❌ HATA: {file_name} bulunamadı! (Kod: {response.status_code})")

    except Exception as e:
        print(f"  ❌ BAĞLANTI HATASI: {e}")

print("\n✨ İndirme bitti! Şimdi 'ingest_memory.py' çalıştırabilirsin.")