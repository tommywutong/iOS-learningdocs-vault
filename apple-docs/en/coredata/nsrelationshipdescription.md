---
title: NSRelationshipDescription
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsrelationshipdescription
source_url: 'https://developer.apple.com/documentation/coredata/nsrelationshipdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsrelationshipdescription.json'
content_hash: 'sha256:505da24f03da62ac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSRelationshipDescription

<sub>Class</sub>

A description of a relationship between two entities.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSRelationshipDescription
```

## Overview

[NSRelationshipDescription](nsrelationshipdescription.md) provides additional attributes that are specific to modeling a relationship between two entities. For the common attributes of all property types, see [NSPropertyDescription](nspropertydescription.md).

For example, use this class to define a relationship’s _cardinality_ — the number of managed objects the relationship can reference.

- For a to-one relationship, set [maxCount](nsrelationshipdescription/maxcount.md) to `1`.
- For a to-many relationship, set [maxCount](nsrelationshipdescription/maxcount.md) to a number greater than `1` to impose an upper limit; otherwise, use `0` to allow an unlimited number of referenced objects.

At runtime, you can modify a relationship description until you associate its owning managed object model with a persistent store coordinator.  If you attempt to modify the model after you associate it, Core Data throws an exception. To modify a model that’s in use, create and modify a copy and then discard any objects that belong to the original model.

## Relationships

- **Inherits From**: [NSPropertyDescription](nspropertydescription.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the Destination

- [inverseRelationship](nsrelationshipdescription/inverserelationship.md) — The relationship that represents the inverse of the current relationship.
- [destinationEntity](nsrelationshipdescription/destinationentity.md) — The type of object the relationship contains.
- [ordered](nsrelationshipdescription/isordered.md) — A Boolean value that determines whether the relationship preserves the order of the referenced managed objects.

### Configuring Cardinality

- [toMany](nsrelationshipdescription/istomany.md) — Returns a Boolean value that indicates whether the relationship can contain many managed objects.
- [minCount](nsrelationshipdescription/mincount.md) — The minimum number of managed objects the relationship can reference.
- [maxCount](nsrelationshipdescription/maxcount.md) — The maximum number of managed objects the relationship can reference.

### Configuring Delete Behavior

- [deleteRule](nsrelationshipdescription/deleterule.md) — The rule to apply when you delete the relationship’s owning managed object.
- [NSDeleteRule](nsdeleterule.md) — Constants that determine what happens when you delete a relationship’s owning managed object.

### Getting Version Data

- [versionHash](nsrelationshipdescription/versionhash.md) — The relationship’s unique identity.

## See Also

### Standard attributes

- [NSPropertyDescription](nspropertydescription.md) — A description of a single property belonging to an entity.
- [NSAttributeDescription](nsattributedescription.md) — A description of a single attribute belonging to an entity.
- [NSAttributeType](nsattributetype.md) — The types of attribute that Core Data supports.
