import streamlit as st
import pandas as pd
import datetime
from io import BytesIO
import os
import io

st.markdown("""
<style>

/* =======================
   FORM INPUT STYLE
========================== */

/* Semua input termasuk kolom Jumlah dibuat sama */
input, select, textarea {
    width: 100%;
    padding: 12px 15px;
    border: 2px solid #2b2b84;   /* BORDER BIRU FULL */
    border-radius: 10px;
    font-size: 16px;
    background: #ffffff;        /* Background putih agar terlihat */
    color: #000;                /* Teks hitam agar kontras */
    box-sizing: border-box;
}

/* Placeholder lebih jelas */
input::placeholder,
textarea::placeholder {
    color: #666;
}


/* =======================
   NAVIGASI MENU
========================== */

/* Hilangkan bullet / lingkaran */
nav ul,
nav li {
    list-style: none !important;
    margin: 0;
    padding: 0;
}

/* Hapus bullet pseudo-element jika ada */
nav li::before,
nav li::after {
    content: none !important;
}

/* Style tiap menu navigasi */
.nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 15px 20px;
    border-radius: 15px;
    margin-bottom: 12px;

    /* Warna background tetap mengikuti aslinya 
       (pink, biru, kuning, ungu, merah muda, dll) */
}

/* Hilangkan lingkaran kecil di kiri */
.nav-item input[type="radio"],
.nav-item input[type="checkbox"] {
    display: none !important;
}

/* Ikon dan teks jelas */
.nav-item span {
    font-size: 20px;
    font-weight: 600;
    color: #000;
}

/* =======================
   HEADER UTAMA
========================== */

.main-header {
    background: #ffffff !important;
    color: #2b2b84 !important;
    font-weight: 800;
    font-size: 32px;
    text-align: center;
    padding: 20px 0;
}


/* ==========================================
   COLOR PALETTE
========================================== */
:root {
    --royal-blue: #3A2D71;
    --tea-pink: #E9D1E1;
    --yellow: #F6D60D;
    --baby-pink: #A0BAC0;
    --soft-red: #FFB4B4;

    --yellow-soft: rgba(246,214,13,0.65);
    --yellow-soft-hover: rgba(246,214,13,0.80);
    --yellow-border: #d7be09;
}

/* ==========================================
   FIX GLOBAL OPACITY & TEXT INVISIBILITY
========================================== */
html, body, *, .stAppViewContainer * {
    opacity: 1 !important;
    color: inherit !important;
}

/* ==========================================
   HEADERS / JUDUL AGAR MUNCUL
========================================== */
h1, h2, h3, h4, h5, h6,
.stMarkdown h1, .stMarkdown h2 {
    color: #1B1F3B !important;
    font-weight: 900 !important;
}

/* Header besar di halaman utama */
.main-header {
    width: 100%;
    padding: 18px 0;
    text-align: center;
    background: linear-gradient(135deg, #3A2D71, #50409B);
    color: white !important;
    font-size: 28px;
    font-weight: 900;
    border-radius: 10px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.18);
    margin-bottom: 25px;
}

/* ==========================================
   INPUT FIELD — PUTIH TERANG
========================================== */

.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stTextArea textarea {
    background: #FFFFFF !important;
    color: #000 !important;
    border: 2px solid var(--royal-blue) !important;
    border-radius: 10px !important;
    box-shadow: none !important;
}

/* Placeholder */
input::placeholder {
    color: #666 !important;
    opacity: 1 !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background: #fff !important;
    border: 2px solid var(--royal-blue) !important;
    border-radius: 10px !important;
    color: #000 !important;
}

/* Focus efek biru */
.stTextInput input:focus,
.stNumberInput input:focus,
.stDateInput input:focus,
.stTextArea textarea:focus,
.stSelectbox > div[data-baseweb="select"]:focus-within {
    border-color: var(--royal-blue) !important;
    box-shadow: 0 0 10px rgba(58,45,113,0.35) !important;
}

/* ==========================================
   LABEL USERNAME & PASSWORD LOGIN
========================================== */
div.stTextInput label,
div.stPasswordInput label {
    color: #1B1F3B !important;
    font-weight: 800 !important;
    font-size: 16px !important;
}

/* Streamlit sempat menyembunyikan label — kita paksa muncul */
label[class] {
    clip: auto !important;
    clip-path: none !important;
    position: relative !important;
    width: auto !important;
    height: auto !important;
    opacity: 1 !important;
}

/* ==========================================
   LOGIN CARD
========================================== */

.login-wrapper {
    width: 420px;
    margin: 110px auto 0 auto;
    text-align: center;
}

.login-card {
    background: rgba(255,255,255,0.50);
    border: 2px solid rgba(255,255,255,0.6);
    backdrop-filter: blur(18px);
    padding: 40px 26px;
    border-radius: 20px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.18);
}

.login-title {
    font-size: 38px;
    font-weight: 900;
    color: var(--royal-blue);
}

.login-sub {
    font-size: 18px;
    font-weight: 700;
    color: #333;
}

/* ==========================================
   BUTTON — KUNING TERANG
========================================== */
.stButton > button,
button[data-testid="baseButton-primary"],
button[kind="secondary"],
.wrap-save button,
.wrap-clear button,
.wrap-download button,
.wrap-reset button {
    background-color: var(--yellow-soft) !important;
    border: 2px solid var(--yellow-border) !important;
    border-radius: 10px !important;

    color: #000 !important;
    font-weight: 800 !important;
    padding: 10px 22px !important;
    height: 45px !important;

    box-shadow:
        0 3px 8px rgba(0,0,0,0.14),
        0 0 10px rgba(246,214,13,0.25) !important;
    transition: 0.22s ease-in-out !important;
}

/* Hover */
.stButton > button:hover,
button[data-testid="baseButton-primary"]:hover {
    background-color: var(--yellow-soft-hover) !important;
    transform: translateY(-2px) !important;
}

/* Active click */
.stButton > button:active {
    transform: scale(0.97) !important;
}

/* ==========================================
   SIDEBAR NAVIGATION BULLETS — PUTIH / SOFT
========================================== */
[data-testid="stSidebar"] {
    background: #fff !important;
    padding: 30px 18px;
    border-right: 2px solid var(--royal-blue);
    box-shadow: 6px 0 20px rgba(0,0,0,0.1);
}

div[role="radiogroup"] > label {
    padding: 12px 16px;
    font-size: 15px;
    font-weight: 600;
    border-radius: 14px;
    cursor: pointer;
    transition: 0.22s;
}

/* Warna latar sesuai palette */
div[role="radiogroup"] > label:nth-child(1) { background: var(--tea-pink); }
div[role="radiogroup"] > label:nth-child(2) { background: var(--baby-pink); }
div[role="radiogroup"] > label:nth-child(3) { background: var(--yellow); }
div[role="radiogroup"] > label:nth-child(4) { background: var(--tea-pink); }
div[role="radiogroup"] > label:nth-child(5) { background: var(--soft-red); }

/* Bullet (titik di kiri) → putih */
div[role="radiogroup"] > label::before {
    content: "";
    width: 16px;
    height: 16px;
    border-radius: 50%;
    background: white !important;
    margin-right: 10px;
    display: inline-block;
}

/* Saat dipilih */
div[role="radiogroup"] > label[data-selected="true"] {
    background: var(--royal-blue) !important;
    color: white !important;
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.20);
}

/* Titik ketika dipilih */
div[role="radiogroup"] > label[data-selected="true"]::before {
    background: white !important;
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


















