---
title: iOS 7.1 Release Notes
apple_id: TP40013935
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-7.1/index.html
archived_at: '2026-07-18T02:54:42.133793Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 7.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmzvfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmzvfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmzvfvbuqmjnknlti)

### Introduction

iOS SDK 7.1 provides support for developing iOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 7. You can also test your apps using the included iOS Simulator, which supports iOS 7. iOS SDK 7.1 requires a Mac computer running OS X v10.8.4 (Mountain Lion) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

To report any bugs not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztsmzvfvbuqmjnknlti) section, use the Apple Bug Reporter on the Apple Developer website ([http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 7.1 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following issues relate to using iOS SDK 7.1 to develop code.

### Bluetooth

### Known Issue

32-bit apps running on a 64-bit device cannot attach to BTServer.

### CFNetwork

### Notes

A compatibility behavior has been added to address an issue where some web servers would send the wrong Content-Length value for “Content-Encoding: gzip” content. Previously, [NSURLConnection](https://developer.apple.com/documentation/foundation/nsurlconnection) and [NSURLSession](https://developer.apple.com/documentation/foundation/urlsession) would send a “network connection was lost” / NSURLErrorNetworkConnectionLost (-1005) error in this situation.

The compatibility behavior applies only if the Content-Length value exactly matches the expanded gzip’d content. It won’t apply for “off by 1” or similar miscounting.

### Safari

### Notes

A property, _minimal-ui_, has been added for the viewport meta tag key that allows minimizing the top and bottom bars on the iPhone as the page loads. While on a page using _minimal-ui_, tapping the top bar brings the bars back. Tapping back in the content dismisses them again.

For example, use _<meta name="viewport" content="width=1024, minimal-ui”>_.

### Siri

### Notes

iOS 7.1 adds new natural-sounding Siri voices for English (Australia), English (United Kingdom), Japanese, and Chinese (Mandarin - China).

The iOS device initially uses a compact voice for Siri. After you have configured a Wi-Fi network and have the device connected to a power source, iOS will automatically download and install a higher quality version.

### UIKit

### Known Issues

- Bar button background images are ignored in apps built and deployed to iOS 7.1 when they are set using [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem) [setBackgroundImage:forState:style:barMetrics:](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617161-setbackgroundimage) with [UIBarButtonItemStyleBordered](https://developer.apple.com/documentation/uikit/uibarbuttonitemstyle/uibarbuttonitemstylebordered) as the style argument.

  __Workaround:__ Use [UIBarButtonItemStylePlain](https://developer.apple.com/documentation/uikit/uibarbuttonitem/style/plain) or `UIBarButtonItemStyleAny` in this case, or use [UIBarButtonItem](https://developer.apple.com/documentation/uikit/uibarbuttonitem) [setBackgroundImage:forState:barMetrics:](https://developer.apple.com/documentation/uikit/uibarbuttonitem/1617138-setbackgroundimage).
- If a [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) or a [UILabel](https://developer.apple.com/documentation/uikit/uilabel) that is baseline aligned with constraints has attributes that change after the constraints have been added, the layout may be incorrect. The exception to this is `-setFont:` on [UILabel](https://developer.apple.com/documentation/uikit/uilabel), which should work as expected.

  __Workaround:__ Avoid making changes in [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) or [UILabel](https://developer.apple.com/documentation/uikit/uilabel) after adding baseline-alignment constraints. If you must make changes, you should remove the constraints and then reapply them afterward. Note that this is a performance hit, so don’t do it unless it is necessary.
- The [backIndicatorTransitionMaskImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624938-backindicatortransitionmaskimage) from a storyboard or a xib will not be interpreted correctly at runtime.

  __Workaround:__ Set the [backIndicatorTransitionMaskImage](https://developer.apple.com/documentation/uikit/uinavigationbar/1624938-backindicatortransitionmaskimage) in code.
