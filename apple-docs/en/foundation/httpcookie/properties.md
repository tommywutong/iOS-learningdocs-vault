---
title: properties
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/properties
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/properties.json'
content_hash: 'sha256:ef2a39c33d277ab5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# properties

<sub>Instance Property</sub>

The cookie’s properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var properties: [HTTPCookiePropertyKey : Any]? { get }
```

## Discussion

This dictionary can be used with [- initWithProperties:](<init(properties_).md>) (or [cookieWithProperties:](../nshttpcookie/cookiewithproperties_.md) in Objective-C) to create an equivalent [HTTPCookie](../httpcookie.md) object.

See [- initWithProperties:](<init(properties_).md>) for more information on the constraints imposed on the `properties` dictionary.

## See Also

### Accessing cookie properties as key-value pairs

- [HTTPCookiePropertyKey](../httpcookiepropertykey.md) — Constants that define the supported keys in a cookie attributes dictionary.
