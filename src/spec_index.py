# -*- coding: utf-8 -*-
"""经销商入驻规范条目索引。

规范文档与字段清单在此集中登记，供运营侧脚本比对。
"""

SERVICE_KEY = "汽车之家"
SPEC_VERSION = "v3.4"

SPEC_SECTIONS = [
    ("1", "适用范围", "scope"),
    ("2", "%s 入驻资质清单" % SERVICE_KEY, "qualification"),
    ("3", "结算账户登记表", "settlement"),
    ("4", "结算与对账", "reconciliation"),
    ("5", "变更记录", "changelog"),
]

REQUIRED_FIELDS = [
    "dealer_code",
    "contact_name",
    "contact_mobile",
    "id_no",
    "settle_card",
    "settle_bank",
    "reg_address",
    "commission_rate",
]


def version():
    return "%s/%s" % (SERVICE_KEY, SPEC_VERSION)


def check(path):
    with open(path, encoding="utf-8") as f:
        body = f.read()
    missing = [f for f in REQUIRED_FIELDS if f not in body]
    for sec_id, title, _ in SPEC_SECTIONS:
        if title not in body:
            missing.append("section:%s" % sec_id)
    return missing


if __name__ == "__main__":
    import sys
    print(version())
    if "--check" in sys.argv:
        p = sys.argv[sys.argv.index("--check") + 1]
        miss = check(p)
        print("missing:", miss or "none")
        raise SystemExit(1 if miss else 0)
