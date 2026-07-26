---
title: NSRelativeSpecifier
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsrelativespecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsrelativespecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrelativespecifier.json'
content_hash: 'sha256:17b61f1df0fb9d82'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSRelativeSpecifier

<sub>Class</sub>

A specifier that indicates an object in a collection by its position relative to another object.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSRelativeSpecifier
```

## Overview

You don’t normally subclass `NSRelativeSpecifier`.

## Relationships

- **Inherits From**: [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a relative specifier

- [- initWithContainerClassDescription:containerSpecifier:key:relativePosition:baseSpecifier:](<nsrelativespecifier/init(containerclassdescription_containerspecifier_key_relativeposition_basespecifier_).md>) — Invokes the super class’s [- initWithContainerClassDescription:containerSpecifier:key:](<nsscriptobjectspecifier/init(containerclassdescription_containerspecifier_key_).md>) method and initializes the relative position and base specifier to `relPos` and `baseSpecifier`.

### Accessing a relative specifier

- [baseSpecifier](nsrelativespecifier/basespecifier.md) — Sets the specifier for the base object.
- [relativePosition](nsrelativespecifier/relativeposition-swift.property.md) — Sets the relative position encapsulated by the receiver.

### Constants

- [RelativePosition](nsrelativespecifier/relativeposition-swift.enum.md) — These constants are used by [relativePosition](nsrelativespecifier/relativeposition-swift.property.md) and [relativePosition](nsrelativespecifier/relativeposition-swift.property.md).

### Initializers

- [- initWithCoder:](<nsrelativespecifier/init(coder_).md>)

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
- [NSIndexSpecifier](nsindexspecifier.md) — A specifier representing an object in a collection (or container) with an index number.
