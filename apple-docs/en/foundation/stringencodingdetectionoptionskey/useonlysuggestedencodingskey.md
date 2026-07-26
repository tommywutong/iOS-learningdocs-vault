---
title: useOnlySuggestedEncodingsKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringencodingdetectionoptionskey/useonlysuggestedencodingskey
source_url: 'https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/useonlysuggestedencodingskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringencodingdetectionoptionskey/useonlysuggestedencodingskey.json'
content_hash: 'sha256:dd16d836880623be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)

# useOnlySuggestedEncodingsKey

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let useOnlySuggestedEncodingsKey: StringEncodingDetectionOptionsKey
```

## Discussion

Option specifying whether to only consider suggested string encodings. Use this only if you specify a value for `NSStringEncodingDetectionSuggestedEncodingsKey`. The corresponding value for this key is an `NSNumber` object containing a Boolean value. By default, this value is `@(NO)`.

## See Also

### Type Properties

- [NSStringEncodingDetectionAllowLossyKey](allowlossykey.md)
- [NSStringEncodingDetectionDisallowedEncodingsKey](disallowedencodingskey.md)
- [NSStringEncodingDetectionFromWindowsKey](fromwindowskey.md)
- [NSStringEncodingDetectionLikelyLanguageKey](likelylanguagekey.md)
- [NSStringEncodingDetectionLossySubstitutionKey](lossysubstitutionkey.md)
- [NSStringEncodingDetectionSuggestedEncodingsKey](suggestedencodingskey.md)
