'''
эта вещь увеличивает введенные цифры 1,2,3 и 0
типа так
  1    333   333   000
 11      3     3   0 0
  1     3     3    0 0
  1    333   333   0 0
  1      3     3   0 0
  1     3     3    0 0
 111   3     3     000
'''
try:
    Digits = [
    [" *** ", " * * ", " * * ", " * * ", " * * ", " * * ", " *** "], # Zero
    ["  *  ", " **  ", "  *  ", "  *  ", "  *  ", "  *  ", " *** "], # One
    [" *** ", "   * ", "   * ", "  *  ", " *   ", " *   ", " *** "], #TwoP
    [" *** ", "   * ", "  *  ", " *** ", "   * ", "  *  ", " *   "], #Three
    [" * * ", " * * ", " * * ", " *** ", "   * ", "   * ", "   * "]  #Four
    ]
    digits = input()
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            st = digit[row]
            st = st.replace('*', str(digits[column]))
            line += st + " "
            column += 1
        print(line)
        row += 1
except ValueError as err:
    print(err, "in", digits)
except IndexError:
    print("usage 1,2,3 and 0, please")

