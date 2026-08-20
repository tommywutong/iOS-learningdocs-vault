---
title: tvOS SDK Release Notes for tvOS 9.1
apple_id: TP40016641
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-tvOSSDK-9.1/index.html
archived_at: '2026-07-18T02:54:43.362031Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# tvOS SDK Release Notes for tvOS 9.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbrfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Introduction

The tvOS SDK leverages many of the same frameworks and technologies that you’re already familiar using for iOS development. However, please note that all libraries and frameworks used in your tvOS apps must be built for tvOS, including any 3rd-party libraries. Do not link your tvOS app against frameworks or libraries that are not built with tvOS. Attempting to do so will result in a build failure. Furthermore, bitcode is now required for all tvOS apps. All apps and frameworks in the app bundle must include bitcode.

tvOS SDK 9.1 provides support for developing tvOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for tvOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

This version of tvOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of tvOS in an unauthorized manner could put your device in an unusable state.

### Bug Reporting

For issues not mentioned in the Notes and Known Issues section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and tvOS SDK 9.1 in the Apple Developer Forums: [https://forums.developer.apple.com/community/pre-release/tvos-beta](https://forums.developer.apple.com/community/pre-release/tvos-beta).

### Notes and Known Issues

### AVKit

### Known Issue

On tvOS, [AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller) automatically resumes playback when video playback stalls. This behavior prevents clients from programmatically pausing playback, as a programmatic pause will appear to be a stall and playback will immediately resume. A future update to allow application control of the autoresume behavior is planned. In the meantime, please file a bug at [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/) describing your use case in detail.

### Networking

### Notes

- Explicit Congestion Notification (ECN) is now enabled by default on Ethernet and Wi-Fi. This is designed to reduce network delays and reduce packet loss.
- The ability to synthesize NAT64 IPv6 addresses from IPv4 literals was added to `getaddrinfo`.

### On-Demand Resources

### Known Issue

When using the [beginAccessingResourcesWithCompletionHandler:](https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/1614840-beginaccessingresources) method, any resource that has already been downloaded will report a progress of `0.0` even though it is available locally.

### Remote

### Known Issue

If the remote sleeps in Simulator, motion control will no longer work when it wakes back up.

__Workaround:__ Restart the app.

### Setup

### Known Issue

After reading the tvOS Terms and Conditions, press MENU to return to the App Analytics screen. Then press Continue and then Accept to complete setup.

### StoreKit

### Note

StoreKit (that is, In-App Purchase) does not work in Simulator.

### UIKit

### Note

When a scroll view is scrolled due to a focus change, the run loop mode will be set to [UITrackingRunLoopMode](https://developer.apple.com/documentation/foundation/runloop/mode/1622929-tracking). When the scrolling ends, the mode will return to the default mode. This is a change from past behavior: Previously, the run loop mode would not change.
