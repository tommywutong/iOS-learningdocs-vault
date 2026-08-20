---
title: Testing your app on Beta OS releases
apple_id: DTS40011977
resource_type: Technical Note
platform: iOS|macOS
topic: General
technology: null
published: '2016-05-20'
source_url: https://developer.apple.com/library/archive/technotes/tn2249/_index.html
archived_at: '2026-07-27T06:57:02.121316Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2249

# Testing your app on Beta OS releases

This document covers the process of testing your apps on beta operating systems, as well as what to do when encountering changes in your app's behavior in the process. APIs and programming languages can evolve from release-to-release, which creates a need to verify your software continues to work as expected. To perform this verification, Apple provides registered developers with early access to the revised operating system before it goes public. Changes in a given update of the operating system might effect your app, so taking the time to check can either give your app an advantage over the competition, or, create a bad user experience for your customers.

[Definition of Terms](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojxg4wugsbrfvkekusnkm)[Summary of things to look for](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojxg4wugsbrfveu4vcsj4)[How to do it?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojxg4wugsbrfvjekukvjfjek)[Best Practices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojxg4wugsbrfvbeku2u)[Test Unique Customer Configurations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojxg4wugsbrfvbvku2u)[What to do if your app behaves differently in the beta](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojxg4wugsbrfvluqqkul5ke6x2ej5pusrs7lfhvkus7ififax2civeecvsfknpuiskgizcverkokrgfsx2jjzpviscfl5bekvcb)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojxg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Definition of Terms

This document refers to the following relevant terms:

- Operating System or __OS__, which encompasses all of the following: __iOS, OS X, tvOS__ and __watchOS__.
- __Beta OS__, __Developer Preview__, or __Pre-Release__ refers to the advance access of Apple software given to developers for the purpose of verifying their third-party apps.
- __OS major revision__ refers to a pending new version of the operating system, for example, __iOS 9__.
- __GM Seed__ refers to a beta version of the operating system that is almost ready to go public. For example, the iOS 9 GM Seed is a version of iOS 9 beta that will most likely represent the first public version of iOS 9.
- The __GM__ version of the OS refers to the version of the OS that has gone public. For example, iOS 9 GM refers to the last GM Seed that was approved by Apple for release to the public.
- __Beta SDK__ refers to the Beta version of Xcode that includes a software development kit (SDK) matching the version number of the beta OS that you wish to test.

