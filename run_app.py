import sys
import os
from streamlit.web import cli as stcli

if __name__ == "__main__":
    # Exe içindeki dosya yolunu bul
    if getattr(sys, 'frozen', False):
        app_path = os.path.join(sys._MEIPASS, "app_ui.py")
    else:
        app_path = "app_ui.py"

    # Streamlit komutunu simüle et
    sys.argv = ["streamlit", "run", app_path, "--global.developmentMode=false"]
    sys.exit(stcli.main())