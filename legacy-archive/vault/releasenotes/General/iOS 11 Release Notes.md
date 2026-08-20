---
title: iOS 11 Release Notes
apple_id: TP40017669
resource_type: Release Note
platform: iOS
topic: null
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-11/index.html
archived_at: '2026-07-18T02:54:41.685766Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS 11 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnrzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnrzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnrzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnrzfvbuqmjnknltenzy)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnrzfvbuqmjnknltc)

### Introduction

iOS 11 SDK provides support for developing iOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS, watchOS, tvOS, and macOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 11. You can also test your apps using the included iOS Simulator, which supports iOS 11. iOS 11 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

### Tools and Developer Resources

You obtain Xcode 9 from the Mac App Store. It is a free download that installs directly into the Applications folder. By default, Xcode downloads developer documentation in the background for offline reading; it also automatically downloads documentation updates. This behavior can be changed after installation using the Downloads preferences pane.

The Apple Developer Program provides access to the App Store, Mac App Store, and Apple TV App Store, additional support and documentation, and signing resources for testing and deployment on Apple TV, Apple Watch, iPad, iPhone, and iPod touch devices. For more information, visit the [Apple Developer Program website](https://developer.apple.com/programs/).

Apple provides the following web resources to support development in iOS:

- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer](https://developer.apple.com/) website. Get the latest development in formation as well as technical documentation for Xcode.
- [iOS homepage](https://developer.apple.com/ios/). Get high-level information about the latest release of iOS. Download current and beta iOS releases.
- For help with using Xcode, choose Help > Xcode Help.

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnrzfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, open Settings > General > About. The version number is shown next to Version and looks like _11.0 (15Axxx)_.

Additionally, you may discuss these issues and iOS 11 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome). To get more information about iCloud for Developers, go to [https://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Release Notes Updates

_iOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _iOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=ios-sdk-release-notes](https://developer.apple.com/go/?id=ios-sdk-release-notes).

_Revision: iOS1100 - IRN1_

### Notes and Known Issues

The following items relate to using iOS 11 SDK to develop code.

### 32-bit Apps

### Deprecations

- 32-bit apps no longer run on iOS 11.

  To include a 32-bit slice in your app, target iOS 10 or earlier.

### App Store

### Known Issues

- Restoring from an iTunes backup containing an offloaded app which is also present in the iTunes library installs the offloaded app and then re-installs it from the App Store. This can result in the restored backup taking more space on your device than the size of the backup. (31461664)

  _Workaround_: After the restore completes, offload the app.

### Apple ID

### Known Issues

- Some accounts using a phone number as the Apple ID may be unable to add certain payment types. (31677442)

### ARKit

### Known Issues

- Continuing from a breakpoint while debugging an `ARSession` may result in VIO breaking. Any visual objects placed in the world/anchor are not visible. (31561202)

### AVFoundation

### Known Issues

- Still capture requests fail and the video stream stops producing a buffer when using the `720p30` video format with the `depthDataDeliveryEnabled` property of `AVCapturePhotoSettings` set to `true`. (32060882)
- Depth values in the non default `160x120` and `160x90` depth data formats are half of the expected values, and disparity values are twice the expected value. (32363942)

### CloudKit

### Known Issues

- CloudKit doesn't support `unsigned long long` values with the high-order bit set. (30567424)
- Applications that use `CKModifyRecordsOperation` should specify an appropriate value for `CKModifyRecordsOperation.isAtomic`. If your client is compiled against iOS 11, operations enqueued against the default `CKRecordZone` have new behavior because `atomic` is `true` by default. If the operation hits a "preflight" failure (most commonly, a network issue uploading a `CKAsset`, or a malformed `CKRecord`), the entire operation is canceled. (30838858)

### EventKit

### Known Issues

- Storing data to a non default event store in EventKit may not work. (31335830)

### Files App (Simulator)

### Known Issues

- In Simulator, documents saved in Local Storage won't load again through the Document Browser. (32947101)

### Foundation

### Known Issues

- Clients of `NSURLSessionStreamTask` that use a non-secure connection fail to connect when an error occurs during PAC file evaluation and the system is configured for either Web Proxy Auto Discovery (WPAD) or Proxy Automatic Configuration (PAC). A PAC evaluation failure can occur when the PAC file contains invalid JavaScript or the HTTP host serving the PAC file is unreachable. (33609198)

  _Workaround_: Use `startSecureConnection` to establish a secure connection.
- In iOS 11, `NSURLSession` and `NSURLConnection` may not to load URLs if the system is configured with certain PAC files. PAC files are JavaScript files that specify the HTTP proxies used for accessing the Internet, and are configured in Settings > Wi-Fi. (32883776)

  _Workaround_: In Settings > Wi-Fi, tap the Info button for the desired network and turn off “HTTP Proxy: Configure Proxy”.

### Media

### Deprecations

- `requestPersonalizationTokenForClientToken` is deprecated in iOS 11. Use `getUserTokenFromDeveloperToken` instead. (32065560)

### Vision

### Known Issues

- `VNFaceLandmarkRegion2D` is currently unavailable in Swift. (33191123)
- Facial landmarks identified by the Vision framework may flicker in temporal use cases such as video. (32406440)

### Xcode

### Known Issues

- Debugging a disabled Messages extension may cause the Messages app to crash. (33657938)

  _Workaround_: Enable the extension before starting the debug session.
- After a simulated iOS device starts up, it’s not possible to pull down the Notification center. (33274699)

  _Workaround_: Lock and unlock the simulated device and then reopen Home screen.
