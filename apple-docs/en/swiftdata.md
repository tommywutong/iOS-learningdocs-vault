---
title: SwiftData
framework: SwiftData
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftdata
source_url: 'https://developer.apple.com/documentation/swiftdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata.json'
content_hash: 'sha256:25d7bd5be1f27035'
translated: false
---

> Navigation: [Technologies](technologies.md)

# SwiftData

<sub>Framework</sub>

Write your model code declaratively to add managed persistence and efficient model fetching.

## Overview

Combining Core Data’s proven persistence technology and Swift’s modern concurrency features, SwiftData enables you to add persistence to your app quickly, with minimal code and no external dependencies. Using modern language features like macros, SwiftData enables you to write code that is fast, efficient, and safe, enabling you to describe the entire model layer (or object graph) for your app. The framework handles storing the underlying model data, and optionally, syncing that data across multiple devices.

SwiftData has uses beyond persisting locally created content. For example, an app that fetches data from a remote web service might use SwiftData to implement a lightweight caching mechanism and provide limited offline functionality.

![A white Swift logo containing ones and zeros on a blueprint-style background.](../../attachments/aa99d190da3e4c58796b4201d5e7b4c7/swiftdata-hero@2x.png)

SwiftData is unintrusive by design and supplements your app’s existing model classes. Attach the [Model()](<swiftdata/model().md>) macro to any model class to make it persistable. Customize the behavior of that model’s properties with the [Attribute(_:originalName:hashModifier:)](<swiftdata/attribute(__originalname_hashmodifier_).md>) and [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](<swiftdata/relationship(__deleterule_minimummodelcount_maximummodelcount_originalname_inverse_hashmodifier_).md>) macros. Use the [ModelContext](swiftdata/modelcontext.md) class to insert, update, and delete instances of that model, and to write unsaved changes to disk.

To display models in a SwiftUI view, use the [Query()](<swiftdata/query().md>) macro and specify a predicate or fetch descriptor. SwiftData performs the fetch when the view appears, and tells SwiftUI about any subsequent changes to the fetched models so the view can update accordingly. You can access the model context in any SwiftUI view using the [modelContext](swiftui/environmentvalues/modelcontext.md) environment value, and specify a particular model container or context for a view with the [modelContainer(_:)](<swiftui/view/modelcontainer(__).md>) and [modelContext(_:)](<swiftui/view/modelcontext(__).md>) view modifiers.

## Topics

### Essentials

- [Preserving your app’s model data across launches](swiftdata/preserving-your-apps-model-data-across-launches.md) — Describe your model classes to SwiftData using the framework’s macros, and store instances of those models so they exist beyond the app’s runtime.
- [Adding and editing persistent data in your app](swiftdata/adding-and-editing-persistent-data-in-your-app.md) — Create a data entry form for collecting and changing data managed by SwiftData.
- [Adopting SwiftData for a Core Data app](coredata/adopting-swiftdata-for-a-core-data-app.md) — Persist data in your app intuitively with the Swift native persistence framework. _(beta)_
- [SwiftData updates](updates/swiftdata.md) — Learn about important changes to SwiftData.
- [Adopting inheritance in SwiftData](swiftdata/adopting-inheritance-in-swiftdata.md) — Add flexibility to your models using class inheritance.

### Model definition

- [Model()](<swiftdata/model().md>) — Converts a Swift class into a stored model that’s managed by SwiftData.
- [Attribute(_:originalName:hashModifier:)](<swiftdata/attribute(__originalname_hashmodifier_).md>) — Specifies the custom behavior that SwiftData applies to the annotated property when managing the owning class.
- [Unique(_:)](<swiftdata/unique(__).md>) — Specifies the key-paths that SwiftData uses to enforce the uniqueness of model instances.
- [Index(_:)](<swiftdata/index(__)-74ia2.md>) — Specifies the key-paths that SwiftData uses to create one or more binary indices for the associated model.
- [Index(_:)](<swiftdata/index(__)-7d4z0.md>) — Specifies the key-paths that SwiftData uses to create one or more indicies for the associated model, where each index is either binary or R-tree.
- [Defining data relationships with enumerations and model classes](swiftdata/defining-data-relationships-with-enumerations-and-model-classes.md) — Create relationships for static and dynamic data stored in your app.
- [Relationship(_:deleteRule:minimumModelCount:maximumModelCount:originalName:inverse:hashModifier:)](<swiftdata/relationship(__deleterule_minimummodelcount_maximummodelcount_originalname_inverse_hashmodifier_).md>) — Specifies the options that SwiftData needs to manage the annotated property as a relationship between two models.
- [Transient()](<swiftdata/transient().md>) — Tells SwiftData not to persist the annotated property when managing the owning class.

