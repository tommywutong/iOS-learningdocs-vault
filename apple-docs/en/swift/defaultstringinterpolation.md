---
title: DefaultStringInterpolation
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/defaultstringinterpolation
source_url: 'https://developer.apple.com/documentation/swift/defaultstringinterpolation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/defaultstringinterpolation.json'
content_hash: 'sha256:76ee20b4f736d054'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# DefaultStringInterpolation

<sub>Structure</sub>

Represents a string literal with interpolations while it’s being built up.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct DefaultStringInterpolation
```

## Overview

You don’t need to create an instance of this type directly. It’s used by the compiler when you create a string using string interpolation. Instead, use string interpolation to create a new string by including values, literals, variables, or expressions enclosed in parentheses, prefixed by a backslash (`\(`…`)`).

```swift
let price = 2
let number = 3
let message = """
              If one cookie costs \(price) dollars, \
              \(number) cookies cost \(price * number) dollars.
              """
print(message)
// Prints "If one cookie costs 2 dollars, 3 cookies cost 6 dollars."
```

When implementing an `ExpressibleByStringInterpolation` conformance, set the `StringInterpolation` associated type to `DefaultStringInterpolation` to get the same interpolation behavior as Swift’s built-in `String` type and construct a `String` with the results. If you don’t want the default behavior or don’t want to construct a `String`, use a custom type conforming to `StringInterpolationProtocol` instead.

## Extending default string interpolation behavior

Code outside the standard library can extend string interpolation on `String` and many other common types by extending `DefaultStringInterpolation` and adding an `appendInterpolation(...)` method. For example:

```swift
extension DefaultStringInterpolation {
    fileprivate mutating func appendInterpolation(
             escaped value: String, asASCII forceASCII: Bool = false) {
        for char in value.unicodeScalars {
            appendInterpolation(char.escaped(asASCII: forceASCII))
        }
    }
}

print("Escaped string: \(escaped: string)")
```

See `StringInterpolationProtocol` for details on `appendInterpolation` methods.

`DefaultStringInterpolation` extensions should add only `mutating` members and should not copy `self` or capture it in an escaping closure.

## Relationships

- **Conforms To**: [Copyable](copyable.md), [CustomStringConvertible](customstringconvertible.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [StringInterpolationProtocol](stringinterpolationprotocol.md), [TextOutputStream](textoutputstream.md)

## Topics

### Initializers

- [init(literalCapacity:interpolationCount:)](<defaultstringinterpolation/init(literalcapacity_interpolationcount_).md>) — Creates a string interpolation with storage pre-sized for a literal with the indicated attributes.

### Instance Methods

- [appendInterpolation(_:)](<defaultstringinterpolation/appendinterpolation(__)-2bzja.md>) — Interpolates the given value’s textual representation into the string literal being created.
- [appendInterpolation(_:)](<defaultstringinterpolation/appendinterpolation(__)-468zr.md>) — Interpolates the given value’s textual representation into the string literal being created.
- [appendInterpolation(_:)](<defaultstringinterpolation/appendinterpolation(__)-6kx4d.md>) — Interpolates the given value’s textual representation into the string literal being created.
- [appendInterpolation(_:)](<defaultstringinterpolation/appendinterpolation(__)-8x6aw.md>) — Interpolates the given value’s textual representation into the string literal being created.
- [appendInterpolation(_:)](<defaultstringinterpolation/appendinterpolation(__)-jfy9.md>)
- [appendInterpolation(_:default:)](<defaultstringinterpolation/appendinterpolation(__default_)-4b2j8.md>) — Interpolates the given optional value’s textual representation, or the specified default string, into the string literal being created.
- [appendInterpolation(_:default:)](<defaultstringinterpolation/appendinterpolation(__default_)-64wk7.md>) — Interpolates the given optional value’s textual representation, or the specified default string, into the string literal being created.
- [appendInterpolation(_:default:)](<defaultstringinterpolation/appendinterpolation(__default_)-8wdp1.md>) — Interpolates the given optional value’s textual representation, or the specified default string, into the string literal being created.
- [appendInterpolation(_:default:)](<defaultstringinterpolation/appendinterpolation(__default_)-9dh5y.md>) — Interpolates the given optional value’s textual representation, or the specified default string, into the string literal being created.
- [appendInterpolation(_:default:)](<defaultstringinterpolation/appendinterpolation(__default_)-ue3g.md>) — Interpolates the given optional value’s textual representation, or the specified default string, into the string literal being created.
- [appendLiteral(_:)](<defaultstringinterpolation/appendliteral(__).md>) — Appends a literal segment of a string interpolation.

### Type Aliases

- [StringLiteralType](defaultstringinterpolation/stringliteraltype.md) — The type that should be used for literal segments.

### Default Implementations

- [CustomStringConvertible Implementations](defaultstringinterpolation/customstringconvertible-implementations.md)
- [TextOutputStream Implementations](defaultstringinterpolation/textoutputstream-implementations.md)

## See Also

### String Literals

- [ExpressibleByStringLiteral](expressiblebystringliteral.md) — A type that can be initialized with a string literal.
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md) — A type that can be initialized with a string literal containing a single extended grapheme cluster.
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md) — A type that can be initialized with a string literal containing a single Unicode scalar value.
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md) — A type that can be initialized by string interpolation with a string literal that includes expressions.
- [StringInterpolationProtocol](stringinterpolationprotocol.md) — Represents the contents of a string literal with interpolations while it’s being built up.
