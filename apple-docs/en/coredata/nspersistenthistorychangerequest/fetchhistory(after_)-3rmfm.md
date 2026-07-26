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
doc_path: '/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(after:)-3rmfm'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(after:)-3rmfm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangerequest/fetchhistory%28after%3A%29-3rmfm.json'
content_hash: 'sha256:435d6e2b336cb3d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)

# fetchHistory(after:)

<sub>Type Method</sub>

Retrieves the request history after a given token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func fetchHistory(after token: NSPersistentHistoryToken?) -> Self
```

## Parameters

- `token` — The bookmark that defines the start of the request history.

## Return Value

A persistent history fetch request ([NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)) with an initial token bookmark boundary.

## See Also

### Fetching History

- [+ fetchHistoryAfterDate:](<fetchhistory(after_)-qi5b.md>) — Retrieves history since a given date.
- [+ fetchHistoryAfterTransaction:](<fetchhistory(after_)-9cuj5.md>) — Retrieves history since a given transaction.
- [+ fetchHistoryWithFetchRequest:](<fetchhistory(withfetch_).md>) — Retrieves history based on a fetch request.
