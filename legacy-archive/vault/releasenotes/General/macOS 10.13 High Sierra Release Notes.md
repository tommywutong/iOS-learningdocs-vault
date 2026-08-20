---
title: macOS 10.13 High Sierra Release Notes
apple_id: TP40017672
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-macOSSDK-10.13/index.html
archived_at: '2026-07-18T02:54:42.944187Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# macOS 10.13 High Sierra SDK Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Tools and Developer Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Release Notes Updates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzsfvbuqmjnknltenzy)
- [System Requirements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzsfvbuqmjnknltc)

### Introduction

macOS 10.13 SDK provides support for developing macOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS, watchOS, tvOS, and macOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for MacBook, MacBook Air, MacBook Pro, iMac, iMac Pro, Mac Pro, and Mac Mini running macOS High Sierra 10.13.

### Tools and Developer Resources

You obtain Xcode 9 from the Mac App Store. It is a free download that installs directly into the Applications folder. By default, Xcode downloads developer documentation in the background for offline reading; it also automatically downloads documentation updates. This behavior can be changed after installation using the Downloads preferences pane.

The Apple Developer Program provides access to the App Store, Mac App Store, and Apple TV App Store, additional support and documentation, and signing resources for testing and deployment on Apple TV, Apple Watch, iPad, iPhone, and iPod touch devices. For more information, visit the [Apple Developer Program website](https://developer.apple.com/programs/).

Apple provides the following web resources to support development in macOS:

- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer](https://developer.apple.com/) website. Get the latest development in formation as well as technical documentation for Xcode.
- [macOS homepage](https://developer.apple.com/macos/). Get high-level information about the latest release of Xcode. Download current and beta Xcode releases.

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmnzsfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, choose About this Mac from the Apple Menu, then click on the version number in the window that appears to show the full version number including the part in parenthesis. The full version number looks like _10.13 (17Axxx)_.

Additionally, you may discuss these issues and macOS 10.13 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome). To get more information about iCloud for Developers, go to [https://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Release Notes Updates

_macOS Release Notes_ is sometimes updated after a release is distributed. You can check for the most up-to-date version of _macOS Release Notes_ at the Apple Developer website by checking [http://developer.apple.com/go/?id=macos-sdk-release-notes](https://developer.apple.com/go/?id=macos-sdk-release-notes).

_Revision: macOS1013 - MRN1_

### System Requirements

macOS 10.13 SDK supports the following Macs:

- MacBook or iMac: Late 2009 or newer
- MacBook Air, MacBook Pro, Mac mini, or Mac Pro: 2010 or newer
- MacBook (Late 2008 Aluminum, or Early 2009 or newer)
- Mac mini (Early 2009 or newer)
- MacBook Pro (Mid/Late 2007 or newer)
- Mac Pro (Early 2008 or newer)
- Xserve (Early 2009)

### Notes and Known Issues

The following items relate to using macOS SDK to develop code.

### Apple File System (APFS)

### Known Issues

- HDD and Fusion drives can't be converted to APFS. (32360337, 31851687)
- Some third-party applications may not correctly recognize volumes that are formatted using APFS.

### CloudKit

### Known Issues

- CloudKit doesn't support `unsigned long long` values with the high-order bit set. (30567424)
- Applications that use `CKModifyRecordsOperation` should specify an appropriate value for `CKModifyRecordsOperation.isAtomic`. If your client is compiled against macOS 10.13, operations enqueued against the default `CKRecordZone` have new behavior because `atomic` is `true` by default. If the operation hits a "preflight" failure (most commonly, a network issue uploading a `CKAsset`, or a malformed `CKRecord`), the entire operation is canceled. (30838858)

### Foundation

### Known Issues

- Clients of `NSURLSessionStreamTask` that use a non-secure connection fail to connect when an error occurs during PAC file evaluation and the system is configured for either Web Proxy Auto Discovery (WPAD) or Proxy Automatic Configuration (PAC). A PAC evaluation failure can occur when the PAC file contains invalid JavaScript or the HTTP host serving the PAC file is unreachable. (33609198)

  _Workaround_: Use `startSecureConnection` to establish a secure connection.

### HEVC and HEIF Images

### Known Issues

- macOS 10.13 adds HEVC and HEIF decode capability. In order to display HEIF image files or HEVC videos captured on iOS 11, your Mac needs to be updated to macOS 10.13.
- The specific hardware and software requirements for HEVC and HEIF are detailed in the WWDC 2017 presentations covering these new technologies. Depending on the capabilities of your Mac and the needs of your content, AVFoundation may use a software-based HEVC encoder which typically has longer encoding times.

### Kernel Extension Loading

### Known Issues

- Some third-party apps may not fully handle instances where their kernel extension is denied user consent to load.
- Kernel extensions blocked in early boot do not display an alert.

### Localization

### Known Issues

- Some text may not be localized to the selected system language.
- Some languages may have clipped or misaligned layout.

### Touch Bar

### Resolved Issues

- An issue preventing the appearance of volume and brightness sliders on tap and immediate drag on the Control Strip buttons has been fixed. (29465989)

### Vision

### Known Issues

- `VNFaceLandmarkRegion2D` is currently unavailable in Swift. (33191123)
- Facial landmarks identified by the Vision framework may flicker in temporal use cases such as video. (32406440)
