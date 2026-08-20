---
title: What’s New in Xcode
apple_id: TP40004626
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/WhatsNewXcode/xcode_9/xcode_9.html
archived_at: '2026-07-15T07:27:10.581782Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](New%20Features%20in%20Xcode%208.md)

# What's New in Xcode 9

Xcode is the complete developer toolset used to create apps for Apple TV, Apple Watch, iPad, iPhone, and Mac. The Xcode development environment bundles the Instruments analysis tool, Simulator, and the OS frameworks in the form of tvOS SDKs, watchOS SDKs, iOS SDKs, and macOS SDKs.

Xcode 9 includes overall quality improvements as well as extensive new features.

- __All new editor.__ Fast, structure-based editor that lets you intelligently highlight and navigate your code. Includes great Markdown support.
- __Refactoring.__ Refactoring built right into the editing experience and works across Swift, Objective-C, Interface Builder, and many other file types.
- __Super-fast search.__ The Find navigator returns results instantly.
- __Debugging.__ Wirelessly debug iOS and tvOS devices over the network, new debuggers for Metal, and more features throughout Xcode.
- __Source Control.__ All new source control navigator and integrated support for GitHub accounts to quickly browse repositories and push them to the cloud.
- __Xcode Server built-in.__ Run continuous integration bots can be run on any Mac with Xcode 9, no need to install macOS Server.
- __New Playground templates.__ New iOS templates that are designed to run well in both Xcode and Swift Playgrounds on iPad.
- __New build system.__ An opt-in preview of Xcode's new build system provides improved reliability and performance.

- Updated way to define text macros using a plist file.

  - Define text macros for a user, a project, or a specific user in a project.
  - Customize the new file header. For more information, see Customizing file headers in Xcode Help.
- Updated the indexing engine to include the ability to index files as they are compiled.
- Split the Devices window into separate panes for devices and simulators.

- Named colors support.
- Added wide gamut app icons.
- Added a larger iOS marketing icon to the App Icon set.
- Added option to preserve image vector data for matching Dynamic Type scaling.
- Added support for HEIF images.

- __New in Xcode 9 – Swift static libary support.__

  - Added support for static library targets that contain Swift code.
- __New in Xcode 9 – Preview of a new build system written in Swift.__ Currently, This system is optional but it will become the default in a future version of Xcode

  - Added a preview of a new build system written in Swift.
  - Provides higher reliability.
  - Catches many project configuration problems.
  - Improves overall build-system performance.

    Note, build system performance does not include the compilers, linkers, and other tools used by the build system.

  To opt into the new build system for a project or workspace, choose File > Project Settings or File > Workspace Settings, and then choose New Build System (Preview) for the Build System type. For notes on compatibility with existing projects, see the _[Xcode Release Notes](../../../releasenotes/Developer%20Tools/Xcode%20Release%20Notes/Xcode%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjr)_.

- New configurations for iOS hotspot and for Multipath TCP.
- New network configurations, including content filtering, proxying DNS queries, and proxying TCP and UDP connections.
- New background mode for watchOS for use with audio recording and turn-by-turn directions.
- New mode for tvOS background fetch.

- __New in Xcode 9 – Core ML editor.__

  - Generate strongly typed interfaces for the model.
  - Model compilation for on-device usage.

- __New in Xcode 9 – Network debugging for iOS and tvOS devices.__

  - Debug iOS and tvOS devices over WiFi or wired networks.
  - Connect through Bonjour or enter an IP address.
  - To enable network debugging, see Pair a wireless device in Xcode Help.
- __New in Xcode 9 – GPU frame capture and GPU overrides.__

  - View command buffers, attachments, resources, and call stacks.
  - Modify shaders and save changes to your app.
  - Move through the timeline for the sequence.
  - Inspect and modify values for individual pixels in attachments including color values, alpha, depth, and more.
  - Experiment with the rendering state without modifying code by minimizing texture bandwidth, minimizing number of rendered pixels, disabling the blending stage, showing only the wireframe, and scaling the amount of tessellation.
