---
title: iOS 4.1 Release Notes
apple_id: TP40010153
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2010-08-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iPhoneSDK-4_1/index.html
archived_at: '2026-07-18T02:54:42.786740Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 4.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjtfvbuqmjnknltg)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjtfvbuqmjnknlti)
- [Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcnjtfvbuqmjnknlte)

### Introduction

iOS SDK 4.1 provides support for developing iOS applications and includes the complete set of Xcode tools, compilers, and frameworks for creating applications for iOS and Mac OS X. These tools include the Xcode IDE and the Instruments analysis tool among many others.

With this software you can develop applications that run on iPhone or iPod touch running iOS 4.1. Additionally, you can develop applications for iPad, which runs iOS 3.2. You can also test your applications using the included iOS Simulator, which supports both iOS 4.1 and iOS 3.2. Installing iOS SDK 4.1 requires a Macintosh computer running Mac OS X 10.6.2 (Snow Leopard) or later.

We encourage developers to apply to the iOS Developer Program for access to additional support resources, including provisioning resources to enable development directly on an iOS-based device. For more information visit:

[http://developer.apple.com/devcenter/ios/program/](https://developer.apple.com/devcenter/ios/program/)

### Bug Reporting

Please report any bugs not mentioned in the "Known Issues" section using the Apple Bug Reporter on the Developer Connection website at: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/).

### Known Issues

The following issues relate to using the 4.1 SDK to develop code.

### Xcode

- Xcode can hang sometimes when doing a clean build if you are running on Mac OS X 10.6.3 or lower. To fix this problem please upgrade to Mac OS X 10.6.4 (Software update to Snow Leopard).

### AVFoundation

- The [AVQueuePlayer](https://developer.apple.com/documentation/avfoundation/avqueueplayer) class is now available in AV Foundation. This class allows you to play a sequence of [AVPlayerItem](https://developer.apple.com/documentation/avfoundation/avplayeritem) objects.
- The [AVAssetReader](https://developer.apple.com/documentation/avfoundation/avassetreader) and [AVAssetWriter](https://developer.apple.com/documentation/avfoundation/avassetwriter) classes and their supporting classes are now available in AV Foundation. The `AVAssetReader` class allows clients to read decompressed samples from media. The `AVAssetWriter` class allows clients to supply uncompressed samples for compression and file writing.

### Debugger

- When debugging your multitasking enabled app, avoid manually pausing and continuing from the debugger when the application is suspended in the background. Pausing an application that is suspended in the background disrupts proper multitasking behavior until the application is relaunched.

### GameKit

- In this release, a Game Center-aware application's bundle name must conform to RFC1808. It may not include spaces or other characters not allowed in the definition for 'pchar'.
- Game Center supports iPhone 4, iPhone 3GS, and iPod touch (second-generation and higher)
- To access a leaderboard, applications now need to specify the leaderboard's category identifier string.
- APIs that previously returned or took a [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer) object now take a player identifier string.
- A range checking exception has been added to leaderboard requests.
- Apps no longer have access to the players' status.
- Apps using the iOS 4 Game Center Preview are no longer supported. Only apps using the iOS 4.1 (or greater) version of Game Center are supported.
- For this release, `GameKitPreview.h` was renamed `Gamekit.h`.
- For iOS 4.1, the string format used by the [playerID](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid) property (of the `GKPlayer` class) changed. Your application should never assume anything about the length or format of a player identifier string.

### iAd

- In some cases, changing the center, transform, bounds, or alpha properties of an ADBannerView may not have the expected outcome. To ensure correct results when changing these properties, reset the hidden property after changing these properties. For example:

  bannerView.center = newCenter;

  bannerView.hidden = bannerView.hidden;
- Animating the alpha property of an ADBannerView to 0.0 may not render correctly. To work around this limitation, use a small value greater than 0.0, such as 0.01.

### Instruments

- _NEW:_ In Energy Diagnostic instrument the CPU activity instrument is not reporting activity for Foreground app, Audio processing and Graphics

### Media Player

- If your application plays background audio, it is recommended that you implement support for remote-control events to let users control the audio directly from the application switcher. For more information, see Remote Control of Multimedia in _Event Handling Guide for iOS_.

### Simulator

- _NEW:_ For the simulator SDKs Static Analyzer results are not displayed. To workaround this problem you can switch to device SDKs from the overview pop-up.
- _NEW:_ The iPhone 4 profile with the 4.0.1 SDK in the simulator will not behave correctly. You can workaround the problem by:

  sudo ln -s \

  /Developer/Platforms/iOS Simulator.platform/Developer/SDKs/iOS Simulator4.0.sdk/System/Library/CoreServices/SpringBoard.app/N90AP.plist

  /Developer/Platforms/iOS Simulator.platform/Developer/SDKs/iOS Simulator4.0.sdk/System/Library/CoreServices/SpringBoard.app/iPhone4Simulator.plist

### UIKit

- Setting some animatable properties inside a transition animation block may not work.
- The default behavior for the new `UIView` block-based animation API in iOS 4 is to disable user interactions across the whole interface while the animation is playing. Developers should not rely on this behavior remaining the default as it may be reversed in future releases, thereby allowing user interactions to occur by default while the animation is playing. Programs compiled against iOS SDK 4 will continue to work as-is, but code compiled under future versions of the SDK may require setting a different option flag to enable the original behavior.
- The default behavior for the new `UIView` block-based animation API in iOS 4 is to inherit the animation duration from an enclosing animation block (when present). Developers should not rely on this behavior remaining the default, as it may be reversed in future releases, thereby preventing animations from automatically inheriting the duration of their enclosing animation. Programs compiled against iOS SDK 4.0 will continue to work as-is but code compiled under future versions of the SDK may require setting a different option flag to enable the original behavior.
