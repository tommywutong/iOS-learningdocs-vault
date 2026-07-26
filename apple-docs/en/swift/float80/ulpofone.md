---
title: ulpOfOne
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/ulpofone
source_url: 'https://developer.apple.com/documentation/swift/float80/ulpofone'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/ulpofone.json'
content_hash: 'sha256:ec2443070c74bb3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# ulpOfOne

<sub>Type Property</sub>

The unit in the last place of 1.0.

<sub>macOS</sub>

```swift
static var ulpOfOne: Float80 { get }
```

## Discussion

The positive difference between 1.0 and the next greater representable number. The `ulpOfOne` constant corresponds to the C macros `FLT_EPSILON`, `DBL_EPSILON`, and others with a similar purpose.
