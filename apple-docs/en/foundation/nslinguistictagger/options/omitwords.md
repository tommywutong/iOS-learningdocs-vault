---
title: omitWords
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslinguistictagger/options/omitwords
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/options/omitwords'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/options/omitwords.json'
content_hash: 'sha256:6c12193c6535c0b9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSLinguisticTagger](../../nslinguistictagger.md) · [Options](../options.md)

# omitWords

<sub>Type Property</sub>

Omit tokens of type [NSLinguisticTagWord](../../nslinguistictag/word.md) (items considered to be words).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var omitWords: NSLinguisticTagger.Options { get }
```

## See Also

### Constants

- [NSLinguisticTaggerOmitPunctuation](omitpunctuation.md) — Omit tokens of type [NSLinguisticTagPunctuation](../../nslinguistictag/punctuation.md) (all punctuation).
- [NSLinguisticTaggerOmitWhitespace](omitwhitespace.md) — Omit tokens of type [NSLinguisticTagWhitespace](../../nslinguistictag/whitespace.md) (whitespace of all sorts).
- [NSLinguisticTaggerOmitOther](omitother.md) — Omit tokens of type [NSLinguisticTagOther](../../nslinguistictag/other.md) (non-linguistic items, such as symbols).
- [NSLinguisticTaggerJoinNames](joinnames.md) — Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.  If this option is set, then multiple-word names will be joined together and returned as a single token.
