---
title: iOS 4.2 Release Notes
apple_id: TP40010243
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-4_2/index.html
archived_at: '2026-07-18T02:54:41.736069Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 4.2

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydenbtfvbuqmjnknltg)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydenbtfvbuqmjnknlti)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydenbtfvbuqmjnknlte)

### Introduction

iOS SDK 4.2 provides support for developing iOS applications and includes the complete set of Xcode tools, compilers, and frameworks for creating applications for iOS and Mac OS X. These tools include the Xcode IDE and the Instruments analysis tool among many others.

With this software you can develop applications that run on iPhone, iPad, or iPod touch running iOS 4.2. You can also test your applications using the included iOS Simulator, which supports iOS 4.2. Installing iOS SDK 4.2 requires a Macintosh computer running Mac OS X 10.6.4 (Snow Leopard) or later.

For more information and additional support resources, visit:

[http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/)

### Bug Reporting

Please report any bugs not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydenbtfvbuqmjnknlte) section using the Apple Bug Reporter on the Apple Developer website at: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/). Additionally, you may discuss these issues and iOS SDK 4.2 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/).

### Notes and Known Issues

The following issues relate to using the 4.2 SDK to develop code.

### Xcode

- If you are upgrading your iPad from iOS 4.2 GM Seed to iOS 4.2 GM, Xcode will extract symbols from the device the first time you connect the device. This process takes only a few minutes.
- There is a new Base SDK setting called "Latest SDK". This is the recommended choice for all projects and will cause your project to always build against the newest available iOS SDK.
- The Overview popup menu will display "Base SDK Missing" if a project was created with an SDK earlier than iOS SDK 4.2. However, after selecting a new SDK that Overview popup may still display "Base SDK Missing".

  To work around the issue, close and reopen the project window.

### Audio

- The iPad screen rotation lock switch now functions as a sound/silent switch in iOS 4.2. This switch behaves the same way as the Ring/Silent switch on iPhone.

  Applications targeted for iPad will need to take this into account when implementing audio behaviors.

  For more information on audio behavior guidelines and how to implement them, see User Experience Guidelines in _iPhone Human Interface Guidelines_ and the _[Audio Session Programming Guide](../../documentation/Audio/Audio%20Session%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tqnzv)_.

### Calendar

- Calendar can now import `.ics` files directly as a way to add events. If your app has access to `.ics` files, you should test importing them using the [UIDocumentInteractionController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller) API.

### GameKit

- Applications can use the [GKFriendRequestComposeViewController](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller) class to initiate friend requests.
- The GameKit view controllers for leaderboards, achievements, matchmaking, and friend requests must be presented modally. Presenting them any other way will result in an exception and unexpected behavior. This affects [GKLeaderboardViewController](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller), [GKAchievementViewController](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller), [GKMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller) and [GKFriendRequestComposeViewController](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller).
- In iOS 4.2, the local player is automatically authenticated again when an app enters the foreground. This will generate an authentication changed notification. If the app is linked with iOS 4.2 or later, the authentication completion handler will also be called (it is retained indefinitely).

### GDB

- During debugging, pausing or resuming an iOS application while it is backgrounded is currently unsupported and can result in undefined application behavior.

### MapKit

- For applications built against iOS 4.2 and later, MapKit will now conditionally display annotation views based on the currently visible region of the map. To account for this, developers should make sure they reuse annotation views as documented and never assume that the absence of an annotation view implies the absence of a corresponding annotation

### Printing

- iOS 4.2 devices can print wirelessly only to printers that support AirPrint and are running the latest available firmware. Some currently available printers that support AirPrint are:

  - HP Photosmart Premium Fax e-All-in-One Printer - C410
  - HP Photosmart Premium e-All-in-One Printer series - C310
  - HP Photosmart Plus e-All-in-One Printer series - B210
  - HP ENVY 100 e-All-in-One Printer Series - D410
  - HP Photosmart eStation Printer series - C510

### Simulator

- Building an app that weak links `CoreVideo.framework` against the 4.2 Simulator SDK and then running that application against the 3.2 Simulator will result in a crash. The same configuration will work when building against the 4.2 device SDK and running on a 3.2 device.

### Weak Linking

- The following frameworks currently do not support weak linking by way of the `NS_CLASS_AVAILABLE` macro:

  - AV Foundation
  - Core Animation
  - Core Telephony
  - MobileLaunchServices

  When targeting older versions of iOS, you can check the class availability in these frameworks by calling the [NSClassFromString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSClassFromString) function and seeing if it returns a non-`nil` value. For information about using the `NS_CLASS_AVAILABLE` macro, see iOS 4.2 in _[What's New in iOS](What%27s%20New%20in%20iOS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denbw)_.
