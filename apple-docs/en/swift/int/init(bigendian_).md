---
title: 'init(bigEndian:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/init(bigendian:)'
source_url: 'https://developer.apple.com/documentation/swift/int/init(bigendian:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/init%28bigendian%3A%29.json'
content_hash: 'sha256:829a552903596d5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# init(bigEndian:)

<sub>Initializer</sub>

Creates an integer from its big-endian representation, changing the byte order if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bigEndian value: Self)
```

## Parameters

- `value` — A value to use as the big-endian representation of the new integer.

## See Also

### Working with Byte Order

- [byteSwapped](byteswapped.md) — A representation of this integer with the byte order swapped.
- [littleEndian](littleendian.md) — The little-endian representation of this integer.
- [bigEndian](bigendian.md) — The big-endian representation of this integer.
- [init(littleEndian:)](<init(littleendian_).md>) — Creates an integer from its little-endian representation, changing the byte order if necessary.
