---
title: Resolving Compatibility Problems on New OS Releases
apple_id: DTS40017626
resource_type: Technical Note
platform: watchOS|tvOS|iOS|Xcode Developer Tools|macOS
topic: General
technology: null
published: '2017-11-08'
source_url: https://developer.apple.com/library/archive/technotes/tn2456/_index.html
archived_at: '2026-07-26T19:54:15.284409Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2456

# Resolving Compatibility Problems on New OS Releases

Compatibility problems are bugs that appear when your application is run on a newer version of the operating system (macOS, iOS, tvOS, or watchOS), but not on a previous version of the operating system. Though not readily apparent, every compatibility problem can be classified as either a binary compatibility problem (also referred to as backwards compatibility problem) or a source compatibility problem. This distinction is important as it determines how you go about resolving the problem.

To determine whether a compatibility problem is a binary compatibility problem or a source compatibility problem, ask whether the version of Xcode used to build the application is the version of Xcode that is aligned with the operating system release where the problem is occurring. Each major operating system release (and some minor operating system releases) have a corresponding release of Xcode. This Xcode release contains a matching version of the operating system's SDK, that allows your application to take advantage of the latest features available on the operating system.

If you are building the application with a version of Xcode (and SDK) that is older than the version of the operating system where the problem is occurring, then the problem is classified as a __binary compatibility problem__ - the newer operating system is not compatible with existing binaries built with older tools.

If you are building the application with a version of Xcode (and SDK) that is aligned with, or newer than, the version of the operating system where the problem is occurring, then the problem is classified as a __source compatibility problem__ - the same source code is not compatible with the newer operating system or tools.

__Note:__ This assumes that the application behaved correctly when it was a) built with older tools and b) run on an older operating system. If both of these criteria are not met, this is not a compatibility problem.

