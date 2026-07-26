---
title: NSMergePolicyType.rollbackMergePolicyType
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergepolicytype/rollbackmergepolicytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicytype/rollbackmergepolicytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicytype/rollbackmergepolicytype.json'
content_hash: 'sha256:3bd7eb635197a1f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergePolicyType](../nsmergepolicytype.md)

# NSMergePolicyType.rollbackMergePolicyType

<sub>Case</sub>

A merge policy that discards unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case rollbackMergePolicyType
```

## Discussion

This policy merges conflicts between the persistent store’s version of the object and the current in-memory version by discarding unsaved changes.

## See Also

### Policies

- [NSErrorMergePolicyType](errormergepolicytype.md) — The default merge policy for all managed object contexts.
- [NSMergeByPropertyStoreTrumpMergePolicyType](mergebypropertystoretrumpmergepolicytype.md) — A property-based merge policy that applies external changes.
- [NSMergeByPropertyObjectTrumpMergePolicyType](mergebypropertyobjecttrumpmergepolicytype.md) — A property-based merge policy that applies in-memory changes.
- [NSOverwriteMergePolicyType](overwritemergepolicytype.md) — A merge policy type that overwrites the entire stored object.
