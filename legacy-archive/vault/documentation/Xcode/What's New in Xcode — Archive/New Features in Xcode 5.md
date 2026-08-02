---
title: What's New in Xcode — Archive
apple_id: TP40017029
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/WhatsNewXcode-Archive/Articles/xcode_5_0.html
archived_at: '2026-07-18T02:24:18.017135Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [What's New in Xcode — Archive](What%E2%80%99s%20New%20in%20Xcode%20-%20Archive.md)


[Next](New%20Features%20in%20Xcode%204.md)[Previous](New%20Features%20in%20Xcode%206.md)

# New Features in Xcode 5

- [Xcode 5.0](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsnjtfvjvomjy) provides many new features along with support for development with iOS 7.0 SDK.
- [Xcode 5.0.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsnjtfvjvomrq) adds support for development on OS X v10.9 and other feature additions.
- [Xcode 5.0.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsnjtfvjvomzq) addresses reported developer issues.
- [Xcode 5.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsnjtfvjvomzr) includes SDKs for OS X v10.8, OS X v10.9, and iOS v7.1 and other enhancements.
- [Xcode 5.1.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsnjtfvjvomzs) is a maintenance release addressing reported bugs.

Xcode 5 is the latest release of the Apple developer tools. Building on the design of Xcode 4, this release focuses on features and enhancements to improve your ability to adopt core platform features, design new interfaces, and deliver high-quality applications.

Xcode 5 adds support for developing with iOS 7.0 SDK. Xcode 5 requires a Mac running OS X v10.8.4.

- The Xcode 5 user experience has a cleaner UI with more working space for your content. The changes are many and subtle—for instance, the toolbar has been shortened and simplified to produce more space in the editors. The new look is simpler with fewer distracting details, and the highlighting of buttons and panels is clearer and easier to see at a glance. At the same time, your familiarity with Xcode 4 works for you—you can be familiar with the new Xcode 5 UI in just a few minutes of use. You’ll find all the familiar controls there for you, clearer to see and use, putting your content first and foremost.
- Open Quickly has been revamped with a streamlined input panel that is easier to use. The changes under the hood include a much stronger matching algorithm that returns highly prioritized results faster, and the results are presented with more content.
- The refined search navigator allows all current search options and settings to be seen at a glance. The options are easily manipulated by clicking directly on them in the search navigator. You can set search scopes, including selecting multiple folders in a project, and save them by name for easy re-use. The search results display wraps to allow you to see more results easily and quickly.

- The new Accounts preferences pane allows you to manage your Apple IDs, repositories, and continuous integration servers from one place in Xcode preferences. Add and view your Developer Program Apple IDs, add source code repositories to store the location and authentication information used when accessing Subversion and Git, and add continuous integration servers to take advantage of Xcode Services on OS X Server.
- The streamlined Capabilities settings in the project editor allow you to easily configure platform features such as iCloud, Game Center, and more.
- You choose the signing identity from the target editor.
- Xcode 5 uses the Accounts preferences, the Capabilities settings, and the signing identity settings to automatically create provisioning profiles with proper settings for you. It can also identify and offer to fix issues in provisioning profiles as well.

  To learn more about the tasks and workflow required to develop and distribute OS X or iOS apps with Xcode 5, see _App Distribution Guide_.

- Xcode 5 provides a new test navigator that offers an overview of all tests in the workspace. The new test navigator has the ability to easily add new test targets and test classes, as well as the ability to run individual tests or ad hoc collections of tests. It can also show the status of the last test run for each test.
- New test categories in the assistant editor enable you to edit code and tests side by side. The source editor provides the status of the tests, and you can run individual tests from within the editor.  The assistant editor’s “Test Callers” and “Test Classes” categories provide access to unit tests related to the current source code in the primary editor.
- The new XCTest testing framework provides support for iOS and OS X projects. It is the default for new projects and works for iOS 7 and later, as well as all versions of OS X.
- The `xcodebuild` command-line tool now supports the `test` action for both iOS and OS X tests, allowing a scheme’s test action to be performed from the command line or integrated into other scripts. Detailed information on using `xcodebuild` for running tests can be obtained using `man` from a Terminal window. Type: `man xcodebuild`

