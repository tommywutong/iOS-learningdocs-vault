---
title: What’s New in Xcode
apple_id: TP40004626
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/WhatsNewXcode/Chapters/xcode_6_0.html
archived_at: '2026-07-15T07:27:10.543871Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [What’s New in Xcode](What%27s%20New%20in%20Xcode%209.md)


[Next](New%20Features%20in%20Xcode%205.md)[Previous](New%20Features%20in%20Xcode%207.md)

# New Features in Xcode 6

- [Xcode 6.0](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbzfvjvomjw) includes SDKs for OS X version 10.9, iOS 8, and other enhancements.
- [Xcode 6.0.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbzfvjvomjx) is a maintenance update responding to developer input and Apple SQA testing.
- [Xcode 6.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbzfvjvomjy) adds the SDK for OS X version 10.10 and Swift language development for OS X.
- [Xcode 6.1.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbzfvjvomjz) is a maintenance update with bug fixes and performance improvements.
- [Xcode 6.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbzfvjvomrq) Xcode 6.2 adds support for iOS 8.2 and WatchKit.
- [Xcode 6.3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbzfvjvomrr) adds support for iOS 8.3, Swift 1.2, and many other new features..
- [Xcode 6.3.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbzfvjvomrv) is a maintenance update with bug fixes and performance improvements.
- [Xcode 6.3.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbzfvjvomzs) fixes a Swift compilation speed regression.
- [Xcode 6.4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dkmbzfvjvomzw) includes support for development on iOS 8.4.

Xcode 6 includes Swift, an innovative programming language with an interactive work area called a _playground_. Developers can directly manipulate and experiment with Swift code live—enter the code for a Bézier path in the playground and watch the path drawn directly beside the code. Perfect new code within the playground, then easily promote that code into your main project.

Xcode 6 extends the Xcode feature set with new live visualization capabilities. For example, view debugging pauses a running app and then explodes all the UI layers into a 3D visualization, making it easy to understand how the interface is drawn. Live rendering within Interface Builder displays your handwritten UI code as you design, so that you can edit your view’s code and the IB rendering changes instantly. And the preview assistant now shows your app in different languages with only a mouse click.

Xcode 6 requires a Mac running OS X version 10.9.4 or later or 10.10. It includes SDKs for OS X version 10.9 and 10.10, and iOS 8.

Xcode 6 includes the following highlighted features.

Swift is a advanced object-oriented programming language for iOS development. Swift is modern, powerful, expressive, and easy to use.

- __Fast.__ Swift compiles and is optimized with the advanced code analysis in LLVM to create high-performance apps.
- __Complete platform.__ Access all of the Cocoa Touch frameworks with Swift.
- __Safe by design.__ Eliminate huge categories of bugs, crashes, and security holes.

  Swift pairs increased type safety with type inference, restricts direct access to pointers, and automatically manages memory using ARC, making it easy for you to use Swift and create secure, stable software. Other language safety related features include mandatory variables initialization, automatic bounds checking to prevent overflows, conditionals that break by default, and elimination of pointers to direct memory by default.
- __Modern.__ Write, debug, and maintain less code, with an easy to write and read syntax, and no headers to maintain.

  Swift includes optionals, generics, closures, tuples, and other modern language features. Inspired by and improving upon Objective-C, Swift code feels natural to read and write.
- __Interactive.__ Use Swift interactively to experiment with your ideas and see instant results.
- __Unified.__ Swift is a complete replacement for both the C and Objective-C languages. It provides full object-oriented features, and includes low-level language primitives such as types, flow control, and operators.

For full information about the Swift language and to get started using it, see _The Swift Programming Language_.

- __Playgrounds.__ Playgrounds make writing Swift code productive and easy. Enter a line of code, and the result appears immediately. If your code runs over time—for instance through a loop—you can add that line of code to Timeline Assistant to watch it progress. Display variables in a graph, inspect each step of drawing a view, or watch an animated SpriteKit scene. When you’ve perfected your code in the playground, simply move that code into your project. Some uses for playgrounds include:

  - Designing a new algorithm, watching its results every step of the way
  - Experimenting with new API or trying out new Swift syntax
  - Creating new tests and then verifying that they work before promoting them into your test suite
