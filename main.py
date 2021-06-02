from BukoPyInterpreter import *


def main():
    while True:
        text = input('BukoPy >> ')
        if text.strip() == "":
            continue

        result, error = run('<stdin>', text)

        if error:
            print(error.as_string())

        elif result:
            if len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))


if __name__ == '__main__':
    main()
