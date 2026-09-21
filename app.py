# CÂND VINE APROBAREA, CODUL TĂU VA ARĂTA AȘA:
from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="ro">
    <head>
        <meta charset="UTF-8">
        <title>Tech Catalog 2026 - Versiunea Completă</title>
        
        <!-- CODUL TĂU DE RECLAME GOOGLE ADSENSE -->
        <script async src="https://googlesyndication.com" crossorigin="anonymous"></script>
    </head>
    <body>
        <!-- UNITATE DE RECLAMĂ TOP -->
        <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-5645412202166539" data-ad-slot="xxxxxx" data-ad-format="auto"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>

        <!-- AICI SE VA ÎNCĂRCA CATALOGUL TĂU MASIV, PERFECT FUNCȚIONAL -->
        <iframe src="ADRESA_CATALOGULUI_TĂU" width="100%" height="900px" style="border:none;"></iframe>
    </body>
    </html>
    """
    return render_template_string(html_content)

                for k, v in d.get("spec", {}).items():
                    st.write(f"• **{k}:** {v}")
            st.markdown("---")
