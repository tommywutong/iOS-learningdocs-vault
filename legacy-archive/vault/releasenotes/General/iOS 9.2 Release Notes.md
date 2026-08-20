---
title: iOS 9.2 Release Notes
apple_id: TP40016638
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-9.2/index.html
archived_at: '2026-07-18T02:54:42.524842Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 9.2

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmmzyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmmzyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmmzyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Introduction

iOS SDK 9.2 provides support for developing iOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for iOS and OS X. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

With this software you can develop apps for iPhone, iPad, or iPod touch running iOS 9. You can also test your apps using the included Simulator, which supports iOS 9. iOS SDK 9.2 requires a Mac computer running OS X v10.10.3 (Yosemite) or later.

This version of iOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of iOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/).

### Bug Reporting

For issues not mentioned in the Notes and Known Issues section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/ios/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and iOS SDK 9.2 in the Apple Developer Forums: [https://forums.developer.apple.com/community](https://forums.developer.apple.com/community/pre-release/ios-9-beta). To get more information about iCloud for Developers, go to [http://developer.apple.com/icloud](https://developer.apple.com/icloud).

### Notes and Known Issues

### Dictionary

### Known Issue

A user updating to an iOS 9 GM build from a seed build may see duplicate dictionaries in the definition dictionary list if the user switched primary language, added secondary languages, or added new keyboards.

__Workaround:__ To remove the duplicate dictionaries, go to the definition dictionary list, swipe the dictionary, and tap the Delete button.

### Keyboards

### Known Issues

- If using a third-party keyboard as the default keyboard, you will be unable to enter your username and password in a Captive Wi-Fi login page.

  __Workaround:__ Leave the login screen, go to a different app and invoke the Apple system keyboard, then return to the Captive Wi-Fi login screen and use the system keyboard.
- Smiley emoji may not be rendered correctly when input from the Frequently Used category.

  __Workaround:__ Input the emoji from the Smileys & People category or clear your keyboard dictionary in General > Reset > Reset Keyboard Dictionary.

### Networking

### Notes

- Explicit Congestion Notification (ECN) is enabled by default on Wi-Fi and on select carriers. This is designed to reduce network delays and reduce packet loss.
- The ability to synthesize NAT64 IPv6 addresses from IPv4 literals was added to `getaddrinfo`.

### Safari

### Notes

- [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) now supports 3rd party Action extensions. Any Action extension that works in Safari will also work in `SFSafariViewController`.
- Long tapping the Reload button in Safari View Controller now gives options to Reload Without Content Blockers and Request Desktop Site, as it does in Safari.
- Safari View Controller can now be dismissed using an edge swipe. You must rebuild your app against the iOS 9.2 SDK or later to take advantage of this new behavior.

### Known Issue

The content blocker loader XPC service may crash when no content blocker content is provided.

### Wi-Fi Calling on Other Devices

### Known Issue

To prevent improper use of Wi-Fi Calling on Other Devices that belong to other users, do not put your AT&T SIM card in another user’s iPhone.
