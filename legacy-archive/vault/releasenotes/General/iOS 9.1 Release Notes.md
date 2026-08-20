---
title: iOS 9.1 Release Notes
apple_id: TP40016570
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-9.1/index.html
archived_at: '2026-07-18T02:54:42.493082Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 9.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknzqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknzqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknzqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Introduction

iOS SDK 9.1 provides support for developing iOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 9. You can also test your apps using the included Simulator, which supports iOS 9. iOS SDK 9.1 requires a Mac computer running OS X v10.10.3 (Yosemite) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in the Notes and Known Issues section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/ios/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 9.1 in the Apple Developer Forums: [https://forums.developer.apple.com/community/pre-release/ios-9-beta](https://forums.developer.apple.com/community/pre-release/ios-9-beta). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

### iCloud Keychain

### Known Issue

Sometimes while setting up iCloud Keychain, you receive a "Could Not Set Up iCloud Keychain" error.

__Workaround:__ Reboot the device.

### PhotoKit

### Known Issue

If your app gets the gesture recognizer from the [PHLivePhotoView](https://developer.apple.com/documentation/photokit/phlivephotoview) object (via [playbackGestureRecognizer](https://developer.apple.com/documentation/photokit/phlivephotoview/1623426-playbackgesturerecognizer)) to install it on a different view, subsequently setting a new value for [livePhoto](https://developer.apple.com/documentation/photokit/phlivephotoview/1623424-livephoto) on the `PHLivePhotoView` object causes it to reinstall the gesture recognizer on itself.

__Workaround:__ Your app can get the gesture recognizer and reinstall it on the appropriate view every time after setting a value for [livePhoto](https://developer.apple.com/documentation/photokit/phlivephotoview/1623424-livephoto).

### Restore

### Known Issue

Sometimes while restoring from iCloud backup, you will not see your list of backups, if you have two-factor authentication enabled on your iCloud account.

### UIKit

### Note

On 3D Touch capable devices, touch pressure changes cause [touchesMoved:withEvent:](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1619996-touchesmoved) to be called for all apps running on iOS 9.0. When running iOS 9.1, the method is called only for apps linked with the iOS 9.0 (or later) SDK.

Apps should be prepared to receive touch move events with no change in the x/y coordinates.
