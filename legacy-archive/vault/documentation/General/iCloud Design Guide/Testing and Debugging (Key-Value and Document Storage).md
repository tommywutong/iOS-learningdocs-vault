---
title: iCloud Design Guide
apple_id: TP40012094
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: null
published: '2015-12-17'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/TestingandDebuggingforiCloud.html
archived_at: '2026-07-15T07:34:40.433299Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iCloud Design Guide](About%20Incorporating%20iCloud%20into%20Your%20App.md)


[Next](Document%20Revision%20History.md)[Previous](Designing%20for%20CloudKit.md)

# Testing and Debugging (Key-Value and Document Storage)

Although no app is finished until it has been thoroughly tested and debugged, these steps are perhaps more important when you adopt iCloud: the number of user scenarios that your app must gracefully handle is greater. A user can have different versions of your app on different devices or run your app on more than one device simultaneously. A user can turn on airplane mode while a large file is uploading to iCloud. In rare cases, a user might log out of iCloud or switch to a different iCloud account.

This chapter helps orient you toward thinking about iCloud when testing and debugging your app.

If things aren’t working as expected, first make sure that the preliminaries are correctly in place.

- __Ensure that your test devices are correctly provisioned for iCloud.__

  Your device provisioning profile and [App ID](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AppID.html#//apple_ref/doc/uid/TP40008195-CH64) must be correctly configured for iCloud. Review _App Distribution Quick Start_ and Adding iCloud Support in _App Distribution Guide_.
- __Ensure that your iCloud entitlement requests are correct.__

  Without the appropriate entitlement requests in place in your Xcode project, your app has no access to its iCloud containers or to key-value storage. Carefully review the information in [Request Access to iCloud Using Xcode Capabilities](iCloud%20Fundamentals%20%28Key-Value%20and%20Document%20Storage%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqnrnknltcmy).

  Ensure that when you access your app’s iCloud containers, you are using fully qualified entitlement values.

When testing, don’t expect changes to instantly propagate from one device to another.

You can programmatically determine if a file has made it to the iCloud servers by checking the value of its URL’s [NSURLUbiquitousItemIsUploadedKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416038-ubiquitousitemisuploadedkey) key. Do this by calling the `NSURL` method [getResourceValue:forKey:error:](https://developer.apple.com/documentation/foundation/nsurl/1408874-getresourcevalue). The key’s Boolean [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) value contains `true` if the file has been successfully uploaded.

Likewise, you can programmatically determine if an iCloud file is present locally. Check the value of the [NSURLUbiquitousItemIsDownloadedKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1572053-ubiquitousitemisdownloadedkey) key of the corresponding URL by calling the `NSURL` method [getResourceValue:forKey:error:](https://developer.apple.com/documentation/foundation/nsurl/1408874-getresourcevalue).

In both cases, obtain the file URLs from your app’s [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery) object, as described in [App Responsibilities for Using iCloud Documents](Designing%20for%20Documents%20in%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqmrnknlte).

Keep an eye on network activity while testing your app, checking for undue amounts of network traffic. For iOS, use the Network Activity instrument found in the Instruments analysis tool. On a Mac, you can use the OS X Network Utility app.

If your app’s network traffic seems excessive, look for optimizations in your app design. For example, you may be able to design your document file package in a way to better support incremental uploads and downloads, as described in [Design for Network Transfer Efficiency](Designing%20for%20Documents%20in%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqmrnknlts).

For information on profiling an app with Instruments, see _[Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)_.

Real-world use of your iCloud-enabled app can result in a wide range of conflict scenarios between versions of a document. Beyond that unavoidable truth, issues in an app’s logic can cause needless conflicts, as described in [Design for Persistent Document State](Designing%20for%20Documents%20in%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqmrnknlto).

Here are some ideas for simulating real-world conflicts. To prepare for these tests, set up two devices to be connected to a single iCloud account. Implement your app to handle these scenarios and others that come to mind for your particular app.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To test document version conflicts with one device offline

1. On device 1, create and open a new document using your app, and then open the document on device 2.

   The document is now open on both devices.
2. On device 1, turn on airplane mode and then edit the document.
3. On device 2 (which is still online), edit the document as well.
4. On device 1, turn off airplane mode.
5. On each device, check whether the conflict resolution behavior is as you intend it to be.
![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To test document version conflicts with two devices offline

1. On device 1, create and open a new document using your app, then open the document on device 2.

   The document is now open on both devices.
2. Turn on airplane mode on both devices, then edit the document on both devices.

   Try varying this procedure by finishing your changes on the two devices at the same time or at different times.
3. On both devices, turn off airplane mode.

   For this step as well, try varying this procedure by turning off airplane mode at the same time or at different times for the two devices.
4. On each device, check whether the conflict resolution behavior is as you intend it to be.
![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To test forward and backward compatibility of your document format

1. Install the oldest supported version of your app on device 1; install the newest version on device 2.
2. Create a document on each device. Allow enough time to elapse so that each doc appears on the other device.
3. Open each document on the device that was not used to create it. Or, in the case of a version mismatch in which you do not support opening, ensure that the behavior is as you intend it to be. Check for issues.
![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To test document management

1. Save a document to iCloud, then open that document on two devices.
2. Using device 1, rename (or, alternatively, delete) the document.
3. Check on device 2 whether the behavior is as you intend it to be.

While you are developing an app, it is possible for data in the app’s iCloud container to become inconsistent. If this happens, your app’s behavior can become inconsistent as well. If previously working code is now not working, try emptying the iCloud container for your app to start fresh.

You can empty your app’s iCloud container using an iOS device or a Mac.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To empty the iCloud container for your app, using an iOS device

1. On each device containing an instance of your app, delete that instance.
2. In iOS, navigate to Settings > iCloud > Storage & Backup > Manage Storage.
3. If your app is not shown in the Documents & Data group, tap Show All.
4. On the Manage Storage screen, tap your app’s name.
5. On your app’s storage Info screen, tap Edit, then tap Delete All.

   In the confirmation alert that appears, tap Delete All.

After completing these steps, wait to ensure that deletion of your iCloud container’s contents has propagated to all devices attached to your iCloud account. If the container had a large amount of data, this takes longer. On a Mac, you can use the Finder to see if the iCloud container has been emptied. The path to the container on a Mac is:

`~/Library/Mobile Documents/<bundle-identifier-for-app>`

Then reinstall your app on each device.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To empty the iCloud container for your app, using a Mac

1. On each device containing an instance of your app, delete that instance.
2. In OS X, open iCloud preferences in System Preferences and click Manage.
3. In the Manage Storage dialog that appears, locate your app in the list and click it.
4. Click Delete All.

   In the confirmation alert that appears, click Delete. Then click Done.

After completing these steps, wait to ensure that deletion of your iCloud container’s contents has propagated to all devices attached to your iCloud account. If the container had a large amount of data, this takes longer. On a Mac, you can use the Finder to see if the iCloud container has been emptied. The path to the container on a Mac is:

`~/Library/Mobile Documents/<bundle-identifier-for-app>`

Then reinstall your app on each device.

If you provide an OS X version of your iCloud-enabled app, and you want to start completely fresh, also delete the contents of the app’s App Sandbox container on each Mac on which your app was installed. This ensures that any other app-specific data that might have become inconsistent is also removed. The path for an App Sandbox container on a Mac is:

```
~/Library/Containers/<bundle-name-for-app>
```

[Next](Document%20Revision%20History.md)[Previous](Designing%20for%20CloudKit.md)

