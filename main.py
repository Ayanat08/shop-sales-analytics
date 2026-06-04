import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt


db_url = 'postgresql+psycopg2://postgres:123456789@127.0.0.1:5433/shopkz_db'
engine = create_engine(db_url)


query = "SELECT sale_date, total_amount FROM sales ORDER BY sale_date ASC;"
df = pd.read_sql(query, engine)


df['sale_date'] = pd.to_datetime(df['sale_date'])
df.set_index('sale_date', inplace=True)




daily_sales = df['total_amount'].resample('D').sum().fillna(0)


cumulative_revenue = daily_sales.cumsum()


rolling_trend = daily_sales.rolling(window=7, min_periods=1).mean()


print("Daily Sales")
print(daily_sales.tail(5))
print("\n")
print(cumulative_revenue.tail(5))




fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
fig.suptitle('Деректерді талдау қорытындысы (Shop Analytics Dashboard)', fontsize=16, fontweight='bold')


ax1.bar(daily_sales.index, daily_sales.values, color='skyblue', alpha=0.7, label='Күнделікті түсім (Daily Revenue)')
ax1.plot(rolling_trend.index, rolling_trend.values, color='crimson', linewidth=2, label='7 күндік сырғымалы орташа мән')
ax1.set_title('Күнделікті түсім және Сырғымалы орташа мән тренді', fontsize=12, fontweight='bold')
ax1.set_ylabel('Сомасы (₸)')
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.5)


ax2.fill_between(cumulative_revenue.index, cumulative_revenue.values, color='teal', alpha=0.3, label='Жинақталған түсім')
ax2.plot(cumulative_revenue.index, cumulative_revenue.values, color='teal', linewidth=2)
ax2.set_title('Барлық уақыттағы жинақталған қорытынды', fontsize=12, fontweight='bold')
ax2.set_xlabel('Уақыт (Күндер)')
ax2.set_ylabel('Жалпы сомасы (₸)')
ax2.legend(loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.5)


plt.tight_layout()


plt.savefig('analytics_dashboard.png', dpi=300)
print("\n")


plt.show()