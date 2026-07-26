---
title: StringTransform
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringtransform
source_url: 'https://developer.apple.com/documentation/foundation/stringtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringtransform.json'
content_hash: 'sha256:5a3e6b81a767d80d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# StringTransform

<sub>Structure</sub>

Constants representing an ICU string transform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StringTransform
```

## Discussion

These constants are used by the [NSString](nsstring.md) method [- stringByApplyingTransform:reverse:](<nsstring/applyingtransform(__reverse_).md>).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Transliteration

- [NSStringTransformToLatin](stringtransform/tolatin.md) — A constant containing the transliteration of a string from any script to Latin script.
- [NSStringTransformLatinToArabic](stringtransform/latintoarabic.md) — A constant containing the transliteration of a string from Latin script to Arabic script.
- [NSStringTransformLatinToCyrillic](stringtransform/latintocyrillic.md) — A constant containing the transliteration of a string from Latin script to Cyrillic script.
- [NSStringTransformLatinToGreek](stringtransform/latintogreek.md) — A constant containing the transliteration of a string from Latin script to Greek script.
- [NSStringTransformLatinToHangul](stringtransform/latintohangul.md) — A constant containing the transliteration of a string from Latin script to Hangul script.
- [NSStringTransformLatinToHebrew](stringtransform/latintohebrew.md) — A constant containing the transliteration of a string from Latin script to Hebrew script.
- [NSStringTransformLatinToHiragana](stringtransform/latintohiragana.md) — A constant containing the transliteration of a string from Latin script to Hiragana script.
- [NSStringTransformLatinToKatakana](stringtransform/latintokatakana.md) — A constant containing the transliteration of a string from Latin script to Katakana script.
- [NSStringTransformLatinToThai](stringtransform/latintothai.md) — A constant containing the transliteration of a string from Latin script to Thai script.
- [NSStringTransformHiraganaToKatakana](stringtransform/hiraganatokatakana.md) — A constant containing the transliteration of a string from Hiragana script to Katakana script.
- [NSStringTransformMandarinToLatin](stringtransform/mandarintolatin.md) — A constant containing the transliteration of a string from Han script to Latin.

### Diacritic and Combining Mark Removal

- [NSStringTransformStripDiacritics](stringtransform/stripdiacritics.md) — A constant containing the transformation of a string by removing diacritics.
- [NSStringTransformStripCombiningMarks](stringtransform/stripcombiningmarks.md) — A constant containing the transformation of a string by removing combining marks.

### Halfwidth and Fullwidth Form Conversion

- [NSStringTransformFullwidthToHalfwidth](stringtransform/fullwidthtohalfwidth.md) — A constant containing the transformation of a string from full-width CJK characters to half-width forms.

### Character Representation

- [NSStringTransformToUnicodeName](stringtransform/tounicodename.md) — An identifier for a transform that converts characters to Unicode names.
- [NSStringTransformToXMLHex](stringtransform/toxmlhex.md) — A constant containing the transformation of a string from characters to XML hexadecimal escape codes.

### Initializers

- [init(_:)](<stringtransform/init(__).md>)
- [init(rawValue:)](<stringtransform/init(rawvalue_).md>)

## See Also

### Transforming Strings

- [- stringByApplyingTransform:reverse:](<nsstring/applyingtransform(__reverse_).md>) — Returns a new string by applying a specified transform to the string.
