import re

def mobilevalidation(mobile):
    regg=re.compile("^(?:0|\+?977)\s?(?:\d\s?){9,14}$")
    if re.fullmatch(regg, mobile):
        Result=True
    else:
        Result=False

    return Result



def emailvalidation(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        emailresult = True

    else:
        emailresult = False

    return emailresult


def namevalidation(name):
    regex=re.compile("^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)")
    if re.fullmatch(regex, name):
        nameResult=True
    else:
        nameResult=False
    return nameResult