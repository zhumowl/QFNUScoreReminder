import requests
import logging


def feishu_notify(FEISHU_BOT_URL, FEISHU_BOT_SECRET, title, text):
    """
    发送飞书通知
    参数:
        FEISHU_BOT_URL: 飞书机器人URL
        FEISHU_BOT_SECRET: 飞书机器人验证关键词
        title: 消息标题
        text: 消息内容
    """
    if not FEISHU_BOT_URL or not FEISHU_BOT_SECRET:
        logging.error("飞书机器人URL或SECRET未配置")
        return

    headers = {"Content-Type": "application/json"}
    data = {
        "msg_type": "text",
        "content": {"text": f"{title}\n{text}\n{FEISHU_BOT_SECRET}"},
    }

    response = requests.post(FEISHU_BOT_URL, headers=headers, json=data)
    if response.json()["code"] == 0:
        logging.info("飞书通知发送成功")
        return response.json()
    else:
        logging.error(
            f"飞书通知发送失败，状态码: {response.status_code}，错误信息: {response.json()}"
        )
        return response.json()


if __name__ == "__main__":
    FEISHU_BOT_URL = "https://open.feishu.cn/open-apis/bot/v2/hook/f20a7d17-af7c-4b1f-b495-68ebf1ddd714"
    FEISHU_BOT_SECRET = "W1ndys"
    res = feishu_notify(
        FEISHU_BOT_URL,
        FEISHU_BOT_SECRET,
        "测试",
        "测试内容",
    )
    print(res)
