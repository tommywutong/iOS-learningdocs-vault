---
title: 'unsafeBitCast(_:to:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafebitcast(_:to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafebitcast(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebitcast%28_%3Ato%3A%29.json'
content_hash: 'sha256:f36c5b122bfde107'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# unsafeBitCast(_:to:)

<sub>Function</sub>

Returns the bits of the given instance, interpreted as having the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unsafeBitCast<T, U>(_ x: T, to type: U.Type) -> U
```

## Discussion

Use this function only to convert the instance passed as `x` to a layout-compatible type when conversion through other means is not possible. Common conversions supported by the Swift standard library include the following:

- Value conversion from one integer type to another. Use the destination type’s initializer or the `numericCast(_:)` function.
- Bitwise conversion from one integer type to another. Use the destination type’s `init(truncatingIfNeeded:)` or `init(bitPattern:)` initializer.
- Conversion from a pointer to an integer value with the bit pattern of the pointer’s address in memory, or vice versa. Use the `init(bitPattern:)` initializer for the destination type.
- Casting an instance of a reference type. Use the casting operators (`as`, `as!`, or `as?`) or the `unsafeDowncast(_:to:)` function. Do not use `unsafeBitCast(_:to:)` with class or pointer types; doing so may introduce undefined behavior.

Warning: Calling this function breaks the guarantees of the Swift type system; use with extreme care.

Warning: Casting from an integer or a pointer type to a reference type is undefined behavior. It may result in incorrect code in any future compiler release. To convert a bit pattern to a reference type:

1. convert the bit pattern to an UnsafeRawPointer.
2. create an unmanaged reference using Unmanaged.fromOpaque()
3. obtain a managed reference using Unmanaged.takeUnretainedValue() The programmer must ensure that the resulting reference has already been manually retained.

Parameters:

- x: The instance to cast to `type`.
- type: The type to cast `x` to. `type` and the type of `x` must have the same size of memory representation and compatible memory layout. Returns: A new instance of type `U`, cast from `x`.

## See Also

### Instance Casting

- [unsafeDowncast(_:to:)](<unsafedowncast(__to_).md>) — Returns the given instance cast unconditionally to the specified type.
