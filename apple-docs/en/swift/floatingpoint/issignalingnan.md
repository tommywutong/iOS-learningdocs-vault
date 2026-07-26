---
title: isSignalingNaN
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/issignalingnan
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/issignalingnan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/issignalingnan.json'
content_hash: 'sha256:a50753cbe726ff06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# isSignalingNaN

<sub>Instance Property</sub>

A Boolean value indicating whether the instance is a signaling NaN.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSignalingNaN: Bool { get }
```

## Discussion

Signaling NaNs typically raise the Invalid flag when used in general computing operations.
