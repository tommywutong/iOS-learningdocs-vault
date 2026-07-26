---
title: Transform Identifiers for CFStringTransform
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/transform-identifiers-for-cfstringtransform
source_url: 'https://developer.apple.com/documentation/corefoundation/transform-identifiers-for-cfstringtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/transform-identifiers-for-cfstringtransform.json'
content_hash: 'sha256:dbab642811fb3d49'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFMutableString](cfmutablestring.md)

# Transform Identifiers for CFStringTransform

<sub>API Collection</sub>

Constants that identify transforms used with [CFStringTransform](<cfstringtransform(________).md>).

## Overview

In macOS 10.4 and later, with [CFStringTransform](<cfstringtransform(________).md>) you can also use any valid ICU transform ID defined in the [ICU User Guide for Transforms](https://unicode-org.github.io/icu/userguide/transforms/general/).

## Topics

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
- [kCFStringTransformToUnicodeName](kcfstringtransformtounicodename.md) — The identifier of a reversible transform to transliterate characters other than printable ASCII to their Unicode character name in braces.
- [kCFStringTransformStripDiacritics](kcfstringtransformstripdiacritics.md) — The identifier of a transform to remove diacritic markings.

## See Also

### Constants

- [CFStringNormalizationForm](cfstringnormalizationform.md) — Unicode normalization forms as described in Unicode Technical Report #15.
