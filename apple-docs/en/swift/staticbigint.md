---
title: StaticBigInt
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/staticbigint
source_url: 'https://developer.apple.com/documentation/swift/staticbigint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticbigint.json'
content_hash: 'sha256:6267c4264d713c54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# StaticBigInt

<sub>Structure</sub>

An immutable arbitrary-precision signed integer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct StaticBigInt
```

## Overview

`StaticBigInt` is primarily intended to be used as the associated type of an `ExpressibleByIntegerLiteral` conformance.

```swift
extension UInt256: ExpressibleByIntegerLiteral {
    public init(integerLiteral value: StaticBigInt) {
        precondition(
            value.signum() >= 0 && value.bitWidth <= 1 + Self.bitWidth,
            "integer overflow: '\(value)' as '\(Self.self)'"
        )
        self.words = Words()
        for wordIndex in 0..<Words.count {
            self.words[wordIndex] = value[wordIndex]
        }
    }
}
```

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [Escapable](escapable.md), [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Instance Properties

- [bitWidth](staticbigint/bitwidth.md) — Returns the minimal number of bits in this value’s binary representation, including the sign bit, and excluding the sign extension.

### Instance Methods

- [signum()](<staticbigint/signum().md>) — Indicates the value’s sign.

### Subscripts

- [subscript(_:)](<staticbigint/subscript(__).md>) — Returns a 32-bit or 64-bit word of this value’s binary representation.

### Type Aliases

- [IntegerLiteralType](staticbigint/integerliteraltype.md) — A type that represents an integer literal.

### Default Implementations

- [CustomDebugStringConvertible Implementations](staticbigint/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](staticbigint/customreflectable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](staticbigint/expressiblebyintegerliteral-implementations.md)

## See Also

### Value Literals

- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md) — A type that can be initialized with an integer literal.
- [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md) — A type that can be initialized with a floating-point literal.
- [ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md) — A type that can be initialized with the Boolean literals `true` and `false`.
- [ExpressibleByNilLiteral](expressiblebynilliteral.md) — A type that can be initialized using the nil literal, `nil`.
