---
title: NSMutableCharacterSet
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutablecharacterset
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablecharacterset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablecharacterset.json'
content_hash: 'sha256:45a9e506cf508fe4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableCharacterSet

<sub>Class</sub>

An object representing a mutable set of Unicode character values for use in search operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableCharacterSet
```

## Overview

In Swift, this object bridges to [CharacterSet](characterset.md); use [NSMutableCharacterSet](nsmutablecharacterset.md) when you need reference semantics or other Foundation-specific behavior.

The `NSMutableCharacterSet` class declares the programmatic interface to objects that manage a modifiable set of Unicode characters. You can add or remove characters from a mutable character set as numeric values in `NSRange` structures or as character values in strings, combine character sets by union or intersection, and invert a character set.

Mutable character sets are less efficient to use than immutable character sets. If you don’t need to change a character set after creating it, create an immutable copy with `copy` and use that.

`NSMutableCharacterSet` defines no primitive methods. Subclasses must implement all methods declared by this class in addition to the primitives of [NSCharacterSet](nscharacterset.md). They must also implement [- mutableCopyWithZone:](<nsmutablecopying/mutablecopy(with_).md>).

`NSMutableCharacterSet` is “toll-free bridged” with its Core Foundation counterpart, [CFMutableCharacterSet](../corefoundation/cfmutablecharacterset.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

> [!important] Important
> The Swift overlay to the Foundation framework provides the [CharacterSet](characterset.md) structure, which bridges to the [NSMutableCharacterSet](nsmutablecharacterset.md) class and its immutable superclass, [NSCharacterSet](nscharacterset.md).  For more information about value types, see [Working with Foundation Types](../swift/working-with-foundation-types.md).

## Relationships

- **Inherits From**: [NSCharacterSet](nscharacterset.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Standard Character Sets

- [+ alphanumericCharacterSet](<nsmutablecharacterset/alphanumeric().md>) — Returns a character set containing the characters in Unicode General Categories L*, M*, and N*.
- [+ capitalizedLetterCharacterSet](<nsmutablecharacterset/capitalizedletter().md>) — Returns a character set containing the characters in Unicode General Category Lt.
- [+ controlCharacterSet](<nsmutablecharacterset/control().md>) — Returns a character set containing the characters in Unicode General Category Cc and Cf.
- [+ decimalDigitCharacterSet](<nsmutablecharacterset/decimaldigit().md>) — Returns a character set containing the characters in the category of decimal numbers.
- [+ decomposableCharacterSet](<nsmutablecharacterset/decomposable().md>) — Returns a character set containing individual Unicode characters that can also be represented as composed character sequences (such as for letters with accents), by the definition of “standard decomposition” in version 3.2 of the Unicode character encoding standard.
- [+ illegalCharacterSet](<nsmutablecharacterset/illegal().md>) — Returns a character set containing values in the category of Non-Characters or that have not yet been defined in version 3.2 of the Unicode standard.
- [+ letterCharacterSet](<nsmutablecharacterset/letter().md>) — Returns a character set containing the characters in Unicode General Category L* & M*.
- [+ lowercaseLetterCharacterSet](<nsmutablecharacterset/lowercaseletter().md>) — Returns a character set containing the characters in Unicode General Category Ll.
- [+ newlineCharacterSet](<nsmutablecharacterset/newline().md>) — Returns a character set containing the newline characters (`U+000A` ~ `U+000D`, `U+0085`, `U+2028`, and `U+2029`).
- [+ nonBaseCharacterSet](<nsmutablecharacterset/nonbase().md>) — Returns a character set containing the characters in Unicode General Category M*.
- [+ punctuationCharacterSet](<nsmutablecharacterset/punctuation().md>) — Returns a character set containing the characters in Unicode General Category P*.
- [+ symbolCharacterSet](<nsmutablecharacterset/symbol().md>) — Returns a character set containing the characters in Unicode General Category S*.
- [+ uppercaseLetterCharacterSet](<nsmutablecharacterset/uppercaseletter().md>) — Returns a character set containing the characters in Unicode General Category Lu and Lt.
- [+ whitespaceAndNewlineCharacterSet](<nsmutablecharacterset/whitespaceandnewline().md>) — Returns a character set containing characters in Unicode General Category Z*, `U+000A` ~ `U+000D`, and `U+0085`.
- [+ whitespaceCharacterSet](<nsmutablecharacterset/whitespace().md>) — Returns a character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION` (`U+0009`).

### Creating Custom Character Sets

- [+ characterSetWithCharactersInString:](<nsmutablecharacterset/init(charactersin_).md>) — Returns a character set containing the characters in a given string.
- [+ characterSetWithRange:](<nsmutablecharacterset/init(range_).md>) — Returns a character set containing characters with Unicode values in a given range.
- [+ characterSetWithBitmapRepresentation:](<nsmutablecharacterset/init(bitmaprepresentation_).md>) — Returns a character set containing characters determined by a given bitmap representation.
- [+ characterSetWithContentsOfFile:](<nsmutablecharacterset/init(contentsoffile_).md>) — Returns a character set read from the bitmap representation stored in the file a given path.

### Adding and Removing Characters

- [- addCharactersInRange:](<nsmutablecharacterset/addcharacters(in_)-4ppyw.md>) — Adds to the receiver the characters whose Unicode values are in a given range.
- [- removeCharactersInRange:](<nsmutablecharacterset/removecharacters(in_)-70nqp.md>) — Removes from the receiver the characters whose Unicode values are in a given range.
- [- addCharactersInString:](<nsmutablecharacterset/addcharacters(in_)-7q02.md>) — Adds to the receiver the characters in a given string.
- [- removeCharactersInString:](<nsmutablecharacterset/removecharacters(in_)-762gt.md>) — Removes from the receiver the characters in a given string.

### Combining Character Sets

- [- formIntersectionWithCharacterSet:](<nsmutablecharacterset/formintersection(with_).md>) — Modifies the receiver so it contains only characters that exist in both the receiver and another set.
- [- formUnionWithCharacterSet:](<nsmutablecharacterset/formunion(with_).md>) — Modifies the receiver so it contains all characters that exist in either the receiver or another set.

### Inverting a Character Set

- [- invert](<nsmutablecharacterset/invert().md>) — Replaces all the characters in the receiver with all the characters it didn’t previously contain.
