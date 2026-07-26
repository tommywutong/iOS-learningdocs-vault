---
title: isSignalingNaN
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/issignalingnan
source_url: 'https://developer.apple.com/documentation/swift/float16/issignalingnan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/issignalingnan.json'
content_hash: 'sha256:0bb60a47f4365497'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# isSignalingNaN

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is a signaling NaN.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSignalingNaN: Bool { get }
```

## Discussion

Signaling NaNs typically raise the Invalid flag when used in general computing operations.
