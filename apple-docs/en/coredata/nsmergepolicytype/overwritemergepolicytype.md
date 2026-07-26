---
title: NSMergePolicyType.overwriteMergePolicyType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergepolicytype/overwritemergepolicytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicytype/overwritemergepolicytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicytype/overwritemergepolicytype.json'
content_hash: 'sha256:7caad49b55dd5795'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergePolicyType](../nsmergepolicytype.md)

# NSMergePolicyType.overwriteMergePolicyType

<sub>Case</sub>

A merge policy type that overwrites the entire stored object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case overwriteMergePolicyType
```

## Discussion

This policy merges conflicts between the persistent store’s version of the object and the current in-memory version by saving the entire in-memory object to the persistent store.

## See Also

### Policies

- [NSErrorMergePolicyType](errormergepolicytype.md) — The default merge policy for all managed object contexts.
- [NSMergeByPropertyStoreTrumpMergePolicyType](mergebypropertystoretrumpmergepolicytype.md) — A property-based merge policy that applies external changes.
- [NSMergeByPropertyObjectTrumpMergePolicyType](mergebypropertyobjecttrumpmergepolicytype.md) — A property-based merge policy that applies in-memory changes.
- [NSRollbackMergePolicyType](rollbackmergepolicytype.md) — A merge policy that discards unsaved changes.
