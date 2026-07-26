---
title: resultType
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorychangerequest/resulttype
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/resulttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangerequest/resulttype.json'
content_hash: 'sha256:cf87ac4c3ebb6f31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)

# resultType

<sub>Instance Property</sub>

The type of result that this request returns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resultType: NSPersistentHistoryResultType { get set }
```

## Discussion

This value defaults to [NSPersistentHistoryResultTypeTransactionsAndChanges](../nspersistenthistoryresulttype/transactionsandchanges.md).

## See Also

### Configuring the Request

- [fetchRequest](fetchrequest.md) — The specified fetch request, when retrieving history.
