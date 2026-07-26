---
title: NSWhoseSpecifier
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nswhosespecifier
source_url: 'https://developer.apple.com/documentation/foundation/nswhosespecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nswhosespecifier.json'
content_hash: 'sha256:ada4c77640cf77a8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSWhoseSpecifier

<sub>Class</sub>

A specifier that indicates every object in a collection matching a condition.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSWhoseSpecifier
```

## Overview

`NSWhoseSpecifier` specifies every object in a collection (or every element in a container) that matches the condition defined by a single Boolean expression or multiple Boolean expressions connected by logical operators. `NSWhoseSpecifier` is unique among object specifiers in that its top-level container is typically not the application object but an evaluated object specifier involved in the tested-for condition. An `NSWhoseSpecifier` object encapsulates a “test” object for defining this condition. A test object is instantiated from a subclass of the abstract [NSScriptWhoseTest](nsscriptwhosetest.md) class, whose one declared method is [- isTrue](<nsscriptwhosetest/istrue().md>). See “Boolean Expressions and Logical Operations” in [NSScriptObjectSpecifier](nsscriptobjectspecifier.md) and the descriptions in NSComparisonMethods and NSScriptingComparisonMethods for more information.

The set of elements specified by an `NSWhoseSpecifier` object can be a subset of those that pass the `NSWhoseSpecifier` object’s test. This subset is specified by the various sub-element properties of the `NSWhoseSpecifier` object . Consider as an example the specifier `paragraphs where color of third word is blue`. This would be represented by an `NSWhoseSpecifier` object  that uses a test specifier and another object specifier to identify a subset of the objects with the specified property. That is, the specifier’s property is `paragraphs`; the test specifier is an index specifier with property `words` and `index 3`; and the qualifier is a key value qualifier for key `color` and value `[NSColor blueColor]`. The test object specifier (`word at index 3`) is evaluated for each object (paragraph) using that object as the container; the resulting objects (if any) are tested with the qualifier (`color blue`).

`NSWhoseSpecifier` is part of Cocoa’s built-in script handling. You don’t normally subclass it.

## Relationships

- **Inherits From**: [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a whose specifier

- [- initWithContainerClassDescription:containerSpecifier:key:test:](<nswhosespecifier/init(containerclassdescription_containerspecifier_key_test_).md>) — Returns an `NSWhoseSpecifier` object initialized with the given attributes.

### Accessing information about a whose specifier

- [endSubelementIdentifier](nswhosespecifier/endsubelementidentifier.md) — Sets the end sub-element identifier for the specifier to the value of a given sub-element.
- [endSubelementIndex](nswhosespecifier/endsubelementindex.md) — Sets the index position of the last sub-element within the range of objects being tested that pass the specifier’s test.
- [startSubelementIdentifier](nswhosespecifier/startsubelementidentifier.md) — Returns the start sub-element identifier for the receiver.
- [startSubelementIndex](nswhosespecifier/startsubelementindex.md) — Returns the index position of the first sub-element within the range of objects being tested that pass the receiver’s test.
- [test](nswhosespecifier/test.md) — Returns the test object encapsulated by the receiver.

### Constants

- [SubelementIdentifier](nswhosespecifier/subelementidentifier.md) — `NSWhoseSpecifier` uses these constants to specify sub-elements within the collection of objects being tested that pass the specifier’s test.

### Initializers

- [- initWithCoder:](<nswhosespecifier/init(coder_).md>)

## See Also

### Object Specifiers

- [NSScriptObjectSpecifier](nsscriptobjectspecifier.md) — An abstract class used to represent natural language expressions.
- [NSPropertySpecifier](nspropertyspecifier.md) — A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [NSPositionalSpecifier](nspositionalspecifier.md) — A specifier for an insertion point in a container relative to another object in the container.
- [NSRandomSpecifier](nsrandomspecifier.md) — A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [NSRangeSpecifier](nsrangespecifier.md) — A specifier for a range of objects in a container.
- [NSUniqueIDSpecifier](nsuniqueidspecifier.md) — A specifier for an object in a collection (or container) by unique ID.
- [NSNameSpecifier](nsnamespecifier.md) — A specifier for an object in a collection (or container) by name.
- [NSMiddleSpecifier](nsmiddlespecifier.md) — A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [NSIndexSpecifier](nsindexspecifier.md) — A specifier representing an object in a collection (or container) with an index number.
- [NSRelativeSpecifier](nsrelativespecifier.md) — A specifier that indicates an object in a collection by its position relative to another object.
