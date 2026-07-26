---
title: regionCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslocale/regioncode
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/regioncode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/regioncode.json'
content_hash: 'sha256:1f3efd0a2207c71e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# regionCode

<sub>Instance Property</sub>

Returns the region code of the locale. If the `rg` subtag is present, the value of the subtag will be used. For example,  returns “GB” for “en_US@rg=gbzzzz” locale. If the `localeIdentifier` doesn’t contain a region, returns `nil`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var regionCode: String? { get }
```
