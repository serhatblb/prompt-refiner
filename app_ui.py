import streamlit as st
from app.core.refiner import refine_prompt
from app.memory.history import save_to_history, load_history

# Sayfa Ayarları
st.set_page_config(page_title="PromptRefiner", page_icon="✨", layout="centered")

st.title("✨ PromptRefiner")
st.markdown("Ham fikrini gir, senin tarzında profesyonel prompta dönüşsün.")

# Sol taraf (Sidebar) - Geçmiş
with st.sidebar:
    st.header("📜 Geçmiş")
    history = load_history()
    # Geçmiş varsa göster
    if history:
        for item in history:
            # Timestamp kontrolü ve dilimleme hatası olmaması için
            time_str = item.get('timestamp', '')[11:16]
            raw_str = item.get('raw', '')[:20]

            with st.expander(f"{time_str} - {raw_str}..."):
                st.code(item['refined'], language="text")
    else:
        st.info("Henüz geçmiş yok.")

# Ana Ekran
user_input = st.text_area("Ham Prompt:", height=100, placeholder="Örn: bana python ile bir api yaz")

if st.button("Refine Et ✨", type="primary"):
    if user_input:
        with st.spinner("Hafıza taranıyor ve prompt iyileştiriliyor..."):
            try:
                refined_output = refine_prompt(user_input)
                save_to_history(user_input, refined_output)

                st.success("İşlem Başarılı!")
                st.text_area("Sonuç:", value=refined_output, height=200)
                st.info("Kopyalamak için sağ üstteki kopyala ikonunu kullanabilirsin.")

                # Sayfayı yenile ki geçmiş güncellensin (Rerun)
                st.rerun()
            except Exception as e:
                st.error(f"Hata oluştu: {e}")
    else:
        st.warning("Lütfen bir şeyler yaz.")