---
title: How to reproduce bugs reported against App Store submissions
apple_id: DTS40012028
resource_type: QA
platform: iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2016-02-18'
source_url: https://developer.apple.com/library/archive/qa/qa1764/_index.html
archived_at: '2026-07-18T02:34:39.928829Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1764

# How to reproduce bugs reported against App Store submissions

## Q:  I have reports of a bug in an app I submitted to the App Store, but I can't reproduce it with Xcode. How can I build my app so that it matches the App Store version and reproduces the issue?

A: To reproduce a bug that App Review or your users are seeing you need to be sure that you are testing the __exact__ build of the app that you submitted to the App Store.

If there are bugs or [undefined behavior](http://blog.llvm.org/2011/05/what-every-c-programmer-should-know_14.html) in your code, compiler optimizations may cause the app you submitted to the App Store to behave differently than any test builds made with different build settings.

Using Xcode's [Archive](https://developer.apple.com/library/ios/recipes/xcode_help-scheme_editor/Articles/SchemeArchive.html) feature, you can be sure you are testing the __exact__ same build of your app that you plan to publish to the App Store.

In Xcode choose "Archive" from the "Product" menu to archive a build of your app. You can find the archive in the Archives tab in the Organizer window.

With Ad-Hoc distribution, you can test variants of your application that are built locally by Xcode. Applications built with Bitcode enabled can be exported for Ad-Hoc distribution. However, since final compilation of Bitcode happens on the App Store you should also test the binaries created by the store using TestFlight.

1. Follow the steps listed under [Exporting Your App for Testing Outside the Store](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/TestingYouriOSApp/TestingYouriOSApp.html#//apple_ref/doc/uid/TP40012582-CH8-SW17) in the App Distribution Guide to export your archive for Ad-Hoc distribution. Xcode will create an iOS App file (a file with an `.ipa` filename extension) that you can install on your device.
2. It is best to install your app with iTunes and launch it __without__ Xcode for quality assurance testing. Launching with Xcode is good during development because it's faster, but it can mask issues with your app. Running your app with Xcode's debugger attached also masks problems like "[watchdog crashes](https://developer.apple.com/library/ios/#qa/qa1592/_index.html)" that can happen if an app takes too long to launch.

   Delete any builds of the app from your device. Then follow the steps listed under [Installing Your App on Test Devices Using iTunes](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/TestingYouriOSApp/TestingYouriOSApp.html#//apple_ref/doc/uid/TP40012582-CH8-SW6) in the App Distribution Guide to sync the `.ipa` file to your testing device.
3. After testing the build to your satisfaction, you can submit it to the App Store [by following these steps](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/UploadingYourApptoiTunesConnect/UploadingYourApptoiTunesConnect.html).

With TestFlight beta testing, you can distribute a prerelease build of your application to a wider audience to collect feedback prior to submitting it for release in the App Store. TestFlight offers a testing environment that most closely matches the real world environment of a customer's device. For application's built with Bitcode, distributing with TestFlight is the only way to test the final build of your application that is created by the App Store.

Refer to the [TestFlight Beta Testing](https://developer.apple.com/library/ios/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/BetaTestingTheApp.html) chapter in the iTunes Connect Developer Guide for steps to upload your archive for TestFlight beta testing, invite beta testers, and distribute prerelease builds.

After testing the build to your satisfaction, you can submit it to the App Store [by following these steps](https://developer.apple.com/library/ios/documentation/LanguagesUtilities/Conceptual/iTunesConnect_Guide/Chapters/SubmittingTheApp.html#//apple_ref/doc/uid/TP40011225-CH33).

Prior to distributing a new version of your application, you should test its full functionality. Seemingly unrelated code changes can have unintended effects on parts of your application that you don't expect. This section lists a few scenarios to focus testing on, but don't let these define the full extent of your testing!

It is easy to accidentally introduce dependencies on previously created data being present as you iteratively develop and test your app. Xcode's app install process is optimized for development, but is slightly different than how iTunes and the App Store install apps. Prior to distributing a new version of your application, thoroughly test launching from a clean installation - where no data previously created by your application is present on the device.

1. Remove previous builds of your application from the testing device. You can delete an application and its container from the iOS home screen or using [Xcode's Devices window](https://developer.apple.com/library/ios/recipes/xcode_help-general/AbouttheDevicesWindow/AbouttheDevicesWindow.html).
2. If your application uses a shared app group container to store common data files, you should also remove all other applications in that app group from the testing device. Shared containers are not deleted until all applications in the app group are removed from the device.
3. Keychain data previously created by your application may not be deleted when the app is removed from the device. To clear its keychain, an application can call the [SecItemDelete](https://developer.apple.com/library/ios/documentation/Security/Reference/keychainservices/#//apple_ref/c/func/SecItemDelete) API with a query that matches all existing items. You may find it more convenient to prepare a small utility application that you can quickly install on your test device for this task. This utility application must have the same bundle identifier as your real application to modify its keychain.

Unless this is the a new application, the majority of your customers will be upgrading from a previous release. Test that upgrading from previously released build of your application works smoothly and, if you have made changes to your file format, that existing data is successfully migrated. See [Testing iOS App Updates](https://developer.apple.com/library/ios/technotes/tn2285/_index.html) for a discussion of testing an update to an iOS app that has already been deployed through the App Store.

The behavior of the network on which the problem is reproducing may be significantly different than the network you used during development. Test that your application launches and [remains responsive](https://developer.apple.com/library/ios/qa/qa1693/_index.html#//apple_ref/doc/uid/DTS40010599) even under poor network conditions. You can use the __Network Link Conditioner__ on your device to test how your app behaves on a slow or unreliable internet connection. The Network Link Conditioner can be activated by navigating to `Settings > Developer > Network Link Conditioner` on your testing device.

__If a problem reproduces in an Ad Hoc build__ you may also be able to reproduce the problem by running the Release configuration of your application in Xcode. This will allow Xcode's debugger to attach to your application. Due to the optimizations applied to release builds debugger functionality may be limited however.

1. From the Scheme toolbar menu, choose a scheme.
2. From the same menu, choose Edit Scheme to display the scheme dialog.
3. In the left column, select Run.
4. From the Build Configuration pop-up menu, choose Release.
5. Click Close.
6. Click the Run button or choose Product > Run.

__Figure 1__  The Run action panel for a scheme.

!!

__If a problem only reproduces in a build distributed via TestFlight__ you'll need to analyze Crash Logs and Console output from the device to debug it. [Debugging Deployed iOS Apps](https://developer.apple.com/library/ios/qa/qa1747/) explains how to gather this information. See [Understanding and Analyzing iOS Application Crash Reports](https://developer.apple.com/library/ios/#technotes/tn2151/_index.html) and the [Understanding Crash Reports on iOS](https://developer.apple.com/videos/wwdc/2010/?id=317) WWDC Session for tips on interpreting it.

Consider adopting Activity Tracing in your application. Activity Tracing is a collection of low-overhead APIs that allow your application to emit various kinds of trace messages as it runs. If your application crashes, the most recent trace messages are included in the generated crash report. Crash reports with activity tracing information can provide deeper insight into the cause of a crash than backtraces alone. For more information, watch the [Fix Bugs Faster Using Activity Tracing](https://developer.apple.com/videos/wwdc/2014/?id=714) WWDC session.

If you are still unable to reproduce a crash, follow the steps in [How to Match a Crash Report to a Build](https://developer.apple.com/library/ios/qa/qa1765/) to verify that you are testing the build that exhibited the crash.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-02-18 | Updated testing steps to discuss TestFlight and Activity Tracing. Added a discussion of common things to test. |
| 2013-04-02 | Editorial update. |
| 2013-01-10 | This document was previously titled, "Testing Workflow with Xcode's Archive feature". |
| 2012-05-22 | Added more troubleshooting information. |
| 2012-03-20 | New document that describes how to build and archive your app in order to reproduce issues only seen after submission to the App Store |

