---
title: leastNonzeroMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/leastnonzeromagnitude
source_url: 'https://developer.apple.com/documentation/swift/float80/leastnonzeromagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/leastnonzeromagnitude.json'
content_hash: 'sha256:4bf2cb303740abae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# leastNonzeroMagnitude

<sub>Type Property</sub>

The least positive number.

<sub>macOS</sub>

```swift
static var leastNonzeroMagnitude: Float80 { get }
```

## Discussion

This value compares less than or equal to all positive numbers, but greater than zero. If the type supports subnormal values, `leastNonzeroMagnitude` is smaller than `leastNormalMagnitude`; otherwise they are equal.