If you are building a new application, and want to support the current and one or more previous operating system versions, refer to the [SDK Compatibility Guide](https://developer.apple.com/library/content/documentation/DeveloperTools/Conceptual/cross_development/Introduction/Introduction.html).

__Note:__ Compilation failures when using a new version of Xcode is also a source compatibility problem.

__Table 1__  Recent Xcode versions and the SDKs they included.

|  | Xcode 9 | Xcode 8 | Xcode 7 | Xcode 6 |
| macOS SDK Version | 10.13 (High Sierra) | 10.12 (Sierra) | 10.11 (El Capitan) | 10.10 (Yosemite) |
| iOS SDK Version | 11.0 | 10.0 | 9.0 | 8.0 |
| tvOS SDK Version | 11.0 | 10.0 | 9.0 |  |
| watchOS SDK Version | 4.0 | 3.0 | 2.0 |  |

[Binary Compatibility Problems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrsgywugsbrfvbestsdj5gvaqku)[Resolving Binary Compatibility Problems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrsgywugsbrfvbestsdj5gvaqkufvjeku2pjrlestshl5bestsbkjmv6q2pjviecvcjijeuyskulfpvauspijgektkt)[Source Compatibility Problems](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrsgywugsbrfvju6vksincugt2nkbavi)[Tips For Updating an Existing Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrsgywugsbrfvkvarcbkreu4ry)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrsgywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Binary Compatibility Problems

Each release of Apple's operating systems strive to be binary compatible (also referred to as backward compatible) with applications built using older versions of Xcode. Within the system frameworks, this is accomplished by checking the SDK version (Xcode version) that the application was built with and altering behavior when necessary. This is often referred to as a __linked-on-or-after check__. These checks are scattered throughout the system and are used to alter behavior to be more like a previous operating system version when running an older application. This is what allows, for example, the standard UIKit elements to revert to their legacy (iOS 6) look when running an application built with Xcode 4.

Binary compatibility on each OS isn't always perfect. Apps that stop working as expected after an OS upgrade may be caused by a number of different factors including:

__Regressions and bugs in the OS__

In such cases, you are encouraged to file bug reports so that the engineering team can fix the compatibility in a future OS release.

__Using supported APIs in unsupported ways__

The API documentation describes the contract between your application and the operating system: what inputs an API consumes, what tasks it is expected to perform, and what results it returns.

Your application may be relying on API behavior beyond what's documented, that appeared to work in testing on the older operating system. Any behavior not covered in the API documentation can change without notice in future OS versions.

__Performance changes between OS versions__

While an API contract specifies behavior, it rarely guarantees a particular level of performance. Improvements (and regressions) in an operating system often mean that some APIs perform faster or with a smaller memory footprint while others are slower or require more memory.

Code often has intentional or unintentional dependencies on an API's performance, and multithreaded code makes these dependencies more likely. Race conditions between threads can often be exposed when a new operating system is installed.

__Bug fixes in the new OS__

The changes made to fix a bug in the operating system may conflict with existing workarounds in your application.

Your workarounds should avoid modifying Apple framework code (sometimes referred to as "method swizzling") or manipulating framework objects in a manner other than what their API permits. [Developer Technical Support](https://developer.apple.com/support/technical/) may be able to provide a supported workaround (if one is available).

__Objective-C class name collisions__

New Objective-C classes (both public and private) are typically added in each operating system release. The names of these classes may conflict with (match) the names of existing classes in your application, causing undefined behavior.

__Listing 1__  The following message will be logged to the device's console when a class name collision is detected.

```
"Class <ClassName> is implemented in both <YourApplicationName> and <AppleFrameworkName>. One of the two will be used. Which one is undefined."
```

All Objective-C classes, as well as any Swift classes exposed to Objective-C [with custom names](https://developer.apple.com/library/content/documentation/Swift/Conceptual/BuildingCocoaApps/InteractingWithObjective-CAPIs.html#//apple_ref/doc/uid/TP40014216-CH4-ID55), must have a unique name (within a process). Always follow the conventions outlined in the [Programming with Objective-C](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/Conventions/Conventions.html) document when naming your classes.

__Objective-C category method name collisions__

An operating system release may add new methods to existing Objective-C classes. The names of new methods of a class may [conflict](https://developer.apple.com/library/content/qa/qa1908/_index.html) with the names of methods that your application has added to that class using categories (extensions in Swift). Your category methods will override the implementation in Apple's class, often leading to unexpected behavior.

When using a category to add methods to an Apple framework class, include a [prefix](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html#//apple_ref/doc/uid/TP40011210-CH6-SW4) on all method names within to avoid clashes.

__Security hardening changes__

Operating system changes are sometimes introduced in response to security threats or bugs in order to protect the user's data. Some of these changes require your app to change in order to keep working. For example, iOS 6 began preventing all apps from accessing the unique device identifier. And System Integrity Protection in OS X El Capitan blocked access to parts of the filesystem that were previously accessible.

### Resolving Binary Compatibility Problems

The first step to resolve any compatibility problem is to identify the root cause of the failure, which means reproducing the results or at least gathering logs from affected users so you have some idea of which part of the code needs to be examined. Then you can determine whether the root cause is a bug in your code or in the operating system. File [bug reports](https://developer.apple.com/bug-reporting) with the results of your testing. Check the operating system [Release Notes](https://developer.apple.com/library/prerelease/content/navigation/#section=Resource%20Types&topic=Release%20Notes) for changes that are expected to have an impact on existing applications.

It's important to test your apps on the beta releases Apple makes available, and to file any bug reports early. Once the operating system release has exited the beta period and shipped to customers, compatibility bug fixes can not be retroactively added to that version. In this case, the only way to resolve the compatibility issue is to update the application.

[Back to Top](#)

## Source Compatibility Problems

As a result of building your application with the latest Xcode, you might notice different behaviors, some of which might cause incompatibilities. Your application may fail to build, or may build with additional warnings, due to API changes in the newer SDK (e.g, API deprecations).

In these cases because the application is being rebuilt, compatibility checks that are used by the system to modify behavior for older applications no longer apply. Thus, you are expected to modify your application's code to resolve these incompatibilities and adopt the latest best practices for the newer operating system (see [Tips For Updating an Existing Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrsgywugsbrfvkvarcbkreu4ry)).

If you are doing a small incremental update of your application to address a few bugs, it's usually best to continue building with the same version of Xcode used originally.

[Back to Top](#)

## Tips For Updating an Existing Application

Before you begin updating your application, take some time to familiarize yourself with the recent changes to your target operating system (macOS, iOS, tvOS, watchOS) and Xcode. Every WWDC typically includes key sessions that cover important changes for that year's tools and operating systems releases: the Platforms State of the Union, What's New in Cocoa (for macOS), and What's New in Cocoa Touch (for iOS, tvOS, and watchOS). In these sessions, Apple engineers discuss new API, important deprecations, and general expectations for all applications. Below are links to the Platforms State of the Union and What's New in Cocoa Touch session videos for the past five years. All past WWDC session videos can be found [here](https://developer.apple.com/videos).

- __2017 (iOS 11)__: [Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2017/102/), [What's New in Cocoa](https://developer.apple.com/videos/play/wwdc2017/207/), [What's New in Cocoa Touch](https://developer.apple.com/videos/play/wwdc2017/201/)
- __2016 (iOS 10)__: [Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2016/102/), [What's New in Cocoa](https://developer.apple.com/videos/play/wwdc2016/203/), [What's New in Cocoa Touch](https://developer.apple.com/videos/play/wwdc2016/205/)
- __2015 (iOS 9)__: [Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2015/102/), [What's New in Cocoa](https://developer.apple.com/videos/play/wwdc2015/202/), [What's New in Cocoa Touch](https://developer.apple.com/videos/play/wwdc2015/107/)
- __2014 (iOS 8)__: [Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2014/102/), [What's New in Cocoa](https://developer.apple.com/videos/play/wwdc2014/204/), [What's New in Cocoa Touch](https://developer.apple.com/videos/play/wwdc2014/202/)
- __2013 (iOS 7)__: [Platforms State of the Union](https://developer.apple.com/videos/play/wwdc2013/101/), [What's New in Cocoa](https://developer.apple.com/videos/play/wwdc2013/205/), [What's New in Cocoa Touch](https://developer.apple.com/videos/play/wwdc2013/203/)
- __2012 (iOS 6)__: [Platforms Kickoff](https://developer.apple.com/videos/play/wwdc2012/101/), [What's New in Cocoa](https://developer.apple.com/videos/play/wwdc2012/204/), [What's New in Cocoa Touch](https://developer.apple.com/videos/play/wwdc2012/200/)

If your application includes Swift code, you may need to convert your code to the latest Swift syntax. A Swift migrator is provided to help upgrade your Swift code to the latest Swift language specifications and SDK requirements but you should familiarize yourself with the [latest Swift changes](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/RevisionHistory.html) so that you can fix any remaining issues.

Other resources for tracking important changes in each release include:

- the _[What’s New in Xcode](../documentation/Developer%20Tools/What%E2%80%99s%20New%20in%20Xcode/What%27s%20New%20in%20Xcode%209.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmrw)_ document
- the [What's New in macOS](https://developer.apple.com/library/content/releasenotes/MacOSX/WhatsNewInOSX/WhatsNewInOSX.html) document
- the [What's New in iOS](https://developer.apple.com/library/content/releasenotes/General/WhatsNewIniOS/Introduction/Introduction.html) document
- the [What's New in tvOS](https://developer.apple.com/library/content/releasenotes/General/WhatsNewinTVOS/Introduction/Introduction.html) document
- the [What's New in watchOS](https://developer.apple.com/library/content/releasenotes/General/WhatsNewInwatchOS/Introduction/Introduction.html) document
- the [release notes and API differences between OS versions](https://developer.apple.com/library/content/navigation/#section=Resource%20Types&topic=Release%20Notes)

[Sample code](https://developer.apple.com/library/content/navigation/#section=Resource%20Types&topic=Sample%20Code) is also a great resource to study the current best practices in action.

Once your application is building with the latest Xcode and running great on the latest OS version, be sure to thoroughly test your application before submitting an update. In particular, test that data from the previous version(s) of your application can be read (and migrated/updated as necessary) by your forthcoming update. The [App Testing Guide](https://developer.apple.com/library/content/technotes/tn2431/_index.html) lists strategies for testing the app update process and many other common causes of customer facing issues.

__Important:__ While modifying your application to be compatible with the latest operating system, you might accidentally introduce regressions on previous operating system versions. Don't forget to also test your updated application on any previous OS versions that you have chosen to continue supporting.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-11-08 | Updated with information for the 2017 releases of Xcode, iOS, macOS, watchOS, and tvOS |
| 2017-04-03 | New document that discusses compatibility problems and provides guidance for developers looking to update older applications. |