- __Learn in a playground.__ Open select documentation in a playground to learn from the tutorial in an interactive environment. The combination of richly formatted documentation and an interactive playground makes it easy to fully explore the API, changing and experimenting with the sample code.
- __Read-eval-print loop (REPL) in LLDB.__ The debugging console in Xcode includes an interactive version of the Swift language called the _read-eval-print loop (REPL)_ built right in. Use Swift syntax to evaluate and interact with your running app, or write new code to see how it works in a script-like environment. REPL is available from within the Xcode console or by using LLDB from within Terminal when attached to a running process.
- __Per-language documentation.__ The Xcode documentation viewer shows Quick Help or reference documentation in the language of your choice—Objective-C, Swift, or both.
- __Synthesized headers.__ When you need to see how the API you are using was written, Xcode shows it to you in the language you expect. For API originally written in Objective-C, Xcode shows you a version of the original header file in Swift syntax, complete with the author’s comments.

Bringing more live visualization to your existing projects, the following enhancements are also Swift compatible.

- __Performance measurement.__ The enhanced XCTest framework now supports the ability to quantify the performance of each part of an app. Xcode runs your performance tests and allows you to define a baseline performance metric. Each subsequent test run compares performance, displays the change over time, and—by highlighting the problem area—alerts you to sudden regressions a code commit could introduce.
- __Asynchronous code testing.__ XCTest now provides API for testing code that executes asynchronously. You can now create tests for network operations, file IO, and other system interactions that execute using asynchronous calls in a straightforward and simple manner.

