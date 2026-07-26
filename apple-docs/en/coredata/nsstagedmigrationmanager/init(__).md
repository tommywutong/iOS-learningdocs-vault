---
title: 'init(_:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+, Swift 5.8+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsstagedmigrationmanager/init(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsstagedmigrationmanager/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsstagedmigrationmanager/init%28_%3A%29.json'
content_hash: 'sha256:8d3f90bad2f06c57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSStagedMigrationManager](../nsstagedmigrationmanager.md)

# init(_:)

<sub>Initializer</sub>

Creates a migration manager with the specified stages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(_ stages: [NSMigrationStage])
```

## Parameters

- `stages` — The array of migration stages to execute.

## Discussion

> [!important] Important
> Core Data processes the migration stages in the order that you provide them.
