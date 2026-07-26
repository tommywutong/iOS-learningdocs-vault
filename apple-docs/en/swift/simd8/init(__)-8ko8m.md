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
doc_path: '/documentation/swift/simd8/init(_:)-8ko8m'
source_url: 'https://developer.apple.com/documentation/swift/simd8/init(_:)-8ko8m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/simd8/init%28_%3A%29-8ko8m.json'
content_hash: 'sha256:aa440a6e40b2e766'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SIMD8](../simd8.md)

# init(_:)

<sub>Initializer</sub>

Creates a new vector from the given vector of integers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Other>(_ other: SIMD8<Other>) where Other : FixedWidthInteger, Other : SIMDScalar
```

## Parameters

- `other` — The vector to convert.
