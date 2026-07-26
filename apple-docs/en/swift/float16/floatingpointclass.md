---
title: floatingPointClass
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/floatingpointclass
source_url: 'https://developer.apple.com/documentation/swift/float16/floatingpointclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/floatingpointclass.json'
content_hash: 'sha256:1929a40040587cfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# floatingPointClass

<sub>Instance Property</sub>

The classification of this value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var floatingPointClass: FloatingPointClassification { get }
```

## Discussion

A value’s `floatingPointClass` property describes its “class” as described by the [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933).
