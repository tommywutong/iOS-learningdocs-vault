---
title: description
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/description
source_url: 'https://developer.apple.com/documentation/swift/float16/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/description.json'
content_hash: 'sha256:c7c7098bd17f09ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# description

<sub>Instance Property</sub>

A textual representation of the value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## Discussion

For any finite value, this property provides a string that can be converted back to an instance of `Float16` without rounding errors.  That is, if `x` is an instance of `Float16`, then `Float16(x.description) == x` is always true.  For any NaN value, the property’s value is “nan”, and for positive and negative infinity its value is “inf” and “-inf”.
