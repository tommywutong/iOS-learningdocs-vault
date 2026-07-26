---
title: Core Data model
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/core-data-model
source_url: 'https://developer.apple.com/documentation/coredata/core-data-model'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/core-data-model.json'
content_hash: 'sha256:d6ac9886c2b51ed7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# Core Data model

<sub>API Collection</sub>

Describe your app’s object structure.

## Overview

In most cases, you describe your app’s data model using Xcode’s data model editor. [NSManagedObjectModel](nsmanagedobjectmodel.md) represents the `.xcdatamodeld` file in your project’s source list. This is where you define entities that you use to generate [NSManagedObject](nsmanagedobject.md) subclasses for Core Data to manage.

The entities you create are [NSEntityDescription](nsentitydescription.md) instances. Entities’ properties are subclasses of [NSPropertyDescription](nspropertydescription.md), namely [NSAttributeDescription](nsattributedescription.md) for attributes, [NSRelationshipDescription](nsrelationshipdescription.md) for relationships, and [NSFetchedPropertyDescription](nsfetchedpropertydescription.md) for fetched properties.

The various attribute types are enumerated in [NSAttributeType](nsattributetype.md).

## Topics

### Objects and entities

- [NSManagedObject](nsmanagedobject.md) — The base class that all Core Data model objects inherit from.
- [NSEntityDescription](nsentitydescription.md) — A description of a Core Data entity.

### Standard attributes

- [NSPropertyDescription](nspropertydescription.md) — A description of a single property belonging to an entity.
- [NSAttributeDescription](nsattributedescription.md) — A description of a single attribute belonging to an entity.
- [NSAttributeType](nsattributetype.md) — The types of attribute that Core Data supports.
- [NSRelationshipDescription](nsrelationshipdescription.md) — A description of a relationship between two entities.

### Computed attributes

- [NSCompositeAttributeDescription](nscompositeattributedescription.md) — A description of an attribute that derives its value by composing other attributes.
- [NSDerivedAttributeDescription](nsderivedattributedescription.md) — A description of an attribute that derives its value by performing a calculation on a related attribute.

### Fetched properties

- [NSFetchedPropertyDescription](nsfetchedpropertydescription.md) — A description object used to define which properties are fetched from Core Data.

## See Also

### Data modeling

- [Modeling data](modeling-data.md) — Configure the data model file to contain your app’s object graph.
