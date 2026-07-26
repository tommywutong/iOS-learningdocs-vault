---
title: byteSwapped
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/int/byteswapped
source_url: 'https://developer.apple.com/documentation/swift/int/byteswapped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/byteswapped.json'
content_hash: 'sha256:93008945dcb6a866'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# byteSwapped

<sub>Instance Property</sub>

A representation of this integer with the byte order swapped.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var byteSwapped: Int { get }
```

## See Also

### Working with Byte Order

- [littleEndian](littleendian.md) — The little-endian representation of this integer.
- [bigEndian](bigendian.md) — The big-endian representation of this integer.
- [init(littleEndian:)](<init(littleendian_).md>) — Creates an integer from its little-endian representation, changing the byte order if necessary.
- [init(bigEndian:)](<init(bigendian_).md>) — Creates an integer from its big-endian representation, changing the byte order if necessary.
