---
title: How to reproduce bugs reported against Mac App Store submissions
apple_id: DTS40013062
resource_type: QA
platform: Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2017-06-28'
source_url: https://developer.apple.com/library/archive/qa/qa1778/_index.html
archived_at: '2026-07-18T02:34:41.472397Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1778

# How to reproduce bugs reported against Mac App Store submissions

## Q:  I have reports of a bug in a macOS app I submitted to the Mac App Store, but I can't reproduce it with Xcode. How can I build my app so that it matches the Mac App Store version and reproduces the issue?

A: To reproduce a bug that Mac App Review or your users are seeing, you need to be sure that you are testing the __exact__ build of the app that you submitted to the Mac App Store, in a minimally-privileged environment.

The most common reason for an app to work in your test environment but fail in Mac App Review or on a user's system is your test environment giving the app more privileges or including optional system components. The simplest way to rule this out is to test your app on a Guest account, ideally on a fresh install of the OS indicated in any crash or bug reports.

If there are bugs or [undefined behavior](http://blog.llvm.org/2011/05/what-every-c-programmer-should-know_14.html) in your code, compiler optimizations may cause the app you submitted to the Mac App Store to behave differently than any test builds made with different build settings.

Using Xcode's Archive feature, you can be sure you are testing the __exact__ same build of your app that you plan to publish to the Mac App Store.

To [create an archived build](http://help.apple.com/xcode/mac/current/#/devf37a1db04) that you can both test and submit:

__1)__ In Xcode, choose `Product > Archive` to archive a build of your app. You can find the archive in the Archives tab of the Organizer window as shown in Figure 1.

If you have trouble with this step, follow the directions in [Technical Note, TN2215, Troubleshooting application archiving in Xcode](https://developer.apple.com/library/mac/technotes/tn2215/).

__Figure 1__  The MyProject archive in the Archives organizer.

!!

__2)__ Deploy the build by selecting it in the Archives organizer and clicking `Export`, then `Export as macOS App` in the sheet that appears. Proceed to export it to the appropriate location.

__Figure 2__  Select Export as a macOS App in the sheet to export the MyProject archive.

!!

__3)__ Run the app on a Guest account, ideally on a fresh install of the OS indicated in any crash or bug reports.

If you have problems installing a provisioning profile on your test system so you can run your test app, try the troubleshooting information in [QA1759: Installing Production Provisioning Profiles](https://developer.apple.com/library/mac/qa/qa1759/).

Once you can reproduce a problem, you will need to debug it. After launching your archived build, you can use Xcode's debugger on it by choosing `Debug > Attach to Process`, see [Debug an app or process that is already running](http://help.apple.com/xcode/mac/current/#/devaeaf4813e) for more information. If a problem only reproduces in an optimized build, you may find that Xcode's debugger sometimes behaves oddly. This is because compiler optimizations make it difficult to translate back from machine code to a line number or variable name in source code. Do not be afraid to fall back on "caveman debugging" by using `NSLog` or `printf` if you are unsure what a value really is. For more information on writing rich `NSLog` statements, see [QA1669: Improved Logging in Objective-C](https://developer.apple.com/library/ios/qa/qa1669/) for more information.

For more information on debugging at the assembly level, see [TN2124: Mac OS X Debugging Magic](https://developer.apple.com/library/mac/technotes/tn2124/).

If you are still unable to reproduce a crash, follow the steps in [QA1765: How to Match a Crash Report to a Build](https://developer.apple.com/library/mac/qa/qa1765/) to verify that you are testing the build that exhibited the crash.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-06-28 | Updated for Xcode 8. |
| 2013-01-24 | New document that describes how to build and test your macOS app in order to reproduce issues only seen after submission to the Mac App Store. |

