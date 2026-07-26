---
title: 'What''s New in iOS SDK 4.2'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/11/whats-new-in-ios-sdk-4-2/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:c6b69bad76cffacb'
translated: false
---

> 原文：[What's New in iOS SDK 4.2](https://oleb.net/blog/2010/11/whats-new-in-ios-sdk-4-2/)　·　Ole Begemann

# What's New in iOS SDK 4.2

Now that the [final version of iOS SDK 4.2](http://developer.apple.com/devcenter/ios/) is available, let’s have a look at what is new. What follows is a detailed overview of the [What’s New in iOS 4.2](https://developer.apple.com/library/ios/#releasenotes/General/WhatsNewIniPhoneOS/Articles/iOS4.html#//apple_ref/doc/uid/TP40010313-SW1) and [iOS 4.2 API Diffs](https://developer.apple.com/library/ios/#releasenotes/General/iOS42APIDiffs/index.html#//apple_ref/doc/uid/TP40010312) documents.

# The iPad makes the jump to 4.x

iOS 4.2 is the release that finally unifies the iPhone and iPad SDKs. Consequently, the iPad gains some features that already came to the iPhone in iOS 4.0 and 4.1, such as:

- C block objects
- Grand Central Dispatch
- Multitasking support
- Local Notifications
- Core Motion
- Assets Library
- Event Kit

  for calendar access
- iAd
- Game Center
- Quick Look
- Accelerate framework

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

- `AVAsset.hasProtectedContent`

  .
- `AVMetadataItem.duration`

  .

## Core Location

- `+[CLLocationManager authorizationStatus]`
- `-[CLLocationManagerDelegate locationManager:didChangeAuthorizationStatus:]`

  that notifies your app about changes in the authorization status of your app (important for multitasking apps).

## Core Text

- `CTFontDrawGlyphs()`

  . No need to convert CTFont objects to Core Graphics fonts with

  `CTFontCopyGraphicsFont()`

  before drawing them anymore.
- `CTFontGetLigatureCaretPositions()`

  retrieves a list of possible caret positions inside a ligature.

## Event Kit

`EKEventViewController` now requires you to set a delegate [`EKEventKitViewDelegate`](https://developer.apple.com/library/ios/#documentation/EventKitUI/Reference/EKEventViewDelegateProtocolRef/Reference/Reference.html#//apple_ref/occ/intf/EKEventViewDelegate) that informs your app when the view controller should be closed and what action the user took (tapped the Done button, responded to an event and saved it, or deleted it).

## Game Kit

The new [`GKFriendRequestComposeViewController`](https://developer.apple.com/library/ios/#documentation/GameKit/Reference/GKFriendRequestComposeViewController_Ref/Reference/Reference.html#//apple_ref/occ/cl/GKFriendRequestComposeViewController) and [`GKFriendRequestComposeViewControllerDelegate`](https://developer.apple.com/library/ios/#documentation/GameKit/Reference/GKFriendRequestComposeViewControllerDelegate_Ref/Reference/Reference.html#//apple_ref/occ/intf/GKFriendRequestComposeViewControllerDelegate) can be used to present a screen that allows the player to send Game Center friend requests to other players from inside your app.

## iAd

iAd now supports iPad-sized banners (1024x66 and 768x66 points). Your app should use the `ADBannerContentSizeIdentifierPortrait` and `ADBannerContentSizeIdentifierLandscape` constants to request the appropriate banner size for the current platform.

## Map Kit

- has a new method:

  `-annotationsInMapRect:`

  returns a set of all map annotations in a specified region. According to Apple, “This method is much faster than doing a linear search of the objects in the annotations property yourself.”
- ’s new

  `-setDrageState:animated:`

  method to implement drag and drop support for custom annotation views. As the system detects user actions that would indicate a drag, it calls this method to update the drag state. In response, your app can perform animations to visualize state changes.

## Media Player

- `MPMediaEntity`

  is the new common abstract superclass for

  `MPMediaItem`

  and

  `MPMediaItemCollection`

  . With this change, collections can now contain both items and other collections.
- `MPVolumeView`

  interface now includes a control for routing audio content to AirPlay-enabled devices. It gained two new properties,

  `showsRouteButton`

  and

  `showsVolumeSlider`

  , to control which UI elements should be visible.
- artists

  ,

  albums

  ,

  album artists

  ,

  composers

  ,

  genres

  , and

  podcasts

  .
- `+[MPMediaItem persistentIDPropertyForGroupingType:]`

  helps translate between persistent ID keys and

  `MPMediaGrouping`

  keys. Similarly,

  `+[MPMediaItem titlePropertyForGroupingType:]`

  translates between

  keys and title keys.
- `MPMediaQuery`

  can now further be divided into sections, represented by the new

  `MPMediaQuerySection`

  class. Each section has a localized

  and identifies the

  of items in the media query that fall into that section. You access a query’s sections through MPMediaQuery’s

  `itemSections`

  or

  `collectionSections`

  properties.
- `MPMoviePlayerController`

  ’s playback interface has been standardized in the

  `MPMediaPlayback` protocol

  .

## Quartz Core

- `CAShapeLayer`

  , the layer class to display Core Graphics paths, gained new properties to control the relative start and end points of the path:

  `strokeStart`

  and

  `strokeEnd`

  . These properties are animatable and should come in handy if you want to animate the creation of a path from start to finish.

## Quick Look

- `QLPreviewControllerDelegate`

  gained two new methods to help provide a smooth transition between a document icon or thumbnail and the full-size quick look view.

  `-previewController:frameForPreviewItem:inSourceView:`

  asks for the frame of the preview item to animate a zoom effect between the preview and the full-screen view.

  `-previewController:transitionImageForPreviewItem:contentRect:`

  requests a

  of the preview item that the quick look controller can crossfade with during the zoom animation.

## UIKit

- `-accessibilityScroll:`

  method in the

  `UIAccessibilityAction` informal protocol

  .
- has a new method,

  `-application:openURL:sourceApplication:annotation:`

  , which provides your app with further information when it was launched from another app. You not only get notified which app launched yours, but the calling application can also pass arbitrary data in the form of a property list to your app using the

  argument. Unfortunately, the

  property is only available if the calling app uses

  `UIDocumentInteractionController`

  . If the calling app uses

  `-[UIApplication openURL:]`

  , it still has to resort to

  URL parameters

  to pass information along.
- now has a

  -playInputClick

  method that lets us play the standard keyboard click sound from our app. A click plays only if the user has enabled keyboard clicks. Yay!
- class now exposes the language in use for inputting text.

  primaryLanguage

  property.
