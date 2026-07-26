---
title: latinToCyrillic
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringtransform/latintocyrillic
source_url: 'https://developer.apple.com/documentation/foundation/stringtransform/latintocyrillic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringtransform/latintocyrillic.json'
content_hash: 'sha256:aa835fa6a0df1764'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StringTransform](../stringtransform.md)

# latinToCyrillic

<sub>Type Property</sub>

A constant containing the transliteration of a string from Latin script to Cyrillic script.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let latinToCyrillic: StringTransform
```

## Discussion

This transformation is reversible.

For example, the string “kirillica” transliterates to “кириллица”.

This is equivalent to [kCFStringTransformLatinCyrillic](../../corefoundation/kcfstringtransformlatincyrillic.md).

## See Also

### Constants

- [NSStringTransformLatinToKatakana](latintokatakana.md) — A constant containing the transliteration of a string from Latin script to Katakana script.
- [NSStringTransformLatinToHiragana](latintohiragana.md) — A constant containing the transliteration of a string from Latin script to Hiragana script.
- [NSStringTransformLatinToHangul](latintohangul.md) — A constant containing the transliteration of a string from Latin script to Hangul script.
- [NSStringTransformLatinToArabic](latintoarabic.md) — A constant containing the transliteration of a string from Latin script to Arabic script.
- [NSStringTransformLatinToHebrew](latintohebrew.md) — A constant containing the transliteration of a string from Latin script to Hebrew script.
- [NSStringTransformLatinToThai](latintothai.md) — A constant containing the transliteration of a string from Latin script to Thai script.
- [NSStringTransformToLatin](tolatin.md) — A constant containing the transliteration of a string from any script to Latin script.
- [NSStringTransformMandarinToLatin](mandarintolatin.md) — A constant containing the transliteration of a string from Han script to Latin.
- [NSStringTransformHiraganaToKatakana](hiraganatokatakana.md) — A constant containing the transliteration of a string from Hiragana script to Katakana script.
- [NSStringTransformFullwidthToHalfwidth](fullwidthtohalfwidth.md) — A constant containing the transformation of a string from full-width CJK characters to half-width forms.
- [NSStringTransformToXMLHex](toxmlhex.md) — A constant containing the transformation of a string from characters to XML hexadecimal escape codes.
- [NSStringTransformToUnicodeName](tounicodename.md) — An identifier for a transform that converts characters to Unicode names.
- [NSStringTransformStripCombiningMarks](stripcombiningmarks.md) — A constant containing the transformation of a string by removing combining marks.
- [NSStringTransformStripDiacritics](stripdiacritics.md) — A constant containing the transformation of a string by removing diacritics.
