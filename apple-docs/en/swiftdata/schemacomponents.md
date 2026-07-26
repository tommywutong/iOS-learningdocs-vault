---
title: Schema components
framework: SwiftData
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/schemacomponents
source_url: 'https://developer.apple.com/documentation/swiftdata/schemacomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schemacomponents.json'
content_hash: 'sha256:696d07c159bdb3da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md) · [ModelContainer](modelcontainer.md) · [Schema](schema.md)

# Schema components

<sub>API Collection</sub>

Specify the constituent parts of your schema, including entities, attributes, and relationships.

## Topics

### Entities

- [Entity](schema/entity.md) — An object that provides a blueprint for the associated model class.

### Attributes

- [Attribute](schema/attribute.md) — An object that describes the configuration and behavior of a specific property of a model class.
- [CompositeAttribute](schema/compositeattribute.md) — An object that describes an attribute that derives its value by composing other attributes.

### Relationships

- [Relationship](schema/relationship.md) — An object that describes the configuration and behavior of a relationship between two model classes.

### Internal

- [Internal symbols](schemacomponentsinternal.md) — Restricted-use symbols that the framework requires for macro expansion and other internal tasks.

## See Also

### Creating a schema

- [init(_:version:)](<schema/init(__version_)-8el78.md>)
- [init(_:version:)](<schema/init(__version_)-8jo9o.md>)
- [init(versionedSchema:)](<schema/init(versionedschema_).md>)
- [VersionedSchema](versionedschema.md) — An interface for describing a specific version of a schema, including the models it contains.
- [init()](<schema/init().md>)
