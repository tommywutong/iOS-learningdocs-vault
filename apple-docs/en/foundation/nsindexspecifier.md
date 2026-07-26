---
title: NSIndexSpecifier
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsindexspecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsindexspecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsindexspecifier.json'
content_hash: 'sha256:b4e16d35234c75c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSIndexSpecifier

<sub>Class</sub>

A specifier representing an object in a collection (or container) with an index number.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSIndexSpecifier
```

## Overview

The script terms `first` and `front` specify the object with index `0`, while `last` specifies the object with index of `count-1`. A negative index indicates a location by counting backward from the last object in the collection.

You don’t normally subclass `NSIndexSpecifier`.

## Relationships

- **Inherits From**: [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Index Specifiers

- [- initWithContainerClassDescription:containerSpecifier:key:index:](<nsindexspecifier/init(containerclassdescription_containerspecifier_key_index_).md>) — Initializes an allocated [NSIndexSpecifier](nsindexspecifier.md) object with a class description, container specifier, collection key, and object index.

### Accessing the Index

- [index](nsindexspecifier/index.md) — Sets the value of the receiver’s `index` property.

## See Also

### Object Specifiers

- [NSScriptObjectSpecifier](nsscriptobjectspecifier.md) — An abstract class used to represent natural language expressions.
- [NSPropertySpecifier](nspropertyspecifier.md) — A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [NSPositionalSpecifier](nspositionalspecifier.md) — A specifier for an insertion point in a container relative to another object in the container.
- [NSRandomSpecifier](nsrandomspecifier.md) — A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [NSRangeSpecifier](nsrangespecifier.md) — A specifier for a range of objects in a container.
- [NSUniqueIDSpecifier](nsuniqueidspecifier.md) — A specifier for an object in a collection (or container) by unique ID.
- [NSWhoseSpecifier](nswhosespecifier.md) — A specifier that indicates every object in a collection matching a condition.
- [NSNameSpecifier](nsnamespecifier.md) — A specifier for an object in a collection (or container) by name.
- [NSMiddleSpecifier](nsmiddlespecifier.md) — A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [NSRelativeSpecifier](nsrelativespecifier.md) — A specifier that indicates an object in a collection by its position relative to another object.
