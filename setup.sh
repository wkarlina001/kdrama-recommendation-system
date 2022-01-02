mkdir -p ~/.streamlit/

ech "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headles = true\n\
\n\
" > ~/.streamlit/config.toml