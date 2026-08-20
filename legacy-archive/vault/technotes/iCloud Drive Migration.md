---
title: iCloud Drive Migration
apple_id: DTS40014955
resource_type: Technical Note
platform: iOS|macOS
topic: Data Management
technology: CloudKit
published: '2014-09-15'
source_url: https://developer.apple.com/library/archive/technotes/tn2348/_index.html
archived_at: '2026-07-26T19:54:14.848003Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2348

# iCloud Drive Migration

iOS 8 and OS X Yosemite introduced iCloud Drive, giving users access to all their documents in iCloud. When installing iOS 8 and OS X Yosemite, users will be presented an option to upgrade to iCloud Drive and will see the upgrade screen during set up time. iCloud Drive is a one-time and one-way upgrade from the current Ubiquity-based Documents and Data.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojvguwugsbrfvke4vcbi4yq)[iOS 8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojvguwugsbrfvke4vcbi4za)[OS X Yosemite](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojvguwugsbrfvke4vcbi4zq)[Entitlements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojvguwugsbrfvke4vcbi42a)[Ubiquity URLs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojvguwugsbrfvke4vcbi42q)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojvguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

If a user upgrades their iCloud account from Ubiquity (“Documents in the Cloud”) to iCloud Drive, their documents and data will be moved and their iCloud-enabled applications will work as before.

__Important:__ iOS 8 supports both Ubiquity and iCloud Drive. Users will be presented the choice to upgrade their iCloud account during the iOS 8 set up. If a user upgrades to iCloud Drive on iOS 8, devices running iOS 7 or earlier and OS X Mavericks or earlier will be no longer able to keep documents and data up to date. iCloud Drive requires iOS 8 and OS X Yosemite.

In all cases, existing apps will continue working without requiring modifications.

[Back to Top](#)

## iOS 8

- In iOS 8 Setup, the users will be presented with an option to “Upgrade to iCloud Drive”. Users will be warned that they will not be able to access documents currently stored in iCloud from the devices listed until they are upgraded to iOS 8 or OS X Yosemite.
- iOS 8 has both Ubiquity and iCloud Drive support.
- - If a user chooses not to upgrade her account to iCloud Drive, on iOS 8 Ubiquity and Ubiquity-based apps will continue to keep documents and data up to date across all her devices with iCloud.
  - If a user chooses to upgrade her account to iCloud Drive, on iOS 8 she will need to upgrade to iOS 8 across all her devices.

[Back to Top](#)

## OS X Yosemite

OS X Yosemite has only iCloud Drive support. If a developer is using Ubiquity to keep her data up to date between an iOS app and OS X app, their apps will stop synching if the user upgrades to iCloud Drive and has OS X Mavericks or earlier on their Mac.

If a user does not migrate his iCloud account to iCloud Drive, the app will still be able to write documents, but they will not be uploaded to iCloud. Already downloaded documents can be read, but documents that weren't downloaded will just cause file coordination calls to never return.

[Back to Top](#)

## Entitlements

You may keep both the Ubiquity and Cloud Drive entitlements in your app binary in order to support both Ubiquity and iCloud Drive accounts.

[Back to Top](#)

## Ubiquity URLs

Do not store `NSURLs` obtained from `NSFileManager` as a preference and assume it’s the same location next time.

After you move a document to iCloud, it is not necessary to save a URL to the document’s location persistently. If you manage a document using a `UIDocument` or `NSDocument` objects, that object automatically updates its local data structures with the document’s new URL. Because documents can move while in a user’s iCloud storage, you should use an `NSMetadataQuery` object to search for documents. Searching guarantees that your app has the correct URL for accessing the document. Use NSMetaDataQuery if you need to obtain an NSURL for any particular document or directory.

For more information on finding documents in iCloud, refer to the “File System Programming Guide”, section “Searching for Documents in Cloud” - [File System Programming Guide](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/iCloud/iCloud.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-09-15 | New document that describes the details of iCloud Drive migration. |

