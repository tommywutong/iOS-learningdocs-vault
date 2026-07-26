---
title: NSMergePolicyType.errorMergePolicyType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergepolicytype/errormergepolicytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicytype/errormergepolicytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicytype/errormergepolicytype.json'
content_hash: 'sha256:10150130889dda5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergePolicyType](../nsmergepolicytype.md)

# NSMergePolicyType.errorMergePolicyType

<sub>Case</sub>

The default merge policy for all managed object contexts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case errorMergePolicyType
```

## Discussion

If a save fails because of conflicting objects, you can find the IDs of those objects in error’s `userInfo` dictionary. Use the [NSInsertedObjectsKey](../nsinsertedobjectskey.md) and [NSUpdatedObjectsKey](../nsupdatedobjectskey.md) keys to extract the object IDs.

## See Also

### Policies

- [NSMergeByPropertyStoreTrumpMergePolicyType](mergebypropertystoretrumpmergepolicytype.md) — A property-based merge policy that applies external changes.
- [NSMergeByPropertyObjectTrumpMergePolicyType](mergebypropertyobjecttrumpmergepolicytype.md) — A property-based merge policy that applies in-memory changes.
- [NSOverwriteMergePolicyType](overwritemergepolicytype.md) — A merge policy type that overwrites the entire stored object.
- [NSRollbackMergePolicyType](rollbackmergepolicytype.md) — A merge policy that discards unsaved changes.
