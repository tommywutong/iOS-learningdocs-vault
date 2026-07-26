---
title: 'init(truncatingIfNeeded:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/binaryinteger/init(truncatingifneeded:)'
source_url: 'https://developer.apple.com/documentation/swift/binaryinteger/init(truncatingifneeded:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/binaryinteger/init%28truncatingifneeded%3A%29.json'
content_hash: 'sha256:09afd90f30ebafc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [BinaryInteger](../binaryinteger.md)

# init(truncatingIfNeeded:)

<sub>Initializer</sub>

Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(truncatingIfNeeded source: T) where T : BinaryInteger
```

## Parameters

- `source` — An integer to convert to this type.

## Discussion

When the bit width of `T` (the type of `source`) is equal to or greater than this type’s bit width, the result is the truncated least-significant bits of `source`. For example, when converting a 16-bit value to an 8-bit type, only the lower 8 bits of `source` are used.

```swift
let p: Int16 = -500
// 'p' has a binary representation of 11111110_00001100
let q = Int8(truncatingIfNeeded: p)
// q == 12
// 'q' has a binary representation of 00001100
```

When the bit width of `T` is less than this type’s bit width, the result is _sign-extended_ to fill the remaining bits. That is, if `source` is negative, the result is padded with ones; otherwise, the result is padded with zeros.

```swift
let u: Int8 = 21
// 'u' has a binary representation of 00010101
let v = Int16(truncatingIfNeeded: u)
// v == 21
// 'v' has a binary representation of 00000000_00010101

let w: Int8 = -21
// 'w' has a binary representation of 11101011
let x = Int16(truncatingIfNeeded: w)
// x == -21
// 'x' has a binary representation of 11111111_11101011
let y = UInt16(truncatingIfNeeded: w)
// y == 65515
// 'y' has a binary representation of 11111111_11101011
```

## Default Implementations

### BinaryInteger Implementations

- [init(truncatingIfNeeded:)](<init(truncatingifneeded_)-54a40.md>) — Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.

## See Also

### Converting Integers

- [init(_:)](<init(__)-8gmdl.md>) — Creates a new instance from the given integer.
- [init(clamping:)](<init(clamping_).md>) — Creates a new instance with the representable value that’s closest to the given integer.
