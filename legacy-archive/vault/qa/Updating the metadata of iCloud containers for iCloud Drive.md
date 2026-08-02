---
title: Updating the metadata of iCloud containers for iCloud Drive
apple_id: DTS40016580
resource_type: QA
platform: iOS
topic: Data Management
technology: Foundation
published: '2016-04-04'
source_url: https://developer.apple.com/library/archive/qa/qa1893/_index.html
archived_at: '2026-07-18T02:35:33.227841Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1893

# Updating the metadata of iCloud containers for iCloud Drive

## Q:  I am trying to expose my iCloud container on iCloud Drive by adding an `NSUbiquitousContainers` entry in my Info.plist. It seems that iCloud Drive doesn’t accept any changes once the metadata specified in that entry has ever been gathered. Why is that?

A: The first time your app is installed and launched on an iOS (8.0 or later) device, the metadata specified in the `NSUbiquitousContainers` entry (if existing) in your Info.plist will be extracted, associated with your iCloud containers, and used by iCloud Drive. After that, the metadata won’t be updated until a newer build of your app is detected.

For the metadata changes to be accepted by iCloud Drive, you need to bump the `Bundle` `version` of your app. Here are the steps:

1. Open your project with Xcode (6.0 or later) and make sure the `iCloud Documents` option under `Capabilities` pane of your target is checked and the iCloud container is specified. (For details about how to configure your app for iCloud, see [iCloud Fundamentals](https://developer.apple.com/library/ios/documentation/General/Conceptual/iCloudDesignGuide/Chapters/iCloudFundametals.html#//apple_ref/doc/uid/TP40012094-CH6-SW24) section of iCloud Design Guide).
2. Log in your devices with your iCloud account and enable iCloud Drive for you app. Be sure to use the same account on your Mac (with OS X Yosemite or later) if you are using Finder to view the content of iCloud Drive.
3. Bump the `Bundle` `version` (`CFBundleVersion`) in the Info.plist of your app (or the `Build` field in the `General` pane of your target in Xcode Project Editor). Be sure that the new value is higher than the previous one by string comparison with `NSNumericSearch` option, and only contains numeric (0-9) and period (.) characters. (See [CFBundleVersion](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/20001431-102364) section of Information Property List Key Reference for more information.)
4. Make changes on the `NSUbiquitousContainers` entry. (See [Enabling Document Storage in iCloud Drive](https://developer.apple.com/library/mac/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesigningForDocumentsIniCloud.html#//apple_ref/doc/uid/TP40012094-CH2-SW20) section of iCloud Design Guide for a sample `NSUbiquitousContainers` entry.)
5. Build and run your app on your device.

After the new metadata is picked up and synchronized through iCloud, you can view the changes with Finder in OS X or the iCloud Drive app in iOS 9. (Use the `UIDocumentPickerViewController` class to view the iCloud Drive content before iOS 9.)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-04-04 | Fixed a broken link. Mentioned the iCloud Drive app in iOS 9. |
| 2015-09-14 | New document that explains how to update the metadata of iCloud containers for iCloud Drive. |

