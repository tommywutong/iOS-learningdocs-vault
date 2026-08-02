---
title: iOS 6.1 Release Notes
apple_id: TP40012869
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2013-01-28'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-6_1/index.html
archived_at: '2026-07-18T02:54:41.999270Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 6.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnrzfvbuqmjnknlte)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnrzfvbuqmjnknltg)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnrzfvbuqmjnknlti)

### Introduction

iOS SDK 6.1 provides support for developing iOS apps, and it includes the complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 6.1. You can also test your apps using the included iOS Simulator, which supports iOS 6.1. iOS SDK 6.1 requires a Mac computer running OS X v10.7.4 (Lion) or later.

This version of iOS is intended for installation only on devices registered with Apple’s Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

To report any bugs not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnrzfvbuqmjnknlti) section, use the Apple Bug Reporter on the Apple Developer website ([http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 6.1 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/). You can get more information about iCloud for Developers at [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

The following issues relate to using iOS SDK 6.1 to develop code.

### Core Image

### Notes

- In iOS 6.0 and later, Core Image introduced new filters to the set provided in iOS 5. The complete set of filters can be found in _[Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346)_.
- In iOS 6.0 and later, Core Image allows for the creation of [CIImage](https://developer.apple.com/documentation/coreimage/ciimage) objects that reference OpenGL texture objects via the [imageWithTexture:size:flipped:colorSpace:](https://developer.apple.com/documentation/coreimage/ciimage/1547006-imagewithtexture) method.

### Known Issues

None.

### iCloud

### Notes

None.

### Known Issues

Moving data from a local sandbox to iCloud using `migratePersistentStore` causes a crash. Instead, manually migrate the data store by iterating over the objects in the local data store file.

### Language Support: Thai

### Notes

iOS 6.0 introduced a five-row Thai keyboard and removed the previous four-row keyboard. In iOS 6.1, both the five-row and the four-row Thai keyboards are available.

### Known Issues

None.

### Maps

### Notes

In iOS 6.1, the Map Kit framework introduces the [MKLocalSearch](https://developer.apple.com/documentation/mapkit/mklocalsearch), [MKLocalSearchRequest](https://developer.apple.com/documentation/mapkit/mklocalsearch/request), and [MKLocalSearchResponse](https://developer.apple.com/documentation/mapkit/mklocalsearch/response) classes. Apps can use these classes to perform map-based searches for addresses and points of interest. The results are then delivered to the app as an array of map item objects. For information about these new classes, see _[Map Kit Framework Reference](https://developer.apple.com/documentation/mapkit)_.

### Known Issues

Please note that this API is not currently supported for use in Japan and Russia.

### Passbook

### Notes

As of iOS 6.1, the relevance behavior has changed for boarding passes that include both a relevant date and a relevant location. The date must match for these passes to be relevant. If both the date and location match, they are relevant for a longer window of time. You are encouraged to provide both pieces of information when they make sense for your passes.

### Known Issues

None.

### Settings

### Notes

In iOS 6.1, a new Reset Advertising Identifier button has been added to Advertising Settings. This button resets the Advertising Identifier so that future requests will return a different value.

### Known Issues

None.

### Social

### Notes

- Weibo shows up in the Settings app only if a Chinese keyboard is enabled.

- When using the iOS 6.1 SDK on OS X v10.8 (Mountain Lion), if you use the iOS 5.0 or iOS 5.1 “Legacy SDK” in iOS Simulator, you will not be able to sign in to Twitter via the Settings pane, and `Twitter.framework` will not work correctly. If you need to test Twitter features, you will need to choose either the iOS 6.1 or iOS 6.0 Simulator run destination, or test with iOS 5.x on a device. These problems do not occur when running Simulator on OS X v10.7 (Lion).

### Known Issues

None.

### UIKit

### Notes

- [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) drawing additions and [UILabel](https://developer.apple.com/documentation/uikit/uilabel) do not support [NSTextAlignmentJustified](https://developer.apple.com/documentation/uikit/nstextalignment/justified) or [NSTextAlignmentNatural](https://developer.apple.com/documentation/uikit/nstextalignment/nstextalignmentnatural) text alignments. Instead, use [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString) drawing additions, which support all text alignments.
- In iOS 6.0, when an app with a valid state restoration archive is starting up, a snapshot of the app is displayed instead of the `default.png` image. In iOS 6.1, the snapshot is not displayed in this situation, because there are cases where the snapshot would not be appropriate. Instead, the `default.png` image is always displayed.

### Known Issues

None.
