---
title: kCTFontWidthTrait
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontwidthtrait
source_url: 'https://developer.apple.com/documentation/coretext/kctfontwidthtrait'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontwidthtrait.json'
content_hash: 'sha256:ef8b01e78539480f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontWidthTrait

<sub>Global Variable</sub>

The normalized proportion (width condense or expand) trait from the font traits dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontWidthTrait: CFString
```

## Discussion

This value corresponds to the relative interglyph spacing for a given font. The value returned is a [CFNumber](../corefoundation/cfnumber.md) object representing a float between `-1.0` and `1.0`. The value of `0.0` corresponds to regular glyph spacing, and negative values represent condensed glyph spacing.

## See Also

### Font Trait Keys

- [kCTFontSymbolicTrait](kctfontsymbolictrait.md) — The symbolic traits value from the font traits dictionary.
- [kCTFontWeightTrait](kctfontweighttrait.md) — The normalized weight trait from the font traits dictionary.
- [kCTFontSlantTrait](kctfontslanttrait.md) — The normalized slant angle from the font traits dictionary.
