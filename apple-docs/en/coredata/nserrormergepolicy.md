---
title: NSErrorMergePolicy
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nserrormergepolicy
source_url: 'https://developer.apple.com/documentation/coredata/nserrormergepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nserrormergepolicy.json'
content_hash: 'sha256:b69f5d9cb3d6582d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSErrorMergePolicy

<sub>Global Variable</sub>

The default merge policy for all managed object contexts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSErrorMergePolicy: AnyObject
```

## Discussion

If a save fails because of conflicting objects, you can find the IDs of those objects in error’s `userInfo` dictionary. Use the [NSInsertedObjectsKey](nsinsertedobjectskey.md) and [NSUpdatedObjectsKey](nsupdatedobjectskey.md) keys to extract the object IDs.

## See Also

### Policies

- [NSMergeByPropertyStoreTrumpMergePolicy](nsmergebypropertystoretrumpmergepolicy.md) — A property-based merge policy that applies external changes.
- [NSMergeByPropertyObjectTrumpMergePolicy](nsmergebypropertyobjecttrumpmergepolicy.md) — A property-based merge policy that applies in-memory changes.
- [NSOverwriteMergePolicy](nsoverwritemergepolicy.md) — A merge policy that overwrites the entire stored object.
- [NSRollbackMergePolicy](nsrollbackmergepolicy.md) — A merge policy that discards unsaved changes.
- [NSMergePolicyType](nsmergepolicytype.md) — Constants that define merge policy types.
