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
doc_path: '/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(after:)-qi5b'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(after:)-qi5b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangerequest/fetchhistory%28after%3A%29-qi5b.json'
content_hash: 'sha256:a74f0ad33cdb86da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)

# fetchHistory(after:)

<sub>Type Method</sub>

Retrieves history since a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func fetchHistory(after date: Date) -> Self
```

## Parameters

- `date` — The date used to define the start of the fetch history.

## Return Value

A persistent history fetch request ([NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)) with an initial date boundary.

## See Also

### Fetching History

- [+ fetchHistoryAfterToken:](<fetchhistory(after_)-3rmfm.md>) — Retrieves the request history after a given token.
- [+ fetchHistoryAfterTransaction:](<fetchhistory(after_)-9cuj5.md>) — Retrieves history since a given transaction.
- [+ fetchHistoryWithFetchRequest:](<fetchhistory(withfetch_).md>) — Retrieves history based on a fetch request.
