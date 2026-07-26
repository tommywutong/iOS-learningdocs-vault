---
title: isSubnormal
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/issubnormal
source_url: 'https://developer.apple.com/documentation/swift/float16/issubnormal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/issubnormal.json'
content_hash: 'sha256:b76ce97d08e468ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

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
