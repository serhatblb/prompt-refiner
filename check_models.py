import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("🔍 Senin API Anahtarın İçin Açık Olan Modeller:")
print("-" * 40)

try:
    available_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ {m.name}")
            available_models.append(m.name)

    if not available_models:
        print("❌ Hiçbir model bulunamadı! API Key veya bölge kısıtlaması olabilir.")

except Exception as e:
    print(f"HATA: {e}")