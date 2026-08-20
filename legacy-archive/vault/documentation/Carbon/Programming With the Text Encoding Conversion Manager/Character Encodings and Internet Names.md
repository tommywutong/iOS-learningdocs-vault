---
title: Programming With the Text Encoding Conversion Manager
apple_id: TP40000932
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgWithTECM/tecmgr_encnames/tecmgr_encnames.html
archived_at: '2026-07-15T05:24:12.112888Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming With the Text Encoding Conversion Manager](Introduction%20to%20Programming%20With%20the%20Text%20Encoding%20Conversion%20Manager.md)


[Next](Mac%20OS%20Encoding%20Variants.md)[Previous](Writing%20Custom%20Plug-Ins.md)

# Character Encodings and Internet Names

This document provides information on character encodings and the Internet. It discusses the Internet Assigned Numbers Authority (IANA) registry, Internet names used for similar character encodings that could lead to confusion, and provides a list of common Internet names for character encodings along with their availability in the Mac OS.

In many Internet protocols, a `charset` parameter may be used in certain contexts to specify both a character set and a character encoding scheme. The value of the `charset` parameter is a case-insensitive string limited to the characters A–Z, a–z, 0–9, hyphen–minus, underscore, period, and colon. The character encoding names specified for this parameter are generally expressed in US–ASCII octet values.

The character encoding name may be an experimental name beginning with `x-`; if it is not an experimental name, it must be a name registered with the Internet Assigned Numbers Authority (IANA) that corresponds to a character encoding that has a formal specification. Multiple names exist for most character encodings in the registry. Note that the IANA registry is updated periodically. [Table A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmzsfvbuqmrqgqwugsscjbbusq2e) identifies character encodings for various languages, gives some of their common Internet names, and tells when the character encoding was first supported for the Text Encoding Converter and the Unicode Converter. To preview the style of character set name used on the Internet, here are a few sample names:

`ISO-8859-1 latin1 UNICODE-1-1-UTF-7 Shift_JIS X-EUC-CN`

Many of the character encodings in use on the Internet are not registered with IANA and do not have official Internet names, although they may have names that have become de facto standards. Moreover, even when an encoding is registered, the name specified by IANA may not be the one that is actually used on the Internet. For example, EUC-JP has been registered for some time with the unwieldy name `Extended_UNIX_Code_Packed_Format_for_Japanese`, but the name actually used is the unofficial `X-EUC-JP`. Another example, `Shift_JIS`,is the official name, but the names commonly used in its stead are `x-shift-jis` and `x-sjis`. In many cases, mail and browser software recognizes only the unofficial names, not the official ones.

In some cases, the names for unregistered encodings follow a pattern established by other, registered encodings. For example, some IBM/Microsoft code pages are registered with names consisting of `cp` followed by the code page number: `cp437`, `cp850`, `cp852`. Code page `874` is not registered, but the name `cp874` would be expected. Most Windows code pages are registered using the form used in these examples: `windows-1250`, `windows-1251`. Windows Latin-1 is, oddly enough, not registered as either `windows-1252` or `cp1252`, although both forms are in use.

Some Internet names used for similar character encodings could lead to confusion. For example, the Windows Latin-1 character encoding is commonly labeled `ISO-8859-1` on the Internet because it is a superset of ISO 8859-1. Clients that actually treat it as ISO 8859-1 may be confused by the extra characters in the C1 area.

The Mac OS Roman character set used for Western European languages was created several years before ISO 8859-1. It does not have exactly the same repertoire, and many of the characters it does share with ISO 8859-1 have different code points. Many Mac OS Internet applications use an encoding developed by André Pirard in which the Mac OS Roman repertoire is assigned new code points to align as much as possible with ISO 8859-1; this character encoding is referred to as Mac Latin-1 or Mac Mail and is usually labeled as ISO-8859-1 on the Internet.

