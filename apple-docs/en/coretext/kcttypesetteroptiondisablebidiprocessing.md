---
title: kCTTypesetterOptionDisableBidiProcessing
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+（6.0 起废弃）, iPadOS 3.2+（6.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coretext/kcttypesetteroptiondisablebidiprocessing
source_url: 'https://developer.apple.com/documentation/coretext/kcttypesetteroptiondisablebidiprocessing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kcttypesetteroptiondisablebidiprocessing.json'
content_hash: 'sha256:ce1570ee9f510bff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTTypesetterOptionDisableBidiProcessing

<sub>Global Variable</sub>

> [!warning] Deprecated
> Deprecated

<sub>tvOS, visionOS, watchOS</sub>

```swift
let kCTTypesetterOptionDisableBidiProcessing: CFString
```

## Discussion

Disables bidirectional processing. Value must be a CFBoolean object. Default value is `false`. Normally, typesetting applies the Unicode Bidirectional Algorithm as described in Unicode Standard Annex #9. If a typesetter is created with this option set to `true`, no directional reordering is performed, and any directional control characters are ignored.

## See Also

### Constants

- [kCTTypesetterOptionForcedEmbeddingLevel](kcttypesetteroptionforcedembeddinglevel.md) — A key that specifies the embedding level of the typesetter’s text.
- [kCTTypesetterOptionAllowUnboundedLayout](kcttypesetteroptionallowunboundedlayout.md) — A key that specifies whether the text system lays out text that requires unreasonable effort.
