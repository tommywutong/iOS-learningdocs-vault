---
title: 'What''s New in Xcode 3.2.2'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2010/04/whats-new-in-xcode-3-2-2/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:58e3fe949f3836ce'
translated: false
---

> 原文：[What's New in Xcode 3.2.2](https://oleb.net/blog/2010/04/whats-new-in-xcode-3-2-2/)　·　Ole Begemann

# What's New in Xcode 3.2.2

After [yesterday’s post about the changes in iPhone SDK 3.2](https://oleb.net/blog/2010/04/whats-new-in-iphone-sdk-3-2/), let’s have a look at what’s new in Xcode 3.2.2. Contrary to the minimal jump in the version number from 3.2 to 3.2.2, Apple has made some major improvements for iPhone/iPad developers.

# Support for iPad development and universal apps

This is a given. After all, the iPad launch is the sole reason for this release. Xcode 3.2.2 includes new project templates for iPad apps and has a menu command (Project \> Upgrade Current Target for iPad…) that helps you get the project settings setup correctly when you want to add iPad support to your existing iPhone project. The Upgrade command gives you two options:

1. Upgrade your existing iPhone app to a universal application that runs on both iPhone and iPad. Customers buy such an app once and can install it on multiple devices. The code that runs on the iPhone and iPad is identical and device-dependent branching in your code happens at runtime.
2. Create a separate iPad target based on your existing iPhone target. Both targets will use much of the same codebase but in the end, you compile two separate apps. Customers who want to use both the iPhone and iPad-optimized apps have to buy both of them. Since you end up with different binaries, device-dependent branching in your code can be handled with conditional compilation directives.

Apple has explained this process very well in the _iPad Programming Guide_ so I’m not gonna go into more detail here. See [Creating a Universal Application](http://developer.apple.com/iphone/library/documentation/General/Conceptual/iPadProgrammingGuide/StartingYourProject/StartingYourProject.html#//apple_ref/doc/uid/TP40009370-CH9-SW2) or [Using a Single Xcode Project to Build Two Applications](http://developer.apple.com/iphone/library/documentation/General/Conceptual/iPadProgrammingGuide/StartingYourProject/StartingYourProject.html#//apple_ref/doc/uid/TP40009370-CH9-SW8), respectively.

# Build and Archive

The new Build \> Build and Archive command builds your app as usual, creates an `.ipa` file (the zip archive of your app bundle you need to create to submit your app to iTunes Connect) and then archives the app bundle, the `.ipa` file and the associated `.dSYM` file (containing the debug symbols you need to debug crash logs) in a subfolder of `~/Library/MobileDevice/Archived Applications`. These archives also appear in the new Archived Applications view in the Organizer.

[![Xcode 3.2.2 Archived Applications folder](https://oleb.net/media/xcode-3-2-2-archived-applications-folder.png)](https://oleb.net/media/xcode-3-2-2-archived-applications-folder.png)

<sub>An application build in the Finder as archived by Xcode 3.2.2.</sub>

[![/media/xcode-3-2-2-organizer-archived-applications.png](https://oleb.net/media/xcode-3-2-2-organizer-archived-applications.png)](https://oleb.net/media/xcode-3-2-2-organizer-archived-applications.png)

<sub>/media/xcode-3-2-2-organizer-archived-applications.png.</sub>

Unless you already have another automated method in place to archive your distribution builds (such as a custom build script), I encourage you to use Build and Archive for all Distribution builds, both for Ad Hoc and App Store distribution. That way, you won’t have to manually copy the all-important `.dSYM` file to a safe location and it also saves you the hassle of manually creating the `.ipa` zip archive. Whenever you want to distribute an Ad Hoc build to your beta testers, just set your build config Distribution, choose Build and Archive, and you’re done.

# iTunes Connect integration: Build validation and uploading

The Organizer now also helps you with the next logical step after you have created a distribution build: sharing your Ad Hoc app with beta testers or uploading the final version to iTunes Connect. Take another look at the screenshot of the Organizer window above and note the three buttons at the bottom:

- _Share Application_ lets you sign the build with an Ad Hoc distribution certificate and then save the signed `.ipa` file to disk or put it directly into an e-mail for distribution to your beta testers. Very handy.
- _Validate Application_ will, in [Apple’s words](http://developer.apple.com/iphone/library/releasenotes/General/RN-iPhoneSDK-3_2/index.html#//apple_ref/doc/uid/TP40009477-CH1-SW16), run all of the validation tests that will be run upon submission to the App Store so that you can fix any problems before submitting your app. It’s not quite clear to me what exactly these tests consist of, but it will definitely give you an error message if you failed to include an icon in your app (or if it has the wrong size) or if your code signing identity does not match the app’s bundle identifier in iTunes Connect. When I first read about this feature, I was very excited because I figured that the tests also include Apple’s apparently automated testing for use of undocumented APIs, but now I doubt this is the case. Does anybody know more?
- Finally, _Submit Application to iTunes Connect_ will sign the app with your App Store code signing identity and upload the binary directly to Apple. Before you do this, you must have set up the application with all its metadata (screenshots, 512 x 512 icon, keywords) in iTunes Connect (this is also true for the _Validate Application_ step). Make especially sure that all your keywords are correct because you cannot change them afterwards unless you reject the binary.

# Transfer your iPhone developer identity to a new computer

With all the certificates and provisioning profiles Apple requires iPhone developers to manage, it can be quite a hassle to reinstall everything correctly after switching to a fresh install of OS X. In Xcode 3.2.2, there is a new Developer Profile item in the Organizer window that allows you to export all your provisioning profiles and code signing certificates into a single file which you can then import on a new computer with a single click.

[![Developer Profile view in the Xcode 3.2.2 Organizer](https://oleb.net/media/xcode-3-2-2-organizer-developer-profile.png)](https://oleb.net/media/xcode-3-2-2-organizer-developer-profile.png)

<sub>Developer Profile view in the Xcode 3.2.2 Organizer.</sub>

# Redesigned documentation

Finally, the 3.2 API documentation has gotten a new look. I quite like the design. Functionality-wise, the help system seems to be unchanged.

[![Xcode 3.2.2 API Documentation view](https://oleb.net/media/xcode-3-2-2-documentation.png)](https://oleb.net/media/xcode-3-2-2-documentation.png)

<sub>Xcode 3.2.2 API Documentation view.</sub>

**Update April 7, 2010:** Message from Jens Ayton:

> The compilers have also been updated. Clang is now listed as “LLVM Compiler 1.0.2” (corresponding to something between 2.6 and 2.7 in the public LLVM project). GCC is still identified as “GCC 4.2” (“gcc version 4.2.1 (Apple Inc. build 5659)” according to gcc -v).
> 
> Oh, and distcc has been updated so distributed builds now work (for the first time in Snow Leopard).

Thanks for the additions, Jens. Maybe I should have titled my post “What’s new in the Xcode UI” since I haven’t really looked under the hood.
