import requests
import json

# URL của API
url = "https://ms.vietnamworks.com/company-profile/v1.0/company/search"


# Gửi yêu cầu GET tới API
response = requests.get('https://www.vietnamworks.com/danh-sach-cong-ty')
# response = requests.get(url)

# Kiểm tra nếu yêu cầu thành công (HTTP status code 200)
if response.status_code == 200:
    # Phân tích dữ liệu JSON trả về
    data = response.text
    # print(len(data["data"]))
    print(response.text)
else:
    print(f"Lỗi {response.status_code}")


json_data = json.dumps(data, indent=4, ensure_ascii=False)

with open('company.json', 'w', encoding='utf-8') as f:
    f.write(json_data)

print("Dữ liệu đã được xuất ra file one_mount.json")
