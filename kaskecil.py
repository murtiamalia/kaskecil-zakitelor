import streamlit as st
import pandas as pd
import datetime
from io import BytesIO
import os
import io

st.markdown("""
<style>

:root {
    --royal-blue: #3A2D71;
    --tea-pink: #E9D1E1;
    --yellow: #F6D60D;
    --baby-pink: #A0BAC0;
    --soft-red: #FFB4B4;
}

/* ============================== */
/*         LOGIN CONTAINER        */
/* ============================== */
.login-container {
    background: #F5F7FF !important;      /* background terang */
    border-radius: 15px !important;
    padding: 30px !important;
    box-shadow: 0 4px 25px rgba(0,0,0,0.15) !important;
    border: 1px solid #D6DAF0 !important;
}

/* Judul login */
.login-title {
    color: #1B1F3B !important;
    font-size: 28px !important;
    font-weight: 800 !important;
    text-align: center !important;
    margin-bottom: 20px !important;
}

/* ============================== */
/*         INPUT FIELD LOGIN      */
/* ============================== */
.stTextInput label {
    color: #1B1F3B !important;  /* warna label terlihat */
    font-weight: 700 !important;
    font-size: 16px !important;
    margin-bottom: 8px !important;
}

/* Input box */
.stTextInput input {
    background-color: #FFFFFF !important;
    color: #1B1F3B !important;
    border: 2px solid #6A5ACD !important;  /* ungu medium */
    border-radius: 10px !important;
    padding: 10px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}

/* Fokus pada input */
.stTextInput input:focus {
    border-color: #483D8B !important;      /* ungu gelap */
    box-shadow: 0 0 5px rgba(72,61,139,0.6) !important;
}

/* Placeholder lebih gelap */
input::placeholder {
    color: #555 !important;
    opacity: 1 !important;
}

/* ============================== */
/*         BUTTON LOGIN           */
/* ============================== */
.stButton > button {
    background: linear-gradient(135deg, #6A5ACD, #483D8B) !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 12px 20px !important;
    font-size: 17px !important;
    font-weight: 700 !important;
    border: none !important;
    cursor: pointer !important;
    width: 100% !important;
    transition: 0.2s ease-in-out !important;
}

/* Hover effect */
.stButton > button:hover {
    background: linear-gradient(135deg, #7B6DFF, #5A4DDE) !important;
    transform: scale(1.02) !important;
    box-shadow: 0 3px 10px rgba(0,0,0,0.2) !important;
}

/* ============================== */
/*       SIDEBAR / NAV MENU       */
/*   (supaya teks terlihat jelas) */
/* ============================== */
.sidebar, .sidebar-content, .css-1d391kg, .css-1v0mbdj {
    color: #1B1F3B !important;
}

/* Link / menu tulisan */
.sidebar a, .css-17eq0hr, .css-1lcbmhc, .css-nxf4we {
    color: #1B1F3B !important;
    font-weight: 700 !important;
    font-size: 16px !important;
}

/* ============================== */
/*   HILANGKAN OPACITY CONTAINER  */
/*   (agar teks tidak memudar)    */
/* ============================== */
.block-container {
    opacity: 1 !important;
}

/* ============================== */
/*      TOMBOL UMUM STREAMLIT     */
/* ============================== */
button[kind="secondary"] {
    background-color: #ffffff !important;
    border: 2px solid #6A5ACD !important;
    color: #1B1F3B !important;
    font-weight: 600 !important;
}

button[kind="secondary"]:hover {
    background-color: #ECEBFF !important;
}

/* ============================== */
/*   FIX KECIL – TEKS TERSEMBUNYI */
/* ============================== */
* {
    text-shadow: none !important;
}


/* ============================================================
       TOMBOL KUNING SOFT (TRANSPARANSI 60%) — FINAL
   ============================================================ */

:root {
    --yellow-soft: rgba(246,214,13,0.6);   /* kuning 60% */
    --yellow-soft-hover: rgba(246,214,13,0.75);
    --yellow-border: #e0bf0a;
}

/* Semua tombol dalam wrapper khusus */
.wrap-save button,
.wrap-clear button,
.wrap-download button,
.wrap-reset button,
button[data-testid="baseButton-primary"],   /* UNDuh Excel */
.stButton > button,                         /* tombol biasa */
button[kind="secondary"]                    /* Logout */
{
    background-color: var(--yellow-soft) !important;
    color: #000 !important;
    font-weight: 800 !important;   /* bold */
    border-radius: 10px !important;
    border: 2px solid var(--yellow-border) !important;
    padding: 10px 22px !important;
    font-size: 15px !important;
    height: 45px !important;

    box-shadow:
        0 3px 8px rgba(0,0,0,0.15),
        0 0 10px rgba(246,214,13,0.20) !important;

    transition: 0.22s ease-in-out !important;
}

/* Hover */
.wrap-save button:hover,
.wrap-clear button:hover,
.wrap-download button:hover,
.wrap-reset button:hover,
button[data-testid="baseButton-primary"]:hover,
.stButton > button:hover,
button[kind="secondary"]:hover
{
    background-color: var(--yellow-soft-hover) !important;
    transform: translateY(-2px);
    box-shadow:
        0 4px 14px rgba(0,0,0,0.22),
        0 0 12px rgba(246,214,13,0.45) !important;
}

/* Active */
.wrap-save button:active,
.wrap-clear button:active,
.wrap-download button:active,
.wrap-reset button:active,
button[data-testid="baseButton-primary"]:active,
.stButton > button:active,
button[kind="secondary"]:active
{
    transform: scale(0.97);
}

/* =====================================================
                REMOVE WHITE HEADER GAP
   ===================================================== */

div.block-container { padding-top: 0 !important; }
header[data-testid="stHeader"] { height: 0 !important; padding: 0 !important; }
section[data-testid="stToolbar"] { display: none !important; }
div[data-testid="stAppViewBlockContainer"] { padding-top: 0 !important; }

html, body, [data-testid="stApp"] {
    background: white !important;
}

body.login-mode [data-testid="stApp"] {
    background: transparent !important;
}

/* -----------------------------------------
        LOGIN WRAPPER TENGAH
------------------------------------------*/
.login-wrapper {
    width: 420px;
    margin: 110px auto 0 auto;
    text-align: center;
}

/* -----------------------------------------
        LOGIN CARD — GLASS (TANPA NEON)
------------------------------------------*/
.login-card {
    background: rgba(255,255,255,0.40);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    padding: 40px 26px;
    border-radius: 20px;

    border: 2px solid rgba(255,255,255,0.55);
    box-shadow: 0 6px 22px rgba(0,0,0,0.18);
}

/* -----------------------------------------
        TITLE & SUBTITLE (BESAR + TENGAH)
------------------------------------------*/
.login-title {
    font-size: 38px;
    font-weight: 900;
    text-align: center;
    color: var(--royal-blue);
    margin-bottom: 6px;
}

.login-sub {
    font-size: 18px;
    font-weight: 700;
    text-align: center;
    color: #333;
    margin-bottom: 20px;
}


/* =====================================================
        INPUT FORM FULL BORDER BLUE (FIX)
===================================================== */

.stTextInput > div > div > input,
.stNumberInput > div > div > input {
    border: 2px solid var(--royal-blue) !important;
    border-radius: 10px !important;
    background: white !important;
    box-shadow: none !important;
}

.stTextArea textarea {
    border: 2px solid var(--royal-blue) !important;
    border-radius: 10px !important;
    background: white !important;
}

.stDateInput > div > div > input {
    border: 2px solid var(--royal-blue) !important;
    border-radius: 10px !important;
    background: white !important;
}

.stSelectbox > div > div {
    border: 2px solid var(--royal-blue) !important;
    border-radius: 10px !important;
    background: white !important;
}

.stSelectbox > div[data-baseweb="select"] {
    border-color: var(--royal-blue) !important;
}

.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus,
.stTextArea textarea:focus,
.stDateInput > div > div > input:focus,
.stSelectbox > div[data-baseweb="select"]:focus-within {
    border-color: var(--royal-blue) !important;
    box-shadow: 0 0 10px rgba(58,45,113,0.4) !important;
}


/* =====================================================
                SIDEBAR PREMIUM
   ===================================================== */

[data-testid="stSidebar"] {
    background: white !important;
    padding: 30px 18px 40px 18px;
    border-right: 2px solid var(--royal-blue);
    box-shadow: 6px 0 20px rgba(0,0,0,0.10);
}

[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2 {
    color: var(--royal-blue) !important;
    font-weight: 800 !important;
    margin-bottom: 18px;
}

div[role="radiogroup"] {
    gap: 10px;
    display: flex;
    flex-direction: column;
}

div[role="radiogroup"] > label {
    padding: 14px 16px;
    font-size: 15px;
    font-weight: 600;
    border-radius: 14px;
    cursor: pointer;
    border: none !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    transition: all 0.22s ease-in-out;
}

div[role="radiogroup"] > label:nth-child(1) {
    background: linear-gradient(135deg, #E9D1E1, #FFFFFF);
    color: #3A2D71 !important;
}

div[role="radiogroup"] > label:nth-child(2) {
    background: linear-gradient(135deg, #A0BAC0, #DDE7EB);
    color: #1a1a1a !important;
}

div[role="radiogroup"] > label:nth-child(3) {
    background: linear-gradient(135deg, #F6D60D, #FFF6C5);
    color: #4A4008 !important;
}

div[role="radiogroup"] > label:nth-child(4) {
    background: linear-gradient(135deg, #E9D1E1, #F7E8F4);
    color: #3A2D71 !important;
}

div[role="radiogroup"] > label:nth-child(5) {
    background: linear-gradient(135deg, #FFB4B4, #FFDADA);
    color: #7a0000 !important;
}

div[role="radiogroup"] > label:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.14);
}

div[role="radiogroup"] > label[data-selected="true"] {
    background: var(--royal-blue) !important;
    color: white !important;
    box-shadow: 0 6px 18px rgba(58,45,113,0.45) !important;
    transform: translateY(-2px) scale(1.02);
}
/* ============================================================
   HEADER UTAMA — BANNER BIRU ELEGAN
   ============================================================ */

.main-header {
    width: 100%;
    padding: 18px 0;
    text-align: center;
    background: linear-gradient(135deg, #3A2D71, #50409B);
    color: white;
    font-size: 28px;
    font-weight: 900;
    border-radius: 10px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.18);
    margin-bottom: 25px;
}
/* Tambahkan warna teks agar terlihat jelas di dalam input */
.stTextInput input,
.stNumberInput input,
.stTextArea textarea,
.stDateInput input {
    color: #000 !important; /* Warna teks di dalam input */
}

/* Selectbox (Dropdown) */
.stSelectbox > div > div {
    /* ... kode lama ... */
    color: #000 !important; /* Warna teks di selectbox utama */
}

/* Teks label untuk st.sidebar.radio (Navigasi) */
[data-testid="stSidebar"] div.stRadio > label {
    color: #333 !important; /* Warna teks label radio (misalnya 'Navigasi') */
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# ===============         LOGIN       ==================
# =====================================================

if "logged" not in st.session_state:
    st.session_state.logged = False

### FIX BACKGROUND LOGIN ACTIVATION
if not st.session_state.logged:
    st.markdown("<div clas='login-bg-gradient'></div>", unsafe_allow_html=True)
    st.markdown("<script>document.body.classList.add('login-mode');</script>", unsafe_allow_html=True)
else:
    st.markdown("<script>document.body.classList.remove('login-mode');</script>", unsafe_allow_html=True)

def login_page():

    st.markdown("<div class='login-wrapper'>", unsafe_allow_html=True)

    st.markdown("""
        <div class="login-card">
            <div class="login-title">APLIKASI KAS KECIL</div>
            <div class="login-sub">SILAKAN LOGIN</div>
        </div>
    """, unsafe_allow_html=True)

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        login = st.form_submit_button("Login")

        if login:
            if username == "kaskecilzakitelor" and password == "adminz4k1":
                st.session_state.logged = True
                st.rerun()
            else:
                st.error("Username atau password salah!")

    st.markdown("</div>", unsafe_allow_html=True)

if not st.session_state.logged:
    login_page()
    st.stop()
# =====================================================
# =============== HEADER UTAMA APLIKASI ===============
# =====================================================

st.markdown("""
    <div class="main-header">
        PENCATATAN KAS KECIL ZAKI TELOR
    </div>
""", unsafe_allow_html=True)


# =====================================================
# ===============     SIDEBAR MENU     =================
# =====================================================

with st.sidebar:
    if st.button("Logout"):
        st.session_state.logged = False
        st.rerun()

st.sidebar.title("📘 Menu Utama")
menu = st.sidebar.radio(
    "Navigasi",
    [
        "📌 Beranda",
        "🧾 Transaksi",
        "📑 Laporan Bulanan",
        "📥 Unduh Laporan Kas Kecil",
        "🗑 Reset Semua Transaksi"
    ]
)

# =====================================================
# ======================= DATA ========================
# =====================================================

SALDO_AWAL = 5000000
FILE_PATH = "data_transaksi.csv"

COA = {
    "Beban ATK": "511-001",
    "Beban Transport": "511-002",
    "Beban Konsumsi": "511-003",
    "Beban Lainnya": "511-999",
}

def load_transaksi():
    if os.path.exists(FILE_PATH):
        df = pd.read_csv(FILE_PATH)
        st.session_state.transaksi = df.to_dict("records")
    else:
        st.session_state.transaksi = []

def save_transaksi():
    df = pd.DataFrame(st.session_state.transaksi)
    df.to_csv(FILE_PATH, index=False)

load_transaksi()

# =====================================================
# ===================== BERANDA =======================
# =====================================================
if menu == "📌 Beranda":
    st.title("Aplikasi Kas Kecil")

    # --- ROW CARD ---
    col1, col2 = st.columns(2)

    # ==== CARD 1 — METODE PENCATATAN ====
    with col1:
        st.markdown("""
            <div style="
                background: linear-gradient(135deg, #E9D1E1, #FFFFFF);
                padding: 22px;
                border-radius: 14px;
                border: 2px solid #3A2D71;
                box-shadow: 0 4px 14px rgba(0,0,0,0.12);
                text-align: center;
            ">
                <h3 style="color:#3A2D71; font-weight:900; margin-bottom:6px;">
                    Metode Pencatatan
                </h3>
                <p style="color:#000; font-size:17px; font-weight:700; margin:0;">
                    Fluktuatif
                </p>
            </div>
        """, unsafe_allow_html=True)

    # ==== CARD 2 — SALDO AWAL ====
    with col2:
        st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #A0BAC0, #DDE7EB);
                padding: 22px;
                border-radius: 14px;
                border: 2px solid #3A2D71;
                box-shadow: 0 4px 14px rgba(0,0,0,0.12);
                text-align: center;
            ">
                <h3 style="color:#3A2D71; font-weight:900; margin-bottom:6px;">
                    Saldo Awal Sistem
                </h3>
                <p style="color:#000; font-size:17px; font-weight:700; margin:0;">
                    Rp {SALDO_AWAL:,}
                </p>
            </div>
        """, unsafe_allow_html=True)

# =====================================================
# ================== INPUT TRANSAKSI ==================
# =====================================================
elif menu == "🧾 Transaksi":

    st.header("📝 Input Transaksi Kas Kecil")

    if "tanggal_input" not in st.session_state:
        st.session_state["tanggal_input"] = datetime.date.today()
    if "deskripsi_input" not in st.session_state:
        st.session_state["deskripsi_input"] = ""
    if "akun_filter_input" not in st.session_state:
        st.session_state["akun_filter_input"] = "Semua"
    if "jenis_input" not in st.session_state:
        st.session_state["jenis_input"] = "Pengeluaran"
    if "jumlah_input" not in st.session_state:
        st.session_state["jumlah_input"] = 0

    tanggal = st.date_input("Tanggal", key="tanggal_input")
    deskripsi = st.text_input("Deskripsi", key="deskripsi_input")
    akun_list = ["Semua"] + list(COA.keys()) + ["Kas Kecil"]
    akun_pilihan = st.selectbox("Fitur Akun", akun_list, key="akun_filter_input")

    jenis = st.selectbox("Jenis Transaksi", ["Pengeluaran", "Topup"], key="jenis_input")
    jumlah = st.number_input("Jumlah (Rp)", min_value=0, key="jumlah_input")

    col1, col2 = st.columns(2)

    # --- helper: reset input via callback (solusi aman)
    def reset_input():
        st.session_state["tanggal_input"] = datetime.date.today()
        st.session_state["deskripsi_input"] = ""
        st.session_state["akun_filter_input"] = "Semua"
        st.session_state["jenis_input"] = "Pengeluaran"
        st.session_state["jumlah_input"] = 0

    # BUTTON SIMPAN 
    with col1:
        st.markdown("<div class='wrap-save'>", unsafe_allow_html=True)
        
        if st.button("Simpan Transaksi", key="save_btn"):
            if deskripsi.strip() == "":
                st.error("Deskripsi tidak boleh kosong")
            elif jumlah <= 0:
                st.error("Jumlah harus lebih besar dari 0")
            elif akun_pilihan == "Semua":
                st.error("Pilih akun yang benar")
            else:
                if jenis == "Pengeluaran":
                    debit, kredit = akun_pilihan, "Kas Kecil"
                else:
                    debit, kredit = "Kas Kecil", "Kas Besar / Bank"

                st.session_state.transaksi.append({
                    "Tanggal": str(tanggal),
                    "Deskripsi": deskripsi,
                    "Jenis": jenis,
                    "Jumlah": jumlah,
                    "Debit": debit,
                    "Kredit": kredit
                })
                
                save_transaksi()
                st.success("Transaksi berhasil ditambahkan!")
                
        st.markdown("</div>", unsafe_allow_html=True)

      # BUTTON CLEAR (use on_click callback — safe)
    with col2:
        st.markdown("<div class='wrap-clear'>", unsafe_allow_html=True)
        st.button("Clear Input", key="clear_btn", on_click=reset_input)
        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# ================= LAPORAN BULANAN ===================
# =====================================================
# =====================================================
# ================= LAPORAN BULANAN ===================
# =====================================================
elif menu == "📑 Laporan Bulanan":

    st.header("📑 Laporan Bulanan")

    if len(st.session_state.transaksi) == 0:
        st.info("Belum ada transaksi.")
    else:
        df = pd.DataFrame(st.session_state.transaksi)
        df["Tanggal"] = pd.to_datetime(df["Tanggal"]) # Keep as datetime for easier filtering

        # --- Filter Bulan dan Tahun Awal ---
        all_years = sorted(df["Tanggal"].dt.year.unique())
        
        # Ensure 'bulan' and 'tahun' exist in session_state or initialize them
        # Note: Added logic to handle case where no data exists for current year/month
        current_year = datetime.date.today().year
        current_month = datetime.date.today().month
        
        # Determine initial year/month for selectbox
        initial_year = current_year if current_year in all_years else (all_years[-1] if all_years else current_year)
        
        if "bulan_lap" not in st.session_state or st.session_state["bulan_lap"] not in list(range(1, 13)):
            st.session_state["bulan_lap"] = current_month
        if "tahun_lap" not in st.session_state or st.session_state["tahun_lap"] not in all_years:
            st.session_state["tahun_lap"] = initial_year
        
        try:
            bulan_index = st.session_state["bulan_lap"] - 1
            tahun_index = all_years.index(st.session_state["tahun_lap"])
        except ValueError:
            # Handle case where the initial value might not be in the list (e.g., if initial_year is current_year but no data exists yet)
            bulan_index = current_month - 1
            tahun_index = 0 # Fallback

        bulan = st.selectbox("Pilih Bulan", list(range(1, 13)), index=bulan_index, key="bulan_lap")
        tahun = st.selectbox("Pilih Tahun", all_years, index=tahun_index, key="tahun_lap")

        akun_data = set(df["Debit"].unique()) | set(df["Kredit"].unique())
        daftar_akun = sorted(set(COA.keys()) | akun_data)
        
        if "akun_lap" not in st.session_state:
            st.session_state["akun_lap"] = "Semua"

        akun_filter = st.selectbox("Filter Akun", ["Semua"] + daftar_akun, key="akun_lap")

        # --- Fungsi Saldo Bulanan & Penomoran Ulang ---
        def hitung_saldo_dan_nomor(df, bulan, tahun):
            # 1. Saldo Awal (sebelum bulan/tahun terpilih)
            df_sebelumnya = df[
                (df["Tanggal"].dt.year < tahun) |
                ((df["Tanggal"].dt.year == tahun) & (df["Tanggal"].dt.month < bulan))
            ]

            saldo_awal_bulan = SALDO_AWAL
            # Hitung saldo dari transaksi sebelumnya
            for _, tr in df_sebelumnya.iterrows():
                if tr["Debit"] == "Kas Kecil" and tr["Kredit"] != "Kas Kecil": # Topup (Debit Kas Kecil)
                    saldo_awal_bulan += tr["Jumlah"]
                elif tr["Kredit"] == "Kas Kecil" and tr["Debit"] != "Kas Kecil": # Pengeluaran (Kredit Kas Kecil)
                    saldo_awal_bulan -= tr["Jumlah"]


            # 2. Transaksi Bulan Ini (Untuk Tampilan dan Saldo Akhir)
            df_bulan_ini = df[
                (df["Tanggal"].dt.year == tahun) &
                (df["Tanggal"].dt.month == bulan)
            ].copy() # Penting menggunakan .copy()

            # --- REVISI KUNCI: Tambahkan Kolom Nomor Transaksi Bulanan ---
            # Penomoran hanya pada transaksi bulan ini.
            # Mengurutkan berdasarkan tanggal dan memberi nomor urut dalam bulan tersebut
            df_bulan_ini.sort_values(by="Tanggal", inplace=True)
            
            # **INILAH BARIS YANG MEMASTIKAN PENOMORAN DIMULAI DARI 1**
            df_bulan_ini["No."] = df_bulan_ini.groupby(
                [df_bulan_ini["Tanggal"].dt.year, df_bulan_ini["Tanggal"].dt.month]
            ).cumcount() + 1
            # ---------------------------------------------------------------------

            # 3. Hitung Saldo Akhir Bulan
            saldo_akhir_bulan = saldo_awal_bulan
            # Hitung saldo dari transaksi bulan ini
            for _, tr in df_bulan_ini.iterrows():
                if tr["Debit"] == "Kas Kecil" and tr["Kredit"] != "Kas Kecil": # Topup (Debit Kas Kecil)
                    saldo_akhir_bulan += tr["Jumlah"]
                elif tr["Kredit"] == "Kas Kecil" and tr["Debit"] != "Kas Kecil": # Pengeluaran (Kredit Kas Kecil)
                    saldo_akhir_bulan -= tr["Jumlah"]

            return saldo_awal_bulan, saldo_akhir_bulan, df_bulan_ini

        saldo_awal, saldo_akhir, df_bulan_ini = hitung_saldo_dan_nomor(df, bulan, tahun)

        # --- Filter Akun (Jika dipilih) ---
        if akun_filter != "Semua":
            df_filter_akun = df_bulan_ini[
                (df_bulan_ini["Debit"] == akun_filter) |
                (df_bulan_ini["Kredit"] == akun_filter)
            ].copy()
        else:
            df_filter_akun = df_bulan_ini.copy()

        # --- Format Tampilan DataFrame ---
        # Pastikan kolom "No." ada di urutan pertama
        df_display = df_filter_akun[
            ["No.", "Tanggal", "Deskripsi", "Jenis", "Jumlah", "Debit", "Kredit"]
        ].copy()
        df_display["Tanggal"] = df_display["Tanggal"].dt.date
        df_display["Jumlah"] = df_display["Jumlah"].apply(lambda x: f"Rp {x:,}")

        st.dataframe(df_display, use_container_width=True, hide_index=True)
        st.markdown(f"### Saldo Awal Bulan: Rp {saldo_awal:,}")
        st.markdown(f"### Saldo Akhir Bulan: Rp {saldo_akhir:,}")

# =====================================================
# ================= UNDUH LAPORAN =====================
# =====================================================
elif menu == "📥 Unduh Laporan Kas Kecil":

    st.header("📥 Download Laporan Kas Kecil")

    # Jika tidak ada transaksi
    if len(st.session_state.transaksi) == 0:
        st.info("Belum ada transaksi.")
        st.stop()

    # Jika ada transaksi
    df = pd.DataFrame(st.session_state.transaksi)

    # Fungsi untuk membuat file Excel
    def generate_excel_openpyxl(df):
        buf = io.BytesIO()
        with pd.ExcelWriter(buf, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Petty Cash")
        buf.seek(0)
        return buf

    # Tombol download (TIDAK error lagi)
    st.markdown("<div class='wrap-download'>", unsafe_allow_html=True)
    st.download_button(
        label="📥 Unduh Excel",
        data=generate_excel_openpyxl(df),   # ← PERHATIKAN: Panggil fungsi DI SINI
        file_name=f"Laporan_Kas_{datetime.date.today()}.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",            key="download_excel"
    )
    st.markdown("</div>", unsafe_allow_html=True)
    

# =====================================================
# ================== RESET TRANSAKSI ==================
# =====================================================
elif menu == "🗑 Reset Semua Transaksi":

    st.header("🗑 Reset Semua Transaksi")
    st.markdown("<div class='wrap-reset'>", unsafe_allow_html=True)
    if st.button("Hapus Semua Data", key="reset_btn"):
        st.session_state.transaksi = []
        if os.path.exists(FILE_PATH):
            os.remove(FILE_PATH)
        st.success("Semua transaksi berhasil dihapus!")

        st.markdown("</div>", unsafe_allow_html=True)













