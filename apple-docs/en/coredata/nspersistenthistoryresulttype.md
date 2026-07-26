---
title: NSPersistentHistoryResultType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistoryresulttype
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistoryresulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistoryresulttype.json'
content_hash: 'sha256:6b6a36423fea4363'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentHistoryResultType

<sub>Enumeration</sub>

The types of results from a persistent history change request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSPersistentHistoryResultType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Result Types

- [NSPersistentHistoryResultTypeStatusOnly](nspersistenthistoryresulttype/statusonly.md) — The status of the persistent history change request.
- [NSPersistentHistoryResultTypeCount](nspersistenthistoryresulttype/count.md) — The number of persistent history changes since the requested date, token, or transaction.
- [NSPersistentHistoryResultTypeObjectIDs](nspersistenthistoryresulttype/objectids.md) — The identifiers of managed objects changed since the requested date, token, or transaction.
- [NSPersistentHistoryResultTypeTransactionsAndChanges](nspersistenthistoryresulttype/transactionsandchanges.md) — The persistent history transactions and changes since the requested date, token, or transaction.
- [NSPersistentHistoryResultTypeTransactionsOnly](nspersistenthistoryresulttype/transactionsonly.md) — The persistent history transactions since the requested date, token, or transaction.
- [NSPersistentHistoryResultTypeChangesOnly](nspersistenthistoryresulttype/changesonly.md) — The persistent history changes since the requested date, token, or transaction.

### Initializers

- [init(rawValue:)](<nspersistenthistoryresulttype/init(rawvalue_).md>)

## See Also

### Inspecting History Results

- [result](nspersistenthistoryresult/result.md) — The result of the history request determined by the persistent history result type.
- [resultType](nspersistenthistoryresult/resulttype.md) — The type of result that the persistent history change request returns.
