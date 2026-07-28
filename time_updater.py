from datetime import datetime
from zoneinfo import ZoneInfo


def get_city_time(time_zone_name):
    """Считает точное время в любой часовой зоне встроенными средствами Python"""
    try:
        now = datetime.now(ZoneInfo(time_zone_name))
        return now.strftime("%H:%M")
    except Exception as e:
        print(f"Ошибка: {e}")
        return "Н/Д"


# Получаем время без внешних сайтов и API
moscow_time = get_city_time("Europe/Moscow")
ny_time = get_city_time("America/New_York")
last_update = datetime.now(ZoneInfo("UTC")).strftime("%Y-%m-%d %H:%M:%S UTC")

# Формируем HTML-страницу
html_content = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>What1unkpg9 | Live Time</title>
    <style>
        body {{
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }}
        .card {{
            background: #161b22;
            padding: 2rem 3rem;
            border-radius: 16px;
            border: 1px solid #30363d;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
            text-align: center;
        }}
        h1 {{ margin-top: 0; color: #58a6ff; font-size: 1.8rem; }}
        .time-box {{
            display: flex;
            gap: 2rem;
            justify-content: center;
            margin: 2rem 0;
        }}
        .time-item {{
            background: #21262d;
            padding: 1rem 1.5rem;
            border-radius: 10px;
            border: 1px solid #30363d;
        }}
        .city {{ font-size: 0.9rem; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; }}
        .clock {{ font-size: 2.2rem; font-weight: bold; color: #f0f6fc; margin-top: 0.3rem; }}
        .footer {{ font-size: 0.75rem; color: #484f58; margin-top: 1.5rem; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>What1unkpg9!</h1>
        <div class="time-box">
            <div class="time-item">
                <div class="city">Москва 🇷🇺</div>
                <div class="clock">{moscow_time}</div>
            </div>
            <div class="time-item">
                <div class="city">Нью-Йорк 🇺🇸</div>
                <div class="clock">{ny_time}</div>
            </div>
        </div>
        <div class="footer">
            Автоматически обновлено через Python & GitHub Actions<br>
            {last_update}
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Сайт успешно обновлён!")
