from agents.data_agent import fetch_data
from agents.clean_agent import clean_data
from agents.analysis_agent import analyze
from agents.chart_agent import generate_chart
from agents.report_agent import generate_report

def run(ticker="AAPL"):
    print("1. 抓取数据...")
    raw_data = fetch_data(ticker)

    print("2. 清洗数据...")
    clean_df = clean_data(raw_data)

    print("3. 财务分析...")
    analysis = analyze(raw_data)

    print("4. 生成图表...")
    chart_path = generate_chart(clean_df, ticker)

    print("5. 生成研报...")
    report = generate_report(ticker, analysis)

    print("\n===== 研报 =====\n")
    print(report)

    print(f"\n图表已保存: {chart_path}")

if __name__ == "__main__":
    run("AAPL")
