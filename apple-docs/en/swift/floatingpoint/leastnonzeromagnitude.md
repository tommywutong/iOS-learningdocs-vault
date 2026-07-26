---
title: leastNonzeroMagnitude
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/floatingpoint/leastnonzeromagnitude
source_url: 'https://developer.apple.com/documentation/swift/floatingpoint/leastnonzeromagnitude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/floatingpoint/leastnonzeromagnitude.json'
content_hash: 'sha256:afba5dc558fe1a65'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [FloatingPoint](../floatingpoint.md)

# leastNonzeroMagnitude

<sub>Type Property</sub>

The least positive number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var leastNonzeroMagnitude: Self { get }
```

## Discussion

This value compares less than or equal to all positive numbers, but greater than zero. If the type supports subnormal values, `leastNonzeroMagnitude` is smaller than `leastNormalMagnitude`; otherwise they are equal.
