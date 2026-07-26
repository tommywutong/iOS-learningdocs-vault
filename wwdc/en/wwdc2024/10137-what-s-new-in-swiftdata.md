---
title: What’s new in SwiftData
session_id: 10137
collection: wwdc2024
year: 2024
duration: '14:01'
topics: [App Services, Swift]
group: H · 持久化与文件系统
evergreen: false
source_url: 'https://developer.apple.com/videos/play/wwdc2024/10137/'
content_hash: 'sha256:6a6459e459b349f2'
translated: false
---

# What’s new in SwiftData

<sub>WWDC2024 · 14:01 · App Services、Swift</sub>

SwiftData makes it easy to add persistence to your app with its expressive, declarative API. Learn about refinements to SwiftData,...

> [!note] 归档理由
> SwiftData 年度更新

## Chapters

- [Introduction](/videos/play/wwdc2024/10137/?time=0)
- [Adopt SwiftData](/videos/play/wwdc2024/10137/?time=57)
- [Customize the schema](/videos/play/wwdc2024/10137/?time=131)
- [#Unique macro](/videos/play/wwdc2024/10137/?time=163)
- [History API](/videos/play/wwdc2024/10137/?time=217)
- [Tailor a model container](/videos/play/wwdc2024/10137/?time=269)
- [Custom data stores](/videos/play/wwdc2024/10137/?time=339)
- [Xcode previews](/videos/play/wwdc2024/10137/?time=401)
- [Customize queries](/videos/play/wwdc2024/10137/?time=560)
- [#Expression macro](/videos/play/wwdc2024/10137/?time=618)
- [#Index macro](/videos/play/wwdc2024/10137/?time=716)

## Resources

- [Introduction](https://developer.apple.com/videos/play/wwdc2024/10137/?time=0)
- [Adopt SwiftData](https://developer.apple.com/videos/play/wwdc2024/10137/?time=57)
- [Customize the schema](https://developer.apple.com/videos/play/wwdc2024/10137/?time=131)
- [#Unique macro](https://developer.apple.com/videos/play/wwdc2024/10137/?time=163)
- [History API](https://developer.apple.com/videos/play/wwdc2024/10137/?time=217)
- [Tailor a model container](https://developer.apple.com/videos/play/wwdc2024/10137/?time=269)
- [Custom data stores](https://developer.apple.com/videos/play/wwdc2024/10137/?time=339)
- [Xcode previews](https://developer.apple.com/videos/play/wwdc2024/10137/?time=401)
- [Customize queries](https://developer.apple.com/videos/play/wwdc2024/10137/?time=560)
- [#Expression macro](https://developer.apple.com/videos/play/wwdc2024/10137/?time=618)
- [#Index macro](https://developer.apple.com/videos/play/wwdc2024/10137/?time=716)
- [Forum: Programming Languages](https://developer.apple.com/forums/topics/programming-languages-topic?cid=vf-a-0010)
- [SwiftData](https://developer.apple.com/documentation/SwiftData)
- [Adopting SwiftData for a Core Data app](https://developer.apple.com/documentation/CoreData/adopting-swiftdata-for-a-core-data-app)
- [HD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10137/4/44213251-C991-4280-BBF1-5CA6AFCA5222/downloads/wwdc2024-10137_hd.mp4?dl=1)
- [SD Video](https://devstreaming-cdn.apple.com/videos/wwdc/2024/10137/4/44213251-C991-4280-BBF1-5CA6AFCA5222/downloads/wwdc2024-10137_sd.mp4?dl=1)
- [Create a custom data store with SwiftData](https://developer.apple.com/videos/play/wwdc2024/10138)
- [Track model changes with SwiftData history](https://developer.apple.com/videos/play/wwdc2024/10075)
- [Meet SwiftData](https://developer.apple.com/videos/play/wwdc2023/10187)
- [SampleTrips models decorated with @Model](https://developer.apple.com/videos/play/wwdc2024/10137/?time=92)
- [SampleTrips using modelContainer scene modifier](https://developer.apple.com/videos/play/wwdc2024/10137/?time=103)
- [SampleTrips using @Query](https://developer.apple.com/videos/play/wwdc2024/10137/?time=113)
- [SampleTrips models decorated with @Model](https://developer.apple.com/videos/play/wwdc2024/10137/?time=136)
- [Add unique constraints to avoid duplication](https://developer.apple.com/videos/play/wwdc2024/10137/?time=188)
- [Add .preserveValueOnDeletion to capture unique columns](https://developer.apple.com/videos/play/wwdc2024/10137/?time=216)
- [SampleTrips using modelContainer scene modifier](https://developer.apple.com/videos/play/wwdc2024/10137/?time=275)
- [Customize a model container in the app](https://developer.apple.com/videos/play/wwdc2024/10137/?time=292)
- [Add a model container to the app](https://developer.apple.com/videos/play/wwdc2024/10137/?time=313)
- [Use your own custom data store](https://developer.apple.com/videos/play/wwdc2024/10137/?time=359)
- [Make preview data using traits](https://developer.apple.com/videos/play/wwdc2024/10137/?time=418)
- [Use sample data in a preview](https://developer.apple.com/videos/play/wwdc2024/10137/?time=495)
- [Create a preview query using @Previewable](https://developer.apple.com/videos/play/wwdc2024/10137/?time=530)
- [Create a predicate to find a Trip based on search text](https://developer.apple.com/videos/play/wwdc2024/10137/?time=595)
- [Create a Compound Predicate to find a Trip based on Search Text](https://developer.apple.com/videos/play/wwdc2024/10137/?time=606)
- [Build a predicate to find Trips with BucketListItems that are not in the plan](https://developer.apple.com/videos/play/wwdc2024/10137/?time=646)
- [Add Index for commonly used KeyPaths or combination of KeyPaths](https://developer.apple.com/videos/play/wwdc2024/10137/?time=761)

## Transcript

> [!warning] 关于逐字稿
> 这份逐字稿是 Apple 的自动语音识别产物，**未经人工校对**，可能有术语转写错误。段落已按原始 HTML 的 `<p>` 结构重组，但断句仍可能不自然。

Hello, I am Rishi Verma, and I am an engineer on the SwiftData Team. I am excited to share with you today all that is new in SwiftData.

iOS 17 introduced SwiftData — a framework that allows you to model and persist your app’s data in Swift across all of Apple’s platforms. It lets you write code that is fast, efficient, and safe by harnessing modern Swift language features, like macros. In this video, we’ll start with a quick re-introduction to the SwiftData framework, and dive into what’s new, starting with how to avoid duplicate models with a new Schema Macro! Then, we’ll cover new ways you can set up and configure model containers.

And lastly, a deep dive into how to optimize queries with complex filters and harness a new macro to improve performance! First, let’s take a quick tour of SwiftData. SwiftData is a framework that makes it easy to build your app’s model layer and persist it across launches of your app.

The framework not only provides persistence, but modeling and migration of your schema, Graph management, synchronization with CloudKit and so much more! To show you how easy it is to adopt SwiftData in your app, let me show you an app that me and team have been working on — Trips! Trips is an app written in SwiftUI, and keeps track of all the different vacation ideas I’m thinking about.

To use SwiftData with the models in this app, I just needed to import the framework, and decorate each model with the @Model macro - this is the powerhouse of SwiftData! And in the app’s definition, the modelContainer modifier on the WindowGroup tells the entire view hierarchy about the model Trip.

With this in place, my views can remove static data, and instead populate the view using @Query. This will fetch Trip models from the model container and return an array of Trips. And that is it! The app now persists all of the trips that I create, and fits perfectly into my SwiftUI views.

The first step was adding the @Model macro and that was just the beginning of how to customize the Schema.

The @Model macro is powerful and jump starts the persistence experience. By simply decorating all of my persistable classes with the macro, the Trip class and related models will have their stored properties persisted.

And you can go even further to customize the schema with the macros for @Attributes and @Relationships and the ability to mark a stored property as @Transient to avoid persisting that data.

And this year, there is a new schema macro that allows you to construct a compound constraint on persistent models! You can use the new #Unique macro to tell SwiftData which combinations of your model’s properties must always remain unique in the model data. When two model instances share the same unique values, SwiftData will perform an upsert on collision with an existing model! For example, in the Trips app, I can use the #Unique macro to ensure trips are unique across their name, startDate, and endDate. This lets my app have multiple trips with the same name, but only if they have different start or end dates. This makes it really easy to avoid duplicates in the data, since SwiftData has more information to reason about which models actually represent duplicates, and performs updates to the data instead.

And because these #Unique properties help ensure these @Models are not duplicated, they also represent the identity of this model. You can also use the @Attribute macro to decorate these properties with preserveValueOnDeletion. This will ensure these identity values will be available when using the history API in SwiftData.

SwiftData history provides a way for your app to know what models have been inserted, updated, or deleted over time. When models are deleted, values marked to be preserved are kept in the history information as tombstone values, giving your app the information it may need to process those changes. It also works seamlessly with custom data stores built to support it. To learn more, watch the video “Track model changes with SwiftData history”.

Tailoring the model container allows an app to fine tune its data location and how it is used throughout the app.

The modelContainer modifier is the easiest way to get started with SwiftData. Just by providing the model types to persist, SwiftData sets up a container for you. The modelContainer modifier also lets you customize some of the properties of the container.

For example, it can keep data in memory, rather than on disk, it can enable or disable autosave, and, it can have undo-redo support turned on or off.

To customize the modelContainer even more, like changing where it is saved on disk, you can build your own modelContainer instance, separately. Let me do this for the Trip’s app.

Instead of using the modelContainer modifier to construct a container, I will create one of my own, by using a property called container.

In the property’s closure, I will create a configuration for my model and pass the schema. This is where I will customize the URL of the data on disk, as well.

Then, I will pass this configuration to the ModelContainer initializer and return it.

In iOS 18, SwiftData lets you customize your modelContainer even further with fully custom data stores. The default data store provides a robust persistence backend supporting all of SwiftData’s features. But now, you can create your own data store, which uses its own implementation to persist data across the container.

For example, in the Trips app, I’ve implemented my own custom document format made of JSON files. To use it in the app, I just need to swap out the model configuration with one provided by the custom data store — in this example, JSONStoreConfiguration.

Custom data stores let you use familiar SwiftData APIs, like the @Model and @Query macros, no matter what format the data needs to be persisted with. It also provides a way for data stores to adopt features incrementally, so you can get started quickly. To learn more, watch the video “Create a custom data store with SwiftData”.

You can also create custom containers for use with Xcode previews. Previews are the perfect companion when developing your app with SwiftUI, and work great with SwiftData.

I want to create great previews for every view in the Trips app. I will start by using preview traits.

To do this, I will create a new struct called SampleData that conforms to PreviewModifier which has these two functions I need to fill out. One for setting up a shared context for the preview and another to apply the shared context to a view. For my Trips previews, I will vend a ModelContainer as the shared context for the sampleData.

Since a preview doesn’t need to store anything to disk, I will create a ModelConfiguration that stores data in memory only, and set up the ModelContainer.

I will then call a method I created earlier which creates an assortment of sample trips, and saves them into the model container. Since trips are now unique by name and dates, this code doesn’t need to de-duplicate any data — SwiftData does it for me! Finally, I will return the container. Next, I will need to implement a method which adds this modelContainer to whichever view this sampleData is used for. To do that, I will just apply the container using the modelContainer modifier.

Finally, I will add an extension to PreviewTrait so that I can easily access this sampleData. This creates a new static property, called sampleData(), which will apply this SampleData() structure as a modifier.

And now, when I declare a preview for any of my SwiftUI views, I can use.sampleData with the traits parameter. This will create an in-memory model container, load the sampleData, and modify my preview to use it in its SwiftUI views.

Having great sample data available makes it easy to work on any of my app’s views using SwiftData queries.

But some of the app’s views might not include queries, because they rely on models being passed to them. Now, you can use the @Previewable macro to make great previews for these, too.

For example, in Trips, the BucketListItemView takes a single trip as a parameter. With my sampleData, the bucketListItemView now has a model container with some sampleData, but it hasn’t queried for the data yet! Now, you can use the @Previewable macro to create a query right in the preview declaration. This provides an array of trips that can be passed to the BucketListItemView to create a preview with sampleData.

Finally, let’s talk about creating rich and optimized queries for SwiftData. Query drives your SwiftUI Views with an array of Models that can be sorted and filtered with ease, and it automatically reacts to changes made to the ModelContainer! #Predicate facilitates filtering, and can be evaluated during the data queries, rather than with large in memory data sets! Let’s look at a few ways I can filter for Trips! If I add a search bar to the Trips app, the searchText can be used to build a predicate for filtering my queries or even a fetch! Building a predicate is easy, I take the user provided searchText and see if a Trip’s name contains that text! But the text might apply to more than just a Trip’s name.

So I will build a compound predicate to also check the destination property on a Trip! That was all it took to build a compound predicate, but I can also make my predicates do so much more! New in iOS 18 is the ability to use Foundation’s new #Expression macro to build complex predicates easily! Expressions allow for reference values that do not produce true or false but instead allow for arbitrary types.

Expressions can be used to represent complex evaluations using a model’s properties and composed within predicates to tailor the results of queries even further! In the Trips app, I want create a query that fetches any ongoing trip where there is still some sights left to see! These are modeled by BucketListItems on the trip whose isInPlan property is still false. I will start by building a predicate.

In the predicate, I will specify that the trip should be ongoing, so the current date falls within the start and end.

But I also need to specify at least one of the BucketListItems on the trip has the isInPlan property set to false. Predicate alone doesn’t let me express this, because there’s no property that counts how many unplanned BucketListItems there are. To do this, I can construct an expression that builds this logic into the predicate.

This expression will count the number of bucket list items that I haven’t yet planned. It takes an array of bucket list items, and returns the number of items that meet the filter criteria.

Now, I can evaluate this expression as part of my predicate with the provided trip’s bucketList items. Then, my predicate can check whether the result of the expression is greater than zero. Expressions make the predicate macro an even more powerful and expressive tool to write queries, that efficiently fetch the data needed for your app. But there is one more way that I can make these queries performant, and that is with an all new schema macro, #Index! The new #Index macro adds the ability to create a single or compound index on your model. Like a table of contents in a book, an index represents additional metadata which SwiftData generates and saves in the container. This metadata makes queries for specified key paths faster and more efficient.

To get these benefits, you’ll declare which properties that SwiftData should create an index for. Consider those properties that most frequently occur in sorting and filtering of queries.

In the Trips app, trips are frequently queried with filters and sorts that utilize the name, start and end date properties. To make these queries even faster, I can add the #Index macro and specify key paths for the name, start and end dates, and a compound index of the three. For a large data set, like my extensive vacation ideas, this makes filtering and sorting substantially faster. Queries are easy to use in SwiftUI with the predicate macro, and become more powerful with expressions. Now with the #Index macro, you can make them even more performant in your app.

Use the power of SwiftData to build your app’s model layer. Consider adding #Unique constraints to your schema to make it easier to avoid duplicate models. And speed up your queries by adding the new #Index macro.

Use the new history API to track changes to your app’s models. And with custom data stores, you can now harness the power of SwiftData with your own document format or persistence backend.

Thank you! It has been an honor and we look forward to the amazing things you will make!
