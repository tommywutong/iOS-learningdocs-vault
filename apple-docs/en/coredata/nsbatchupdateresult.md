---
title: NSBatchUpdateResult
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsbatchupdateresult
source_url: 'https://developer.apple.com/documentation/coredata/nsbatchupdateresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsbatchupdateresult.json'
content_hash: 'sha256:3389d502069b7f4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSBatchUpdateResult

<sub>Class</sub>

The result returned when executing a batch update request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSBatchUpdateResult
```

## Relationships

- **Inherits From**: [NSPersistentStoreResult](nspersistentstoreresult.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing Results

- [result](nsbatchupdateresult/result.md) — The result of a batch-update request, either the number of updated objects, the identifiers of the updated objects, or a status value.
- [resultType](nsbatchupdateresult/resulttype.md) — The type of result that Core Data returns from the request.
- [NSBatchUpdateRequestResultType](nsbatchupdaterequestresulttype.md) — Result types for a batch-update request.

## See Also

### Data Updates

- [NSBatchUpdateRequest](nsbatchupdaterequest.md) — A request to Core Data to do a batch update of data in a persistent store without loading any data into memory.
