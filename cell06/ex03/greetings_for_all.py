def greetings(text=None):
    if text is None:
        print("noble stranger")
    elif type(text) != str:
        print("Error! It was not a name")
    else:
        print(f"Hello, {text}!")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)