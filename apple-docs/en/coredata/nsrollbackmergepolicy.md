---
title: NSRollbackMergePolicy
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsrollbackmergepolicy
source_url: 'https://developer.apple.com/documentation/coredata/nsrollbackmergepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsrollbackmergepolicy.json'
content_hash: 'sha256:ed640446b3b775b6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSRollbackMergePolicy

<sub>Global Variable</sub>

A merge policy that discards unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSRollbackMergePolicy: AnyObject
```

## Discussion

This policy merges conflicts between the persistent store’s version of the object and the current in-memory version by discarding unsaved changes.

## See Also

### Policies

- [NSErrorMergePolicy](nserrormergepolicy.md) — The default merge policy for all managed object contexts.
- [NSMergeByPropertyStoreTrumpMergePolicy](nsmergebypropertystoretrumpmergepolicy.md) — A property-based merge policy that applies external changes.
- [NSMergeByPropertyObjectTrumpMergePolicy](nsmergebypropertyobjecttrumpmergepolicy.md) — A property-based merge policy that applies in-memory changes.
- [NSOverwriteMergePolicy](nsoverwritemergepolicy.md) — A merge policy that overwrites the entire stored object.
- [NSMergePolicyType](nsmergepolicytype.md) — Constants that define merge policy types.
