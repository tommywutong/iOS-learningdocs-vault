---
title: NSMigratePersistentStoresAutomaticallyOption
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmigratepersistentstoresautomaticallyoption
source_url: 'https://developer.apple.com/documentation/coredata/nsmigratepersistentstoresautomaticallyoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmigratepersistentstoresautomaticallyoption.json'
content_hash: 'sha256:aa6ae90061810791'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSMigratePersistentStoresAutomaticallyOption

<sub>Global Variable</sub>

Key to automatically attempt to migrate versioned stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSMigratePersistentStoresAutomaticallyOption: String
```

## Discussion

The corresponding value is an `NSNumber` object. If the [boolValue](../foundation/nsnumber/boolvalue.md) of the number is [true](../swift/true.md) and if the version hash information for the added store is determined to be incompatible with the model for the coordinator, Core Data will attempt to locate the source and mapping models in the application bundles, and perform a migration.

## See Also

### Constants

- [NSIgnorePersistentStoreVersioningOption](nsignorepersistentstoreversioningoption.md) — Key to ignore the built-in versioning provided by Core Data.
- [NSInferMappingModelAutomaticallyOption](nsinfermappingmodelautomaticallyoption.md) — Key to attempt to create the mapping model automatically.
