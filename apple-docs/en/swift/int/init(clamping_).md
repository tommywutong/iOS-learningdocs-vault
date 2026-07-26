---
title: 'init(clamping:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/init(clamping:)'
source_url: 'https://developer.apple.com/documentation/swift/int/init(clamping:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/init%28clamping%3A%29.json'
content_hash: 'sha256:2ea7a0e44331db28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

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

## See Also

### Converting Integers

- [init(_:)](<init(__)-4ekvl.md>) — Creates a new instance from the given integer.
- [init(exactly:)](<init(exactly_)-b1dy.md>)
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(bitPattern:)](<init(bitpattern_)-72037.md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<init(exactly_)-177ax.md>)
- [init(truncating:)](<init(truncating_).md>)
