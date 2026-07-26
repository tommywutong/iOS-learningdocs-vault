---
title: 'fetchHistory(after:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(after:)-9cuj5'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(after:)-9cuj5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangerequest/fetchhistory%28after%3A%29-9cuj5.json'
content_hash: 'sha256:20ba8a6fef0a2ef0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)

# fetchHistory(after:)

<sub>Type Method</sub>

Retrieves history since a given transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func fetchHistory(after transaction: NSPersistentHistoryTransaction?) -> Self
```

## Parameters

- `transaction` — The transaction that marks the beginning of the history request.

## Return Value

A persistent history fetch request ([NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)) with an initial transaction boundary.

## See Also

### Fetching History

- [+ fetchHistoryAfterDate:](<fetchhistory(after_)-qi5b.md>) — Retrieves history since a given date.
- [+ fetchHistoryAfterToken:](<fetchhistory(after_)-3rmfm.md>) — Retrieves the request history after a given token.
- [+ fetchHistoryWithFetchRequest:](<fetchhistory(withfetch_).md>) — Retrieves history based on a fetch request.
