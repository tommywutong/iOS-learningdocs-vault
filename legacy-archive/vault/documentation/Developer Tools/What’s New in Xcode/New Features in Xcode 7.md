---
title: What’s New in Xcode
apple_id: TP40004626
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/WhatsNewXcode/Chapters/xcode_7_0.html
archived_at: '2026-07-15T07:27:10.559733Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [What’s New in Xcode](What%27s%20New%20in%20Xcode%209.md)


[Next](New%20Features%20in%20Xcode%206.md)[Previous](New%20Features%20in%20Xcode%208.md)

# New Features in Xcode 7

- [Xcode 7.0](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbsfvjvooi) includes SDKs for OS X version 10.11, iOS 9, watchOS 2, and other enhancements.
- [Xcode 7.0.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbsfvjvomjr) is a maintenance release that includes refinements to support app thinning.
- [Xcode 7.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbsfvjvomjt) adds support for developing on new iOS devices and the new Apple TV.
- [Xcode 7.1.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbsfvjvomjw) is a maintenance update with bug fixes and performance improvements.
- [Xcode 7.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbsfvjvomjq) includes support for iOS 9.2, OS X 10.11.2, tvOS 9.1, and watchOS 2.1, as well as other enhancements.
- [Xcode 7.2.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbsfvjvomjy) is a maintenance update with bug fixes and performance improvements.
- [Xcode 7.2.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbsfvjvomjy) includes updated SDK support as well as many feature improvements.
- [Xcode 7.3.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbsfvjvomrq) is a maintenance update with bug fixes and performance improvements.

With Xcode 7, the Xcode development tools have expanded to support the new watchOS 2 platform in addition to iOS 9 and OS X El Capitan, with a host of new features to support making your development, testing, debugging, and deployment more seamless and efficient. Xcode 7 allows you to achieve things that weren’t possible before, such as enabling you to detect memory corruption just before it happens, test your app UI while reporting on the testing coverage, or ensure that apps and products downloaded to users’ devices have a sensible footprint and do not consume too many precious resources unnecessarily.

Xcode 7 enables you to to create products that are tailored for each Apple device’s unique platform. Whether that’s implementing glances to help your users stay up to date right from their Apple Watch, or size classes, which let you take advantage of the wide array of configurations of a MacBook Air, an iPhone, or an iPad, Xcode provides the tools to quickly translate your ideas into a reality that fits the target perfectly.

Xcode 7 requires a Mac running OS X version 10.10.4 or later. It includes SDKs for watchOS 2.0, iOS 9, and OS X version 10.11.

Xcode 7 includes the following highlighted features.

__Now everyone can run and test their own app on a device—for free.__ You can run and debug your own creations on a Mac, iPhone, iPad, iPod touch, or Apple Watch without any fees, and no programs to join. All you need to do is enter your free Apple ID into Xcode. You can even use the same Apple ID you already use for the App Store or iTunes. Once you’ve perfected your app the Apple Developer Program can help you get it on the App Store.

See Launching Your App on Devices for detailed information about installing and running on devices.

Swift 2.0 takes the advanced object-oriented Swift programming language to the next level.

Swift 2.0 is modern, powerful, expressive, and easy to use. It extends Swift 1.2 with:

- __Error handling.__ Now you can create routines that throw, catch, and manage errors in Swift. You can surface and deal with recoverable errors, such as “file-not-found” or network timeouts. Swift 2.0 error handling interoperates transparently with `NSError`.
- __Availability.__ Availability features enable you to mark up methods with the OS that they are available on, providing compile time checking and preventing unavailable methods from being used. You can adopt new APIs while still deploying back to older OS versions. Compile-time errors are provided when you’re using an API that isn’t guaranteed to be available on the deployment target.
- __Testability.__ With testability, you are now able to write tests of Swift 2.0 frameworks and apps without having to make all of your internal routines public. Use `@testable import {ModuleName}` in your test source code to make all public and internal routines usable by XCTest targets, but not by other framework and app targets.
- __Protocol extensions.__ You can now add methods and properties to any class that conforms to a particular protocol, allowing you to reuse more of your code. For example, in the standard library, instead of having to use global functions for all of the generic algorithms in the standard library (such as map, filter, and sort), those generic algorithms are now available as methods on all of the collection types.

The __Swift 1.2 to 2.0 migrator__ in Xcode 7 enables you to efficiently upgrade your existing Swift source code to take advantage of Swift 2.0.

