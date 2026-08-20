---
title: What’s New in Xcode
apple_id: TP40004626
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/WhatsNewXcode/Chapters/xcode_4_0.html
archived_at: '2026-07-15T07:27:10.516295Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [What’s New in Xcode](What%27s%20New%20in%20Xcode%209.md)


[Next](Document%20Revision%20History.md)[Previous](New%20Features%20in%20Xcode%205.md)

# New Features in Xcode 4

- [Xcode 4.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvooi) adds features to support OS X v10.7 Lion as well as other enhancements to the application.
- [Xcode 4.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvomjq) adds features to support iOS 5 as well as other enhancements to the application.
- [Xcode 4.3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvomq) adds features to support iOS 5.0 and OS X v10.7, as well as other enhancements to the toolset.
- [Xcode 4.3.1 and 4.3.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvomy) adds support for the updated iOS SDK 5.1.
- [Xcode 4.3.3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvona) provides an update to the included OS X SDK.
- [Xcode 4.4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvomjr) adds features to support OS X v10.8 and iOS 5.1 as well as other enhancements to the toolset.
- [Xcode 4.5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvomjs) adds support for development with iOS 6 SDK and includes additional features.
- [Xcode 4.6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvoni) adds support for development with the iOS 6.1 SDK and includes new features for the compiler and debugger.
- [Xcode 4.6.1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvonq) supports development with OS X 10.8.3 SDK and provides compatibility for ARC in projects targeting OS X 10.6.
- [Xcode 4.6.2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvony) is a maintenance release responding to developer reported issues and Apple QA testing input.
- [Xcode 4.6.3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dcnbxfvjvooa) fixes an issue where debugging in the iOS Simulator could hang on OS X 10.8.4.

Xcode 4.1 adds features to support OS X v10.7 Lion as well as other enhancements to the application.

