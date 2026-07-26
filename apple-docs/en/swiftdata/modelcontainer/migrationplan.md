---
title: migrationPlan
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontainer/migrationplan
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontainer/migrationplan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontainer/migrationplan.json'
content_hash: 'sha256:6169e22eb1996b91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContainer](../modelcontainer.md)

# migrationPlan

<sub>Instance Property</sub>

The plan that describes the evolution of your app’s schema and how to migrate between specific versions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final let migrationPlan: (any SchemaMigrationPlan.Type)?
```

## Discussion

This property provides a reference to the migration plan you specified when calling one the container’s initializers. If you didn’t specify one, the property’s value is `nil`.

## See Also

### Managing schema and configuration details

- [schema](schema.md) — The schema that maps your app’s model classes to the associated data in the app’s persistent storage.
- [configurations](configurations.md) — The configurations that describe how to manage the persisted data for specific groups of models.
