---
title: iOS 4.3.2 Release Notes
apple_id: TP40010884
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/releasenotes/Miscellaneous/RN-iOSSDK-4_3_2/index.html
archived_at: '2026-07-18T02:58:58.765606Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 4.3.2

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqobufvbuqmjnknltg)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqobufvbuqmjnknlti)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqobufvbuqmjnknlte)

### Introduction

iOS SDK 4.3.2 is an update to iOS 4.3 which provides support for developing iOS applications and includes the complete set of Xcode tools, compilers, and frameworks for creating applications for iOS and Mac OS X. These tools include the Xcode IDE and the Instruments analysis tool among many others.

With this software you can develop applications that run on iPhone, iPad, or iPod touch running iOS 4.3 or iOS 4.3.2. You can also test your applications using the included iOS Simulator, which supports iOS 4.3. Installing iOS SDK 4.3.2 requires a Macintosh computer running Mac OS X 10.6.6 or later.

For more information and additional support resources, visit:

[http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/)

### Bug Reporting

Please report any bugs not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqobufvbuqmjnknlte) section using the Apple Bug Reporter on the Apple Developer website at: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/). Additionally, you may discuss these issues and iOS SDK 4.3.2 in the Apple Developer Forums: [http://devforums.apple.com](http://devforums.apple.com/).

### Notes and Known Issues

The following issues relate to using the 4.3.2 SDK to develop code.

### Xcode

- _NEW:_ While running an application on a device with an iOS version 4.3 or earlier, you might not be able to see formatted content of variables and a “/Developer/usr/lib/libXcodeDebuggerSupport.dylib (file not found)“ message is shown in the gdb console window. You can use the 'po' command in gdb console to get around the issue.