This article describes the new features in Xcode 4.1. For details on how to use these features, see [Xcode Help](http://help.apple.com/xcode).

When you open a project, Xcode 4 evaluates it to see whether there are any settings that should be updated. This feature provides an easy way to make sure your projects conform to the latest SDKs and best practices.

Open the Issue navigator to see whether anything in your project needs to be updated. You can also select the project in the project navigator and choose Editor > Validate Settings.

If the Issue navigator lists modernization issues, click the issue to see a dialog that explains the updates that should be made and lets you perform any or all of them.

After you have clicked Perform Changes, whether you choose to make all the changes or not, Xcode does not show the warning again. To rerun the check, select your project in the Project navigator and choose Validate Settings from the Editor menu.

The default compiler for iOS development in Xcode 4.1 is LLVM-GCC 4.2. Compared with the GCC compiler that was the default in Xcode 4.0, LLVM-GCC provides better code generation and optimization than GCC, while being exactly source compatible with GCC 4.2.

The Behaviors preferences pane lets you specify what should happen when a variety of events occur. Xcode 4.1 introduces new Behavior options, such as running a script, collapsing and expanding the navigator and utilities panes and the toolbar, or switching to Full Screen mode. This feature greatly expands the power of Xcode behaviors, enabling Xcode to run a script or perform a variety of actions in response to a large number of triggers.

You can also can design custom behaviors by defining behaviors that are triggered by menu items or their key equivalents. This feature allows you to create behaviors that you can invoke at any time. Once you’ve created a behavior, it appears in the Xcode > Behaviors menu.

To assign key equivalents to custom behaviors, in the Key Bindings preferences pane, select the Customized tab to find the behavior for which you want to assign a key equivalent.

Xcode 4.1 introduces commands in the Product > Generate Output menu to process source files and generate the preprocessed output or assembly output.

The preprocessor evaluates directives in your source code (instructions starting with the pound sign (#) such as includes, defines, and conditional logic) and converts them into C code to be sent to the compiler. You can examine the preprocessed output to make sure that the logic in your source code is being interpreted by the preprocessor as you expect in order to debug compilation problems.

The assembly output is the set of instructions that the compiler generated from the preprocessed output. You can study the assembly output to see how the instructions were formed or ordered, to seek out better optimization patterns, or to look for compiler bugs.

The output type is also a new category in the assistant editor for a selected primary file.

Interface Builder in Xcode 4.1 adds support for the new AppKit Autolayout feature. Autolayout, available starting with OS X v10.7 Lion, uses relationships called _constraints_ to govern the layout of objects in the user interface. This feature is a complete replacement for the autoresizing mask. As you make changes to any view or control in Interface Builder (move it around, resize it, change an attribute, add a subview, and so forth), Interface Builder automatically adds and removes constraints based on the new layout. When you enable this feature, Interface Builder shows the constraints as you work.

Autolayout is enabled per nib. To start using Autolayout, select the Use Autolayout checkbox in the File inspector for each nib. When you enable Autolayout, Xcode updates your build settings, if necessary, to ensure your deployment target is OS X v10.7 or greater. For nib files in projects that had been targeted for OS X v10.6 or earlier, Interface Builder adds constraints to your nib files automatically when you enable Autolayout.

You can edit an automatic constraint or add your own. To add a constraint, select the view or views for which you want to add the constraint and choose a constraint from the Editor > Add Constraint menu.

You can delete a user constraint, but not an automatic constraint. Rather than trying to delete automatic constraints, create the constraints you want.

There is often a need to access values from the target build settings in pre- and post-action scripts (similar to the way shell script build phases work). This enhancement allows a pre- or post-action script to define the target build settings to use via a pop-up menu in the scheme editor’s pre- and post-action panes.

An application sandbox enforces restrictions, known as _entitlements_, on how an application can interact with the rest of the system. A sandboxed application is harder to compromise and therefore enhances security for users. For example, if your application has no need to have access to the network, you can specify that the application’s sandbox should prohibit network access. Then if a hostile hacker manages to take over control of your application on a user’s computer, the hacker won’t be able to use the application to send email or connect to the internet.

The iOS platform has supported entitlements for a while, and with Lion, OS X does as well. With Xcode 4.1, the project editor provides a UI for setting up entitlements for OS X applications. You can set entitlements for each target in the project editor. There is also a default code-signing entitlements file available in the file templates in the utilities pane.

When you enable application sandboxing, you can select an entitlements file if you already have one. If you do not, Xcode creates one with the name of your project and the extension `entitlements`. You can view and edit this file with the property list editor in Xcode.

The debugger disassembly feature provides you the ability to select what kind of content you view when debugging: source only (when available), disassembly only, or source and disassembly. The disassembly is the set of assembly-language instructions seen by the debugger while your program is running. Viewing the disassembly can give you more insight into what your code is doing when it’s stopped at a breakpoint. By viewing the disassembly and source code together, you can more easily relate the instruction being executed with the code you wrote.

Choose Product > Debug Workflow to enable the disassembly-only display. The source and disassembly display is implemented as an Assistant category.

Support has been added in Xcode 4.1 for managing GIT remote repositories. You can select remote repositories from appropriate SCM workflows (such as push or pull). This feature enhances the ability of Xcode to be used for source control management.

With the Xcode 4.0 release, snapshots could not be restored on top of the current project content. The workflow for replacing the current version of your application with the version preserved in a snapshot involved restoring the snapshot, and then using the Finder to delete the current version and move the snapshot version into the appropriate folder. With Xcode 4.1, snapshots are automatically restored on top of the current version, unless you specify otherwise.

In Xcode 4.1, when you choose Restore Snapshot from the File menu and select the snapshot to restore, Xcode displays a preview dialog in which you can review the differences between the current version of the project and the snapshot version. When you click Restore, Xcode replaces the current version of the project with the version in the snapshot. Xcode makes a snapshot of the current version before replacing it.

To restore a snapshot in a new location instead of restoring on top of the current project, select the snapshot in the Projects pane of the Organizer window, choose the project you want to restore, and click the Export Snapshot button at the bottom of the window.

This feature provides visibility into internal project files (schemes, user interface settings, and so forth) when looking at SCM details in the SCM commit and update workflows. You can use this facility to save and keep track of versions of project files in the same way as you save and keep track of source files.

The popup menu for selecting schemes and run destinations has been changed to a path control, in order to provide you the ability to select either the scheme or run destination independently. You can still select both in a single gesture (using the submenus of the schemes). For projects or workspaces having a large number of schemes and several run destinations, this path control makes the menu much shorter and easier to deal with.

In Xcode 4.0, there was no default key binding to close a project or workspace. If you held the Option key when clicking the close box in the upper-left corner of the workspace window, all tabs, windows, and the project were closed, so that when you reopened the project, your previous set of windows and tabs did not reopen. In Xcode 4.1, the Command-Option-W key combination closes the project or workspace. Also, when you hold the Option key and click the close box, the project or workspace closes without first closing all windows and tabs. In this way, your window configuration is restored the next time you open the project.

If you used Interface Builder plug-ins in Xcode 3, you can continue to build and run your project in Xcode 4, and you can update your project to make your nib files editable in Xcode 4.

Xcode 4 provides limited support for Interface Builder 3 plug-ins. Specifically, you can build a project with Interface Builder plug-in dependencies, but you can’t edit the nib files. When you try to open a nib file with plug-in dependencies, Xcode 4 displays a dialog suggesting that you update the file. If you agree, Xcode converts the class of custom objects built with plug-ins to the nearest AppKit class. If the conversion isn’t possible, Xcode 4 provides a detailed error message. In that case, you must remove the plug-in dependency using Interface Builder 3 before you can edit the nib file in Xcode 4.

Xcode 4.2 adds features to support iOS 5 as well as other enhancements to the application.

Xcode 4.2 includes a menu item to convert targets to use Automatic Reference Counting (ARC), which automates memory management for Objective-C objects. ARC makes memory management much easier, greatly reducing the chance that your program will have memory leaks. First, Xcode reviews your project to determine whether there are items that cannot be converted (and that you must therefore change manually). Then, Xcode rewrites your source code to use ARC.

To initiate the process, enable Continue building after errors in the General Preferences pane, then choose Edit > Refactor > Convert to Objective-C ARC. The targets that you convert are updated to build using the Apple LLVM compiler. Xcode attempts to build your target and to determine what changes must be made to use ARC. If it finds any issues that prevent conversion, Xcode displays a dialog directing you to review the errors in the Issue navigator. After you correct the errors, choose the Convert to Objective-C Automatic Reference Counting menu item again to restart the ARC-conversion workflow.

When Xcode successfully builds your application, it takes a snapshot of the current code so that you can revert later if you want to. Then Xcode displays a preview dialog showing the changes it’s going to make. When you accept the changes, Xcode converts your code to use ARC.

For more information on ARC, see _[Transitioning to ARC Release Notes](../../../releasenotes/Objective%20C/Transitioning%20to%20ARC%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrw)_.

The default compiler for iOS development in Xcode 4.2 is LLVM 3.0. Compared with the GCC compiler that was the default in Xcode 4.0 and the LLVM-GCC compiler in Xcode 4.1, LLVM provides better code generation and optimization than GCC, along with newer language support than LLVM-GCC, including support for ARC in Objective-C and for the new C++ standard, C++0x.

In Xcode 4.2, the Interface Builder user interface for iOS app UI design is based on using storyboards, that is, images of view controllers populated with user interface objects and connected together with segues. Storyboards enable you to use Interface Builder to specify all the screens in your application, including the transitions between them and the controls used to trigger the transitions. With storyboards, you can lay out every possible path through your application graphically, greatly reducing the amount of code you need to write for a complex multiscreen application.

To create a project that uses view controllers, choose File > New > New Project and select the Use Storyboard checkbox in the options dialog.

You start with a view controller object that represents your first scene (the _initial view controller_). To get view controllers for your storyboard, select Objects and Controllers from the Object library and drag the view controllers you want onto the canvas. Each view controller manages a single scene. On the iPhone, each scene represents the contents of a single screen. For iPad applications, a screen can be composed of the contents of more than one scene.

To storyboard your application, you link each object that’s in a view controller and that can cause a change in the display, to another view controller that configures and implements the new scene. As you can see in the illustration below, the initial view controller has a green outline. You link the various view controllers in Interface Builder by Control-dragging between controls and view controllers. You can drag from any control that has an output to the header of any other view controller. You can add controls and views to each view controller’s view just as you would add objects to a window or a view in the nib file of an Xcode 3 or Xcode 4.0 application.

The arrows between view controllers represent the segues from one scene to another. To configure a segue—for example, to specify the kind of transition to use between scenes—click the arrow and open the Attributes inspector. To define a custom transition, select Custom for the style of the segue and fill in the name of your custom segue class. Standard segue classes are in UIKit (see _[UIKit Framework Reference](https://developer.apple.com/documentation/uikit)_). For information about implementing the methods in the `UIViewController` class, see _[UIViewController Class Reference](https://developer.apple.com/documentation/uikit/uiviewcontroller)_.

The result is a storyboard that graphically represents every screen of your application and the flow of control among the screens. Double-click the canvas to zoom out to see the entire storyboard.

The debugging experience has been updated to include a new workflow for debugging iOS OpenGL ES applications. When frame capture is enabled in the scheme for the application, the debug bar provides a new control for entering the OpenGL ES frame debugging view.

To enable this feature, you must run the application on a device and the device must be running iOS 5.0 or later. Set the destination in the scheme menu to an iOS device and choose Edit Scheme from the scheme selector in the toolbar. Select the Run action, click the Options tab, and select the OpenGL ES Enable Frame Capture checkbox.

When you build and run your OpenGL ES application, the debug bar includes a frame capture button. Click that button to capture a frame.

You can use Xcode 4.2 to:

- Inspect OpenGL ES state information.
- Introspect OpenGL ES objects such as view textures and shaders.
- Step through draw calls and watch the changes with each call.
- Step through the state calls that precede each draw call to see exactly how the image is constructed.

The debug navigator has a list of every draw call and state call associated with that frame. The buffers associated with the frame are shown in the editor pane, and the state information is shown in the debug pane.

You can step through draw calls in the debug navigator, or by using the double arrows and slider in the debug bar.

When you use the draw call arrows or slider, you can have Xcode select the stepped-to draw call in the debug navigator. To do so, Control-click below the captured frame and choose Reveal in Debug Navigator from the shortcut menu.

You can also use the shortcut menu to toggle between a standard view of the drawing and a wireframe view. The wireframe view highlights the element being drawn by the selected draw call.

Open the Assistant editor to see the objects associated with the captured frame. In the Assistant editor you can choose to see all the objects, only bound objects, or the stack. Open a second Assistant editor pane to see both the objects and the stack for the frame at the same time.

Double-click an object in the Assistant editor to see details about that object. For example, if you double-click a texture object, you can see the texture in detail.

In Xcode 4.0 and 4.1, you could simulate only the current location in your application. As of Xcode 4.2, you can simulate locations other than your current location in iOS applications that use Core Location. To set a location, choose Edit Scheme from the scheme selector in the toolbar, select the Run action, and click the Options tab. You can then choose a location from the Location menu.

In addition, if you are running an application for iOS 5.0 or later that uses Core Location, the debug bar has the same location drop-down menu.

To improve download time and installation efficiency with Xcode 4.2, the standard Xcode installer excludes some large tool components, such as older simulators, that are not essential to the current development toolset. Xcode presents you with a dialog when the simulator needs to be downloaded. Documentation preferences has consequently been replaced with Downloads preferences, including both documentation and components (simulators and SDKs). Using the Components tab of the Downloads preferences pane, you can view a description of each available component, download and install it.

This version of Xcode is distributed as a single application bundle, `Xcode.app`, installed through the Mac App Store directly to the Applications folder. Installing Xcode 4.3 no longer requires the Install Xcode application. These changes make it easier for you to install and update Xcode using the standard Mac App Store mechanism.

The Xcode 4.3 installation reorganizes other key development tools and allows launching them using the Xcode > Open Developer Tool menu. For your convenience, you can also add these tools to the Dock to allow direct access.

The command-line tools are not bundled with Xcode 4.3 by default. Instead, they can be installed optionally using the Components tab of the Downloads preferences panel.

The simplification afforded by repackaging Xcode 4.3 as a single app bundle eliminates the need for the `/Developer` directory containing prior versions of Xcode. As a result, the Install Xcode application and the `uninstall-devtools` command line script are also no longer needed.

Since the `/Developer` directory no longer exists with Xcode 4.3, some other parts of prior Xcode installations have moved.

__Sample Code.__ The three sample projects previously available in `/Developer/Examples`—TextEdit, Sketch and CircleView—have been moved to the Sample Code sections of the iOS and OS X Developer Libraries at [developer.apple.com](https://developer.apple.com/).

__Plug-ins, templates and other sub-components.__ Any path for component additions to developer tools that was previously found in a subdirectory of `/Developer` is now going to be located internal to the Xcode 4.3 application bundle. For example, Instruments templates—files such as `Automation.tracetemplate`—previously located in the `/Developer` subdirectory at `/Developer/Platforms/iPhoneOS.platform/…` is now stored in a similar path inside `/Applications/Xcode.app/Contents/Developer/…`.

__Other standalone utility applications and add-on technologies.__ Several additional tools are no longer part of the default Xcode installation, they are now downloadable as separate packages. The More Developer Tools menu command provides a direct jump to [developer.apple.com/downloads](https://developer.apple.com/downloads) in Safari where these development tools can be found.

The available downloads include:

- Audio tools: AULab, HALLab, and audio utility source code
- Accessibility tools: Accessibility Inspector, Accessibility Verifier
- Hardware IO tools: Bluetooth tools, IORegistryExplorer, USB Prober
- Graphics tools: CI Filter Browser Widget, OpenGL tools, Pixie, Quartz Debug, Quartz Composer tools
- Auxiliary tools: Clipboard Viewer, CrashReporterPrefs, Help Indexer, PackageMaker, Speech tools, SleepX
- Dashcode: Dashcode application

New Cocoa projects created in Xcode 4.3 now use Interface Builder’s Auto Layout feature by default. It can be disabled by deselecting an option in the Interface Builder design canvas:

Xcode 4.3.1 and 4.3.2 add support for iOS 5.1 and include the new features of Xcode 4.3.

Xcode 4.3.3 provides an update to the included OS X SDK, supporting new OS X v10.7.4 APIs. Otherwise, Xcode 4.3.3 offers no new features.

Additional improvements to Xcode robustness and reliability have been incorporated. See _[Xcode Release Notes — Archive](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/Introduction.html#//apple_ref/doc/uid/TP40016994)_ for more detailed update information.

Xcode 4.4 adds features to support OS X v10.8 and iOS 5.1 as well as other enhancements to the toolset.

Xcode includes an updated LLVM Compiler version 4.0 with the following enhancements.

- Literals syntax is supported for `NSArray`, `NSDictionary`, and `NSNumber` objects, using the same ‘`@`’ operator as for `NSString` literals.
- Subscripting is enabled for Objective-C containers, including `NSDictionary` and `NSArray`. Use the ‘`[ ]`’ syntax convention.
- Objective-C `@properties` are synthesized by default when not explicitly implemented.

Xcode supports backward deployment of code that uses the literal syntax and object subscripting to OS X v10.7 and later, you must use the OS X v10.8 SDK to make these features available. The default `@synthesize` feature requires no special SDK or runtime support.

- Lambda expressions are allowed and permit interoperability with blocks-based APIs in Objective-C++.
- Generalized initializer lists are supported.
- Generalized constant expressions (`constexpr`) are supported.

Xcode’s built-in source code analysis tool, launched with the Analyze command in the Product menu, is enhanced for common security mistakes in API and malloc usages.

- The static analyzer engine can find complicated bugs that span function boundaries using interprocedural analysis.
- More exhaustive memory checks are made to `malloc`-related memory management and the detection of insecure API uses.

Xcode’s Interface Builder includes support for new AppKit features.

- Autolocalization
- Improved trackpad API
- Auto Layout improvements
- CoreUI-based UI customization
- `NSView` API
- Paging control
- The addition of Page Control View

Xcode 4.4 introduces a viewer and editor for 3D scene files, included in a project as DAE documents, to support use of the Scene Kit API. The Scene Kit editor allows you to preview and fine-tune the 3D scenes, and play embedded animations. You can also inspect 3D scenes for information to use in your source code. The Scene Kit editor is invoked by selecting a DAE file in the project navigator.

Code completion now has an integrated form of QuickHelp with a short description of each item in the list based on the documentation or the specific code snippet. Integrated within the code completion window, it is displayed in a section either above or below the code completion list.

Xcode can offer symbols during code completion that haven't yet been included or imported in the current file (the framework was added to the project, but the `#import` was not included in the file). When possible, Xcode will use umbrella headers for auto import completions and will denote not-yet-linked symbols with a #error indicating which binary needs to be linked. It is a known limitation that auto import completions are available only for symbols that are already visible in at least one file in the current workspace. If necessary, this can be turned off in the Text Editing preferences.

Find and Search have been enhanced with three new capabilities:

- The Find Bar and Search Navigator have added support for find patterns as a simpler alternative to regular expressions. In the search field, click the magnifying glass icon and select Insert Pattern.
- The Find Navigator now supports searching for references to indexed symbols. Choose Symbolic from the Find Navigator's Style pop-up menu. This form of search performs significantly faster than textual searches and excludes results from comments and nonsource files.
- Xcode can show the callers and callees of the current function or method. This function is accessed from the Show Related Items menu, or by using the Assistant editor and selecting Callers or Callees in the jump bar pop-up menu.

The source editor jump bar pop-up menu now lists TODO and `#pragma mark` comments that are inside methods and functions.

Pinch-to-zoom and two-finger-double-tap change the zoom level in the following editors and viewers:

- User Interface editor
- Hex editor
- Core Data Model editor
- Quicklook editor
- OpenGL ES viewers
- Instruments track view

Three-finger-single-tap invokes QuickHelp.

Two-finger-swipe moves back and forth in the Xcode history.

Xcode 4.4 allows the OS X v10.8 systemwide notification system to display build and warning notifications.

Xcode 4.5 adds support for development with iOS 6 SDK and includes these additional features:

- LLDB is now the default debugger.
- LLDB supports hardware watchpoints on iOS devices.
- OpenGL debugging and performance analysis for iOS apps is integrated into Xcode.
- Auto Layout is supported for iOS 6.

Xcode 4.5 also extends new features released in Xcode 4.4 as listed below:

- Improved localization workflow using base language `.xib` files now supports OS X 10.8 in addition to iOS Storyboards.
- Objective-C literals syntax in `NSNumber`, `NSArray`, and `NSDictionary` classes are supported for iOS.
- Support for subscripting using `'[ ]'` syntax with `NSDictionary` and `NSArray` are supported and deploy back to iOS 5.
- Compatibility with the C++11 standard is improved with added support for lambda expressions.

For full details of Objective-C language feature availability, tools, and deployment capability, see _[Objective-C Feature Availability Index](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/ObjCAvailabilityIndex/index.html#//apple_ref/doc/uid/TP40012243)_.

For the compiler:

- Compilation warnings are added which assist in finding bugs when using ARC and weak references.
- `otool` is enhanced to support disassembly of Intel AVX instructions.
- The LLVM compiler now supports C++11 “user defined literals” and “unrestricted unions” features.
- The static analyzer has enhanced cross-function analysis for C++ and Objective-C methods. With this enhancement, the static analyzer can now find deeper bugs that cross method calls in Objective-C and C++ code. This new capability extends the cross-function analysis for C functions that was introduced in Xcode 4.5.

For the debugger:

- LLDB has been enhanced to read metadata from the Objective-C runtime. This enhancement greatly reduces the need to cast arguments and the results of message sends, and makes properties more often usable (particularly from system classes).
- LLDB has improved support for stepping over inlined functions. This improved support is particularly useful for `libc++` and `always_inline` functions like `NSMakeRange`.
- LLDB now prints function argument information in backtraces by default.
- LLDB now supports “thread return,” temporary breakpoints, and a variety of aliases to add common shortcuts from GDB.
- The elements of `NSArray` and `NSDictionary` objects can now be inspected in the Xcode debugger.

Xcode 4.6.1 is a maintenance release responding to reported developer issues and Apple qualification testing. Major highlights of this release include:

- Xcode 4.6.1 provides an update to the included OS X SDK, supporting new OS X v10.8.3 APIs.
- ARC compatibility has been ensured for projects targeting OS X 10.6

- The Xcode 4.6.2 release is a maintenance release responding to reported developer issues and Apple qualification testing.

- The Xcode 4.6.3 release fixes an issue where debugging in the iOS Simulator could hang on OS X 10.8.4.

Additional improvements to Xcode robustness and reliability have been incorporated. See _[Xcode Release Notes — Archive](https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/Introduction.html#//apple_ref/doc/uid/TP40016994)_ for more information.

[Next](Document%20Revision%20History.md)[Previous](New%20Features%20in%20Xcode%205.md)

