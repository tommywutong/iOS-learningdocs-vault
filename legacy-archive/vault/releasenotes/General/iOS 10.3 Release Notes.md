---
title: iOS 10.3 Release Notes
apple_id: TP40017612
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-10.3/index.html
archived_at: '2026-07-18T02:54:41.647573Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 10.3

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmjsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmjsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [File System Conversion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmjsfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmjsfvbuqmjnknltc)

### Introduction

iOS 10.3 SDK provides support for developing iOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and macOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 10.3. You can also test your apps using the included iOS Simulator, which supports iOS 10.3. iOS 10.3 SDK requires a Mac computer running macOS 10.10.3 (Yosemite) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [https://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmjsfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/). Additionally, you may discuss these issues and iOS 10.3 SDK in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome). To get more information about iCloud for Developers, go to [https://developer.apple.com/icloud](https://developer.apple.com/icloud).

### File System Conversion

When you update to iOS 10.3, your iOS device will update its file system to Apple File System (APFS). This conversion preserves existing data on your device. However, as with any software update, it is recommended that you create a backup of your device before updating.

### Notes and Known Issues

The following items relate to using iOS 10.3 SDK to develop code.

### Managed and Shared Devices

The ability to update devices from a remote server is in development and may not yet work as expected.

### openURL

When a third party application invokes [openURL:](https://developer.apple.com/documentation/uikit/uiapplication/1622961-openurl) on a `tel://`, `facetime://`, or `facetime-audio://` URL, iOS displays a prompt and requires user confirmation before dialing.

### SiriKit

The SiriKit car commands are still in development and may not yet work as expected.

### SOS

SOS is only supported in India.

### WebKit

Safari now supports the `prefers-reduced-motion` media query. This query allows a web developer to provide alternate page styles for users who are sensitive to large areas of motion. Users can change their preference for reduced motion in the Accessibility section of System Preferences.

The iOS 10.3 update removes support for SHA-1 signed certificates used for Transport Layer Security (TLS) in Safari and WebKit that are issued from a root Certification Authority (CA) included in the operating system default trust store. All other TLS connections will continue to support SHA-1 signed certificates until late 2017. SHA-1 signed root CA certificates, enterprise-distributed SHA-1 certificates, and user-installed SHA-1 certificates are not affected by this change. For more information, see [https://support.apple.com/kb/HT207459](https://support.apple.com/kb/HT207459).
