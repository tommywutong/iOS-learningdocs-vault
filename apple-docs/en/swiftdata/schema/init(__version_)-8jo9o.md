---
title: 'init(_:version:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/schema/init(_:version:)-8jo9o'
source_url: 'https://developer.apple.com/documentation/swiftdata/schema/init(_:version:)-8jo9o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/schema/init%28_%3Aversion%3A%29-8jo9o.json'
content_hash: 'sha256:a3a5a8fd5d71f278'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Schema](../schema.md)

# init(_:version:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ types: [any PersistentModel.Type], version: Schema.Version = Version(1, 0, 0))
```

## See Also

### Creating a schema

- [init(_:version:)](<init(__version_)-8el78.md>)
- [init(versionedSchema:)](<init(versionedschema_).md>)
- [VersionedSchema](../versionedschema.md) — An interface for describing a specific version of a schema, including the models it contains.
- [init()](<init().md>)
- [Schema components](../schemacomponents.md) — Specify the constituent parts of your schema, including entities, attributes, and relationships.
