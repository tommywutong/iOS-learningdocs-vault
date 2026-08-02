---
title: iCloud Programming Guide for Core Data
apple_id: TP40013491
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/UsingCoreDataWithiCloudPG/Troubleshooting/Troubleshooting.html
archived_at: '2026-07-15T07:24:01.249516Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iCloud Programming Guide for Core Data](About%20Using%20iCloud%20with%20Core%20Data.md)


[Next](Using%20the%20iCloud%20Debugging%20Tools.md)[Previous](Best%20Practices.md)

# Troubleshooting

With iCloud, users can create content on one device and finish creating it on another. Use these troubleshooting steps when your app isn’t maintaining this seamless user experience. To learn about the iCloud debugging tools available in Xcode that you’ll use along with these steps, read [Using the iCloud Debugging Tools](Using%20the%20iCloud%20Debugging%20Tools.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqobnknltc). For additional important debugging tips relevant to every iCloud-enabled app, see [Testing and Debugging Your iCloud App](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/TestingandDebuggingforiCloud.html#//apple_ref/doc/uid/TP40012094-CH8) in _[iCloud Design Guide](../../General/iCloud%20Design%20Guide/About%20Incorporating%20iCloud%20into%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaoju)_

To make it easier to find issues when you use Core Data with iCloud, simplify the architecture of your Core Data stack—overcomplicating your implementation can make finding bugs difficult. Do this by following the guidelines in [Using the SQLite Store with iCloud](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknltc).

If your managed objects are behaving inconsistently, ensure that you are resetting your managed object context(s) in your `NSPersistentStoreCoordinatorStoresWillChangeNotification` notification handler and dropping any managed object references your app is holding. After receiving the `NSPersistentStoreCoordinatorStoresDidChangeNotification` notification, you should refetch your content.

If you are not receiving a notification you expect to receive, make sure that you have subscribed to these notifications early enough. Many of Core Data’s iCloud-state-change notifications are posted during app launch or soon after—for example, before adding the iCloud-enabled persistent store to your persistent store coordinator.

When your app loses data or creates multiple records, the root cause is usually related to how you migrated or merged your data. You should test your app concurrently on multiple devices to determine what happens when records are created or deleted. Review [Core Data Posts Content Changes from iCloud](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknltm) and [Detecting and Removing Duplicate Records](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknltq) for implementation strategies.

If the app has duplicate records or can’t find a record to delete when you merge changes, you may have registered for Core Data’s iCloud notifications in multiple places. Deregister view controllers that go offscreen on iOS and inactive windows on OS X.

If the app has duplicate records when you migrate multiple peers, your deduplication algorithm is not functioning or it does not correctly determine uniqueness. When your app runs migration on multiple devices, they all need to pick the same record to keep and the same record(s) to delete.

If the app’s records are deleted when you migrate multiple peers, your deduplication algorithm does not deterministically choose a winning record. When your app runs migration on multiple devices, they all need to pick the same record to keep and the same record(s) to delete. Otherwise, each device will choose different records and those decisions will all be persisted to iCloud.

When you integrate your Core Data app with iCloud, follow the Core Data framework’s guidelines and best practices to tune your app’s performance in the context of iCloud. As part of this effort, consider the content that’s created on other devices while your app is running.

If your user interface fails to update when you import changes to content, check that you are correctly dispatching back onto the main queue using the `dispatch_async(3)` function or an [NSOperationQueue](https://developer.apple.com/documentation/foundation/operationqueue) queue. You can also configure your notification subscriptions to invoke your handler on the main queue. Recall that managed objects are not thread-safe, so you might merge changes on a background managed object context and then refetch on your main thread. If your change set is small, merge changes into a managed object context on the main thread.

If your user interface freezes when you import changes to content, open the iCloud Report to find out when your app receives changes from iCloud. Then look at the CPU Report and the Memory Report right after that event—you should see a short spike in CPU and memory usage while Core Data imports the changes. A long block of high CPU and memory usage is a sign that either the set of changes is too large or your app is receiving many change sets in quick succession. To increase performance and decrease CPU and memory usage, you can optimize when you save your managed object context. For optimization strategies, read [Core Data Posts Content Changes from iCloud](Using%20the%20SQLite%20Store%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqmznknltm) and [Best Practices](Best%20Practices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqnrnknltc).

[Next](Using%20the%20iCloud%20Debugging%20Tools.md)[Previous](Best%20Practices.md)

