---
title: watchOS 2.1 Release Notes
apple_id: TP40016640
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-watchOSSDK-2.1/index.html
archived_at: '2026-07-18T02:54:43.651714Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# watchOS SDK Release Notes for watchOS 2.1

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbqfvbuqmjnknltc)

### Introduction

watchOS SDK 2.1 provides support for developing watchOS apps. It is packaged with a complete set of Xcode tools, compilers, and frameworks for creating apps for watchOS. These tools include the Xcode IDE and the Instruments analysis tool, among many others.

This version of watchOS is intended for installation only on devices registered with the Apple Developer Program. Attempting to install this version of watchOS in an unauthorized manner could put your device in an unusable state.

### Bug Reporting

For issues not mentioned in the [Notes and Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbqfvbuqmjnknltc) section, please file bugs through the Apple Developer website ([https://developer.apple.com/bug-reporting/ios/](https://developer.apple.com/bugreporter/)). Additionally, you may discuss these issues and watchOS SDK 2.1 in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome).

### Notes and Known Issues

### Activation Lock

### Note

Activation Lock is enabled on your Apple Watch if you have Find My iPhone enabled on your iPhone.

### Connectivity

### Note

Enable "Install All Apps" in Watch.app > General > App Install for Watch Connectivity to work correctly during Build and Run cycles.

### Keychain

### Note

Keychain items created on an Apple Watch are not viewable on an iOS device.

### Maps

### Known Issues

- If you do not see map tiles load in watch Simulator, launch the Maps app in iOS simulator first. After that, map tiles will load.
- The [MKMapItem](https://developer.apple.com/documentation/mapkit/mkmapitem) method [openInMapsWithLaunchOptions:](https://developer.apple.com/documentation/mapkit/mkmapitem/1452239-openinmapswithlaunchoptions) does not work.

### WatchKit

### Notes

- [WKInterfacePicker](https://developer.apple.com/documentation/watchkit/wkinterfacepicker) includes the [resignFocus](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/1627937-resignfocus) method to remove focus.
- The method `focusForCrownInput` has been renamed to [focus](https://developer.apple.com/documentation/watchkit/wkinterfacepicker/1627944-focus).
- Installing a WatchKit 1.0 app with an Xcode prior to 7.0 requires that "Automatic App Install" be enabled in the Watch app under General > App Install.
