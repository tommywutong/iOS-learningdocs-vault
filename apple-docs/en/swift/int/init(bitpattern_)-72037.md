---
title: 'init(bitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/init(bitpattern:)-72037'
source_url: 'https://developer.apple.com/documentation/swift/int/init(bitpattern:)-72037'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/init%28bitpattern%3A%29-72037.json'
content_hash: 'sha256:ac96da2863066bd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# init(bitPattern:)

<sub>Initializer</sub>

Creates a new instance with the same memory representation as the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bitPattern x: UInt)
```

## Parameters

- `x` — A value to use as the source of the new instance’s binary representation.

## Discussion

This initializer does not perform any range or overflow checking. The resulting instance may not have the same numeric value as `bitPattern`—it is only guaranteed to use the same pattern of bits in its binary representation.

## See Also

### Converting Integers

- [init(_:)](<init(__)-4ekvl.md>) — Creates a new instance from the given integer.
- [init(exactly:)](<init(exactly_)-b1dy.md>)
- [init(clamping:)](<init(clamping_).md>) — Creates a new instance with the representable value that’s closest to the given integer.
- [init(truncatingIfNeeded:)](<init(truncatingifneeded_).md>) — Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(exactly:)](<init(exactly_)-177ax.md>)
- [init(truncating:)](<init(truncating_).md>)
