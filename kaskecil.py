import streamlit as st
import pandas as pd
import datetime
from io import BytesIO
import os
import io

st.markdown("""
<style>

<style>

:root {
    --pink-soft: #E9D1E1;
    --blue-soft: #A0BAC0;
    --yellow: #F6D60D;
    --purple-soft: #D8C9E8;
    --red-soft: #FFB4B4;

    --grad-pink: linear-gradient(135deg, #E9D1E1, #D7BFD3);
    --grad-blue: linear-gradient(135deg, #A0BAC0, #8CA8AF);
    --grad-yellow: linear-gradient(135deg, #F6D60D, #E8C70A);
    --grad-purple: linear-gradient(135deg, #E9D1E1, #D8C9E8);
    --grad-red: linear-gradient(135deg, #FFB4B4, #E79A9A);
}

/* ====== Perbaikan cepat untuk NumberInput (Jumlah) ====== */

/* Terapkan border & radius pada wrapper luar supaya tidak terpotong */
.stNumberInput > div {
    background: #FFFFFF !important;
    border: 2px solid var(--royal-blue) !important;
    border-radius: 10px !important;
    padding: 0 !important;           /* hilangkan padding wrapper agar kontrol di dalam rata */
    box-shadow: none !important;
}

/* Atur input sendiri: biarkan tanpa border internal (border ada di wrapper) */
.stNumberInput > div > div > input[type="number"] {
    border: none !important;
    outline: none !important;
    background: transparent !important;
    padding: 12px 14px !important;   /* jarak teks sama seperti input lain */
    color: #000 !important;
    font-size: 16px !important;
    box-shadow: none !important;
    -moz-appearance: textfield !important; /* firefox: hilangkan spin */
}

/* Sembunyikan spin buttons di WebKit (Chrome/Safari) */
.stNumberInput > div > div > input[type="number"]::-webkit-outer-spin-button,
.stNumberInput > div > div > input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none !important;
    margin: 0 !important;
}

/* Jika Streamlit menambahkan tombol stepper sendiri (CSS internal), sembunyikan elemen tombol di wrapper kanan */
.stNumberInput button, 
.stNumberInput > div > button {
    display: none !important;
    visibility: hidden !important;
}

/* Pastikan focus masih menampilkan glow biru konsisten */
.stNumberInput:focus-within,
.stNumberInput > div:focus-within {
    box-shadow: 0 0 10px rgba(58,45,113,0.35) !important;
    border-color: var(--royal-blue) !important;
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
   GLOBAL OVERRIDE — FIX TULISAN & OPACITY
========================================== */
html, body, *, .stAppViewContainer * {
    opacity: 1 !important;
    color: inherit !important;
}

/* ==========================================
   HEADER UTAMA
========================================== */
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
   INPUT FIELD — BORDER BIRU, BACKGROUND PUTIH
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

/* Kolom Jumlah = full border biru (revisi khusus) */
input[type="number"] {
    border: 2px solid var(--royal-blue) !important;
    background: #fff !important;
}

/* Select Box */
.stSelectbox > div > div {
    background: #fff !important;
    border: 2px solid var(--royal-blue) !important;
    border-radius: 10px !important;
    color: #000 !important;
}

/* ==========================================
   LOGIN LABELS (USERNAME & PASSWORD)
========================================== */
div.stTextInput label,
div.stPasswordInput label {
    color: #1B1F3B !important;
    font-weight: 800 !important;
    font-size: 16px !important;
}

/* Fix label invisibility */
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

/* ==========================================
   BUTTON KUNING
========================================== */
.stButton > button {
    background-color: var(--yellow-soft) !important;
    border: 2px solid var(--yellow-border) !important;
    border-radius: 10px !important;
    color: #000 !important;
    font-weight: 800 !important;
    padding: 10px 22px !important;
    height: 45px !important;
    transition: 0.22s ease-in-out !important;
}

.stButton > button:hover {
    background-color: var(--yellow-soft-hover) !important;
    transform: translateY(-2px) !important;
}

.stButton > button:active {
    transform: scale(0.97) !important;
}


/* ==========================================
   SIDEBAR MENU ITEM — TANPA BULAT-BULAT
========================================== */

/* ================================ */
/* SIDEBAR GRADIENT MENU */
/* ================================ */
[data-testid="stSidebar"] {
background: linear-gradient(180deg, #3A2D71 0%, #6A5BA9 45%, #B69CE3 100%) !important;
padding: 30px 18px;
border-right: 3px solid rgba(255,255,255,0.25);
box-shadow: 6px 0 25px rgba(0,0,0,0.18);
}


/* Hilangkan bullet default */
div[role="radiogroup"] input {
display: none !important;
}


/* Style tombol menu */
div[role="radiogroup"] > label {
padding: 14px 16px;
margin-bottom: 12px;
font-size: 17px;
font-weight: 800;
border-radius: 14px;
cursor: pointer;
transition: 0.25s ease-in-out;
display: block;
color: #fff !important;
border: 1px solid rgba(255,255,255,0.35);
backdrop-filter: blur(6px);
/* GRADASI TIAP TOMBOL NAVIGASI */
background: linear-gradient(135deg, #FFC6E0, #FF9AD1);
}


/* Variasi gradiasi berdasarkan urutan tombol */
div[role="radiogroup"] > label:nth-child(2) {
background: linear-gradient(135deg, #A0BAC0, #7DA0A8);
}


div[role="radiogroup"] > label:nth-child(3) {
background: linear-gradient(135deg, #F6D60D, #E8C70A);
color: #000 !important;
}


div[role="radiogroup"] > label:nth-child(4) {
background: linear-gradient(135deg, #D8C9E8, #B7A7D3);
}


div[role="radiogroup"] > label:nth-child(5) {
background: linear-gradient(135deg, #FFB4B4, #E79A9A);
}


/* Efek Hover */
div[role="radiogroup"] > label:hover {
transform: translateX(6px);
background: rgba(255,255,255,0.30);
border-color: rgba(255,255,255,0.45);
}


/* Warna saat dipilih */
div[role="radiogroup"] > label[data-selected="true"] {
background: linear-gradient(90deg, #F6D60D, #FFEA74) !important;
color: #000 !important;
border-color: #fff;
box-shadow: 0 6px 16px rgba(0,0,0,0.25);
transform: translateX(6px) scale(1.02);
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

st.sidebar.title("📘 Menu Utama")
menu = st.sidebar.radio(
    "",
    [
        "📌 Beranda",
        "🧾 Transaksi",
        "📑 Laporan Bulanan",
        "📥 Unduh Laporan",
        "🗑 Reset Semua Transaksi"
    ]
)

# ============================
# FUNCTION ITEM CARD
# ============================
def menu_item(label, icon, key, card_class):
    selected = (st.session_state.menu == key)
    active_class = "selected" if selected else ""

    html = f"""
        <div class="sidebar-card {card_class} {active_class}"
             onclick="document.querySelector('input[value='{key}']).click()">
            <span>{icon}</span> <span>{label}</span>
        </div>
    """
    st.sidebar.markdown(html, unsafe_allow_html=True)
    return key

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
                <p style="color:#000; font-size:25px; font-weight:700; margin:0;">
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
                <p style="color:#000; font-size:25px; font-weight:700; margin:0;">
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
elif menu == "📥 Unduh Laporan":

    st.header("📥 Unduh File Laporan Kas Kecil")

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






















