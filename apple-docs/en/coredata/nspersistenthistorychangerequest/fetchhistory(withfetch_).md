---
title: 'fetchHistory(withFetch:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(withfetch:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/fetchhistory(withfetch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangerequest/fetchhistory%28withfetch%3A%29.json'
content_hash: 'sha256:7a66c3f21d26123e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)

# fetchHistory(withFetch:)

<sub>Type Method</sub>

Retrieves history based on a fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func fetchHistory(withFetch fetchRequest: NSFetchRequest<any NSFetchRequestResult>) -> Self
```

## Parameters

- `fetchRequest` — The fetch request that defines the history bounds.

## Return Value

A persistent history fetch request ([NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)) built using an existing fetch request.

## See Also

### Fetching History

- [+ fetchHistoryAfterDate:](<fetchhistory(after_)-qi5b.md>) — Retrieves history since a given date.
- [+ fetchHistoryAfterToken:](<fetchhistory(after_)-3rmfm.md>) — Retrieves the request history after a given token.
- [+ fetchHistoryAfterTransaction:](<fetchhistory(after_)-9cuj5.md>) — Retrieves history since a given transaction.
