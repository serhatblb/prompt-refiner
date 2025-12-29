# ✨ PromptRefiner (v1.0.0)

PromptRefiner, ham ve özensiz girilen promptları (istemleri), kullanıcının geçmişteki yazım stilini ve teknik alışkanlıklarını analiz ederek profesyonel hale getiren **yerel (local) ve görsel arayüzlü** bir yapay zeka aracıdır.

![Streamlit UI](https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png)

## 🚀 Özellikler (v1.0.0)

* **Görsel Arayüz (GUI):** Streamlit ile tarayıcı üzerinden kolay kullanım.
* **Kişisel Hafıza (RAG):** Geçmiş promptlarınızdan öğrenir, sizin dilinizle konuşur.
* **Tamamen Ücretsiz:** Local Embedding (MiniLM) ve Google Gemini Flash kullanarak maliyetsiz çalışır.
* **Gizlilik Odaklı:** Verileriniz yerel bilgisayarınızda (ChromaDB) saklanır.
* **Geçmiş Takibi:** Yapılan tüm iyileştirmeleri kaydeder ve listeler.

## 🗺️ Yol Haritası (Product Roadmap)

PromptRefiner, kişisel bir araçtan kurumsal bir SaaS platformuna dönüşmeyi hedeflemektedir.

### 🟢 Faz 1: Kişisel MVP (Tamamlandı ✅)
- [x] Ham prompt'u kişisel stile göre refine etme (RAG)
- [x] Yerel Vektör Veritabanı entegrasyonu (ChromaDB Local)
- [x] Ücretsiz LLM Entegrasyonu (Google Gemini Flash)
- [x] Streamlit ile Görsel Arayüz (GUI)
- [x] Geçmiş (History) yönetimi

### 🔵 Faz 2: Cloud SaaS & API (Sıradaki Adım 🚧)
*Bireysel kullanıcılar için bulut tabanlı sürüm.*
- [ ] Backend'in FastAPI ile yeniden yazılması (API First mimari)
- [ ] Veritabanı geçişi (PostgreSQL & Hosted Vector DB)
- [ ] Kullanıcı Kimlik Doğrulama (JWT Auth / Google Login)
- [ ] Çoklu oturum ve bulut senkronizasyonu

### 🟠 Faz 3: Takım & Profesyonel Özellikler
*Takımlar ve yoğun kullanıcılar için gelişmiş araçlar.*
- [ ] **Takım Hafızası:** Ekip arkadaşlarının en iyi promptlarından öğrenme
- [ ] Browser Extension (Chrome/Edge eklentisi ile her yerden erişim)
- [ ] Prompt Şablonları ve Kategorilendirme
- [ ] Abonelik ve Ödeme altyapısı (Stripe)

### 🔴 Faz 4: Enterprise & On-Premise
*Büyük kurumlar için ölçeklenebilir altyapı.*
- [ ] SSO (Single Sign-On) Desteği
- [ ] Kurum içi (On-Premise) LLM kurulumu ve Fine-Tuning
- [ ] Gelişmiş Audit Log ve Güvenlik
- [ ] Kubernetes üzerinde ölçeklenebilir mimari

## 🛠️ Kurulum (v1 - Local)

1.  Repoyu klonlayın:
    ```bash
    git clone [https://github.com/kullaniciadi/prompt-refiner.git](https://github.com/kullaniciadi/prompt-refiner.git)
    cd prompt-refiner
    ```

2.  Sanal ortamı kurun ve bağımlılıkları yükleyin:
    ```bash
    # Windows için
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  `.env` dosyası oluşturun ve Gemini API Key ekleyin:
    ```
    GEMINI_API_KEY=AIzaSy...
    ```

4.  Modeli indirmek ve hafızayı kurmak için (bir kereye mahsus):
    ```bash
    python download_model.py
    python scripts/ingest_memory.py
    ```

## 🎮 Nasıl Çalıştırılır?

Proje klasöründeki **`baslat.bat`** dosyasına çift tıklayın. Tarayıcınız otomatik olarak açılacaktır.

---
**Teknolojiler:** Python, Streamlit, ChromaDB, Google Gemini, Sentence-Transformers.