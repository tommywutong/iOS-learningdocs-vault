---
title: schema
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontainer/schema
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontainer/schema'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontainer/schema.json'
content_hash: 'sha256:1990ca95e97f1da8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContainer](../modelcontainer.md)

# schema

<sub>Instance Property</sub>

The schema that maps your app’s model classes to the associated data in the app’s persistent storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let schema: Schema
```

## Discussion

This property provides a reference to the schema you specified when calling one the container’s initializers.

## See Also

### Managing schema and configuration details

- [configurations](configurations.md) — The configurations that describe how to manage the persisted data for specific groups of models.
- [migrationPlan](migrationplan.md) — The plan that describes the evolution of your app’s schema and how to migrate between specific versions.
