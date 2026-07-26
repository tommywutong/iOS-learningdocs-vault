---
title: kCFStringTransformToUnicodeName
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfstringtransformtounicodename
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfstringtransformtounicodename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfstringtransformtounicodename.json'
content_hash: 'sha256:10eb9c90047797d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFStringTransformToUnicodeName

<sub>Global Variable</sub>

The identifier of a reversible transform to transliterate characters other than printable ASCII to their Unicode character name in braces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFStringTransformToUnicodeName: CFString!
```

## Discussion

Examples include `"\N{AIRPLANE}"` for “✈” and `"\N{GREEK CAPITAL LETTER PSI}"` for “Ψ”.

> [!note] Note
> The result of a forward transformation delimits each Unicode name with enclosing curly braces and the leading character sequence `"\N"`. In some programming languages, `"\N{...}"` is used as an escape sequence for Unicode characters in strings and regular expressions; this isn’t supported in Swift or Objective-C. To perform the reverse transform of a string literal in Swift or Objective-C, escape the leading backslash (`"\\N{...}"`) for each Unicode name.

## See Also

### Constants

- [kCFStringTransformStripCombiningMarks](kcfstringtransformstripcombiningmarks.md) — The identifier of a transform to strip combining marks (accents or diacritics).
- [kCFStringTransformToLatin](kcfstringtransformtolatin.md) — The identifier of a transform to transliterate all text possible to Latin script. Ideographs are transliterated as Mandarin Chinese.
- [kCFStringTransformFullwidthHalfwidth](kcfstringtransformfullwidthhalfwidth.md) — The identifier of a reversible transform to convert full-width characters to their half-width equivalents.
- [kCFStringTransformLatinKatakana](kcfstringtransformlatinkatakana.md) — The identifier of a reversible transform to transliterate text to Katakana from Latin.
- [kCFStringTransformLatinHiragana](kcfstringtransformlatinhiragana.md) — The identifier of a reversible transform to transliterate text to Hiragana from Latin.
- [kCFStringTransformHiraganaKatakana](kcfstringtransformhiraganakatakana.md) — The identifier of a reversible transform to transliterate text to Katakana from Hiragana.
- [kCFStringTransformMandarinLatin](kcfstringtransformmandarinlatin.md) — The identifier of a transform to transliterate text to Latin from ideographs interpreted as Mandarin Chinese. This transform is not reversible.
- [kCFStringTransformLatinHangul](kcfstringtransformlatinhangul.md) — The identifier of a reversible transform to transliterate text to Hangul from Latin.
- [kCFStringTransformLatinArabic](kcfstringtransformlatinarabic.md) — The identifier of a reversible transform to transliterate text to Arabic from Latin.
- [kCFStringTransformLatinHebrew](kcfstringtransformlatinhebrew.md) — The identifier of a reversible transform to transliterate text to Hebrew from Latin.
- [kCFStringTransformLatinThai](kcfstringtransformlatinthai.md) — The identifier of a reversible transform to transliterate text to Thai from Latin.
- [kCFStringTransformLatinCyrillic](kcfstringtransformlatincyrillic.md) — The identifier of a reversible transform to transliterate text to Cyrillic from Latin.
- [kCFStringTransformLatinGreek](kcfstringtransformlatingreek.md) — The identifier of a reversible transform to transliterate text to Greek from Latin.
- [kCFStringTransformToXMLHex](kcfstringtransformtoxmlhex.md) — The identifier of a reversible transform to transliterate characters other than printable ASCII to XML/HTML numeric entities.
- [kCFStringTransformStripDiacritics](kcfstringtransformstripdiacritics.md) — The identifier of a transform to remove diacritic markings.
