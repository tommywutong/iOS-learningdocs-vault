---
title: tvOS 11.3 SDK Release Notes
apple_id: TP40017700
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-tvOS-11.3/index.html
archived_at: '2026-07-18T02:54:43.075591Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# tvOS 11.3 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombqfvbuqmjnknltg)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombqfvbuqmjnknlti)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombqfvbuqmjnknltk)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombqfvbuqmjnknltenzy)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombqfvbuqmjnknltc)

### Introduction

tvOS SDK leverages many of the same frameworks and technologies that you’re already using for iOS development. However, please note that all libraries and frameworks used in your tvOS apps must be built for tvOS, including any 3rd-party libraries. Do not link your tvOS app against frameworks or libraries that are not built with tvOS. Attempting to do so will result in a build failure. Furthermore, bitcode is required for all tvOS apps. All apps and frameworks in the app bundle must include bitcode.

tvOS 11.3 SDK provides support for developing tvOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for tvOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for Apple TV running tvOS 11.3. You can also test your apps using the included tvOS Simulator, which supports tvOS 11.3. tvOS 11.3 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

This version of tvOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of tvOS in an unauthorized manner could put your device in an unusable state.

### Tools and Developer Resources

You obtain Xcode 9.3 from the Mac App Store. It is a free download that installs directly into the Applications folder.

The Apple Developer Program provides everything you need to build and distribute your apps on the App Store for iPhone, iPad, Mac, and Apple Watch. Membership includes access to beta OS releases, advanced app capabilities, and tools to develop, test, and distribute apps and Safari extensions. For more information, visit [Apple Developer Program](https://developer.apple.com/programs/).

Apple provides the following resources to support development in tvOS:

- Developer documentation is available both on the [Apple Developer website](https://developer.apple.com/documentation) and from Xcode by choosing Help > Developer Documentation.
- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer website](https://developer.apple.com/). Get the latest development information.
- [tvOS homepage](https://developer.apple.com/tvos/). Get high-level information about the latest release of Xcode. Download current and beta Xcode releases.
- For help with using Xcode, Simulator, or Instruments, choose Help > _app name_ Help.

### Bug Reporting

For issues not mentioned in the [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombqfvbuqmjnknlti) section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/](https://developer.apple.com/bugreporter/)).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, open Settings > General > About. The version number is shown next to Version and looks like _11.3 (15Lxxxxx)_.

Additionally, you may discuss these issues and tvOS 11.3 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/](https://forums.developer.apple.com/).

### Release Notes Updates

_tvOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _tvOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=tvos-sdk-release-notes](https://developer.apple.com/go/?id=tvos-sdk-release-notes).

_Revision: tvOS1130 - TRN1_

### Notes and Known Issues

The following items relate to using tvOS 11.3 SDK to develop code.

### General

### Resolved Issues

- The TV Provider sign-in prompt is now shown on initial tvOS setup screens. (36559610)
- Backgrounding an app that was launched with a restrictions PIN code no longer causes Home Screen instability. (36845891)

### Foundation

### Known Issues

- Clients of [NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask) that use a non-secure connection fail to connect when an error occurs during PAC file evaluation and the system is configured for either Web Proxy Auto Discovery (WPAD) or Proxy Automatic Configuration (PAC). A PAC evaluation failure can occur when the PAC file contains invalid JavaScript or the HTTP host serving the PAC file is unreachable. (33609198)

  _Workaround_: Use [startSecureConnection()](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411567-startsecureconnection) to establish a secure connection.

### Mobile Device Management

### New Features

- Added the following settings to device management. For more information, see the [Configuration Profile Reference](https://developer.apple.com/library/content/featuredarticles/iPhoneConfigurationProfileRef/Introduction/Introduction.html) and [MDM Protocol Reference](https://developer.apple.com/library/content/documentation/Miscellaneous/Reference/MobileDeviceManagementProtocolRef/1-Introduction/Introduction.html#//apple_ref/doc/uid/TP40017387-CH1-SW1):

  - Restrict explicit music and bookstore erotica by rating.
  - Restrict apps, movies and TV shows by rating.
  - Skip the Privacy screen during setup.
  - Restrict Remote app connections to specified iOS devices.
  - Update an app while in Single App Mode.

### Resolved Issues

- Skipping all setup screens now works correctly when using an MDM server configuration with Device Enrollment Program supervised devices. (35919886)
- Upgrading a supervised device no longer requires a remote to complete the upgrade. (36674710)

### Mode Switching

### New Features

- Added support for automatic frame rate to AVKit for Apple TV (4th generation). Apps that don’t use AVKit for video playback can add support using APIs previously introduced in the tvOS 11.2 SDK. For more information, see: [https://developer.apple.com/fall17/503](https://developer.apple.com/fall17/503).

### Resolved Issues

- Application UI now successfully resumes the system default frame rate or dynamic range when suspending a video player. (37094440)

### On-Demand Resources

### Resolved Issues

- Conditionally pinned on-demand resource loading (using `conditionallyBeginAccessingResourcesWithCompletionHandler`) now works correctly when upgrading to tvOS 11.3 (36836402)
- On-demand resources now work correctly in the tvOS simulator. (36554589)
- Resources embedded directly in asset packs in the product bundle are now loaded properly. (37089083)

### TVMLKit / Web Inspector

### New Features

- Enhanced the prototype element to provide different structure through the use of queries and enhanced binding support to bind the children of a node.
- Added viewing of local and remote image resources for XHR requests to the Network tab of Safari Web Inspector.
- Clicking on the Start Element Selection button of Safari Web Inspector now opens the Elements tab to the focussed view of a TVMLKit app.

### Resolved Issues

- `oneupTemplate` now renders full screen images. (37045770)
