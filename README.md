# ✨ PromptRefiner (v1.0.0)

PromptRefiner, ham ve özensiz girilen promptları (istemleri), kullanıcının geçmişteki yazım stilini analiz ederek profesyonel hale getiren **yerel (local) ve görsel arayüzlü** bir yapay zeka aracıdır.

![Streamlit UI](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)

## 🚀 Özellikler

* **Görsel Arayüz (GUI):** Streamlit ile tarayıcı üzerinden kolay kullanım.
* **Kişisel Hafıza:** Geçmiş promptlarınızdan öğrenir (RAG teknolojisi).
* **Tamamen Ücretsiz:** Local Embedding (MiniLM) ve Google Gemini Flash kullanır.
* **Geçmiş Takibi:** Sol panelde eski promptlarınızı görebilirsiniz.

## 🛠️ Kurulum

1.  Bu klasörü indirin.
2.  `setup_env.bat` (veya `pip install -r requirements.txt`) ile kurulumu yapın.
3.  `.env` dosyasına Gemini API Key ekleyin.
4.  Modeli indirmek için bir kereye mahsus `python download_model.py` çalıştırın.

## 🎮 Nasıl Çalıştırılır?

Proje klasöründeki **`baslat.bat`** dosyasına çift tıklayın. Tarayıcınız otomatik açılacaktır.

---
**Teknolojiler:** Python, Streamlit, ChromaDB, Google Gemini, Sentence-Transformers.