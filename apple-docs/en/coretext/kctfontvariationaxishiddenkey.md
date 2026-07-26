---
title: kCTFontVariationAxisHiddenKey
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctfontvariationaxishiddenkey
source_url: 'https://developer.apple.com/documentation/coretext/kctfontvariationaxishiddenkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctfontvariationaxishiddenkey.json'
content_hash: 'sha256:122a90b1ac8eb78d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFontVariationAxisHiddenKey

<sub>Global Variable</sub>

The key to find out if the axis is hidden.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFontVariationAxisHiddenKey: CFString
```

## Discussion

This key contains a [CFBoolean](../corefoundation/cfboolean.md) value that is [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md) when the font designer recommends the axis not be exposed directly to end users in application interfaces.

Reasons for setting this flag might include that the axis is intended only for programmatic interaction, or is intended for font-internal use by the font developer.

## See Also

### Constants

- [kCTFontVariationAxisIdentifierKey](kctfontvariationaxisidentifierkey.md) — Key to get the variation axis identifier.
- [kCTFontVariationAxisMinimumValueKey](kctfontvariationaxisminimumvaluekey.md) — Key to get the variation axis minimum value.
- [kCTFontVariationAxisMaximumValueKey](kctfontvariationaxismaximumvaluekey.md) — Key to get the variation axis maximum value.
- [kCTFontVariationAxisDefaultValueKey](kctfontvariationaxisdefaultvaluekey.md) — Key to get the variation axis default value.
- [kCTFontVariationAxisNameKey](kctfontvariationaxisnamekey.md) — Key to get the localized variation axis name string.
