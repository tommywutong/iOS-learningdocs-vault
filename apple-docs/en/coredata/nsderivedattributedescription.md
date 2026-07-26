---
title: NSDerivedAttributeDescription
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsderivedattributedescription
source_url: 'https://developer.apple.com/documentation/coredata/nsderivedattributedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsderivedattributedescription.json'
content_hash: 'sha256:174b4bf61e112e9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSDerivedAttributeDescription

<sub>Class</sub>

A description of an attribute that derives its value by performing a calculation on a related attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSDerivedAttributeDescription
```

## Overview

Use derived attributes to optimize fetch performance; for example:

- Create a derived `searchName` attribute to reflect a `name` attribute with case and diacritics removed for more efficient comparison.
- Create a derived `relationshipCount` attribute to reflect the number of objects in a relationship and avoid having to do a join.

Derived attributes support the following expressions:

| **Expression** | **Description** | **Example** |
|---|---|---|
| to-one keypath | A single value to replicate. | `name` or `author.name` |
| to-one keypath with a function | The result of calling a function on a single value. ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Supported functions include `canonical:`, `uppercase:`, and `lowercase:`. ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) The `canonical:` function returns a case- and diacritic-insensitive String value. | `canonical:(name)` |
| to-many keypath with a function | The result of calling an aggregate function on a set of values. ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Supported functions include `@count` and `@sum`. | `friends.@count` |
| time | The current time. | `now()` |

> [!important] Important
> Data recomputes derived attributes when you save a context. A managed object’s property does not reflect unsaved changes until you save the context and refresh the object.

## Relationships

- **Inherits From**: [NSAttributeDescription](nsattributedescription.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying the Derivation Expression

- [derivationExpression](nsderivedattributedescription/derivationexpression.md) — An expression for generating derived data.

## See Also

### Computed attributes

- [NSCompositeAttributeDescription](nscompositeattributedescription.md) — A description of an attribute that derives its value by composing other attributes.
