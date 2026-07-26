---
title: NSBatchDeleteResult
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchdeleteresult
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchdeleteresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchdeleteresult.json'
content_hash: 'sha256:4d018a7d3f849ea1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBatchDeleteResult

<sub>Class</sub>

An object that describes the result of a batch delete request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSBatchDeleteResult
```

## Relationships

- **Inherits From**: [NSPersistentStoreResult](nspersistentstoreresult.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the Result

- [result](nsbatchdeleteresult/result.md) — The value the request returns after it executes.
- [resultType](nsbatchdeleteresult/resulttype.md) — The data type of the request’s result value.
- [NSBatchDeleteRequestResultType](nsbatchdeleterequestresulttype.md) — The types of result a batch delete request can provide when it executes.

## See Also

### Data Deletion

- [NSBatchDeleteRequest](nsbatchdeleterequest.md) — A request that deletes objects in the SQLite persistent store without loading them into memory.
