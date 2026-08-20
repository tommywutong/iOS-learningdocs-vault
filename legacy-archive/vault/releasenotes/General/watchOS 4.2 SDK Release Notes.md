---
title: watchOS 4.2 SDK Release Notes
apple_id: TP40017697
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2017-12-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-watchOS-4.2/index.html
archived_at: '2026-07-18T02:54:43.437568Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# watchOS 4.2 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojxfvbuqmjnknltg)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojxfvbuqmjnknlti)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojxfvbuqmjnknltk)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojxfvbuqmjnknltenzy)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojxfvbuqmjnknltc)

### Introduction

watchOS 4.2 SDK provides support for developing watchOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for watchOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for Apple Watch running watchOS 4.2. You can also test your apps using the included watchOS Simulator, which supports watchOS 4.2. watchOS 4.2 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

This version of watchOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of watchOS in an unauthorized manner could put your device in an unusable state.

### Tools and Developer Resources

You obtain Xcode 9.2 from the Mac App Store. It is a free download that installs directly into the Applications folder.

The Apple Developer Program provides everything you need to build and distribute your apps on the App Store for iPhone, iPad, Mac, and Apple Watch. Membership includes access to beta OS releases, advanced app capabilities, and tools to develop, test, and distribute apps and Safari extensions. For more information, visit [Apple Developer Program](https://developer.apple.com/programs/).

Apple provides the following resources to support development in watchOS:

- Developer documentation is available both on the [Apple Developer website](https://developer.apple.com/documentation) and from Xcode by choosing Help > Developer Documentation.
- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer website](https://developer.apple.com/). Get the latest development information.
- [watchOS homepage](https://developer.apple.com/watchOS/). Get high-level information about the latest release of Xcode. Download current and beta Xcode releases.
- For help with using Xcode, Simulator, or Instruments, choose Help > _app name_ Help.

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmojxfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, on iPhone open Apple Watch and navigate to My Watch > General > About. The version number is next to Version and looks like _4.2 (15Sxxxxx)_.

Additionally, you may discuss these issues and watchOS 4.2 SDK in the Apple Developer Forums at [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome).

### Release Notes Updates

_watchOS Release Notes_ is sometimes updated after a release is distributed. Please check this document for updates.

_Revision: watchOS420 - WRN1_

### Notes and Known Issues

The following items relate to using watchOS 4.2 SDK to develop code.

### CoreBluetooth

### Notes

- CoreBluetooth is not supported on original Apple Watch or Apple Watch Series 1. (34049299)
