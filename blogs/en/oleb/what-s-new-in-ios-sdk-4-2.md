---
title: 'What''s New in iOS SDK 4.2'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/11/whats-new-in-ios-sdk-4-2/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c6b69bad76cffacb'
translated: false
---

> 原文：[What's New in iOS SDK 4.2](https://oleb.net/blog/2010/11/whats-new-in-ios-sdk-4-2/)　·　Ole Begemann

# What's New in iOS SDK 4.2

Now that the [final version of iOS SDK 4.2](http://developer.apple.com/devcenter/ios/) is available, let’s have a look at what is new. What follows is a detailed overview of the [What’s New in iOS 4.2](https://developer.apple.com/library/ios/#releasenotes/General/WhatsNewIniPhoneOS/Articles/iOS4.html#//apple_ref/doc/uid/TP40010313-SW1) and [iOS 4.2 API Diffs](https://developer.apple.com/library/ios/#releasenotes/General/iOS42APIDiffs/index.html#//apple_ref/doc/uid/TP40010312) documents.

# The iPad makes the jump to 4.x

iOS 4.2 is the release that finally unifies the iPhone and iPad SDKs. Consequently, the iPad gains some features that already came to the iPhone in iOS 4.0 and 4.1, such as:

- [C block objects](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007502)
- [Grand Central Dispatch](https://developer.apple.com/library/ios/documentation/Performance/Reference/GCD_libdispatch_Ref/Reference/reference.html#//apple_ref/doc/uid/TP40008079)
- [Multitasking support](https://developer.apple.com/library/ios/#documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/CoreApplication/CoreApplication.html#//apple_ref/doc/uid/TP40007072-CH3-SW1)
- [Local Notifications](https://developer.apple.com/library/ios/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008194)
- [Core Motion](https://developer.apple.com/library/ios/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/MotionEvents/MotionEvents.html#//apple_ref/doc/uid/TP40009541-CH4)
- The [Assets Library](https://developer.apple.com/library/ios/documentation/AssetsLibrary/Reference/ALAssetsLibrary_Class/Reference/Reference.html#//apple_ref/occ/cl/ALAssetsLibrary)
- [Event Kit](https://developer.apple.com/library/ios/documentation/EventKit/Reference/EventKitFrameworkRef/_index.html#//apple_ref/doc/uid/TP40009662) for calendar access
- [iAd](https://developer.apple.com/library/ios/documentation/UserExperience/Reference/iAd_ReferenceCollection/_index.html#//apple_ref/doc/uid/TP40009705)
- [Game Center](https://developer.apple.com/library/ios/#documentation/GameKit/Reference/GameKit_Collection/_index.html#//apple_ref/doc/uid/TP40008303)
- [Quick Look](https://developer.apple.com/library/ios/documentation/QuickLook/Reference/QuickLookFrameworkReference_iPhoneOS/_index.html#//apple_ref/doc/uid/TP40009672)
- The [Accelerate framework](https://developer.apple.com/library/ios/documentation/Accelerate/Reference/AccelerateFWRef/_index.html#//apple_ref/doc/uid/TP40009465)

iPad developers that have been living under a rock over the summer should also have a look at the [What’s New in iOS 4.0](https://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniPhoneOS/Articles/iPhoneOS4.html#//apple_ref/doc/uid/TP40009559-SW1) and [iOS 4.1](https://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniPhoneOS/Articles/iOS4_1.html#//apple_ref/doc/uid/TP40010180-SW1) documents.

# Printing

Apps can now support wireless printing from iOS devices to supported printers. Unfortunately, Apple pulled the functionality to print to any printer shared by an OS X machine on the network at the last minute, but this feature can already be reinstalled with third-party tools such as [Printopia](http://www.ecamm.com/mac/printopia/) or [FingerPrint](http://www.collobos.com/) and [will hopefully return in a future OS X 10.6.x release](http://www.macrumors.com/2010/11/23/steve-jobs-on-airprint-lots-more-coming-soon/).

To support printing in your app, first determine if the device supports printing (`+[UIPrintInteractionController isPrintingAvailable]`), then retrieve the singleton [`UIPrintInteractionController`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIPrintInteractionController_Class/Reference/Reference.html#//apple_ref/occ/cl/UIPrintInteractionController) with `+[UIPrintInteractionController sharedPrintController]` and provide your content to the print controller via one of its `printingItem`, `printingItems`, `printPageRenderer`, or `printFormatter` properties. `UIPrintInteractionController` can directly print images or PDF content (from URLs or in the form of `NSData`, `UIImage`, or `ALAsset` objects).

Via built-in subclasses of the abstract [`UIPrintFormatter`](https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIPrintFormatter_Class/Reference/Reference.html#//apple_ref/occ/cl/UIPrintFormatter) class, the printing of plain text ([`UISimpleTextPrintFormatter`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UISimpleTextPrintFormatter_Class/Reference/Reference.html#//apple_ref/occ/cl/UISimpleTextPrintFormatter)), HTML ([`UIMarkupTextPrintFormatter`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIMarkupTextPrintFormatter_Class/Reference/Reference.html#//apple_ref/occ/cl/UIMarkupTextPrintFormatter)), and `UIView` contents ([`UIViewPrintFormatter`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIViewPrintFormatter_Class/Reference/Reference.html#//apple_ref/occ/cl/UIViewPrintFormatter)) is also supported out of the box.

To render the printable content yourself, subclass [`UIPrintPageRenderer`](https://developer.apple.com/library/ios/documentation/iPhone/Reference/UIPrintPageRenderer_Class/Reference/Reference.html#//apple_ref/doc/c_ref/UIPrintPageRenderer).

# AirPlay

With the 4.2 SDK, third-party apps can use AirPlay to stream *audio- to AirPlay devices such as the Apple TV. Video streaming is not supported at the moment. Apple:

> AirPlay support is built in to the AV Foundation framework and the Core Audio family of frameworks. Any audio content you play using these frameworks is automatically made eligible for AirPlay distribution. Once the user chooses to play your audio using AirPlay, it is routed automatically by the system.

# Core MIDI

[Core MIDI](https://developer.apple.com/library/ios/documentation/MusicAudio/Reference/CACoreMIDIRef/_index.html#//apple_ref/doc/uid/TP40002091) is a new framework to let an iOS device communicate with MIDI devices such as keyboards and synthesizers. It consists of three classes to setup and manage MIDI connections: [`MIDINetworkHost`](https://developer.apple.com/library/ios/documentation/CoreMidi/Reference/MIDINetworkHost_ClassReference/Reference/Reference.html#//apple_ref/doc/uid/TP40010385), [`MIDINetworkConnection`](https://developer.apple.com/library/ios/documentation/CoreMidi/Reference/MIDINetworkConnection_ClassReference/Reference/Reference.html#//apple_ref/doc/uid/TP40010386), and [`MIDINetworkSession`](https://developer.apple.com/library/ios/documentation/CoreMidi/Reference/MIDINetworkSession_ClassReference/Reference/Reference.html#//apple_ref/doc/uid/TP40010387). The framework also includes the C-based [MIDI Services](https://developer.apple.com/library/ios/#documentation/CoreMidi/Reference/MIDIServices_Reference/Reference/reference.html#//apple_ref/doc/uid/TP40010316) API. I have not had the opportunity to investigate this further, especially how to connect a MIDI device to an iPhone or iPad (Apple says devices can be connected via the dock connector or network).

# Weak Linking Support

Developers can now opt to weak-link certain classes (instead of entire frameworks) to their apps that are not available in their deployment target iOS version. This mechanism can simplify the code you need to use to check for the availability of certain features at runtime. Marco Arment has already written a great tutorial on this topic: [Supporting older versions of iOS while using new APIs](http://www.marco.org/1648550153).

# Enhancements to Existing Frameworks

## AVFoundation

- AVAsset now has a property to indicate whether the asset is DRM-protected: [`AVAsset.hasProtectedContent`](https://developer.apple.com/library/ios/#documentation/AVFoundation/Reference/AVAsset_Class/Reference/Reference.html#//apple_ref/occ/instp/AVAsset/hasProtectedContent).
- An asset’s metadata now includes its duration: [`AVMetadataItem.duration`](https://developer.apple.com/library/ios/#documentation/AVFoundation/Reference/AVMetadataItem_Class/Reference/Reference.html#//apple_ref/occ/instp/AVMetadataItem/duration).

## Core Location

- New API for determining if the user has authorized the device/your app to use location services: [`+[CLLocationManager authorizationStatus]`](https://developer.apple.com/library/ios/documentation/CoreLocation/Reference/CLLocationManager_Class/CLLocationManager/CLLocationManager.html#//apple_ref/occ/clm/CLLocationManager/authorizationStatus)
- There is also a new delegate method [`-[CLLocationManagerDelegate locationManager:didChangeAuthorizationStatus:]`](https://developer.apple.com/library/ios/documentation/CoreLocation/Reference/CLLocationManagerDelegate_Protocol/CLLocationManagerDelegate/CLLocationManagerDelegate.html#//apple_ref/occ/intfm/CLLocationManagerDelegate/locationManager:didChangeAuthorizationStatus:) that notifies your app about changes in the authorization status of your app (important for multitasking apps).

## Core Text

- New function: [`CTFontDrawGlyphs()`](https://developer.apple.com/library/ios/#documentation/Carbon/Reference/CTFontRef/Reference/reference.html#//apple_ref/c/func/CTFontDrawGlyphs). No need to convert CTFont objects to Core Graphics fonts with [`CTFontCopyGraphicsFont()`](https://developer.apple.com/library/ios/#documentation/Carbon/Reference/CTFontRef/Reference/reference.html#//apple_ref/doc/uid/TP40005110-CH3-SW56) before drawing them anymore.
- New function: [`CTFontGetLigatureCaretPositions()`](https://developer.apple.com/library/ios/#documentation/Carbon/Reference/CTFontRef/Reference/reference.html#//apple_ref/c/func/CTFontGetLigatureCaretPositions) retrieves a list of possible caret positions inside a ligature.

## Event Kit

`EKEventViewController` now requires you to set a delegate [`EKEventKitViewDelegate`](https://developer.apple.com/library/ios/#documentation/EventKitUI/Reference/EKEventViewDelegateProtocolRef/Reference/Reference.html#//apple_ref/occ/intf/EKEventViewDelegate) that informs your app when the view controller should be closed and what action the user took (tapped the Done button, responded to an event and saved it, or deleted it).

## Game Kit

The new [`GKFriendRequestComposeViewController`](https://developer.apple.com/library/ios/#documentation/GameKit/Reference/GKFriendRequestComposeViewController_Ref/Reference/Reference.html#//apple_ref/occ/cl/GKFriendRequestComposeViewController) and [`GKFriendRequestComposeViewControllerDelegate`](https://developer.apple.com/library/ios/#documentation/GameKit/Reference/GKFriendRequestComposeViewControllerDelegate_Ref/Reference/Reference.html#//apple_ref/occ/intf/GKFriendRequestComposeViewControllerDelegate) can be used to present a screen that allows the player to send Game Center friend requests to other players from inside your app.

## iAd

iAd now supports iPad-sized banners (1024x66 and 768x66 points). Your app should use the `ADBannerContentSizeIdentifierPortrait` and `ADBannerContentSizeIdentifierLandscape` constants to request the appropriate banner size for the current platform.

## Map Kit

- `MKMapView` has a new method: [`-annotationsInMapRect:`](https://developer.apple.com/library/ios/#documentation/MapKit/Reference/MKMapView_Class/MKMapView/MKMapView.html#//apple_ref/doc/uid/TP40008205-CH3-SW46) returns a set of all map annotations in a specified region. According to Apple, “This method is much faster than doing a linear search of the objects in the annotations property yourself.”
- Apps should override `MKAnnotationView`’s new [`-setDrageState:animated:`](https://developer.apple.com/library/ios/#documentation/MapKit/Reference/MKAnnotationView_Class/Reference/Reference.html#//apple_ref/occ/instm/MKAnnotationView/setDragState:animated:) method to implement drag and drop support for custom annotation views. As the system detects user actions that would indicate a drag, it calls this method to update the drag state. In response, your app can perform animations to visualize state changes.

## Media Player

- [`MPMediaEntity`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMediaEntity_ClassReference/Reference/Reference.html#//apple_ref/occ/cl/MPMediaEntity) is the new common abstract superclass for [`MPMediaItem`](https://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/occ/cl/MPMediaItem) and [`MPMediaItemCollection`](https://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMediaItemCollection_ClassReference/Reference/Reference.html#//apple_ref/occ/cl/MPMediaItemCollection). With this change, collections can now contain both items and other collections.
- The [`MPVolumeView`](https://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPVolumeView_Class/Reference/Reference.html#//apple_ref/occ/cl/MPVolumeView) interface now includes a control for routing audio content to AirPlay-enabled devices. It gained two new properties, [`showsRouteButton`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPVolumeView_Class/Reference/Reference.html#//apple_ref/occ/instp/MPVolumeView/showsRouteButton) and [`showsVolumeSlider`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPVolumeView_Class/Reference/Reference.html#//apple_ref/occ/instp/MPVolumeView/showsVolumeSlider), to control which UI elements should be visible.
- Persistent IDs are now not only available for songs, but also for [artists](https://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/c/data/MPMediaItemPropertyArtistPersistentID), [albums](https://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/c/data/MPMediaItemPropertyAlbumPersistentID), [album artists](https://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/c/data/MPMediaItemPropertyAlbumArtistPersistentID), [composers](https://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/c/data/MPMediaItemPropertyComposerPersistentID), [genres](https://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/c/data/MPMediaItemPropertyGenrePersistentID), and [podcasts](https://developer.apple.com/library/ios/documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/c/data/MPMediaItemPropertyPodcastPersistentID).
- [`+[MPMediaItem persistentIDPropertyForGroupingType:]`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/occ/clm/MPMediaItem/persistentIDPropertyForGroupingType:) helps translate between persistent ID keys and [`MPMediaGrouping`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMediaQuery_ClassReference/Reference/Reference.html#//apple_ref/c/tdef/MPMediaGrouping) keys. Similarly, [`+[MPMediaItem titlePropertyForGroupingType:]`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMediaItem_ClassReference/Reference/Reference.html#//apple_ref/occ/clm/MPMediaItem/titlePropertyForGroupingType:) translates between `MPMediaGrouping` keys and title keys.
- Results of a [`MPMediaQuery`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMediaQuery_ClassReference/Reference/Reference.html#//apple_ref/occ/cl/MPMediaQuery) can now further be divided into sections, represented by the new [`MPMediaQuerySection`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMediaQuerySection_ClassReference/Reference/Reference.html#//apple_ref/occ/cl/MPMediaQuerySection) class. Each section has a localized `title` and identifies the `range` of items in the media query that fall into that section. You access a query’s sections through MPMediaQuery’s [`itemSections`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMediaQuery_ClassReference/Reference/Reference.html#//apple_ref/occ/instp/MPMediaQuery/itemSections) or [`collectionSections`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMediaQuery_ClassReference/Reference/Reference.html#//apple_ref/occ/instp/MPMediaQuery/collectionSections) properties.
- [`MPMoviePlayerController`](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMoviePlayerController_Class/MPMoviePlayerController/MPMoviePlayerController.html#//apple_ref/occ/cl/MPMoviePlayerController)’s playback interface has been standardized in the [`MPMediaPlayback` protocol](https://developer.apple.com/library/ios/#documentation/MediaPlayer/Reference/MPMediaPlayback_protocol/Reference/Reference.html#//apple_ref/occ/intf/MPMediaPlayback).

## Quartz Core

- [`CAShapeLayer`](https://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html), the layer class to display Core Graphics paths, gained new properties to control the relative start and end points of the path: [`strokeStart`](https://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html#//apple_ref/occ/instp/CAShapeLayer/strokeStart) and [`strokeEnd`](https://developer.apple.com/library/ios/#documentation/GraphicsImaging/Reference/CAShapeLayer_class/Reference/Reference.html#//apple_ref/occ/instp/CAShapeLayer/strokeEnd). These properties are animatable and should come in handy if you want to animate the creation of a path from start to finish.

## Quick Look

- [`QLPreviewControllerDelegate`](https://developer.apple.com/library/ios/#documentation/NetworkingInternet/Reference/QLPreviewControllerDelegate_Protocol/Reference/Reference.html) gained two new methods to help provide a smooth transition between a document icon or thumbnail and the full-size quick look view. [`-previewController:frameForPreviewItem:inSourceView:`](https://developer.apple.com/library/ios/#documentation/NetworkingInternet/Reference/QLPreviewControllerDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/QLPreviewControllerDelegate/previewController:frameForPreviewItem:inSourceView:) asks for the frame of the preview item to animate a zoom effect between the preview and the full-screen view. [`-previewController:transitionImageForPreviewItem:contentRect:`](https://developer.apple.com/library/ios/#documentation/NetworkingInternet/Reference/QLPreviewControllerDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/QLPreviewControllerDelegate/previewController:transitionImageForPreviewItem:contentRect:) requests a `UIImage` of the preview item that the quick look controller can crossfade with during the zoom animation.

## UIKit

- New “scroll by page” capabilities using VoiceOver. If your app contains a view that supports a scroll by page action, you should implement the [`-accessibilityScroll:`](https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIAccessibilityAction_Protocol/Introduction/Introduction.html#//apple_ref/occ/instm/NSObject/accessibilityScroll:) method in the [`UIAccessibilityAction` informal protocol](https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIAccessibilityAction_Protocol/Introduction/Introduction.html).
- `UIApplicationDelegate` has a new method, [`-application:openURL:sourceApplication:annotation:`](https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIApplicationDelegate_Protocol/Reference/Reference.html#//apple_ref/occ/intfm/UIApplicationDelegate/application:openURL:sourceApplication:annotation:), which provides your app with further information when it was launched from another app. You not only get notified which app launched yours, but the calling application can also pass arbitrary data in the form of a property list to your app using the `annotation` argument. Unfortunately, the `annotation` property is only available if the calling app uses [`UIDocumentInteractionController`](https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIDocumentInteractionController_class/Reference/Reference.html). If the calling app uses [`-[UIApplication openURL:]`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/Reference/Reference.html#//apple_ref/doc/uid/TP40006728-CH3-SW14), it still has to resort to [URL parameters](http://mobileorchard.com/lite-to-paid-iphone-application-data-migrations-with-custom-url-handlers/) to pass information along.
- `UIDevice` now has a [-playInputClick](https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIDevice_Class/Reference/UIDevice.html#//apple_ref/occ/instm/UIDevice/playInputClick) method that lets us play the standard keyboard click sound from our app. A click plays only if the user has enabled keyboard clicks. Yay!
- The `UITextInputMode` class now exposes the language in use for inputting text. [primaryLanguage](https://developer.apple.com/library/ios/#documentation/UIKit/Reference/UITextInputMode_Class/Reference/Reference.html#//apple_ref/occ/instp/UITextInputMode/primaryLanguage) property.