For more information, see _[Testing with Xcode](../Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_.

- __Live rendering.__ Interface Builder displays your custom objects at design time exactly as they appear when your app is run. When you update the code for your custom view, the Interface Builder design canvas updates automatically with the new look you just entered in the source editor, with no need to build and run. You can use the Interface Builder inspector to see properties automatically as well. Take advantage of new APIs that allow you to customize the behavior of custom controls on the Interface Builder canvas—for instance, you can load sample data on the fly.

  For more information on live rendering, see Creating a Custom View That Renders in Interface Builder.
- __Size classes.__ Size classes for iOS 8 enable designing a single universal storyboard with customized layouts for both iPhone and iPad. With size classes you can define common views and constraints once, and then add variations for each supported form factor. iOS Simulator and asset catalogs fully support size classes as well.

  For more information on size classes, see _Size Classes Design Help_.
- __Custom iOS fonts.__ Interface Builder renders embedded custom fonts during design time, giving a more accurate preview of how the finished app will look, with correct dimensions.

- __View debugging.__ Using the view debugger makes debugging an app’s appearance as easy as debugging lines of code. A single button click pauses your running app and “explodes” the paused UI into a 3D rendering, separating each layer of a stack of views. Using the view debugger makes it immediately obvious why an image may be clipped and invisible, and the order of the graphical elements becomes clear. By selecting any view, you can inspect the details by jumping to the relevant code in the assistant editor source view. The view debugger also displays Auto Layout constraints, making it easy to see where conflicts cause problems.
- __Enhanced queue debugging.__ The debug navigator records and displays recently executed blocks, as well as enqueued blocks. You can use it to see where your enqueued blocks are and to examine the details of what’s been set up to execute.
- __Debug gauges.__ Debug gauges provide at-a-glance information about resource usage while debugging. They call your attention to previously unknown problems, especially related to areas that could create poor user experience or drain excess battery on portable Mac computers and devices.

  - __I/O gauges.__ Two new debug gauges, Network Activity and File Activity, visually highlight spikes in input/output activity while your app is running.
  - __iCloud gauge.__ The iCloud debug gauge includes support for the new Documents in the Cloud and CloudKit features that provide access to files outside the app-specific container.

- __Graphics and game development.__ Support for SpriteKit has been significantly enhanced with a new SpriteKit level designer and improved display of SpriteKit variables when debugging.
- __Support for iOS.__ SpriteKit and SceneKit are now enhanced to work together and on iOS. Create scenes for your SpriteKit games from within Xcode. It is easier than ever to define how your characters, backgrounds, and the rest of your game comes together—it has never been easier to share code when creating great games for both iOS and OS X.

- __Extensions support.__ Add an extension target to any iOS or Mac app to expand your app’s functionality to other apps in the OS. Xcode connects to the extension when launched, debugging the extension as it runs in the safe, embedded OS context.
- __Frameworks for iOS.__ iOS developers can now create dynamic frameworks. Frameworks are a collection of code and resources to encapsulate functionality that is valuable across multiple projects. Frameworks work perfectly with extensions, sharing logic that can be used by both the main application and the bundled extensions.

For more information, see _[App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)_.

- __Configurations.__ New iOS Simulator configurations allow you to keep data and configuration settings grouped together. Run one configuration for one version of an app, with its own data, and another configuration for a different app version.

For more information on iOS Simulator, see _[Simulator User Guide](../../IDEs/Simulator%20User%20Guide/About%20Simulator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnby)_.

- __XLIFF import-export.__ Xcode can package your localizable strings into the industry standard XLIFF format to send off for localization. When localization is completed, it’s easy to integrate the new languages back into the project.
- __Implicit .strings file.__ Xcode automatically generates the base language `.strings` file directly from your source code—now you no longer need to manage this `.strings` file by hand.
- __Preview in Interface Builder.__ While designing in Interface Builder, the preview assistant can show how the interface appears in other languages. You can see how your interface responds to longer or shorter languages.
- __Run in locale.__ Xcode can run your app on iOS Simulator, or directly on devices, as it would appear to customers in other countries.

For more information on Xcode 6 localization, see _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_.

- __Profile Guided Optimization.__ Profile Guided Optimization (PGO) works with the LLVM optimizer and your performance tests to profile the most actively used parts of your app. You can also exercise your app manually to generate a performance profile. PGO uses the profile to further optimize your app, targeting the areas that most need optimization, improving performance beyond what setting optimization options alone can achieve.

  For more information on Profile Guided Optimization, see _Xcode Profile Guided Optimization_.
- __User-defined modules.__ Developers are now able to define modules for their own Objective-C code, making it easier than ever for them to share frameworks across all their projects. By combining user-defined modules with Swift’s automatic creation of modules, the two languages work together seamlessly.

- __New user interface.__ The new Instruments user interface makes configuring your performance tuning session easier and improves control. The new template chooser allows you to choose your device and target as well as the starting point for your profiling session. The track view allows direct click-and-drag to set the time filter range. The toolbar takes up less space to let you focus on the task at hand.

  Instruments now looks and works more like Xcode. The tracks of recorded data are given more space, and configuration for how data is collected and viewed is managed in a unified inspector area.
- __Profile tests.__ Choose any test or test suite to profile, great for analyzing memory leaks in a functional test or time profiling a performance test to see why it has regressed.
- __Support for simulator configurations.__ Simulator configurations are treated like devices by Instruments, making it easy to launch or attach to processes in the simulator.
- __New Counters instrument.__ Counters and Events instruments have been combined into a more powerful instrument and made easier to configure. It can track individual CPU events, and you can specify formulas to measure event aggregates, ratios, and more. iOS developers on 64-bit devices can now use Counters to fine-tune apps.
- __Swift and Extensions support.__ Of course, Swift is supported—you’ll see Swift symbols in stack traces and Swift types in Allocations. You can also use Instruments to profile your app extensions.

- __Triggers.__ Triggers allow you to make more complex integration scenarios by configuring server-side rules to launch custom scripts before or after the execution of an Xcode scheme.
- __Performance test integrations.__ Xcode Server supports the new Xcode performance-testing features, making it easy for a team to share a Mac computer and a group of iOS devices for continual performance testing.
- __Delta tracking.__ Issues are now tracked per integration, so you can see when an issue appeared or when it or was fixed, and by whom.
- __Greater control.__ Configuration options in Xcode Server give development teams even greater control over the execution of bots. New settings for integration intervals, grouping of bots, and iOS Simulator configurations make Xcode bots more powerful than ever. The new reports UI includes bot-level statistics—for example, the number of successful integrations, commit and test addition tracking, and so forth.

For more information on Xcode Server, see _[Xcode Server and Continuous Integration Guide](https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/xcode_guide-continuous_integration/index.html#//apple_ref/doc/uid/TP40013292)_.

- __HomeKit capability.__ The new HomeKit framework allows your app to communicate with and control connected accessories in a user’s home. To use HomeKit with your iOS apps, set the HomeKit switch in the project editor capabilities panel. Choose Xcode > Open Developer Tool > HomeKit Accessory Simulator to start using the simulator.

For more information on HomeKit, see _[Home Kit Framework Reference](https://developer.apple.com/documentation/homekit)_.

Xcode 6.0.1 is a maintenance release responding to reported developer issues and Apple qualification testing.

Xcode 6.1 adds development for OS X with Swift, and includes bug fixes as well as other new features.

- Xcode 6.1 includes development support with SDKs for OS X version 10.9, OS X version 10.10, and iOS 8.

- Swift has access to all Cocoa frameworks for OS X development using the SDK for OS X version 10.10.
- Swift development targets can deploy on both OS X Mavericks and OS X Yosemite.

- __Storyboards for OS X.__ Storyboards come to OS X with Xcode 6, taking advantage of new view controller APIs in AppKit. Storyboards make it easy to wire together multiple views and define segue animations without writing code. Storyboards for OS X encourage interfaces that follow Mac standards so that your apps behave the way users expect.

  For more information on storyboards, see _Storyboard Help_.

Xcode 6.1.1 includes bug fixes and performance improvements.

Xcode 6.2 adds support for iOS 8.2. It includes the new WatchKit framework for developing Apple Watch apps.

Tools Support for WatchKit includes:

- Design tools for building Apple Watch interfaces, glances, and notifications
- Debugging and profiling support
- Apple Watch support in iOS Simulator for testing apps, glances, and notifications

Xcode 6.3 adds support for iOS 8.3, updates to Swift, and many other new features.

- Swift 1.2 generates substantially faster performing code compared to Swift 1.1.
- Xcode now builds Swift targets incrementally for greater efficiency: a single file change no longer invokes building all of the source files in a target.

  These and other noteworthy improvements to Swift and Swift standard library are detailed in [Xcode 6.3 Release Notes](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/xc6_release_notes.html#//apple_ref/doc/uid/TP40016994-CH4-SW26).
- The new Swift migrator in Xcode 6.3 eases moving your Swift 1.1 code to Swift 1.2.

  In Xcode, select `Edit > Convert > To Latest Swift Syntax` to invoke the migrator.

- A new feature that helps opted-in App Store users and TestFlight users collect and analyze crash log data for your apps.

  Crash reports gathered from opted-in App Store users and TestFlight users can be displayed in the Crashes Organizer. More details are available in [Xcode 6.3 Release Notes](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/xc6_release_notes.html#//apple_ref/doc/uid/TP40016994-CH4-SW26) and [Xcode Help](http://help.apple.com/xcode).

- Improved documentation authoring with inline marked-up comments, inline playground results, the ability to view and edit resources embedded in playgrounds, and the ability to integrate auxiliary source files into Playgrounds. These features enable the creation of rich new experiences in playgrounds.

  For more information, see [Xcode 6.3 Release Notes](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/xc6_release_notes.html#//apple_ref/doc/uid/TP40016994-CH4-SW26), _[Playground Reference](https://developer.apple.com/library/archive/documentation/Swift/Reference/Playground_Ref/Chapters/XCPlayground.html#//apple_ref/doc/uid/TP40014789)_, and [Xcode Help](http://help.apple.com/xcode).

- Xcode uses Force Touch trackpad gestures for Macs that include it, and supports configuring Force Touch trackpad functionality on OS X in Interface Builder editor for `NSButton` and `NSSegmentedControl`.

- In Objective-C code, you can now directly express the nullability of pointers in header files, improving interoperability between Swift and Objective-C.

  See [Xcode 6.3 Release Notes](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/xc6_release_notes.html#//apple_ref/doc/uid/TP40016994-CH4-SW26) for details on the changes and enhancements.

- LLDB has been enhanced to improve the support for modules in C-based languages as well as provide overall improvements in Swift debugging support.

  The LLDB Objective-C expression parser can now import modules, enabling subsequent expressions to rely on function and method prototypes defined in the module. Additional benefits of importing modules include better error messages, eliminating potentially incorrect inferred argument types, and more.

  See [Xcode 6.3 Release Notes](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/xc6_release_notes.html#//apple_ref/doc/uid/TP40016994-CH4-SW26) for details on the enhancements.

- LLVM version 6.1 includes support for C++14, enhanced warning diagnostics, and new optimizations.

  This updated compiler includes full support for the C++14 language standard, a wide range of enhanced warning diagnostics, and new optimizations. Support for the arm64 architecture has been significantly revised to better align with the ARM implementation; the most visible impact is that several vector intrinsics have changed to more closely match the ARM specifications.

- The argument ordering for the arm64 vfma/vfms lane intrinsics has changed.

  By default, the compiler now warns about any use of the intrinsics but will retain the old behavior. To reduce risk, the transition to the new ordering is being completed in stages.

Xcode 6.3.1 is a maintenance update with bug fixes and performance improvements.

Xcode 6.3.2 is a maintenance update with bug fixes and performance improvements.

- Swift projects now compile quickly, fixing a speed regression in Xcode 6.3.1.

Xcode 6.4 includes support for development on iOS 8.4, along with bug fixes and performance improvements.

For additional details on the Xcode 6.4 release, see _[Xcode Release Notes — Archive](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/Introduction.html#//apple_ref/doc/uid/TP40016994)_.

[Next](New%20Features%20in%20Xcode%205.md)[Previous](New%20Features%20in%20Xcode%207.md)

