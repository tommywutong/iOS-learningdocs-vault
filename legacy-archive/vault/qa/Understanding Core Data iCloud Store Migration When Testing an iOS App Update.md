---
title: Understanding Core Data iCloud Store Migration When Testing an iOS App Update
apple_id: DTS40015176
resource_type: QA
platform: iOS
topic: Data Management
technology: CoreData
published: '2015-03-05'
source_url: https://developer.apple.com/library/archive/qa/qa1883/_index.html
archived_at: '2026-07-18T02:35:16.201832Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1883

# Understanding Core Data iCloud Store Migration When Testing an iOS App Update

## Q:  I have an App Store app using Core Data iCloud and I'm testing an update with a new model. When I build and run my update over the App Store version with Xcode, the existing data disappears. Why is that?

A: When you run an Xcode build with a new model over an App Store version, it is expected that the existing data of the Core Data iCloud store won't appear. The same behavior occurs in an Ad Hoc update as well, but not in an update installed from App Store. There are two points to understand this:

First, changes to your Core Data iCloud store are recorded and organized by device. For each device your app is running on (and signed in with the same iCloud account), Core Data creates a peer folder with a unique name in your app's iCloud container to preserve the changes originating from it.

However, the peer folder name of an App Store version is normally different from that of a non-App Store version (such as a test build installed with Xcode, an Ad Hoc version, or a TestFlight version): for an App Store version, the folder name is determined by data supplied by the App Store, while for a non-App Store version, it is calculated based on the app’s bundle ID. As a result, when you install an Xcode build or an Ad Hoc update over your App Store version, launch it, and add data to the iCloud store, a different peer folder will be created in your iCloud container. For Core Data, this is like another new device getting involved.

Second, when doing lightweight migration on an iCloud store, Core Data only migrates the changes originating from the current device (and then merges them with any other devices configured with that new model version), as discussed in the [Migration and iCloud](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/CoreDataVersioning/vmCloud/vmCloud.html#//apple_ref/doc/uid/TP40004399-CH9-SW1) section of Core Data Model Versioning and Data Migration Programming Guide.

In your case, Core Data will create a new peer folder for your testing update, which is the same as running your update on a new device. Thus, when doing lightweight migration on your iCloud store, Core Data can’t find any change originating from this “new” device, so no existing data would be migrated to the newer version store.

In the production environment, as users download your update from App Store, its peer folder won’t be different from the previous version, so the existing data originating from the current device will be found and migrated.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-03-05 | New document that explains why the Core Data iCloud Store isn't migrated from your App Store version to your test build with a new model. |

