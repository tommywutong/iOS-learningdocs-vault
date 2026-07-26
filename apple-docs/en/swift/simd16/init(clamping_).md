---
title: 'init(clamping:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/simd16/init(clamping:)'
source_url: 'https://developer.apple.com/documentation/swift/simd16/init(clamping:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd16/init%28clamping%3A%29.json'
content_hash: 'sha256:16b7ac616eb7fd2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD16](../simd16.md)

# init(clamping:)

<sub>Initializer</sub>

Creates a new vector from the given vector, clamping the values of the given vector’s elements if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Other>(clamping other: SIMD16<Other>) where Other : FixedWidthInteger, Other : SIMDScalar
```

## Parameters

- `other` — The vector to convert.
