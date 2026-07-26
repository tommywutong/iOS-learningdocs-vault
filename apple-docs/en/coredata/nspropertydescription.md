---
title: NSPropertyDescription
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspropertydescription
source_url: 'https://developer.apple.com/documentation/coredata/nspropertydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspropertydescription.json'
content_hash: 'sha256:097af93170726074'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPropertyDescription

<sub>Class</sub>

A description of a single property belonging to an entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPropertyDescription
```

## Overview

A property describes a single value within an object managed by the Core Data Framework. There are different types of property, each represented by a subclass which encapsulates the specific property behavior—see [NSAttributeDescription](nsattributedescription.md), [NSRelationshipDescription](nsrelationshipdescription.md), and [NSFetchedPropertyDescription](nsfetchedpropertydescription.md).

Note that a property name cannot be the same as any no-parameter method name of `NSObject` or `NSManagedObject`. For example, you cannot give a property the name “description”. There are hundreds of methods on `NSObject` which may conflict with property names—and this list can grow without warning from frameworks or other libraries. You should avoid very general words (like “font”, and “color”) and words or phrases which overlap with Cocoa paradigms (such as “isEditing” and “objectSpecifier”).

Properties—relationships as well as attributes—may be transient. A managed object context knows about transient properties and tracks changes made to them. Transient properties are ignored by the persistent store, and not just during saves: you cannot fetch using a predicate based on transients (although you can use transient properties to filter in memory yourself).

### Editing Property Descriptions

Property descriptions are editable until they are used by an object graph manager (such as a persistent store coordinator). This allows you to create or modify them dynamically. However, once a description is used (when the managed object model to which it belongs is associated with a persistent store coordinator), it _must not_ (indeed cannot) be changed. This is enforced at runtime: any attempt to mutate a model or any of its sub-objects after the model is associated with a persistent store coordinator causes an exception to be thrown. If you need to modify a model that is in use, create a copy, modify the copy, and then discard the objects with the old model.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSAttributeDescription](nsattributedescription.md), [NSExpressionDescription](nsexpressiondescription.md), [NSFetchedPropertyDescription](nsfetchedpropertydescription.md), [NSRelationshipDescription](nsrelationshipdescription.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing Features of a Property

- [entity](nspropertydescription/entity.md) — The entity description of the receiver.
- [indexed](nspropertydescription/isindexed.md) — A Boolean value that indicates whether the receiver should be indexed for searching. _(deprecated)_
- [optional](nspropertydescription/isoptional.md) — A Boolean value that indicates whether the receiver is optional.
- [transient](nspropertydescription/istransient.md) — A Boolean value that indicates whether the receiver is transient.
- [name](nspropertydescription/name.md) — The name of the receiver.
- [userInfo](nspropertydescription/userinfo.md) — The user info dictionary of the receiver.

### Supporting Validation

- [validationPredicates](nspropertydescription/validationpredicates.md) — The validation predicates of the receiver.
- [validationWarnings](nspropertydescription/validationwarnings.md) — The error strings associated with the receiver’s validation predicates.
- [- setValidationPredicates:withValidationWarnings:](<nspropertydescription/setvalidationpredicates(__withvalidationwarnings_).md>) — Sets the validation predicates and warnings of the receiver.

### Supporting Versioning

- [versionHash](nspropertydescription/versionhash.md) — The version hash for the receiver.
- [versionHashModifier](nspropertydescription/versionhashmodifier.md) — The version hash modifier for the receiver.
- [renamingIdentifier](nspropertydescription/renamingidentifier.md) — The renaming identifier for the receiver.

### Specifying Spotlight Support

- [indexedBySpotlight](nspropertydescription/isindexedbyspotlight.md) — A Boolean value that indicates whether Core Data adds the property’s value to the Core Spotlight index.
- [storedInExternalRecord](nspropertydescription/isstoredinexternalrecord.md) — A Boolean value that indicates whether to write the property’s data in an external record file that corresponds to the managed object. _(deprecated)_

### Initializers

- [init(coder:)](<nspropertydescription/init(coder_).md>)

## See Also

### Standard attributes

- [NSAttributeDescription](nsattributedescription.md) — A description of a single attribute belonging to an entity.
- [NSAttributeType](nsattributetype.md) — The types of attribute that Core Data supports.
- [NSRelationshipDescription](nsrelationshipdescription.md) — A description of a relationship between two entities.
