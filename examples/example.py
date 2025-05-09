import qchat
from datetime import datetime

@qchat.command("help")
def cmd_help():
    "Show available commands"
    return qchat.show_help()

@qchat.command("echo")
def cmd_echo(*params):
    "Echo back the message"
    return " ".join(params)

@qchat.command("time")
def cmd_time():
    "Show current time"
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@qchat.command("add")
def cmd_add(a: int, b: int):
    "Add two numbers"
    return a + b

@qchat.command("html")
def cmd_html():
    "Demo of HTML output"
    return """<h1>HTML Demo</h1>
    <p>This is a paragraph of text.</p>
    <p>It can contain <strong>bold</strong> and <em>italic</em> text.</p>
    """

if __name__ == "__main__":
    qchat.run()
