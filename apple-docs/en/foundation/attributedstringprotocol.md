---
title: AttributedStringProtocol
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstringprotocol
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol.json'
content_hash: 'sha256:94d62193adf7e212'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AttributedStringProtocol

<sub>Protocol</sub>

A protocol that provides common functionality to attributed strings and attributed substrings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup protocol AttributedStringProtocol : AttributedStringAttributeMutation, CustomStringConvertible, Hashable, Sendable
```

## Overview

Don’t declare new conformances to [AttributedStringProtocol](attributedstringprotocol.md). Only the [AttributedString](attributedstring.md) and [AttributedSubstring](attributedsubstring.md) types in the standard library are valid conforming types.

## Relationships

- **Inherits From**: [AttributedStringAttributeMutation](attributedstringattributemutation.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

- **Conforming Types**: [AttributedString](attributedstring.md), [AttributedSubstring](attributedsubstring.md)

## Topics

### Applying Attributes

- [settingAttributes(_:)](<attributedstringprotocol/settingattributes(__).md>) — Returns an attributed string by setting the attributed string’s attributes to those in a specified attribute container.
- [mergingAttributes(_:mergePolicy:)](<attributedstringprotocol/mergingattributes(__mergepolicy_).md>) — Returns an attributed string by merging the attributed string’s attributes with those in a specified attribute container.
- [AttributeMergePolicy](attributedstring/attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
- [replacingAttributes(_:with:)](<attributedstringprotocol/replacingattributes(__with_).md>) — Returns an attributed string by replacing occurrences of attributes in one attribute container with those in another attribute container.

### Searching for a Substring

- [range(of:options:locale:)](<attributedstringprotocol/range(of_options_locale_).md>) — Returns the range of a substring in the attributed string, if it exists.

### Accessing a Range

- [subscript(_:)](<attributedstringprotocol/subscript(__)-109me.md>) — Returns a substring of the attributed string using a range to indicate the substring bounds.

### Accessing Indices

- [startIndex](attributedstringprotocol/startindex.md) — The position of the first character in a nonempty attributed string.
- [endIndex](attributedstringprotocol/endindex.md) — A string’s past-the-end position — the position one greater than the last valid subscript argument.
- [index(_:offsetByCharacters:)](<attributedstringprotocol/index(__offsetbycharacters_).md>) — Returns the position of the character offset a given distance, measured in characters, from a given string index.
- [index(_:offsetByRuns:)](<attributedstringprotocol/index(__offsetbyruns_).md>) — Returns the position of the run offset a given number of runs from a given string index.
- [index(_:offsetByUnicodeScalars:)](<attributedstringprotocol/index(__offsetbyunicodescalars_).md>) — Returns the position of the Unicode scalar offset a given distance, measured in Unicode scalars, from a given string index.
- [index(afterCharacter:)](<attributedstringprotocol/index(aftercharacter_).md>) — Returns the position of the character immediately after another charcter indicated by an index.
- [index(afterRun:)](<attributedstringprotocol/index(afterrun_).md>) — Returns the position of the run immediately after a run indicated by an index.
- [index(afterUnicodeScalar:)](<attributedstringprotocol/index(afterunicodescalar_).md>) — Returns the position of the Unicode scalar immediately after a Unicode scalar indicated by an index.
- [index(beforeCharacter:)](<attributedstringprotocol/index(beforecharacter_).md>) — Returns the position of the character immediately before another charcter indicated by an index.
- [index(beforeRun:)](<attributedstringprotocol/index(beforerun_).md>) — Returns the position of the run immediately before a run indicated by an index.
- [index(beforeUnicodeScalar:)](<attributedstringprotocol/index(beforeunicodescalar_).md>) — Returns the position of the Unicode scalar immediately before a Unicode scalar indicated by an index.
- [Index](attributedstring/index.md) — A type that represents the position of a character or code unit within an attributed string.

### Accessing Views into the Attributed String

- [characters](attributedstringprotocol/characters.md) — The characters of the attributed string, as a view into the underlying string.
- [unicodeScalars](attributedstringprotocol/unicodescalars.md) — The Unicode scalars of the attributed string, as a view into the underlying string.
- [runs](attributedstringprotocol/runs.md) — The attributed runs of the attributed string, as a view into the underlying string.

### Accessing Whole-String Attributes

- [subscript(_:)](<attributedstringprotocol/subscript(__)-4thnp.md>) — Returns an attribute value that corresponds to an attributed string key.
- [subscript(dynamicMember:)](<attributedstringprotocol/subscript(dynamicmember_)-2wake.md>) — Returns an attribute value that a key path indicates.
- [AttributeDynamicLookup](attributedynamiclookup.md) — A type to support dynamic member lookup of attributes and containers.
- [subscript(dynamicMember:)](<attributedstringprotocol/subscript(dynamicmember_)-55pcu.md>) — Returns a scoped attribute container that a key path indicates.
- [ScopedAttributeContainer](scopedattributecontainer.md) — An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.

### Comparing Attributed Strings or Substrings

- [==(_:_:)](<attributedstringprotocol/==(____).md>)

### Instance Properties

- [utf16](attributedstringprotocol/utf16.md)
- [utf8](attributedstringprotocol/utf8.md)

### Default Implementations

- [CustomStringConvertible Implementations](attributedstringprotocol/customstringconvertible-implementations.md)
- [Hashable Implementations](attributedstringprotocol/hashable-implementations.md)
