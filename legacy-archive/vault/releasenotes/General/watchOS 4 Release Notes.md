---
title: watchOS 4 Release Notes
apple_id: TP40017670
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-watchOS-4/index.html
archived_at: '2026-07-18T02:54:43.517481Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# watchOS 4 SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzqfvbuqmjnknltenzy)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzqfvbuqmjnknltc)

### Introduction

watchOS 4 SDK provides support for developing watchOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for watchOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for Apple Watch running watchOS 4. You can also test your apps using the included watchOS Simulator, which supports watchOS 4. watchOS 4 SDK requires a Mac computer running macOS Sierra 10.12.6 or later.

This version of watchOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of watchOS in an unauthorized manner could put your device in an unusable state.

### Tools and Developer Resources

You obtain Xcode 9 from the Mac App Store. It is a free download that installs directly into the Applications folder. By default, Xcode downloads developer documentation in the background for offline reading; it also automatically downloads documentation updates. This behavior can be changed after installation using the Downloads preferences pane.

The Apple Developer Program provides access to the App Store, Mac App Store, and Apple TV App Store, additional support and documentation, and signing resources for testing and deployment on Apple TV, Apple Watch, iPad, iPhone, and iPod touch devices. For more information, visit the [Apple Developer Program website](https://developer.apple.com/programs/).

Apple provides the following web resources to support development in watchOS:

- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer](https://developer.apple.com/) website. Get the latest development in formation as well as technical documentation for Xcode.
- [watchOS homepage](https://developer.apple.com/watchOS/). Get high-level information about the latest release of Xcode. Download current and beta Xcode releases.
- For help with using Xcode, choose Help > Xcode Help.

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzqfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, on iPhone open Apple Watch and navigate to My Watch > General > About. The version number is next to Version and looks like _4.0 (15Rxxxxx)_.

Additionally, you may discuss these issues and watchOS 4 SDK in the Apple Developer Forums at [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome).

### Release Notes Updates

_watchOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _watchOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=watchos-sdk-release-notes](https://developer.apple.com/go/?id=watchos-sdk-release-notes).

_Revision: watchOS400 - WRN1_

### Notes and Known Issues

The following items relate to using watchOS 4 SDK to develop code.

### CloudKit

### Known Issues

- CloudKit doesn't support `unsigned long long` values with the high-order bit set. (30567424)
- Applications that use `CKModifyRecordsOperation` should specify an appropriate value for `CKModifyRecordsOperation.isAtomic`. If your client is compiled against watchOS 4, operations enqueued against the default `CKRecordZone` have new behavior because `atomic` is `true` by default. If the operation hits a "preflight" failure (most commonly, a network issue uploading a `CKAsset`, or a malformed `CKRecord`), the entire operation is canceled. (30838858)

### CoreBluetooth

### Known Issues

- CoreBluetooth is not supported on original Apple Watch or Apple Watch Series 1. (34049299)

### HealthKit

### Known Issues

- To track location in the background while a user is in a workout session, add `UIBackgroundModes/location` in the `Info.plist` file. (29483437)

### WatchKit

### Known Issues

- Automatic display of attachments in default WatchKit Notification interfaces do not work. (31589086)

### Xcode

### Known Issues

- Crashlogs may take a few minutes to sync and be visible in Xcode. (31156191)
