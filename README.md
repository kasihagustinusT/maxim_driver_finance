# 🚗 Maxim Driver Finance AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.5+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Railway](https://img.shields.io/badge/Deployed_on-Railway-0B0D0E.svg)

**Sistem Manajemen Keuangan Cerdas untuk Driver Maxim dengan Analisis AI**

[Live Demo](https://maximdriverfinance-production.up.railway.app) • [Report Bug](https://github.com/kasihagustinusT/maxim_driver_finance/issues) • [Request Feature](https://github.com/kasihagustinusT/maxim_driver_finance/issues)

</div>

## 📖 Tentang Proyek

Maxim Driver Finance AI adalah sistem manajemen keuangan cerdas yang dirancang khusus untuk driver Maxim. Aplikasi ini membantu driver dalam:

- 📊 **Analisis Keuangan Real-time** - Memantau pendapatan dan pengeluaran secara live
- 🤖 **AI Financial Advisor** - Analisis cerdas dengan saran finansial otomatis
- 💰 **Auto Calculation** - Perhitungan otomatis komisi, tabungan, dan pendapatan bersih
- 📈 **Visualisasi Data** - Grafik dan chart interaktif untuk tracking performa
- 🎯 **Target Management** - Setting dan monitoring target harian/mingguan

### ✨ Fitur Unggulan

| Fitur | Deskripsi |
|-------|-----------|
| 🧮 **Auto Calculation** | Hitung otomatis komisi Maxim (15%), tabungan saldo (10%), BBM (10%), oli (10%) |
| 📊 **Real-time Analytics** | Dashboard live dengan metrik performa terkini |
| 🤖 **AI Insights** | Analisis cerdas dengan saran finansial berbasis AI |
| 📱 **Responsive Design** | Tampilan optimal di desktop, tablet, dan mobile |
| 📈 **Visual Charts** | Grafik revenue trend, distribusi order, breakdown pendapatan |
| 🎯 **Target Tracking** | Monitoring pencapaian target harian dan mingguan |
| 📋 **Transaction History** | Riwayat transaksi lengkap dengan filter dan search |
| 🗑️ **Data Management** | Tambah, edit, hapus data transaksi dengan mudah |

## 🚀 Demo Live

Aplikasi sudah terdeploy dan dapat diakses di:  
**🔗 https://maximdriverfinance-production.up.railway.app**

## 🛠️ Teknologi

### Backend
- **Python 3.9+** - Bahasa pemrograman utama
- **HTTP Server** - Web server built-in Python
- **Pandas** - Data processing dan analytics
- **CSV/JSON** - Penyimpanan data lokal

### Frontend
- **HTML5** - Struktur web
- **Tailwind CSS** - Styling dan responsive design
- **Chart.js** - Visualisasi data dan grafik
- **Font Awesome** - Icons
- **JavaScript Vanilla** - Interaktivitas

### Deployment
- **Railway** - Platform deployment
- **Docker** - Containerization (optional)

## 📦 Instalasi

### Prerequisites
- Python 3.9 atau lebih tinggi
- Pip (Python package manager)

### Local Development

1. **Clone Repository**
```bash
git clone https://github.com/kasihagustinusT/maxim_driver_finance.git
cd maxim_driver_finance
```

2. **Setup Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Jalankan Aplikasi**
```bash
python run.py
```

5. **Buka Browser**
```
http://localhost:8000/dashboard
```

### Dengan Docker

```bash
# Build image
docker build -t maxim-finance-ai .

# Jalankan container
docker run -p 8000:8000 maxim-finance-ai
```

## 🏗️ Arsitektur Projek

```
maxim_driver_finance/
├── app/
│   ├── models/           # Data models
│   │   ├── financial_record.py
│   │   └── analytics.py
│   ├── services/         # Business logic
│   │   ├── finance_manager.py
│   │   ├── ai_advisor.py
│   │   └── data_handler.py
│   ├── handlers/         # HTTP handlers
│   │   └── api_handler.py
│   ├── utils/           # Utilities
│   │   ├── config.py
│   │   └── helpers.py
│   └── main.py          # Entry point
├── data/                # Data storage
│   ├── riwayat_orderan.csv
│   └── config.json
├── requirements.txt
├── railway.toml
├── Procfile
└── README.md
```

## 💻 Cara Penggunaan

### 1. Dashboard Overview
- Akses `/dashboard` untuk melihat ringkasan keuangan
- Monitor total revenue, pendapatan bersih, efisiensi
- Lihat analisis AI dan tips finansial

### 2. Tambah Order Baru
- Akses `/orders` untuk menambah transaksi baru
- Input total orderan dan pilih jenis order
- Sistem otomatis hitung:
  - Komisi Maxim: 15%
  - Tabungan Saldo: 10%
  - Tabungan BBM: 10%
  - Tabungan Oli: 10%
  - Pendapatan Bersih & Siap Pakai

### 3. Riwayat Transaksi
- Akses `/history` untuk melihat semua transaksi
- Filter berdasarkan tanggal dan jenis order
- Hapus multiple data sekaligus

### 4. Management Target
- Akses `/targets` untuk set target performa
- Atur target pendapatan harian
- Set target jumlah order mingguan

## 🔧 Konfigurasi

### Rates Default
```python
COMMISSION_RATE = 0.15      # Komisi Maxim 15%
SALDO_SAVINGS_RATE = 0.10   # Tabungan Saldo 10%
BBM_SAVINGS_RATE = 0.10     # Tabungan BBM 10%
OLI_SAVINGS_RATE = 0.10     # Tabungan Oli 10%
```

### Custom Configuration
Edit `data/config.json` untuk mengubah:
- Nama perusahaan
- Target performa
- Currency settings

## 🚀 Deployment

### Deploy ke Railway (Recommended)

1. **Fork repository** ini ke GitHub account Anda

2. **Login ke [Railway](https://railway.com/)**

3. **Create New Project** → "Deploy from GitHub repo"

4. **Pilih repository** yang sudah di-fork

5. **Railway akan otomatis deploy** aplikasi Anda

6. **Akses aplikasi** di URL yang disediakan Railway

### Environment Variables (Optional)
```env
HOST=0.0.0.0
PORT=8000
DATA_DIR=/app/data
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/dashboard` | GET | Halaman dashboard utama |
| `/orders` | GET | Form tambah order baru |
| `/history` | GET | Riwayat transaksi |
| `/targets` | GET | Management target |
| `/api/data` | GET | Data transaksi lengkap (JSON) |
| `/api/analytics` | GET | Data analytics (JSON) |
| `/api/add-order` | POST | Tambah order baru |
| `/api/delete-orders` | POST | Hapus multiple orders |

## 🤖 AI Features

### Financial Analysis
- **Efficiency Ratio** - Mengukur efisiensi pendapatan
- **Performance Score** - Skor performa 0-100
- **Revenue Trend** - Analisis trend pendapatan
- **Order Pattern** - Pola jenis order terbaik

### Smart Insights
- **Performance Alerts** - Peringatan performa menurun
- **Financial Tips** - Saran pengelolaan keuangan
- **Earnings Prediction** - Prediksi pendapatan 7 hari ke depan
- **Optimization Suggestions** - Saran optimasi bisnis

## 🐛 Troubleshooting

### Common Issues

**Data tidak tampil di dashboard**
```bash
# Check file permissions
chmod 755 data/
chmod 644 data/*.csv data/*.json
```

**Port already in use**
```bash
# Ganti port di main.py
port = 8001  # atau port lain yang available
```

**Error CSV parsing**
```bash
# Reset data file
python reset_data.py
```

### Logs & Debug
Aktifkan debug mode dengan menambahkan environment variable:
```env
DEBUG=True
```

## 📈 Contoh Perhitungan

**Input:**
- Total Order: Rp 100,000
- Jenis Order: Regular

**Perhitungan Otomatis:**
```
Komisi Maxim (15%):    Rp 15,000
Tabungan Saldo (10%):  Rp 10,000  
Tabungan BBM (10%):    Rp 10,000
Tabungan Oli (10%):    Rp 10,000
─────────────────────────────────
Pendapatan Bersih:     Rp 85,000
Pendapatan Siap Pakai: Rp 55,000
```

## 🤝 Kontribusi

Kontribusi sangat diterima! Untuk berkontribusi:

1. Fork project ini
2. Buat feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` file untuk detail lebih lanjut.

## 👨‍💻 Developer

**Kasih Agustinus**  
- GitHub: [@kasihagustinusT](https://github.com/kasihagustinusT)
- Email: kasihagustinus22@gmail.com

## 🙏 Acknowledgments

- [Tailwind CSS](https://tailwindcss.com) untuk styling system
- [Chart.js](https://chartjs.org) untuk visualisasi data
- [Railway](https://railway.app) untuk platform deployment
- [Font Awesome](https://fontawesome.com) untuk icons

---

<div align="center">

### 💡 Tips untuk Driver Maxim

**"Kelola keuangan dengan bijak, pantau performa secara real-time, dan optimalkan pendapatan dengan AI insights!"**

⭐ Jika project ini membantu Anda, jangan lupa beri star di GitHub!

</div>
