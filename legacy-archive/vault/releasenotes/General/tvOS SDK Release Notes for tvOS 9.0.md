---
title: tvOS SDK Release Notes for tvOS 9.0
apple_id: TP40016575
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-tvOSSDK-9.0/index.html
archived_at: '2026-07-18T02:54:43.257729Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# tvOS SDK Release Notes for tvOS 9.0

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknzvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknzvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dknzvfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)

### Introduction

The tvOS SDK leverages many of the same frameworks and technologies that you are already familiar with when developing for iOS. However, please note that all libraries and frameworks that you use in your tvOS apps must be built for tvOS, including any 3rd-party libraries. Do not link your tvOS app against frameworks or libraries that are not built with tvOS. Attempting to do so will result in a build failure. Furthermore, bitcode is now required for all tvOS apps. All apps and frameworks in the app bundle need to include bitcode.

tvOS SDK 9.0 provides support for developing tvOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for tvOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

This version of tvOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of tvOS in an unauthorized manner could put your device in an unusable state.

### Bug Reporting

For issues not mentioned in the Notes and Known Issues section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and tvOS SDK 9.0 in the Apple Developer Forums: [https://forums.developer.apple.com/community/pre-release/tvos-beta](https://forums.developer.apple.com/community/pre-release/tvos-beta).

### Notes and Known Issues

### Metal

### Note

For tvOS Metal development, it is now required that tvOS specific feature set enum is used. Specifically: `MTLFeatureSet_TVOS_GPUFamily1_v1`.

### Parallax Images

### Note

- Please regenerate any LCR images from source material using the latest SDK. There have been several improvements to performance, size, and accuracy of LCR images.

### Remote

### Known Issue

- In the Simulator, if the remote sleeps, when it wakes back up motion control will no longer work.

  __Workaround:__ Restart the app.

### On Demand Resources

### Known Issues

- When using the beginAccessingResourcesWithCompletionHandler: method, any resource that has already downloaded will report a progress of 0.0 even though it is available locally.
- Initial On Demand Resource asset packs are not currently downloaded during install-time. They can be fetched at first runtime.

### Setup

### Note

- Tap To Setup requires iOS 9.1 or later.

### StoreKit

### Note

- StoreKit (In-App purchases) do not work in the Simulator.
