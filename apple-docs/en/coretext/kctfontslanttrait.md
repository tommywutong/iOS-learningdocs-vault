---
title: kCTFontSlantTrait
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontslanttrait
source_url: 'https://developer.apple.com/documentation/coretext/kctfontslanttrait'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontslanttrait.json'
content_hash: 'sha256:7eb37e6fb65b1a45'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontSlantTrait

<sub>Global Variable</sub>

The normalized slant angle from the font traits dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontSlantTrait: CFString
```

## Discussion

The value returned is a [CFNumber](../corefoundation/cfnumber.md) object representing a float value between `-1.0` and `1.0` for normalized slant angle. The value of `0.0` corresponds to 0 degrees clockwise rotation from the vertical and `1.0` corresponds to 30 degrees clockwise rotation.

## See Also

### Font Trait Keys

- [kCTFontSymbolicTrait](kctfontsymbolictrait.md) — The symbolic traits value from the font traits dictionary.
- [kCTFontWeightTrait](kctfontweighttrait.md) — The normalized weight trait from the font traits dictionary.
- [kCTFontWidthTrait](kctfontwidthtrait.md) — The normalized proportion (width condense or expand) trait from the font traits dictionary.
