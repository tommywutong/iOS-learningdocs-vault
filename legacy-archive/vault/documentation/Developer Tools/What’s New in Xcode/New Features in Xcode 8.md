---
title: What’s New in Xcode
apple_id: TP40004626
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/WhatsNewXcode/Chapters/xcode_8_0.html
archived_at: '2026-07-15T07:27:10.570793Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [What’s New in Xcode](What%27s%20New%20in%20Xcode%209.md)


[Next](New%20Features%20in%20Xcode%207.md)[Previous](What%27s%20New%20in%20Xcode%209.md)

# New Features in Xcode 8

Xcode is the complete developer toolset used to create apps for Apple TV, Apple Watch, iPad, iPhone, and Mac. The Xcode development environment bundles the Instruments analysis tool, Simulator, and the OS frameworks in the form of tvOS SDKs, watchOS SDKs, iOS SDKs, and macOS SDKs.

Xcode 8.3 is a maintenance update with bug fixes and performance improvements. It includes support for iOS 10.3, watchOS 3.2, macOS 10.12.4, and tvOS 10.2.

For more information on Xcode 8.3, see _[Xcode Release Notes](../../../releasenotes/Developer%20Tools/Xcode%20Release%20Notes/Xcode%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjr)_.

- Added autocompletion of symbols in Breakpoint navigator fields.
- Added a text field for entering an intents extension query.
- Added support for visually debugging the view hierarchy of iOS iMessage Extensions.

- Removed the Display Settings pane and moved features to new locations. For more information, see Help > Instruments Help and [New Features](../../../releasenotes/Developer%20Tools/Xcode%20Release%20Notes/Xcode%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltcobq) for Instruments in the _[Xcode Release Notes](../../../releasenotes/Developer%20Tools/Xcode%20Release%20Notes/Xcode%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjr)_.
- The ability to view graphs for multiple runs at the same time in the timeline pane has been removed.

- Moved viewing and managing manual provisioning profiles to the General tab of the project editor.
- Simplified viewing and managing of signing certificates.

- Choose Hardware > Siri to invoke Siri.
- The `simctl` tool of the `xcrun` command line tool adds two new commands that provide additional information for filing bug reports.

- Added checks for synthesized copy properties of mutable types, for calls to `dispatch_once()` that use an instance variable as the predicate, and for unintended comparisons between scalar values and number objects.

- Xcode 8.3 includes Swift 3.1.
- The `Sequence` protocol adds two new members, `prefix(while:)` and `drop(while:)`.

- Added new APIs to simplify writing asynchronous tests.

Xcode 8.2 is a maintenance update with bug fixes and performance improvements. It includes support for tvOS 10.1, watchOS 3.1, iOS 10.2, and macOS Sierra 10.12.2.

For more information, see the _[Xcode Release Notes](../../../releasenotes/Developer%20Tools/Xcode%20Release%20Notes/Xcode%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjr)_.

- You can customize Touch Bar controls for the source editor, playground editor, Interface Builder, view debugger, and memory graph debugger. Open the desired editor and choose View > Customize Touch Bar. For more information, open Xcode Help and search for Customize the Touch Bar controls.

- Xcode 8.2 is the last release with support for Swift 2.3. Use Edit > Convert > To Current Swift Syntax to migrate your projects to Swift 3.

- Dragging an app bundle previously built with Xcode from disk onto Simulator installs the app.
- You can take a screenshot or a video recording of the simulator using the `xcrun` command-line utility. For more information, see [Taking a Screenshot and Recording Video Using the Command Line](../../IDEs/Simulator%20User%20Guide/Interacting%20with%20Simulator.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdqnbyfvbuqmznknlti).

- Xcode 8.2 is the last release with support for Swift 2.3.

Xcode 8.1 is a maintenance update with bug fixes and performance improvements. It includes support for iOS 10.01, watchOS 3.1, macOS 10.12.1, and tvOS 10.0.

Xcode 8.1 requires a Mac running macOS 10.11.5 or later.

- Xcode adds context-specific items to the Touch Bar, enabling easy access to Xcode functions and access to debugging facilities from within your running app.
- Interface Builder supports adding items to the Touch Bar for your macOS app as well as previewing the items you've added in the Touch Bar.
- Xcode includes a Touch Bar simulator window.

