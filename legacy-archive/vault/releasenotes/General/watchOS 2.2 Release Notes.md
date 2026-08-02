---
title: watchOS 2.2 Release Notes
apple_id: TP40016678
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-watchOSSDK-2.2/index.html
archived_at: '2026-07-18T02:54:43.686713Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# watchOS SDK Release Notes for watchOS 2.2

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnzyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnzyfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnzyfvbuqmjnknltc)

### Introduction

watchOS SDK 2.2 provides support for developing watchOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for watchOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

This version of watchOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of watchOS in an unauthorized manner could put your device in an unusable state.

For more information and additional support resources, visit [https://developer.apple.com/programs/](https://developer.apple.com/programs/).

### Bug Reporting

For issues not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnzyfvbuqmjnknltc) section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/ios/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and watchOS SDK 2.2 in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome)

### Notes and Known Issues

### WatchKit

### Known Issue

watchOS 1 apps install and begin to launch, but fail to attach.

### Xcode

### Known Issues

- Crash reports for watchOS 2 apps do not appear in the Xcode Devices window.

  __Workaround:__ Attach to the WatchKit extension and reproduce the crash to get a stack trace.
- You may receive an `SPErrorUnknownMessage` when building and running a watchOS 2 app.

  __Workaround:__ Build and run the app a second time.
