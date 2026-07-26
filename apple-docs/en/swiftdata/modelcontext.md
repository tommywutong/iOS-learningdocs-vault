---
title: ModelContext
framework: SwiftData
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata/modelcontext
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext.json'
content_hash: 'sha256:03bccefee04f9e0e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftData](../swiftdata.md)

# ModelContext

<sub>Class</sub>

An object that enables you to fetch, insert, and delete models, and save any changes to disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ModelContext
```

## Overview

A model context is central to SwiftData as it’s responsible for managing the entire lifecycle of your persistent models. You use a context to insert new models, track and persist changes to those models, and to delete those models when you no longer need them. A context understands your app’s schema but doesn’t know about any individual models until you tell it to fetch some from the persistent storage or populate it with new models. Afterwards, any changes made to those models exist only in memory until the context implicitly writes them to the persistent storage, or you manually invoke [save()](<modelcontext/save().md>). For more information about implicit writes, see [autosaveEnabled](modelcontext/autosaveenabled.md).

If your app’s schema describes relationships between models, you don’t need to manually insert each model into the context when you first create them. Instead, create the graph of related models and insert only the graph’s root model into the context. The context recognizes the hierarchy and automatically handles the insertion of the related models. The same behavior applies even if the graph contains both new and existing models.

A model context depends on a model container for knowledge about your app’s schema and persistent storage. After you attach a container to your app’s window group or view hierarchy, an associated context becomes available in the SwiftUI environment. This context is bound to the main actor and the framework configures the context to implicitly save future model changes. The [Query()](<query().md>) macros use the same context to perform their fetches.

```swift
struct LastModifiedView: View {
    @Environment(\.modelContext) private var modelContext

}
```

> [!important] Important
> If you don’t explicitly attach a model container, the environment provides a context bound to an in-memory, schema-less container. Any attempt to insert a model into this context causes the framework to throw an error, and any fetches you run will return empty results.

After you establish access to a model context, use that context’s [insert(_:)](<modelcontext/insert(__).md>) and [delete(_:)](<modelcontext/delete(__).md>) methods to add and remove models. You can also delete several models at once using [delete(model:where:includeSubclasses:)](<modelcontext/delete(model_where_includesubclasses_).md>). There isn’t a corresponding method to update a model because the context automatically tracks all changes to its known models. Use the [hasChanges](modelcontext/haschanges.md) property to determine if the context has unsaved changes, and call [rollback()](<modelcontext/rollback().md>) to discard any pending inserts and deletes and any restore changed models to their most recent saved state.

Although you fetch models primarily with the `Query()` macro (and its variants), you can use a model context to perform almost identical fetches. For example, use the [fetch(_:)](<modelcontext/fetch(__).md>) and [fetch(_:batchSize:)](<modelcontext/fetch(__batchsize_).md>) methods to retrieve all models of a certain type that match a set of criteria. And use [fetchCount(_:)](<modelcontext/fetchcount(__).md>) to determine the number of models that match some criteria without the overhead of fetching the models themselves. If you need to be able to identify models that match some criteria but don’t require all of the associated data, use [fetchIdentifiers(_:)](<modelcontext/fetchidentifiers(__).md>) and [fetchIdentifiers(_:batchSize:)](<modelcontext/fetchidentifiers(__batchsize_).md>) to retrieve only those models’ persistent identifiers.

A model context posts a [willSave](modelcontext/willsave.md) notification before it attempts a save operation, and a [didSave](modelcontext/didsave.md) notification immediately after that operation succeeds. Subscribe to one, or both, of these notifications if your app needs to be aware of these events. The `didSave` notification provides additional information about any inserted, updated, and deleted models.

```swift
struct LastModifiedView: View {
    @Environment(\.modelContext) private var context
    @State private var lastModified = Date.now
    
    private var didSavePublisher: NotificationCenter.Publisher {
        NotificationCenter.default
            .publisher(for: ModelContext.willSave, object: context)
    }
    
