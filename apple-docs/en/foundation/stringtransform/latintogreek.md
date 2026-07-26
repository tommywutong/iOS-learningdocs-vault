---
title: latinToGreek
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringtransform/latintogreek
source_url: 'https://developer.apple.com/documentation/foundation/stringtransform/latintogreek'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringtransform/latintogreek.json'
content_hash: 'sha256:abca81c888d674d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StringTransform](../stringtransform.md)

# latinToGreek

<sub>Type Property</sub>

A constant containing the transliteration of a string from Latin script to Greek script.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let latinToGreek: StringTransform
```

## Discussion

This transformation is reversible.

For example, the string “Ellēnikó alphábēto‎” transliterates to “Ελληνικό αλφάβητο”.

This is equivalent to [kCFStringTransformLatinGreek](../../corefoundation/kcfstringtransformlatingreek.md).

## See Also

### Transliteration

- [NSStringTransformToLatin](tolatin.md) — A constant containing the transliteration of a string from any script to Latin script.
- [NSStringTransformLatinToArabic](latintoarabic.md) — A constant containing the transliteration of a string from Latin script to Arabic script.
- [NSStringTransformLatinToCyrillic](latintocyrillic.md) — A constant containing the transliteration of a string from Latin script to Cyrillic script.
- [NSStringTransformLatinToHangul](latintohangul.md) — A constant containing the transliteration of a string from Latin script to Hangul script.
- [NSStringTransformLatinToHebrew](latintohebrew.md) — A constant containing the transliteration of a string from Latin script to Hebrew script.
- [NSStringTransformLatinToHiragana](latintohiragana.md) — A constant containing the transliteration of a string from Latin script to Hiragana script.
- [NSStringTransformLatinToKatakana](latintokatakana.md) — A constant containing the transliteration of a string from Latin script to Katakana script.
- [NSStringTransformLatinToThai](latintothai.md) — A constant containing the transliteration of a string from Latin script to Thai script.
- [NSStringTransformHiraganaToKatakana](hiraganatokatakana.md) — A constant containing the transliteration of a string from Hiragana script to Katakana script.
- [NSStringTransformMandarinToLatin](mandarintolatin.md) — A constant containing the transliteration of a string from Han script to Latin.
