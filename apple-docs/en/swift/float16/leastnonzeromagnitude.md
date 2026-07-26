---
title: leastNonzeroMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float16/leastnonzeromagnitude
source_url: 'https://developer.apple.com/documentation/swift/float16/leastnonzeromagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float16/leastnonzeromagnitude.json'
content_hash: 'sha256:a3dbe3fd41234ed0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float16](../float16.md)

# leastNonzeroMagnitude

<sub>Type Property</sub>

The least positive number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var leastNonzeroMagnitude: Float16 { get }
```

## Discussion

This value compares less than or equal to all positive numbers, but greater than zero. If the type supports subnormal values, `leastNonzeroMagnitude` is smaller than `leastNormalMagnitude`; otherwise they are equal.
