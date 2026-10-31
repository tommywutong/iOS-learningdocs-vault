---
title: 预定义的 CFCharacterSet 选择器值
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/predefined_cfcharacterset_selector_values
source_url: 'https://developer.apple.com/documentation/corefoundation/predefined_cfcharacterset_selector_values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/predefined_cfcharacterset_selector_values.json'
content_hash: 'sha256:ee7e39a2ff544443'
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFCharacterSet](cfcharacterset.md)

# 预定义的 CFCharacterSet 选择器值

<sub>API 集合</sub>

可用预定义 CFCharacterSet 对象的标识符。

## 概述

将这些常量与 [CFCharacterSetGetPredefined](<cfcharactersetgetpredefined(__).md>) 函数一起使用，以获取某个预定义字符集。

## 主题

### 常量

- [kCFCharacterSetControl](cfcharactersetpredefinedset/control.md) — 控制字符集（Unicode 通用类别 Cc 与 Cf）。
- [kCFCharacterSetWhitespace](cfcharactersetpredefinedset/whitespace.md) — 空白字符集（Unicode 通用类别 Zs 与 U0009 CHARACTER TABULATION）。
- [kCFCharacterSetWhitespaceAndNewline](cfcharactersetpredefinedset/whitespaceandnewline.md) — 空白与换行字符集（Unicode 通用类别 Z*、`U000A ~ U000D`，以及 `U0085`）。
- [kCFCharacterSetDecimalDigit](cfcharactersetpredefinedset/decimaldigit.md) — 十进制数字字符集。
- [kCFCharacterSetLetter](cfcharactersetpredefinedset/letter.md) — 字母字符集（Unicode 通用类别 L* 与 M*）。
- [kCFCharacterSetLowercaseLetter](cfcharactersetpredefinedset/lowercaseletter.md) — 小写字母字符集（Unicode 通用类别 Ll）。
- [kCFCharacterSetUppercaseLetter](cfcharactersetpredefinedset/uppercaseletter.md) — 大写字母字符集（Unicode 通用类别 Lu 与 Lt）。
- [kCFCharacterSetNonBase](cfcharactersetpredefinedset/nonbase.md) — 非基字符集（Unicode 通用类别 M*）。
- [kCFCharacterSetDecomposable](cfcharactersetpredefinedset/decomposable.md) — 可规范分解字符集。
- [kCFCharacterSetAlphaNumeric](cfcharactersetpredefinedset/alphanumeric.md) — 字母数字字符集（Unicode 通用类别 L*、M* 与 N*）。
- [kCFCharacterSetPunctuation](cfcharactersetpredefinedset/punctuation.md) — 标点字符集（Unicode 通用类别 P*）。
- [kCFCharacterSetCapitalizedLetter](cfcharactersetpredefinedset/capitalizedletter.md) — 标题大小写字符集（Unicode 通用类别 Lt）。
- [kCFCharacterSetSymbol](cfcharactersetpredefinedset/symbol.md) — 符号字符集（Unicode 通用类别 S*）。
- [kCFCharacterSetNewline](cfcharactersetpredefinedset/newline.md) — 换行字符集（`U000A ~ U000D`、`U0085`、`U2028` 与 `U2029`）。
- [kCFCharacterSetIllegal](cfcharactersetpredefinedset/illegal.md) — 非法字符集。
