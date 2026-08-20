---
title: iOS 4.3 Release Notes
apple_id: TP40010565
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2011-02-28'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-4_3/index.html
archived_at: '2026-07-18T02:54:41.776458Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 4.3

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknrvfvbuqmjnknltg)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknrvfvbuqmjnknlti)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknrvfvbuqmjnknlte)

### Introduction

iOS SDK 4.3 provides support for developing iOS applications and includes the complete set of Xcode tools, compilers, and frameworks for creating applications for iOS and Mac OS X. These tools include the Xcode IDE and the Instruments analysis tool among many others.

With this software you can develop applications that run on iPhone, iPad, or iPod touch running iOS 4.3. You can also test your applications using the included iOS Simulator, which supports iOS 4.3. Installing iOS SDK 4.3 requires a Macintosh computer running Mac OS X 10.6.6 or later.

For more information and additional support resources, visit:

[http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/)

### Bug Reporting

Please report any bugs not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknrvfvbuqmjnknlte) section using the Apple Bug Reporter on the Apple Developer website at: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/). Additionally, you may discuss these issues and iOS SDK 4.3 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/).

### Notes and Known Issues

The following issues relate to using the 4.3 SDK to develop code.

### AirPlay Video

- AirPlay Video requires the AppleTV Software.
- AirPlay Video support is now available as an option for developers in the [MPMoviePlayerController](https://developer.apple.com/documentation/mediaplayer/mpmovieplayercontroller) class. It is also available to web authors via the QuickTime Plug-In or media element. Supported formats include:

  - H.264 video with AAC audio
  - HTTP streaming, both live and on demand
  - progressive download content
  - local content
- For web-based content, AirPlay Video can be enabled in the QuickTime Plug-in or HTML5 video element as described below:

  - QTPlug-in:

    - `airplay="allow"`
    - `airplay="deny"` (Default)

    For example: `<embed src="movie.mov" width="320" height="240" airplay="allow">`
  - HTML5 video element:

    - `x-webkit-airplay="allow"`
    - `x-webkit-airplay="deny" (Default)`

    For example: `<video controls width="640" height="368" x-webkit-airplay="allow" src="movie.mov"> </video>`

### iAD

- The new API, `ADInterstitialView`, has been removed and replaced with the [ADInterstitialAd](https://developer.apple.com/documentation/iad/adinterstitialad) class, which inherits from `NSObject`, not from `UIView`. Behavior has not changed except that two new methods are available, [presentInView:](https://developer.apple.com/documentation/iad/adinterstitialad/1614646-presentinview) and `presentFromViewController:`, that formalize two distinct use cases. For additional information on these API changes, see _[ADInterstitialAd Class Reference](https://developer.apple.com/documentation/iad/adinterstitialad)_. The sample code, _[iAdInterstitialSuite](../../samplecode/iAdInterstitialSuite/iAdInterstitialSuite.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytanrsg4)_, has also been updated to work with these API changes.

  - The [presentInView:](https://developer.apple.com/documentation/iad/adinterstitialad/1614646-presentinview) method should be used in paging applications, such as magazines, and requires that the application provide a container view in a view controller-managed view hierarchy in which the interstitial ad will be displayed.
  - The [presentFromViewController:](https://developer.apple.com/documentation/iad/adinterstitialad/1621985-presentfromviewcontroller) method displays the interstitial ad with a modal presentation, suitable as a transition between game levels.

### Multitasking Gestures

This release contains a preview of new multitasking gestures for iPad. You can use four or five fingers to pinch to the Home Screen, swipe up to reveal the multitasking bar, and swipe left or right between apps. This feature will not be enabled in iOS 4.3 for customers, but we are providing this preview to gather input on how these gestures work with your apps.

Developers are encouraged to evaluate any existing interactions in their applications for potential sources of interference. In order to properly interoperate with multitasking gestures, applications must properly handle the following methods and notifications:

- [touchesCancelled:withEvent:](https://developer.apple.com/documentation/uikit/uiresponder/1621116-touchescancelled) (`UIResponder`)
- [cancelTrackingWithEvent:](https://developer.apple.com/documentation/uikit/uicontrol/1618219-canceltrackingwithevent) (`UIControl`)
- [applicationDidBecomeActive:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622956-applicationdidbecomeactive) and [applicationWillResignActive:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622950-applicationwillresignactive) (application delegate)
- [UIApplicationDidBecomeActiveNotification](https://developer.apple.com/documentation/uikit/uiapplication/1622953-didbecomeactivenotification) and [UIApplicationWillResignActiveNotification](https://developer.apple.com/documentation/uikit/uiapplication/1622973-willresignactivenotification) notifications

These can be enabled for development via Xcode so you can update your apps to interoperate with these new gestures. Test them and give us your feedback in the Apple Developer Forums.

### Xcode

- _NEW:_ The use of composite SDKs with distributed builds can, on occasion, cause exceptions during the build process. To avoid these issues, disable distributed builds for those projects that use composite SDKs.
- _NEW:_ While running an application on a device with an iOS version earlier than 4.3, you might not be able to see formatted content of variables and a `"/Developer/usr/lib/libXcodeDebuggerSupport.dylib (file not found)"` message is shown in the gdb console window. You can use the `po` command in gdb console to get around the issue.
- _NEW:_ Installing Xcode 3.2.6 over Xcode 4 (or later)—that is, installing both into the same directory (normally the `/Developer` directory)—is not a supported configuration and is likely to result in a non-functional install.

  Installing Xcode 4 or later over older Xcode installations should work. Similarly, installing the two versions to separate directories should work (preferred order is older first, then newer).
- Xcode 4 does not automatically download the documentation for iOS 4.3. To do so manually, launch Xcode and open the Preferences window. In the Documentation tab, click the Get button next to the iOS 4.3 Library to begin the download.
