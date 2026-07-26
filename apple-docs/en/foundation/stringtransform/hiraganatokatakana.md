---
title: hiraganaToKatakana
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringtransform/hiraganatokatakana
source_url: 'https://developer.apple.com/documentation/foundation/stringtransform/hiraganatokatakana'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringtransform/hiraganatokatakana.json'
content_hash: 'sha256:fd630bef3ab32699'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StringTransform](../stringtransform.md)

# hiraganaToKatakana

<sub>Type Property</sub>

A constant containing the transliteration of a string from Hiragana script to Katakana script.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let hiraganaToKatakana: StringTransform
```

## Discussion

This transformation is reversible.

For example, the string “ひらがな” transliterates to “カタカナ”.

This is equivalent to [kCFStringTransformHiraganaKatakana](../../corefoundation/kcfstringtransformhiraganakatakana.md).

## See Also

### Constants

- [NSStringTransformLatinToKatakana](latintokatakana.md) — A constant containing the transliteration of a string from Latin script to Katakana script.
- [NSStringTransformLatinToHiragana](latintohiragana.md) — A constant containing the transliteration of a string from Latin script to Hiragana script.
- [NSStringTransformLatinToHangul](latintohangul.md) — A constant containing the transliteration of a string from Latin script to Hangul script.
- [NSStringTransformLatinToArabic](latintoarabic.md) — A constant containing the transliteration of a string from Latin script to Arabic script.
- [NSStringTransformLatinToHebrew](latintohebrew.md) — A constant containing the transliteration of a string from Latin script to Hebrew script.
- [NSStringTransformLatinToThai](latintothai.md) — A constant containing the transliteration of a string from Latin script to Thai script.
- [NSStringTransformLatinToCyrillic](latintocyrillic.md) — A constant containing the transliteration of a string from Latin script to Cyrillic script.
- [NSStringTransformToLatin](tolatin.md) — A constant containing the transliteration of a string from any script to Latin script.
- [NSStringTransformMandarinToLatin](mandarintolatin.md) — A constant containing the transliteration of a string from Han script to Latin.
- [NSStringTransformFullwidthToHalfwidth](fullwidthtohalfwidth.md) — A constant containing the transformation of a string from full-width CJK characters to half-width forms.
- [NSStringTransformToXMLHex](toxmlhex.md) — A constant containing the transformation of a string from characters to XML hexadecimal escape codes.
- [NSStringTransformToUnicodeName](tounicodename.md) — An identifier for a transform that converts characters to Unicode names.
- [NSStringTransformStripCombiningMarks](stripcombiningmarks.md) — A constant containing the transformation of a string by removing combining marks.
- [NSStringTransformStripDiacritics](stripdiacritics.md) — A constant containing the transformation of a string by removing diacritics.
