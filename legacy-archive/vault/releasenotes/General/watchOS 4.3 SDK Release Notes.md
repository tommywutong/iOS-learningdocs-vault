---
title: watchOS 4.3 SDK Release Notes
apple_id: TP40017701
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-watchOS-4.3/index.html
archived_at: '2026-07-18T02:54:43.467284Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# watchOS 4.3 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombrfvbuqmjnknltg)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombrfvbuqmjnknlti)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombrfvbuqmjnknltk)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombrfvbuqmjnknltenzy)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombrfvbuqmjnknltc)

### Introduction

watchOS 4.3 SDK provides support for developing watchOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for watchOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for Apple Watch running watchOS 4.3. You can also test your apps using the included watchOS Simulator, which supports watchOS 4.3. watchOS 4.3 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

This version of watchOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of watchOS in an unauthorized manner could put your device in an unusable state.

### Tools and Developer Resources

You obtain Xcode 9.3 from the Mac App Store. It is a free download that installs directly into the Applications folder.

The Apple Developer Program provides everything you need to build and distribute your apps on the App Store for iPhone, iPad, Mac, and Apple Watch. Membership includes access to beta OS releases, advanced app capabilities, and tools to develop, test, and distribute apps and Safari extensions. For more information, visit [Apple Developer Program](https://developer.apple.com/programs/).

Apple provides the following resources to support development in watchOS:

- Developer documentation is available both on the [Apple Developer website](https://developer.apple.com/documentation) and from Xcode by choosing Help > Developer Documentation.
- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer website](https://developer.apple.com/). Get the latest development information.
- [watchOS homepage](https://developer.apple.com/watchOS/). Get high-level information about the latest release of Xcode. Download current and beta Xcode releases.
- For help with using Xcode, Simulator, or Instruments, choose Help > _app name_ Help.

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombrfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, on iPhone open Apple Watch and navigate to My Watch > General > About. The version number is next to Version and looks like _4.3 (15Txxxxx)_.

Additionally, you may discuss these issues and watchOS 4.3 SDK in the Apple Developer Forums at [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome).

### Release Notes Updates

_watchOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _watchOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=watchos-sdk-release-notes](https://developer.apple.com/go/?id=watchos-sdk-release-notes).

_Revision: watchOS430 - WRN1_

### Notes and Known Issues

The following items relate to using watchOS 4.3 SDK to develop code.

### Clock

### Resolved Issues

- The battery complication no longer reports remaining battery percentage in increments of 5. (36558500)

### Weather

### Resolved Issues

- Weather will now report information for Greater China. (37331232)
