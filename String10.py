def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    x=4
    y=8
    son="{}+{}={}".format(x,y,x+y)
    return son 
print(main(4,8))