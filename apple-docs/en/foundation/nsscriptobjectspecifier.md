---
title: NSScriptObjectSpecifier
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier.json'
content_hash: 'sha256:3e73724ec5741c15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSScriptObjectSpecifier

<sub>Class</sub>

An abstract class used to represent natural language expressions.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSScriptObjectSpecifier
```

## Overview

`NSScriptObjectSpecifier` is the abstract superclass for classes that instantiate objects called “object specifiers.” An object specifier represents an AppleScript reference form, which is a natural-language expression such as `words 10 through 20` or `front document` or `words whose color is red`.

The scripting system maps these words or phrases to attributes and relationships of scriptable objects. A reference form rarely occurs in isolation; usually a script statement consists of a series of reference forms preceded by a command and typically connected to each other by `of`, such as:

```objc
get words whose color is blue of paragraph 10 of front document
```

The expression `words whose color is blue of paragraph 10 of front document` specifies a location in the application’s AppleScript object model—the objects the application makes available to scripters. The classes of objects in the object model often closely match the classes of actual objects in the application, but they are not required to. An object specifier locates objects in the running application that correspond to the specified object model objects.

Your application typically creates object specifiers when it implements the `objectSpecifier` method for its scriptable classes. That method is defined by the NSScriptObjectSpecifiers protocol.

It is unlikely that you would ever need to create your own subclass of `NSScriptObjectSpecifier`; the set of valid AppleScript reference forms is determined by Apple Computer and object specifier classes are already implemented for this set. If for some reason you do need to create a subclass, you must override the primitive method [- indicesOfObjectsByEvaluatingWithContainer:count:](<nsscriptobjectspecifier/indicesofobjectsbyevaluating(withcontainer_count_).md>) to return indices to the elements within the container whose values are matched with the child specifier’s key. In addition, you probably need to declare any special instance variables and implement an initializer that invokes super’s designated initializer, [- initWithContainerClassDescription:containerSpecifier:key:](<nsscriptobjectspecifier/init(containerclassdescription_containerspecifier_key_).md>), and initializes these variables.

For a comprehensive treatment of object specifiers, including sample code, see [Object Specifiers](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_object_specifiers/SAppsObjectSpecifiers.html#//apple_ref/doc/uid/TP40002164-CH3) in [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSIndexSpecifier](nsindexspecifier.md), [NSMiddleSpecifier](nsmiddlespecifier.md), [NSNameSpecifier](nsnamespecifier.md), [NSPropertySpecifier](nspropertyspecifier.md), [NSRandomSpecifier](nsrandomspecifier.md), [NSRangeSpecifier](nsrangespecifier.md), [NSRelativeSpecifier](nsrelativespecifier.md), [NSUniqueIDSpecifier](nsuniqueidspecifier.md), [NSWhoseSpecifier](nswhosespecifier.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Obtaining an object specifier for a descriptor

- [+ objectSpecifierWithDescriptor:](<nsscriptobjectspecifier/init(descriptor_).md>) — Returns a new object specifier for an Apple event descriptor.

### Initializing an object specifier

- [- initWithContainerClassDescription:containerSpecifier:key:](<nsscriptobjectspecifier/init(containerclassdescription_containerspecifier_key_).md>) — Returns an `NSScriptObjectSpecifier` object initialized with the given attributes.
- [- initWithContainerSpecifier:key:](<nsscriptobjectspecifier/init(containerspecifier_key_).md>) — Returns an `NSScriptObjectSpecifier` object initialized with a given container specifier  and key.

### Evaluating an object specifier

- [- indicesOfObjectsByEvaluatingWithContainer:count:](<nsscriptobjectspecifier/indicesofobjectsbyevaluating(withcontainer_count_).md>) — This primitive method must be overridden by subclasses to return a pointer to an array of indices identifying objects in the key of a given container that are identified by the receiver of the message.
- [objectsByEvaluatingSpecifier](nsscriptobjectspecifier/objectsbyevaluatingspecifier.md) — Returns the actual object represented by the nested series of object specifiers.
- [- objectsByEvaluatingWithContainers:](<nsscriptobjectspecifier/objectsbyevaluating(withcontainers_).md>) — Returns the actual object or objects specified by the receiver as evaluated in the context of given container object.

### Getting, testing, and setting containers

- [containerClassDescription](nsscriptobjectspecifier/containerclassdescription.md) — Sets the class description of the receiver’s container specifier to a given specifier.
- [containerIsObjectBeingTested](nsscriptobjectspecifier/containerisobjectbeingtested.md) — Sets whether the receiver’s container should be an object involved in a filter reference or the top-level object.
- [containerIsRangeContainerObject](nsscriptobjectspecifier/containerisrangecontainerobject.md) — Sets whether the receiver’s container is to be the container for a range specifier or a top-level object.
- [containerSpecifier](nsscriptobjectspecifier/container.md) — Sets the container specifier of the receiver.

### Getting and setting child references

- [childSpecifier](nsscriptobjectspecifier/child.md) — Sets the receiver’s child reference.

### Getting and setting object keys

- [key](nsscriptobjectspecifier/key.md) — Sets the key of the receiver.
- [keyClassDescription](nsscriptobjectspecifier/keyclassdescription.md) — Returns the class description of the objects specified by the receiver.

### Getting evaluation errors

- [evaluationErrorSpecifier](nsscriptobjectspecifier/evaluationerror.md) — Returns the object specifier in which an evaluation error occurred.
- [evaluationErrorNumber](nsscriptobjectspecifier/evaluationerrornumber.md) — Sets the value of the evaluation error.

### Getting a descriptor for the object specifier

- [descriptor](nsscriptobjectspecifier/descriptor.md) — Returns an Apple event descriptor that represents the receiver.

### Constants

- [NSScriptObjectSpecifier—Specifier Evaluation Errors](specifier-evaluation-errors.md) — `NSScriptObjectSpecifier` provides the following constants for error codes for specific problems evaluating specifiers:

### Initializers

- [- initWithCoder:](<nsscriptobjectspecifier/init(coder_).md>)

## See Also

### Object Specifiers

- [NSPropertySpecifier](nspropertyspecifier.md) — A specifier for a simple attribute value, a one-to-one relationship, or all elements of a to-many relationship.
- [NSPositionalSpecifier](nspositionalspecifier.md) — A specifier for an insertion point in a container relative to another object in the container.
- [NSRandomSpecifier](nsrandomspecifier.md) — A specifier for an arbitrary object in a collection or, if not a one-to-many relationship, the sole object.
- [NSRangeSpecifier](nsrangespecifier.md) — A specifier for a range of objects in a container.
- [NSUniqueIDSpecifier](nsuniqueidspecifier.md) — A specifier for an object in a collection (or container) by unique ID.
- [NSWhoseSpecifier](nswhosespecifier.md) — A specifier that indicates every object in a collection matching a condition.
- [NSNameSpecifier](nsnamespecifier.md) — A specifier for an object in a collection (or container) by name.
- [NSMiddleSpecifier](nsmiddlespecifier.md) — A specifier indicating the middle object in a collection or, if not a one-to-many relationship, the sole object.
- [NSIndexSpecifier](nsindexspecifier.md) — A specifier representing an object in a collection (or container) with an index number.
- [NSRelativeSpecifier](nsrelativespecifier.md) — A specifier that indicates an object in a collection by its position relative to another object.
