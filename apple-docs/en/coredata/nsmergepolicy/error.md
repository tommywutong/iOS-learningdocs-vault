---
title: error
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergepolicy/error
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicy/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicy/error.json'
content_hash: 'sha256:2f5e9a80290d4e0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergePolicy](../nsmergepolicy.md)

# error

<sub>Type Property</sub>

The default merge policy for all managed object contexts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var error: NSMergePolicy { get }
```

## Discussion

If a save fails because of conflicting objects, you can find the IDs of those objects in error’s `userInfo` dictionary. Use the [NSInsertedObjectsKey](../nsinsertedobjectskey.md) and [NSUpdatedObjectsKey](../nsupdatedobjectskey.md) keys to extract the object IDs.

## See Also

### Defining Merge Policies

- [mergeByPropertyStoreTrumpMergePolicy](mergebypropertystoretrump.md) — A property-based merge policy that applies external changes.
- [mergeByPropertyObjectTrumpMergePolicy](mergebypropertyobjecttrump.md) — A property-based merge policy that applies in-memory changes.
- [overwriteMergePolicy](overwrite.md) — A merge policy that overwrites the entire stored object.
- [rollbackMergePolicy](rollback.md) — A merge policy that discards unsaved changes.
- [Merge Policies](../merge-policies.md) — Define standard ways to handle conflicts during a save operation.
