---
title: Conflict resolution
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/conflict-resolution
source_url: 'https://developer.apple.com/documentation/coredata/conflict-resolution'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/conflict-resolution.json'
content_hash: 'sha256:9bc8f1fc40393984'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# Conflict resolution

<sub>API Collection</sub>

Detect and resolve conflicts that occur when data is changed on multiple threads.

## Topics

### Conflict Management

- [NSConstraintConflict](nsconstraintconflict.md) — An encapsulation of conflicts that occur during an attempt to save a managed object.
- [NSMergeConflict](nsmergeconflict.md) — An encapsulation of conflicts that occur during an attempt to save changes in a managed object context.
- [NSMergePolicy](nsmergepolicy.md) — A policy object that you use to resolve conflicts between the persistent store and in-memory versions of managed objects.
- [NSQueryGenerationToken](nsquerygenerationtoken.md) — A token that indicates which generation of the persistent store is being accessed.

## See Also

### Background tasks

- [Using Core Data in the background](using-core-data-in-the-background.md) — Use Core Data in both a single-threaded and multithreaded app.
- [Loading and displaying a large data feed](../swiftui/loading-and-displaying-a-large-data-feed.md) — Consume data in the background, and lower memory use by batching imports and preventing duplicate records.
- [Batch processing](batch-processing.md) — Use batch processes to manage large data changes.
