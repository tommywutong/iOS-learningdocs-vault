---
title: VersionedSchema
framework: SwiftData
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/versionedschema
source_url: 'https://developer.apple.com/documentation/swiftdata/versionedschema'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/versionedschema.json'
content_hash: 'sha256:10ca42bda7eb3838'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# VersionedSchema

<sub>Protocol</sub>

An interface for describing a specific version of a schema, including the models it contains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol VersionedSchema : SendableMetatype
```

## Relationships

- **Inherits From**: [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Describing the version

- [versionIdentifier](versionedschema/versionidentifier.md) — The textual description of the migration’s version or purpose.

### Specifying the included models

- [models](versionedschema/models.md) — The models to include in this version of the schema.

## See Also

### Creating a schema

- [init(_:version:)](<schema/init(__version_)-8el78.md>)
- [init(_:version:)](<schema/init(__version_)-8jo9o.md>)
- [init(versionedSchema:)](<schema/init(versionedschema_).md>)
- [init()](<schema/init().md>)
- [Schema components](schemacomponents.md) — Specify the constituent parts of your schema, including entities, attributes, and relationships.
