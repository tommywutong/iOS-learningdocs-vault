---
title: WatchKit Project Configuration Reference
apple_id: DTS40015545
resource_type: Technical Note
platform: iOS
topic: Xcode
technology: WatchKit
published: '2016-08-30'
source_url: https://developer.apple.com/library/archive/technotes/tn2410/_index.html
archived_at: '2026-07-27T06:57:05.404143Z'
---
> 导航：[总目录](../../README.md) · [technotes](../../_indexes/technotes.md)



Technical Note TN2410

# WatchKit Project Configuration Reference

This document discusses the proper configuration of a WatchKit Extension and WatchKit App when added to an existing Xcode project. Refer to this document if you have made a change to your project which is causing your WatchKit App to no longer run, or if you are encountering WatchKit-related validation errors when submitting your app.

If you are just getting started with WatchKit, refer to [Adding a WatchKit App to Your iOS Project](https://developer.apple.com/library/ios/documentation/General/Conceptual/WatchKitProgrammingGuide/ConfiguringYourXcodeProject.html) in the Apple Watch Programming Guide for the steps to add a WatchKit App to your existing project.

__Important:__ This document discusses the configuration of watchOS 1 applications. Refer to [Project Configuration Reference for watchOS Applications](https://developer.apple.com/library/watchos/technotes/tn2424/_index.html) for information about configuring watchOS 2 or later projects.

[The WatchKit App](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvke4vcbi4yq)[Information Property List](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvke4vcbi4ys2skoizhvetkbkreu6ts7kbje6ucfkjkfsx2mjfjvi)[Build Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvke4vcbi4ys2qsvjfgeix2tivkfiskoi5jq)[Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvke4vcbi4ys2usfknhvkusdivjq)[The WatchKit Extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvkeqrk7k5aviq2ijnevix2flbkektstjfhu4)[Information Property List](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvkeqrk7k5aviq2ijnevix2flbkektstjfhu4lkjjzde6usnifkest2ol5ifet2qivjfiwk7jrevgva)[Build Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvkeqrk7k5aviq2ijnevix2flbkektstjfhu4lkckveuyrc7kncvivcjjzdvg)[Dependencies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvkeqrk7k5aviq2ijnevix2flbkektstjfhu4lkeiviektseivhegskfkm)[Validation Troubleshooting](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvlectcjiraviskpjzpviuspkvbeyrktjbhu6vcjjzdq)[WatchKit apps must have a deployment target equal to iOS 8.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvlectcjiraviskpjzpviuspkvbeyrktjbhu6vcjjzds2v2bkrbuqs2jkrpucucqknpu2vktkrpuqqkwivpucx2eivieyt2zjvcu4vc7kraver2fkrpukukvifgf6vcpl5eu6u27hbpte)[CFBundleIdentifier Collision](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvlectcjiraviskpjzpviuspkvbeyrktjbhu6vcjjzds2q2gijku4rcmiveuirkokreumskfkjpugt2mjrevgskpjy)[Invalid CFBundleIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvlectcjiraviskpjzpviuspkvbeyrktjbhu6vcjjzds2skokzauyskel5bumqsvjzceyrkjircu4vcjizeukuq)[WKAppBundleIdentifier Mismatch](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvlectcjiraviskpjzpviuspkvbeyrktjbhu6vcjjzds2v2lififaqsvjzceyrkjircu4vcjizeukus7jvevgtkbkrbuq)[Missing Icon](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvlectcjiraviskpjzpviuspkvbeyrktjbhu6vcjjzds2tkjknjustshl5eugt2o)[Appendix A: Retrieving Device Logs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwugsbrfvavaucfjzceswc7ifpv6usfkrjesrkwjfheox2eivlesq2fl5ge6r2t)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytknjuguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## The WatchKit App

The WatchKit app is a user launchable app that appears on the Apple Watch home screen. It contains only the storyboards and resource files associated with your app’s user interface and it works in tandem with your WatchKit extension. The WatchKit app does not contain any code; instead an Xcode provided binary is inserted into the WatchKit app bundle at build time. Being an app bundle, the WatchKit app must have a unique bundle identifier and it must be code signed. During installation the WatchKit app bundle is copied to the paired watch. The watch validates the bundle's code signature, information property list, and executable. If your application fails to install on the Watch, the problem is most likely caused by the incorrect configuration of your WatchKit app target. Additional information about the error which triggered the installation failure is logged to the paired iPhone's console. See Retrieving Device Logs.

### Information Property List

The WatchKit App must have an associated information property list. One is created for you by default when adding a WatchKit App to your project. By default it can be found under __<Product Name> WatchKit App/Supporting Files__ in the project navigator where __<Product Name>__ is the name of your iOS app. Some information property list keys are invalid for WatchKit apps and will produce a verification failure upon install. The offending key will be logged to the paired iPhone's device console.

__Figure 1__  Information property list for a properly configured WatchKit app target.

> 原归档配图未能恢复：`tn2410_WatchApp_InfoPlist.png`

- __Bundle Identifier (CFBundleIdentifier)__: The value for this key must be a unique reverse DNS string that is prefixed with the containing iOS app's bundle identifier. For example, if your iOS app has the bundle identifier `com.example.apple-samplecode.WatchKit-Catalog`, then the WatchKit app's bundle identifier should be `com.example.apple-samplecode.WatchKit-Catalog.watchkitapp`.
- __Bundle versions string, short (CFBundleShortVersionString)__: The value for this key must match the corresponding value in the containing iOS app's information property list.
- __Bundle version (CFBundleVersion)__: The value for this key must match the corresponding value in the containing iOS app's information property list.
- __WKCompanionAppBundleIdentifier__: The value for this key must match the bundle identifier of the containing iOS app.
- __WKWatchKitApp__: The value for this key must be `YES`.

### Build Settings

Because the WatchKit app does not contain any code, most build settings are ignored. Build settings for the WatchKit app can only be viewed in Xcode 6.3 and later.

__Figure 2__  Build settings for a properly configured WatchKit app target.

> 原归档配图未能恢复：`tn2410_WatchApp_BuildSettings.png`

- __Targeted Device Family__: Must be 4 (Watch) for running on the device, and 1 (Phone) for running in the simulator. If you have configured this build setting at the project level, reset it back to the default value, then modify the setting for your iOS app and extension targets individually. If you have modified this setting for the WatchKit app target, remove your WatchKit app and WatchKit extension targets then recreate them.
- __iOS Deployment Target__: Must be 8.2, regardless of the deployment target for the extension and containing iOS app.
- __Info.plist File__: Must be the project relative path to the information property list for the WatchKit app.

### Resources

A storyboard and asset catalog must be associated with your WatchKit app target. The asset catalog associated with your WatchKit app target must contain the [icons](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/WatchHumanInterfaceGuidelines/IconandImageSizes.html) for the WatchKit app and should not be associated with any other target in your project, to avoid duplicating resources. Additional resources that you want included in the WatchKit app bundle must also be associated with the WatchKit app target.

__Figure 3__  You can modify the target associations for a resource under the Target Membership pane of the File Inspector.

> 原归档配图未能恢复：`tn2410_WathApp_Resources.png`

__Note:__ Images displayed on the Apple Watch should use retina assets (@2x). See [Images](https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/WatchHumanInterfaceGuidelines/Images.html#//apple_ref/doc/uid/TP40014992-CH25-SW1) in the Apple Watch Human Interface Guidelines.

__Note:__ Some images authored with third-party graphics editing software may fail to load on the watch. If you notice images missing when running your application on the watch, reexport the affected images with Preview or move them into the WatchKit app's asset catalog.

[Back to Top](#)

## The WatchKit Extension

The WatchKit extension contains the code for managing content, responding to user interactions, and updating your user interface. Like all extensions, the WatchKit extension must have a unique bundle identifier and it must be code signed. Validation errors related to the WatchKit extension are normally reported by Xcode when running the WatchKit App but additional information can sometimes be found in the paired iPhone's console. See Retrieving Device Logs.

### Information Property List

The WatchKit extension must have an associated information property list. One is created for you by default when adding a WatchKit App to your project. By default it can be found under __<Product Name> WatchKit Extension/Supporting Files__ in the project navigator where __<Product Name>__ is the name of your iOS app.

__Figure 4__  Information property list for a properly configured WatchKit extension target.

> 原归档配图未能恢复：`tn2410_WatchExtension_InfoPlst.png`

- __Bundle Identifier (CFBundleIdentifier)__: The value for this key must be a unique reverse DNS string that is prefixed with the containing iOS app's bundle identifier. For example, if your iOS app has the bundle identifier `com.example.apple-samplecode.WatchKit-Catalog`, then the WatchKit extension's bundle identifier should be `com.example.apple-samplecode.WatchKit-Catalog.watchkitextension`.
- __Bundle versions string, short (CFBundleShortVersionString)__: The value for this key must match the corresponding value in the containing iOS app's information property list.
- __Bundle version (CFBundleVersion)__: The value for this key must match the corresponding value in the containing iOS app's information property list.
- __WKAppBundleIdentifier__: The value for this key must match the bundle identifier of the WatchKit app.
- __NSExtensionPointIdentifier__: The value for this key must be `com.apple.watchkit`.

### Build Settings

__Figure 5__  Build settings for a properly configured WatchKit extension target.

> 原归档配图未能恢复：`tn2410_WatchExtension_BuildSettings.png`

- __Architectures__: Should be __Standard architectures__. If you manually specify the architectures, you must include armv7 and arm64.
- __Valid Architectures__: Must include armv7, armv7s, and arm64..
- __Targeted Device Family__: Should be iPhone.
- __iOS Deployment Target__: Must be 8.2 or later.
- __Info.plist File__: Must be the project relative path to the information property list for the WatchKit extension.

### Dependencies

The WatchKit extension must include the WatchKit app target as a dependency. The WatchKit app product must also be copied into the WatchKit extension's bundle at build time.

__Figure 6__  Build phases for a properly configured WatchKit extension target.

> 原归档配图未能恢复：`tn2410_WatchExtension_Phases.png`

[Back to Top](#)

## Validation Troubleshooting

This section discusses WatchKit related validation errors you may receive when submitting your app.

### WatchKit apps must have a deployment target equal to iOS 8.2

The WatchKit app target has a deployment target greater than 8.2. The WatchKit App target must have a deployment target of iOS 8.2, regardless of the deployment target for your WatchKit extension and containing iOS app. See Configuring the WatchKit App's Build Settings.

### CFBundleIdentifier Collision

The WatchKit App or the WatchKit extension has the same bundle identifier as the containing iOS app. The WatchKit app, WatchKit extension, and containing iOS app must have unique bundle identifiers.

### Invalid CFBundleIdentifier

The bundle identifier for your WatchKit App or WatchKit Extension is not prefixed with the containing iOS app's bundle identifier. The bundle identifier for the WatchKit App and the WatchKit Extension must be prefixed with the containing iOS app's bundle identifier. For example, if the containing iOS app has a bundle identifier of `com.example.apple-samplecode.WatchKit-Catalog`, then the WatchKit app's bundle identifier should be `com.example.apple-samplecode.WatchKit-Catalog.watchkitapp`, and the WatchKit extension's bundle identifier should be `com.example.apple-samplecode.WatchKit-Catalog.watchkitextension`.

### WKAppBundleIdentifier Mismatch

The value for the __WKCompanionAppBundleIdentifier__ key in the Watch app's information property list does not match the bundle identifier of the containing iOS app. The value for the __WKCompanionAppBundleIdentifier__ key in the Watch app's information property must match the bundle identifier of the containing iOS app. See Configuring the WatchKit App's Information Property List.

### Missing Icon

Refer to [Technical QA1686](https://developer.apple.com/library/ios/qa/qa1686/_index.html) for help troubleshooting icon-related validation failures.

[Back to Top](#)

## Appendix A: Retrieving Device Logs

Error messages relating to installation failures on the Watch are sent over to the paired iPhone, where they are logged to the iPhone's device console. To view the device console:

1. Connect the iPhone and open Xcode.
2. Choose __Window__ > __Devices__ from the menu.
3. Under the DEVICES section in the left column, select the iPhone.
4. To see the device console, click the up-triangle at the bottom left of the right hand panel to show the device console.

Installation failure error messages are logged by the `companionappd` process.

__Figure 7__  The device logs window with an installation failure error message highlighted. This particular error was caused by the WatchKit app having a deployment target greater than 8.2.

> 原归档配图未能恢复：`tn2410_device_logs.png`

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-08-30 | Marked document as Legacy. Added a link to the replacement Project Configuration Reference for watchOS 2 Applications document. |
| 2015-05-04 | New document that describes the proper configuration for a project with a WatchKit app. |
