
from backend.src.main import query_prices

try:
    data = query_prices("AAPL")
    print('success')
    print(data[0])

except Exception as e:
    print("Error:", e)