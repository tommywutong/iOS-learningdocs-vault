---
title: kCTTypesetterOptionForcedEmbeddingLevel
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kcttypesetteroptionforcedembeddinglevel
source_url: 'https://developer.apple.com/documentation/coretext/kcttypesetteroptionforcedembeddinglevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kcttypesetteroptionforcedembeddinglevel.json'
content_hash: 'sha256:692f8b698b1a33f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTTypesetterOptionForcedEmbeddingLevel

<sub>Global Variable</sub>

A key that specifies the embedding level of the typesetter’s text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTTypesetterOptionForcedEmbeddingLevel: CFString
```

## Discussion

The value for this key must be a `CFNumberRef` object. There’s no default value.

Normally, typesetting applies the Unicode Bidirectional Algorithm as described in [Unicode Standard Annex #9](https://unicode.org/reports/tr9/). If present, this option specifies the embedding level, and the text system ignores any directional control characters.

## See Also

### Constants

- [kCTTypesetterOptionAllowUnboundedLayout](kcttypesetteroptionallowunboundedlayout.md) — A key that specifies whether the text system lays out text that requires unreasonable effort.
- [kCTTypesetterOptionDisableBidiProcessing](kcttypesetteroptiondisablebidiprocessing.md) _(deprecated)_
