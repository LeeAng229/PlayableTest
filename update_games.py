import os
import json

# 配置路径
GAME_DIR = 'game'
OUTPUT_FILE = 'games.json'

def generate_games_json():
    games_list = []
    
    # 检查 game 目录是否存在
    if not os.path.exists(GAME_DIR):
        print(f"错误: 找不到目录 '{GAME_DIR}'")
        return

    # 遍历文件夹中的所有 html 文件
    for filename in os.listdir(GAME_DIR):
        if filename.endswith('.html'):
            file_path = os.path.join(GAME_DIR, filename)
            
            # 去掉后缀名作为标题
            title = filename.replace('.html', '').replace('_', ' ').capitalize()
            
            # 构造游戏对象
            game_data = {
                "title": title,
                "path": f"{GAME_DIR}/{filename}",
                "icon": "🎮",  # 默认图标
                "desc": f"这是关于 {title} 的小游戏。"
            }
            games_list.append(game_data)
            print(f"已发现游戏: {title}")

    # 将结果写入 JSON
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(games_list, f, ensure_ascii=False, indent=4)
    
    print(f"\n成功！共识别 {len(games_list)} 个游戏，已更新至 {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_games_json()