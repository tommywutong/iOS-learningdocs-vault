---
title: bitWidth
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/staticbigint/bitwidth
source_url: 'https://developer.apple.com/documentation/swift/staticbigint/bitwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticbigint/bitwidth.json'
content_hash: 'sha256:5183af8a4314162b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticBigInt](../staticbigint.md)

# bitWidth

<sub>Instance Property</sub>

Returns the minimal number of bits in this value’s binary representation, including the sign bit, and excluding the sign extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var bitWidth: Int { get }
```

## Discussion

The following examples show the least significant byte of each value’s binary representation, separated (by an underscore) into excluded and included bits. Negative values are in two’s complement.

- `-4` (`0b11111_100`) is 3 bits.
- `-3` (`0b11111_101`) is 3 bits.
- `-2` (`0b111111_10`) is 2 bits.
- `-1` (`0b1111111_1`) is 1 bit.
- `+0` (`0b0000000_0`) is 1 bit.
- `+1` (`0b000000_01`) is 2 bits.
- `+2` (`0b00000_010`) is 3 bits.
- `+3` (`0b00000_011`) is 3 bits.
