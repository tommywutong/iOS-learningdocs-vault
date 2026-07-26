---
title: NSMergeByPropertyObjectTrumpMergePolicy
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergebypropertyobjecttrumpmergepolicy
source_url: 'https://developer.apple.com/documentation/coredata/nsmergebypropertyobjecttrumpmergepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergebypropertyobjecttrumpmergepolicy.json'
content_hash: 'sha256:8146eee14de0d060'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSMergeByPropertyObjectTrumpMergePolicy

<sub>Global Variable</sub>

A property-based merge policy that applies in-memory changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject
```

## Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with in-memory changes trumping external changes.

## See Also

### Policies

- [NSErrorMergePolicy](nserrormergepolicy.md) — The default merge policy for all managed object contexts.
- [NSMergeByPropertyStoreTrumpMergePolicy](nsmergebypropertystoretrumpmergepolicy.md) — A property-based merge policy that applies external changes.
- [NSOverwriteMergePolicy](nsoverwritemergepolicy.md) — A merge policy that overwrites the entire stored object.
- [NSRollbackMergePolicy](nsrollbackmergepolicy.md) — A merge policy that discards unsaved changes.
- [NSMergePolicyType](nsmergepolicytype.md) — Constants that define merge policy types.
