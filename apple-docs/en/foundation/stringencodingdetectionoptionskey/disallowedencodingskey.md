---
title: disallowedEncodingsKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringencodingdetectionoptionskey/disallowedencodingskey
source_url: 'https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/disallowedencodingskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringencodingdetectionoptionskey/disallowedencodingskey.json'
content_hash: 'sha256:5526c9fbef641998'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)

# disallowedEncodingsKey

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let disallowedEncodingsKey: StringEncodingDetectionOptionsKey
```

## Discussion

Option specifying any string encodings not to be considered. The corresponding value for this key is an `NSArray` of `NSNumber` objects that contain `NSStringEncoding` values. If this option is unspecified, no additional string encodings are removed from consideration.

## See Also

### Type Properties

- [NSStringEncodingDetectionAllowLossyKey](allowlossykey.md)
- [NSStringEncodingDetectionFromWindowsKey](fromwindowskey.md)
- [NSStringEncodingDetectionLikelyLanguageKey](likelylanguagekey.md)
- [NSStringEncodingDetectionLossySubstitutionKey](lossysubstitutionkey.md)
- [NSStringEncodingDetectionSuggestedEncodingsKey](suggestedencodingskey.md)
- [NSStringEncodingDetectionUseOnlySuggestedEncodingsKey](useonlysuggestedencodingskey.md)
