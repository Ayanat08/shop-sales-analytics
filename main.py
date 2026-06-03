import pandas as pd
import matplotlib.pyplot as plt

print("Деректер қорынан экспортталған CSV файлы жүктелуде...")

try:

    df = pd.read_csv('sales_data.csv')
    print("Деректер сәтті жүктелді!")
except FileNotFoundError:
    print("\n[ҚАТЕ!] 'sales_data.csv' файлы жоба папкасынан табылмады.")
    print("Өтініш, 1-қадамды орындап, файлды PyCharm жобаңыздың ішіне сақтаңыз.")
    exit()


df['sale_date'] = pd.to_datetime(df['sale_date'])
df.set_index('sale_date', inplace=True)

daily_sales = df['total_amount'].resample('D').sum().fillna(0)
cumulative_revenue = daily_sales.cumsum()
rolling_trend = daily_sales.rolling(window=7, min_periods=1).mean()

print("\n--- Соңғы 5 күндік сатылымдар (Daily Sales) ---")
print(daily_sales.tail(5))


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
fig.suptitle('Shop Analytics Dashboard', fontsize=16, fontweight='bold')


ax1.bar(daily_sales.index, daily_sales.values, color='skyblue', alpha=0.7, label='Күнделікті түсім')
ax1.plot(rolling_trend.index, rolling_trend.values, color='crimson', linewidth=2, label='7 күндік тренд')
ax1.set_title('Күнделікті түсім және Сырғымалы орташа мән тренді')
ax1.set_ylabel('Сомасы (₸)')
ax1.legend(loc='upper left')
ax1.grid(True, linestyle='--', alpha=0.5)


ax2.fill_between(cumulative_revenue.index, cumulative_revenue.values, color='teal', alpha=0.3, label='Жинақталған түсім')
ax2.plot(cumulative_revenue.index, cumulative_revenue.values, color='teal', linewidth=2)
ax2.set_title('Барлық уақыттағы жинақталған қорытынды')
ax2.set_xlabel('Уақыт')
ax2.set_ylabel('Жалпы сомасы (₸)')
ax2.legend(loc='upper left')
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()


plt.savefig('analytics_dashboard.png', dpi=300)
print("\nГрафик 'analytics_dashboard.png' файлы болып сәтті сақталды!")


plt.show()