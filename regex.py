import re
# formats dd/mm/yyyy,dd-mm-yyyy or dd.mm.yyyy
dateRe = re.compile("^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$")


def checkDate(date):
    return dateRe.search(date)
