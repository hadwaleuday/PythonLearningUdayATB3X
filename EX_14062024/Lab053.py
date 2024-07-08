
browser = input("Enter the browser name: \t")
print(browser)
print(type(browser))
browser = browser.lower()
print(browser)

match browser :
    case "chrome":
        print("Chrome code executed")

    case "edge":
        print("Edge code executed")

    case "firefox":
        print("Fire fox code executed")

    case _:
        print("No browser Found")