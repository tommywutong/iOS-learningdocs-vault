---
title: CharacterSet
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/characterset
source_url: 'https://developer.apple.com/documentation/foundation/characterset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset.json'
content_hash: 'sha256:39e6818dfd3293cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# CharacterSet

<sub>Structure</sub>

A set of Unicode character values for use in search operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CharacterSet
```

## Overview

A `CharacterSet` represents a set of Unicode-compliant characters. Foundation types use `CharacterSet` to group characters together for searching operations, so that they can find any of a particular set of characters during a search.

This type provides “copy-on-write” behavior, and is also bridged to the Objective-C `NSCharacterSet` class.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [Hashable](../swift/hashable.md), [ReferenceConvertible](referenceconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting Standard Character Sets

- [alphanumerics](characterset/alphanumerics.md) — Returns a character set containing the characters in Unicode General Categories L*, M*, and N*.
- [capitalizedLetters](characterset/capitalizedletters.md) — Returns a character set containing the characters in Unicode General Category Lt.
- [controlCharacters](characterset/controlcharacters.md) — Returns a character set containing the characters in Unicode General Category Cc and Cf.
- [decimalDigits](characterset/decimaldigits.md) — Returns a character set containing the characters in the category of Decimal Numbers.
- [decomposables](characterset/decomposables.md) — Returns a character set containing individual Unicode characters that can also be represented as composed character sequences (such as for letters with accents), by the definition of “standard decomposition” in version 3.2 of the Unicode character encoding standard.
- [illegalCharacters](characterset/illegalcharacters.md) — Returns a character set containing values in the category of Non-Characters or that have not yet been defined in version 3.2 of the Unicode standard.
- [letters](characterset/letters.md) — Returns a character set containing the characters in Unicode General Category L* & M*.
- [lowercaseLetters](characterset/lowercaseletters.md) — Returns a character set containing the characters in Unicode General Category Ll.
- [newlines](characterset/newlines.md) — Returns a character set containing the newline characters (`U+000A ~ U+000D`, `U+0085`, `U+2028`, and `U+2029`).
- [nonBaseCharacters](characterset/nonbasecharacters.md) — Returns a character set containing the characters in Unicode General Category M*.
- [punctuationCharacters](characterset/punctuationcharacters.md) — Returns a character set containing the characters in Unicode General Category P*.
- [symbols](characterset/symbols.md) — Returns a character set containing the characters in Unicode General Category S*.
- [uppercaseLetters](characterset/uppercaseletters.md) — Returns a character set containing the characters in Unicode General Category Lu and Lt.
- [whitespaces](characterset/whitespaces.md) — Returns a character set containing the characters in Unicode General Category Zs and `CHARACTER TABULATION (U+0009)`.
- [whitespacesAndNewlines](characterset/whitespacesandnewlines.md) — Returns a character set containing characters in Unicode General Category Z*, `U+000A ~ U+000D`, and `U+0085`.

### Getting Character Sets for URL Encoding

- [urlFragmentAllowed](characterset/urlfragmentallowed.md) — Returns the character set for characters allowed in a fragment URL component.
- [urlHostAllowed](characterset/urlhostallowed.md) — Returns the character set for characters allowed in a host URL subcomponent.
- [urlPasswordAllowed](characterset/urlpasswordallowed.md) — Returns the character set for characters allowed in a password URL subcomponent.
- [urlPathAllowed](characterset/urlpathallowed.md) — Returns the character set for characters allowed in a path URL component.
- [urlQueryAllowed](characterset/urlqueryallowed.md) — Returns the character set for characters allowed in a query URL component.
- [urlUserAllowed](characterset/urluserallowed.md) — Returns the character set for characters allowed in a user URL subcomponent.

### Creating a Custom Character Set

- [init()](<characterset/init().md>) — Initialize an empty instance.

### Creating and Managing Bitmap Representations

- [bitmapRepresentation](characterset/bitmaprepresentation.md) — Returns a representation of the `CharacterSet` in binary format.

### Inverting a Character Set

- [invert()](<characterset/invert().md>) — Invert the contents of the `CharacterSet`.
- [inverted](characterset/inverted.md) — Returns an inverted copy of the receiver.

### Combining Character Sets

- [formIntersection(_:)](<characterset/formintersection(__).md>) — Sets the value to an intersection of the `CharacterSet` with another `CharacterSet`.
- [formSymmetricDifference(_:)](<characterset/formsymmetricdifference(__).md>) — Sets the value to an exclusive or of the `CharacterSet` with another `CharacterSet`.
- [formUnion(_:)](<characterset/formunion(__).md>) — Sets the value to a union of the `CharacterSet` with another `CharacterSet`.
- [hasMember(inPlane:)](<characterset/hasmember(inplane_).md>) — Returns true if the `CharacterSet` has a member in the specified plane.
- [insert(charactersIn:)](<characterset/insert(charactersin_)-2syuj.md>) — Insert the values from the specified string into the `CharacterSet`.
- [intersection(_:)](<characterset/intersection(__).md>) — Returns an intersection of the `CharacterSet` with another `CharacterSet`.
- [invert()](<characterset/invert().md>) — Invert the contents of the `CharacterSet`.
- [isSuperset(of:)](<characterset/issuperset(of_).md>) — Returns true if `self` is a superset of `other`.
- [remove(charactersIn:)](<characterset/remove(charactersin_)-3sayw.md>) — Remove the values from the specified string from the `CharacterSet`.
- [subtracting(_:)](<characterset/subtracting(__).md>) — Returns a `CharacterSet` created by removing elements in `other` from `self`.
- [symmetricDifference(_:)](<characterset/symmetricdifference(__).md>) — Returns an exclusive or of the `CharacterSet` with another `CharacterSet`.
- [union(_:)](<characterset/union(__).md>) — Returns a union of the `CharacterSet` with another `CharacterSet`.

### Adding Characters

- [insert(charactersIn:)](<characterset/insert(charactersin_)-2syuj.md>) — Insert the values from the specified string into the `CharacterSet`.

### Removing Characters

- [remove(charactersIn:)](<characterset/remove(charactersin_)-3sayw.md>) — Remove the values from the specified string from the `CharacterSet`.
- [subtracting(_:)](<characterset/subtracting(__).md>) — Returns a `CharacterSet` created by removing elements in `other` from `self`.

### Testing Set Membership

- [hasMember(inPlane:)](<characterset/hasmember(inplane_).md>) — Returns true if the `CharacterSet` has a member in the specified plane.
- [isSuperset(of:)](<characterset/issuperset(of_).md>) — Returns true if `self` is a superset of `other`.

### Comparing Character Sets

- [==(_:_:)](<characterset/==(____).md>) — Returns true if the two `CharacterSet`s are equal.

### Using Reference Types

- [NSCharacterSet](nscharacterset.md) — An object representing a fixed set of Unicode character values for use in search operations.
- [NSMutableCharacterSet](nsmutablecharacterset.md) — An object representing a mutable set of Unicode character values for use in search operations.

### Initializers

- [init(bitmapRepresentation:)](<characterset/init(bitmaprepresentation_).md>) — Initialize with a bitmap representation.
- [init(charactersIn:)](<characterset/init(charactersin_)-87iva.md>) — Initialize with a closed range of integers.
- [init(charactersIn:)](<characterset/init(charactersin_)-87m2b.md>) — Initialize with the characters in the given string.
- [init(charactersIn:)](<characterset/init(charactersin_)-8tcll.md>) — Initialize with a range of integers.
- [init(contentsOfFile:)](<characterset/init(contentsoffile_).md>) — Initialize with the contents of a file.

### Instance Methods

- [contains(_:)](<characterset/contains(__).md>) — Test for membership of a particular `Unicode.Scalar` in the `CharacterSet`.
- [insert(_:)](<characterset/insert(__).md>) — Insert a `Unicode.Scalar` representation of a character into the `CharacterSet`.
- [insert(charactersIn:)](<characterset/insert(charactersin_)-7urdg.md>) — Insert a range of integer values in the `CharacterSet`.
- [insert(charactersIn:)](<characterset/insert(charactersin_)-803uz.md>) — Insert a closed range of integer values in the `CharacterSet`.
- [remove(_:)](<characterset/remove(__).md>) — Remove a `Unicode.Scalar` representation of a character from the `CharacterSet`.
- [remove(charactersIn:)](<characterset/remove(charactersin_)-1kqte.md>) — Remove a closed range of integer values from the `CharacterSet`.
- [remove(charactersIn:)](<characterset/remove(charactersin_)-5td97.md>) — Remove a range of integer values from the `CharacterSet`.
- [subtract(_:)](<characterset/subtract(__).md>) — Sets the value to a `CharacterSet` created by removing elements in `other` from `self`.
- [update(with:)](<characterset/update(with_).md>) — Insert a `Unicode.Scalar` representation of a character into the `CharacterSet`.

## See Also

### Characters

- [UnicodeScalar](../swift/unicodescalar.md)
