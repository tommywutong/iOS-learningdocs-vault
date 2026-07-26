---
title: NSIgnorePersistentStoreVersioningOption
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsignorepersistentstoreversioningoption
source_url: 'https://developer.apple.com/documentation/coredata/nsignorepersistentstoreversioningoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsignorepersistentstoreversioningoption.json'
content_hash: 'sha256:e705ba8796b930af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSIgnorePersistentStoreVersioningOption

<sub>Global Variable</sub>

Key to ignore the built-in versioning provided by Core Data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSIgnorePersistentStoreVersioningOption: String
```

## Discussion

The corresponding value is an `NSNumber` object. If the [boolValue](../foundation/nsnumber/boolvalue.md) of the number is [true](../swift/true.md), Core Data will not compare the version hashes between the managed object model in the coordinator and the metadata for the loaded store. (It will, however, continue to update the version hash information in the metadata.) This key and corresponding value of [true](../swift/true.md) is specified by default for all applications linked on or before OS X v10.4.

## See Also

### Constants

- [NSMigratePersistentStoresAutomaticallyOption](nsmigratepersistentstoresautomaticallyoption.md) — Key to automatically attempt to migrate versioned stores.
- [NSInferMappingModelAutomaticallyOption](nsinfermappingmodelautomaticallyoption.md) — Key to attempt to create the mapping model automatically.
