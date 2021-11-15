mkdir -p ~/.streamlit/
echo "[theme]
primaryColor = '#5093F6'
backgroundColor = '#000000'
secondaryBackgroundColor = '#3E5661'
textColor= '#FFFFFF'
font = ‘sans serif’
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml