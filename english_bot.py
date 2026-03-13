import os
import requests
from google import genai

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=data)

def generate_english_lesson():
    try:
        client = genai.Client()
        
        prompt = """
        Đóng vai một giáo viên tiếng Anh xuất sắc. Hãy cung cấp 1 từ vựng hoặc 1 thành ngữ tiếng Anh MỚI (nằm trong 600 từ vựng cơ bản giao tiếp hằng ngày).
        Trình bày cực kỳ ngắn gọn, dễ nhìn bằng Markdown theo cấu trúc sau:
        
        📚 **[Từ vựng/Thành ngữ đó]** 🗣️ Phiên âm: 
        🏷️ Loại từ: 
        💡 Nghĩa tiếng Việt: 
        
        📝 **Ví dụ thực tế:** (1 câu ví dụ tiếng Anh áp dụng trong công việc thực tế, kèm lời dịch tiếng Việt ngay bên dưới).
        
        Lưu ý: Chỉ gửi đúng nội dung học, không dài dòng chào hỏi. Từ vựng phải mang tính thực chiến cao.
        """
        
        # Đã cập nhật chính xác cú pháp mới của Google (thêm .models.)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        send_telegram(response.text)
        
    except Exception as e:
        send_telegram(f"⚠️ Sếp ơi, quá trình tạo từ vựng gặp lỗi: {e}")

if __name__ == "__main__":
    generate_english_lesson()