    var body: some View {
        Text(lastModified.formatted(date: .abbreviated, time: .shortened))
            .onReceive(didSavePublisher) { _ in
                lastModified = Date.now
            }
    }
}
```

> [!note] Note
> To avoid receiving unwanted or unexpected notifications, always specify the model context as the `object` parameter when creating a publisher.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a model context

- [init(_:)](<modelcontext/init(__).md>) — Creates a context that belongs to the specified model container.
- [ModelContainer](modelcontainer.md) — An object that manages an app’s schema and model storage configuration.

### Fetching models

- [fetch(_:)](<modelcontext/fetch(__).md>) — Returns an array of typed models that match the criteria of the specified fetch descriptor.
- [fetch(_:batchSize:)](<modelcontext/fetch(__batchsize_).md>) — Returns a collection of typed models, in batches, which match the criteria of the specified fetch descriptor.
- [fetchCount(_:)](<modelcontext/fetchcount(__).md>) — Returns the number of models that match the criteria of the specified fetch descriptor.
- [FetchDescriptor](fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.
- [FetchResultsCollection](fetchresultscollection.md) — A collection that efficiently provides the results of a completed fetch.
- [enumerate(_:batchSize:allowEscapingMutations:block:)](<modelcontext/enumerate(__batchsize_allowescapingmutations_block_).md>) — Runs a closure for each model that matches the criteria of the specified fetch descriptor.
- [model(for:)](<modelcontext/model(for_).md>) — Returns the persistent model for the specified identifier.
- [registeredModel(for:)](<modelcontext/registeredmodel(for_).md>) — Returns the typed model for the specified identifier.

### Inserting models

- [insertedModelsArray](modelcontext/insertedmodelsarray.md) — The array of inserted models that the context is yet to persist.
- [insert(_:)](<modelcontext/insert(__).md>) — Registers the specified model with the context so it can include the model in the next save operation.

### Modifying models

- [hasChanges](modelcontext/haschanges.md) — A Boolean value that indicates whether the context has unsaved changes.
- [changedModelsArray](modelcontext/changedmodelsarray.md) — The array of registered models that have unsaved changes.

### Deleting models

- [deletedModelsArray](modelcontext/deletedmodelsarray.md) — The array of registered models that the context will remove from the persistent storage during the next save operation.
- [delete(_:)](<modelcontext/delete(__).md>) — Removes the specified model from the persistent storage during the next save operation.
- [delete(model:where:includeSubclasses:)](<modelcontext/delete(model_where_includesubclasses_).md>) — Removes each model satisfying the given predicate from the persistent storage during the next save operation.

### Persisting unsaved changes

- [autosaveEnabled](modelcontext/autosaveenabled.md) — A Boolean value that indicates whether the context should automatically save any pending changes when certain events occur.
- [save()](<modelcontext/save().md>) — Writes any pending inserts, changes, and deletes to the persistent storage.
- [transaction(block:)](<modelcontext/transaction(block_).md>) — Runs the provided closure, and once it finishes, writes any pending inserts, changes, and deletes to the persistent storage.
- [rollback()](<modelcontext/rollback().md>) — Discards pending inserts and deletes, restores changed models to their most recent committed state, and empties the undo stack.

### Fetching only persistent identifiers

- [fetchIdentifiers(_:)](<modelcontext/fetchidentifiers(__).md>) — Returns an array of persistent identifiers, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.
- [fetchIdentifiers(_:batchSize:)](<modelcontext/fetchidentifiers(__batchsize_).md>) — Returns a collection of persistent identifiers, in batches, where each identifier represents a single model that satisfies the criteria of the specified fetch descriptor.

### Accessing the container

- [container](modelcontext/container.md) — The context’s model container.

### Performing undo and redo

- [processPendingChanges()](<modelcontext/processpendingchanges().md>) — Tells the undo manager to record any changes made to the context’s registered models.
- [undoManager](modelcontext/undomanager.md) — The object that provides undo support for the context.

### Registering for notifications

- [willSave](modelcontext/willsave.md) — A notification that posts when the context is about to process pending inserts, changes, and deletes.
- [didSave](modelcontext/didsave.md) — A notification that posts when the context finishes processing pending inserts, changes, and deletes.
- [NotificationKey](modelcontext/notificationkey.md) — Describes the data in the user info dictionary of a notification sent by a model context.

### Debugging contexts

- [debugDescription](modelcontext/debugdescription.md) — A textual representation of the context, suitable for debugging.

### Instance Properties

- [author](modelcontext/author.md)
- [editingState](modelcontext/editingstate.md)

### Instance Methods

- [deleteHistory(_:)](<modelcontext/deletehistory(__).md>)
- [fetchHistory(_:)](<modelcontext/fetchhistory(__).md>)

## See Also

### Model life cycle

- [ModelContainer](modelcontainer.md) — An object that manages an app’s schema and model storage configuration.
- [Fetching and filtering time-based model changes](fetching-and-filtering-time-based-model-changes.md) — Track all inserts, updates, and deletes that occur in a data store and process them as a series of chronological transactions.
- [HistoryDescriptor](historydescriptor.md) — A type that describes the criteria, and, optionally, sort order, to use when fetching history data
- [Deleting persistent data from your app](deleting-persistent-data-from-your-app.md) — Explore different ways to use SwiftData to delete persistent data.
- [Reverting data changes using the undo manager](reverting-data-changes-using-the-undo-manager.md) — Automatically record data change operations that people perform in your SwiftUI app, and let them undo and redo those changes.
- [Syncing model data across a person’s devices](syncing-model-data-across-a-persons-devices.md) — Add the required capabilities and define a compatible schema to enable SwiftData to automatically sync your app’s model data using iCloud.
- [Concurrency support](concurrencysupport.md) — Types you use to access model attributes and perform storage-related tasks in a safe and isolated way.
