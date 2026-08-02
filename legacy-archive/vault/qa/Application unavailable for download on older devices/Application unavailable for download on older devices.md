---
title: Application unavailable for download on older devices
apple_id: DTS40016693
resource_type: QA
platform: iOS
topic: General
technology: null
published: '2016-01-19'
source_url: https://developer.apple.com/library/archive/qa/qa1910/_index.html
archived_at: '2026-07-18T02:35:43.120205Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1910

# Application unavailable for download on older devices

## Q:  Why can't users install my application on an iPhone 4s, iPhone 5, or iPhone 5c?

A: The App Store prevents applications which include the `arm64` required device capability from being installed on devices that do not support the arm64 instruction set. Devices that run recent versions of iOS but do not support the arm64 instruction set include:

- iPhone 4
- iPhone 4s
- iPhone 5
- iPhone 5c
- iPod touch (5th Generation)
- iPad 2
- iPad 3rd generation
- iPad 4th generation
- iPad Mini

Users browsing the App Store on these devices will receive an error if they try to download your app.

iTunes Connect lists the supported architectures and required device capabilities for each version of your app under the Build Details. See [Viewing Build Details](https://developer.apple.com/library/ios/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/ChangingAppMetadata.html#//apple_ref/doc/uid/TP40011225-CH3-SW19) in the iTunes Connect Developer Guide.

__Figure 1__  Supported architectures and required device capabilities are listed under the Device Requirements section.

!!

If `arm64` appears under the Required Capabilities then your app is prevented from being installed on devices that do not support the arm64 instruction set.

In order to be eligible for installation on the devices listed at the beginning of this document, your application must be compiled for armv7 (in addition to arm64) and must __not__ include the `arm64` required device capability.

Required device capabilities are specified in the application's information property list, as an array of strings associated with the [Required device capabilities](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html) (`UIRequiredDeviceCapabilities`) key. Open the Info pane for your application's target and expand the Required device capabilities property, as shown in Figure 2. Locate the entry with `arm64` in the value column and remove it.

__Figure 2__  You can view and edit required device capabilities in the Info pane for your application target.

!!

The __Architectures__, __Valid Architectures__, and __Build Active Architectures Only__ build settings determine which architectures the target is compiled for.

- The __Architectures__ build setting should be set to __Standard Architectures__, which is the default.
- The __Valid Architectures__ list should contain `armv7`, `armv7s` and `arm64`, which is the default.
- The __Build Active Architectures Only__ build setting should be set to __NO__ for the Release configuration.

Open the Build Settings pane for your application's target. Remove any project or target overrides for the __Architectures__, __Valid Architectures__, and __Build Active Architectures Only__ build settings.

__Figure 3__  The Levels view makes it easy to spot where a build setting may be overridden.

!!

If your application is dependent on one or more frameworks, check the build settings for their targets as well.

Build a new version of your application and upload it to iTunes Connect. Confirm that the details page for this new build lists __armv7__ and __arm64__ under Supported Architectures and that __arm64__ is not listed under Required Capabilities. Finally, submit your build for review.

For more information about device capabilities, refer to the [iOS Device Compatibility Reference](https://developer.apple.com/library/ios/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/DeviceCompatibilityMatrix/DeviceCompatibilityMatrix.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-01-19 | New document that discusses project configurations that restrict the availability of an app on devices that do not support the arm64 instruction set. |

