---
title: 'initWithMigrationStages:'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsstagedmigrationmanager/initwithmigrationstages:'
source_url: 'https://developer.apple.com/documentation/coredata/nsstagedmigrationmanager/initwithmigrationstages:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsstagedmigrationmanager/initwithmigrationstages%3A.json'
content_hash: 'sha256:30297f01ad90ead7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSStagedMigrationManager](../nsstagedmigrationmanager.md)

# initWithMigrationStages:

<sub>Instance Method</sub>

Creates a migration manager with the specified stages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (instancetype) initWithMigrationStages:(NSArray<__kindof NSMigrationStage *> *) stages;
```

## Parameters

- `stages` — The array of migration stages to execute.

## Return Value

An initialized migration manager, or `nil` if Core Data can’t create one.

## Discussion

> [!important] Important
> Core Data processes the migration stages in the order that you provide them.
