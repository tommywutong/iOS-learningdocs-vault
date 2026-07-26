---
title: Default Literal Types
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/default-literal-types
source_url: 'https://developer.apple.com/documentation/swift/default-literal-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/default-literal-types.json'
content_hash: 'sha256:22e20c494bfb9d3b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md) · [Initialization with Literals](initialization-with-literals.md)

# Default Literal Types

<sub>API Collection</sub>

Type aliases representing the concrete type that a literal takes when no other type information is provided.

## Overview

This example declares the `numberOfCookies` constant, using an integer literal to express its value:

```swift
let numberOfCookies = 5
// type(of: numberOfCookies) == Int.self
```

When a literal expression is written with no type information, Swift uses these type aliases to determine what type to use for the expression. In this case, the `numberOfCookies` constant has the default type for an integer literal, `Int`, as designated by the `IntegerLiteralType` type alias.

## Topics

### Basic Values

- [BooleanLiteralType](booleanliteraltype.md) — The default type for an otherwise-unconstrained Boolean literal.
- [IntegerLiteralType](integerliteraltype.md) — The default type for an otherwise-unconstrained integer literal.
- [FloatLiteralType](floatliteraltype.md) — The default type for an otherwise-unconstrained floating-point literal.

### Strings and Text

- [StringLiteralType](stringliteraltype.md) — The default type for an otherwise-unconstrained string literal.
- [ExtendedGraphemeClusterType](extendedgraphemeclustertype.md) — The default type for an otherwise-unconstrained Unicode extended grapheme cluster literal.
- [UnicodeScalarType](unicodescalartype.md) — The default type for an otherwise-unconstrained unicode scalar literal.
