import requests
import random

URL = "http://192.168.10.20:3000"
EMAIL = "admin@admin.com"
PASSWORD = "1234"

TICKETS = [
    {
        "title": "Can't log into my computer",
        "detail": "Hi, I've been trying to log in since 8am and it just keeps saying my password is wrong. I haven't changed anything. I have a meeting in an hour and really need to get in asap. Please help!"
    },
    {
        "title": "Emails not coming through",
        "detail": "Hey, not sure if this is just me but I haven't received any emails since yesterday afternoon. I'm expecting something important from a client. Webmail seems fine but Outlook is just stuck. Can someone take a look?"
    },
    {
        "title": "Printer on 2nd floor not working",
        "detail": "The printer near the kitchen on the 2nd floor is showing offline again. I've tried turning it off and on and it didn't help. A few of us need to print documents for a 2pm meeting, is there any chance someone can come sort it?"
    },
    {
        "title": "My laptop is really slow today",
        "detail": "Hi there, my laptop has been absolutely crawling for the past couple of days. It takes forever to open anything and the fan is constantly running. I don't think I've installed anything new. It's making it really hard to get work done."
    },
    {
        "title": "Need access to the shared drive",
        "detail": "Hi, I've just started on the marketing team and my manager said I should have access to the shared drive but whenever I try to open it I get an access denied message. Could someone sort this out for me? Thanks"
    },
    {
        "title": "Zoom keeps crashing mid-call",
        "detail": "This is the third time this week Zoom has crashed on me during a call. It's really embarrassing when it happens in client meetings. I've tried restarting my laptop but it keeps happening. Is there an update or something I need to do?"
    },
    {
        "title": "Second monitor stopped working",
        "detail": "Hi, came in this morning and my second monitor isn't displaying anything. Just a black screen. I've checked the cable is plugged in properly. I really rely on it for my work so hoping this can be sorted quickly."
    },
    {
        "title": "Locked out of my account",
        "detail": "Hi I think I've been locked out, I tried my password a few times and now it won't let me try again. I know what my password is I think I just kept mistyping it. Can someone reset it or unlock me? Quite urgent as I have deadlines today."
    },
    {
        "title": "WiFi keeps dropping in the boardroom",
        "detail": "Just wanted to flag that the WiFi in the boardroom has been really unreliable lately. It drops every 10-15 minutes which is a nightmare when we have video calls in there. Can someone look into it? We have an important call with a client Friday."
    },
    {
        "title": "Request for Adobe Acrobat",
        "detail": "Hi, I've been asked by my manager to start handling some contract documents but I need Adobe Acrobat Pro to do it properly. I'm currently just using the free version and it won't let me edit PDFs. Is this something that can be arranged?"
    },
    {
        "title": "New starter needs setting up",
        "detail": "Hi IT, we have a new team member starting on Monday called Jamie. They'll need a laptop, company email, and access to Slack and the project management tool. Could you let me know what info you need from me to get this sorted before they arrive? Thanks"
    },
    {
        "title": "VPN won't connect from home",
        "detail": "Hi, I'm working from home today and I can't get the VPN to connect at all. It just times out every time. I was working fine from home last week so not sure what's changed. I can't access any of the systems I need without it."
    },
]

def get_token():
    response = requests.post(f"{URL}/api/v1/auth/login", json={"email": EMAIL, "password": PASSWORD})
    data = response.json()
    return data["token"]

def create_ticket(token):
    ticket = random.choice(TICKETS)
    response = requests.post(f"{URL}/api/v1/ticket/create", headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"}, json={"title": ticket["title"], "detail": ticket["detail"], "priority": random.choice(["Low", "Medium", "High"])})

if __name__ == "__main__":
    token = get_token()
    create_ticket(token)
