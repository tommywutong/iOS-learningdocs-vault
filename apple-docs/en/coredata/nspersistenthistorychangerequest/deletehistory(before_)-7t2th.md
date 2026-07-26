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
doc_path: '/documentation/coredata/nspersistenthistorychangerequest/deletehistory(before:)-7t2th'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest/deletehistory(before:)-7t2th'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangerequest/deletehistory%28before%3A%29-7t2th.json'
content_hash: 'sha256:2c005d0f4dafce26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)

# deleteHistory(before:)

<sub>Type Method</sub>

Purges history older than a given date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func deleteHistory(before date: Date) -> Self
```

## Parameters

- `date` — The date used to define the end of the delete history request.

## Return Value

A delete history change request ([NSPersistentHistoryChangeRequest](../nspersistenthistorychangerequest.md)) using an end date boundary.

## See Also

### Purging History

- [+ deleteHistoryBeforeToken:](<deletehistory(before_)-5kghb.md>) — Purges history older than that defined by a given token.
- [+ deleteHistoryBeforeTransaction:](<deletehistory(before_)-9l06p.md>) — Purges history older than a given transaction.
