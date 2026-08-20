---
title: iOS 4.0.2 Release Notes
apple_id: TP40010239
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2010-08-10'
source_url: https://developer.apple.com/library/archive/releasenotes/General/RN-iPhone-4_0_2/index.html
archived_at: '2026-07-18T02:54:42.614953Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# iOS SDK Release Notes for iOS 4.0.2

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemzzfvbuqmjnknltg)
- [Bug Reporting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemzzfvbuqmjnknlti)
- [Known Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemzzfvbuqmjnknlte)

### Introduction

iOS SDK 4.0.2 is an update to iOS 4.0 or iOS 4.0.1, which provide support for developing iPhone and iPod touch applications and includes the complete set of Xcode tools, compilers, and frameworks for creating applications for iOS and Mac OS X. These tools include the Xcode IDE and the Instruments analysis tool among many others.

With this software you can develop applications that run on iPhone or iPod touch using the included iOS Simulator. Installing iOS SDK 4.0.2 requires a Macintosh computer running Mac OS X 10.6.2 (Snow Leopard) or later.

We encourage developers to apply to the iOS Developer Program for access to additional support resources, including provisioning resources to enable development directly on an iPhone or iPod touch. For more information visit:

[http://developer.apple.com/devcenter/ios/program/](https://developer.apple.com/devcenter/ios/program/)

### Bug Reporting

Please report any bugs not mentioned in the "Known Issues" section using the Apple Bug Reporter on the Developer Connection website at: [http://developer.apple.com/bugreporter/](https://developer.apple.com/bugreporter/).

### Known Issues

The following issues relate to using the 4.0 SDK to develop code.

### UIAutomation

- The Automation Instrument in this release looks for the `com.apple.Accessibility.plist` file under the iOS Simulator 4.0.2 folder; however, it is only present under the iOS Simulator 4.0 folder if that SDK was ever installed. You can workaround this bug by making a symlink between your iOS Simulator 4.0 and 4.0.2 folders.
- Follow these steps to create a symlink between your iOS Simulator 4.0 and 4.0.2 folders:

  - Quit Instruments and the iOS Simulator if they are running.
  - Run the following commands in the Terminal application on your machine:

    `cd ~/Library/Application\ Support/iPhone\ Simulator/`

    `ln -s 4.0.2 4.0`
- You can find more details in Q&A 1705, which is available in the iOS Reference Library.
