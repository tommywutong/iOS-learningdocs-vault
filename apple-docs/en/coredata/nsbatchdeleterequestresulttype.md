---
title: NSBatchDeleteRequestResultType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchdeleterequestresulttype
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchdeleterequestresulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchdeleterequestresulttype.json'
content_hash: 'sha256:8505c719f0f8744f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBatchDeleteRequestResultType

<sub>Enumeration</sub>

The types of result a batch delete request can provide when it executes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSBatchDeleteRequestResultType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Result Types

- [NSBatchDeleteResultTypeCount](nsbatchdeleterequestresulttype/resulttypecount.md) — Returns the number of managed objects the request deletes.
- [NSBatchDeleteResultTypeObjectIDs](nsbatchdeleterequestresulttype/resulttypeobjectids.md) — Returns an array of the deleted managed objects’ identifiers.
- [NSBatchDeleteResultTypeStatusOnly](nsbatchdeleterequestresulttype/resulttypestatusonly.md) — Returns a Boolean value that indicates if the request succeeds.

### Initializers

- [init(rawValue:)](<nsbatchdeleterequestresulttype/init(rawvalue_).md>)

## See Also

### Configuring the Result Type

- [resultType](nsbatchdeleterequest/resulttype.md) — The type of result the request provides when it executes.
