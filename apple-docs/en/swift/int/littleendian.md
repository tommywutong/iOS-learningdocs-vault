---
title: littleEndian
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/littleendian
source_url: 'https://developer.apple.com/documentation/swift/int/littleendian'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/littleendian.json'
content_hash: 'sha256:92076c85e1c21998'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# littleEndian

<sub>Instance Property</sub>

The little-endian representation of this integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var littleEndian: Self { get }
```

## Discussion

If necessary, the byte order of this value is reversed from the typical byte order of this integer type. On a little-endian platform, for any integer `x`, `x == x.littleEndian`.

## See Also

### Working with Byte Order

- [byteSwapped](byteswapped.md) — A representation of this integer with the byte order swapped.
- [bigEndian](bigendian.md) — The big-endian representation of this integer.
- [init(littleEndian:)](<init(littleendian_).md>) — Creates an integer from its little-endian representation, changing the byte order if necessary.
- [init(bigEndian:)](<init(bigendian_).md>) — Creates an integer from its big-endian representation, changing the byte order if necessary.
