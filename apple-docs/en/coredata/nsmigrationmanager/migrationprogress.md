---
title: migrationProgress
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanager/migrationprogress
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/migrationprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/migrationprogress.json'
content_hash: 'sha256:757d804d7305c34c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# migrationProgress

<sub>Instance Property</sub>

A number between `0` and `1` that indicates the proportion of completeness of the migration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var migrationProgress: Float { get }
```

## Discussion

If a migration is not taking place, this property is `1`. You can observe this value using key-value observing.

## See Also

### Monitoring a Migration’s Progress

- [currentEntityMapping](currententitymapping.md) — The entity mapping currently being processed.
