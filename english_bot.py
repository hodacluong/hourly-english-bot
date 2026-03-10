import os
import requests
import google.generativeai as genai

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    # Dùng Markdown để tin nhắn hiển thị đẹp mắt
    data = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, data=data)

def generate_english_lesson():
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Sử dụng model gemini-1.5-flash cho tốc độ siêu nhanh
        model = genai.GenerativeModel('gemini-pro')
        
        # Lệnh điều khiển AI (Prompt)
        prompt = """
        Đóng vai một giáo viên tiếng Anh xuất sắc. Hãy cung cấp 1 từ vựng hoặc 1 thành ngữ tiếng Anh MỚI (xoay vòng ngẫu nhiên giữa 3 chủ đề: Quản lý dự án xây dựng, Luật pháp, hoặc Đầu tư tài chính).
        Trình bày cực kỳ ngắn gọn, dễ nhìn bằng Markdown theo cấu trúc sau:
        
        📚 **[Từ vựng/Thành ngữ đó]** 🗣️ Phiên âm: 
        🏷️ Loại từ: 
        💡 Nghĩa tiếng Việt: 
        
        📝 **Ví dụ thực tế:** (1 câu ví dụ tiếng Anh áp dụng trong công việc thực tế, kèm lời dịch tiếng Việt ngay bên dưới).
        
        Lưu ý: Chỉ gửi đúng nội dung học, không dài dòng chào hỏi. Từ vựng phải mang tính thực chiến cao.
        """
        
        response = model.generate_content(prompt)
        send_telegram(response.text)
        
    except Exception as e:
        send_telegram(f"⚠️ Sếp ơi, quá trình tạo từ vựng gặp lỗi: {e}")

if __name__ == "__main__":
    generate_english_lesson()
