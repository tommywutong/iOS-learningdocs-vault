---
title: NSClassDescription
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsclassdescription
source_url: 'https://developer.apple.com/documentation/foundation/nsclassdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsclassdescription.json'
content_hash: 'sha256:4fc71081707efacb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSClassDescription

<sub>Class</sub>

An abstract class that provides the interface for querying the relationships and properties of a class.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSClassDescription
```

## Overview

Concrete subclasses of `NSClassDescription` provide the available attributes of objects of a particular class and the relationships between that class and other classes. Defining these relationships between classes allows for more intelligent and flexible manipulation of objects with key-value coding.

It is important to note that there are no class descriptions by default. To use `NSClassDescription` objects in your code you have to implement them for your model classes. For all concrete subclasses, you must provide implementations for all instance methods of `NSClassDescription`. (`NSClassDescription` provides only the implementation for the class methods that maintain the cache of registered class descriptions.) Once created, you must register a class description with the `NSClassDescription` method [+ registerClassDescription:forClass:](<nsclassdescription/register(__for_).md>).

You can use the `NSString` objects in the arrays returned by methods such as [attributeKeys](nsclassdescription/attributekeys.md) and [toManyRelationshipKeys](nsclassdescription/tomanyrelationshipkeys.md)  to access—using key-value coding—the properties of an instance of the class to which a class description object corresponds. For more about attributes and relationships, see Cocoa Fundamentals Guide. For more about key-value coding, see [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).

[NSScriptClassDescription](nsscriptclassdescription.md), which is used to map the relationships between scriptable classes, is the only concrete subclass of `NSClassDescription` provided as part of the Cocoa framework.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSScriptClassDescription](nsscriptclassdescription.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Working with class descriptions

- [+ classDescriptionForClass:](<nsclassdescription/init(for_).md>) — Returns the class description for a given class.
- [+ invalidateClassDescriptionCache](<nsclassdescription/invalidateclassdescriptioncache().md>) — Removes all `NSClassDescription` objects from the cache.
- [+ registerClassDescription:forClass:](<nsclassdescription/register(__for_).md>) — Registers an `NSClassDescription` object for a given class in the `NSClassDescription` cache.

### Attribute keys

- [attributeKeys](nsclassdescription/attributekeys.md) — Overridden by subclasses to return the names of attributes of instances of the described class.

### Relationship keys

- [- inverseForRelationshipKey:](<nsclassdescription/inverse(forrelationshipkey_).md>) — Overridden by subclasses to return the name of the inverse relationship from a relationship specified by a given key.
- [toManyRelationshipKeys](nsclassdescription/tomanyrelationshipkeys.md) — Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.
- [toOneRelationshipKeys](nsclassdescription/toonerelationshipkeys.md) — Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.

### Notifications

- [NSClassDescriptionNeededForClassNotification](nsnotification/name-swift.struct/nsclassdescriptionneededforclass.md) — Posted by [+ classDescriptionForClass:](<nsclassdescription/init(for_).md>) when a class description cannot be found for a class.

### Initializers

- [init(forClass:)](<nsclassdescription/init(forclass_).md>)

## See Also

### Script Dictionary Description

- [NSScriptSuiteRegistry](nsscriptsuiteregistry.md) — The top-level repository of scriptability information for an app at runtime.
- [NSScriptClassDescription](nsscriptclassdescription.md) — A scriptable class that a macOS app supports.
- [NSScriptCommandDescription](nsscriptcommanddescription.md) — A script command that a macOS app supports.
