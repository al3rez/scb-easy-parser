#!/usr/bin/env python3

import re
import sys

AMOUNT_REGEX = '\d{1,3}(,\d{3})*(\.\d+)'
DATE_REGEX = '\d{1,2}\/\d{1,2}\/\d{4}'
CASH_OUT = 'เงินออก'
MONEY_IN = 'เงินเข้า'
PAY = 'ชำระเงิน'

def regex_search(pattern, str):
    return re.compile(pattern).search(str).group(0)

with open(sys.argv[1]) as f:
    lines = f.read().replace(r'\r','\n').split('\n')
    print("Category|", "Date|", "Amount")
    for line in lines:
        if CASH_OUT in line:
            amount = regex_search(AMOUNT_REGEX, line)
            date = regex_search(DATE_REGEX, line)
            print("[CASH OUT]|", date+"|", amount)
            continue
        if MONEY_IN in line:
            amount = regex_search(AMOUNT_REGEX, line)
            date = regex_search(DATE_REGEX, line)
            print("[MONEY IN]|", date+"|", amount)
            continue
        if PAY in line:
            amount = regex_search(AMOUNT_REGEX, line)
            date = regex_search(DATE_REGEX, line)
            print("[PAY]|", date+"|", amount)
            continue