The Swift migrator works with both projects and playgrounds.

See _The Swift Programming Language_ to learn more about the Swift programming language, and check the Revision History chapter for pointers to the updated Swift features.

Objective-C has been updated to enable it and Swift to work together more easily and efficiently. The new Objective-C language features include:

- __Generics.__  Allow you to specify type information for collection classes such as `NSArray`, `NSSet`, and `NSDictionary`. The type information improves Swift access when you bridge from Objective-C and simplifies the code you have to write.
- __Nullability annotation.__  Lets you indicate in Objective-C source when to expect a value to be nil or non-nil, smoothing the use of Objective-C frameworks and modules from Swift code.
- __KindOf.__  Objects declared as `__kindof` types express “some kind of `X`” to the compiler and can be used within generic parameters to constrain types to a particular class or its subclasses. Using `__kindof` allows constraints to be more flexible than an explicit class, and more explicit than just using `id`.

These new language features help the Objective-C/Swift interaction. They express more information to the compiler about your expectations in the code rather than in documentation, which provides a means for Xcode to inform you of problems earlier in the development cycle, before your code is run.

See _Using Swift with Cocoa and Objective-C_ for detailed information on Objective-C language features and how they interact with Swift.

Playgrounds, since their introduction with Swift in Xcode 6, have proven a great way to explore and prototype Swift code. With Swift 2.0, you can use playgrounds to help explain how to use an API or demonstrate a concept.

