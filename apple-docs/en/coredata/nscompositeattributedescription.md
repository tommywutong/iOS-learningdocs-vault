---
title: NSCompositeAttributeDescription
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nscompositeattributedescription
source_url: 'https://developer.apple.com/documentation/coredata/nscompositeattributedescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nscompositeattributedescription.json'
content_hash: 'sha256:221f31c992d7275c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSCompositeAttributeDescription

<sub>Class</sub>

A description of an attribute that derives its value by composing other attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSCompositeAttributeDescription
```

## Overview

Composite attributes enable you to define and store complex data types, and then query, index, and apply constraints to those types. Model classes use dictionaries to represent those composites in-memory, where each dictionary contains keys corresponding to the names of the underlying attributes. You may use composite attributes anywhere you use standard attributes, including lightweight migrations and CloudKit, through [NSPersistentCloudKitContainer](nspersistentcloudkitcontainer.md). You can even nest composites inside other composites to create complex object hierarchies without additional model classes.

> [!note] Note
> Composite attributes are available only to persistent stores that you configure with the [sqlite](nspersistentstore/storetype/sqlite.md) store type.

In most scenarios, prefer to use Xcode’s model editor to add composite attributes to your entities and then regenerate your model classes. However, if you need to create composites dynamically at runtime, create an instance of this class and populate its [elements](nscompositeattributedescription/elements.md) property with the necessary attribute descriptions.

You can access a composite’s underlying attributes using namespaced key paths and property-like setters and getters, as the following example demonstrates:

```swift
// A model class that represents the Quake entity.
class Quake: NSManagedObject {
    @NSManaged var code: String?
    @NSManaged var place: String?
    @NSManaged var date: Date?

    // A composite attribute that uses a dictionary for its in-memory storage.
    @NSManaged var magnitude: [String: Any]?
}

// Use namespaced key paths to access a composite's indvidual attributes.
let request = NSFetchRequest(entityName: "Quake")
request.predicate = NSPredicate(format: "magnitude.richter > 4.5")

// Use property-like setters and getters to manage the underlying attributes directly.
quake.magnitude.richter = 4.6
print(quake.magnitude.richter)

```

## Relationships

- **Inherits From**: [NSAttributeDescription](nsattributedescription.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Composing attributes

- [elements](nscompositeattributedescription/elements.md) — The composed attribute descriptions.

## See Also

### Computed attributes

- [NSDerivedAttributeDescription](nsderivedattributedescription.md) — A description of an attribute that derives its value by performing a calculation on a related attribute.
