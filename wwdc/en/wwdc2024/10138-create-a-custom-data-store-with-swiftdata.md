---
title: Create a custom data store with SwiftData
session_id: 10138
collection: wwdc2024
year: 2024
duration: '13:52'
topics: [App Services, Swift]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10138/'
content_hash: 'sha256:fbe35bba5505e8bf'
translated: false
---

# Create a custom data store with SwiftData

<sub>WWDC2024 · 13:52 · App Services、Swift</sub>

Combine the power of SwiftData's expressive, declarative modeling API with your own persistence backend. Learn how to build a custom data...

> [!note] 归档理由
> 自定义数据存储后端，看清 SwiftData 抽象层

## Chapters

- [Introduction](/videos/play/wwdc2024/10138/?time=0)
- [Overview](/videos/play/wwdc2024/10138/?time=81)
- [Meet DataStore](/videos/play/wwdc2024/10138/?time=290)
- [Example store](/videos/play/wwdc2024/10138/?time=462)

## Resources

- [Introduction](https://developer.apple.com/videos/play/wwdc2024/10138/?time=0)
- [Overview](https://developer.apple.com/videos/play/wwdc2024/10138/?time=81)
- [Meet DataStore](https://developer.apple.com/videos/play/wwdc2024/10138/?time=290)
- [Example store](https://developer.apple.com/videos/play/wwdc2024/10138/?time=462)
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010)
- [SwiftData](https://developer.apple.com/documentation/SwiftData)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10138/4/A149C0AB-2AB1-48C1-B259-4D5621873D5F/downloads/wwdc2024-10138_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10138/4/A149C0AB-2AB1-48C1-B259-4D5621873D5F/downloads/wwdc2024-10138_sd.mp4?dl=1)
- [Track model changes with SwiftData history](https://developer.apple.com/videos/play/wwdc2024/10075)
- [Implement a JSON store](https://developer.apple.com/videos/play/wwdc2024/10138/?time=495)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

Hi everyone! My name is Luvena, and I’m excited to chat with you about custom DataStores in SwiftData, a way to use SwiftData with your own persistence backend. Custom data stores are a new feature in SwiftData that allow you to use any document, file format, or persistence backend of your choice. And they work great with all of your existing SwiftData code.

Here, in the implementation for the SampleTrips app, I can change the type of store just by replacing the ModelConfiguration with the JSONStoreConfiguration, an example I will implement later in this video. With just this one replacement, the ModelContainer now knows to use a different store type, without requiring me to change any of the model or view code in the SampleTrips app.

In this video I will first introduce the role a store plays in SwiftData and how it interacts with the ModelContext and ModelContainer.

Then, I’ll explore how they are built using the new DataStore protocol. Finally, I’ll cover the essentials of implementing a custom DataStore by taking you through an example that uses a JSON file for persistence. At a high level, the store is responsible for fetching and saving all of the data required to support the persistent models. To explore how custom data stores work in SwiftData, I’m going to examine how they provide persistence for my app, SampleTrips. SampleTrips is built on the powerful synergy of SwiftUI and SwiftData. And a typical app is composed of three important parts. SwiftUI provides the user interface, typically a view, like a list or label that displays data from a Model in a ModelContext The ModelContext reads and writes data using a store in a ModelContainer. In this video I'm going to focus specifically on the role the store plays in SwiftData.

SampleTrips uses a ModelContext to power the view and display the trips. The ModelContext instantiates persistent models for each trip in the view. Each of these trips also have a corresponding Persistent Identifier that uniquely identifies the model. And the ModelContext tracks the changes I make so they can be saved to the store when needed.

For example if I decide to cancel my trip to Los Angeles, and also add a new trip to Tokyo, these changes are tracked by the ModelContext. When the new Tokyo model is inserted in to the model context, it is identified by a temporary PersistentIdentifier. When the ModelContext saves, it tells the store to delete the Los Angeles trip and insert the new Tokyo trip.

The store will then assign the Tokyo model a permanent persistent identifier, Trip-5, and map it to its former temporary identifier, Trip-t1, in a process known as “remapping”.

The store then responds to the ModelContext with the updated persistent identifier for the Tokyo trip.

After the model context finishes updating its state, the UI can update the view rendering the trips.

Persisting changes is just one example of how the ModelContext and store work together to support PersistentModels in SwiftData. They communicate using a set of requests and responses that define operations like fetch or save. The store's role is to provide the implementation for how model values are persisted. This communication leverages a sendable, codable representation of the model called the DataStoreSnapshot.

In the SampleTrips app, the view communicates with the ModelContext using persistent models.

However, when the ModelContext needs to communicate with a store, it creates a snapshot to hold the current state of the model.

The snapshot is a sendable, codable container of the values in the model at that point in time. Like persistent models, each is identified by a Persistent Identifier.

The store then consumes these snapshots and applies the values to its storage. And the reverse is also true.

When data is read by the ModelContext from the store, the store creates a set of snapshots that align with the PersistentModels the context is asking for.

The ModelContext then creates PersistentModels for each snapshot for use in views, queries, or other work the context is doing.

Stores play a critical role in SwiftData allowing the ModelContext to read and write model data to any storage format. Let me take you through the new DataStore protocol and how it makes this possible.

There are three key parts to a store: a configuration to describe the store, snapshots to communicate model values with the model context, and a store implementation that the ModelContainer can manage. Each of these parts conform to three different protocols: DataStoreConfiguration, DataStoreSnapshot, and DataStore.

The default store in SwiftData provides its own implementation of these types: ModelConfiguration, DefaultSnapshot, and the DefaultStore. The DefaultStore supports all the rich features of SwiftData like migration, history tracking, and CloudKit sync. And it encapsulates the platforms best practices for performance and scalability, making it the best default choice for persisting models.

The DataStore protocol defines all of the functionality SwiftData needs for the store to be usable by the ModelContext, including save, fetch, and caching. Additional protocols define optional data store features, like the new History protocol for describing all of the changes made to a store.

The model context communicates with stores using requests and responses from the DataStore protocol.

For example, when fetching data from a store, the ModelContext sends the store a DataStoreFetchRequest containing the FetchDescriptor that describes the data the store should retrieve.

Once the store retrieves the model values, It creates a snapshot for each model, and returns them in a DataStoreFetchResult.

Then the ModelContext creates a PersistentModel for each of the snapshots.

A similar process happens when models are changed in a model context and save is called. The model context creates a DataStoreSaveChangesRequest containing snapshots for all of the modified models, and sends the request to the store.

Then, the store applies the snapshots to its storage and creates a DataStoreSaveChangesResult to send back to the ModelContext. In the result, the store provides a map of the remapped identifiers for any newly inserted models, like Trip-t1. This tells the model context to update the persistent identifier for the inserted Trip to Trip-5.

Finally, the model context processes the save result from the store and updates its state, assigning the new permanent persistent identifier to the inserted trip.

Now that I’ve covered the mechanics of a DataStore, I want to explore what it's like to actually implement one. I'll implement a store that uses a JSON file to persist the models in the SampleTrips application. Before I get started, there are two points I'd like to clarify. This store is an “archival store”, meaning the entire file is loaded when reading or writing.

Additionally, I'll be using the JSON coders provided by Foundation and storing data as an array of snapshots in the file.

The first step to creating a store is to declare the configuration and store types that conform to the DataStoreConfiguration and DataStore protocols.

These types reference each other using associated types. On the configuration, I set the Store type as JSONStore and on the store I set Configuration to JSONStoreConfiguration.

Additionally, the JSONStore declares the type of snapshot it uses to communicate with the ModelContext. Here, I am using the DefaultSnapshot, because I don't need to customize the encoding or decoding of the model data.

Now I can begin implementing the two required methods for a DataStore to be usable with the ModelContext: fetch and save.

When the ModelContext sends a DataStoreFetchRequest, I need to load the data that’s in the store, and instantiate a DataStoreFetchResult.

Because the DefaultSnapshot is codable, I can use the JSONDecoder to load the data for the store from the file URL provided by the configuration.

Then, I'll instantiate and return a DataStoreFetchResult with the snapshots from the file. Currently, this implementation doesn't process the predicate or sort comparators that are on a FetchDescriptor. The translation of a Predicate or sort comparator can be an involved process, and I can instead use the ModelContext to perform this work for me.

To do this, I’ll throw the `preferInMemoryFilter` and `preferInMemorySort` errors when the request contains a predicate or sort descriptor. This works great for my case, because this is a small data set that can be loaded into memory. I now have a fully functional fetch implementation that can support queries and sorting. With fetch implemented, I can implement save to write the snapshots in to the JSON file. When implementing save, I want to consider and handle 3 types of changes: insertions, updates, and deletions.

Before I begin processing the incoming snapshots in the save request, I first have to read in the current contents of the file, which I handle in a separate method that I defined called read. I’ll organize all of the snapshots into a dictionary keyed by their persistent identifier, which will be my working copy for the new JSON file that will be written to disk at the end.

Then I process the snapshots of the inserted models within the save request. This involves assigning and remapping identifiers for each inserted snapshot. Let me examine this in a little more detail.

Recall that when models are inserted into the store, each model contains a temporary identifier that’s not associated with any store. For each inserted snapshot here, I create a new, permanent persistent identifier. I then create a copy of the snapshot that uses the new persistent identifier.

This new persistent identifier is mapped to the temporary one in the remappedIdentifiers dictionary to return to the ModelContext later in the save result. Finally, I add the inserted snapshots to the ones initially loaded from the file.

After processing the inserted snapshots, I process the updates by replacing the snapshots from the file with the ones in the save request.

And finally, I remove the deleted snapshots from those loaded from the file. I now have a complete and updated set of data in the snapshotsByIdentifier dictionary that I want to write back to the file.

I’ll use the JSONEncoder to write this working copy of the snapshots back to disk in a single JSON file.

Finally, I return a DataStoreSaveChangesResult with the results of the save. The DataStoreSaveChangesResult includes the remapped persistentIdentifiers for the context to update.

Now that I have a complete custom data store, I can adopt it in SampleTrips. In the app definition, I can change the type of store just by replacing the ModelConfiguration with the JSONStoreConfiguration. With just this one replacement, the ModelContainer now knows to use a different store type, without requiring me to change any of the model or view code in the SampleTrips app.

With DataStore, SwiftData can read and write data to any storage format or persistence backend.

This allows you to use the power of SwiftUI and PersistentModel with any document, database, or cloud storage you need, while the ModelContext helps reduce the complexity of simple store implementations by providing filtering and sorting for you.

Adopting a custom store in SwiftData is as straightforward as just changing the DataStoreConfiguration, And with the new DataStore protocol you can implement support for any persistence backend. This opens SwiftData to a huge range of new possibilities.

Be sure to check out "What's New in SwiftData" to learn about other new features like Indexing and Unique constraints. And don't miss "Track model changes with SwiftData History" to learn all about how you can examine the history of a store.

Thanks for joining me! I can’t wait to see what you build.
