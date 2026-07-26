---
title: jsonRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/jsonrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/product/jsonrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/jsonrepresentation.json'
content_hash: 'sha256:414ec0989d1da5ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Product](../product.md)

# jsonRepresentation

<sub>Instance Property</sub>

The JSON representation of the product information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var jsonRepresentation: Data { get }
```

## Discussion

The [jsonRepresentation](jsonrepresentation.md) is UTF-8 string data. You can use the JSON data to decode the product information into your own data type instead of using the [Product](../product.md) value directly.
