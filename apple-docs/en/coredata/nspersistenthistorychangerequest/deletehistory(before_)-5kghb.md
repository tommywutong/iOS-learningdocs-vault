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
doc_path: '/documentation/coredata/nspersistenthistorychangerequest/deletehistory(before:)-5kghb'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/deletehistory(before:)-5kghb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangerequest/deletehistory%28before%3A%29-5kghb.json'
content_hash: 'sha256:ab4b6218a8bec2af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)

# deleteHistory(before:)

<sub>Type Method</sub>

Purges history older than that defined by a given token.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func deleteHistory(before token: NSPersistentHistoryToken?) -> Self
```

## Parameters

- `token` — The bookmark that marks the end of the delete history request.

## Return Value

A delete history change request ([NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)) using an end token bookmark boundary.

## See Also

### Purging History

- [+ deleteHistoryBeforeDate:](<deletehistory(before_)-7t2th.md>) — Purges history older than a given date.
- [+ deleteHistoryBeforeTransaction:](<deletehistory(before_)-9l06p.md>) — Purges history older than a given transaction.
