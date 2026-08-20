---
title: iCloud Programming Guide for Core Data
apple_id: TP40013491
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/UsingCoreDataWithiCloudPG/BestPractices/BestPractices.html
archived_at: '2026-07-15T07:24:01.225070Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iCloud Programming Guide for Core Data](About%20Using%20iCloud%20with%20Core%20Data.md)


[Next](Troubleshooting.md)[Previous](Using%20Document%20Storage%20with%20iCloud.md)

# Best Practices

Follow the tips and guidelines discussed in this chapter to improve your app’s user experience, stability, and performance. In general, use an iCloud-enabled persistent store as you would a local persistent store, while keeping several key design differences in mind.

Traditionally, you profile and optimize for memory, storage, and CPU usage. With iCloud, there are other important factors—namely network availability, bandwidth, and multiple peers. Core Data’s iCloud integration handles these issues for you, but by following these best practices, you can directly impact the quality of your app and the degree to which Core Data can optimize for you.

Bandwidth, network availability, and storage are limited resources and have real, financial consequences for your users. When you design your schema, store in iCloud only information that can’t be re-created.

Core Data’s managed object model configuration feature simplifies working with data that’s split between two storage locations. With model configurations, you can set where specific entities—or even individual attributes—are stored. Use managed object model configuration to separate attributes and entities that need only be stored locally from those that should be persisted to iCloud. See Managed Object Models in _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ for further discussion about model configurations. Additionally, Core Data efficiently persists external data to iCloud. Use the external data setting on attributes that are likely to hold more than 4 KB of data.

For an example of how to reduce what you store in iCloud, consider a Newsstand app that downloads and caches high-resolution magazines in Core Data and has a feature that allows the user to add bookmarks. Rather than store the entire model in iCloud, the app stores only the bookmark entities, with attributes containing the unique identifier of the magazine that each bookmark corresponds to.

A good approach is that if your app seeds a large set of initial data, it should not be stored in iCloud, because those records can be re-created. If the records are to be modified, it may be beneficial to design a schema and associated configurations that allow you to store only the changes in iCloud.

iCloud-enabled Core Data apps are not only aware of data created on the device, they’re aware of data on other devices. It’s a good idea to keep this fact in mind when designing your Core Data stack.

For example, you traditionally use merge policies when you want to merge changes that were made in separate managed object contexts and persistent store coordinators. With iCloud, in contrast, you use merge policies to merge changes made to a record on multiple peers. For further discussion of merge policies, see Change Management in _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_.

Avoid using nested managed object contexts with iCloud-enabled persistent stores. Because changes saved in child contexts are not persisted to iCloud until the parent context is also saved, nested contexts create unnecessary complexity. If your app doesn’t persist changes to iCloud quickly, you may confuse your app’s users or, worse, fail to meet their expectations.

When you save a managed object context, Core Data creates, in the ubiquity container, a set of transaction changes that are guaranteed to be applied together on other peers. The size of this transaction set, and the frequency with which you save your context, both directly impact the performance of your app.

You decide when to save your managed object context by mapping actions in your user interface to the managed objects that are created, changed, and deleted in your model. Because a save corresponds to a complete set of changes that will be applied at the same time, you meet users’ expectations when you consider the events the user expects to be persisted to other peers. By tuning your save points to match complete sets of changes, you meet users’ expectations, avoid incomplete data from being persisted to other peers, and reduce the complexity of merging. You also increase performance by limiting the number of changes in a single merge and by limiting the frequency at which your context performs a merge.

For example, consider a recipe app that persists the user’s recipes to iCloud. Rather than save the context every time an attribute is set, the context is saved when the user finishes creating an entire recipe. Because factors like network availability, bandwidth, and storage were taken into account, each peer will either receive the entire recipe or nothing, rather than a partial record.

If your app creates, changes, or deletes managed objects in large batches, be sure to save and reset your managed object context frequently or divide the task up into smaller parts so that you divide the changes among multiple transaction containers.

How you migrate existing user data into the iCloud container depends on the size of your store file. If your store file is small, invoke [migratePersistentStore:toURL:options:withType:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468927-migratepersistentstore) on your persistent store coordinator, passing your existing persistent store and the URL returned from adding the iCloud-enabled store to your persistent store coordinator.

If your store file is large, create a separate persistent store coordinator and managed object context that you use to read from your existing store. Keep in mind that the amount of memory consumed during migration is about twice the size of the store. Use the [NSReadOnlyPersistentStoreOption](https://developer.apple.com/documentation/coredata/nsreadonlypersistentstoreoption) option when you add the existing persistent store to improve performance. Transfer data in batches to your iCloud-enabled managed object context along with efficiently constructed fetch requests, setting the amount of data-per-batch with the [setFetchBatchSize:](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506558-fetchbatchsize) method. Each time you reach the size of the batch, save and reset the managed object context.

See [Seeding Initial Data](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknltgma) for more about importing data and [Detecting and Removing Duplicate Records](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknltq) for more about deduplication.

In iOS 7 and OS X 10.9, Core Data and iCloud are tightly integrated to simplify the work you do to integrate your app with iCloud. Core Data now creates and manages a fallback store for you, long running processes have been made asynchronous, and notifications provide more insight into the state of your app’s data. Consider re-writing your persistent store setup and notification handler code to take advantage of these improvements—you’ll find that your implementation is simpler, smaller, and more straightforward.

Because of the large improvements made to iCloud’s Core Data integration, the persistent store your app created in previous versions of iOS and OS X is not compatible with iOS 7 and OS X 10.9. When you update your app, use a different [NSPersistentStoreUbiquitousContentNameKey](https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitouscontentnamekey) to create a new iCloud-enabled persistent store. Then migrate your user’s existing data from the old store to the new one. Take a look at Migrating User Data to iCloud, because the steps you take to migrate from an old iCloud-enabled persistent store are similar. The guidelines in [Performing Schema Migrations](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknlts) are useful as well—the behavior of your app with different schema versions is just like the behavior of your app with different iCloud-enabled store versions.

[Next](Troubleshooting.md)[Previous](Using%20Document%20Storage%20with%20iCloud.md)

