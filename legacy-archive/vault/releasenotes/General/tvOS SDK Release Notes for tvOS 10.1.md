---
title: tvOS SDK Release Notes for tvOS 10.1
apple_id: TP40017586
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-tvOSSDK-10.1/index.html
archived_at: '2026-07-18T02:54:43.155174Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# tvOS SDK Release Notes for tvOS 10.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [About tvOS 10.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Autosubmission of Diagnostic and Usage Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobwfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6ni)

### Introduction

The tvOS SDK leverages many of the same frameworks and technologies that you’re already using for iOS development. However, please note that all libraries and frameworks used in your tvOS apps must be built for tvOS, including any 3rd-party libraries. Do not link your tvOS app against frameworks or libraries that are not built with tvOS. Attempting to do so will result in a build failure. Furthermore, bitcode is required for all tvOS apps. All apps and frameworks in the app bundle must include bitcode.

tvOS 10.1 SDK provides support for developing tvOS apps. It’s packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for tvOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

This version of tvOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of tvOS in an unauthorized manner could put your device in an unusable state.

### About tvOS 10.1

tvOS 10.1 includes general bug fixes and improvements in the OS and SDK.

### Bug Reporting

For issues not mentioned in the Notes and Known Issues section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and tvOS SDK 10.1 in the Apple Developer Forums: [https://forums.developer.apple.com/](https://forums.developer.apple.com/).

### Autosubmission of Diagnostic and Usage Data

By default, tvOS 10.1 automatically sends anonymous diagnostic and usage data back to Apple. This includes information about crashes, freezes, kernel panics, and information about how you use Apple and third-party software, hardware, and services. This information is used to help Apple improve the quality and performance of its products and services. You can stop autosubmission of diagnostics and usage data by going to Settings > Privacy > Diagnostics and Usage > Don’t Send.

### Notes and Known Issues

### Top Shelf App Extension

tvOS apps with a deployment target of tvOS 10.0 or greater that use a Top Shelf extension will now require a “Top Shelf Image Wide” (2320x720) image in the asset catalog when submitting to the App Store.

tvOS apps with a deployment target of tvOS 9.0 or greater that use a Top Shelf extension now require both a "Top Shelf Image Wide” (2320x720) and "Top Shelf Image” (1920x720) image in the asset catalog when submitting to the App Store.

### TVMLKit

For layered images retrieved from a content server at runtime, only the `.lcr` image format is supported; `.lsr` images are not supported.

For more information, please refer to the “Runtime Layered Images” section at [https://developer.apple.com/tvos/human-interface-guidelines/icons-and-images](https://developer.apple.com/tvos/human-interface-guidelines/icons-and-images).
