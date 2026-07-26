---
title: Track model changes with SwiftData history
session_id: 10075
collection: wwdc2024
year: 2024
duration: '16:52'
topics: [App Services, Swift]
group: H · 持久化与文件系统
evergreen: true
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10075/'
content_hash: 'sha256:bffbe518c3b49c3f'
translated: false
---

# Track model changes with SwiftData history

<sub>WWDC2024 · 16:52 · App Services、Swift</sub>

Reveal the history of your model's changes with SwiftData! Use the history API to understand when data store changes occurred, and learn...

> [!note] 归档理由
> 历史追踪（change history）机制

## Chapters

- [Introduction](/videos/play/wwdc2024/10075/?time=0)
- [Fundamentals](/videos/play/wwdc2024/10075/?time=45)
- [Transactions and changes](/videos/play/wwdc2024/10075/?time=318)
- [Custom stores](/videos/play/wwdc2024/10075/?time=757)

## Resources

- [Introduction](https://developer.apple.com/videos/play/wwdc2024/10075/?time=0)
- [Fundamentals](https://developer.apple.com/videos/play/wwdc2024/10075/?time=45)
- [Transactions and changes](https://developer.apple.com/videos/play/wwdc2024/10075/?time=318)
- [Custom stores](https://developer.apple.com/videos/play/wwdc2024/10075/?time=757)
- [Fetching and filtering time-based model changes](https://developer.apple.com/documentation/SwiftData/Fetching-and-filtering-time-based-model-changes)
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010)
- [SwiftData](https://developer.apple.com/documentation/SwiftData)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10075/4/0F3D64B6-B594-42E8-8B59-2088D1B251F8/downloads/wwdc2024-10075_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10075/4/0F3D64B6-B594-42E8-8B59-2088D1B251F8/downloads/wwdc2024-10075_sd.mp4?dl=1)
- [Create a custom data store with SwiftData](https://developer.apple.com/videos/play/wwdc2024/10138)
- [Preserve values in history on deletion](https://developer.apple.com/videos/play/wwdc2024/10075/?time=297)
- [Fetch transactions from history](https://developer.apple.com/videos/play/wwdc2024/10075/?time=386)
- [Process history changes](https://developer.apple.com/videos/play/wwdc2024/10075/?time=454)
- [Save and use a history token](https://developer.apple.com/videos/play/wwdc2024/10075/?time=619)
- [Update the user interface](https://developer.apple.com/videos/play/wwdc2024/10075/?time=690)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

Salutations! My name is David, and I’m an engineer on the SwiftData team. SwiftData History is a new technology that lets your app track modifications to its data. You can use History to build features that need to process these changes, like syncing with your server, or responding to changes from an app extension. In this video, I’ll cover the fundamentals of SwiftData History, and build a new feature in my sample app using History transactions and changes.

Finally, I’ll cover some considerations for supporting History with a custom data store.

Let’s talk about what SwiftData History is, and why you might want to use it.

As people use an app, the content stored by SwiftData changes over time. For example, when the app launches, it may create some models, or insert models fetched from a remote server.

When the model context is saved, all pending changes are saved into the data store.

Over time, some of these models may change, or be deleted as someone uses and interacts with your app, and its different functions.

At any time, your app can query the data in the store. However, a query’s results represent what’s currently in the data store. Without history or manual diffing, there’s no way to know from a query which models may have been added, deleted, or updated since a previous one. SwiftData History provides an easy and efficient way to track the changes in your data store over time.

You can use this to build a number of different features. For example, you may want to have a time-ordered log of changes that occur when the app is offline. Later, these changes can be efficiently synced with a remote server.

You may want to discover changes in the data that occurred in a different process, like a widget extension, so that you can reflect those changes properly in your app.

Or, you may simply want an efficient way to know which models were inserted or deleted since a previous query, in order to update some state at runtime. Let’s explore how it works.

SwiftData History lets your app query and process changes in the order that they occurred.

Each time your model is saved, it records a transaction, which contains metadata about all of the changes.

SwiftData History is composed of Transactions and Changes. Transactions group together all of the changes that occurred in the data store on a boundary, such as on a ModelContext save. Transactions are ordered by when they occurred.

Within a transaction, the set of changes it contains also preserve the order in which each change occurred. Each change represents a model that has been inserted, updated, or deleted and are parameterized by a PersistentModel. This allows references to properties of the PersistentModel using KeyPaths.

SwiftData History uses the concept of a token, which acts as a bookmark for transactions in History. A token can help your app keep track of the last transaction it processed in the stream of History.

Tokens are only valid for the data stores they are associated with. In SwiftData, history information can be deleted through the model context.

When that happens, tokens from deleted parts of history become expired and cannot be used for fetches.

SwiftData History operations involving an expired token will throw a historyTokenExpired error. If this happens, discard the token, as it is no longer valid and fetch a new one.

When models are deleted, the data in the model is discarded. This means that essential data like identifiers might be lost and don’t provide enough information to your app when processing history information. To address this, SwiftData History lets you preserve specific attributes on a model. When the model is deleted, these attributes are preserved as tombstone values, and let you process the history information for the deleted models.

Attributes in a PersistentModel that have been marked with the modifier.preserveValueOnDeletion are preserved in the tombstone. Tombstones are also parameterized by a PersistentModel, so that their KeyPaths can be used to retrieve the tombstone values or iterated as desired.

History in SwiftData is easy to consume and built on the rich type system of Swift. Let’s explore how to use it in an app. To see it in action, I’m going to work on a new feature for the SampleTrips app. This app lets me record all of my favorite trips, to help me plan my next vacation.

I want to add a new feature where Trips that have unread changes are badged for my review. This can happen outside the app in the context of a sync from a remote server or in the app’s widget.

In the widget, I am going to add the capability to confirm a given living accommodation right from my Home Screen. Using SwiftData History, I can build this feature by finding out when this data changed, who changed it and update the UI.

To do this, I am going to break the task into three steps: Fetch SwiftData History, process the changes by inspecting the properties on the change, and finally, update my user interface. To start, I’ll build a function that fetches transactions in the data store based on a token parameter and author. In this case, the token is of type DefaultHistoryToken, because the app uses the DefaultStore in SwiftData.

Next, I’ll create a HistoryDescriptor, which lets me configure constraints for my request.

I’ll build a predicate that constrains the transaction to have occurred after the provided token.

Since I want this function to only surface changes from my widget, I’ll also add a constraint to fetch changes authored by a specified author. If I’m calling this function without a token, I’ll just fetch all of the available history.

Next, I’ll create an array that will contain all of the transactions that need to be processed. And I’ll call fetchHistory on the ModelContext using the descriptor. This will provide a set of DefaultHistoryTransactions that I can then iterate through. Now that I am able to retrieve the transactions I care about, I'm going to define another function for processing them. This function will accept an array of transactions and return a set of Trips that need to be badged having unread changes and a token. Each time the function runs, it will return a new token that I can use the next time I want to find changes.

I’ll begin by defining a ModelContext and a set that will store my trips with unread changes.

For each transaction and change in a transaction, the History API provides the persistent model id. To get the model instance for the Trip, I’ll build a fetch descriptor for LivingAccommodation using that persistent model id. Then, I’ll fetch that model from the model context and store the trip associated with the LivingAccommodation.

To determine if a change in a transaction represents an insert, update, or deletion, I’ll use a switch statement to check its type.

In the app, I want to apply a badge in the UI if my widget inserts, changes, or deletes a LivingAccommodation model. To do that, I’ll start by checking for changes of type DefaultHistoryInsert for LivingAccommodation. If this case matches, it represents an insert of a LivingAccommodation, so add this trip to the set. Again, notice that the type is called DefaultHistoryInsert because in this case, I’m using the DefaultStore for this model. I’ll also check for updates by adding a case for the type DefaultHistoryUpdate of a LivingAccommodation. If this change is an update, I’ll update the trip in the set.

If the trip is deleted, there’s nothing I need to do in the app’s interface. To handle this, I’ll add a case for the type DefaultHistoryDelete of a LivingAccommodation and remove it from my set.

Finally, I’ll return the last token along with my set of trips, so that future calls to this function return only the changes that have occurred after that transaction.

Using SwiftData History, the app can now discover which Trips were changed from the widget since the last time the app checked for changes. Now, I need to store this token, so that it only considers changes since the last time changes were discovered. To do this, I’ll define a third function and use UserDefaults to store the most recent token. In my function findUnreadTrips, I’ll fetch the token, if there’s one available, and decode it from JSON, before calling my findTransactions function with that token. The author I want to specify is the widget so, in the widget, I’ve set the.author property on a ModelContext equal to TransactionAuthor.widget.

After calling findTrips I’ll store the returned token back into UserDefaults. Now, each time I call findUnreadTrips, it will only return Trips which need to be badged since the last time it was called.

My feature is almost ready. There’s just two more pieces I need to add: One, when the app is opened, I’ll check for unread trips and two, when a trip is tapped on, I’ll remove it from the set of unread trips, so that the badge disappears. On my SwiftUI view, I’ll call findUnreadTripIdentifiers any time the scene phase becomes active. This will update the interface with the new trips that need to be badged.

Then, when a trip is selected, I’ll remove its identifier from the unreadTripIdentifiers set, so that the badge disappears.

Finally, I’ll add the badge to any Trip that is contained within the unreadTripIdentifiers set.

Now that all the required code is implemented, I’ll build and run the app. There is already a trip entered in the app and I want to confirm the living accommodations in my widget right on the home screen.

I’ll tap Accommodation and the UI will change to indicate it is confirmed. The next time I launch the trips app, the trip to the formation flyover will have a blue unread badge indicating there's been changes to that trip. After reviewing the trip, the badge is removed.

For those of you building custom data stores with SwiftData, your custom store can also support history. If your underlying model supports it, you can support these same workflows with your store implementation as well. To add history to your custom data store, you’ll need to implement your own types to represent the fundamental elements of the SwiftData History API for your data store. This includes transactions, each type of change, and a token, to act as a bookmark between transactions. In addition, your custom data store will need to conform to HistoryProviding.

The boundaries of a transaction will need to be well-defined because write operations in your data store need to be coalesced and ordered In the default store, all of the changes to model instances on the ModelContext at save time are grouped as a single transaction.

When you create your transaction type, you’ll need to define a way to uniquely identify a transaction within your persistence back end. Similarly to transactions, what defines the boundaries of a change must be well-defined. In the DefaultStore, the boundaries of a change are scoped to an individual model instance.

Pick an identifier that can track the granular nature of these changes.

It’s possible that your app may not need all of the existing change types, or, it may need different change types. For example, if your app only ever inserts models as a time-series log you may not need update and delete change types. An additional consideration, is if your app will need to support preserving values on deletion and how the deleted values will be stored.

The custom store will need to implement the HistoryProviding protocol to vend history. This will require being able to pull together rows from the store that define the transaction and changes.

After identifying which rows are part of a transaction, you’ll need to build the specific sets of models.

The default data store manages the time to live of history records. As a custom provider, you’ll need to decide when to delete history. While SwiftData History is robust, and can handle a large amount of history data, in some specific cases, you may want to delete history. For example, if you remove models from your app, there may be history data about those models that you would never use going forward. In that case, you might like to delete this history from the data store.

Finally, when adding history support to your custom store, you’ll need to create a custom type of token. HistoryToken is the base protocol for a token. The state is needed to uniquely identify your position in the stream of transactions.

Consider if your app uses multiple, related stores. Your custom token should include the state of all the stores used in the transaction.

History is a powerful feature that lets you query for changes, like discovering the update from the widget in Trips. SwiftData uses Swift’s expressive type system to make it easy to understand how each model change gets used in your app. You can build delightful experiences in your app with SwiftData History. For those of you using co-existence with Core Data to benefit from persistent history, you can now migrate to SwiftData History instead. And if you’re building a custom store, you can support all of the features of history tracking by creating your own history types. Thanks for watching.
