---
title: currentEntityMapping
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanager/currententitymapping
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/currententitymapping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/currententitymapping.json'
content_hash: 'sha256:ef02372ef2b9abc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# currentEntityMapping

<sub>Instance Property</sub>

The entity mapping currently being processed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentEntityMapping: NSEntityMapping { get }
```

## Discussion

Each entity is processed a total of three times—instance creation, relationship creation, and validation.

### Special Considerations

You can observe this value using key-value observing.

## See Also

### Monitoring a Migration’s Progress

- [migrationProgress](migrationprogress.md) — A number between `0` and `1` that indicates the proportion of completeness of the migration.
