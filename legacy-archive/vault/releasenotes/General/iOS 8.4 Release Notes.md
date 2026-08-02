---
title: iOS 8.4 Release Notes
apple_id: TP40015246
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-06-30'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-8.4/index.html
archived_at: '2026-07-18T02:54:42.379043Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 8.4

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbwfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbwfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbwfvbuqmjnknlti)

### Introduction

iOS SDK 8.4 provides support for developing iOS apps. The SDK is packaged with a complete set of tools, compilers, and frameworks for creating apps for iOS and OS X. The tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software, you can develop apps for iPhone, iPad, or iPod touch running iOS 8. It now includes WatchKit, a framework for developing Apple Watch apps. You can test your apps using the included iOS Simulator.

iOS SDK 8.4 requires a Mac computer running OS X v10.10 (Yosemite) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbwfvbuqmjnknlti) section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/ios/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 8.4 in the Apple Developer Forums: [https://forums.developer.apple.com](https://forums.developer.apple.com/). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following issues relate to using iOS SDK 8.4 to develop code.

### App Extensions

### Notes

- App extensions need an arm64 slice to run on 64-bit devices. If you try to run the armv7 slice on a 64-bit device it won’t work.
- Apps need to have an arm64 slice if the bundle contains a framework that both the app and the app extension link against.

### Music

### Known Issue

- Home Sharing and Genius Mixes are not currently available.
- The Music app may forget its place when you go to the Home screen and come back.

### Siri

“Play <Song> Siri” requests from a watch are failing for a few days when the iPhone has a new install of iOS 8.4.

__Workaround:__ Request playback of Artists or Albums instead of a specific song.

### UIKit

When linking against iOS 8.3 or later, any code that relies on layout information (such as the frame) of a [UIButton](https://developer.apple.com/documentation/uikit/uibutton) subview when the button is not in the window hierarchy will need to send [layoutIfNeeded](https://developer.apple.com/documentation/uikit/uiview/1622507-layoutifneeded) to the button before retrieving layout information (such as `button.titleLabel.frame`) to ensure that the layout values are up to date.

For example, if you had something like this:

```
UIButton *button = [UIButton buttonWithType:UIButtonTypeSystem];
// code that sets up the button, but doesn’t yet add it to a window
CGRect titleFrame = button.titleLabel.frame;
// code that relies on the correct value for titleFrame
```

You now need:

```
UIButton *button = [UIButton buttonWithType:UIButtonTypeSystem];
// code that sets up the button, but doesn’t yet add it to a window
[button layoutIfNeeded]; // This is also safe pre-iOS 8.3
CGRect titleFrame = button.titleLabel.frame;
// code that relies on the correct value for titleFrame
```


### WatchKit

### Note

A bug where continuous background location updates fail to update has been resolved. If your Watch app relies on continuous background location updates to function, it is recommended that you update your WatchKit extension deployment target to iOS 8.3 and submit your app with Xcode 6.3.

### Known Issue

- Creating an animated image using the [UIImage](https://developer.apple.com/documentation/uikit/uiimage) method [animatedImageWithImages:duration:](https://developer.apple.com/documentation/uikit/uiimage/1624149-animatedimagewithimages) and then playing the animation using `startAnimating` ignores the duration and plays back as fast as possible.

  __Workaround:__ Use `startAnimatingWithImagesInRange:duration:repeatCount:` instead.
