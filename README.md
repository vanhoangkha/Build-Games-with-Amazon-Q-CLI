# Canvas Dreams - Trò chơi sáng tạo nghệ thuật

![Canvas Dreams](https://placeholder-for-screenshot.png)

Canvas Dreams là một trò chơi sáng tạo nghệ thuật tương tác cho phép người dùng tạo ra các tác phẩm nghệ thuật kỹ thuật số đẹp mắt. Với nhiều chế độ vẽ, hiệu ứng hạt và công cụ tùy chỉnh, Canvas Dreams mang đến trải nghiệm sáng tạo thú vị cho mọi người.

## Tính năng nổi bật

### Giao diện chuyên nghiệp
- **Thanh bên (Sidebar)**: Chứa tất cả các điều khiển và tùy chọn
- **Khu vực vẽ**: Được phân tách rõ ràng với viền
- **Bảng màu**: Nằm ở phía dưới để dễ dàng chọn màu
- **Hệ thống trợ giúp**: Hiển thị hướng dẫn chi tiết khi cần

### Đa dạng chế độ vẽ
- **Vẽ thông thường**: Vẽ nét cơ bản với độ chính xác cao
- **Phun sơn**: Tạo hiệu ứng phun mềm mại với hệ thống hạt
- **Kaleidoscope**: Tạo các mẫu đối xứng tuyệt đẹp tự động
- **Trọng lực**: Tạo hiệu ứng phun nước với vật lý hấp dẫn

### Tùy chỉnh linh hoạt
- Điều chỉnh kích thước bút vẽ
- Bảng màu phong phú
- Điều chỉnh mức độ đối xứng cho chế độ kaleidoscope
- Chuyển đổi giữa nền đen và nền trắng

### Hai phiên bản
- **Phiên bản Desktop**: Sử dụng Pygame, chạy như ứng dụng độc lập
- **Phiên bản Web**: Sử dụng HTML5 Canvas, chạy trên trình duyệt web

## Cài đặt

### Yêu cầu hệ thống
- Python 3.x
- Pygame (cho phiên bản desktop)
- Flask và Werkzeug (cho phiên bản web)

### Các bước cài đặt
1. Clone repository này:
   ```
   git clone https://github.com/vanhoangkha/Build-Games-with-Amazon-Q-CLI.git
   ```

2. Di chuyển vào thư mục dự án:
   ```
   cd Build-Games-with-Amazon-Q-CLI
   ```

3. Tạo môi trường ảo và kích hoạt:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Cài đặt các thư viện cần thiết:
   ```
   pip install pygame
   ```

   Đối với phiên bản web, cài đặt thêm:
   ```
   pip install flask==2.0.1 werkzeug==2.0.1
   ```

## Cách chạy trò chơi

### Phiên bản Desktop
1. Di chuyển vào thư mục canvas_dreams:
   ```
   cd canvas_dreams
   ```

2. Chạy script run.sh:
   ```
   ./run.sh
   ```

   Hoặc chạy trực tiếp:
   ```
   python main.py
   ```

### Phiên bản Web
1. Di chuyển vào thư mục canvas_dreams_web:
   ```
   cd canvas_dreams_web
   ```

2. Cài đặt các thư viện cần thiết:
   ```
   pip install -r requirements.txt
   ```

3. Chạy script run.sh:
   ```
   ./run.sh
   ```

   Hoặc chạy trực tiếp:
   ```
   python server.py
   ```

4. Mở trình duyệt web và truy cập:
   ```
   http://localhost:1313
   ```

## Hướng dẫn sử dụng

### Điều khiển chuột
- **Chuột trái**: Vẽ trên canvas
- **Chuột phải**: Đổi sang màu ngẫu nhiên
- **Nhấp vào bảng màu**: Chọn màu cụ thể
- **Nhấp vào các nút**: Kích hoạt các chức năng

### Phím tắt
| Phím | Chức năng |
|------|-----------|
| 1-4 | Chuyển đổi giữa các chế độ vẽ |
| Mũi tên Lên/Xuống | Tăng/giảm kích thước bút |
| Mũi tên Trái/Phải | Điều chỉnh mức độ đối xứng (trong chế độ kaleidoscope) |
| C | Xóa canvas |
| S | Lưu tác phẩm dưới dạng PNG |
| B | Chuyển đổi màu nền (đen/trắng) |
| H | Hiển thị/ẩn trợ giúp |

### Các chế độ vẽ
1. **Vẽ thông thường (phím 1)**: Chế độ vẽ cơ bản với nét vẽ liên tục
2. **Phun sơn (phím 2)**: Tạo hiệu ứng phun với các hạt nhỏ
3. **Kaleidoscope (phím 3)**: Tạo các mẫu đối xứng xung quanh tâm canvas
4. **Trọng lực (phím 4)**: Tạo hiệu ứng phun nước với các hạt chịu tác động của trọng lực

## Mẹo sáng tạo

- Kết hợp nhiều chế độ vẽ để tạo hiệu ứng độc đáo
- Thử nghiệm với các mức độ đối xứng khác nhau trong chế độ kaleidoscope
- Sử dụng kích thước bút khác nhau trong cùng một tác phẩm
- Thử cả nền đen và nền trắng để tạo hiệu ứng tương phản
- Lưu tác phẩm thường xuyên để xây dựng bộ sưu tập

## Xử lý sự cố

### Phiên bản Desktop
- **Lỗi âm thanh ALSA**: Đã được xử lý bằng cách tắt âm thanh trong mã nguồn
- **Không hiển thị giao diện**: Kiểm tra cài đặt Pygame và môi trường Python

### Phiên bản Web
- **Lỗi ImportError với Flask**: Đảm bảo cài đặt đúng phiên bản Flask và Werkzeug
  ```
  pip install flask==2.0.1 werkzeug==2.0.1
  ```
- **Không thể truy cập localhost:1313**: Kiểm tra xem server đã chạy chưa và không có ứng dụng nào khác đang sử dụng cổng 1313

## Thông tin kỹ thuật

### Công nghệ sử dụng
- **Phiên bản Desktop**: Python, Pygame
- **Phiên bản Web**: HTML5, CSS, JavaScript, Flask

### Cấu trúc dự án
```
Build-Games-with-Amazon-Q-CLI/
├── canvas_dreams/           # Phiên bản desktop
│   ├── main.py              # Mã nguồn chính
│   ├── run.sh               # Script chạy game
│   └── README.md            # Hướng dẫn
│
├── canvas_dreams_web/       # Phiên bản web
│   ├── server.py            # Máy chủ Flask
│   ├── requirements.txt     # Thư viện cần thiết
│   ├── run.sh               # Script chạy server
│   ├── templates/           # Mẫu HTML
│   │   └── index.html
│   ├── static/              # Tài nguyên tĩnh
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── canvas_dreams.js
│   └── README.md            # Hướng dẫn
│
└── README.md                # Tài liệu chính
```

## Phát triển trong tương lai

Các tính năng dự kiến phát triển:
- Khả năng ghi lại hoạt ảnh
- Thêm chế độ vẽ và hiệu ứng mới
- Hệ thống lớp cho tác phẩm phức tạp
- Tính năng vẽ cộng tác
- Hình dạng bút tùy chỉnh
- Tối ưu hóa cho thiết bị di động

## Giới thiệu về dự án

Canvas Dreams được phát triển để minh họa cách Amazon Q CLI có thể hỗ trợ trong việc xây dựng các ứng dụng sáng tạo. Dự án này là ví dụ về cách AI có thể giúp tạo ra các trò chơi tương tác với giao diện người dùng chuyên nghiệp và các tính năng phong phú.

## Tác giả

Dự án được phát triển với sự hỗ trợ của Amazon Q CLI.

## Giấy phép

Mã nguồn được cung cấp cho mục đích học tập và phi thương mại.

## Hãy thỏa sức sáng tạo!

Hãy để trí tưởng tượng của bạn bay bổng và tạo ra những tác phẩm nghệ thuật kỹ thuật số tuyệt đẹp với Canvas Dreams!
