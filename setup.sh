mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
mkdir -p ~/.streamlit/

# echo "[theme]
# primaryColor = ‘#84a3a7’
# backgroundColor = ‘#EFEDE8’
# secondaryBackgroundColor = ‘#fafafa’
# textColor= ‘#424242’
# font = ‘sans serif’
# [server]
# headless = true
# port = $PORT
# enableCORS = false
# " > ~/.streamlit/config.toml