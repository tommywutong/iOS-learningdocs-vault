---
title: NSRangeSpecifier
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsrangespecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsrangespecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrangespecifier.json'
content_hash: 'sha256:8e955299bd17473c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSRangeSpecifier

<sub>Class</sub>

A specifier for a range of objects in a container.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSRangeSpecifier
```

## Overview

An `NSRangeSpecifier` object specifies a range (that is, an uninterrupted series) of objects in a container through two delimiting objects. The range is represented by two object specifiers, a start specifier and an end specifier, which can be of any specifier type (such as [NSIndexSpecifier](nsindexspecifier.md) or [NSWhoseSpecifier](nswhosespecifier.md) object). These specifiers are evaluated in the context of the same container object as the range specifier itself.

You don’t normally subclass `NSRangeSpecifier`.

## Relationships

- **Inherits From**: [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a range specifier

- [- initWithContainerClassDescription:containerSpecifier:key:startSpecifier:endSpecifier:](<nsrangespecifier/init(containerclassdescription_containerspecifier_key_start_end_).md>) — Returns a range specifier initialized with the given properties.

### Accessing a range specifier

- [endSpecifier](nsrangespecifier/endspecifier.md) — Sets the object specifier representing the last object of the range to a given object.
- [startSpecifier](nsrangespecifier/startspecifier.md) — Returns the object specifier representing the first object of the range.

### Initializers

- [- initWithCoder:](<nsrangespecifier/init(coder_).md>)
- [init(containerClassDescription:containerSpecifier:key:startSpecifier:endSpecifier:)](<nsrangespecifier/init(containerclassdescription_containerspecifier_key_startspecifier_endspecifier_).md>)

## See Also

### Object Specifiers

- [NSScriptObjectSpecifier](nsscriptobjectspecifier.md) — An abstract class used to represent natural language expressions.
- [NSPropertySpecifier](nspropertyspecifier.md) — A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [NSPositionalSpecifier](nspositionalspecifier.md) — A specifier for an insertion point in a container relative to another object in the container.
- [NSRandomSpecifier](nsrandomspecifier.md) — A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [NSUniqueIDSpecifier](nsuniqueidspecifier.md) — A specifier for an object in a collection (or container) by unique ID.
- [NSWhoseSpecifier](nswhosespecifier.md) — A specifier that indicates every object in a collection matching a condition.
- [NSNameSpecifier](nsnamespecifier.md) — A specifier for an object in a collection (or container) by name.
- [NSMiddleSpecifier](nsmiddlespecifier.md) — A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [NSIndexSpecifier](nsindexspecifier.md) — A specifier representing an object in a collection (or container) with an index number.
- [NSRelativeSpecifier](nsrelativespecifier.md) — A specifier that indicates an object in a collection by its position relative to another object.
