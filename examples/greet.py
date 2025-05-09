import qchat

@qchat.command("greet")
def greet(name: str):
    """Greet a user"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    qchat.run()