---
title: isNormal
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/isnormal
source_url: 'https://developer.apple.com/documentation/swift/float16/isnormal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/isnormal.json'
content_hash: 'sha256:e567a71720b14861'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# isNormal

<sub>Instance Property</sub>

A Boolean value indicating whether this instance is normal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isNormal: Bool { get }
```

## Discussion

A _normal_ value is a finite number that uses the full precision available to values of a type. Zero is neither a normal nor a subnormal number.