[Back to Top](#)

## Summary of things to look for

The following is a categorization of the things you might encounter when testing your app on a beta OS release. These are the primary points of interest to look for when verifying your app works correctly in the new OS.

- __Framework Bugs__

  Framework bug reports should be filed early and often to give the best chance they can be fixed before the OS revision goes public.

  __Important:__ Discussing an issue on a Developer Forum is not a substitute for filling a bug report. Filing the bug first is a better way to ensure that a real framework bug can be diagnosed and fixed __before__ the OS-update goes public.

  • To file a bug report, use the [Bug Reporter](https://developer.apple.com/bug-reporting) tool on the Apple developer website.
- __API or Language Evolution__

  Changes to your app can be required for various reasons, for example, due to deprecation or changes in API semantics. The earlier you identify these types of potential changes, the wider the development window is for implementation and testing.

[Back to Top](#)

## How to do it?

This section covers the required packages that must be downloaded and installed to begin testing your app on the beta.

1. The beta OS must be installed on your device (Mac, Apple TV, Apple Watch or iOS device). The beta OS, when offered, is available on the respective developer download page. For example, see [iOS Downloads](https://developer.apple.com/ios/download/).
2. You must build and run your app using a version of Xcode that includes the beta SDK matching the version number of the OS you wish to test. Beta Xcode releases, when they are offered, are available on the [Xcode Downloads](https://developer.apple.com/xcode/downloads/) developer webpage.

__Important:__ Before installing the beta OS on your device, heed the warnings and recommendations made within the following sections of this document: [Best Practices](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojxg4wugsbrfvbeku2u) and [Test Unique Customer Configurations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcojxg4wugsbrfvbvku2u) to avoid any unexpected circumstances.

[Back to Top](#)

## Best Practices

These are best practices to follow in general when testing your app on the beta.

- Beta OS versions should be installed on a machine allocated specifically for testing. Since the purpose of pre-release access is to verify software runs correctly, it is not recommended to assume other production or mission-critical services that your business relies on will work as expected on the beta.
- __OS X__-specific Best Practices

  1. When upgrading from a beta to a build that isn’t available from software update, you should always erase the drive/partition before you install the new beta.
  2. Keep a copy of the previous operating system release running on a system for regression testing so that it can be cloned for use on a test system configured as an upgrade from the previous operating system release.
- __iOS, watchOS, tvOS__ Best Practices

  1. Devices with an iOS beta installed may be restored to the current GM version of the OS, but they cannot be downgraded to the previous, non-beta, major OS version. See the [Apple Support pages](https://support.apple.com/en-us/HT203282) for more information.

     __Note:__ Plan your beta installation such that you still have other devices running the older OS. You will need the other devices for regression testing should you intend your app to deploy back to the older OS.
  2. Be sure to back up your devices data using the latest version of iTunes or through iCloud backup prior to installing a beta. After installing the beta, you can restore device data through iTunes or iCloud backup.

[Back to Top](#)

## Test Unique Customer Configurations

It is also important to be aware of the unique software configurations that your users may have. As an example, you should focus your efforts on the following software configurations:

1. Testing on the previous operating system.
2. Development and testing on the latest operating system your customers are using.
3. Development and testing on the current beta.

- __OS X__-specific recommendations

  - To test against these configurations it is recommended that you have at least three different external hard drives with the software configurations listed above installed on them. At a minimum, you can set up one drive that has three partitions with the above software configurations.
  - You should have at least one of each family of Macs (Macs with the same architecture, CPU, memory, graphics processor and so on) your customers are using to test each OS configuration against. If you can afford it, you should have one of each of the Macs your customers may have to test each OS configuration against.
- __iOS, watchOS, tvOS__-specific recommendations

  - Maintain a collection of devices for testing each version of the OS your customers may have, and also test on beta releases that your customers don't have yet. Because devices updated to an iOS, tvOS, or watchOS version may not be restored to a previous OS, it requires you to have multiple similar devices to maintain the ability to test customer configurations that involve that a particular device running the older OS.
  - You should have at least one of each family of devices (devices that have the same architecture, 32-bit or 64-bit, screen resolution and PPI) for each OS major version your app aims to support. To avoid missing issues that might occur on a unique device configuration, you should own and test on e.

    __Note:__ At a minimum, you can test your iOS or watchOS apps Simulator. However, the simulator provides limited testing coverage and is not a substitute for real hardware with real memory and performance constraints.

[Back to Top](#)

## What to do if your app behaves differently in the beta

Differences in behavior can result from a framework bug in the beta, or, a framework change that exposes a bug in your app's code. The following process should be used to distinguish between the two:

1. Isolate the issue into a minimal reproducible case. By removing code not necessary to reproduce the bug, the cause of the problem is often easier to find. If the issue looks like a framework bug, the sample code you created in the process can more easily be attached to a bug report which is critical to expediting its fix.
2. Issues with your app's code can be discussed on the Developer Forums: [https://forums.developer.apple.com/](https://forums.developer.apple.com/) but remember to file a bug report for anything you think could be a framework issue.
3. For framework bugs:

   - Its just as important to include a runnable Xcode project that reproduces the problem as it is to clearly describe the issue using the Bug Reporter: [http://developer.apple.com/bugreporter](https://developer.apple.com/bugreporter).

     __Note:__ Filing the bug report sooner rather than later gives the best chance at getting it fixed before the OS goes GM.
   - Use the Developer Forums to discuss potential workarounds for framework bugs in the event that a fix does not make the first public release: [https://forums.developer.apple.com/](https://forums.developer.apple.com/).
4. Bugs that reproduce on the older, non-beta OS should be handled differently. Follow this process to deal with bugs that are present in a GM OS version:

   - Submit a bug report that mentions all OS versions the issue is present within, and also include a runnable Xcode project that reproduces the bug here: [http://developer.apple.com/bugreporter](https://developer.apple.com/bugreporter).
   - Use the Developer Forums to discuss potential workarounds for framework bugs in the event that a fix does not make the first public release: [https://forums.developer.apple.com/](https://forums.developer.apple.com/).
   - Submit a Developer Technical Support Incident to get help from Apple DTS: [https://developer.apple.com/support/technical/](https://developer.apple.com/support/technical/).

     __Note:__ Apple DTS does not support issues that only occur in a beta OS. You must submit a bug report for issues that only occur in the beta using [Bug Reporter](https://developer.apple.com/bug-reporting) as well as discuss the issue on the beta section of the [Developer Forums](http://forums.developer.apple.com).

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-05-20 | Editorial update. |
| 2015-09-02 | Updated to include specific information about iOS, OS X and watchOS seeds. |
| 2012-03-09 | New document that covers the process of testing apps on beta pre-release Apple operating systems to catch early framework bugs or adapt to changes. |
