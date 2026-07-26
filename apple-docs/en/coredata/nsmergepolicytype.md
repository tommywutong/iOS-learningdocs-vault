---
title: NSMergePolicyType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergepolicytype
source_url: 'https://developer.apple.com/documentation/coredata/nsmergepolicytype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergepolicytype.json'
content_hash: 'sha256:6ec40a31be775208'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSMergePolicyType

<sub>Enumeration</sub>

Constants that define merge policy types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSMergePolicyType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Policies

- [NSErrorMergePolicyType](nsmergepolicytype/errormergepolicytype.md) — The default merge policy for all managed object contexts.
- [NSMergeByPropertyStoreTrumpMergePolicyType](nsmergepolicytype/mergebypropertystoretrumpmergepolicytype.md) — A property-based merge policy that applies external changes.
- [NSMergeByPropertyObjectTrumpMergePolicyType](nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype.md) — A property-based merge policy that applies in-memory changes.
- [NSOverwriteMergePolicyType](nsmergepolicytype/overwritemergepolicytype.md) — A merge policy type that overwrites the entire stored object.
- [NSRollbackMergePolicyType](nsmergepolicytype/rollbackmergepolicytype.md) — A merge policy that discards unsaved changes.

### Initializers

- [init(rawValue:)](<nsmergepolicytype/init(rawvalue_).md>)

## See Also

### Policies

- [NSErrorMergePolicy](nserrormergepolicy.md) — The default merge policy for all managed object contexts.
- [NSMergeByPropertyStoreTrumpMergePolicy](nsmergebypropertystoretrumpmergepolicy.md) — A property-based merge policy that applies external changes.
- [NSMergeByPropertyObjectTrumpMergePolicy](nsmergebypropertyobjecttrumpmergepolicy.md) — A property-based merge policy that applies in-memory changes.
- [NSOverwriteMergePolicy](nsoverwritemergepolicy.md) — A merge policy that overwrites the entire stored object.
- [NSRollbackMergePolicy](nsrollbackmergepolicy.md) — A merge policy that discards unsaved changes.
