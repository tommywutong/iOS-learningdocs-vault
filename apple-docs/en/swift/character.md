---
title: Character
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/character
source_url: 'https://developer.apple.com/documentation/swift/character'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/character.json'
content_hash: 'sha256:38b4bd05f4ce7f93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Character

<sub>Structure</sub>

A single extended grapheme cluster that approximates a user-perceived character.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Character
```

## Overview

The `Character` type represents a character made up of one or more Unicode scalar values, grouped by a Unicode boundary algorithm. Generally, a `Character` instance matches what the reader of a string will perceive as a single character. Strings are collections of `Character` instances, so the number of visible characters is generally the most natural way to count the length of a string.

```swift
let greeting = "Hello! 🐥"
print("Length: \(greeting.count)")
// Prints "Length: 8"
```

Because each character in a string can be made up of one or more Unicode scalar values, the number of characters in a string may not match the length of the Unicode scalar value representation or the length of the string in a particular binary representation.

```swift
print("Unicode scalar value count: \(greeting.unicodeScalars.count)")
// Prints "Unicode scalar value count: 8"

print("UTF-8 representation count: \(greeting.utf8.count)")
// Prints "UTF-8 representation count: 11"
```

Every `Character` instance is composed of one or more Unicode scalar values that are grouped together as an _extended grapheme cluster_. The way these scalar values are grouped is defined by a canonical, localized, or otherwise tailored Unicode segmentation algorithm.

For example, a country’s Unicode flag character is made up of two regional indicator scalar values that correspond to that country’s ISO 3166-1 alpha-2 code. The alpha-2 code for The United States is “US”, so its flag character is made up of the Unicode scalar values `"\u{1F1FA}"` (REGIONAL INDICATOR SYMBOL LETTER U) and `"\u{1F1F8}"` (REGIONAL INDICATOR SYMBOL LETTER S). When placed next to each other in a string literal, these two scalar values are combined into a single grapheme cluster, represented by a `Character` instance in Swift.

```swift
let usFlag: Character = "\u{1F1FA}\u{1F1F8}"
print(usFlag)
// Prints "🇺🇸"
```

For more information about the Unicode terms used in this discussion, see the [Unicode.org glossary](http://www.unicode.org/glossary/). In particular, this discussion mentions [extended grapheme clusters](http://www.unicode.org/glossary/#extended_grapheme_cluster) and [Unicode scalar values](http://www.unicode.org/glossary/#unicode_scalar_value).

## Relationships

- **Conforms To**: [Comparable](comparable.md), [Copyable](copyable.md), [CustomDebugStringConvertible](customdebugstringconvertible.md), [CustomReflectable](customreflectable.md), [CustomStringConvertible](customstringconvertible.md), [Equatable](equatable.md), [Escapable](escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md), [Hashable](hashable.md), [LosslessStringConvertible](losslessstringconvertible.md), [RegexComponent](regexcomponent.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md), [TextOutputStreamable](textoutputstreamable.md)

## Topics

### Creating a Character

- [init(_:)](<character/init(__)-6o1aq.md>) — Creates a character from a single-character string.

### Writing to a Text Stream

- [write(to:)](<character/write(to_).md>) — Writes the character into the given output stream.

### Comparing Characters

- [==(_:_:)](<character/==(____).md>) — Returns a Boolean value indicating whether two values are equal.
- [!=(_:_:)](<character/!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.

### Working with a Character’s Unicode Values

- [init(_:)](<character/init(__)-8hq6x.md>) — Creates a character containing the given Unicode scalar value.
- [unicodeScalars](character/unicodescalars.md)
- [UnicodeScalarView](character/unicodescalarview.md)
- [isASCII](character/isascii.md) — A Boolean value indicating whether this is an ASCII character.
- [asciiValue](character/asciivalue.md) — The ASCII encoding value of this character, if it is an ASCII character.

### Inspecting a Character

- [isLetter](character/isletter.md) — A Boolean value indicating whether this character is a letter.
- [isPunctuation](character/ispunctuation.md) — A Boolean value indicating whether this character represents punctuation.
- [isNewline](character/isnewline.md) — A Boolean value indicating whether this character represents a newline.
- [isWhitespace](character/iswhitespace.md) — A Boolean value indicating whether this character represents whitespace, including newlines.
- [isSymbol](character/issymbol.md) — A Boolean value indicating whether this character represents a symbol.
- [isMathSymbol](character/ismathsymbol.md) — A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [isCurrencySymbol](character/iscurrencysymbol.md) — A Boolean value indicating whether this character represents a currency symbol.

### Checking a Character’s Case

- [isCased](character/iscased.md) — A Boolean value indicating whether this character changes under any form of case conversion.
- [isUppercase](character/isuppercase.md) — A Boolean value indicating whether this character is considered uppercase.
- [uppercased()](<character/uppercased().md>) — Returns an uppercased version of this character.
- [isLowercase](character/islowercase.md) — A Boolean value indicating whether this character is considered lowercase.
- [lowercased()](<character/lowercased().md>) — Returns a lowercased version of this character.

### Checking a Character’s Numeric Properties

- [isNumber](character/isnumber.md) — A Boolean value indicating whether this character represents a number.
- [isWholeNumber](character/iswholenumber.md) — A Boolean value indicating whether this character represents a whole number.
- [wholeNumberValue](character/wholenumbervalue.md) — The numeric value this character represents, if it represents a whole number.
- [isHexDigit](character/ishexdigit.md) — A Boolean value indicating whether this character represents a hexadecimal digit.
- [hexDigitValue](character/hexdigitvalue.md) — The numeric value this character represents, if it is a hexadecimal digit.

### Creating a Range Expression

- [...(_:_:)](<character/'...(____).md>) — Returns a closed range that contains both of its bounds.
- [...(_:)](<character/'...(__)-4mm4x.md>) — Returns a partial range up to, and including, its upper bound.
- [...(_:)](<character/'...(__)-6ct59.md>) — Returns a partial range extending upward from a lower bound.

### Describing a Character

- [description](character/description.md) — A textual representation of this instance.
- [debugDescription](character/debugdescription.md) — A textual representation of the character, suitable for debugging.
- [customMirror](character/custommirror.md) — A mirror that reflects the `Character` instance.
- [customPlaygroundQuickLook](character/customplaygroundquicklook.md) — A custom playground Quick Look for the `Character` instance. _(deprecated)_
- [hash(into:)](<character/hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

### Infrequently Used Functionality

- [init(extendedGraphemeClusterLiteral:)](<character/init(extendedgraphemeclusterliteral_).md>) — Creates a character with the specified value.
- [init(unicodeScalarLiteral:)](<character/init(unicodescalarliteral_).md>)

### Instance Properties

- [utf16](character/utf16.md) — A UTF-16 encoding of `self`.
- [utf8](character/utf8.md) — A UTF-8 encoding of `self`.

### Type Aliases

- [Output](character/output.md)
- [UTF16View](character/utf16view.md) — A view of a character’s contents as a collection of UTF-16 code units. See String.UTF16View for more information
- [UTF8View](character/utf8view.md) — A view of a character’s contents as a collection of UTF-8 code units. See String.UTF8View for more information

### Default Implementations

- [Comparable Implementations](character/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](character/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](character/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](character/customstringconvertible-implementations.md)
- [Equatable Implementations](character/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](character/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](character/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](character/hashable-implementations.md)
- [LosslessStringConvertible Implementations](character/losslessstringconvertible-implementations.md)
- [TextOutputStreamable Implementations](character/textoutputstreamable-implementations.md)

## See Also

### Strings and Characters

- [String](string.md) — A Unicode string value that is a collection of characters.
