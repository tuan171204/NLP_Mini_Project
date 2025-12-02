Trợ Lý Phân Loại Cảm Xúc Tiếng Việt (Vietnamese Sentiment Assistant)
Mô Tả Dự Án
Đây là đồ án môn học nhằm xây dựng một ứng dụng phân loại cảm xúc từ văn bản tiếng Việt sử dụng kiến trúc mô hình Transformer.
Ứng dụng nhận vào một câu tiếng Việt bất kỳ, sau đó sử dụng mô hình AI được huấn luyện sẵn (Pre-trained Model) để phân loại cảm xúc của câu thành 3 nhãn chính: Tích cực (POSITIVE), Trung tính (NEUTRAL), hoặc Tiêu cực (NEGATIVE).

Tính năng chính
Phân loại cảm xúc (Sentiment Analysis): Xử lý văn bản tiếng Việt để xác định cảm xúc.
Sử dụng AI tiên tiến: Triển khai mô hình PhoBERT (một phiên bản Transformer tối ưu cho tiếng Việt) thông qua thư viện Hugging Face Transformers.
Giao diện Web: Xây dựng bằng framework Flask (Python).
Lưu trữ lịch sử: Lưu lại tất cả các lần phân loại vào cơ sở dữ liệu SQLite cục bộ.

Hướng Dẫn Cài Đặt và Chạy Ứng Dụng
Ứng dụng được xây dựng hoàn toàn bằng Python và yêu cầu các thư viện tiêu chuẩn trong môi trường ảo (Virtual Environment - venv).

# 1. Yêu cầu hệ thống & cài đặt
Python: Phiên bản 3.8 trở lên.
Hệ điều hành: Windows, macOS, hoặc Linux.

Tạo thư mục trống để chứa repository, dùng git bash/github desktop:
>> git clone 

# 2. Thiết lập Môi trường Ảo (Virtual Environment)
Nnên tạo môi trường ảo để quản lý các thư viện dự án một cách cô lập.
Mở Terminal (hoặc Command Prompt) trong thư mục gốc của dự án
# a. Tạo môi trường ảo (tên là venv)
>> python -m venv venv

# b. Kích hoạt môi trường ảo
# Trên Windows:
>> .\venv\Scripts\activate
# Trên macOS/Linux:
>> source venv/bin/activate

(Sau khi kích hoạt, sẽ thấy (venv) xuất hiện ở đầu dòng lệnh).

# 3. Cài đặt các Thư viện Phụ thuộc
Sử dụng pip để cài đặt tất cả các thư viện cần thiết:
>> pip install -r requirements.txt

Lưu ý: Lần đầu tiên chạy lệnh này, thư viện torch sẽ được cài đặt và model Transformer (PhoBERT) sẽ được tải về máy (khoảng 300-500 MB).
Quá trình này có thể mất vài phút tùy thuộc vào tốc độ mạng.

# 4. Chạy Ứng DụngSau khi cài đặt thành công, chạy file app.py:
>> python app.py

# 5. Truy cập Ứng Dụng
Mở trình duyệt web của bạn.Truy cập vào địa chỉ: http://127.0.0.1:5000/
Ứng dụng sẽ tự động khởi tạo cơ sở dữ liệu sentiment.db và bắt đầu lắng nghe yêu cầu.

Cấu Trúc Dự ÁnCấu trúc file đã được phân chia rõ ràng theo các lớp chức năng:
Final_Project/
│
├── venv/                  # Môi trường ảo
├── app.py                 # Core: Thiết lập Flask server, Routing, Logic Database
├── nlp_model.py           # Core: Hàm chứa logic gọi model AI (Transformer Pipeline)
├── sentiment.db           # Cơ sở dữ liệu SQLite (Tự động tạo)
└── templates/             # Giao diện người dùng
    └── index.html         # Template chính sử dụng Jinja2