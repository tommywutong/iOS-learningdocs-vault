---
title: iOS 9.3 Release Notes
apple_id: TP40016779
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-05-24'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-9.3/index.html
archived_at: '2026-07-18T02:54:42.567205Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 9.3

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3donzzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3donzzfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3donzzfvbuqmjnknltc)

### Introduction

iOS SDK 9.3 provides support for developing iOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 9. You can also test your apps using the included Simulator, which supports iOS 9. iOS SDK 9.3 requires a Mac computer running OS X v10.10.3 (Yosemite) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3donzzfvbuqmjnknltc) section, please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/). Additionally, you may discuss these issues and iOS SDK 9.3 in the Apple Developer Forums: [https://forums.developer.apple.com/community](https://forums.developer.apple.com/community/pre-release/ios-9-beta). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

### App Store

### Known Issue

Users who performed an iCloud or iTunes restore onto a device with iOS 9.3 beta 3 from a backup created with iOS 9.3 beta 1 or 2 may be unable to install apps or log into iCloud when upgrading to iOS 9.3 beta 5.

__Workaround:__ Perform an erase-install of iOS 9.3 beta 5 and restore data from either the iCloud or iTunes backup.

### Apple ID

### Known Issues

- When using a Shared iPad, the device may hang for a few minutes at logout.
- If you reboot your Access Point and a Shared iPad cannot reconnect to your network, you also need to reboot your Shared iPad.

### Apple Watch

### Known Issue

Certain features in the Apple Watch app require the developer seed of watchOS 2.2.

### Dictionary

### Known Issue

A user updating to an iOS 9 GM build from a seed build may see duplicate dictionaries in the definition dictionary list if the user switched primary language, added secondary languages, or added new keyboards.

__Workaround:__ To remove the duplicate dictionaries, go to the definition dictionary list, swipe the dictionary, and tap the Delete button.

### Simulator

### Known Issue

Photos app in Simulator does not sync photos from iCloud Photo Library.

### Wi-Fi

### Known Issue

In a classroom environment with many iPad devices connected to a single access point, some devices may intermittently lose data connectivity with Classroom, other devices, and the Internet, even though the status bar shows that the device is connected to a Wi-Fi access point.

__Workaround:__ Disable and then reenable Wi-Fi from Settings > Wi-Fi to resume connectivity. Note that for a Shared iPad, you may need to reboot the affected device.
