mkdir -p ~/.streamlit/

echo -e "\
[general]\n\
email = \"email@domain\"\n\
" > ~/.streamlit/credentials.toml

echo -e "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
