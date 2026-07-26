---
title: reset()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigrationmanager/reset()
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/reset()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/reset%28%29.json'
content_hash: 'sha256:b2e781bcb1a592dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# reset()

<sub>Instance Method</sub>

Resets the association tables for the migration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func reset()
```

## Discussion

This method does not reset the source or destination contexts.

## See Also

### Aborting a Migration

- [- cancelMigrationWithError:](<cancelmigrationwitherror(__).md>) — Cancels the migration with a given error.
