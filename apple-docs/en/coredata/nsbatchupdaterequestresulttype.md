---
title: NSBatchUpdateRequestResultType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchupdaterequestresulttype
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchupdaterequestresulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchupdaterequestresulttype.json'
content_hash: 'sha256:167542c64b6a9949'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBatchUpdateRequestResultType

<sub>Enumeration</sub>

Result types for a batch-update request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSBatchUpdateRequestResultType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Request Types

- [NSStatusOnlyResultType](nsbatchupdaterequestresulttype/statusonlyresulttype.md) — A value that indicates the return type is a Boolean value representing whether the batch-update request succeeds.
- [NSUpdatedObjectIDsResultType](nsbatchupdaterequestresulttype/updatedobjectidsresulttype.md) — A value that indicates the return type is an array of object IDs that corresponds to the updated rows.
- [NSUpdatedObjectsCountResultType](nsbatchupdaterequestresulttype/updatedobjectscountresulttype.md) — A value that indicates the return type is the number of updated rows.

### Initializers

- [init(rawValue:)](<nsbatchupdaterequestresulttype/init(rawvalue_).md>)

## See Also

### Accessing Results

- [result](nsbatchupdateresult/result.md) — The result of a batch-update request, either the number of updated objects, the identifiers of the updated objects, or a status value.
- [resultType](nsbatchupdateresult/resulttype.md) — The type of result that Core Data returns from the request.
