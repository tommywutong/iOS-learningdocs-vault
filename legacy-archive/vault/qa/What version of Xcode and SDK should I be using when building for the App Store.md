---
title: What version of Xcode and SDK should I be using when building for the App Store?
apple_id: DTS40013838
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2013-10-16'
source_url: https://developer.apple.com/library/archive/qa/qa1806/_index.html
archived_at: '2026-07-18T02:34:53.221788Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1806

# What version of Xcode and SDK should I be using when building for the App Store?

## Q:  What version of Xcode and SDK should I be using when building my app for the App Store?

A: Plan to build with [the latest version of Xcode](http://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12), and to set the __Base SDK__ build setting to `Latest iOS` or `Latest Mac OS`.

For more information, see [Setting the Deployment Target](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/ConfiguringYourApp/ConfiguringYourApp.html#//apple_ref/doc/uid/TP40012582-CH28-SW47) in the [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/ConfiguringYourApp/ConfiguringYourApp.html).

Building with the latest SDK gives your app all possible bug fixes and new behavior. For compatibility reasons, frameworks can't always expose improved behavior, unless apps are built with the latest SDK.

For example, when Retina enabled iPads were first introduced, only iPad apps built with the very latest iOS SDK could create Retina images by simply loading an image with an `@2x` suffix.

Other Retina iOS devices already treated `@2x` file names specially, but the existing non-Retina iPads did not. Because some apps were relying on this behavior by re-using Retina iPhone images as larger 1x images on iPads, it was not possible for the new Retina iPads to always special case all `@2x` images. That could have caused problems in existing apps. To support those apps, iOS checked the SDK an app was built with to determine if it got improved handling, or legacy behavior, when loading `@2x` images. This kind of test is called a __linked on or after check__.

By building with the latest SDK, apps signal that they are ready for all API improvements and bug fixes.

It is not practical for Xcode to force every project to build with the latest SDK. For example, it may be necessary to ship an immediate hot-fix version of app - without waiting until the app has been fully updated for a newer SDK.

But it's important to understand that using an older SDK is a __temporary workaround__, not a solution. Issues preventing your app from using the latest SDK should be fixed as soon as possible. It will be much easier to fix these issues while the older build system is still supported.

For compatibility reasons, the App Store will often accept apps that are built with some older versions of Xcode or Base SDK.

To determine if an older Xcode configuration is currently accepted by the App Store, you can choose "Archive" under the "Product" menu to make an archived build, then [use the Validate feature](https://developer.apple.com/library/ios/recipes/xcode_help-archives_organizer/articles/validating_apps.html), to test if that build meets minimum requirements for submission to the App Store.

You may find it easier to create a test test bundle ID in the Member Center and application record in iTunes Connect to test your build environment, so you don't need to correctly configure every entitlement your app uses.

[SDK Compatibility Guide](https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/cross_development/)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-10-16 | New document that describes why you should be using the latest SDK, and how to check if an older development system is obsolete. |

