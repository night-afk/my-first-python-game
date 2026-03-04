import random

def game_start():
    print("=== 歡迎來到終極密碼（數字炸彈） ===")
    print("1. 單人挑戰模式")
    print("2. 人機對戰模式")
    
    choice = input("請選擇模式 (1 或 2): ")
    
    # 初始化遊戲參數
    target = random.randint(1, 100)
    low = 1
    high = 100
    current_player = "玩家"  # 對戰模式用

    if choice == '1':
        print(f"\n遊戲開始！目標數字在 {low} 到 {high} 之間。")
        while True:
            try:
                guess = int(input(f"請輸入介於 {low}-{high} 的數字: "))
                
                # 檢查數字是否在範圍內
                if guess <= low or guess >= high:
                    print(f"無效輸入！請輸入介於 {low} 到 {high} 之間的數字。")
                    continue
                
                if guess == target:
                    print(f"💥 砰！爆炸了！ {target}是炸彈！")
                    break
                elif guess < target:
                    low = guess
                    print(f"提示：數字在 {low} 到 {high} 之間")
                else:
                    high = guess
                    print(f"提示：數字在 {low} 到 {high} 之間")
            except ValueError:
                print("請輸入有效的整數！")

    elif choice == '2':
        print(f"\n對戰模式開始！目標數字在 {low} 到 {high} 之間。")
        while True:
            if current_player == "玩家":
                try:
                    guess = int(input(f"【玩家回合】請輸入 {low}-{high} 的數字: "))
                    if guess <= low or guess >= high:
                        print(f"超過範圍了，請重新輸入。")
                        continue
                except ValueError:
                    print("請輸入整數！")
                    continue
            else:
                # 電腦隨機在目前範圍內猜一個數字
                guess = random.randint(low + 1, high - 1)
                print(f"【電腦回合】電腦猜了：{guess}")

            # 判定邏輯
            if guess == target:
                print(f"💥 爆炸！炸彈是 {target} {current_player} 輸了，遊戲結束！")
                break
            elif guess < target:
                low = guess
                print(f"範圍縮小為：{low} 到 {high}")
            else:
                high = guess
                print(f"範圍縮小為：{low} 到 {high}")

            # 切換玩家
            current_player = "電腦" if current_player == "玩家" else "玩家"

    else:
        print("選擇錯誤，請重新執行程式。")

if __name__ == "__main__":
    game_start()