- Xcode 5 supports using services offered by the Xcode service included with OS X Server. You create a bot in Xcode to build, analyze, test, and archive your project on an OS X Server shared by your development team.
- Bots can be configured to launch an integration on every commit to your SVN or Git repository, or at defined intervals.
- Continuous integration allows you to see immediately when anyone on the team breaks a build or starts failing tests.
- You can view bot integration results in Xcode 5, drilling into build and test failures to find and fix the problem.

  For more information about continuous integration, see _[Xcode Server and Continuous Integration Guide](https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/xcode_guide-continuous_integration/index.html#//apple_ref/doc/uid/TP40013292)_.

- Debug gauges have been added to the debug navigator to show real-time memory, CPU activity, energy use, iCloud, and OpenGL data with very low overhead. This improves the visibility of program data and provides key indicators for application performance debugging.
- Debug gauges serve as a gateway to Instruments. Open Instruments templates direct from the debug gauge detail display to investigate a variety of memory, performance, and energy use situations.
- The variables view and data tips display has been refined to show a summarized value for the variable, and presents the same hierarchical display as the variables view in the Xcode debugger area for looking at child values. The data tips support presenting variable info, and can print the Objective-C `description` of the object to the console.

  Clicking on the info button (![../Art/xc5-debug-chkview-info-button_2x.png](attachments/Art/xc5-debug-chkview-info-button_2x.png)) next to a variable brings up a display showing the console output.
- Clicking on the Quick Look button (![../Art/xc5-debug-chkview-quicklook-button_2x.png](attachments/Art/xc5-debug-chkview-quicklook-button_2x.png)) next to a variable presents a graphical display of the variable’s contents, for known graphical types.
- The debugger automatically creates a new debug session for any embedded XPC services in an application.
- The debugger now provides control options to make `NSView` objects more visible when debugging. The options include turning on frame rectangles, alignment rectangles, flashing drawing done by `NSView`, and others.
- The Debug menu includes an iCloud submenu with two new commands designed to help facilitate iCloud development.

  - “Trigger Sync in Simulator” provides a convenient way to force an iCloud sync from an iOS app without having to switch to the simulator. See the [iOS Simulator](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsnjtfvjvomjr) section for details on the Trigger iCloud Sync feature.
  - “Delete Container Contents” enables you to delete all documents and data in an app’s iCloud container.

- Apps using the OpenGL ES 3.0 API can now be debugged with the OpenGL ES frame debugger.
- The OpenGL ES shader profiler enables you to profile OpenGL ES shaders on compatible iOS devices.

  When inspecting a captured OpenGL ES frame, set the debug navigator to “View Frame By Program” mode. In this mode, you see timings for all programs, their constituent shaders, and the draw calls using those shaders. Select a shader to see further detail on where time is spent within the shader.
- The new auto variables view mode automatically shows the relevant OpenGL ES state and bound objects for the current OpenGL ES command.
- Issues found in your OpenGL ES frame capture can now also be seen in the context of the frame. Issue badges appear in the debug navigator marking commands that triggered an issue. The auto variables view in the debug area lists the issues found at the current command.
- New OpenGL ES error breakpoints add support for breaking in the debugger in response to OpenGL ES errors including multi-threading issues, shader compilation failures, and program link failures.

- Interface Builder in Xcode 5 includes support for the iOS 7 user experience and user interface objects.
- The Auto Layout editor provides more flexibility when designing app interfaces. The enhanced workflow for designing interfaces with auto layout puts you in greater control of setting object relationships.

  See [Xcode Help](http://help.apple.com/xcode) for more information on using new Interface Builder features.
- The new Preview mode of the Assistant editor can show how the iOS 7 UI you are designing would look in portrait or landscape mode, or even how it would look when viewed on a device running iOS 6.
- The asset catalog manages images and icons in multiple resolutions. An asset catalog is a new asset management file type and editor in Xcode 5. You use asset catalogs to store and manage images for different platforms, devices, and scale factors. The catalog presents the image variants required, and provides you with the ability to define slice and stretch points for images that are resized at runtime. For more information on using asset catalogs, see [Xcode Help](http://help.apple.com/xcode).

- The source control management workflow in Xcode 5 creates a project-centric experience by removing the Repositories organizer and moving these functions into the project window and the Source Control menu. The Source Control menu provides convenient access to many workflows including Check Out, Commit and Push changes, Update, Add, and History.
- The Xcode 5 source control management features also include the ability to check out multiple working copies and handle branch management directly. You manage all repository location and authentication information in one place using Accounts preferences.

  For more information about using the new source control management workflow, see [Xcode Help](http://help.apple.com/xcode).
- Subversion has been upgraded to version 1.7.9.

- The new Auto Vectorizer supports automatic optimization of computational loops for both iOS and OS X apps. To enable this option, use the `Vectorize Loops` option in the target build settings.
- Modules for system frameworks speed build time and provide an alternate means to import APIs from the SDK instead of using the C preprocessor. Modules provide many of the build-time improvements of precompiled headers with less maintenance or need for optimization. They are designed for easy adoption with little or no source changes. Beyond build-time improvements, modules provide a cleaner API model that enables many great features in the tools, such as Auto Linking.
- Auto Linking is enabled for frameworks imported by code modules. When a source file includes a header from a framework that supports modules, the compiler generates extra information in the object file to automatically link in that framework. The result is that, in most cases, you will not need to specify a separate list of the frameworks to link with your target when you use a framework API that supports modules.
- The default C++ standard library for projects deploying to iOS 7 is now the LLVM libc++ library, which utilizes many of the benefits of C++11. Applications built using this library can deploy back to iOS 5 and OS X 10.7.
- LLVM now supports the AVX2 vector instruction extensions available in new Macs. To enable these extensions, use the Xcode build setting `Enable Additional Vector Extensions`.
- A new optimization level `-Ofast`, available in LLVM, enables aggressive optimizations. `-Ofast` relaxes some conservative restrictions, mostly for floating-point operations, that are safe for most code. It can yield significant high-performance wins from the compiler.

- iOS Simulator now supports iCloud syncing of documents and KVS data within an app, enabling apps to sync between devices using iCloud. This feature is useful when testing to ensure that the app documents and data are syncing properly across multiple devices.
- Chinese Sina Weibo and Tencent Weibo character systems have been added to the iOS Simulator.

See _[Simulator User Guide](../../IDEs/Simulator%20User%20Guide/About%20Simulator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnby)_ for more information on using the new iOS Simulator features.

- The Zombies instrument template has been enhanced in Xcode 5 and now supports use on devices. Using Zombies on devices requires iOS 7.
- The Allocations instrument now includes virtual memory mappings.
- Retain-release pairing in the Allocations instrument has been enhanced to help track down imbalanced retain counts.

- The documentation experience for Xcode 5 has been redone. A separate window tailored to search and display provides fast access to documentation resources. The documentation window supports tabs so that you can have multiple documentation references simultaneously available.
- A dedicated table of contents display area is incorporated into the documentation window, allowing you to easily see and browse topics in open documents.
- The new documentation experience includes support for bookmarks and integrated, easy sharing via Mail, Messages, and other tools.
- Project documentation from framework API reference documentation and structured comments in your own source code are displayed in the quick help panel and in code completion popover views. Doxygen and HeaderDoc structured comments are supported formats.

- The Xcode 5 build system incorporates support for including Sprite Kit texture atlases as part of your project’s build cycle. A texture atlas provides you with a way to improve the performance of Sprite Kit–enabled apps by combining all of an app’s image assets into one or more large images. You can improve the performance of your app by drawing multiple images with a single draw call. More information about texture atlases in available in [Xcode Help](http://help.apple.com/xcode) and _[SpriteKit Programming Guide](../../Graphics%20Animation/SpriteKit%20Programming%20Guide/About%20SpriteKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbt)_.
- Xcode 5 includes a new editor for Sprite Kit particle emitters. Particle emitters are a function of the Sprite Kit framework that allow you to specify a specific point in your display and create images that move and change over time. Using emitters, you can simulate rain, snow, spinning car wheels, fire, and many other effects in your game. More information on particle emitters can be found in the _[Particle Emitter Editor Guide](../../IDEs/Particle%20Emitter%20Editor%20Guide/About%20the%20Particle%20Emitter%20Editor.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezteojx)_, _[Sprite Kit Framework Reference](https://developer.apple.com/documentation/spritekit)_, and the _[SpriteKit Programming Guide](../../Graphics%20Animation/SpriteKit%20Programming%20Guide/About%20SpriteKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztanbt)_.

Xcode 5.0.1 adds support for development on OS X v10.9 and other feature additions.

- Development with Xcode 5.0.1 is hosted on OS X 10.8.4 or later, and OS X 10.9.
- SDKs for OS X 10.8 and OS X 10.9, and iOS 7.0.3 SDK, are included.
- Xcode 5.0.1 supports continuous integration bots, hosted on OS X Server.

  Use the Add button (`+`) button to add OS X Servers in the Accounts preferences panel, then click the menu command Product > Create Bot.
- Includes support for OS X Server hosted repositories.
- iOS 6 (32-bit) and iOS 7 (32-bit and 64-bit) binaries build with a single build target.

- The Xcode 5.0.2 release is a maintenance release responding to reported developer issues and Apple qualification testing. See _[Xcode Release Notes — Archive](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/Introduction.html#//apple_ref/doc/uid/TP40016994)_ for more detailed information.

Xcode 5.1 requires a Mac running OS X 10.8.4 (or later), or OS X 10.9. It includes the following highlighted features:

- SDKs for OS X v10.8, OS X v10.9, and iOS v7.1
- Updates to the LLVM compiler
- Enhancements to Auto Layout constraints and editing tools in Interface Builder

  Interface Builder supports the creation of proportional and aspect ratio constraints. Enhancements to the Attributes inspector enable the creation of cross-attribute constraints as, for example, to align the leading edge of one object with the center horizontal position of another. See Adding Layout Constraints to Objects by Control-Dragging and Editing Auto Layout Constraints.
- Variables Quick Look in the Xcode debugger supporting custom object types

  Developers can now provide Quick Look content for their classes. When an instance of a class is viewed with Quick Look using the variables view or a data tip, the debugger looks for a method named `debugQuickLookObject` in the class implementation. For more details, see _[Quick Look for Custom Types in the Xcode Debugger](../../IDEs/Quick%20Look%20for%20Custom%20Types%20in%20the%20Xcode%20Debugger/About%20Variables%20Quick%20Look%20for%20Custom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dambr)_.

- The Xcode 5.1.1 release is a maintenance release addressing reported developer issues and Apple qualification testing.

For additional details on Xcode releases, see _[Xcode Release Notes — Archive](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/Introduction.html#//apple_ref/doc/uid/TP40016994)_.

[Next](New%20Features%20in%20Xcode%204.md)[Previous](New%20Features%20in%20Xcode%206.md)

