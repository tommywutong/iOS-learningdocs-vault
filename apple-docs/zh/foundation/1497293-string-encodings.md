---
title: 字符串编码
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/1497293-string-encodings
source_url: 'https://developer.apple.com/documentation/foundation/1497293-string-encodings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/1497293-string-encodings.json'
content_hash: 'sha256:40ad8a0691cad551'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md)

# 字符串编码

<sub>API 集合</sub>

在原始数据与字符串表示形式之间进行转换时所使用的编码标准常量。

## 主题

### 7- and 8-bit Encodings

- [NSASCIIStringEncoding](nsasciistringencoding.md) — 使用 8 位字符表示的严格 7 位 ASCII 编码；仅支持 0…127 的 ASCII 值。
- [NSISOLatin1StringEncoding](nsisolatin1stringencoding.md) — 8 位 ISO Latin 1 编码。
- [NSISOLatin2StringEncoding](nsisolatin2stringencoding.md) — 8 位 ISO Latin 2 编码。
- [NSMacOSRomanStringEncoding](nsmacosromanstringencoding.md) — 经典 Macintosh Roman 编码。
- [NSNEXTSTEPStringEncoding](nsnextstepstringencoding.md) — 带有 NEXTSTEP 扩展的 8 位 ASCII 编码。
- [NSNonLossyASCIIStringEncoding](nsnonlossyasciistringencoding.md) — 用于表示所有 Unicode 字符的 7 位详细 ASCII 编码。
- [NSSymbolStringEncoding](nssymbolstringencoding.md) — 8 位 Adobe Symbol 编码向量。

### 7- and 8-bit Japanese Encodings

- [NSISO2022JPStringEncoding](nsiso2022jpstringencoding.md) — 用于电子邮件的 ISO 2022 日语编码。
- [NSJapaneseEUCStringEncoding](nsjapaneseeucstringencoding.md) — 用于日语文本的 8 位 EUC 编码。
- [NSShiftJISStringEncoding](nsshiftjisstringencoding.md) — 用于日语文本的 8 位 Shift-JIS 编码。

### Unicode Encodings

- [NSUTF8StringEncoding](nsutf8stringencoding.md) — Unicode 字符的一种 8 位表示形式，适用于基于 ASCII 的系统进行传输或存储。
- [NSUTF16BigEndianStringEncoding](nsutf16bigendianstringencoding.md) — 指定了明确字节序的 `NSUTF16StringEncoding` 编码。
- [NSUTF16LittleEndianStringEncoding](nsutf16littleendianstringencoding.md) — 指定了明确字节序的 `NSUTF16StringEncoding` 编码。
- [NSUTF16StringEncoding](nsutf16stringencoding.md)
- [NSUnicodeStringEncoding](nsunicodestringencoding.md) — 字符串对象的规范 Unicode 编码。
- [NSUTF32BigEndianStringEncoding](nsutf32bigendianstringencoding.md) — 指定了明确字节序的 `NSUTF32StringEncoding` 编码。
- [NSUTF32LittleEndianStringEncoding](nsutf32littleendianstringencoding.md) — 指定了明确字节序的 `NSUTF32StringEncoding` 编码。
- [NSUTF32StringEncoding](nsutf32stringencoding.md) — 32 位 UTF 编码。

### Windows Code Page Encodings

- [NSWindowsCP1250StringEncoding](nswindowscp1250stringencoding.md) — Microsoft Windows 代码页 1250；等同于 WinLatin2。
- [NSWindowsCP1251StringEncoding](nswindowscp1251stringencoding.md) — Microsoft Windows 代码页 1251，用于编码西里尔字符；等同于 AdobeStandardCyrillic 字体编码。
- [NSWindowsCP1252StringEncoding](nswindowscp1252stringencoding.md) — Microsoft Windows 代码页 1252；等同于 WinLatin1。
- [NSWindowsCP1253StringEncoding](nswindowscp1253stringencoding.md) — Microsoft Windows 代码页 1253，用于编码希腊字符。
- [NSWindowsCP1254StringEncoding](nswindowscp1254stringencoding.md) — Microsoft Windows 代码页 1254，用于编码土耳其字符。

## 另请参阅

### Strings

- [String](../swift/string.md) — 一个 Unicode 字符串值，是字符的集合。
