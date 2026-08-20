---
title: What's New in Xcode 4
apple_id: TP40013516
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/00-Introduction/Introduction.html
archived_at: '2026-07-18T02:58:39.562305Z'
---
> 导航：[总目录](../README.md) · [releasenotes](../_indexes/releasenotes.md)


[Next](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_6.html)

# What’s New in Xcode 4

Xcode is the complete developer toolset used to create applications for Mac, iPhone, and iPad. The Xcode development environment bundles the Instruments analysis tool, iOS Simulator, and OS frameworks in the form of iOS SDKs and OS X SDKs.

[Xcode 4.6.3](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_6.html#//apple_ref/doc/uid/TP40012895-SW5) fixes an issue where debugging in the iOS Simulator could hang on OS X 10.8.4.

[Xcode 4.6.2](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_6.html#//apple_ref/doc/uid/TP40012895-SW4) is a maintenance release responding to reported developer issues and Apple QA testing.

[Xcode 4.6.1](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_6.html#//apple_ref/doc/uid/TP40012895-SW3) supports development with OS X 10.8.3 SDK and provides compatibility for ARC in projects targeting OS X 10.6.

Xcode 4.6 adds support for the iOS 6.1 SDK and includes the following additional features.

For the compiler:

- Compilation warnings are added which assist in finding bugs when using ARC and weak references.
- `otool` is enhanced to support disassembly of Intel AVX instructions.
- The LLVM compiler now supports C++11 “user defined literals” and “unrestricted unions” features.
- The static analyzer has enhanced cross-function analysis for C++ and Objective-C methods.

For the debugger:

- LLDB has been enhanced to read metadata from the Objective-C runtime.
- LLDB has improved support for stepping over inlined functions
- LLDB now prints function argument information in backtraces by default.
- LLDB now supports “thread return,” temporary breakpoints, and a variety of aliases to add common shortcuts from GDB.
- The elements of `NSArray` and `NSDictionary` objects can now be inspected in the Xcode debugger.

For information on all releases, check in the release chapters: [New Features in Xcode by Release](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmzvfvjvomjr).

Xcode 4.6 requires a Mac running OS X v10.7 or OS X v10.8, and includes iOS 6.1 SDK and OS X 10.8 SDK. To develop apps targeting prior versions of iOS or OS X, see [About SDKs and the iOS Simulator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmzvfvjvomq).

The iOS and Mac Developer Programs provide access to the App Store, additional support and documentation, and provisioning resources to enable testing and deployment on an iPhone, iPod Touch, or iPad device. For more information visit:

- iOS: [http://developer.apple.com/programs/ios/](https://developer.apple.com/programs/ios/)
- Mac: [http://developer.apple.com/programs/mac/](https://developer.apple.com/programs/mac/)

For discussions about any Apple developer software, including prerelease products, visit the Apple Developer Forums at [http://devforums.apple.com/](http://devforums.apple.com/).

For the latest security information visit [http://support.apple.com/kb/HT1222](http://support.apple.com/kb/HT1222).

For more detailed information please see the complete Xcode release notes, available from the Help menu.

A software development kit (SDK) is a collection of frameworks (libraries, headers, and resources) that represent the API for a specific iOS or OS X version. Most of the functionality your app gets from an SDK is actually provided by the host operating system, which makes the right Base SDK and OS Deployment Target settings critical for app compatibility. Xcode automates this configuration for you, building with the latest SDK and targeting the latest OS by default.

If your app doesn’t require the latest OS features, you can configure it to run on a previous version of iOS or OS X version via the OS Deployment Target option in the Xcode Project settings. If your project was created in a much older version of Xcode, you can let Xcode update your project. When you do, Xcode automatically sets the Base SDK to Latest in your build settings. You use the Xcode Project Modernization feature to perform this task, see the description in [Project Modernization](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_1.html#//apple_ref/doc/uid/00100-SW4) for more details.

For iOS, Xcode automatically switches between the iOS Simulator SDK and the device SDK, depending on where you intend to run your app. You don’t need to select these settings manually.

You obtain Xcode 4.6 from the Mac App Store, it is a free download that installs directly into the Applications folder. By default, Xcode downloads developer documentation in the background for offline reading, and automatically downloads documentation updates as well. This behavior can be changed after installation via the Documentation tab of the Downloads preferences pane.

Xcode 4.6 can coexist on a Mac with previous versions of Xcode.

Chapter articles are listed by major revision. Minor update release information is appended in the chapter for the major revision.

__Xcode 4.6__ adds support for development on iOS v6.1.

Relevant Chapter: [New Features in Xcode 4.6](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_6.html#//apple_ref/doc/uid/TP40012895-SW1)

__Xcode 4.5__ adds support for development on iOS v6.0.

Relevant Chapter: [New Features in Xcode 4.5](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_5.html#//apple_ref/doc/uid/TP40012559-SW1)

__Xcode 4.4__ adds support for new Objective-C language features and supports development on OS X v10.8 Mountain Lion.

Relevant Chapter: [New Features in Xcode 4.4](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_4.html#//apple_ref/doc/uid/TP40011649-SW1)

__Xcode 4.3__ adds enhancements to Xcode installation, improves operations and workflow, and support development for iOS v5.0.

Relevant Chapter: [New Features in Xcode 4.3](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_3.html#//apple_ref/doc/uid/1006-SW1)

__Xcode 4.2__ adds enhancements to the features and workflow of Xcode 4.1 to support development for iOS v5.0.

Relevant Chapter: [New Features in Xcode 4.2](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_2.html#//apple_ref/doc/uid/00200-SW1)

__Xcode 4.1__ adds enhancements to the features and workflow of Xcode 4.0 and, when running on OS X Lion, implements user interface features standard in OS X Lion such as full-screen windows.

Relevant Chapter: [New Features in Xcode 4.1](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_1.html#//apple_ref/doc/uid/00100-SW1)

For short tutorials that walk you through some of the most commonly used features of Xcode, see either:

- _[Start Developing iOS Apps Today (Retired)](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/index.html#//apple_ref/doc/uid/TP40011343)_
- _[Start Developing Mac Apps Today](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapOSX/index.html#//apple_ref/doc/uid/TP40012262)_

These documents provide the perfect starting point for iOS and Mac app development. Follow either road map to learn how to get and use Xcode to create your first app. You will learn how to use Xcode to test and debug your source code, analyze and improve your app’s performance, perform source control operations, and archive and submit your app to the App Store.

To learn about using Xcode 4 in detail, see _[Xcode Overview](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/index.html#//apple_ref/doc/uid/TP40010215)_.

To learn more about the tasks and workflow required to develop and distribute Mac or iOS apps, see _App Distribution Guide_.

[Next](https://developer.apple.com/library/archive/releasenotes/IDEs/whatsnewxcode4/Articles/xcode_4_6.html)

