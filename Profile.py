# PROFILE NGUYỄN NHƯ SƠN

import time

def show_profile():
    profile = {
        "Họ tên"    : "Nguyễn Như Sơn",
        "Tuổi"      : 18,
        "Sở thích"  : "Chơi game 🎮",
        "Facebook"  : "https://www.facebook.com/sxndeptrai",
        "Instagram" : "https://www.instagram.com/_nooson_/",
        "Game chính": "Counter-Strike 2 (CS2)",
        "Chuột"     : "ATK X1 SE",
        "Sens"      : "1.25 (DPI mặc định)",
        "Laptop"    : "ASUS ROG Strix G814JIR",
        "Bàn phím"  : "AULA WIN68 HE"
    }

    print("\n=== PROFILE CÁ NHÂN ===")
    for k, v in profile.items():
        time.sleep(0.3)
        print(f"{k:12}: {v}")
    print("="*50)

if __name__ == "__main__":
    show_profile()
