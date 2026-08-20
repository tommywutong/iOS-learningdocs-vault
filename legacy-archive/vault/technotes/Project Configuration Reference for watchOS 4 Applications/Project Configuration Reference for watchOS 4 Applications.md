---
title: Project Configuration Reference for watchOS 4 Applications
apple_id: DTS40017251
resource_type: Technical Note
platform: watchOS|Xcode Developer Tools
topic: null
technology: WatchKit
published: '2018-05-15'
source_url: https://developer.apple.com/library/archive/technotes/tn2424/_index.html
archived_at: '2026-07-27T06:57:05.430604Z'
---
> 导航：[总目录](../../README.md) · [technotes](../../_indexes/technotes.md)



Technical Note TN2424

# Project Configuration Reference for watchOS 4 Applications

This document discusses the proper configuration of a WatchKit extension and Watch app when added to an existing Xcode project. Refer to this document if you have made a change to your project which is causing your Watch app to no longer run, or if you are encountering validation errors related to the Watch app when submitting your app.

If you are just getting started with WatchKit, refer to [Adding a Watch App to Your iOS Project](https://developer.apple.com/library/watchos/documentation/General/Conceptual/WatchKitProgrammingGuide/ConfiguringYourXcodeProject.html) in the Apple Watch Programming Guide for the steps to add a Watch app to your existing project.

[The Watch App](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvkeqrk7k5aviq2il5avaua)[Information Property List](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvkeqrk7k5aviq2il5avaubnjfhemt2sjvaviskpjzpvauspkbcvevczl5gesu2u)[Build Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvkeqrk7k5aviq2il5avaubnijkustcel5jukvcujfheouy)[Resources](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvkeqrk7k5aviq2il5avaubnkjcvgt2vkjbukuy)[The WatchKit Extension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvkeqrk7k5aviq2ijnevix2flbkektstjfhu4)[Information Property List](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvkeqrk7k5aviq2ijnevix2flbkektstjfhu4lkjjzde6usnifkest2ol5ifet2qivjfiwk7jrevgva)[Build Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvkeqrk7k5aviq2ijnevix2flbkektstjfhu4lkckveuyrc7kncvivcjjzdvg)[The iOS App](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvkeqrk7jfhvgx2bkbia)[Dependencies](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvkeqrk7jfhvgx2bkbic2rcfkbcu4rcfjzbusrkt)[Appendix A: Retrieving Device Logs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewugsbrfvavaucfjzceswc7ifpv6usfkrjesrkwjfheox2eivlesq2fl5ge6r2t)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytomrvgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## The Watch App

The Watch app is the actual app that the user launches from the Apple Watch home screen. It contains only the resource files associated with your app’s user interface and it works in tandem with your WatchKit extension. The Watch app target does not contain any of your code; instead an Xcode provided binary is inserted into the Watch app bundle at build time. Being an app bundle, the Watch app must have a unique bundle identifier and it must be code signed. During installation the Watch app bundle is copied to the paired watch. The watch validates the bundle's code signature, information property list, and executable. If your Watch app fails to install on the watch, the problem is most likely caused by the incorrect configuration of your Watch app or WatchKit extension target. Additional information about the error which triggered the installation failure is logged to the paired iPhone's console. See Retrieving Device Logs.

### Information Property List

The Watch app must have an associated information property list. One is created for you by default when adding a Watch app to your project. By default it can be found under the folder named <Target Name> in the project navigator where <Target Name> is the name of your Watch app. Certain information property list keys are invalid for Watch apps and will produce a verification failure upon install. The offending key will be logged to the paired iPhone's device console.

__Figure 1__  Information property list for a properly configured Watch app target.

> 原归档配图未能恢复：`tn2424_Figure_1.png`

- __Bundle Identifier (CFBundleIdentifier)__: Should be set to `$(PRODUCT_BUNDLE_IDENTIFIER)`.
- __Bundle versions string, short (CFBundleShortVersionString)__: The value for this key must match the corresponding value in the containing iOS app's information property list.
- __Bundle version (CFBundleVersion)__: The value for this key must match the corresponding value in the containing iOS app's information property list.
- __WKCompanionAppBundleIdentifier__: The value for this key must match the bundle identifier of the containing iOS app.
- __WKWatchKitApp__: The value for this key must be YES.

__Note:__ The information property list for a Watch app should not contain the __CFBundleSupportedPlatformsKey__. It will be automatically added with a value of WatchOS at build time.

### Build Settings

Because the Watch app does not contain any code, most build settings are ignored.

__Figure 2__  Build settings for a properly configured Watch app target.

> 原归档配图未能恢复：`tn2424_Figure_2.png`

- __Product Bundle Identifier__: Must be a unique reverse DNS string that is prefixed with the containing iOS app's bundle identifier. For example, if your iOS app has the bundle identifier `com.example.apple-samplecode.WatchKit-Catalog`, then the Watch app's bundle identifier should be `com.example.apple-samplecode.WatchKit-Catalog.watchkitapp`.
- __Architectures__: Must be set to `Standard architectures`.
- __Base SDK__: Must be set to `Latest watchOS`.
- __Supported Platforms__: Must be set to `watchOS`.
- __Valid Architectures__: Must contain `armv7k`.
- __Info.plist File__: Must be the project relative path to the information property list for the Watch app.
- __watchOS Deployment Target__: Must be set to `watchOS 2.0` or later.
- __Asset Catalog App Icon Set Name__: Must be set to the name of the app icon set in the asset catalog. The default name is `AppIcon`.
- __Default Module__: Interface Builder uses this setting when compiling storyboards that reference Swift class names. The value must match the __Product Module Name__ of the WatchKit extension.
- __TARGETED_DEVICE_FAMILY__: Must be set to `4`. This is a User-Defined build setting that is automatically created by the Xcode templates.

### Resources

A storyboard and asset catalog must be associated with your Watch app target. The asset catalog associated with your Watch app target must contain the icons for the Watch app and should not be associated with any other target in your project, to avoid duplicating resources. Additional resources that you want to include in the Watch app bundle must either be included in the asset catalog or be associated with the Watch app target.

__Figure 3__  You can modify the target associations for a resource under the Target Membership pane of the File Inspector.

> 原归档配图未能恢复：`tn2424_Figure_3.png`

__Note:__ Images displayed on the Apple Watch should use retina assets (@2x). See [Images](https://developer.apple.com/watch/human-interface-guidelines/icons-and-images/) in the Apple Watch Human Interface Guidelines.

__Note:__ Images created with some third-party graphics editing software may fail to load on the watch. If you notice images missing when running your application on the watch, re-export the affected images with Preview or move them into the Watch app's asset catalog.

[Back to Top](#)

## The WatchKit Extension

The WatchKit extension contains the code for managing content, responding to user interactions, and updating your user interface. It is packaged inside the Watch app bundle. Like all extensions, the WatchKit extension must have a unique bundle identifier and it must be code signed. Validation errors related to the WatchKit extension will cause the Watch app to fail to install. Additional information about the error which triggered the installation failure is logged to the paired iPhone's console. See Retrieving Device Logs.

### Information Property List

The WatchKit extension must have an associated information property list. One is created for you by default when adding a Watch app to your project. By default it can be found under the folder named <Target Name> in the project navigator where <Target Name> is the name of your WatchKit extension.

__Figure 4__  Information property list for a properly configured WatchKit extension target.

> 原归档配图未能恢复：`tn2424_Figure_4.png`

- __Bundle Identifier (CFBundleIdentifier)__: Should be set to `$(PRODUCT_BUNDLE_IDENTIFIER)`.
- __Bundle versions string, short (CFBundleShortVersionString)__: The value for this key must match the corresponding value in the containing iOS app's information property list.
- __Bundle version (CFBundleVersion)__: The value for this key must match the corresponding value in the containing iOS app's information property list.
- __WKAppBundleIdentifier__: The value for this key must match the bundle identifier of the Watch app.
- __NSExtensionPointIdentifier__: The value for this key must be `com.apple.watchkit`.

### Build Settings

__Figure 5__  Build settings for a properly configured WatchKit extension target.

> 原归档配图未能恢复：`tn2424_Figure_5.png`

- __Product Bundle Identifier__: Must be a unique reverse DNS string that is prefixed with the iOS app's bundle identifier or the Watch app's bundle identifier. For example, if your Watch app has the bundle identifier `com.example.apple-samplecode.WatchKit-Catalog.watchkitapp`, then the WatchKit extension's bundle identifier should be `com.example.apple-samplecode.WatchKit-Catalog.watchkitapp.watchkitextension`.
- __Architectures__: Must be set to `Standard architectures`.
- __Base SDK__: Must be set to `Latest watchOS`.
- __Supported Platforms__: Must be set to `watchOS`.
- __Valid Architectures__: Must contain `armv7k`.
- __Info.plist File__: Must be the project relative path to the information property list for the WatchKit extension.
- __watchOS Deployment Target__: Must be set to `watchOS 2.0` or later.
- __TARGETED_DEVICE_FAMILY__: Must be set to `4`. This is a User-Defined build setting that is automatically created by the Xcode templates.
[Back to Top](#)

## The iOS App

The iOS application must include the Watch app target as a dependency. The Watch app product must also be copied into the iOS application's bundle at build time.

### Dependencies

__Figure 6__  Build phases for an iOS app that includes a Watch app.

> 原归档配图未能恢复：`tn2424_Figure_6.png`

[Back to Top](#)

## Appendix A: Retrieving Device Logs

Error messages relating to installation failures on the Watch are sent over to the paired iPhone, where they are logged to the iPhone's device console. To view the device console:

1. Connect the iPhone and open Xcode.
2. Choose Window > Devices and Simulators from the menu.
3. Under the DEVICES tab in the left column, select the iPhone.
4. To see the device console, click the up-triangle at the bottom left of the right hand panel to show the device console.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-05-15 | Updated for watchOS 4 and Xcode 9. |
| 2016-05-23 | New document that describes the proper configuration for a project with a watchOS 2 app. |
