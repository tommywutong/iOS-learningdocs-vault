---
title: HistoryDescriptor
framework: SwiftData
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/historydescriptor
source_url: 'https://developer.apple.com/documentation/swiftdata/historydescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/historydescriptor.json'
content_hash: 'sha256:3b4baf3915be1570'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# HistoryDescriptor

<sub>Structure</sub>

A type that describes the criteria, and, optionally, sort order, to use when fetching history data

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct HistoryDescriptor<TransactionType> where TransactionType : HistoryTransaction
```

## Topics

### Creating a descriptor

- [init(predicate:)](<historydescriptor/init(predicate_).md>) — Initializes a new history descriptor with the provided predicate.
- [init(predicate:sortBy:)](<historydescriptor/init(predicate_sortby_).md>) — Initializes a new history descriptor with the provided predicate and sort descriptor.

### Getting the descriptor configuration

- [fetchLimit](historydescriptor/fetchlimit.md) — The maximum number of transactions to retrieve from the model store’s history.
- [predicate](historydescriptor/predicate.md) — The predicate used to initialize the history descriptor.
- [sortBy](historydescriptor/sortby.md) — The sort descriptor to use to sort the returned history data.

## See Also

### Model life cycle

- [ModelContainer](modelcontainer.md) — An object that manages an app’s schema and model storage configuration.
- [ModelContext](modelcontext.md) — An object that enables you to fetch, insert, and delete models, and save any changes to disk.
- [Fetching and filtering time-based model changes](fetching-and-filtering-time-based-model-changes.md) — Track all inserts, updates, and deletes that occur in a data store and process them as a series of chronological transactions.
- [Deleting persistent data from your app](deleting-persistent-data-from-your-app.md) — Explore different ways to use SwiftData to delete persistent data.
- [Reverting data changes using the undo manager](reverting-data-changes-using-the-undo-manager.md) — Automatically record data change operations that people perform in your SwiftUI app, and let them undo and redo those changes.
- [Syncing model data across a person’s devices](syncing-model-data-across-a-persons-devices.md) — Add the required capabilities and define a compatible schema to enable SwiftData to automatically sync your app’s model data using iCloud.
- [Concurrency support](concurrencysupport.md) — Types you use to access model attributes and perform storage-related tasks in a safe and isolated way.
