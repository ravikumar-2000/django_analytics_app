import base64
from io import BytesIO
import seaborn as sns
import matplotlib.pyplot as plt


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode("utf-8")
    buffer.close()
    return graph


def get_chart(chart_type, data, **kwargs):
    plt.switch_backend("AGG")
    fig = plt.figure(figsize=(10, 4))
    if chart_type == "#1":
        sns.barplot(x="transaction_id", y="position_total_price", data=data)
    elif chart_type == "#2":
        plt.pie(
            data=data, x="position_total_price", labels=data["transaction_id"].values
        )
    elif chart_type == "#3":
        plt.plot(
            data["transaction_id"],
            data["position_total_price"],
            color="green",
            marker="o",
            linestyle="dashed",
        )
    else:
        print("ups... failed to identify the chart type")
    plt.tight_layout()
    chart = get_graph()
    return chart
