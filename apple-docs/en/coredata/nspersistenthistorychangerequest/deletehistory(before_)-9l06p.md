---
title: 'deleteHistory(before:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistenthistorychangerequest/deletehistory(before:)-9l06p'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/deletehistory(before:)-9l06p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangerequest/deletehistory%28before%3A%29-9l06p.json'
content_hash: 'sha256:9ac62a37814a79de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)

# deleteHistory(before:)

<sub>Type Method</sub>

Purges history older than a given transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func deleteHistory(before transaction: NSPersistentHistoryTransaction?) -> Self
```

## Parameters

- `transaction` — The transaction that marks the end of the delete history request.

## Return Value

A delete history change request ([NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)) using an end transaction boundary.

## See Also

### Purging History

- [+ deleteHistoryBeforeDate:](<deletehistory(before_)-7t2th.md>) — Purges history older than a given date.
- [+ deleteHistoryBeforeToken:](<deletehistory(before_)-5kghb.md>) — Purges history older than that defined by a given token.
