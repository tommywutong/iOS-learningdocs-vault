---
title: unicodeScalar
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/staticstring/unicodescalar
source_url: 'https://developer.apple.com/documentation/swift/staticstring/unicodescalar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticstring/unicodescalar.json'
content_hash: 'sha256:f90bcff2d5ae62cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticString](../staticstring.md)

# unicodeScalar

<sub>Instance Property</sub>

A single Unicode scalar value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var unicodeScalar: Unicode.Scalar { get }
```

## Discussion

> [!important] Important
> Accessing this property when `hasPointerRepresentation` is `true` triggers a runtime error.
