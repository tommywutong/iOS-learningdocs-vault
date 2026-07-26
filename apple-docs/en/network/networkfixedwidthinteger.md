---
title: NetworkFixedWidthInteger
framework: Network
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkfixedwidthinteger
source_url: 'https://developer.apple.com/documentation/network/networkfixedwidthinteger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkfixedwidthinteger.json'
content_hash: 'sha256:bf6460c7e194e350'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NetworkFixedWidthInteger

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NetworkFixedWidthInteger : FixedWidthInteger
```

## Relationships

- **Inherits From**: [AdditiveArithmetic](../swift/additivearithmetic.md), [BinaryInteger](../swift/binaryinteger.md), [Comparable](../swift/comparable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md), [FixedWidthInteger](../swift/fixedwidthinteger.md), [Hashable](../swift/hashable.md), [LosslessStringConvertible](../swift/losslessstringconvertible.md), [Numeric](../swift/numeric.md), [Strideable](../swift/strideable.md)

## Topics

### Initializers

- [init(bigEndian:)](<networkfixedwidthinteger/init(bigendian_).md>) — Creates an integer from its big-endian representation, changing the byte order if necessary.

### Instance Properties

- [bigEndian](networkfixedwidthinteger/bigendian.md) — The big-endian representation of this integer.
