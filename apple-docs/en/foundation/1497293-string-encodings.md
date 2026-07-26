---
title: String Encodings
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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md)

# String Encodings

<sub>API Collection</sub>

Constants for encoding standards used when converting raw data to and from string representations.

## Topics

### 7- and 8-bit Encodings

- [NSASCIIStringEncoding](nsasciistringencoding.md) — Strict 7-bit ASCII encoding within 8-bit chars; ASCII values 0…127 only.
- [NSISOLatin1StringEncoding](nsisolatin1stringencoding.md) — 8-bit ISO Latin 1 encoding.
- [NSISOLatin2StringEncoding](nsisolatin2stringencoding.md) — 8-bit ISO Latin 2 encoding.
- [NSMacOSRomanStringEncoding](nsmacosromanstringencoding.md) — Classic Macintosh Roman encoding.
- [NSNEXTSTEPStringEncoding](nsnextstepstringencoding.md) — 8-bit ASCII encoding with NEXTSTEP extensions.
- [NSNonLossyASCIIStringEncoding](nsnonlossyasciistringencoding.md) — 7-bit verbose ASCII to represent all Unicode characters.
- [NSSymbolStringEncoding](nssymbolstringencoding.md) — 8-bit Adobe Symbol encoding vector.

### 7- and 8-bit Japanese Encodings

- [NSISO2022JPStringEncoding](nsiso2022jpstringencoding.md) — ISO 2022 Japanese encoding for email.
- [NSJapaneseEUCStringEncoding](nsjapaneseeucstringencoding.md) — 8-bit EUC encoding for Japanese text.
- [NSShiftJISStringEncoding](nsshiftjisstringencoding.md) — 8-bit Shift-JIS encoding for Japanese text.

### Unicode Encodings

- [NSUTF8StringEncoding](nsutf8stringencoding.md) — An 8-bit representation of Unicode characters, suitable for transmission or storage by ASCII-based systems.
- [NSUTF16BigEndianStringEncoding](nsutf16bigendianstringencoding.md) — `NSUTF16StringEncoding` encoding with explicit endianness specified.
- [NSUTF16LittleEndianStringEncoding](nsutf16littleendianstringencoding.md) — `NSUTF16StringEncoding` encoding with explicit endianness specified.
- [NSUTF16StringEncoding](nsutf16stringencoding.md)
- [NSUnicodeStringEncoding](nsunicodestringencoding.md) — The canonical Unicode encoding for string objects.
- [NSUTF32BigEndianStringEncoding](nsutf32bigendianstringencoding.md) — `NSUTF32StringEncoding` encoding with explicit endianness specified.
- [NSUTF32LittleEndianStringEncoding](nsutf32littleendianstringencoding.md) — `NSUTF32StringEncoding` encoding with explicit endianness specified.
- [NSUTF32StringEncoding](nsutf32stringencoding.md) — 32-bit UTF encoding.

### Windows Code Page Encodings

- [NSWindowsCP1250StringEncoding](nswindowscp1250stringencoding.md) — Microsoft Windows codepage 1250; equivalent to WinLatin2.
- [NSWindowsCP1251StringEncoding](nswindowscp1251stringencoding.md) — Microsoft Windows codepage 1251, encoding Cyrillic characters; equivalent to AdobeStandardCyrillic font encoding.
- [NSWindowsCP1252StringEncoding](nswindowscp1252stringencoding.md) — Microsoft Windows codepage 1252; equivalent to WinLatin1.
- [NSWindowsCP1253StringEncoding](nswindowscp1253stringencoding.md) — Microsoft Windows codepage 1253, encoding Greek characters.
- [NSWindowsCP1254StringEncoding](nswindowscp1254stringencoding.md) — Microsoft Windows codepage 1254, encoding Turkish characters.

## See Also

### Strings

- [String](../swift/string.md) — A Unicode string value that is a collection of characters.
