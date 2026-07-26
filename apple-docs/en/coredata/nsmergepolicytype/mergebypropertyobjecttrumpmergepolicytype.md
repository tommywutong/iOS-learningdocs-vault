---
title: NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype.json'
content_hash: 'sha256:8c609126d555a3b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergePolicyType](../nsmergepolicytype.md)

# NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType

<sub>Case</sub>

A property-based merge policy that applies in-memory changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case mergeByPropertyObjectTrumpMergePolicyType
```

## Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with in-memory changes trumping external changes.

## See Also

### Policies

- [NSErrorMergePolicyType](errormergepolicytype.md) — The default merge policy for all managed object contexts.
- [NSMergeByPropertyStoreTrumpMergePolicyType](mergebypropertystoretrumpmergepolicytype.md) — A property-based merge policy that applies external changes.
- [NSOverwriteMergePolicyType](overwritemergepolicytype.md) — A merge policy type that overwrites the entire stored object.
- [NSRollbackMergePolicyType](rollbackmergepolicytype.md) — A merge policy that discards unsaved changes.
