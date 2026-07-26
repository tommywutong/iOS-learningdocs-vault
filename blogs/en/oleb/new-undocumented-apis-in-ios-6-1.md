---
title: New Undocumented APIs in iOS 6.1
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/02/new-undocumented-apis-ios-6-1/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:73b637e822a52834'
translated: false
---

> 原文：[New Undocumented APIs in iOS 6.1](https://oleb.net/blog/2013/02/new-undocumented-apis-ios-6-1/)　·　Ole Begemann

# New Undocumented APIs in iOS 6.1

# (Or: What The Hell Is MPGobblerGestureRecognizer?)

Now that Apple has released iOS 6.1, I wanted to see whether the new OS version contained any exciting new APIs beside the rather meager additions in the [public API diffs](https://developer.apple.com/library/ios/#releasenotes/General/iOS61APIDiffs/index.html).

With the help of [Nicolas Seriot’s](http://seriot.ch/) excellent [iOS Runtime Headers](https://github.com/nst/iOS-Runtime-Headers) repository, I compiled a list of all API changes between iOS 6.1 and 6.0. In the following, I discuss the most interesting additions. It is not an exhaustive list of everything that changed.

# MediaPlayer.framework

## MPGobblerGestureRecognizer

The [MediaPlayer framework](https://github.com/nst/iOS-Runtime-Headers/tree/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/MediaPlayer.framework)^[1](#fn:1) contains a number of new undocumented classes in iOS 6.1.

The most interesting one to me is [`MPGobblerGestureRecognizer`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/MediaPlayer.framework/MPGobblerGestureRecognizer.h), a UIGestureRecognizer subclass. To be honest, I don’t have the slightest idea what a “gobbler gesture” could be. If you know of a new gesture in iOS that is related to the media player or if you have any idea what kind of gesture this class is meant to detect, I’d love to hear from you.

**Update February 5 and 7:** Turns out that people have been speculating about the purpose of [`UIGobblerGestureRecognizer`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/UIKit.framework/UIGobblerGestureRecognizer.h), an undocumented class which was [introduced in iOS 5.0](https://twitter.com/bjhomer/statuses/298865856492998656) but I was unaware of, for quite some time.

[BJ Homer believes](https://twitter.com/bjhomer/statuses/298866732980912128) `UIGobblerGestureRecognizer` is used to avoid recognition while animations are in progress. Otherwise, it’s inactive. In an [interesting Twitter conversation](https://twitter.com/ortwingentz/status/225508227234791424), Filippo Bigarella and Conrad Kramer discovered that `UIGobblerGestureRecognizer` can “gobble” touches in order to prevent other gesture recognizers from receiving them in certain situations. What situations those are, I don’t know.

## _MPGlowLabel and MPScrollingTitlesView

The new [`_MPGlowLabel`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/MediaPlayer.framework/_MPGlowLabel.h) is a UILabel subclass with two additional properties, `glowColor` and `glowRadius`. Apple probably uses such a label in one or more places in its media player UI.

[`MPScrollingTitlesView`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/MediaPlayer.framework/MPScrollingTitlesView.h) seems to model a view that is used to display album and song titles in a scrolling marquee.

## Other Media Player Changes

Other new classes in this framework include [`MPCloudDownloadButton`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/MediaPlayer.framework/MPCloudDownloadButton.h), [`MP­Floating­Air­Play­Debug­View­Controller`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/MediaPlayer.framework/MPFloatingAirPlayDebugViewController.h) and [`MPLoggingUtility`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/MediaPlayer.framework/MPLoggingUtility.h).

# iAd.framework

I was especially curious if Apple had added new functionality for [remote view controllers](https://oleb.net/blog/2012/10/remote-view-controllers-in-ios-6/) in iOS 6.1. While the underlying APIs seem to be unchanged, I found at least a small change in wording in the iAd framework. A property of the [`ADLocalViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/iAd.framework/ADLocalViewController.h) class, used to display full-screen iAd ads, was renamed from `modalViewController` to `modalRemoteViewController`.

# UIKit.framework

The [`_UIWebViewController`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/UIKit.framework/_UIWebViewController.h) class is a big candidate to be made a public API in iOS 7 in my opinion. If I understand it correctly, it lets an app present a web view through remote view controllers. In addition to improved security, this new model for displaying web views could also mean that third-party apps could profit from WebKit’s just-in-time Javascript compilation, which is currently disabled for `UIWebView`.

The class got two new methods in iOS 6.1, `-_webContentSizeWithReplyHandler:` and `-loadHTMLString:baseURL:`.

# CoreData.framework

A large number of Core Data classes saw changes in iOS 6.1, albeit most of them quite small (such as the addition of a single method). As far as I can tell from names of the new methods, most changes are related to iCloud syncing. Whether this means that Core Data syncing over iCloud will work more reliably with iOS 6.1 is anybody’s guess.

Changes include:

- [`NSPersistentStore`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/CoreData.framework/NSPersistentStore.h) added the method `-_storeInfoForEntityDescription:`.
- [`NSSQLConnection`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/CoreData.framework/NSSQLConnection.h) and [`NSSQLiteConnection`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/CoreData.framework/NSSQLiteConnection.h) added the method `-dropUbiquityTables`.
- [`PFUbiquitySetupAssistant`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/CoreData.framework/PFUbiquitySetupAssistant.h) added the method `-removeUbiquityMetadataFromStore:`.
- Several classes got a new property of the type [`PFUbiquityKnowledgeVector *`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/CoreData.framework/PFUbiquityKnowledgeVector.h). I have no idea what this class does.
- [`_PFUbiquityRecordsImporter`](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/CoreData.framework/_PFUbiquityRecordsImporter.h) added the methods `-cancelAllOperationsForStoreName:` and `-check­Stores­And­Container`.

# PassKit.framework

Lots of changes in PassKit, but the vast majority of them are rather less exciting class renamings from the old `WL` prefix to the new `PK`. Does anybody know what `WL` stands for? **Update:** Eric Firestone [bets WL stands for “Wallet”](https://twitter.com/firetweet/status/298867427205328898).

# CoreTelephony.framework

The [CTTelephonyNetworkInfo](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/CoreTelephony.framework/CTTelephonyNetworkInfo.h) class has a new property `radioAccessTechnology` and the framework contains a corresponding new class named [CTRadioAccessTechnology](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/CoreTelephony.framework/CTRadioAccessTechnology.h).

It’s hard to tell from the headers what data this new class encapsulates.

# CoreMotion.framework

The [CMMotionManager](https://github.com/nst/iOS-Runtime-Headers/blob/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/Frameworks/CoreMotion.framework/CMMotionManager.h) class got two new methods, `-gyttNumTemperatures` and `-rebuildGytt`. I have no idea what they might do.

# AirPlayDiagnostics.framework

[AirPlayDiagnostics](https://github.com/nst/iOS-Runtime-Headers/tree/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/PrivateFrameworks/AirPlayDiagnostics.framework) is a new private framework in iOS. It contains these five classes:

- [AirPlayDiagnosticsFullscreenController](https://github.com/nst/iOS-Runtime-Headers/tree/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/PrivateFrameworks/AirPlayDiagnostics.framework/AirPlayDiagnosticsFullscreenController.h)
- [AirPlayDiagnosticsIssuesController](https://github.com/nst/iOS-Runtime-Headers/tree/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/PrivateFrameworks/AirPlayDiagnostics.framework/AirPlayDiagnosticsIssuesController.h)
- [AirPlayDiagnosticsPopoverController](https://github.com/nst/iOS-Runtime-Headers/tree/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/PrivateFrameworks/AirPlayDiagnostics.framework/AirPlayDiagnosticsPopoverController.h)
- [AirPlayDiagnosticsRoutePicker](https://github.com/nst/iOS-Runtime-Headers/tree/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/PrivateFrameworks/AirPlayDiagnostics.framework/AirPlayDiagnosticsRoutePicker.h)
- [AirPlayDiagnosticsStateMachine](https://github.com/nst/iOS-Runtime-Headers/tree/76cc1d4a6e6bc5546f04448535f9e64ec22a9716/PrivateFrameworks/AirPlayDiagnostics.framework/AirPlayDiagnosticsStateMachine.h)

1. Note that all links in this article to specific classes or frameworks inside the iOS Runtime Headers repository point to a specific commit (the iOS 6.1 version of these files). If you are reading this at a later date, the links might not reflect the current state of these APIs. [↩︎](#fnref:1)
