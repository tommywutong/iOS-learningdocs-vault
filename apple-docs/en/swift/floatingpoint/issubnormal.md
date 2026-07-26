---
title: isSubnormal
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/issubnormal
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/issubnormal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/issubnormal.json'
content_hash: 'sha256:0e6190e66e6a12e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# isSubnormal

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is subnormal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSubnormal: Bool { get }
```

## Discussion

A _subnormal_ value is a nonzero number that has a lesser magnitude than the smallest normal number. Subnormal values don’t use the full precision available to values of a type.

Zero is neither a normal nor a subnormal number. Subnormal numbers are often called _denormal_ or _denormalized_—these are different names for the same concept.
