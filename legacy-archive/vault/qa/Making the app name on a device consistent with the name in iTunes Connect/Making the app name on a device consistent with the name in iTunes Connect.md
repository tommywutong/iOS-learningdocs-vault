---
title: Making the app name on a device consistent with the name in iTunes Connect.
apple_id: DTS40015307
resource_type: QA
platform: iOS
topic: Xcode
technology: WatchKit
published: '2017-07-24'
source_url: https://developer.apple.com/library/archive/qa/qa1892/_index.html
archived_at: '2026-07-18T02:35:23.444568Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1892

# Making the app name on a device consistent with the name in iTunes Connect.

## Q:  My app name on a device is inconsistent with the name in iTunes Connect. How to fix that?

A: The app names in iTunes Connect and as displayed on a device should be similar so as not to cause confusion. For a WatchKit app, this means the app name in iTunes Connect should be similar to the names on the home screen of an iPhone, the iOS Watch app, and an Apple Watch. You can make these names consistent by specifying appropriate values in the Info.plist of your iOS app and WatchKit app.

The app name on the iPhone home screen comes from the `CFBundleDisplayName` (or "Bundle display name", the human-readable string in Xcode) entry of your iOS app’s Info.plist (see Figure 1). If the bundle display name is not provided, the system will fall back to the app's bundle name, which is specified in the `CFBundleName` entry of the Info.plist.

__Figure 1__  iOS app's bundle display name used on iPhone home screen

!!

Similarly, the app name on the iOS Watch app and the WatchKit app's notifications comes from the `CFBundleDisplayName` entry of your WatchKit app's Info.plist (see Figure 2).

__Figure 2__  WatchKit app's bundle display name used on the iOS Watch app and WatchKit app's notifications

!!

Before submitting your WatchKit app for review, be sure to set the `CFBundleDisplayName` of your iOS app and WatchKit app to a value matching the app name used in iTunes Connect.

Detailed steps for specifying the bundle display name for an iOS app are covered in [QA1823 (Updating the Display Name of Your App)](https://developer.apple.com/library/ios/qa/qa1823/_index.html#//apple_ref/doc/uid/DTS40014218). For a WatchKit app, the bundle display name is by default set to the product name of its container app. If the name doesn’t match, you can change it by following these steps:

1. Select the Info.plist of your WatchKit app in Xcode’s project navigator to reveal the property list editor, as shown in Figure 2.
2. Select the “Bundle display name” entry in the editor and enter the appropriate name. If the entry isn't there, add it by clicking on any entry in the list, then clicking the "+" button and choosing “Bundle display name” from the ensuing pop-up menu.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-07-24 | Modernized content for the new behavior since iOS 9. |
|  | Modernized content for the new behavior since iOS 9. |
| 2015-04-28 | Minor editorial update. |
| 2015-04-22 | Minor editorial update. |
|  | Minor editorial update. |
| 2015-04-15 | New document that explains how to make the app name on a device consistent with the name in iTunes Connect. |

