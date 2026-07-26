---
title: DocSets App for iOS
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/01/docsets-app-for-ios/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:9833b84d67b86217'
translated: false
---

> 原文：[DocSets App for iOS](https://oleb.net/blog/2012/01/docsets-app-for-ios/)　·　Ole Begemann

# DocSets App for iOS

**Update May 10, 2012:** In the meantime, Ole has submitted DocSets to the App Store and perhaps surprisingly, Apple approved it. I encourage you to [buy the app on the App Store](http://itunes.apple.com/us/app/docsets/id509945577?mt=8) both to support Ole and make future updates easier.

Have you ever tried to use Apple’s developer documentation on your iOS device? While Apple does have a special iPad version of their online documentation at [developer.apple.com/library/ios/ipad/](http://developer.apple.com/library/ios/ipad/), I find it quite frustrating to use. And that’s not so much because Apple did a bad job with it but because of the inherent problems of a web-based solution: the whole thing is just too slow.

Now there is a better solution: my friend and officemate (and namesake) [Ole Moritz](http://omz-software.de/) wrote a native iOS app named [DocSets](https://github.com/omz/DocSets-for-iOS) for reading Apple’s developer documentation on the iPad or iPhone. DocSets is not available on the App Store. Instead, you can [download the source code from GitHub](https://github.com/omz/DocSets-for-iOS) for free and build it for yourself.

![Screenshots of DocSets on iPhone and iPad](https://oleb.net/media/docsets-ios-screenshot.png)

<sub>The DocSets app on iPhone and iPad. Screenshots: Ole Moritz.</sub>

The app does not come with the actual documentation, but it includes links to all of Apple’s current doc sets (iOS SDK 5.0, 4.3, 4.2 and Mac OS X 10.7, 10.6) and lets you download the ones you’re interested in with a single tap. When the download is complete, you have full offline access to the documentation. Other documents in Apple’s docset format can be added manually via iTunes File Sharing or by adding the link to the docset directly to the `AvailableDocSets.plist` file in the Xcode project.

![AvailableDocSets.plist](https://oleb.net/media/docsets-availabledocsets-plist-642px.png)

<sub>Edit this property list to add more downloadable doc sets to the app.</sub>

If you ever wanted to have offline access to Apple’s developer documentation on your iOS device, the DocSets app is a great tool.

PS: Ole also wrote [AppSales](https://github.com/omz/AppSales-Mobile), another open-source app that is worth checking out if you don’t have it. AppSales is an iOS app for downloading and analyzing your sales numbers from the iOS and Mac App Stores.
