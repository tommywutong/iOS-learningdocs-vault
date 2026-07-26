---
title: Persistent history
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/persistent-history
source_url: 'https://developer.apple.com/documentation/coredata/persistent-history'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/persistent-history.json'
content_hash: 'sha256:84453809abb69386'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# Persistent history

<sub>API Collection</sub>

Use persistent history tracking to determine what changes have occurred in the store since the enabling of persistent history tracking.

## Topics

### Tracking History

- [NSPersistentHistoryToken](nspersistenthistorytoken.md) — A bookmark for keeping track the most recent history that you’ve processed.

### Requesting History

- [NSPersistentHistoryChangeRequest](nspersistenthistorychangerequest.md) — A request to fetch or purge persistent history.
- [NSPersistentHistoryResult](nspersistenthistoryresult.md) — The result of a request to fetch persistent history.

### Reading History

- [NSPersistentHistoryTransaction](nspersistenthistorytransaction.md) — A set of changes in the persistent history based on a context save or batch operation.
- [NSPersistentHistoryChange](nspersistenthistorychange.md) — A change representing the insertion, update, or deletion of a managed object in the persistent store.

## See Also

### Change processing

- [Accessing data when the store changes](accessing-data-when-the-store-changes.md) — Guarantee that a context won’t see store changes until you tell it to look.
- [Consuming relevant store changes](consuming-relevant-store-changes.md) — Filter store transactions for changes relevant to the current view.
