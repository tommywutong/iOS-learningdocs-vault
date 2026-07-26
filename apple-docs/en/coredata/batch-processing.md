---
title: Batch processing
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/batch-processing
source_url: 'https://developer.apple.com/documentation/coredata/batch-processing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/batch-processing.json'
content_hash: 'sha256:707653822fb01ac9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# Batch processing

<sub>API Collection</sub>

Use batch processes to manage large data changes.

## Topics

### Data Inserts

- [NSBatchInsertRequest](nsbatchinsertrequest.md) — A request to insert a batch of data in a persistent store.
- [NSBatchInsertResult](nsbatchinsertresult.md) — The result that Core Data returns when executing a batch-insertion request.

### Data Updates

- [NSBatchUpdateRequest](nsbatchupdaterequest.md) — A request to Core Data to do a batch update of data in a persistent store without loading any data into memory.
- [NSBatchUpdateResult](nsbatchupdateresult.md) — The result returned when executing a batch update request.

### Data Deletion

- [NSBatchDeleteRequest](nsbatchdeleterequest.md) — A request that deletes objects in the SQLite persistent store without loading them into memory.
- [NSBatchDeleteResult](nsbatchdeleteresult.md) — An object that describes the result of a batch delete request.

## See Also

### Background tasks

- [Using Core Data in the background](using-core-data-in-the-background.md) — Use Core Data in both a single-threaded and multithreaded app.
- [Loading and displaying a large data feed](../swiftui/loading-and-displaying-a-large-data-feed.md) — Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [Conflict resolution](conflict-resolution.md) — Detect and resolve conflicts that occur when data is changed on multiple threads.
