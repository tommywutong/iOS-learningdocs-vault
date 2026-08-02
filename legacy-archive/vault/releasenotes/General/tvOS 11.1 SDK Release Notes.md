---
title: tvOS 11.1 SDK Release Notes
apple_id: TP40017684
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-tvOS-11.1/index.html
archived_at: '2026-07-18T02:54:42.988942Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# tvOS 11.1 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobufvbuqmjnknltg)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobufvbuqmjnknlti)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobufvbuqmjnknltk)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobufvbuqmjnknltenzy)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobufvbuqmjnknltc)

### Introduction

tvOS SDK leverages many of the same frameworks and technologies that you’re already using for iOS development. However, please note that all libraries and frameworks used in your tvOS apps must be built for tvOS, including any 3rd-party libraries. Do not link your tvOS app against frameworks or libraries that are not built with tvOS. Attempting to do so will result in a build failure. Furthermore, bitcode is required for all tvOS apps. All apps and frameworks in the app bundle must include bitcode.

tvOS 11.1 SDK provides support for developing tvOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for tvOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for Apple TV running tvOS 11.1. You can also test your apps using the included tvOS Simulator, which supports tvOS 11.1. tvOS 11.1 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

This version of tvOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of tvOS in an unauthorized manner could put your device in an unusable state.

### Tools and Developer Resources

You obtain Xcode 9.1 from the Mac App Store. It is a free download that installs directly into the Applications folder.

The Apple Developer Program provides everything you need to build and distribute your apps on the App Store for iPhone, iPad, Mac, and Apple Watch. Membership includes access to beta OS releases, advanced app capabilities, and tools to develop, test, and distribute apps and Safari extensions. For more information, visit [Apple Developer Program](https://developer.apple.com/programs/).

Apple provides the following resources to support development in tvOS:

- Developer documentation is available both on the [Apple Developer website](https://developer.apple.com/documentation) and from Xcode by choosing Help > Developer Documentation.
- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer website](https://developer.apple.com/). Get the latest development information.
- [tvOS homepage](https://developer.apple.com/tvos/). Get high-level information about the latest release of Xcode. Download current and beta Xcode releases.
- For help with using Xcode, Simulator, or Instruments, choose Help > _app name_ Help.

### Bug Reporting

For issues not mentioned in the [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmobufvbuqmjnknlti) section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/](https://developer.apple.com/bugreporter/)).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, open Settings > General > About. The version number is shown next to Version and looks like _11.1 (15Jxxxxx)_.

Additionally, you may discuss these issues and tvOS 11.1 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/](https://forums.developer.apple.com/).

### Release Notes Updates

_tvOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _tvOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=tvos-sdk-release-notes](https://developer.apple.com/go/?id=tvos-sdk-release-notes).

_Revision: tvOS1110 - TRN1_

### Notes and Known Issues

The following items relate to using tvOS 11.1 SDK to develop code.

### Foundation

### Known Issues

- Clients of [NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask) that use a non-secure connection fail to connect when an error occurs during PAC file evaluation and the system is configured for either Web Proxy Auto Discovery (WPAD) or Proxy Automatic Configuration (PAC). A PAC evaluation failure can occur when the PAC file contains invalid JavaScript or the HTTP host serving the PAC file is unreachable. (33609198)

  _Workaround_: Use [startSecureConnection()](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411567-startsecureconnection) to establish a secure connection.

### Vision

### Known Issues

- `VNFaceLandmarkRegion2D` is currently unavailable in Swift. (33191123)
