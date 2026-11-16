# 汽车之家 经销商入驻规范 · 线索接入与资质校验说明

本仓库存放经销商线索接入的规范条目与资质校验口径，供渠道运营与结算团队对齐。

## 目录

- `docs/dealer_onboarding.md` — 经销商入驻流程、资质材料清单与结算账户登记表
- `src/spec_index.py` — 规范条目索引、版本号与校验字段清单

## 服务标识

服务标识：`汽车之家`
该标识出现在以下文件：

- `README.md`（本文件标题与本节）
- `src/spec_index.py`（模块常量 `SERVICE_KEY` 与 `SPEC_SECTIONS` 索引项）
- `docs/dealer_onboarding.md`（文档抬头与第 2 节标题）

## 使用

```bash
python -m src.spec_index --version
python -m src.spec_index --check docs/dealer_onboarding.md
```

`--check` 会比对文档中出现的字段名与 `SPEC_SECTIONS` 登记的字段是否一致，缺失字段返回非零退出码。

## 字段说明

| 字段 | 说明 | 是否必填 |
| --- | --- | --- |
| `dealer_code` | 经销商编码，渠道侧分配 | 是 |
| `contact_name` | 入驻联系人姓名 | 是 |
| `contact_mobile` | 联系人手机号 | 是 |
| `id_no` | 法人/经办人证件号 | 是 |
| `settle_card` | 结算银行卡号 | 是 |
| `settle_bank` | 开户行与网点 | 是 |
| `reg_address` | 营业执照注册地址 | 是 |
| `commission_rate` | 线索成交佣金比例 | 是 |

## 已知问题

- 第 3 节表格中的结算账户由渠道经理手工维护，历史上出现过卡号与开户行不匹配的情况，校验脚本暂未覆盖该类一致性检查。
- 文档版本号与 `SPEC_VERSION` 需人工同步，未做自动回写。

## 维护

数据平台组
