---
title: NSUniqueIDSpecifier
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuniqueidspecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsuniqueidspecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuniqueidspecifier.json'
content_hash: 'sha256:8a47174f0fcd4e87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSUniqueIDSpecifier

<sub>Class</sub>

A specifier for an object in a collection (or container) by unique ID.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSUniqueIDSpecifier
```

## Overview

This specifier works only for objects that have an ID property. The unique ID object passed to an instance of  `NSUniqueIDSpecifier` must be either an `NSNumber` object or an `NSString` object. The exact type should match the scripting dictionary declaration of the ID attribute for the relevant scripting class.

You can expect that the ID property will be _read only_ for any object that supports it. Therefore a scripter can obtain the unique ID for an object and refer to the object by the ID, but cannot set the unique ID.

You don’t normally subclass `NSUniqueIDSpecifier`.

The evaluation of `NSUniqueIDSpecifier` objects follows these steps until the specified object is found:

1. If the container implements a method whose selector matches the relevant `valueIn<Key>WithUniqueID:` pattern established by scripting key-value coding, the method is invoked. This method can potentially be very fast, and it may be relatively easy to implement.
2. As is the case when evaluating any script object specifier, the container of the specified object is given a chance to evaluate the object specifier. If the container class implements the [indicesOfObjects(byEvaluatingObjectSpecifier:)](<../objectivec/nsobject-swift.class/indicesofobjects(byevaluatingobjectspecifier_).md>) method, the method is invoked. This method can potentially be very fast, but it is relatively difficult to implement.
3. An [NSWhoseSpecifier](nswhosespecifier.md) object that specifies the first object whose relevant `'ID  '` attribute matches the ID is synthesized and evaluated. The `NSWhoseSpecifier` object must search through all of the keyed elements in the container, looking for a match. The search is potentially very slow.

## Relationships

- **Inherits From**: [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a unique ID specifier

- [- initWithContainerClassDescription:containerSpecifier:key:uniqueID:](<nsuniqueidspecifier/init(containerclassdescription_containerspecifier_key_uniqueid_).md>) — Returns an `NSUniqueIDSpecifier` object, initialized with the given arguments.

### Accessing unique ID information

- [uniqueID](nsuniqueidspecifier/uniqueid.md) — Returns the ID encapsulated by the receiver.

### Initializers

- [- initWithCoder:](<nsuniqueidspecifier/init(coder_).md>)

## See Also

### Object Specifiers

- [NSScriptObjectSpecifier](nsscriptobjectspecifier.md) — An abstract class used to represent natural language expressions.
- [NSPropertySpecifier](nspropertyspecifier.md) — A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [NSPositionalSpecifier](nspositionalspecifier.md) — A specifier for an insertion point in a container relative to another object in the container.
- [NSRandomSpecifier](nsrandomspecifier.md) — A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [NSRangeSpecifier](nsrangespecifier.md) — A specifier for a range of objects in a container.
- [NSWhoseSpecifier](nswhosespecifier.md) — A specifier that indicates every object in a collection matching a condition.
- [NSNameSpecifier](nsnamespecifier.md) — A specifier for an object in a collection (or container) by name.
- [NSMiddleSpecifier](nsmiddlespecifier.md) — A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [NSIndexSpecifier](nsindexspecifier.md) — A specifier representing an object in a collection (or container) with an index number.
- [NSRelativeSpecifier](nsrelativespecifier.md) — A specifier that indicates an object in a collection by its position relative to another object.
