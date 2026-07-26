---
title: Unicode.Scalar
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/scalar
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar.json'
content_hash: 'sha256:5e886d8e9cf5b7db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unicode](../unicode.md)

# Unicode.Scalar

<sub>Structure</sub>

A Unicode scalar value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Scalar
```

## Overview

The `Unicode.Scalar` type, representing a single Unicode scalar value, is the element type of a string’s `unicodeScalars` collection.

You can create a `Unicode.Scalar` instance by using a string literal that contains a single character representing exactly one Unicode scalar value.

```swift
let letterK: Unicode.Scalar = "K"
let kim: Unicode.Scalar = "김"
print(letterK, kim)
// Prints "K 김"
```

You can also create Unicode scalar values directly from their numeric representation.

```swift
let airplane = Unicode.Scalar(9992)!
print(airplane)
// Prints "✈︎"
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../bitwisecopyable.md), [Comparable](../comparable.md), [Copyable](../copyable.md), [CustomDebugStringConvertible](../customdebugstringconvertible.md), [CustomReflectable](../customreflectable.md), [CustomStringConvertible](../customstringconvertible.md), [Equatable](../equatable.md), [Escapable](../escapable.md), [ExpressibleByUnicodeScalarLiteral](../expressiblebyunicodescalarliteral.md), [Hashable](../hashable.md), [LosslessStringConvertible](../losslessstringconvertible.md), [RegexComponent](../regexcomponent.md), [Sendable](../sendable.md), [SendableMetatype](../sendablemetatype.md), [TextOutputStreamable](../textoutputstreamable.md)

## Topics

### Creating a Scalar

- [init(_:)](<scalar/init(__)-2oo2e.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<scalar/init(__)-5d6us.md>) — Creates a duplicate of the given Unicode scalar.
- [init(_:)](<scalar/init(__)-9eo1y.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<scalar/init(__)-18u1m.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<scalar/init(__)-96l5f.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral:)](<scalar/init(unicodescalarliteral_).md>) — Creates a Unicode scalar with the specified value.
- [init(_:)](<scalar/init(__)-4p868.md>) — Instantiates an instance of the conforming type from a string representation.

### Inspecting a Scalar

- [value](scalar/value.md) — A numeric representation of the Unicode scalar.
- [properties](scalar/properties-swift.property.md) — Properties of this scalar defined by the Unicode standard.
- [Properties](scalar/properties-swift.struct.md) — A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.
- [hash(into:)](<scalar/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [isASCII](scalar/isascii.md) — A Boolean value indicating whether the Unicode scalar is an ASCII character.

### Printing and Displaying a Scalar

- [description](scalar/description.md) — A textual representation of the Unicode scalar.
- [write(to:)](<scalar/write(to_).md>) — Writes the textual representation of the Unicode scalar into the given output stream.
- [escaped(asASCII:)](<scalar/escaped(asascii_).md>) — Returns a string representation of the Unicode scalar.
- [utf16](scalar/utf16.md)
- [UTF16View](scalar/utf16view.md)
- [debugDescription](scalar/debugdescription.md) — An escaped textual representation of the Unicode scalar, suitable for debugging.
- [customMirror](scalar/custommirror.md) — A mirror that reflects the `Unicode.Scalar` instance.
- [customPlaygroundQuickLook](scalar/customplaygroundquicklook.md) — A custom playground Quick Look for the `Unicode.Scalar` instance. _(deprecated)_

### Comparing Scalars

- [==(_:_:)](<scalar/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [!=(_:_:)](<scalar/!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.
- [\<(_:_:)](<scalar/_(____).md>) — Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.

### Creating Ranges of Scalars

- [...(_:)](<scalar/'...(__)-9u9rz.md>) — Returns a partial range extending upward from a lower bound.
- [...(_:)](<scalar/'...(__)-7lhvp.md>) — Returns a partial range up to, and including, its upper bound.
- [...(_:_:)](<scalar/'...(____).md>) — Returns a closed range that contains both of its bounds.
- [..\<(_:)](<scalar/'.._(__).md>) — Returns a partial range up to, but not including, its upper bound.
- [..\<(_:_:)](<scalar/'.._(____).md>) — Returns a half-open range that contains its lower bound but not its upper bound.

### Structures

- [UTF8View](scalar/utf8view.md)

### Instance Properties

- [utf8](scalar/utf8.md)

### Type Aliases

- [Output](scalar/output.md)

### Default Implementations

- [Comparable Implementations](scalar/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](scalar/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](scalar/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](scalar/customstringconvertible-implementations.md)
- [Equatable Implementations](scalar/equatable-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](scalar/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](scalar/hashable-implementations.md)
- [LosslessStringConvertible Implementations](scalar/losslessstringconvertible-implementations.md)
- [TextOutputStreamable Implementations](scalar/textoutputstreamable-implementations.md)
