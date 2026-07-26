---
title: likelyLanguageKey
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringencodingdetectionoptionskey/likelylanguagekey
source_url: 'https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey/likelylanguagekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringencodingdetectionoptionskey/likelylanguagekey.json'
content_hash: 'sha256:97bc4e568dd430a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)

# likelyLanguageKey

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let likelyLanguageKey: StringEncodingDetectionOptionsKey
```

## Discussion

Option specifying the likely two-letter ISO 639-1 language code for the converted string. Use this when you have prior knowledge about the expected language of the converted string. The corresponding value for this key is an `NSString` object. If no value is specified, the language of the converted string is not considered.

## See Also

### Type Properties

- [NSStringEncodingDetectionAllowLossyKey](allowlossykey.md)
- [NSStringEncodingDetectionDisallowedEncodingsKey](disallowedencodingskey.md)
- [NSStringEncodingDetectionFromWindowsKey](fromwindowskey.md)
- [NSStringEncodingDetectionLossySubstitutionKey](lossysubstitutionkey.md)
- [NSStringEncodingDetectionSuggestedEncodingsKey](suggestedencodingskey.md)
- [NSStringEncodingDetectionUseOnlySuggestedEncodingsKey](useonlysuggestedencodingskey.md)
