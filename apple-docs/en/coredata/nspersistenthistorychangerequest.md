---
title: NSPersistentHistoryChangeRequest
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistenthistorychangerequest
source_url: 'https://developer.apple.com/documentation/coredata/nspersistenthistorychangerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistenthistorychangerequest.json'
content_hash: 'sha256:25880b8e004e010b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentHistoryChangeRequest

<sub>Class</sub>

A request to fetch or purge persistent history.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSPersistentHistoryChangeRequest
```

## Relationships

- **Inherits From**: [NSPersistentStoreRequest](nspersistentstorerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the Request

- [fetchRequest](nspersistenthistorychangerequest/fetchrequest.md) — The specified fetch request, when retrieving history.
- [resultType](nspersistenthistorychangerequest/resulttype.md) — The type of result that this request returns.

### Getting the Token

- [token](nspersistenthistorychangerequest/token.md) — The specified token, when retrieving history defined by a token.

### Fetching History

- [+ fetchHistoryAfterDate:](<nspersistenthistorychangerequest/fetchhistory(after_)-qi5b.md>) — Retrieves history since a given date.
- [+ fetchHistoryAfterToken:](<nspersistenthistorychangerequest/fetchhistory(after_)-3rmfm.md>) — Retrieves the request history after a given token.
- [+ fetchHistoryAfterTransaction:](<nspersistenthistorychangerequest/fetchhistory(after_)-9cuj5.md>) — Retrieves history since a given transaction.
- [+ fetchHistoryWithFetchRequest:](<nspersistenthistorychangerequest/fetchhistory(withfetch_).md>) — Retrieves history based on a fetch request.

### Purging History

- [+ deleteHistoryBeforeDate:](<nspersistenthistorychangerequest/deletehistory(before_)-7t2th.md>) — Purges history older than a given date.
- [+ deleteHistoryBeforeToken:](<nspersistenthistorychangerequest/deletehistory(before_)-5kghb.md>) — Purges history older than that defined by a given token.
- [+ deleteHistoryBeforeTransaction:](<nspersistenthistorychangerequest/deletehistory(before_)-9l06p.md>) — Purges history older than a given transaction.

## See Also

### Requesting History

- [NSPersistentHistoryResult](nspersistenthistoryresult.md) — The result of a request to fetch persistent history.
