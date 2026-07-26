---
title: suggestedEncodingsKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringencodingdetectionoptionskey/suggestedencodingskey
source_url: 'https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/suggestedencodingskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringencodingdetectionoptionskey/suggestedencodingskey.json'
content_hash: 'sha256:7b78059190282ee5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)

# suggestedEncodingsKey

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let suggestedEncodingsKey: StringEncodingDetectionOptionsKey
```

## Discussion

Option specifying any suggested string encodings. Use this when you have prior knowledge about the likely or expected encoding. The corresponding value for this key is an `NSArray` of `NSNumber` objects that contain `NSStringEncoding` values. If this option is unspecified, all allowed encodings are evaluated with equal consideration.

## See Also

### Type Properties

- [NSStringEncodingDetectionAllowLossyKey](allowlossykey.md)
- [NSStringEncodingDetectionDisallowedEncodingsKey](disallowedencodingskey.md)
- [NSStringEncodingDetectionFromWindowsKey](fromwindowskey.md)
- [NSStringEncodingDetectionLikelyLanguageKey](likelylanguagekey.md)
- [NSStringEncodingDetectionLossySubstitutionKey](lossysubstitutionkey.md)
- [NSStringEncodingDetectionUseOnlySuggestedEncodingsKey](useonlysuggestedencodingskey.md)
