---
title: allowLossyKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringencodingdetectionoptionskey/allowlossykey
source_url: 'https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/allowlossykey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringencodingdetectionoptionskey/allowlossykey.json'
content_hash: 'sha256:d789b868ca5f99c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)

# allowLossyKey

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let allowLossyKey: StringEncodingDetectionOptionsKey
```

## Discussion

Option specifying whether to allow lossy string conversion. The corresponding value for this key is an `NSNumber` object containing a Boolean value. If `@(NO)`, the a lossy string encoding may not be chosen. By default, this value is `@(YES)`.

## See Also

### Type Properties

- [NSStringEncodingDetectionDisallowedEncodingsKey](disallowedencodingskey.md)
- [NSStringEncodingDetectionFromWindowsKey](fromwindowskey.md)
- [NSStringEncodingDetectionLikelyLanguageKey](likelylanguagekey.md)
- [NSStringEncodingDetectionLossySubstitutionKey](lossysubstitutionkey.md)
- [NSStringEncodingDetectionSuggestedEncodingsKey](suggestedencodingskey.md)
- [NSStringEncodingDetectionUseOnlySuggestedEncodingsKey](useonlysuggestedencodingskey.md)
