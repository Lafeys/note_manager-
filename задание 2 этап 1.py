from datetime import datetime

def format_date_without_year(date_obj):
    return date_obj.strftime('%d-%m')
created_date = datetime(2024, 3, 19)
print(f"Создана: {format_date_without_year(created_date)}")