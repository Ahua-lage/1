from utils.llm import ask_llm

def generate_report(ticker, analysis):
    prompt = f"""
你是一名券商分析师，请根据以下数据写一份简洁专业的股票研报：

公司：{ticker}

财务指标：
{analysis}

请生成：
1. 投资摘要
2. 投资逻辑
3. 财务分析
4. 风险提示

语言：专业、简洁、有逻辑
"""

    return ask_llm(prompt)
