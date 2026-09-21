import random
from io import BytesIO
import requests
import streamlit as st

# Configurare Pagină Streamlit
st.set_page_config(
    page_title="Tech Catalog 2026 - Bază de Date Masivă",
    page_icon="📱",
    layout="wide",
)
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5645412202166539"
     crossorigin="anonymous"></script>
def verifica_bot_si_cookies():
    if "human_verified" not in st.session_state:
        st.session_state.human_verified = False

    if st.session_state.human_verified:
        return True

    st.markdown(
        "<br><h2 style='text-align: center;'>🛡️ Verificare de Securitate</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center; color: #666;'>Confirmați că sunteți om"
        " pentru a accesa catalogul.</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with st.container(border=True):
            st.markdown(
                """
                <div style="background-color: #f9f9f9; border: 1px solid #d3d3d3; border-radius: 4px; padding: 12px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                    <span style="font-size: 15px; font-weight: 500; color: #222; font-family: Roboto, sans-serif;">Verificare Anti-Automated Bot</span>
                    <div style="text-align: center;">
                        <img src="https://www.gstatic.com/recaptcha/api2/logo_48.png" width="32" height="32"><br>
                        <span style="font-size: 8px; color: #555;">reCAPTCHA</span>
                    </div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            nu_sunt_robot = st.checkbox("☑️ **Nu sunt robot**")
            accept_cookies = st.checkbox(
                "🍪 Accept cookie-urile de sesiune", value=True
            )

            st.markdown("<br>", unsafe_allow_html=True)
            submit = st.button(
                "✅ Intră în Catalog",
                type="primary",
                use_container_width=True,
            )

            if submit:
                if nu_sunt_robot and accept_cookies:
                    st.session_state.human_verified = True
                    st.success("Verificare reușită! Se încarcă catalogul...")
                    st.rerun()
                elif not nu_sunt_robot:
                    st.error("❌ Trebuie să bifezi caseta «Nu sunt robot»!")
                elif not accept_cookies:
                    st.warning(
                        "⚠️ Trebuie să accepți cookie-urile pentru a continua."
                    )

    return False


if not verifica_bot_si_cookies():
    st.stop()


# ==========================================
# 1. SISTEM DESCĂRCARE IMAGINI
# ==========================================
@st.cache_resource
def creeaza_sesiune_anti_bot():
    session = requests.Session()
    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"
        ),
        "Referer": "https://www.google.com/",
    })
    return session


http_session = creeaza_sesiune_anti_bot()


@st.cache_data(show_spinner=False)
def descarca_imagine_curata(url):
    if not url or not url.startswith("http"):
        return None
    try:
        response = http_session.get(url, timeout=2.5)
        if response.status_code == 200 and "image" in response.headers.get(
            "Content-Type", ""
        ):
            return BytesIO(response.content)
    except Exception:
        pass
    return None


# ==========================================
# 2. BAZĂ DE DATE MASIVĂ DUBLLATĂ PE PREZENT
# ==========================================
@st.cache_data
def genereaza_baza_de_date_2000():
    random.seed(2026)

    IMG_PHONE = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/IPhone_1st_Gen.svg/400px-IPhone_1st_Gen.svg.png"
    IMG_PHONE_BACK = "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/IPhone_1st_Gen_back.jpg/400px-IPhone_1st_Gen_back.jpg"
    IMG_HARDWARE = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Nvidia_GeForce_GTX_1080_Ti_FE.jpg/400px-Nvidia_GeForce_GTX_1080_Ti_FE.jpg"
    IMG_AUDIO = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/PlayStation_2_Fat_Console.png/400px-PlayStation_2_Fat_Console.png"

    luni = [
        "Ianuarie",
        "Februarie",
        "Martie",
        "Aprilie",
        "Mai",
        "Iunie",
        "Iulie",
        "August",
        "Septembrie",
        "Octombrie",
        "Noiembrie",
        "Decembrie",
    ]
    produse = []

    # 1. TELEFOANE MOBILE (DUBLE PE PREZENT: Apple, Samsung, Poco, Infinix, Motorola, Realme, Honor, etc.)
    branduri_telefoane = {
        "Apple": [
            (
                "iPhone 18",
                ["Pro Max", "Pro", "Plus", "Standard", "Air Slim"],
                2026,
                "A20 Pro (2nm)",
                "Viitor",
            ),
            (
                "iPhone 17",
                ["Pro Max", "Pro", "Plus", "Standard"],
                2025,
                "A19 Pro",
                "Prezent",
            ),
            (
                "iPhone 16",
                ["Pro Max", "Pro", "Plus", "Standard"],
                2024,
                "A18 Pro",
                "Prezent",
            ),
            (
                "iPhone 15",
                ["Pro Max", "Pro", "Plus", "Standard"],
                2023,
                "A17 Pro",
                "Prezent",
            ),
            (
                "iPhone 14",
                ["Pro Max", "Pro", "Plus", "Standard"],
                2022,
                "A16 Bionic",
                "Prezent",
            ),
            (
                "iPhone 13",
                ["Pro Max", "Pro", "Mini", "Standard"],
                2021,
                "A15 Bionic",
                "Prezent",
            ),
            ("iPhone 12", ["Pro Max", "Pro", "Standard"], 2020, "A14 Bionic", "Prezent"),
        ],
        "Samsung": [
            (
                "Galaxy S26",
                ["Ultra", "Plus", "FE", "Standard"],
                2026,
                "Snapdragon 8 Elite Gen 2",
                "Viitor",
            ),
            (
                "Galaxy S25",
                ["Ultra", "Plus", "FE", "Standard"],
                2025,
                "Snapdragon 8 Elite",
                "Prezent",
            ),
            (
                "Galaxy S24",
                ["Ultra", "Plus", "FE", "Standard"],
                2024,
                "Snapdragon 8 Gen 3",
                "Prezent",
            ),
            (
                "Galaxy S23",
                ["Ultra", "Plus", "FE", "Standard"],
                2023,
                "Snapdragon 8 Gen 2",
                "Prezent",
            ),
            (
                "Galaxy S22",
                ["Ultra", "Plus", "Standard"],
                2022,
                "Exynos 2200 / Snapdragon 8 Gen 1",
                "Prezent",
            ),
            (
                "Galaxy Z Fold",
                ["7 Ultra"],
                2026,
                "Snapdragon 8 Elite Gen 2",
                "Viitor",
            ),
            (
                "Galaxy Z Fold",
                ["6 Pro", "5 5G", "4 5G"],
                2024,
                "Snapdragon 8 Gen 3/2",
                "Prezent",
            ),
            (
                "Galaxy A",
                ["56 5G", "36 5G"],
                2026,
                "Exynos Mid-Range",
                "Viitor",
            ),
            (
                "Galaxy A",
                ["55 5G", "54 5G", "35 5G", "25 5G", "15 5G", "05s"],
                2024,
                "Exynos 1480 / Dimensity",
                "Prezent",
            ),
        ],
        "POCO": [
            (
                "POCO F6",
                ["Pro 5G", "Standard 5G"],
                2024,
                "Snapdragon 8s Gen 3 / 8 Gen 2",
                "Prezent",
            ),
            (
                "POCO X6",
                ["Pro 5G", "Standard 5G", "Neo 5G"],
                2024,
                "Dimensity 8300 Ultra",
                "Prezent",
            ),
            (
                "POCO M6",
                ["Pro 4G", "Pro 5G", "Standard 5G"],
                2024,
                "Helio G99 Ultra / Dimensity 6100+",
                "Prezent",
            ),
            (
                "POCO F5",
                ["Pro 5G", "Standard 5G"],
                2023,
                "Snapdragon 7+ Gen 2",
                "Prezent",
            ),
            (
                "POCO X5",
                ["Pro 5G", "Standard 5G"],
                2023,
                "Snapdragon 778G",
                "Prezent",
            ),
            ("POCO C65", ["4G"], 2023, "Helio G85", "Prezent"),
            ("POCO F7", ["Pro 5G", "Ultra 5G"], 2026, "Snapdragon 8 Elite", "Viitor"),
        ],
        "Infinix": [
            (
                "Infinix GT",
                ["20 Pro 5G", "10 Pro 5G"],
                2024,
                "Dimensity 8200 Ultimate",
                "Prezent",
            ),
            (
                "Infinix Note 40",
                ["Pro+ 5G", "Pro 5G", "Pro 4G", "Standard 4G"],
                2024,
                "Dimensity 7020 / Helio G99",
                "Prezent",
            ),
            (
                "Infinix Zero",
                ["40 5G", "30 5G", "Ultra"],
                2024,
                "Dimensity 8200",
                "Prezent",
            ),
            (
                "Infinix Hot",
                ["40 Pro", "40i", "30 5G"],
                2024,
                "Helio G99",
                "Prezent",
            ),
            ("Infinix Smart", ["8 Pro", "8"], 2024, "Unisoc T606", "Prezent"),
            (
                "Infinix GT 30",
                ["Pro 5G"],
                2026,
                "Dimensity Next-Gen",
                "Viitor",
            ),
        ],
        "Motorola": [
            (
                "Moto Edge 50",
                ["Ultra", "Pro", "Fusion"],
                2024,
                "Snapdragon 8s Gen 3",
                "Prezent",
            ),
            (
                "Moto Razr",
                ["50 Ultra", "50", "40 Ultra"],
                2024,
                "Snapdragon 8s Gen 3",
                "Prezent",
            ),
            (
                "Moto G",
                ["84 5G", "54 5G", "24 Power", "14"],
                2024,
                "Snapdragon 695 / Dimensity 7020",
                "Prezent",
            ),
            (
                "Moto Edge 60",
                ["Ultra", "Pro"],
                2026,
                "Snapdragon 8 Elite",
                "Viitor",
            ),
        ],
        "Realme": [
            (
                "Realme GT",
                ["6 5G", "6T 5G", "5 Pro"],
                2024,
                "Snapdragon 8s Gen 3",
                "Prezent",
            ),
            (
                "Realme 12",
                ["Pro+ 5G", "Pro 5G", "+ 5G", "Standard"],
                2024,
                "Snapdragon 7s Gen 2",
                "Prezent",
            ),
            (
                "Realme 11",
                ["Pro+ 5G", "Pro 5G"],
                2023,
                "Dimensity 7050",
                "Prezent",
            ),
            (
                "Realme GT 7",
                ["Pro 5G"],
                2026,
                "Snapdragon 8 Elite Gen 2",
                "Viitor",
            ),
        ],
        "Honor": [
            (
                "Honor Magic",
                ["6 Pro", "6 Lite", "5 Pro", "V2 Fold"],
                2024,
                "Snapdragon 8 Gen 3",
                "Prezent",
            ),
            (
                "Honor",
                ["200 Pro", "200 5G", "200 Lite", "90 5G"],
                2024,
                "Snapdragon 8s Gen 3 / 7 Gen 3",
                "Prezent",
            ),
            ("Honor Magic", ["7 Pro"], 2026, "Snapdragon 8 Elite", "Viitor"),
        ],
        "Nothing": [
            ("Nothing Phone", ["(2a) Plus", "(2a)"], 2024, "Dimensity 7350 Pro", "Prezent"),
            ("Nothing Phone", ["(2)"], 2023, "Snapdragon 8+ Gen 1", "Prezent"),
            ("Nothing Phone", ["(1)"], 2022, "Snapdragon 778G+", "Prezent"),
            ("Nothing Phone", ["(3) Pro"], 2026, "Snapdragon 8 Elite", "Viitor"),
        ],
        "Google": [
            (
                "Pixel 11",
                ["Pro XL", "Pro", "Standard"],
                2026,
                "Tensor G6",
                "Viitor",
            ),
            (
                "Pixel 10",
                ["Pro XL", "Pro", "Standard"],
                2025,
                "Tensor G5",
                "Prezent",
            ),
            (
                "Pixel 9",
                ["Pro XL", "Pro", "Standard", "9a"],
                2024,
                "Tensor G4",
                "Prezent",
            ),
            ("Pixel 8", ["Pro", "Standard", "8a"], 2023, "Tensor G3", "Prezent"),
            ("Pixel 7", ["Pro", "Standard", "7a"], 2022, "Tensor G2", "Prezent"),
        ],
        "Xiaomi": [
            (
                "Xiaomi 16",
                ["Ultra", "Pro"],
                2026,
                "Snapdragon 8 Elite Gen 2",
                "Viitor",
            ),
            (
                "Xiaomi 15",
                ["Ultra", "Pro", "Lite"],
                2025,
                "Snapdragon 8 Elite",
                "Prezent",
            ),
            (
                "Xiaomi 14",
                ["Ultra", "Pro", "T Pro", "Standard"],
                2024,
                "Snapdragon 8 Gen 3",
                "Prezent",
            ),
            (
                "Xiaomi 13",
                ["Ultra", "Pro", "T Pro"],
                2023,
                "Snapdragon 8 Gen 2",
                "Prezent",
            ),
            (
                "Redmi Note 13",
                ["Pro+ 5G", "Pro 5G", "Pro 4G", "Standard"],
                2024,
                "Dimensity 7200 Ultra",
                "Prezent",
            ),
        ],
        "OnePlus": [
            ("OnePlus 14", ["Pro"], 2026, "Snapdragon 8 Elite Gen 2", "Viitor"),
            (
                "OnePlus 13",
                ["Pro", "R", "Standard"],
                2025,
                "Snapdragon 8 Elite",
                "Prezent",
            ),
            (
                "OnePlus 12",
                ["R", "Standard"],
                2024,
                "Snapdragon 8 Gen 3",
                "Prezent",
            ),
            ("OnePlus 11", ["Standard"], 2023, "Snapdragon 8 Gen 2", "Prezent"),
            ("OnePlus Nord", ["4 5G", "CE 4", "3 5G"], 2024, "Snapdragon 7+ Gen 3", "Prezent"),
        ],
    }

    capacitati_stocare = ["128GB", "256GB", "512GB", "1TB"]

    for brand, modele in branduri_telefoane.items():
        for serie, variante, an, soc, stadiu in modele:
            for var in variante:
                for stoc in capacitati_stocare:
                    nume = f"{brand} {serie} {var} {stoc}"
                    pret = (
                        1300
                        if "Pro Max" in var or "Ultra" in var
                        else (
                            900
                            if "Pro" in var or "Fold" in var
                            else (350 if "M" in serie or "A" in serie or "Hot" in serie or "Smart" in serie else 650)
                        )
                    )
                    pret += (
                        capacitati_stocare.index(stoc) * 100
                        + random.randint(-20, 30)
                    )

                    produse.append({
                        "nume": nume,
                        "marca": brand,
                        "an": an,
                        "luna": random.choice(luni),
                        "pret_eur": pret,
                        "categorie": "Telefoane Mobile",
                        "stadiu": stadiu,
                        "statut": (
                            "🔮 Concept / Lansare Viitoare"
                            if stadiu == "Viitor"
                            else "🟢 Produs Existent / Lansat"
                        ),
                        "poza_fata": IMG_PHONE,
                        "poza_spate": IMG_PHONE_BACK,
                        "spec": {
                            "Stadiu Disponibilitate": (
                                "🔮 Viitor (Proiecție 2026+)"
                                if stadiu == "Viitor"
                                else "🟢 Prezent (Existent pe piață)"
                            ),
                            "Procesor": soc,
                            "Stocare": stoc,
                            "Ecran": (
                                "6.7\" AMOLED 120Hz"
                                if "Pro" in var or "GT" in var
                                else "6.5\" IPS/OLED 90Hz/120Hz"
                            ),
                            "🔋 Baterie": f"{random.randint(4500, 6000)} mAh",
                            "RAM": (
                                "16 GB"
                                if "Pro" in var or "Ultra" in var or "GT" in var
                                else "8 GB"
                            ),
                        },
                    })

    # 2. LAPTOPURI & WORKSTATIONS (EXTINS PE PREZENT)
    branduri_laptop = ["Apple", "ASUS", "Lenovo", "Dell", "HP", "Acer", "MSI"]
    linii_laptop = [
        ("Gaming FX", "Prezent"),
        ("ProBook", "Prezent"),
        ("ThinkPad X1", "Prezent"),
        ("ROG Strix", "Prezent"),
        ("Legion 5", "Prezent"),
        ("XPS 15", "Prezent"),
        ("MacBook Pro M3", "Prezent"),
        ("MacBook Air M2", "Prezent"),
        ("Acer Nitro 5", "Prezent"),
        ("HP Omen 16", "Prezent"),
        ("MacBook Pro M5", "Viitor"),
        ("ROG Strix 2026", "Viitor"),
    ]
    ram_options = ["8GB", "16GB", "32GB", "64GB"]

    for brand in branduri_laptop:
        for linie, stadiu_linie in linii_laptop:
            for ram in ram_options:
                ani_list = (
                    [(2023, "Prezent"), (2024, "Prezent"), (2025, "Prezent")]
                    if stadiu_linie == "Prezent"
                    else [(2026, "Viitor")]
                )
                for an, stadiu in ani_list:
                    for ecran_size in ["14\"", "16\""]:
                        nume = f"{brand} {linie} {ecran_size} ({ram} RAM, {an})"
                        pret = (
                            750
                            + (ram_options.index(ram) * 180)
                            + random.randint(30, 250)
                        )
                        if "MacBook" in linie or "ROG" in linie or "XPS" in linie:
                            pret += 450

                        produse.append({
                            "nume": nume,
                            "marca": brand,
                            "an": an,
                            "luna": random.choice(luni),
                            "pret_eur": pret,
                            "categorie": "Laptopuri & Workstations",
                            "stadiu": stadiu,
                            "statut": (
                                "🔮 Concept / Model 2026"
                                if stadiu == "Viitor"
                                else "🟢 Disponibil pe Piață"
                            ),
                            "poza_fata": IMG_HARDWARE,
                            "poza_spate": None,
                            "spec": {
                                "Stadiu": (
                                    "🔮 Viitor (Proiecție 2026)"
                                    if stadiu == "Viitor"
                                    else "🟢 Prezent (Lansat)"
                                ),
                                "Procesor": (
                                    "Intel Core i7/i9 / AMD Ryzen 7/9 / Apple M-Series"
                                ),
                                "Memorie RAM": ram,
                                "Stocare SSD": (
                                    f"{random.choice([512, 1024, 2048])} GB NVMe"
                                ),
                                "Ecran": f"{ecran_size} IPS/OLED 144Hz/165Hz",
                            },
                        })

    # 3. HARDWARE GPU & CPU (EXTINS PREZENT)
    producatori_gpu = ["NVIDIA", "ASUS", "MSI", "Gigabyte", "AMD", "SAPPHIRE", "Zotac"]
    gpus_prezent = [
        ("RTX 4090 24GB", 2023),
        ("RTX 4080 Super 16GB", 2024),
        ("RTX 4070 Ti Super 16GB", 2024),
        ("RTX 4070 Super 12GB", 2024),
        ("RTX 4060 Ti 16GB", 2023),
        ("RX 7900 XTX 24GB", 2023),
        ("RX 7800 XT 16GB", 2023),
        ("RX 7700 XT 12GB", 2023),
    ]
    gpus_viitor = [
        ("RTX 5090 32GB", 2026),
        ("RTX 5080 16GB", 2026),
        ("RX 8900 XT 24GB", 2026),
    ]

    for prod in producatori_gpu:
        for gpu, an in gpus_prezent:
            for ed in ["OC Edition", "TUF Gaming", "Gaming X Trio", "Dual Fan"]:
                produse.append({
                    "nume": f"{prod} {gpu} {ed}",
                    "marca": prod,
                    "an": an,
                    "luna": random.choice(luni),
                    "pret_eur": random.randint(350, 1950),
                    "categorie": "Plăci Video (GPU)",
                    "stadiu": "Prezent",
                    "statut": "🟢 Produs Lansat Existent",
                    "poza_fata": IMG_HARDWARE,
                    "poza_spate": None,
                    "spec": {
                        "Stadiu": "🟢 Prezent (Existent)",
                        "VRAM": gpu.split()[-2] + " " + gpu.split()[-1] if "GB" in gpu else "12GB",
                        "Interfață": "PCIe 4.0/5.0",
                    },
                })
        for gpu, an in gpus_viitor:
            for ed in ["OC Edition", "ROG Strix Next", "AERO White"]:
                produse.append({
                    "nume": f"{prod} {gpu} {ed}",
                    "marca": prod,
                    "an": an,
                    "luna": random.choice(luni),
                    "pret_eur": random.randint(1200, 2500),
                    "categorie": "Plăci Video (GPU)",
                    "stadiu": "Viitor",
                    "statut": "🔮 Lansare Viitoare 2026",
                    "poza_fata": IMG_HARDWARE,
                    "poza_spate": None,
                    "spec": {
                        "Stadiu": "🔮 Viitor (Lansare 2026)",
                        "VRAM": gpu.split()[-2] + " " + gpu.split()[-1] if "GB" in gpu else "16GB",
                        "Interfață": "PCIe 5.0",
                    },
                })

    # 4. CONSOLE, AUDIO, SMARTWATCH (EXTINS PREZENT)
    alte_categorii = [
        (
            "Console de Jocuri",
            [
                ("Sony PS5 Slim Digital", 2023, "Prezent"),
                ("Sony PS5 Pro 2TB", 2024, "Prezent"),
                ("Xbox Series X 2TB", 2024, "Prezent"),
                ("Xbox Series S 1TB Carbon", 2023, "Prezent"),
                ("Nintendo Switch OLED", 2022, "Prezent"),
                ("Steam Deck OLED 1TB", 2023, "Prezent"),
                ("ASUS ROG Ally X", 2024, "Prezent"),
                ("Nintendo Switch 2 OLED", 2026, "Viitor"),
                ("Sony PlayStation 6 Concept", 2026, "Viitor"),
            ],
        ),
        (
            "Audio & Căști",
            [
                ("Sony WH-1000XM5", 2023, "Prezent"),
                ("Sony WF-1000XM5", 2023, "Prezent"),
                ("Apple AirPods Max 2", 2024, "Prezent"),
                ("Apple AirPods Pro 2 USB-C", 2023, "Prezent"),
                ("Bose QuietComfort Ultra", 2024, "Prezent"),
                ("Sennheiser Momentum 4", 2023, "Prezent"),
                ("AirPods Pro 3 Concept", 2026, "Viitor"),
            ],
        ),
        (
            "Smartwatch-uri",
            [
                ("Apple Watch Series 10", 2024, "Prezent"),
                ("Apple Watch Series 9", 2023, "Prezent"),
                ("Apple Watch Ultra 2", 2023, "Prezent"),
                ("Samsung Galaxy Watch 7 Pro", 2024, "Prezent"),
                ("Garmin Fenix 8 Solar", 2024, "Prezent"),
                ("Garmin Epix Pro Gen 2", 2023, "Prezent"),
                ("Apple Watch Ultra 3", 2026, "Viitor"),
            ],
        ),
    ]

    for cat_nume, modele in alte_categorii:
        for mod, an, stadiu in modele:
            for ed in ["Standard Edition", "Pro Edition", "Special Color"]:
                brand = mod.split()[0]
                produse.append({
                    "nume": f"{mod} ({ed})",
                    "marca": brand,
                    "an": an,
                    "luna": random.choice(luni),
                    "pret_eur": random.randint(200, 1100),
                    "categorie": cat_nume,
                    "stadiu": stadiu,
                    "statut": (
                        "🔮 Viitor (2026+)"
                        if stadiu == "Viitor"
                        else "🟢 Prezent (Lansat)"
                    ),
                    "poza_fata": IMG_AUDIO,
                    "poza_spate": None,
                    "spec": {
                        "Stadiu": (
                            "🔮 Viitor" if stadiu == "Viitor" else "🟢 Prezent"
                        ),
                        "Garanție": "24 Luni Producător",
                    },
                })

    return produse


DISPOZITIVE_REALE = genereaza_baza_de_date_2000()

# ==========================================
# 3. CONVERSIE MONEDE
# ==========================================
RATII_SCHIMB = {"EUR": 1.0, "USD": 1.10, "RON": 4.97}


def formateaza_pret(pret_eur, optiunemonedă):
    if not pret_eur:
        return "N/A"
    p_eur = int(pret_eur)
    p_usd = int(pret_eur * RATII_SCHIMB["USD"])
    p_ron = int(pret_eur * RATII_SCHIMB["RON"])

    if optiunemonedă == "Doar EUR (€)":
        return f"**{p_eur:,} €**".replace(",", ".")
    elif optiunemonedă == "Doar USD ($)":
        return f"**${p_usd:,}**".replace(",", ".")
    elif optiunemonedă == "Doar RON (lei)":
        return f"**{p_ron:,} RON**".replace(",", ".")
    else:
        return (
            f"**{p_eur:,} €** | **${p_usd:,}** | **{p_ron:,} RON**".replace(
                ",", "."
            )
        )


# ==========================================
# 4. INTERFAȚĂ ȘI FILTRE
# ==========================================
MARCI = sorted(list(set(d["marca"] for d in DISPOZITIVE_REALE)))
CATEGORII = sorted(list(set(d["categorie"] for d in DISPOZITIVE_REALE)))
ANII = sorted(list(set(d["an"] for d in DISPOZITIVE_REALE)), reverse=True)

st.sidebar.header("🔍 Filtrare & Setări")

# --- SECTIUNEA PREZENT vs VIITOR ---
st.sidebar.subheader("⏳ Stadiu Lansare Produs")
stadiu_sel = st.sidebar.radio(
    "Alege stadiul produsului:",
    [
        "Toate Produsele",
        "🟢 Prezent (Lansate / Existente)",
        "🔮 Viitor (Concepte & Lansări 2026+)",
    ],
    index=0,
)
st.sidebar.markdown("---")

cautare_text = st.sidebar.text_input(
    "🔎 Căutare liberă:", placeholder="ex: POCO F6, Infinix GT, iPhone 15, RTX 4070..."
)
categorie_sel = st.sidebar.selectbox(
    "Alege Categoria:", ["Toate Categoriile"] + CATEGORII
)
marca_sel = st.sidebar.selectbox("Alege Marca:", ["Toate Mărcile"] + MARCI)
an_sel = st.sidebar.selectbox(
    "Alege Anul Lansării:", ["Toți Anii"] + [str(a) for a in ANII]
)

st.sidebar.markdown("---")
st.sidebar.header("💱 Afișare Monedă")
moneda_sel = st.sidebar.selectbox(
    "Selectează valuta preferată:",
    ["Toate (EUR / USD / RON)", "Doar EUR (€)", "Doar USD ($)", "Doar RON (lei)"],
)

st.sidebar.markdown("---")
if st.sidebar.button("🧹 Deconectare / Resetare reCAPTCHA"):
    st.session_state.human_verified = False
    st.rerun()

# Aplicare Filtre
filtrate = DISPOZITIVE_REALE

# Filtru Stadiu: Prezent vs Viitor
if stadiu_sel == "🟢 Prezent (Lansate / Existente)":
    filtrate = [d for d in filtrate if d["stadiu"] == "Prezent"]
elif stadiu_sel == "🔮 Viitor (Concepte & Lansări 2026+)":
    filtrate = [d for d in filtrate if d["stadiu"] == "Viitor"]

if cautare_text:
    filtrate = [
        d
        for d in filtrate
        if cautare_text.lower() in d["nume"].lower()
        or cautare_text.lower() in d["marca"].lower()
    ]

if categorie_sel != "Toate Categoriile":
    filtrate = [d for d in filtrate if d["categorie"] == categorie_sel]

if marca_sel != "Toate Mărcile":
    filtrate = [d for d in filtrate if d["marca"] == marca_sel]

if an_sel != "Toți Anii":
    filtrate = [d for d in filtrate if str(d["an"]) == an_sel]

# Header & Contor Produse
st.title("🖥️ Tech Catalog 2026")
st.caption(
    f"📅 Bază de date structurată (Prezent vs Viitor) | Total în sistem:"
    f" **{len(DISPOZITIVE_REALE)}** produse"
)
st.markdown(
    f"Produse afișate conform filtrului selectat (**{stadiu_sel}**):"
    f" **{len(filtrate)}**"
)
st.markdown("---")

# ==========================================
# 5. AFISARE PRODUSE CU PAGINARE
# ==========================================
if not filtrate:
    st.warning("⚠️ Niciun produs nu corespunde filtrelor selectate.")
else:
    # Configurare Paginare
    PRODUSE_PE_PAGINA = 12
    total_pagini = max(1, (len(filtrate) + PRODUSE_PE_PAGINA - 1) // PRODUSE_PE_PAGINA)

    col_pag1, col_pag2 = st.columns([1, 3])
    with col_pag1:
        pagina_curenta = st.number_input(
            f"Pagina (1 - {total_pagini}):",
            min_value=1,
            max_value=total_pagini,
            value=1,
            step=1,
        )

    start_idx = (pagina_curenta - 1) * PRODUSE_PE_PAGINA
    end_idx = start_idx + PRODUSE_PE_PAGINA
    produse_pagina = filtrate[start_idx:end_idx]

    cols = st.columns(3)
    for index, d in enumerate(produse_pagina):
        col = cols[index % 3]
        with col:
            st.subheader(d["nume"])

            # Etichetă vizuală explicită
            if d.get("stadiu") == "Prezent":
                st.markdown("🟢 **PRODUS LANSAT / EXISTENT**")
            else:
                st.markdown("🔮 **PROIECȚIE / LANSARE VIITOARE**")

            if "statut" in d:
                st.caption(d["statut"])

            img_fata = descarca_imagine_curata(d.get("poza_fata"))
            img_spate = descarca_imagine_curata(d.get("poza_spate"))

            if img_fata or img_spate:
                c1, c2 = st.columns(2)
                with c1:
                    if img_fata:
                        st.image(img_fata, caption="Față", use_container_width=True)
                with c2:
                    if img_spate:
                        st.image(img_spate, caption="Spate", use_container_width=True)

            st.markdown(
                f"**Marcă:** `{d['marca']}` | **An:** `{d['an']}` ({d['luna']})"
            )
            string_pret = formateaza_pret(d.get("pret_eur", 0), moneda_sel)
            st.markdown(f"💰 **Preț:** {string_pret}")

            with st.expander("📋 Specificații Tehnice", expanded=True):
                for k, v in d.get("spec", {}).items():
                    st.write(f"• **{k}:** {v}")
            st.markdown("---")
