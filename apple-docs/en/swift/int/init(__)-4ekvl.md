---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/init(_:)-4ekvl'
source_url: 'https://developer.apple.com/documentation/swift/int/init(_:)-4ekvl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/init%28_%3A%29-4ekvl.json'
content_hash: 'sha256:d6f39fd707d732b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# init(_:)

<sub>Initializer</sub>

Creates a new instance from the given integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ source: T) where T : BinaryInteger
```

## Parameters

- `source` — A value to convert to this type of integer. The value passed as `source` must be representable in this type.

## Discussion

Use this initializer to convert from another integer type when you know the value is within the bounds of this type. Passing a value that can’t be represented in this type results in a runtime error.

In the following example, the constant `y` is successfully created from `x`, an `Int` instance with a value of `100`. Because the `Int8` type can represent `127` at maximum, the attempt to create `z` with a value of `1000` results in a runtime error.

```swift
let x = 100
let y = Int8(x)
// y == 100
let z = Int8(x * 10)
// Error: Not enough bits to represent the given value
```

## See Also

### Converting Integers

- [init(exactly:)](<init(exactly_)-b1dy.md>)
- [init(clamping:)](<init(clamping_).md>) — Creates a new instance with the representable value that’s closest to the given integer.
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(bitPattern:)](<init(bitpattern_)-72037.md>) — Creates a new instance with the same memory representation as the given value.
- [init(exactly:)](<init(exactly_)-177ax.md>)
- [init(truncating:)](<init(truncating_).md>)
