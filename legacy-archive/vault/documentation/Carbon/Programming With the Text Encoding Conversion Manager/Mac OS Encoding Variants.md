---
title: Programming With the Text Encoding Conversion Manager
apple_id: TP40000932
resource_type: Guide
platform: macOS
topic: Data Management
technology: CoreServices
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ProgWithTECM/tecmgr_encvariants/tecmgr_encvariants.html
archived_at: '2026-07-15T05:24:12.136305Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Programming With the Text Encoding Conversion Manager](Introduction%20to%20Programming%20With%20the%20Text%20Encoding%20Conversion%20Manager.md)


[Next](Document%20Revision%20History.md)[Previous](Character%20Encodings%20and%20Internet%20Names.md)

# Mac OS Encoding Variants

For font-based Mac OS encoding variants, Table B-1 gives the variant name in the English language, comments about the variant (such as whether it is the system or application font), and the constant used to represent the variant.

__Table B-1__  Mac OS Encoding Variants

| English Name | Comments | Constant for Variant |
|  |  |  |
| Mac OS Icelandic Script = `smRoman` (`0`), language = `langIcelandic` (`15`), region = `verIceland` (`21`) | Mac OS Icelandic Script = `smRoman` (`0`), language = `langIcelandic` (`15`), region = `verIceland` (`21`) | Mac OS Icelandic Script = `smRoman` (`0`), language = `langIcelandic` (`15`), region = `verIceland` (`21`) |
| Chicago | System font | `kMacIcelandicStdDefaultVariant` |
| Geneva | Application font | `kMacIcelandicStdDefaultVariant` |
| Monaco |  | `kMacIcelandicStdDefaultVariant` |
| New York |  | `kMacIcelandicStdDefaultVariant` |
| Palatino |  | `kMacIcelandicTTDefaultVariant` |
| Times |  | `kMacIcelandicTTDefaultVariant` |
| Helvetica |  | `kMacIcelandicTTDefaultVariant` |
| Courier |  | `kMacIcelandicTTDefaultVariant` |
|  |  |  |
| Mac OS Japanese | Mac OS Japanese | Mac OS Japanese |
| Osaka | System font, application font | kMacJapaneseStandardVariant |
| Osaka Tohaba |  | kMacJapaneseStandardVariant |
| MaruGothic |  | \* |
| HonMincho |  | \* |
| TohabaGothic |  | kMacJapaneseBasicVariant |
| TohabaMincho |  | kMacJapaneseBasicVariant |
| ChuGothic | PostScript | kMacJapanesePostScriptScrnVariant |
| SaiMincho | PostScript | kMacJapanesePostScriptScrnVariant |
| HeiseiKakuGothic |  | kMacJapaneseStandardVariant |
| HeiseiMincho |  | kMacJapaneseStandardVariant |
| ChuGothic BBB |  | kMacJapaneseStandardVariant |
| ChuGothic BBB Tohaba |  | kMacJapaneseStandardVariant |
| Ryumin Light-KL |  | kMacJapaneseStandardVariant |
| Ryumin Light-KL-Tohaba |  | kMacJapaneseStandardVariant |
| \* (For System 7.1-J, the constant is `kMacJapaneseVertAtKuPlusTenVariant`, otherwise it’s kMacJapaneseStandardVariant.) | \* (For System 7.1-J, the constant is `kMacJapaneseVertAtKuPlusTenVariant`, otherwise it’s kMacJapaneseStandardVariant.) | \* (For System 7.1-J, the constant is `kMacJapaneseVertAtKuPlusTenVariant`, otherwise it’s kMacJapaneseStandardVariant.) |
|  |  |  |
| Mac OS Arabic | Mac OS Arabic | Mac OS Arabic |
| Cairo | System font | kMacArabicStandardVariant |
| Geeza | Application font | kMacArabicTrueTypeVariant |
| Nadeem |  | kMacArabicTrueTypeVariant |
| Baghdad |  | kMacArabicTrueTypeVariant |
| Kufi |  | kMacArabicTrueTypeVariant |
| Thuluth | PostScript | kMacArabicThuluthVariant |
| Thuluth Bold | PostScript | kMacArabicThuluthVariant |
| AlBayan |  | kMacArabicAlBayanVariant |
|  |  |  |
| Mac OS Farsi Script = `smArabic` (4), language = `langFarsi` (31), region = `verIran` (48) | Mac OS Farsi Script = `smArabic` (4), language = `langFarsi` (31), region = `verIran` (48) | Mac OS Farsi Script = `smArabic` (4), language = `langFarsi` (31), region = `verIran` (48) |
| Tehran | System font | kMacFarsiStandardVariant |
| Asfahan |  | kMacFarsiTrueTypeVariant |
| Mashad |  | kMacFarsiTrueTypeVariant |
| NadeemFarsi |  | kMacFarsiTrueTypeVariant |
| Kamran |  | kMacFarsiTrueTypeVariant |
| Amir |  | kMacFarsiTrueTypeVariant |
|  |  |  |
| Mac OS Hebrew | Mac OS Hebrew | Mac OS Hebrew |
| Eilat | System font | kMacHebrewStandardVariant |
| Hermon | Application font | kMacHebrewStandardVariant |
| Arial |  | kMacHebrewStandardVariant |
| New Peninim |  | kMacHebrewStandardVariant |
| Corsiva |  | kMacHebrewStandardVariant |
| Raanana |  | kMacHebrewStandardVariant |
| RamatGan |  | kMacHebrewStandardVariant |
| Sinai Book |  | kMacHebrewFigureSpaceVariant |
| Ramat Sharon |  | kMacHebrewFigureSpaceVariant |
| Carmel |  | kMacHebrewFigureSpaceVariant |
| Caesarea |  | kMacHebrewFigureSpaceVariant |
| Gilboa |  | kMacHebrewFigureSpaceVariant |

[Next](Document%20Revision%20History.md)[Previous](Character%20Encodings%20and%20Internet%20Names.md)

