import re
data = open("data.txt")


def getPassports():
    return data.read().split("\n\n")


def getPassportEntries(passportStr):
    return re.split(" |\n", passportStr)


def isRequiredFieldsPresent(entries):
    foundEntries = 0
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for entry in entries:
        if entry.split(":")[0] in requiredFields:
            foundEntries += 1
    return foundEntries == 7


def validateHgt(passportDict):
    hgt = passportDict['hgt']
    for i, c in enumerate(hgt):
        if not c.isdigit():
            break
    number = int(hgt[:i])
    unit = hgt[i:]
    if not unit:
        return False
    if unit == 'cm':
        return 149 < number < 194
    if unit == 'in':
        return 58 < number < 77


def validateHcl(passportDict):
    regex = re.compile('^#(?:[0-9a-f]{3}){1,2}$')
    match = regex.match(passportDict['hcl'])
    return bool(match) and len(passportDict['hcl']) == 7


def validateEcl(passportDict):
    ecl = passportDict['ecl']
    allowed = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in allowed


def validatePid(passportDict):
    regex = re.compile('^(?:[0-9]){9}')
    match = regex.match(passportDict['pid'])
    pid = passportDict['pid']
    return len(pid) == 9 and bool(match)

def validYear(value):
    regex = re.compile('^(?:[0-9]){4}')
    match = regex.match(value)
    return bool(match)


def validateFields(entries):
    passportDict = {}

    for entry in entries:
        entryPair = entry.split(":")
        passportDict[entryPair[0]] = entryPair[1]

    valid = (1919 < int(passportDict['byr']) < 2003
            and 2009 < int(passportDict['iyr']) < 2021
            and 2019 < int(passportDict['eyr']) < 2031
            and validYear(passportDict['byr'])
            and validYear(passportDict['iyr'])
            and validYear(passportDict['eyr'])
            and validateEcl(passportDict)
            and validateHgt(passportDict)
            and validateHcl(passportDict)
            and validatePid(passportDict)
            )
    if valid:
      print(passportDict['pid'])
    return valid


def main():
    validPassports = 0
    passports = getPassports()

    for passportStr in passports:
        entries = getPassportEntries(passportStr)
        if isRequiredFieldsPresent(entries) and validateFields(entries):
            # print(entries)
            validPassports += 1
    print(validPassports)


main()