### Model life cycle

- [ModelContainer](swiftdata/modelcontainer.md) — An object that manages an app’s schema and model storage configuration.
- [ModelContext](swiftdata/modelcontext.md) — An object that enables you to fetch, insert, and delete models, and save any changes to disk.
- [Fetching and filtering time-based model changes](swiftdata/fetching-and-filtering-time-based-model-changes.md) — Track all inserts, updates, and deletes that occur in a data store and process them as a series of chronological transactions.
- [HistoryDescriptor](swiftdata/historydescriptor.md) — A type that describes the criteria, and, optionally, sort order, to use when fetching history data
- [Deleting persistent data from your app](swiftdata/deleting-persistent-data-from-your-app.md) — Explore different ways to use SwiftData to delete persistent data.
- [Reverting data changes using the undo manager](swiftdata/reverting-data-changes-using-the-undo-manager.md) — Automatically record data change operations that people perform in your SwiftUI app, and let them undo and redo those changes.
- [Syncing model data across a person’s devices](swiftdata/syncing-model-data-across-a-persons-devices.md) — Add the required capabilities and define a compatible schema to enable SwiftData to automatically sync your app’s model data using iCloud.
- [Concurrency support](swiftdata/concurrencysupport.md) — Types you use to access model attributes and perform storage-related tasks in a safe and isolated way.

### Model fetch

- [Filtering and sorting persistent data](swiftdata/filtering-and-sorting-persistent-data.md) — Manage data store presentation using predicates and dynamic queries.
- [Query()](<swiftdata/query().md>) — Fetches all instances of the attached model type.
- [Additional query macros](swiftdata/additionalquerymacros.md) — Supplementary macros that enable you to narrow query results and tell SwiftData how to sort, order, and section those results.
- [Query](swiftdata/query.md) — A type that fetches models using the specified criteria, and manages those models so they remain in sync with the underlying data.
- [FetchDescriptor](swiftdata/fetchdescriptor.md) — A type that describes the criteria, sort order, and any additional configuration to use when performing a fetch.

### Model storage

- [Maintaining a local copy of server data](swiftdata/maintaining-a-local-copy-of-server-data.md) — Create and update a persistent store to cache read-only network data.
- [DefaultStore](swiftdata/defaultstore.md) — A data store that uses Core Data as its undelying storage mechanism.
- [DataStore](swiftdata/datastore.md) — An interface that enables SwiftData to read and write model data without knowledge of the underlying storage mechanism.
- [DataStoreBatching](swiftdata/datastorebatching.md) — An interface that enables a custom data store to support batch requests.
- [HistoryProviding](swiftdata/historyproviding.md) — An interface that enables a custom data store to provide the history of changes for its persisted models.
- [Building a document-based app using SwiftData](swiftui/building-a-document-based-app-using-swiftdata.md) — Code along with the WWDC presenter to transform an app with SwiftData.
- [ModelDocument](swiftdata/modeldocument.md) — A document type that uses SwiftData to manage its storage.

### History life cycle

- [HistoryChange](swiftdata/historychange.md) — Values that describe data history transactions.
- [HistoryDelete](swiftdata/historydelete.md) — An interface that enables a custom data store to delete items from the history of changes to its persisted models.
- [HistoryInsert](swiftdata/historyinsert.md)
- [HistoryToken](swiftdata/historytoken.md)
- [HistoryTransaction](swiftdata/historytransaction.md)
- [HistoryUpdate](swiftdata/historyupdate.md)
- [HistoryTombstone](swiftdata/historytombstone.md)
- [DefaultHistoryInsert](swiftdata/defaulthistoryinsert.md)
- [DefaultHistoryUpdate](swiftdata/defaulthistoryupdate.md)
- [DefaultHistoryDelete](swiftdata/defaulthistorydelete.md)
- [DefaultHistoryToken](swiftdata/defaulthistorytoken.md)
- [DefaultHistoryTransaction](swiftdata/defaulthistorytransaction.md)

### Data store observation

- [ResultsObserver](swiftdata/resultsobserver.md) — Observes and tracks changes to a collection of persistent models in a model context. _(beta)_
- [HistoryObserver](swiftdata/historyobserver.md) — Monitors a model container’s data stores for remote changes and notifies when new history transactions are available. _(beta)_

### Codeable support

- [DataStoreSnapshotCodingKey](swiftdata/datastoresnapshotcodingkey.md) — The key space to use when implementing custom coders and decoders for data store snapshots,

### Errors

- [SwiftDataError](swiftdata/swiftdataerror.md) — A type that describes a SwiftData error.
- [DataStoreError](swiftdata/datastoreerror.md) — A type that describes a data store error.
