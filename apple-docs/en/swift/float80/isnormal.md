---
title: isNormal
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/isnormal
source_url: 'https://developer.apple.com/documentation/swift/float80/isnormal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/isnormal.json'
content_hash: 'sha256:0acee2a9897993b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isNormal

<sub>Instance Property</sub>

A Boolean value indicating whether this instance is normal.

<sub>macOS</sub>

```swift
var isNormal: Bool { get }
```

## Discussion

A _normal_ value is a finite number that uses the full precision available to values of a type. Zero is neither a normal nor a subnormal number.
