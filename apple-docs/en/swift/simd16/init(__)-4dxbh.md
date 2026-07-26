---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd16/init(_:)-4dxbh'
source_url: 'https://developer.apple.com/documentation/swift/simd16/init(_:)-4dxbh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd16/init%28_%3A%29-4dxbh.json'
content_hash: 'sha256:570e6618ff64ef6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD16](../simd16.md)

# init(_:)

<sub>Initializer</sub>

Creates a new vector from the given vector of integers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Other>(_ other: SIMD16<Other>) where Other : FixedWidthInteger, Other : SIMDScalar
```

## Parameters

- `other` — The vector to convert.