- Click the new Update Frames button at the bottom of the Interface Builder canvas to update the frames of the selected objects and their children.
- Use the new Custom Gesture Recognizer in the object library for custom subclasses of `UIGestureRecognizer` or `NSGestureRecognizer` instead of using `NSObject`.
- The Pin button at the bottom of the canvas has been renamed to Add New Constraints.

- `Debugger()` and `DebugStr()` are deprecated and the scheme editor no longer provides the option to enable these functions. If your project uses these functions, enable them by setting the environment variable `USERBREAK` with a value of `1`.
- The Automation instrument has been removed from Instruments. Use Xcode’s UI Testing in its place.
- The version of Swift 2 (2.3) used in Xcode 8.1 is very close to the version used in Xcode 7.3.1. However, it has been updated for the newer SDKs, and therefore is not compatible with Swift frameworks compiled in Xcode 7.3.1. Distributing binary Swift frameworks remains unsupported in Xcode 8.

Xcode 8 includes overall quality improvements as well as extensive new features.

- __Security.__ Increased Xcode.app security due to runtime library validation
- __Readability.__ New SF Mono font and updated syntax highlighting themes
- __Downloading.__ Smaller download size and faster installation for App Store downloads
- __Accessibility.__ Enhanced accessibility in core Interface Builder workflows, and throughout Xcode
- __Usability.__ Xcode and Interface Builder improvements throughout to increase performance and reduce memory use
- __Reference.__ Faster, more space-efficient, easier-to-read documentation

__New in Xcode 8 – Swift 3.__ The latest release of Swift includes significant refinement to API naming designed to enhance your code's consistency and clarity. Also in this release, important frameworks have been upgraded to native Swift interfaces, such as Core Graphics and Grand Central Dispatch.

_The Swift Programming Language (Swift 3)_ has been updated to include extensive Swift 3 detail information.

A Swift migrator is provided to help upgrade your Swift code to the latest Swift 3 language specifications and SDK requirements.

- New signing editor with easier to understand configuration and enhanced diagnostics
- Signing certificates available on a per-machine basis—reducing the need to revoke certificates or transfer private keys between development machines

- iCloud available for Mac apps distributed with Developer ID outside the Mac App Store

- New adaptive UI development tools and workflow
- Pixel-perfect rendering of each device type within the design canvas
- Fast, new design canvas with support for editing even when zoomed out

- Expressive Messaging feature support (“Stickers”)

- App extension for the Xcode source editor to enable developer plug-ins
- Auto-creation of documentation for Swift and Objective-C code
- Current line highlighting
- Color and image literals in Swift code
- Code completion for images

- Memory debugging for visualization and navigation of memory relationships while debugging
- Runtime issues while debugging appear in the issue navigator, similar to compile-time issues:

  – Leaks issues identify potential leaked memory detected during debugging sessions.

  – Thread sanitizer issues identify threading-created race conditions on data changes at runtime.

  – View debugging issues identify constraints conflicts.
- Messages and Action extensions debugging support for iOS
- Greater control and visibility for more information when debugging views

- Improved System Trace template with more detail to ease diagnosis of issues

  – Threads strategy view displaying narrative descriptions of exactly what happened to every thread on the system

  – CPU strategy view showing which threads are running on which CPUs

  – Points of Interest instrument permitting programmatically added points and regions of interest to a recording
- Improved Time Profiler instrument with application life cycle events

  – Presenting when an application was launching, running in the background, and similar events
- Improved Metal System Trace template with additional detail and support for macOS
- Interface improvements

- New `build-for-testing` and `test-without-building` options in `xcodebuild`—allows separating operations for use on different machines or at different times
- Test crash logs saved with test reports—especially useful for debugging crashes when running tests with Xcode Server

- New _Xcode Help_ and _Instruments Help_, based on standard macOS Help Viewer, accessible from the Help menu
- New SDK/API reference experience with:

  – Consolidated document sets—all SDKs in one package

  – Faster and more accurate search

  – Multiple, selectable language display

  – Greatly reduced disk space due to efficient database content model

