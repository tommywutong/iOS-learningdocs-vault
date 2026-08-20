---
title: tvOS Release Notes
apple_id: TP40017671
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2017-09-20'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-tvOSSDK-11/index.html
archived_at: '2026-07-18T02:54:43.212465Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# tvOS 11 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzrfvbuqmjnknltenzy)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzrfvbuqmjnknltc)

### Introduction

tvOS SDK leverages many of the same frameworks and technologies that you’re already using for iOS development. However, please note that all libraries and frameworks used in your tvOS apps must be built for tvOS, including any 3rd-party libraries. Do not link your tvOS app against frameworks or libraries that are not built with tvOS. Attempting to do so will result in a build failure. Furthermore, bitcode is required for all tvOS apps. All apps and frameworks in the app bundle must include bitcode.

tvOS 11 SDK provides support for developing tvOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for tvOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for Apple TV running tvOS 11. You can also test your apps using the included tvOS Simulator, which supports tvOS 11. tvOS 11 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

This version of tvOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of tvOS in an unauthorized manner could put your device in an unusable state.

### Tools and Developer Resources

You obtain Xcode 9 from the Mac App Store. It is a free download that installs directly into the Applications folder. By default, Xcode downloads developer documentation in the background for offline reading; it also automatically downloads documentation updates. This behavior can be changed after installation using the Downloads preferences pane.

The Apple Developer Program provides access to the App Store, Mac App Store, and Apple TV App Store, additional support and documentation, and signing resources for testing and deployment on Apple TV, Apple Watch, iPad, iPhone, and iPod touch devices. For more information, visit the [Apple Developer Program website](https://developer.apple.com/programs/).

Apple provides the following web resources to support development in iOS:

- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer](https://developer.apple.com/) website. Get the latest development in formation as well as technical documentation for Xcode.
- [tvOS homepage](https://developer.apple.com/tvos/). Get high-level information about the latest release of Xcode. Download current and beta Xcode releases.
- For help with using Xcode, choose Help > Xcode Help.

### Bug Reporting

For issues not mentioned in the Notes and Known Issues section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/](https://developer.apple.com/bugreporter/)).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, open Settings > General > About. The version number is shown next to Version and looks like _11.0 (15Jxxxxx)_.

Additionally, you may discuss these issues and tvOS 11 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/](https://forums.developer.apple.com/).

### Release Notes Updates

_tvOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _tvOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=tvos-sdk-release-notes](https://developer.apple.com/go/?id=tvos-sdk-release-notes).

_Revision: tvOS1100 - TRN1_

### Notes and Known Issues

The following items relate to using tvOS 11 SDK to develop code.

### CloudKit

### Known Issues

- CloudKit doesn't support `unsigned long long` values with the high-order bit set. (30567424)
- Applications that use `CKModifyRecordsOperation` should specify an appropriate value for `CKModifyRecordsOperation.isAtomic`. If your client is compiled against tvOS 11, operations enqueued against the default `CKRecordZone` have new behavior because `atomic` is `true` by default. If the operation hits a "preflight" failure (most commonly, a network issue uploading a `CKAsset`, or a malformed `CKRecord`), the entire operation is canceled. (30838858)

### Foundation

### Known Issues

- Clients of `NSURLSessionStreamTask` that use a non-secure connection fail to connect when an error occurs during PAC file evaluation and the system is configured for either Web Proxy Auto Discovery (WPAD) or Proxy Automatic Configuration (PAC). A PAC evaluation failure can occur when the PAC file contains invalid JavaScript or the HTTP host serving the PAC file is unreachable. (33609198)

  _Workaround_: Use `startSecureConnection` to establish a secure connection.

### Vision

### Known Issues

- `VNFaceLandmarkRegion2D` is currently unavailable in Swift. (33191123)
