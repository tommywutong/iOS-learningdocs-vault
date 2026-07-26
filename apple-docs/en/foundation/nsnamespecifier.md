---
title: NSNameSpecifier
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnamespecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsnamespecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnamespecifier.json'
content_hash: 'sha256:4ae625f7af352eb5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSNameSpecifier

<sub>Class</sub>

A specifier for an object in a collection (or container) by name.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSNameSpecifier
```

## Overview

As an example, the following script specifies both an application and a window by name. In this script, the named window’s implicitly specified container is the Finder application’s list of open windows.

```objc
tell application "Finder" -- specifies an application  by name
    close window "Reports" -- specifies a window by name
end tell
```

This specifier works only for objects that have a name property. You don’t normally subclass `NSNameSpecifier`.

The evaluation of an instance of `NSNameSpecifier` follows these steps until the specified object is found:

1. If the container implements a method whose selector matches the relevant `valueIn<Key>WithName:` pattern established by scripting key-value coding, the method is invoked. This method can potentially be very fast, and it may be relatively easy to implement.
2. As is the case when evaluating any script object specifier, the container of the specified object is given a chance to evaluate the object specifier. If the container class implements the `indicesOfObjectsByEvaluatingObjectSpecifier` method, the method is invoked. This method can potentially be very fast, but it is relatively difficult to implement.
3. An instance of  `NSWhoseSpecifier` that specifies the first object whose relevant `'pnam'` attribute matches the name is synthesized and evaluated. The instance of `NSWhoseSpecifier` must search through all of the keyed elements in the container, looking for a match. The search is potentially very slow.

## Relationships

- **Inherits From**: [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a name specifier

- [- initWithContainerClassDescription:containerSpecifier:key:name:](<nsnamespecifier/init(containerclassdescription_containerspecifier_key_name_).md>) — Invokes the super class’s [- initWithContainerClassDescription:containerSpecifier:key:](<nsscriptobjectspecifier/init(containerclassdescription_containerspecifier_key_).md>) method and then sets the name instance variable to `name`.

### Accessing a name specifier

- [name](nsnamespecifier/name.md) — Sets the name encapsulated with the receiver for the specified object in the container.

### Initializers

- [- initWithCoder:](<nsnamespecifier/init(coder_).md>)

## See Also

### Object Specifiers

- [NSScriptObjectSpecifier](nsscriptobjectspecifier.md) — An abstract class used to represent natural language expressions.
- [NSPropertySpecifier](nspropertyspecifier.md) — A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [NSPositionalSpecifier](nspositionalspecifier.md) — A specifier for an insertion point in a container relative to another object in the container.
- [NSRandomSpecifier](nsrandomspecifier.md) — A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [NSRangeSpecifier](nsrangespecifier.md) — A specifier for a range of objects in a container.
- [NSUniqueIDSpecifier](nsuniqueidspecifier.md) — A specifier for an object in a collection (or container) by unique ID.
- [NSWhoseSpecifier](nswhosespecifier.md) — A specifier that indicates every object in a collection matching a condition.
- [NSMiddleSpecifier](nsmiddlespecifier.md) — A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [NSIndexSpecifier](nsindexspecifier.md) — A specifier representing an object in a collection (or container) with an index number.
- [NSRelativeSpecifier](nsrelativespecifier.md) — A specifier that indicates an object in a collection by its position relative to another object.
