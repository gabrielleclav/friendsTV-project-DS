mkdir -p ~/.streamlit/
echo "\
[theme]\n\
primaryColor = '#5093F6'\n\
backgroundColor = '#000000'\n\
secondaryBackgroundColor = '#3E5661'\n\
textColor= '#FFFFFF'\n\
font = 'sans serif'\n\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
# " > ~/.streamlit/config.toml


# mkdir -p ~/.streamlit/
# echo "\
# [server]\n\
# headless = true\n\
# port = $PORT\n\
# enableCORS = false\n\
# \n\
# " > ~/.streamlit/config.toml
# # mkdir -p ~/.streamlit/

# echo "[theme]

# primaryColor = '#5093F6' #blue

# backgroundColor = '#000000' #black

# secondaryBackgroundColor = '#3E5661'

# textColor = '#FFFFFF' #white

# font = "sans serif"
# [server]
# headless = true
# port = $PORT
# enableCORS = false
# " > ~/.streamlit/config.toml