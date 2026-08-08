# Student Search API

## Mục tiêu

Xây dựng API `GET /students/search` hỗ trợ tìm kiếm,
lọc và phân trang sinh viên.

## Cấu trúc module

* `main.py`: Khởi tạo FastAPI và đăng ký router.
* `database.py`: Cấu hình database và tạo session.
* `models.py`: Định nghĩa model `Student`.
* `schemas.py`: Định nghĩa schema dữ liệu trả về.
* `routers/student_router.py`: Nhận request và khai báo API.
* `services/student_service.py`: Xử lý nghiệp vụ tìm kiếm, lọc và phân trang.

## API

```text
GET /students/search
```

Các tham số:

```text
keyword
min_age
max_age
is_active
page
page_size
```

Ví dụ:

```text
/students/search?keyword=An&min_age=18&max_age=25&is_active=true&page=1&page_size=5
```

## Yêu cầu

* `main.py` gọn.
* Không lặp nghiệp vụ.
* Các module import đúng.
* Các API cũ vẫn hoạt động.
* Nghiệp vụ tìm kiếm nằm trong `student_service.py`.
