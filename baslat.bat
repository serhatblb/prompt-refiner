@echo off
title PromptRefiner V1 - Baslatiliyor...
echo.
echo =================================================
echo        PROMPT REFINER V1 (GUI MODE)
echo =================================================
echo.
echo Uygulama baslatiliyor, lutfen bekleyin...
echo Tarayiciniz otomatik acilacak.
echo.

call venv\Scripts\activate
streamlit run app_ui.py

pause