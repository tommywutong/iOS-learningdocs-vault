---
title: Initialization with Literals
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/initialization-with-literals
source_url: 'https://developer.apple.com/documentation/swift/initialization-with-literals'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/initialization-with-literals.json'
content_hash: 'sha256:272543f9444efb50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# Initialization with Literals

<sub>API Collection</sub>

Allow values of your type to be expressed using different kinds of literals.

## Topics

### Collection Literals

- [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md) — A type that can be initialized using an array literal.
- [ExpressibleByDictionaryLiteral](expressiblebydictionaryliteral.md) — A type that can be initialized using a dictionary literal.

### Value Literals

- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md) — A type that can be initialized with an integer literal.
- [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md) — A type that can be initialized with a floating-point literal.
- [ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md) — A type that can be initialized with the Boolean literals `true` and `false`.
- [ExpressibleByNilLiteral](expressiblebynilliteral.md) — A type that can be initialized using the nil literal, `nil`.
- [StaticBigInt](staticbigint.md) — An immutable arbitrary-precision signed integer.

### String Literals

- [ExpressibleByStringLiteral](expressiblebystringliteral.md) — A type that can be initialized with a string literal.
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md) — A type that can be initialized with a string literal containing a single extended grapheme cluster.
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md) — A type that can be initialized with a string literal containing a single Unicode scalar value.
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md) — A type that can be initialized by string interpolation with a string literal that includes expressions.
- [StringInterpolationProtocol](stringinterpolationprotocol.md) — Represents the contents of a string literal with interpolations while it’s being built up.
- [DefaultStringInterpolation](defaultstringinterpolation.md) — Represents a string literal with interpolations while it’s being built up.

### Default Types for Literals

- [Default Literal Types](default-literal-types.md) — Type aliases representing the concrete type that a literal takes when no other type information is provided.

## See Also

### Tools for Your Types

- [Basic Behaviors](basic-behaviors.md) — Use your custom types in operations that depend on testing for equality or order and as members of sets and dictionaries.
- [Encoding, Decoding, and Serialization](encoding-decoding-and-serialization.md) — Serialize and deserialize instances of your types with implicit or customized encoding.
