---
title: isSignalingNaN
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/issignalingnan
source_url: 'https://developer.apple.com/documentation/swift/float80/issignalingnan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/issignalingnan.json'
content_hash: 'sha256:66d72a0f5c06bc92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isSignalingNaN

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is a signaling NaN.

<sub>macOS</sub>

```swift
var isSignalingNaN: Bool { get }
```

## Discussion

Signaling NaNs typically raise the Invalid flag when used in general computing operations.
