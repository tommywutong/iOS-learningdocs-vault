---
title: lossySubstitutionKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringencodingdetectionoptionskey/lossysubstitutionkey
source_url: 'https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/lossysubstitutionkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringencodingdetectionoptionskey/lossysubstitutionkey.json'
content_hash: 'sha256:272b58928eb2d1ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)

# lossySubstitutionKey

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let lossySubstitutionKey: StringEncodingDetectionOptionsKey
```

## Discussion

Option specifying the string used to substitute for any unsupported characters when converting to a lossy string encoding. If a `@(NO)` value is specified for `NSStringEncodingDetectionAllowLossyKey`, this option has no effect. The corresponding value for this key is an `NSString` object. By default, this value is `U+FFFD`.

## See Also

### Type Properties

- [NSStringEncodingDetectionAllowLossyKey](allowlossykey.md)
- [NSStringEncodingDetectionDisallowedEncodingsKey](disallowedencodingskey.md)
- [NSStringEncodingDetectionFromWindowsKey](fromwindowskey.md)
- [NSStringEncodingDetectionLikelyLanguageKey](likelylanguagekey.md)
- [NSStringEncodingDetectionSuggestedEncodingsKey](suggestedencodingskey.md)
- [NSStringEncodingDetectionUseOnlySuggestedEncodingsKey](useonlysuggestedencodingskey.md)
