import re
data = open("data.txt")

def getPassports():
    return data.read().split("\n\n")


def getPassportEntries(passportStr):
    return re.split(" |\n", passportStr)


def isValidPassport(entries):
    foundEntries = 0
    requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for entry in entries:
        if entry.split(":")[0] in requiredFields:
            foundEntries += 1
    return foundEntries == 7


def main():
    validPassports = 0
    passports = getPassports()

    for passportStr in passports:
        if isValidPassport(getPassportEntries(passportStr)):
            validPassports += 1
    print(validPassports)

main()
