---
title: isSubnormal
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/issubnormal
source_url: 'https://developer.apple.com/documentation/swift/float80/issubnormal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/issubnormal.json'
content_hash: 'sha256:f183b29f75a86aeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isSubnormal

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is subnormal.

<sub>macOS</sub>

```swift
var isSubnormal: Bool { get }
```

## Discussion

A _subnormal_ value is a nonzero number that has a lesser magnitude than the smallest normal number. Subnormal values don’t use the full precision available to values of a type.

Zero is neither a normal nor a subnormal number. Subnormal numbers are often called _denormal_ or _denormalized_—these are different names for the same concept.
