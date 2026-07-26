---
title: NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergepolicytype/mergebypropertystoretrumpmergepolicytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertystoretrumpmergepolicytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicytype/mergebypropertystoretrumpmergepolicytype.json'
content_hash: 'sha256:6830a592cdb08e31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergePolicyType](../nsmergepolicytype.md)

# NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType

<sub>Case</sub>

A property-based merge policy that applies external changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case mergeByPropertyStoreTrumpMergePolicyType
```

## Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with external changes trumping in-memory changes.

## See Also

### Policies

- [NSErrorMergePolicyType](errormergepolicytype.md) — The default merge policy for all managed object contexts.
- [NSMergeByPropertyObjectTrumpMergePolicyType](mergebypropertyobjecttrumpmergepolicytype.md) — A property-based merge policy that applies in-memory changes.
- [NSOverwriteMergePolicyType](overwritemergepolicytype.md) — A merge policy type that overwrites the entire stored object.
- [NSRollbackMergePolicyType](rollbackmergepolicytype.md) — A merge policy that discards unsaved changes.
