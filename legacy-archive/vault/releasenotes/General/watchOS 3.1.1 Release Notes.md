---
title: watchOS 3.1.1 Release Notes
apple_id: TP40017584
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-watchOSSDK-3.1.1/index.html
archived_at: '2026-07-18T02:54:43.766773Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# watchOS SDK Release Notes for watchOS 3.1.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobufvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobufvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobufvbuqmjnknltc)

### Introduction

watchOS SDK 3.1.1 provides support for developing watchOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for watchOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

This version of watchOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of watchOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [http://developer.apple.com/programs/](https://developer.apple.com/programs/).

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tkobufvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/). Additionally, you may discuss these issues and watchOS SDK 3.1.1 in the Apple Developer Forums at [http://devforums.apple.com](http://devforums.apple.com/).

### Notes and Known Issues

The following items relate to using watchOS 3.1.1 SDK to develop code.

### Xcode

### Known Issue

When launching an app built for watchOS 2.0 or later from an incoming notification, the app exits with code `0` while the debugger is still attached.
