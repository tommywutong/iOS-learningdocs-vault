---
title: Working with Default Data in Core Data Apps
apple_id: DTS40017577
resource_type: Technical Note
platform: iOS
topic: Data Management
technology: CoreData
published: '2016-11-16'
source_url: https://developer.apple.com/library/archive/technotes/tn2350/_index.html
archived_at: '2026-07-26T19:54:15.196287Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2350

# Working with Default Data in Core Data Apps

This technical note discusses how to work with default data in Core Data apps in a way that complies with iOS Data Storage Guidelines.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjxg4wugsbrfveekqkejfheomi)[Working with a Large Default Data Set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjxg4wugsbrfveekqkejfheomq)[Working with a Small Default Data Set](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjxg4wugsbrfveekqkejfheomy)[Creating a Default Data Store](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjxg4wugsbrfveekqkejfheona)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonjxg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Some apps may benefit from shipping with default data. For example, it is almost indispensable for a cooking app to ship with some attractive recipes so that users can begin to cook immediately after downloading it, or for a traveling app to preload some airport information so that users can arrange their trips.

When you ship default data with your apps, it is important to know that apps have to comply with [iOS Data Storage Guidelines](https://developer.apple.com/icloud/documentation/data-storage/index.html), which requires that only user-generated data or the data that can't be re-created should be put into a folder that will be automatically backed up to iCloud or iTunes. (See [Make App Backups More Efficient](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/PerformanceTips/PerformanceTips.html#//apple_ref/doc/uid/TP40007072-CH7-SW16) section of App Programming Guide for iOS for the folders that will be included or excluded from backup.)

Default data is deemed re-creatable but not user-generated data, thus should not be backed up. However, for a Core Data app whose store file normally contains user data and so has to be backed up, separating default data from user-generated data may not be trivial. Depending on the data size, the way to work with default data can be very different.

[Back to Top](#)

## Working with a Large Default Data Set

Default data can be put into a Core Data store (covered in Creating a Default Data Store section) and shipped with your app. Yet working with the default data store may not be as straightforward, because the store will finally reside in your app bundle, thus is separated from your editable user data store and can only be accessed in readonly mode. Copying the store to a writable location may not be a choice because:

- If the location is under a backup folder, the default data can soon be backed up to iCloud or iTunes, thus breaks iOS Data Storage Guidelines. This is especially true for a large default data set.
- If the location is under an non-backup folder, the changes on the store will be lost if the folder is purged.

You can choose to manage your default and user data store independently, or choose to load the stores into one Core Data stack which gives you the following capabilities:

- Creating fetched properties between two stores (covered in [Weak Relationships (Fetched Properties)](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/CoreData/HowManagedObjectsarerelated.html#//apple_ref/doc/uid/TP40001075-CH17-SW13) section of Core Data Programming Guide), which provides you a convenient way for cross-store data access. When you need a relationship crossing your default and user data store, a fetched property is probably the best-suited choice (since Core Data does not let you create cross-store relationships). Be aware though that due to a limit of the current predicate system, cross-store fetched properties can't be used in a predicate for `NSFetchRequest`.
- Fetching data from both stores into one managed object context (`NSManagedObjectContext`). When you save the context, the changes you made automatically go to the user data store because the default data store is readonly.

To add multiple stores into one Core Data stack, you simply call the `NSPersistentStoreCoordinator`'s `addPersistentStore(ofType:configurationName:at:options:)` method multiple times with different store URLs, configurations, and options.

__Note:__ The stores managed by the same coordinator have to share the same Core Data model (`NSManagedObjectModel`), so you might want to use configurations to organize the entities for different stores. To do that, group the default and user data entities with different configurations in your model, then pass the configuration names to the above method when adding the stores.

Since the default data store has to be readonly, it is worth thinking twice about your model design and try to make the store only contain data that is logically readonly for users. As an example, if your app ships with some content which users can annotate, the contents and annotations should be modeled into different entities and configurations which are used on your default data store and user data store respectively. With that, the default data store only contains the contents that users perceive to be readonly, you therefore don't have to add extra logic to let users "change" the default data.

If your default data has to be open for changes by users – like the cooking app, the default recipes may mingle with the user-created recipes, thus are perceived to be changeable by users – you might consider converting the piece of default data to user data by creating an editable copy and put it into your user data store when users save their changes. If your app allows users to "delete" the default data ("delete" here means "hide" for you because default data is readonly), you might have to use your own data structure to prevent the user-deleted data from showing up in your app.

Considering that users may change any field of the editable copy, it is a good practice to add an user-invisible UUID (Universally Unique Identifiers) attribute when modeling your default data so that you can uniquely identify every record. The UUID will be very useful when you need to associate an editable copy with its original record in the default data store, or de-duplicate your default data coming from different devices when working with Core Data iCloud.

__Note:__ Batch importing default data into the user data store may dramatically enlarge the user data store which will finally be backed up, thus breaking iOS Data Storage Guidelines.

[Back to Top](#)

## Working with a Small Default Data Set

iOS Data Storage Guidelines is meant to ensure that backups are as efficient as possible. Ideally, no default data should be backed up. However, since a data set that is small enough doesn’t have a material impact on the efficiency, an app is currently allowed to have a small amount of default data in a backup folder.

In that case, the app doesn't have to manage two separated stores any more. Instead, it copies the default data store to the working folder on the first launch session, and use it as the user data store directly. Since the store doesn't contain any user data before the first edit, you can exclude it from backup when doing the copy – by putting the store into a folder and setting the `isExcludedFromBackupKey` (`URLResourceValues`) of the folder to __true__. Later on when the store is saved for the first time, you then set the key back to __false__ so that the folder can be backed up.

Be aware that how small the data set should be is subject to change and has to be determined in the App Review process. You might only consider this path if your default data set is really small and moving it out from your user data store means a lot of hard work.

[Back to Top](#)

## Creating a Default Data Store

A default data store should be created with Core Data APIs and exactly the same Core Data model file used in your app. You can write a tool to do that but your app can be the tool if it already has the capability to maintain its data store. You can use your app to create an empty store, then add the default data manually (if it has the UI) or write extra code for batch preloading. For an UUID attribute that is used to uniquely identify a default data record (as discussed in Working with a large default data set section), call `NSUUID().UUIDString` to retrieve an UUID and use it as the attribute value.

After populating all the data, you can grab the store file from your app's sandbox on your device or iOS Simulator, then add it into your project and use it as a default data store.

If you are using the iOS Simulator, go to ~/Library/Developer/CoreSimulator/Devices folder on your Mac to find the store file. Otherwise, you can download your app's sandbox container from your device using these steps:

1. Connect your device to Xcode.
2. Go to Xcode  `Window > Devices` menu and click it to show the Devices window.
3. Select your device from the devices list on the right, then select your app in the `Installed` `Apps` section.
4. Click the gear icon and run the `Download` `Container` menu. Your app's sandbox container should be downloaded to your Mac's Desktop.
5. Change the file extension to ".zip", then double click to uncompress it. You should see the container folder and can grab your store file from there.

If you are working with a SQLite store and prefer your default data store to be one single file, remember to specify the rollback journaling mode in the store options (see [QA1809](https://developer.apple.com/library/ios/qa/qa1809/_index.html#//apple_ref/doc/uid/DTS40014115) for details) when creating the store.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-11-16 | New document that discusses how to work with default data in Core Data apps in a way that complies with iOS Data Storage Guidelines. |

