---
title: Reducing Download Size for iOS App Updates
apple_id: DTS40013268
resource_type: QA
platform: iOS
topic: Data Management
technology: null
published: '2014-09-10'
source_url: https://developer.apple.com/library/archive/qa/qa1779/_index.html
archived_at: '2026-07-27T06:57:05.098314Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1779

# Reducing Download Size for iOS App Updates

## Q:  How can I reduce the downloaded size of my app update for users that already have the previous version installed?

A: This document is specific to app updates. See [Technical Q&A QA1795: Reducing the size of my App](https://developer.apple.com/library/ios/qa/qa1795/_index.html) for a collection of techniques to reduce the size of an app when it is downloaded and installed for the first time.

Starting with iOS 6, the app store will automatically produce an update package for all new versions of apps submitted to the store. When generating the update package, the app store compares one or more prior versions of your app to the new version and creates an optimized package for each that contains only the content that has changed between versions of your app, excluding any content that did not change. This comparison looks at everything in the application bundle, including the application executable, nibs, localizations, image files, video files, audio files, text files, and files containing data in a custom format.

__Note:__ The ability to create update packages is not currently available to developers who do not distribute their apps through the app store, such as those distributing enterprise apps.

When used optimally, an update package is significantly smaller to download than the full package of the app and the update will install more quickly. Also, in many cases, this mechanism allows updates to large apps to be downloadable over cellular networks where app downloads are subject to a size limit.

In addition to new content, the update package contains instructions on how to transform the prior version of the app into the new version of the app. New files will be added, modified files will be replaced with their updated counterpart, and deleted files will be removed as part of this transformation. As far as the developer and user are concerned, this process is entirely transparent and the resulting updated app will be indistinguishable from a full download of the corresponding updated version of their app.

To optimize the size of your app updates, you should consider two tips:

- Do not make unnecessary modifications to files. Compare the contents of the prior and new versions of your app with `diff` or another directory comparison tool and verify that you've only changed what you expect within your app bundle.
- Content that you expect to change in an update should be stored in separate files from content that you don't expect to change. This reduces the size of the update package and increases its install speed.

For devices running iOS 6.x and iOS 7.0, the update package will include any file, in its entirety, that has changed in the new version of the app. For example, if you have a 10 MB file in your app and only change 1 KB of content within that file in the new version of the app, the update package for that new version will contain the full 10 MB file.

For devices running iOS 7.1 and later, the update package may include only the differences between the old and new versions of a changed file instead of the full file. This may significantly reduce the size of the update package in the case where only a small part of a large file changes, but will increase the update's installation time on the device. For this reason, the two tips above are still important even for updates on iOS 7.1 and later. Minimizing changed content and localizing it to many smaller files instead of one larger monolithic file will reduce the download size in all cases and will speed up installation on devices running iOS 7.1 and later.

__Warning:__ Your app should not rely on the creation and modification dates of files in your application bundle. When your app is updated using an update package, files are updated only if their content changes and will not be updated if only their metadata (e.g. creation and modification date) changes.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-09-10 | Fixed a bug: App Store offers the new packages on iOS 7.1 and after; iOS 7.0 behavior is identical to iOS 6.x behavior. Pointed to "QA1795: Reducing the size of my App". |
| 2013-08-17 | Made some cleaning and clarifications. Updated for iOS 7. |
| 2013-04-09 | New document that describes how to take advantage of the delta updates feature introduced in iOS 6. |
