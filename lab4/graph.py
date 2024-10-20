import plotly.express as px

x = ["однопоточное", "1", "2", "4", "8", "16", "32", "64"]
y = [164.98 ,169.45, 90.11, 50.85, 31.79, 25.78, 27.32, 28.42]

fig = px.line(x=x, y=y, markers=True, title="Зависимость времени работы программы от числа потоков")
fig.update_layout(xaxis_title="Количество потоков", yaxis_title="Время выполнения, с")
fig.show()