---
title: NSInferMappingModelAutomaticallyOption
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsinfermappingmodelautomaticallyoption
source_url: 'https://developer.apple.com/documentation/coredata/nsinfermappingmodelautomaticallyoption'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsinfermappingmodelautomaticallyoption.json'
content_hash: 'sha256:b95ae09c502c724c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSInferMappingModelAutomaticallyOption

<sub>Global Variable</sub>

Key to attempt to create the mapping model automatically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSInferMappingModelAutomaticallyOption: String
```

## Discussion

The corresponding value is an `NSNumber` object. If the [boolValue](../foundation/nsnumber/boolvalue.md) of the number is [true](../swift/true.md) and the value of the `NSMigratePersistentStoresAutomaticallyOption` is [true](../swift/true.md), the coordinator will attempt to infer a mapping model if none can be found.

## See Also

### Constants

- [NSIgnorePersistentStoreVersioningOption](nsignorepersistentstoreversioningoption.md) — Key to ignore the built-in versioning provided by Core Data.
- [NSMigratePersistentStoresAutomaticallyOption](nsmigratepersistentstoresautomaticallyoption.md) — Key to automatically attempt to migrate versioned stores.
