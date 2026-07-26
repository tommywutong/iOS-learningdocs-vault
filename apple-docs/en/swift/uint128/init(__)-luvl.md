---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/uint128/init(_:)-luvl'
source_url: 'https://developer.apple.com/documentation/swift/uint128/init(_:)-luvl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint128/init%28_%3A%29-luvl.json'
content_hash: 'sha256:668d4e2ebd5e334a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UInt128](../uint128.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance from the given integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ source: T) where T : BinaryInteger
```

## Parameters

- `source` — An integer to convert. `source` must be representable in this type.

## Discussion

If the value passed as `source` is not representable in this type, a runtime error may occur.

```swift
let x = -500 as Int
let y = Int32(x)
// y == -500

// -500 is not representable as a 'UInt32' instance
let z = UInt32(x)
// Error
```
