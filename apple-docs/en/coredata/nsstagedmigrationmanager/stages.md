---
title: stages
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsstagedmigrationmanager/stages
source_url: 'https://developer.apple.com/documentation/coredata/nsstagedmigrationmanager/stages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsstagedmigrationmanager/stages.json'
content_hash: 'sha256:c622d05f2badb606'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSStagedMigrationManager](../nsstagedmigrationmanager.md)

# stages

<sub>Instance Property</sub>

The migration stages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var stages: [NSMigrationStage] { get }
```

## Discussion

Core Data sets this property to the `stages` parameter you specify when creating the migration manager.