- __New in Xcode 9 – Undefined Behavior Sanitizer.__

  - Find sources of program crashes, unexpected behaviors, and incompatibilities with future versions of Xcode.
  - Detect several types of undefined behaviors in C languages such as integer overflow, invalid casts, and alignment violations.

  Enable the [Undefined Behavior Sanitizer](https://developer.apple.com/documentation/code_diagnostics/undefined_behavior_sanitizer) in the Diagnostics pane of the scheme editor.
- __New in Xcode 9 – Main Thread Checker.__

  - Detect AppKit, UIKit, and WebKit method calls that are not made on the main thread.

  Automatically enabled during debugging, and can be disabled in the Diagnostic tab of the scheme editor. Use the [Main Thread Checker](https://developer.apple.com/documentation/code_diagnostics/main_thread_checker) with Swift and C languages.

  [Main Thread Checker](https://developer.apple.com/documentation/code_diagnostics/main_thread_checker) works with Swift and C languages.
- Enhanced the Breakpoint navigator with deep filtering.
- Visual indicators for modified breakpoints.
- Extended the view debugger to show view controllers, and to work with SceneKit and SpriteKit views.
- Enhanced iOS energy gauge.

- New unified browser that integrates reference, sample code, and articles.
- Improved documentation search.
- New jump bar for navigating between pages.
- Integrated sample code downloading.

- New split view for pinning graphs in the graphing area of a trace document.
- Moved the strategy picker into a new toolbar at the top of the trace document and added a new All strategy.
- Enhanced Metal debugging instrument.
- Metal system trace VR support for viewing events such as compositor activity, pose queries, and more.

- Named colors from the asset catalog.
- New margin and baseline view constraints.
- Auto Layout safe-area guides.
- Full-screen watchOS apps.

- __New in Xcode 9 - Capture API.__

  - Define explicit capture boundaries in your code.
  - Use the new [MTLCaptureManager](https://developer.apple.com/documentation/metal/mtlcapturemanager) class and the new [MTLCaptureScope](https://developer.apple.com/documentation/metal/mtlcapturescope) protocol to set, manage, and trigger capture boundaries programatically.
  - Use the extended Xcode GPU Capture UI to start and stop captures manually. You can also use Xcode to capture API boundaries defined in your app.
- __New in Xcode 9 - GPU counters.__

  - Analyze detailed profiling metrics about a specific GPU capture. In iOS and tvOS, GPU counters are shown as a timeline of command encoders; in macOS, GPU counters are shown as a timeline of draw or dispatch calls.
  - Examine runtime performance of render or compute pipeline stages, such as the vertex shader, fragment shader, compute kernel, and more.
  - Compare the amount of GPU time spent in each pipeline stage to find your performance bottlenecks.
- __New in Xcode 9 - GPU remarks.__

  - Find optimization opportunities in your Metal shading language code.
  - Debug device-specific runtime issues in the shader editor.
  - Follow direct resolutions and instructions to improve your code.
- __New in Xcode 9 - Smart filtering.__

  - Find specific debug information by typing into the debug navigator. Xcode dynamically displays suggestions as you type and highlight matching text, such as resources, pixel formats, function names, object labels, and more.
  - Filter search results by selecting options from a predefined menu of Metal objects.
  - Use multiple filters with many matching conditions.
- __New in Xcode 9 - Virtual Reality (VR) support.__

  - View VR submissions and left-eye/right-eye submitted surfaces.
- Texture inspection for inspecting values of individual pixels in render targets, such as color, alpha, depth, and more.
- Inspection of output vertex attributes in the buffer editor.
- Data tips support for Metal objects such as textures, buffers and samplers.

- Rename a symbol in a single file or in a project across Swift, C, Objective-C, C++ files, and Interface Builder files.
- View all the possible changes in one editor pane.
- Convert method signatures between Swift and Objective-C formats.
- Update properties, getters, setters, and synthesized iVars as needed.
- Apply a fix-it everywhere with one button.
- Automatically fill in missing cases in switch statements, and mandatory methods for protocol conformance with one click.
- Extract method functionality for all supported languages, along with other language-specific local refactoring.

- __New in Xcode 9 - Multiple concurrent simulators.__

  - Run multiple simulators at the same time.
  - Run more tests in parallel.
  - Test synching and other multidevice workflows.
- New bezel for iOS and watchOS simulators includes the hardware controls. Use the bezel to move or resize the simulated device.
- Share information with Simulator from Maps, Photos, and Safari.
- Hold down the Option key when closing a simulated device or quitting Simulator to keep simulators running after closing the window or quitting Simulator for better integration with the `simctl` command of the `xcrun` command line tool.
- Record videos of simulators.
- Open the new Simulator documentation by choosing Help > Simulator Help.

- New source control navigator for viewing branches, tags, and remote repositories for the current workspace.
- New source control inspector shows details for the selected navigator item.
- New editor for branch history including a jump bar for easy navigation.
- New side-by-side editor for file diffs.
- Easier and faster access to common tasks.
- GitHub account integration for easy browsing and one-click creation of a project and the associated GitHub repository.

- __New in Xcode 9 – New source editor.__
- Faster and more versatile Find and replace.
- Fast scrolling for files of any size.
- Direct manipulation of code structure such as tokens and blocks.
- Redesigned integration for source control.
- Redesigned presentation of error and warning messages.
- Support for Markdown.

- __New in Xcode 9 – Swift 4.__

  - One compiler for Swift 4 and Swift 3. You can compile Swift 4 and Swift 3 targets together in the same project.
  - Improved migration experience that supports migrating only select targets to Swift 4. See, Migrate to Swift 4 @objc inference in Xcode Help.
  - Faster generic code and decreased code size.

- __New in Xcode 9 – Parallel device testing.__
- Added new APIs to XCTest.

  - Control and capture screenshots.
  - Group test activities.
  - Test attachments.
  - Cleanup test state in a teardown block.
- Target multiple apps in one UI test.
- Run tests using a specified language and region.

- __New in Xcode 9 - Built in Xcode Server.__

  - New Server & Bots pane in Preferences for configuring Xcode Server and for setting Bot permissions.
- Added support for 2-factor authentication.
- Updated functionality for bots.

  - Support automatic and manual provisioning workflows.
  - Pass additional arguments to `xcodebuild`.
  - Run tests in parallel on devices and Simulator.
  - Configure language and region for tests.
  - Send "all clear" emails notifications.

Xcode 9.0 requires a Mac running macOS Sierra 10.12.4 or later.

You obtain Xcode 9 from the Mac App Store. It is a free download that installs directly into the Applications folder. By default, Xcode downloads developer documentation in the background for offline reading; it also automatically downloads documentation updates. This behavior can be changed after installation using the Downloads preferences pane.

The Apple Developer Program provides access to the App Store, Mac App Store, and Apple TV App Store, additional support and documentation, and signing resources for testing and deployment on Apple TV, Apple Watch, iPad, iPhone, and iPod touch devices. For more information, visit the [Apple Developer Program website](https://developer.apple.com/programs/).

Visit [Apple Developer Forums](https://developer.apple.com/devforums/) for discussions about any Apple developer software, including prerelease products.

For the latest security information, visit [Apple security updates](https://support.apple.com/kb/HT1222).

A software development kit (SDK) is a collection of frameworks (libraries, headers, and resources) that represent the API for a specific watchOS, iOS, or macOS version. Most of the functionality your app gets from an SDK is actually provided by the host operating system, which sets the correct base SDK and OS Deployment Target settings that are critical for app compatibility. Xcode automatically builds with the latest SDK and targets the latest OS.

If your app doesn’t require the latest OS features, you can configure it to run on a previous version of the platform operating system by selecting the OS Deployment Target option in the Xcode Project settings. If your project was created in an older version of Xcode, you can let Xcode update your project. For details on this feature, see [Project Modernization](New%20Features%20in%20Xcode%208.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmzvfvjvomzw).

Changes to the signing processes may impede your development if you're working on an older project that has not been updated to the current signing process.

The recommended approach for both enterprise and App Store developer accounts is to use automatic signing in Xcode to code sign apps during both development and distribution. See Xcode Help for documentation on automatic signing. If you have an older project that isn't configured to use automatic signing, read [Technical Q&A (QA1814) "Setting up Xcode for Automatic Provisioning"](https://developer.apple.com/library/ios/qa/qa1814/_index.html#//apple_ref/doc/uid/DTS40014030) to learn how to reconfigure your Xcode project.

Consider automatic signing before using other techniques. If your projects do require manual signing, search for “manually sign” in Xcode Help to review current manual signing practices.

When you open a project, Xcode evaluates it to see whether any settings should be updated. This feature makes it easy to ensure your projects conform to the latest SDKs and best practices.

Open the issue navigator to see whether anything in your project needs to be updated. You can also select the project in the project navigator, and then choose Editor > Validate Settings.

If the issue navigator lists modernization issues, click the issue to see a dialog that explains the updates that should be made and that lets you perform any or all of them.

After you click Perform Changes, regardless of whether you choose to make all the changes, Xcode does not show the warning again. To rerun the check, select your project in the project navigator and choose Editor > Validate Settings.

To learn more about using Xcode, choose Help > Xcode Help.

[Next](New%20Features%20in%20Xcode%208.md)

