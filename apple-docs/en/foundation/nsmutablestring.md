---
title: NSMutableString
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutablestring
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablestring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablestring.json'
content_hash: 'sha256:ba2c9976f0d7e15e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableString

<sub>Class</sub>

A dynamic plain-text Unicode string object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableString
```

## Overview

In Swift, you can use this type instead of a [String](../swift/string.md) in cases that require reference semantics.

The `NSMutableString` class declares the programmatic interface to an object that manages a mutable string—that is, a string whose contents can be edited—that conceptually represents an array of Unicode characters. To construct and manage an immutable string—or a string that cannot be changed after it has been created—use an object of the [NSString](nsstring.md) class.

The `NSMutableString` class adds one primitive method—[- replaceCharactersInRange:withString:](<nsmutablestring/replacecharacters(in_with_).md>)—to the basic string-handling behavior inherited from `NSString`. All other methods that modify a string work through this method. For example, [- insertString:atIndex:](<nsmutablestring/insert(__at_).md>) simply replaces the characters in a range of `0` length, while [- deleteCharactersInRange:](<nsmutablestring/deletecharacters(in_).md>) replaces the characters in a given range with no characters.

NSMutableString is “toll-free bridged” with its Core Foundation counterpart, [CFMutableString](../corefoundation/cfmutablestring.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

## Relationships

- **Inherits From**: [NSString](nsstring.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSItemProviderReading](nsitemproviderreading.md), [NSItemProviderWriting](nsitemproviderwriting.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating and Initializing a Mutable String

- [- initWithCapacity:](<nsmutablestring/init(capacity_).md>) — Returns an `NSMutableString` object initialized with initial storage for a given number of characters,

### Modifying a String

- [- appendString:](<nsmutablestring/append(__).md>) — Adds to the end of the receiver the characters of a given string.
- [- applyTransform:reverse:range:updatedRange:](<nsmutablestring/applytransform(__reverse_range_updatedrange_).md>) — Transliterates the receiver by applying a specified ICU string transform.
- [- deleteCharactersInRange:](<nsmutablestring/deletecharacters(in_).md>) — Removes from the receiver the characters in a given range.
- [- insertString:atIndex:](<nsmutablestring/insert(__at_).md>) — Inserts into the receiver the characters of a given string at a given location.
- [- replaceCharactersInRange:withString:](<nsmutablestring/replacecharacters(in_with_).md>) — Replaces the characters from `range` with those in `aString`.
- [- replaceOccurrencesOfString:withString:options:range:](<nsmutablestring/replaceoccurrences(of_with_options_range_).md>) — Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [- setString:](<nsmutablestring/setstring(__).md>) — Replaces the characters of the receiver with those in a given string.

### Constants

- [String Transformations](string-transformations.md) — These constants specify transforms used by the [- applyTransform:reverse:range:updatedRange:](<nsmutablestring/applytransform(__reverse_range_updatedrange_).md>) method.

### Instance Methods

- [appendFormat(_:_:)](<nsmutablestring/appendformat(____).md>)
