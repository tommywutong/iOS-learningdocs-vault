---
title: kCTFontWeightTrait
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontweighttrait
source_url: 'https://developer.apple.com/documentation/coretext/kctfontweighttrait'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontweighttrait.json'
content_hash: 'sha256:274e99d010cd0e59'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontWeightTrait

<sub>Global Variable</sub>

The normalized weight trait from the font traits dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontWeightTrait: CFString
```

## Discussion

The value returned is a [CFNumber](../corefoundation/cfnumber.md) representing a float value between `-1.0` and `1.0` for normalized weight. The value of `0.0` corresponds to the regular or medium font weight.

## See Also

### Font Trait Keys

- [kCTFontSymbolicTrait](kctfontsymbolictrait.md) — The symbolic traits value from the font traits dictionary.
- [kCTFontWidthTrait](kctfontwidthtrait.md) — The normalized proportion (width condense or expand) trait from the font traits dictionary.
- [kCTFontSlantTrait](kctfontslanttrait.md) — The normalized slant angle from the font traits dictionary.
