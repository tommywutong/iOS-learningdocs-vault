---
title: NSEntityDescription
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsentitydescription
source_url: 'https://developer.apple.com/documentation/coredata/nsentitydescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsentitydescription.json'
content_hash: 'sha256:42f0dfe3f086cec8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSEntityDescription

<sub>Class</sub>

A description of a Core Data entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSEntityDescription
```

## Overview

Entities are to managed objects what `Class` is to `id`, or — to use a database analogy — what tables are to rows. An instance specifies the entity’s name, its attributes and relationships (as instances of [NSAttributeDescription](nsattributedescription.md) and [NSRelationshipDescription](nsrelationshipdescription.md)) and the class that represents it. Instances of that class correspond to entries in the associated persistent store. As a minimum, an entity description requires:

- A name.
- The class name of the corresponding managed object.

If you don’t specify a class name, the framework uses [NSManagedObject](nsmanagedobject.md).

You define entities in a managed object model (an instance of [NSManagedObjectModel](nsmanagedobjectmodel.md)) using Xcode’s data modeling tool. Core Data uses `NSEntityDescription` to map entries in the persistent store to managed objects in your app. It’s unlikely you’ll interact with entity descriptions directly unless you’re specifically working with models. `NSEntityDescription` provides a user dictionary for you to store any related, app-specific information.

### Editing entity descriptions

Entity descriptions are editable until an object graph manager uses them, which allows you to create or modify descriptions dynamically. However, once you associate the description’s managed object model with a persistent store coordinator, you can no longer modify it. The framework enforces this rule at runtime; any attempt to mutate the model, or any of its child objects, after you associate it with a persistent store coordinator results in an exception. If you need to modify a model that’s in use, create a copy of that model, modify it, and then discard the stale model.

If you want to create an entity hierarchy, consider the relevant API. You can only set an entity’s [subentities](nsentitydescription/subentities.md), not an entity’s super-entity. To set an entity’s super-entity, set an array of subentities on the super entity that includes the desired entity; the entity hierarchy is built top-down.

### Using entity descriptions in dictionaries

The `copy` method of `NSEntityDescription` returns an entity such that:

```objc
[[entity copy] isEqual:entity] == NO
```

Since [NSDictionary](../foundation/nsdictionary.md) copies its keys and requires that keys both conform to the [NSCopying](../foundation/nscopying.md) protocol and have a property that `copy` returns an object for where the source and the copy are equal, don’t use entities as keys in a dictionary. Instead, use either the entity’s name as the key or use an [NSMapTable](../foundation/nsmaptable.md) with retain callbacks.

### Fast enumeration

`NSEntityDescription` implements the [NSFastEnumeration](../foundation/nsfastenumeration.md) protocol. Use this to enumerate over an entity’s properties, as the following example illustrates.

```objc
NSEntityDescription *anEntity = ...;
for (NSPropertyDescription *property in anEntity) {
    // property is each instance of NSPropertyDescription in anEntity in turn
}
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSFastEnumeration](../foundation/nsfastenumeration.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting descriptive information

- [name](nsentitydescription/name.md) — The entity name of the receiver.
- [managedObjectModel](nsentitydescription/managedobjectmodel.md) — The managed object model with which the receiver is associated.
- [managedObjectClassName](nsentitydescription/managedobjectclassname.md) — The name of the class that represents the receiver’s entity.
- [renamingIdentifier](nsentitydescription/renamingidentifier.md) — The renaming identifier for the receiver.
- [abstract](nsentitydescription/isabstract.md) — A Boolean value that indicates whether the receiver represents an abstract entity.
- [userInfo](nsentitydescription/userinfo.md) — The user info dictionary of the receiver.
- [coreSpotlightDisplayNameExpression](nsentitydescription/corespotlightdisplaynameexpression.md) — The expression that computes the CoreSpotlight display name for instances of the entity.

### Managing inheritance

- [subentitiesByName](nsentitydescription/subentitiesbyname.md) — A dictionary containing the receiver’s sub-entities.
- [subentities](nsentitydescription/subentities.md) — An array containing the sub-entities of the receiver.
- [superentity](nsentitydescription/superentity.md) — The super-entity of the receiver.
- [- isKindOfEntity:](<nsentitydescription/iskindof(entity_).md>) — Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.

### Working with properties

- [propertiesByName](nsentitydescription/propertiesbyname.md) — A dictionary containing the properties of the receiver.
- [properties](nsentitydescription/properties.md) — An array containing the properties of the receiver.
- [attributesByName](nsentitydescription/attributesbyname.md) — The attributes of the receiver in a dictionary.
- [relationshipsByName](nsentitydescription/relationshipsbyname.md) — The relationships of the receiver in a dictionary.
- [- relationshipsWithDestinationEntity:](<nsentitydescription/relationships(fordestination_).md>) — Returns an array containing the relationships of the receiver where the entity description of the relationship is a given entity.

### Configuring indexes and constraints

- [indexes](nsentitydescription/indexes.md) — An array of fetch index descriptions for the entity.
- [uniquenessConstraints](nsentitydescription/uniquenessconstraints.md) — An array of arrays that contains one or more attributes with a value that must be unique over the instances of that entity.
- [compoundIndexes](nsentitydescription/compoundindexes.md) — The compound indexes for the entity as an array of arrays. _(deprecated)_

### Creating a managed object

- [+ insertNewObjectForEntityForName:inManagedObjectContext:](<nsentitydescription/insertnewobject(forentityname_into_).md>) — Creates, configures, and returns an instance of the class for the entity with a given name.

### Retrieving a description by its name

- [+ entityForName:inManagedObjectContext:](<nsentitydescription/entity(forentityname_in_).md>) — Returns the entity with the specified name from the managed object model associated with the specified managed object context’s persistent store coordinator.

### Managing versioning

- [versionHash](nsentitydescription/versionhash.md) — The version hash for the receiver.
- [versionHashModifier](nsentitydescription/versionhashmodifier.md) — The version hash modifier for the receiver.

### Initializers

- [init(coder:)](<nsentitydescription/init(coder_).md>)

## See Also

### Objects and entities

- [NSManagedObject](nsmanagedobject.md) — The base class that all Core Data model objects inherit from.
