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
doc_path: '/documentation/swift/int128/init(clamping:)-4ogm3'
source_url: 'https://developer.apple.com/documentation/swift/int128/init(clamping:)-4ogm3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int128/init%28clamping%3A%29-4ogm3.json'
content_hash: 'sha256:831e8b1c57c240ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int128](../int128.md)

# init(clamping:)

<sub>Initializer</sub>

Creates a new instance with the representable value that’s closest to the given integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Other>(clamping source: Other) where Other : BinaryInteger
```

## Parameters

- `source` — An integer to convert to this type.

## Discussion

If the value passed as `source` is greater than the maximum representable value in this type, the result is the type’s `max` value. If `source` is less than the smallest representable value in this type, the result is the type’s `min` value.

In this example, `x` is initialized as an `Int8` instance by clamping `500` to the range `-128...127`, and `y` is initialized as a `UInt` instance by clamping `-500` to the range `0...UInt.max`.

```swift
let x = Int8(clamping: 500)
// x == 127
// x == Int8.max

let y = UInt(clamping: -500)
// y == 0
```
