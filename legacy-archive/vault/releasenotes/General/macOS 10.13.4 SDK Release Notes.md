---
title: macOS 10.13.4 SDK Release Notes
apple_id: TP40017702
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-macOS-10.13.4/index.html
archived_at: '2026-07-18T02:54:42.914046Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# macOS 10.13.4 High Sierra SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombsfvbuqmjnknltg)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombsfvbuqmjnknlti)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombsfvbuqmjnknltk)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombsfvbuqmjnknltenzy)
- [System Requirements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombsfvbuqmjnknltm)
- [New 64-bit testing mode](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombsfvbuqmjnknltc)

### Introduction

macOS 10.13.4 SDK provides support for developing macOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS, watchOS, tvOS, and macOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for MacBook, MacBook Air, MacBook Pro, iMac, iMac Pro, Mac Pro, and Mac Mini running macOS High Sierra 10.13.4.

### Tools and Developer Resources

You obtain Xcode 9.3 from the Mac App Store. It is a free download that installs directly into the Applications folder.

The Apple Developer Program provides everything you need to build and distribute your apps on the App Store for iPhone, iPad, Mac, and Apple Watch. Membership includes access to beta OS releases, advanced app capabilities, and tools to develop, test, and distribute apps and Safari extensions. For more information, visit [Apple Developer Program](https://developer.apple.com/programs/).

Apple provides the following resources to support development in macOS:

- Developer documentation is available both on the [Apple Developer website](https://developer.apple.com/documentation) and from Xcode by choosing Help > Developer Documentation.
- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer website](https://developer.apple.com/). Get the latest development information.
- [macOS homepage](https://developer.apple.com/macos/). Get high-level information about the latest release of Xcode. Download current and beta Xcode releases.
- For help with using Xcode, Simulator, or Instruments, choose Help > _app name_ Help.

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tombsfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, choose About this Mac from the Apple Menu, then click on the version number in the window that appears to show the full version number including the part in parenthesis. The full version number looks like _10.13.4 (17Exxx)_.

Additionally, you may discuss these issues and macOS 10.13.4 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome). To get more information about iCloud for Developers, go to [https://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Release Notes Updates

_macOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _macOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=macos-sdk-release-notes](https://developer.apple.com/go/?id=macos-sdk-release-notes).

_Revision: macOS10134 - MRN1_

### System Requirements

macOS 10.13.4 SDK supports the following Macs:

- MacBook or iMac: Late 2009 or newer
- MacBook Air, MacBook Pro, Mac mini, or Mac Pro: 2010 or newer

### New 64-bit testing mode

Developers can use a new 64-bit testing mode in macOS 10.13.4 to test software for 64-bit compatibility.

> [!NOTE]
> 

To enable the 64-bit testing mode:

1. Boot to Recovery OS by restarting your machine and holding down the Command and R keys at startup.
2. Launch Terminal
3. Execute the following command: `nvram boot-args="-no32exec"`
4. Restart the machine

The 64-bit testing mode prevents 32-bit processes from launching. Launching an app that depends on 32-bit software results in a notification that the application can't be opened. Other types of software may fail silently, such as 32-bit versions of Dashboard and WebKit plugins, preference panes, and background processes.

Disable the test mode once the software is updated to work in 64-bit.

To disable the 64-bit testing mode:

1. Boot to Recovery OS by restarting your machine and holding down the Command and R keys at startup.
2. Launch Terminal
3. Execute the following command: `nvram boot-args=""`
4. Restart the machine

In future releases, the 64-bit testing mode may provide additional information for the developer to help test and qualify software.

### Notes and Known Issues

The following items relate to using macOS SDK to develop code.

### General

### Resolved Issues

- Fixed an issue that may result in system shutdown during installation of macOS 10.13.4. (36843839)
- Dragging URLs from the address bar in Safari to Finder now works correctly. (36895105)
- Fixed an issue that resulted in Safari stalling during video streaming. (37019360)
- Fixed an issue with App Store and iBooks that resulted in a “Cannot Connect to the Store” error. (37033819)
- Fixed an issue that resulted in the App Store not showing the password field during authentication. (37082239)
- macOS Recovery over Wi-Fi is not supported on iMac Pros in macOS 10.13.4 beta 3. (37503394)
- Setting the services order may not work in Network Preferences Pane. (35918049)
- Cities added to Weather widget when not signed into iCloud may disappear. (36520283)
- Mac App Store may exit unexpectedly after agreeing to updated Terms & Conditions. (35495094)
- macOS 10.13.4 cannot be installed over macOS 10.13.3 Supplemental Update build 17D2104.
- Safari may randomly crash. (36904314)

### Known Issues

- Portions of the display may flicker on some devices. (37003292)

### Foundation

### Known Issues

- Clients of [NSURLSessionStreamTask](https://developer.apple.com/documentation/foundation/nsurlsessionstreamtask) that use a non-secure connection fail to connect when an error occurs during PAC file evaluation and the system is configured for either Web Proxy Auto Discovery (WPAD) or Proxy Automatic Configuration (PAC). A PAC evaluation failure can occur when the PAC file contains invalid JavaScript or the HTTP host serving the PAC file is unreachable. (33609198)

  _Workaround_: Use [startSecureConnection()](https://developer.apple.com/documentation/foundation/urlsessionstreamtask/1411567-startsecureconnection) to establish a secure connection.

### Messages

### Known Issues

- Messages may be unresponsive on launch.
- All conversations may be missing.
- Conversations may be slow to appear.
