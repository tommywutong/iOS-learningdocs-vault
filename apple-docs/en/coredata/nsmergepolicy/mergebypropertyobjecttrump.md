---
title: mergeByPropertyObjectTrump
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergepolicy/mergebypropertyobjecttrump
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicy/mergebypropertyobjecttrump'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicy/mergebypropertyobjecttrump.json'
content_hash: 'sha256:a380943ffc059120'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergePolicy](../nsmergepolicy.md)

# mergeByPropertyObjectTrump

<sub>Type Property</sub>

A property-based merge policy that applies in-memory changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var mergeByPropertyObjectTrump: NSMergePolicy { get }
```

## Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with in-memory changes trumping external changes.

## See Also

### Defining Merge Policies

- [errorMergePolicy](error.md) — The default merge policy for all managed object contexts.
- [mergeByPropertyStoreTrumpMergePolicy](mergebypropertystoretrump.md) — A property-based merge policy that applies external changes.
- [overwriteMergePolicy](overwrite.md) — A merge policy that overwrites the entire stored object.
- [rollbackMergePolicy](rollback.md) — A merge policy that discards unsaved changes.
- [Merge Policies](../merge-policies.md) — Define standard ways to handle conflicts during a save operation.
