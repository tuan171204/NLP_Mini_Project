# Trợ Lý Phân Loại Cảm Xúc Tiếng Việt
Vietnamese Sentiment Assistant – Flask + PhoBERT + Transformers
## 1. Giới thiệu
Dự án xây dựng một hệ thống phân loại cảm xúc tiếng Việt dựa trên mô hình Transformer hiện đại.
Ứng dụng nhận vào một câu tiếng Việt và phân loại thành ba nhãn:

POSITIVE (Tích cực)
NEUTRAL (Trung tính)
NEGATIVE (Tiêu cực)

Hệ thống sử dụng:

PhoBERT (Pre-trained Transformer cho tiếng Việt)
Thư viện HuggingFace Transformers
Flask Framework
Cơ sở dữ liệu SQLite để lưu lịch sử

## 2. Tính năng chính

Phân loại cảm xúc văn bản tiếng Việt bằng mô hình AI.

Sử dụng mô hình PhoBERT được huấn luyện trước.

Giao diện web chạy trên Flask.

Lưu lại lịch sử phân loại vào SQLite.

Tự động tải và cache mô hình khi chạy lần đầu.

## 3. Yêu cầu hệ thống
Thành phần	Phiên bản
Python	3.8+
Hệ điều hành	Windows / macOS / Linux
Kết nối Internet	Cần cho lần chạy đầu để tải model

## 4. Hướng dẫn cài đặt
### 4.1. Tạo môi trường ảo (Virtual Environment)
Trong thư mục dự án:
> python -m venv venv

### 4.2. Kích hoạt môi trường ảo
Windows:
> .\venv\Scripts\activate


macOS / Linux:
> source venv/bin/activate

### 4.3. Cài đặt các thư viện cần thiết
> pip install -r requirements.txt


### Lưu ý:
Lần đầu tiên chạy lệnh trên, hệ thống sẽ tự động tải mô hình PhoBERT (kích thước 300–500 MB). Việc này có thể mất một vài phút tùy tốc độ mạng.

### 4.4. Chạy ứng dụng Flask
> python app.py

## 5. Truy cập ứng dụng

Truy cập trình duyệt tại địa chỉ: [http://127.0.0.1:5000/]


Hệ thống sẽ tự động tạo tệp cơ sở dữ liệu:
sentiment.db

## 6. Cấu trúc dự án
Final_Project/
│
├── venv/                  # Môi trường ảo (không nên gửi kèm)
├── app.py                 # Flask server, routing, database logic
├── nlp_model.py           # Logic gọi mô hình PhoBERT (Transformers Pipeline)
├── sentiment.db           # Database SQLite (tự động tạo)
└── templates/
    └── index.html         # Giao diện hiển thị bằng Jinja2