Table A-1 lists character encodings for various languages, gives some of their common Internet names, and identifies the version of the Text Encoding Conversion Manager for which character encoding was first supported for use by the Text Encoding Converter and the Unicode Converter. In the last two columns of the table, “N/A” means that the encoding is not supported.

__Table A-1__  Character encoding Internet names and availability in Mac OS

| Character encoding | Common Internet names | Related information | __Version of Text Encoding Conversion Manager that first offered support in:__ | __Version of Text Encoding Conversion Manager that first offered support in:__ |
|  |  |  | Text Encoding Converter | Unicode Converter |
| Universal | Universal | Universal | Universal | Universal |
| Unicode 2.0 (16 bit) | `UTF-16` |  | 1.2 | 1.2 |
| Unicode 2.0 UTF-8 | `UTF-8` |  | 1.2 | 1.2.1 |
| Unicode 2.0 UTF-7 | `UTF-7` |  | 1.2 | N/A |
| Unicode 1.1 (16-bit) | `UNICODE 1-1` |  | 1.2 | 1.2 |
| Unicode 1.1 UTF-8 | `UNICODE-1-1-UTF-8` |  | 1.2 | 1.2.1 |
| Unicode 1.1 UTF-7 | `UNICODE-1-1-UTF-7` |  | 1.2 | N/A |
| Western European languages | Western European languages | Western European languages | Western European languages | Western European languages |
| ASCII | `US-ASCII` |  | 1.2.1 | 1.2.1 |
| ISO 8859-1 (Latin-1) | `ISO-8859-1`, `latin1` |  | 1.2.1 | 1.2.1 |
| ISO 8859-3 (Latin 3) | `ISO-8859-3 , latin3` |  | 1.5 | 1.5 |
| ISO-8859-15 (Latin 9) | `ISO-8859-15, latin9` | Latin-1 with EURO SIGN and CP 1252 letters | 1.5 | 1.5 |
| CP 1252 (Windows Latin-1) | `windows-1252`, `cp1252` | ISO 8859-1, plus additions in C1 area | 1.2 | 1.2 |
| CP 437 (DOS Latin-US) | `cp437` |  | 1.2 | 1.2 |
| CP 850 (DOS Latin-1) | `cp850` |  | 1.4 | 1.4 |
| Mac OS Roman | `mac`, `macintosh`, `x-mac-roman` |  | 1.2 | 1.2 |
| Mac OS Icelandic | `x-mac-icelandic` | based on Mac OS Roman | 1.2 | 1.2 |
| Mac OS Latin-1, Mac OS Mail | `x-mac-latin1` (commonly sent as ISO-8859-1) | Mac OS Roman permuted to align with 8859-1 | 1.2 | 1.2 |
| NextStep Latin |  |  | 1.2 | 1.2 |
| CP 037 (EBCDIC-US) | `cp037` | ISO 8859-1 repertoire, different layout | 1.2.1 | 1.2.1 |
| Arabic | Arabic | Arabic | Arabic | Arabic |
| ISO 8859-6 (Latin/Arabic) | `ISO-8859-6`, `arabic` |  | 1.2 | 1.2 |
| CP 1256 (Windows Arabic) | `windows-1256`, `cp1256` | Partly 8859-6, plus C1 additions | 1.2 | 1.2 |
| CP 864 (DOS Arabic) | `cp864` | Encodes Arabic presentation forms | 1.2 | 1.2 |
| Mac OS Arabic | `x-mac-arabic` |  | 1.2 | 1.2 |
| Mac OS Farsi | `x-mac-farsi` |  | 1.2 | 1.2 |
| Central European languages | Central European languages | Central European languages | Central European languages | Central European languages |
| ISO 8859-2 (Latin-2) | `ISO-8859-2`, `latin2` |  | 1.2 | 1.2 |
| ISO 8859-4 (Latin-4) | `ISO-8859-4`, `latin4` |  | 1.5 | 1.5 |
| CP 1250 (Windows Latin-2) | `windows-1250`, `cp 1250` | Partly 8859-2, plus C1 additions | 1.2 | 1.2 |
| CP 1257 (Windows BalticRim) | `windows-1257,cp 1257` |  | 1.5 | 1.5 |
| Mac OS Central European Roman | `x-mac-centraleurroman` |  | 1.2 | 1.2 |
| Mac OS Croatian | `x-mac-croatian` | Based on Mac OS Roman | 1.2 | 1.2 |
| Mac OS Romanian | `x-mac-romanian` | Based on Mac OS Roman | 1.2 | 1.2 |
| Chinese |  |  |  |  |
| GB 2312-80 |  |  | 1.2 | N/A |
| EUC-CN | `GB2312`, `X-EUC-CN` | ASCII + GB 2312- 80 (8-bit) | 1.2 | 1.2 |
| CP 936 (DOS and Windows Simplified) |  | Similar to GBK | 1.4 | 1.4 |
| Mac OS Chinese Simplified |  | Based on EUC-CN | 1.2 | 1.2 |
| ISO 2022-CN ("GB") | `ISO-2022-CN` | ASCII + GB 2312-80 (7-bit) (see RFC1922) | 1.2 | N/A |
| HZ | `HZ-GB-2312` | ASCII + GB 2312-80 (7-bit) (see RFC1842); | 1.2 | N/A |
| GBK (extended GB) |  | EUC-CN + Unihan repertoire (8-bit) | 1.2 | 1.2 |
| CNS 11643 plane 1 | `x-cns11643-1` |  | N/A | N/A |
| CNS 11643 plane 2 | `x-cns11643-2` |  | N/A | N/A |
| EUC-TW | `X-EUC-TW` | ASCII + CNS 11643-1992 (8-bit) | 1.2 | 1.2 |
| Big-5 | `Big5` | (8-bit) | 1.2 | 1.2 |
| CP 950 (DOS and Windows Traditional) |  | Based on Big-5 | 1.4 | 1.4 |
| Mac OS Chinese Traditional |  | Based on Big-5 | 1.2 | 1.2 |
| CCCII |  |  | N/A | N/A |
| EACC |  |  | N/A | N/A |
| Cyrillic | Cyrillic | Cyrillic | Cyrillic | Cyrillic |
| ISO 8859-5 (Latin/Cyrillic) | `ISO-8859-5`, `cyrillic` |  | 1.2 | 1.2 |
| KOI8-R | `KOI8-R` | See Rfc 1489 | 1.2 | 1.2 |
| CP 1251 (Windows Cyrillic) | `windows-1251`, `cp1251` | Not based on ISO 8859-5 | 1.2 | 1.2 |
| CP 866 (DOS Russian) | `cp866` |  | N/A | N/A |
| Mac OS Cyrillic | `x-mac-cyrillic` |  | 1.2 | 1.2 |
| Mac OS Ukrainian | `x-mac-ukrainian` | Mac OS Cyrillic with two replacements | 1.2 | 1.2 |
| Greek | Greek | Greek | Greek | Greek |
| ISO 8859-7 | `ISO-8859-7`, `greek` |  | 1.2 | 1.2 |
| ISO 5428 | `ISO_5428:1980` |  | N/A | N/A |
| CP 1253 (Windows Greek) | `windows-1253`, `cp1253` | Nearly 8859-7, plus C1 additions | 1.2 | 1.2 |
| Mac OS Greek | `x-mac-greek` |  | 1.2 | 1.2 |
| Greek CCITT | `greek-ccitt` |  | N/A | N/A |
| Hebrew | Hebrew | Hebrew | Hebrew | Hebrew |
| ISO 8859-8 (Latin/Hebrew) | `ISO-8859-8`, `hebrew` |  | 1.2 | 1.2 |
| CP 1255 (Windows Hebrew) | `windows-1255`,`cp1255` | Mostly 8859-8, plus C1 additions | 1.2 | 1.2 |
| Mac OS Hebrew (2 variants) | `x-mac-hebrew` |  | 1.2 | 1.2 |
| Indic | Indic | Indic | Indic | Indic |
| ISCII-91 |  | Parallel encodings for all Indic scripts | N/A | N/A |
| Mac OS Gujarati |  |  | 1.2 | 1.2 |
| Mac OS Devanagari |  |  | 1.2 | 1.2 |
| Mac OS Gurmukhi |  |  | 1.2 | 1.2 |
| Japanese | Japanese | Japanese | Japanese | Japanese |
| JIS X0208 |  |  | 1.2 | N/A |
| JIS X0212 |  |  | N/A | N/A |
| EUC-JP | `EUC-JP`, `X-EUC-JP` | JIS 201 + JIS 208 + JIS 212 (8-bit) | 1.2 | 1.4 |
| ISO 2022-JP ("JIS") | `ISO-2022-JP` | JIS 201 + JIS 208 + JIS 212 (7-bit); Rfc 1468 | 1.2 | N/A |
| Shift-JIS | `Shift_JIS`, `x-sjis`, `x-shift-jis` | JIS 201 + JIS 208 (8-bit) | 1.2 | 1.2 |
| CP 932 (DOS + Windows) |  | Based on Shift-JIS | 1.4 | 1.4 |
| Mac OS Japanese |  | Based on Shift-JIS | 1.2 | 1.2 |
| Korean | Korean | Korean | Korean | Korean |
| KSC 5601-1987 |  |  | 1.2 | N/A |
| EUC-KR | `EUC-KR` | ASCII + KSC 5601-87 (8-bit); Rfc 1557 | 1.2 | 1.2 |
| CP 949 (DOS + Windows) |  | Unified Hangul Code: EUC-KR + Johab | N/A | N/A |
| Mac OS Korean |  | Based on EUC-KR | 1.2 | 1.2 |
| ISO 2022-KR ("KSC") | `ISO-2022-KR` | ASCII + KSC 5601-87 (7-bit): Rfc 1557 | 1.2 | N/A |
| KSC 5700 |  |  | N/A | N/A |
| Symbols encoding | Symbols encoding | Symbols encoding | Symbols encoding | Symbols encoding |
| Adobe Symbol | `Adobe-Symbol-Encoding` |  | N/A | N/A |
| Mac OS Symbol | `x-mac-symbol` | Based on Adobe Symbol | 1.2 | 1.2 |
| Mac OS dingbats | `x-mac-dingbats` | Based on Adobe Zapf Dingbats | 1.2 | 1.2 |
| Thai | Thai | Thai | Thai | Thai |
| TIS 620-2533 |  |  | N/A | N/A |
| CP 874 (DOS + Windows) | `cp874` | Based on TIS 620-2533 | 1.4 | 1.4 |
| Mac OS Thai | `x-mac-thai` | Based on TIS 620-2533 | 1.2 | 1.2 |
| Turkish | Turkish | Turkish | Turkish | Turkish |
| ISO 8859-9 (Latin-5) | `ISO-8859`, `latin5` |  | 1.2 | 1.2 |
| ISO 8859-3 (Latin-3) | `ISO-8859-3` |  | N/A | N/A |
| CP 1254 (Windows Latin-5) | `windows-1254`, `cp1254` |  | 1.2 | 1.2 |
| Mac OS Turkish | `x-mac-turkish` | Based on Mac OS Roman | 1.2 | 1.2 |
| Vietnamese | Vietnamese | Vietnamese | Vietnamese | Vietnamese |
| VISCII | `VISCII` | Rfc 1456 | N/A | N/A |
| TCVN-n |  |  | N/A | N/A |
| CP 1258 (Windows Vietnamese) | `windows-1258, cp1258` |  | 1.5 | 1.5 |

[Next](Mac%20OS%20Encoding%20Variants.md)[Previous](Writing%20Custom%20Plug-Ins.md)

