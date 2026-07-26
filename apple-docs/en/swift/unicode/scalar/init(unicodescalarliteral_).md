---
title: 'init(unicodeScalarLiteral:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/scalar/init(unicodescalarliteral:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/init(unicodescalarliteral:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/init%28unicodescalarliteral%3A%29.json'
content_hash: 'sha256:8be35b08138767cc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# init(unicodeScalarLiteral:)

<sub>Initializer</sub>

Creates a Unicode scalar with the specified value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(unicodeScalarLiteral value: Unicode.Scalar)
```

## Discussion

Do not call this initializer directly. It may be used by the compiler when you use a string literal to initialize a `Unicode.Scalar` instance.

```swift
let letterK: Unicode.Scalar = "K"
print(letterK)
// Prints "K"
```

In this example, the assignment to the `letterK` constant is handled by this initializer behind the scenes.

## See Also

### Creating a Scalar

- [init(_:)](<init(__)-2oo2e.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-5d6us.md>) — Creates a duplicate of the given Unicode scalar.
- [init(_:)](<init(__)-9eo1y.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-18u1m.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-96l5f.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-4p868.md>) — Instantiates an instance of the conforming type from a string representation.
