---
title: 'cancelMigrationWithError(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmigrationmanager/cancelmigrationwitherror(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmigrationmanager/cancelmigrationwitherror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigrationmanager/cancelmigrationwitherror%28_%3A%29.json'
content_hash: 'sha256:e491d1c5fa05bf6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMigrationManager](../nsmigrationmanager.md)

# cancelMigrationWithError(_:)

<sub>Instance Method</sub>

Cancels the migration with a given error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelMigrationWithError(_ error: any Error)
```

## Parameters

- `error` — An error object that describes the reason why the migration is canceled.

## Discussion

You can invoke this method from anywhere in the migration process to abort the migration. Calling this method causes [- migrateStoreFromURL:type:options:withMappingModel:toDestinationURL:destinationType:destinationOptions:error:](<migratestore(from_sourcetype_options_with_todestinationurl_destinationtype_destinationoptions_).md>) to abort the migration and return `error`—you should provide an appropriate error to indicate the reason for the cancellation.

## See Also

### Aborting a Migration

- [- reset](<reset().md>) — Resets the association tables for the migration.