- Updated version editor:

  – Improved support for unversioned files

  – Change tracking across file renames in Git

  – File renames in navigator correctly renamed in Git

  – Full Unicode support for filenames in Git

  – New diff count and stepper to ease moving through diffs

  – Simplified file listings show changes in both flat and hierarchical views
- Support for Subversion 1.9
- Improved clone performance for large projects in Git when using Xcode Server
- Faster log and blame views
- Faster SCM status for files

- Ability to choose background testing user for running integrations, including support for testing as a Standard or Administrator user
- Support for overriding toolchain settings on a bot
- Automatically runs upgrade integrations after Xcode updates to help isolate issues
- Enhanced issue tracking and communications:

  – Improved issue blame and tracking over time

  – Integrations that track bot configuration changes over time, and that can attribute issues to those changes
- Improvements to triggers:

  – Triggers able to be renamed, reordered, and duplicated

  – Support for new issue emails and daily/weekly digest email reports

  – New email notification settings available— to filter recipient domains, set a custom “From:” address, and include server information

Xcode 8.2 requires a Mac running macOS OS X 10.11.5 or later.

You obtain Xcode 8.2 from the Mac App Store. It is a free download that installs directly into the Applications folder. By default, Xcode downloads developer documentation in the background for offline reading; it also automatically downloads documentation updates. This behavior can be changed after installation using the Downloads preferences pane.

The Apple Developer Program provides access to the App Store, Mac App Store, and Apple TV App Store, additional support and documentation, and signing resources for testing and deployment on Apple TV, Apple Watch, iPad, iPhone, and iPod touch devices. For more information, visit the [Apple Developer Program website](https://developer.apple.com/programs/).

Visit [Apple Developer Forums](http://devforums.apple.com/) for discussions about any Apple developer software, including prerelease products.

For the latest security information, visit [http://support.apple.com/kb/HT1222](http://support.apple.com/kb/HT1222).

A software development kit (SDK) is a collection of frameworks (libraries, headers, and resources) that represent the API for a specific watchOS, iOS, or macOS version. Most of the functionality your app gets from an SDK is actually provided by the host operating system, which makes the right Base SDK and OS Deployment Target settings that are critical for app compatibility. Xcode automatically builds with the latest SDK and targets the latest OS.

If your app doesn’t require the latest OS features, you can configure it to run on a previous version of the platform operating system using the OS Deployment Target option in the Xcode Project settings. If your project was created in an older version of Xcode, you can let Xcode update your project. For details on this feature, see [Project Modernization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmzvfvjvomzw).

Changes to the signing processes may impede your development if you're working on an older project that has not been updated to the current signing process.

The recommended approach for both enterprise and App Store developer accounts is to use automatic signing in Xcode to code sign apps during both development and distribution. See [Xcode Help](http://help.apple.com/xcode) for documentation on automatic signing. If you have an older project that is not configured to use automatic signing, read [Technical Q&A (QA1814) "Setting up Xcode for Automatic Provisioning"](https://developer.apple.com/library/ios/qa/qa1814/_index.html#//apple_ref/doc/uid/DTS40014030) to learn the procedure enabling you to reconfigure your Xcode project.

Automatic signing should be considered before using other techniques, but if your projects do require manual signing, search for “manually sign” in [Xcode Help](http://help.apple.com/xcode) to review current manual signing practices.

When you open a project, Xcode evaluates it to see whether any settings should be updated. This feature provides an easy way to make sure your projects conform to the latest SDKs and best practices.

Open the issue navigator to see whether anything in your project needs to be updated. You can also select the project in the project navigator, and then choose Editor > Validate Settings.

If the issue navigator lists modernization issues, click the issue to see a dialog that explains the updates that should be made and that lets you perform any or all of them.

After you have clicked Perform Changes, regardless of whether you choose to make all the changes, Xcode does not show the warning again. To rerun the check, select your project in the project navigator and choose Editor > Validate Settings.

To learn more about using Xcode, choose Help > Xcode Help.

[Next](New%20Features%20in%20Xcode%207.md)[Previous](What%27s%20New%20in%20Xcode%209.md)

