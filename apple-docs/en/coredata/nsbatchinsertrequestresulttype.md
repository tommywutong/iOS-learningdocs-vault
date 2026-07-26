---
title: NSBatchInsertRequestResultType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchinsertrequestresulttype
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchinsertrequestresulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchinsertrequestresulttype.json'
content_hash: 'sha256:abff2f50ed349704'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBatchInsertRequestResultType

<sub>Enumeration</sub>

Result types for a batch-insertion request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSBatchInsertRequestResultType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Request Types

- [NSBatchInsertRequestResultTypeStatusOnly](nsbatchinsertrequestresulttype/statusonly.md) — A value that indicates that the return type is a Boolean value representing whether the batch-insertion request succeeded.
- [NSBatchInsertRequestResultTypeObjectIDs](nsbatchinsertrequestresulttype/objectids.md) — A value that indicates the return type is an array of object IDs that corresponds to the inserted rows.
- [NSBatchInsertRequestResultTypeCount](nsbatchinsertrequestresulttype/count.md) — A value that indicates that the return type is the number of inserted rows.

### Initializers

- [init(rawValue:)](<nsbatchinsertrequestresulttype/init(rawvalue_).md>)

## See Also

### Accessing Results

- [result](nsbatchinsertresult/result.md) — The result of a batch-insertion request.
- [resultType](nsbatchinsertresult/resulttype.md) — The type of result that Core Data returns from this request.
