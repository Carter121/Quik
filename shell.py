import quik

while True:
    text = input("quik > ")
    result, error = quik.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)