---
title: label
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationstage/label
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationstage/label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationstage/label.json'
content_hash: 'sha256:371a908f885176be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationStage](../nsmigrationstage.md)

# label

<sub>Instance Property</sub>

The textual description of the migration stage’s purpose.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var label: String! { get set }
```

## Discussion

Persistent history tracking, if enabled, records the label for later use. The default value is an empty string.