- __Playground authoring.__ Rich comments let you explain what is going on in your Swift code. They provide a simple Markdown-like syntax to let you control their appearance and are visually differentiated from the code, making a playground appear to the user in smaller, more easily consumable pieces. For details on playground rich comments, see _[Playground Reference](https://developer.apple.com/library/archive/documentation/Swift/Reference/Playground_Ref/Chapters/XCPlayground.html#//apple_ref/doc/uid/TP40014789)_ and look at the _Playground Markup Format Reference_.
- __Inline results.__ You can move the display of your code’s results from the timeline area to directly below the code that produces them. This makes the result of a line of code clearer to your audience. Inline results are also more configurable than the display in the timeline.
- __Resources.__ With the resource bundle, you can easily add images, sounds, and other data to your playground using the project navigator.
- __Auxiliary sources.__ Auxiliary sources let you move supporting code out of a playground, which helps you keep the message of the playground clearer. Additionally, auxiliary sources are compiled and execute more quickly.
- __Playground pages.__ New in Xcode 7, pages enable you to bundle related concepts together. A single playground can contain multiple, targeted pages, which lets you thread a narrative together.

See Playground Help for more information about using playground features.

With Xcode 7, you are developing apps for three diverse platforms that run on a variety of devices and configurations.

The devices can have widely different storage and display capabilities. You can deliver an optimized app to each platform device, supplying the functionality you intend without including unneeded resources, using new features supported in Xcode 7 and used by the iTunes App Store.

- __Bitcode.__ When you archive for submission to the App Store, Xcode compiles your app into an intermediate representation. The App Store then compiles the bitcode down into the 64- or 32-bit executables as necessary.
- __Slicing.__ Your artwork incorporated into the asset catalog can be tagged to indicate its suitability for the device that is targeted for installation when a user purchases and downloads your app into his or her device. Xcode supports organizing and tagging in the asset catalog so that the App Store can perform the slicing operation automatically. End users get just the resources needed for their device.
- __On-demand resources.__ For apps that need some content only after the initial download and installation, you can host the additional content for the app on the iTunes App Store repository. You tag these resources for their appropriate categories and control when these assets are downloaded. Xcode builds your app with information that allows it to fetch the resources when are needed, using asynchronous download and installation. See _[On-Demand Resources Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/index.html#//apple_ref/doc/uid/TP40015083)_ for more information.

See App Thinning (iOS, watchOS) in _App Distribution Guide_ for detailed information.

Xcode 7 includes new debugging and profiling features targeted at helping you make better apps for your customers.

- __Energy gauge for iOS.__ Xcode 7 brings insight into the energy usage of your iOS app with the energy gauge. iOS 9 has plumbed in the ability to track energy on a per-process basis, which is surfaced in the energy report. This is a great way to gain insight into how your app is affecting battery life. You can see unexpected behavior, such as high energy usage while your app should be just sitting idle or anomalous spikes in power consumption when you’re expecting a steady profile. Learn more about how to manage power for iOS apps in _[Energy Efficiency Guide for iOS Apps](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243)_.

  The debug gauges and their reports provide quick insight into your running app. When you see situations occur that require more detailed analysis, each gauge’s report includes a means to launch your running app into Instruments. With Xcode 7, the Instruments redesigned track view and UI are natural and easy to interact with. Gestures like “pinch-to-zoom” make navigating through your data smooth and informative. More information on the latest Instruments is available from _[Instruments User Guide](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/index.html#//apple_ref/doc/uid/TP40004652)_.
- __Address sanitizer.__ Xcode 7 can build your app with instrumentation designed to catch and debug memory corruption using the address sanitizer.

  Objective-C and C code is susceptible to memory corruption issues such as stack and heap buffer overruns and use-after-free issues. When these memory violations occur, your app can crash unpredictably or display odd behavior. Memory corruption issues are difficult to track down because the crashes and odd behavior are often hard to reproduce, and the cause can be far from the origin of the problem.

  You enable the address sanitizer in the build scheme. Once enabled, added instrumentation is built into the app to catch memory violations immediately, enabling you to inspect the problem right at the place where it occurs. Other diagnostic information is provided as well, such as the relationship between the faulty address and a valid object on the heap and allocation/deallocation information, which helps you pinpoint and fix the problem quickly.

  The address sanitizer is efficient—fast enough to be used regularly as well as with interactive applications. It is supported in OS X, in the Simulator, and on iOS devices.

Xcode 7 introduces UI testing as a major new feature of the existing XCTest framework. UI testing is implemented as an extension to the existing APIs and concepts in XCTest, making it easy to adopt for developers who have familiarity with Xcode’s testing features.

- __UI recording.__ Create your first UI test method by recording an interaction with your app. As you interact with your app, Xcode emits source code into your test method to find elements in the UI of your app, to access their properties, and to send them events.
- __Correctness and performance.__ XCTest now offers a rich set of features for locating elements in the UI of your app, for accessing elements’ properties, and for synthesizing events. The UI testing support in XCTest integrates with existing features for asserting conditions that must be true and in using baselines to monitor the performance of your app over time and across different devices.
- __Code coverage.__ Visualize the completeness of your test suite by enabling code coverage for your scheme. The code coverage pane in the test report shows which files, functions, and lines of code were exercised and, more importantly, which were not exercised. The source code editor can also show code coverage information inline, allowing you to see at a glance which lines—and parts of a line—the tests exercised.
- __Xcode Server.__ Xcode testing features are designed to integrate completely with Xcode Server, with which you can run tests on multiple devices, repeatedly, in a hands-off environment that allows consistency and better evaluation of both correctness and performance. New Xcode Server report formatting shows trends and regressions over repeated tests of a project throughout your development process.

See _[Testing with Xcode](../Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_ for more information about testing your app using Xcode testing features.

Xcode provides a way to analyze and use crash data submitted by users, with all the facilities of the debugger and your source code at hand.

Now, in Xcode 7, this feature is extended to include crash data from OS X apps, in addition to watchOS and iOS.

- __TestFlight.__ You distribute your app for beta testing to selected testers before you ship to customers, giving you the ability to get real-world feedback. Users can also elect to share reports on crashes with the App Store, where they are collected and symbolicated.
- __Crash reports.__ In the Xcode 7 Organizer window, click the Crashes tab to display a coalesced list of crash logs organized by the apps you’ve submitted. Each entry in the crash report tells you how often this crash was reported and where in the code it occurred. Click items in the crash report to present a historical backtrace of the crashed app, which you can transfer to the debug navigator and use to navigate directly to your source code in Xcode where the problem can be inspected and fixed.

See Analyzing Crash Reports in _App Distribution Guide_ for more information.

Xcode 7.0.1 is a maintenance release responding to reported developer issues. It includes refinements to support app thinning.

Xcode 7.1 adds support for new iOS devices and the new Apple TV. Xcode supports storyboards, unit and UI testing, playgrounds, and crash logs features for tvOS.

- Storyboards now support 3D Touch gestures such as Peek and Pop.

- Swift error breakpoints can be created in the Xcode debugger.

  Swift errors activate defined Swift error breakpoints when the error is thrown. You can edit Swift error breakpoint so that they are activated only for a specified Swift error type.

Xcode 7.1.1 is a maintenance update with bug fixes and performance improvements.

Xcode 7.2 includes support for iOS 9.2, OS X 10.11.2, tvOS 9.1, and watchOS 2.1, in addition to the following:

- The Xcode Crashes Organizer now displays crash reports originating from tvOS apps.

Xcode 7.2.1 is a maintenance update with bug fixes and performance improvements.

Xcode 7.3 requires a Mac running OS X version 10.11 or later. It includes updated support for iOS 9.3, watchOS 2.2, OS X version 10.11.4, and tvOS 9.2 as well as many feature improvements.

- __Swift 2.2__ provides improved warnings and diagnostics, improved compile times, updated features and improved interoperability with Objective-C.

  See the Xcode 7.3 release notes and _The Swift Programming Language (Swift 2.2)_ for details.
- __Code completion__ enhancements in the Xcode source editor help you enter symbols, methods, and property names with less typing. Code completion now provides more intelligent suggestions by using partial matches and the first letter of each word, in addition to prefix matching.
- __Alternative toolchains__ are supported, such as toolchains downloaded from [Swift.org](https://swift.org/).

  A toolchain supplies the tools (compilers, linker, and other tools) necessary to build, run, test, and debug Xcode projects; Xcode is equipped with the default toolchain when it is installed. You can download and install alternative toolchains to use for development, enabling you to explore and test new language features. When you’re using an alternative toolchain, Xcode builds and debugs with the alternative toolchain’s tools instead of the default tools.

  Alternative toolchains, when activated, only affect operations in the Xcode IDE, and you must use the default toolchain to run playgrounds or submit apps to the App Store. See [Using Alternative Toolchains](https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/AlternativeToolchains.html#//apple_ref/doc/uid/TP40010215-CH76) for additional information.
- __Playgrounds__ offer support for live views with user interaction. You can create controls that respond to gestures, taps, or clicks enabling you to easily mock-up a UI design with interaction while experimenting in a playground.

  In addition, playgrounds’ rich comments are enhanced to support inline video display. Video tags enable you to declare a video file to use, as well as specify options for alternate text, a customized poster frame, and customized width and height for the video window. For information about using inline video, see [Videos](../../Xcode/Markup%20Formatting%20Reference/InlineVideo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqojy) in the _[Markup Formatting Reference](https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/index.html#//apple_ref/doc/uid/TP40016497)_.
- __Devices__ window allows pairing multiple Apple Watches to an iPhone for testing.

  With iOS 9.3 and watchOS 2.2, you are able to pair multiple Apple Watches to an iPhone. Enhancements to the Xcode Devices window allow you to pair multiple Apple Watches to your app when running in Simulator for testing and debugging. See Pairing Apple Watch Simulators to iPhone Simulators for more information.
- __Static Analyzer__ includes improvements in its handling of nullability, missing localizability, and common misuses of Objective-C generics.
- __Debugger__ offers enhancements to view debugging, the GPU frame debugger, stepping performance, and the address sanitizer.
- __Debug Navigator__ includes improved filtering and new options for the Views mode.
- __Accounts__ in Xcode preferences enables you to generate Developer IDs for enterprise developers. For information on the steps needed, see Creating Signing Identities in _App Distribution Guide_.

- OS X 10.11 is the last major release of OS X that supports the previously deprecated garbage collection runtime.

  Applications or features that depend upon garbage collection may not function properly or may fail to launch when the runtime is removed. Developers should use Automatic Reference Counting (ARC) or manual retain/release for memory management instead.
- Apple private frameworks have been removed from the iOS, watchOS, and tvOS SDKs.

  If your app fails to link, make sure that you are not using any private frameworks. The use of private frameworks is an unsupported configuration and apps that use non-public APIs will be rejected by the App Store. For details, see [App Store Guideline 2.5](https://developer.apple.com/app-store/review/guidelines/#functionality).

Xcode 7.3.1 is a maintenance update with bug fixes and performance improvements. It includes support for iOS 9.3, watchOS 2.2, OS X version 10.11.4, and tvOS 9.2.

For more details about Xcode 7 releases, see _[Xcode Release Notes — Archive](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/Introduction.html#//apple_ref/doc/uid/TP40016994)_.

[Next](New%20Features%20in%20Xcode%206.md)[Previous](New%20Features%20in%20Xcode%208.md)

