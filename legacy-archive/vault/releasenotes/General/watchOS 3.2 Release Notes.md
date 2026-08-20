---
title: watchOS 3.2 Release Notes
apple_id: TP40017613
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-watchOSSDK-3.2/index.html
archived_at: '2026-07-18T02:54:43.846960Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# watchOS SDK Release Notes for watchOS 3.2

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmjtfvbuqmjnknltc)

### Introduction

watchOS SDK 3.2 provides support for developing watchOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for watchOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

This version of watchOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of watchOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [https://developer.apple.com/programs/](https://developer.apple.com/programs/).

### Bug Reporting

For issues not mentioned in [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3tmmjtfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/). Additionally, you may discuss these issues and watchOS SDK 3.2 in the Apple Developer Forums at [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome).

### Notes and Known Issues

The following items relate to using watchOS 3.2 SDK to develop code.

### Xcode

### Known Issues

- Complication targets may exit if you enable the complication after deploying for the first time.

  __Workaround:__ Deploy the app again.
- When deploying using Xcode, notifications do not show up for WatchKit for watchOS 1 applications.
- Contacts do not show in Simulator.
