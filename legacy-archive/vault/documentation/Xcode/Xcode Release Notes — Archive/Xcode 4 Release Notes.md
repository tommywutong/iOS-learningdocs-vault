---
title: Xcode Release Notes — Archive
apple_id: TP40016994
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/xc4_release_notes.html
archived_at: '2026-07-26T19:54:16.604565Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Release Notes — Archive](Xcode%20Release%20Notes%20%E2%80%94%20Archive.md)


[Next](Document%20Revision%20History.md)[Previous](Xcode%205%20Release%20Notes.md)

# Xcode 4 Release Notes

## Xcode 4.6.3 Release Notes

### Resolved Issues

#### Debugging: LLDB

- Hang when debugging in iOS Simulator on OS X 10.8.4. 13722320

## Xcode 4.6.2 Release Notes

### Changes

#### Building: Kernel Extensions

- Kernel extensions (kexts) built with Xcode 4.6.1 and 4.6.2 fail to load on OS X 10.6 and 10.7, and this error message appears in the console:

  ```
  kernel: kxld: The Mach-O file is malformed: Invalid segment type in MH_KEXT_BUNDLE kext: 42
  ```

To build kexts that load on OS X 10.6 and 10.7, on the targets that build the kexts, set the OS X Deployment Target build setting to OS X 10.6. 13645170

### Resolved Issues

#### General

- Implemented stability fixes. 13518419, 13518436, 13518436, 13518526, 13611415

### New Issues

#### Code Signing: Kernel Extensions

- If you build code signed kexts on OS X 10.8.3 (you turn on code signing in the target that builds the kext), that kext fails to load on OS X 10.7.x and earlier, and this error message appears in the console:

  ```
  kernel: kxld: The Mach-O file is malformed: Invalid segment type in MH_KEXT_BUNDLE kext: 29
  ```

  Workarounds:

  - To build an unsigned kext that loads in OS X 10.7.x and earlier, in the target that builds the kext, set the Code Signing Identity build setting to Don’t Code Sign.

    If you need to build signed and unsigned versions of the kext, you can have in your project separate targets that build the same kext, one configured to code sign the kext and the other configured not to sign it.
  - To build a signed kext that loads in OS X 10.7.x and earlier, code sign the kext on a Mac running OS X 10.8.2 or earlier. 13428950

### Known Issues

#### Building

- When building a product previously built with Xcode 4.6.1 or earlier, the build fails with an error similar to this one:

  ```
  PCH file built from a different branch ((clang-425.0.27)) than the compiler ((clang-425.0.28))
  ```

  To address this issue, choose Product > Clean before building your product. 13663167

## Xcode 4.6.1 Release Notes

### New Features

#### General

- SDKs:

  OS X SDK 10.8.3 (13130441)

### Resolved Issues

#### Compiling

- Crash on launch on OS X v10.6 with apps using ARC built with Xcode 4.6. (13129783)

#### Accessing Help and Documentation

- Documentation doc set update fails with the message:

  ```
  Install path <path_1> points to a different documentation package <path_2> than expected <path_3>
  ```

  13292012.

### Known Issues

#### Accessing Help and Documentation

- More than one Xcode doc set listed in the Documentation organizer. 13207501

To address this issue delete any Xcode doc set whose version number is earlier than 509.12 from Documentation preferences:

1. Open the Xcode preferences window, and click the Downloads button to display Downloads preferences.
2. Click the Documentation button.
3. Select an Xcode doc set (titled “Xcode ...”).
4. Reveal the doc set info by clicking the Show Doc Set Info button (to the left of the + button).
5. If the version of the doc set is earlier than 509.12, delete the doc set by clicking the Remove (–) button.

## Xcode 4.6 Release Notes

### New Features

#### General

- SDKs:

  - OS X SDK 10.8
  - iOS SDK 6.1
- Device support (added):

  - iPad mini
  - iPad with Retina display (4th generation)

### Enhancements

#### Compiling:

- LLVM: New compiler warnings to help find subtle behavioral bugs when using automatic release counting (ARC) and weak references.
- LLVM: Support for the C++11 user defined literals and unrestricted unions.
- LLVM: Advanced optimization to merge disjoint stack objects and to reduce the size of allocated stack memory.
- LLVM: The Type-Based Alias Analysis (TBAA) code optimization is enabled by default.

  You can disable this optimization with the `llvm -fno-strict-aliasing` option.

  In Xcode projects, the Enforce Strict Aliasing build setting controls this capability.
- LLVM: Support for Microsoft-style inline assembly for i386 and x86_64.
- LLVM: Static analyzer supports deeper cross-function analysis of C++ and Objective-C code.
- `otool`: Support for disassembly of Intel AVX instructions.
- `otool`: Precisely decodes all instructions and skips over data entries in text segments.

#### Debugging

- Xcode UI: Inspects elements of [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) and [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) objects.
- LLDB: Reads metadata from the Objective-C runtime.
- LLDB: Improves support for stepping over inlined functions.
- LLDB: Prints function argument information in backtraces by default.
- LLDB: Supports “thread return,” the `temporary breakpoint` command, and a variety of aliases to add common GDB shortcuts.

### Changes

#### General

- DEPRECATED: LLVM-GCC compiler and GDB debugger.

  Xcode 4.6 is the last release to include the LLVM-GCC compiler and the GDB debugger.

  Use the LLVM compiler and the LLDB debugger, and file reports at [https://bugreport.apple.com](https://bugreport.apple.com) for issues that require the use of LLVM-GCC or GDB.
- DEPRECATED: Package Maker app.

  Use the `productbuild` command to create installer packages
- DEPRECATED: ATS.framework (OS X SDK 10.8).

  The use of the ATS API produces compilation warnings.

  In OS X v10.8 there is no loss of functionality, but there could be areas where performance degrades.

  Replace ATS code (including ATSUI) with Core Text calls (see _[Core Text Programming Guide](../../Strings%20Text%20Fonts/Core%20Text%20Programming%20Guide/About%20Core%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzt)_ for details).

## Xcode 4.5.2 Release Notes

### Resolved Issues

#### General

- Fixed Xcode app and LLDB debugger crashes reported on Xcode 4.5. 12482521, 12482518, 12481393, 12481829, 12481363, 12481302, 12481396, 12482364, 12514294, 12364375, 12481322, 12481370, 12481398, 12481373, 12489094, 12483605, 12481863, 12482083, 12482540, 12481426, 12482542, 12481390, 12482362, 12481885

#### Editing User Interfaces

- Improved stability when editing storyboards and using Auto Layout. 12482514, 12482536, 12482526, 12482548

#### Debugging

- Fixed an LLDB memory leak. 12483722
- Improved behavior when quitting iOS Simulator directly. 12481405

#### Distributing Apps

- Fixed occasional Xcode hang when submitting an app to the iOS App Store. 12482847

## Xcode 4.5.1 Release Notes

### Enhancements

#### General

- Improved the responsiveness of the Open Quickly dialog. 12251666
- Improved performance switching between tabs in the Xcode app. 12364395

#### Debugging

- Improved stability and responsiveness running apps on a simulator. 12388056, 12364385, 12364295

### Resolved Issues

#### Editing User Interfaces

- Crashes while editing user interface documents. 12364019, 12389062, 12388854, 12389040, 10261299

#### Editing Property Lists

- Issues adding keys to property list files. 12377407

#### Debugging

- Debug console doesn’t display all input characters. 12364400

#### Source Control

- Issues interacting with working copies known by the Xcode app. 12364258, 12389205, 12389198

## Xcode 4.5 Release Notes

### New Features

#### Editing User Interfaces

- The Interface Builder canvas includes a new button to toggle between iPhone screen layouts. When you click the button, Xcode resizes full-screen views to match the selected iPhone screen size. When the top level views are resized, Xcode uses the resizing rules specified by layout constraints or springs and struts in the size inspector to reflow the contained views. 12290237

  Use this button to toggle between layouts and ensure that the resizing rules you define work as expected on both the new Retina 4 screen and previous screen sizes.

#### Editing User Interfaces: Storyboards

- Storyboards now support view controller containment. You can add child view controllers to a parent view controller in a storyboard. At runtime, when the [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) method is called on the parent controller, its view hierarchy (composed of the view hierarchies of its child controllers) is already loaded. 9630246

  To add a view controller as the child of another view controller:

  1. Add a container view from the Object library.
  2. Connect the container view to the child view controller with an embed segue.

### Enhancements

#### General

- When Xcode autocreates schemes, it now adds the new schemes in project order (within the workspace) and target order (within each project). 7996506

#### Editing User Interfaces: Storyboards

- You can now specify that modal segues be presented without animation. 10384049
- You can now create unwind segues that allow transitioning to existing instances of scenes in a storyboard. 9211697.

  With earlier releases of Xcode, you may have implemented unwind segues programmatically. See [iOS SDK Usage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqmznknltembq) for details.

#### iOS SDK Usage

- When your app runs on iOS 6.0 or later, in the [shouldPerformSegueWithIdentifier:sender:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621502-shouldperformseguewithidentifier) method of your [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) subclass, you can decide whether to trigger a segue with a specific identifier, which you set in the segue’s Attributes inspector. 9447109

#### Source Control: Subversion

- When you update your Subversion-managed project, Xcode now automatically applies the update if there are no conflicts. 11913482

  To see changes from the repository before applying them, choose File > Source Control > Update while holding down the Control key.

### Changes

#### General: iOS

- This version of Xcode does not generate armv6 binaries. 12282156
- The minimum deployment target is iOS 4.3. 12282166
- In this Xcode release, Auto Layout is turned on for new user interface documents (storyboards and nib files). Because Auto Layout requires iOS 6.0, using such user interface documents on earlier iOS releases results in a crash or other undefined behavior. 12289644

  For your app to run on earlier iOS releases, turn off Auto Layout in its user interface documents.

#### Distributing Apps: IOS

- This release of Xcode doesn’t allow submitting to the App Store apps with iOS Deployment Target set to iOS releases earlier than iOS 4.3. The validation process fails with the message “This bundle is invalid. The key UIRequiredDeviceCapabilities in the Info.plist may not contain values that would prevent this application from running on devices that were supported by previous versions.” 12309358

  Set the app’s iOS Deployment Target to iOS 4.3 or later.

#### Creating Projects

- Projects created using this Xcode release use the new libc++ implementation of the standard C++ library. The libc++ library is available only on iOS 5.0 and later and OS X 10.7 and later. 12221787

  To enable deployment on earlier releases of iOS and OS X in your project, set the C++ Standard Library build setting to libstdc++ (Gnu C++ standard library).

#### Managing Devices

- Uploading app data files to an iOS device works correctly on OS X v10.7 and v10.8. 12017933

#### Source Control

- RCS and CVS are deprecated in this Xcode release. 12252058

#### Installing

- Starting in Xcode 4.3, the `Xcode.app` file package contains all the Xcode developer tools. The man pages for the command-line tools Xcode uses are also placed in this package. However, these man pages are not included in the places searched by the `man` command. To access these man pages, you must add them to the index of man pages used by the `man` command. 10658081

  To add the Xcode man pages to the man-page index:

  1. Construct `MANPATH` for the `Xcode.app` package you’re using by executing these shell commands:

     ```
     #!/bin/tcsh
     set xcodeManPathsTmp=/tmp/Xcode

     # Expect to find Xcode.app in /Applications
     find /Applications/Xcode.app -name man >! $xcodeManPathsTmp
     sudo cp $xcodeManPathsTmp /etc/manpaths.d
     ```
  2. Set the `MANPATH` environment variable in your command shell:

     - C-Shell

       Edit `/etc/csh.login` by adding this line before the <code>`if ( -x /usr/libexec/path_helper ) then` line:

       ```
       setenv MANPATH ""
       ```
     - Bourne Shell

       Edit `/etc/profile` by adding this line before the `if [ -x /usr/libexec/path_helper ]; then` line:

       ```
       export MANPATH=""
       ```

       The `path_helper` command adds the paths in the `manpaths.d` file to the `PATH` and `MANPATH` environment variables.

       __Alternative:__ Edit the shell startup files in your home directory to execute this command:

       ```
       /usr/libexec/path_helper -s
       ```
  3. Open a new shell window, and verify that `MANPATH` lists the paths to the `Xcode.app` package you’re using.
  4. Index the man pages by executing this shell command:

     ```
     sudo /usr/libexec/makewhatis
     ```

### New Issues

#### Editing User Interfaces

- When you add a gesture recognizer in a storyboard, it mistakenly overrides the system-supplied gesture recognizers for the target view. For example, adding a tap gesture recognizer to a table view results in a table view that does not scroll. 12200238

  Disconnect the gesture recognizer in the storyboard, and apply it in code.

#### Performance Measurement and Analysis: Instruments

- A UI automation script being run with a simulator target in Instruments fails if your Mac contains multiple copies of Xcode and the Xcode install path is not set up correctly. 12288632

  Determine the path to the running Xcode instance by executing this shell command:

  ```shell
  $ xcode-select --print-path
  ```

  If the returned path doesn’t point to the running Xcode instance, execute this shell command:

  ```shell
  $ xcode-select -switch <path_to_the_Xcode_package>
  ```

  - In the command, `<path_to_the_Xcode_package>` is the path to the `Xcode.app` package you’re using—for example, `/Applications/Xcode.app`.

### Known Issues

#### General

- Xcode may not show any windows when it’s launched. This happens when you download Xcode from [https://developer.apple.com](https://developer.apple.com) and the “Close windows when quitting an application” preference in System Preferences is unselected. 11865559

  Switch to another app and relaunch Xcode.

#### Editing Core Data Models

- MobileMe syncing support is deprecated. However, the `syncable` property is still set to `YES` by default in the User Info Dictionary for entities and properties, but the model editor doesn’t show this setting. 10787672

  To explicitly set `syncable` to `NO` for an entity or a property, add a key-value pair in your User Info Dictionary:

  1. Select the entity or property for which you want to turn off synching on a model file.
  2. In the User Info section in the Data Model inspector, add this key-value pair:

     |  |  |
     | --- | --- |
     | key | `"com.apple.syncservices.Syncable"` |
     | value | `"NO"` |

#### Editing Source Code

- Text and font rendering on OS X v10.8 is optimized for Retina display. On a non–Retina display running OS X v10.8, some font configurations can appear blurry in Xcode. 11486875

  Switch back to non–Retina display optimized text and font appearance in Xcode by entering this command in Terminal:

  ```
  defaults write com.apple.dt.Xcode NSFontDefaultScreenFontSubstitutionEnabled -bool YES
  ```

#### Localization

- When you select the Use Base Internationalization option in the project editor, Xcode generates strings files for each your project’s user interface documents. 11462724

  To resynchronize your strings files with new content from your user interface documents, use the `--generate-strings-file` option of the `ibtool` command to produce new strings files. Then, manually merge the new files into your existing localized strings.

#### Autolayout: Runtime

- At runtime, when adding subviews to a split view while loading both views from nib files, you may see log messages about unsatisfiable constraints because of autoresizing mask constraints on the split view panes. These are benign log messages because a split view automatically fixes the problem after adding the subview. 11614767

  In your code, before adding the subview to the split view, send `setTranslatesAutoresizingMaskIntoConstraints:NO` to the subview.

#### Debugging: LLDB

- The `po`, `print`, and `expression` commands cannot access enumerators directly. You must use the name of the enumeration. 11485295

  For example, if your code contains `enum MyEnum { e1, e2 };`, LLDB emits an error if you type `print e1`. Instead, type `print MyEnum::e1`.

## Xcode 4.4.1 Release Notes

### Changes

#### Distributing Apps

- Xcode no longer preserves an app’s designated requirements when you submit it to the App Store. 12006125

  Some apps where prevented from submission because of designated requirements.

### Resolved Issues

#### Debugging

- After quitting iOS Simulator directly, Xcode continues to show the process launched on the simulator as running. 11998376

#### Editing Source Code

- Xcode doesn’t offer code completion in Objective-C++ files. 12006547

#### Compiling: LLVM

- The LLDB debugger gets the wrong address for some variables. 12006552
- When compiling an Objective-C++ file in C++11 with vectors under automatic reference counting (ARC), the LLVM compiler generates incorrect code. 12006560
- Objective-C code compiled under ARC and optimized for size may crash at runtime. 12006567

#### Unit Testing

- Xcode becomes unresponsive while running unit tests. 12017975

### Known Issues

#### Managing Devices

- Uploading app data files to an iOS device may not work. 12017933

  - On OS X v10.8, duplicate the `.xcappdata` file, and upload the duplicate.
  - On OS X v10.7 there is no workaround to this issue.

## Xcode 4.4 Release Notes

### New Features

#### General

- You can drag file, directory, and group icons from the jump bar to the project navigator, a Finder window, and other apps. 7452760
- The Use Base Internationalization setting in the project editor works only on Mac products for deployment on OS X v.10.8 and later. Xcode must also be running on OS X v.10.8 or later. This setting is not supported on iOS projects. 11712855

#### Editing Source Code

- The source editor can remove trailing whitespace at the end of a line after you have edited it. You control this behavior with the “Automatically trim trailing whitespace” option in Text Editing preferences. 2535591
- When the “Automatically insert closing braces” option in Text Editing preference is turned on, as you type an opening parenthesis, brace, or quotation mark, the source editor adds the corresponding closing character. When the “Enable type-over completions” option is turned on, the editor adds the closing character in a state in which you can type over the character. This feature reduces the appearance of duplicate closing characters, such as when you type both the open and close characters quickly. 3780948

  Press Tab to jump over the closing character.

#### Compiling: ARM

- __LLVM integrated assembler for ARM.__ This new assembler improves compilation times for iOS products, and provides better user level diagnostics for ARM assembly code. This assembler uses only Unified Assembly Language (UAL) assembly code; therefore, you may need to update projects that use manually generated assembly code. 9136376

  Use the `clang``-no-integrated-as` command-line option in projects with substantial Divided Syntax assembly code while transitioning to UAL.

### Enhancements

#### Editing Source Code

- During a code completion interaction, Xcode gives higher priority to completions you have used recently. 9790948

#### Editing Property Lists

- You can view and modify the root object of a custom property list file. 8635494

#### Creating Projects

- When creating a project, you can choose whether to add it to a workspace or create a standalone project. 8032086

### Resolved Issues

#### Editing User Interfaces

- When you hold down Option and place the pointer over views in the canvas, the distance values are not obscured by other elements, such as the resizing handles. 8204499

#### File System

- You can rename a file just by changing the case of one of the letters in its filename, even on a case-insensitive file system. 7846036

### New Issues

#### General

- A failure to rebuild precompiled header (PCH) files causes syntax highlighting, code completion, and Command+click navigation to behave incorrectly. 11538640

  Delete the PCH index folder.
- Xcode may not show any windows when it’s launched. This happens when you download Xcode from [https://developer.apple.com](https://developer.apple.com) and the “Close windows when quitting an application” preference in System Preferences is unselected. 11865559

  Switch to another app and relaunch Xcode.

#### Editing Source Code

- Text and font rendering on OS X v10.8 is optimized for Retina display. On a non–Retina display running OS X v.10.8, some font configurations can appear blurry in Xcode. 11486875

  Switch back to non–Retina display optimized text and font appearance in Xcode by entering this command in Terminal:

  ```
  defaults write com.apple.dt.Xcode NSFontDefaultScreenFontSubstitutionEnabled -bool YES
  ```

#### Editing Core Data Models

- MobileMe syncing support is deprecated. However, the `syncable` property is still set to `YES` by default in the User Info Dictionary for entities and properties, but the model editor doesn’t show this setting. 10787672

  To explicitly set `syncable` to `NO` for an entity or a property, add a key/value pair in your User Info Dictionary:

  1. Select the entity or property for which you want to turn off synching on a model file.
  2. In the User Info section in the Data Model inspector, add this key/value pair:

     |  |  |
     | --- | --- |
     | key | `"com.apple.syncservices.Syncable"` |
     | value | `"NO"` |

#### Localization

- When you select the Use Base Internationalization option in the project editor, Xcode generates strings files for each your project’s user interface documents. 11462724

  To resynchronize your strings files with new content from your user interface documents, use the `--generate-strings-file` option of the `ibtool` command to produce new strings files. Then, manually merge the new files into your existing localized strings.

#### Debugging: LLDB

- The `po`, `print`, and `expression` commands cannot access enumerators directly. You must use the name of the enumeration. 11485295

  For example, if your code contains `enum MyEnum { e1, e2 };`, LLDB emits an error if you type `print e1`. Instead type, `print MyEnum::e1`.

#### Autolayout: Runtime

- At runtime, when adding subviews to a split view while loading both views from nib files, you may see log messages about unsatisfiable constraints because of autoresizing mask constraints on the split view panes. These are benign log messages because a split view automatically fixes the problem after adding the subview. 11614767

  In your code, before adding the subview to the split view, send `setTranslatesAutoresizingMaskIntoConstraints:NO` to the subview.

## Xcode 4.3 Release Notes

### Resolved Issues

#### General

- Xcode crashes when dragging tabs in full-screen mode. 9987358
- Xcode crashes when opening multiple workspaces that contain the same folder reference (blue folder). 10079252

#### Installing

- Installing Xcode on OS X v10.7.3 or later breaks the Xcode 4.3 Instruments app. 10619572

#### Editing User Interfaces

- After enabling autolayout in a nib file, the wrong constraints are applied. 8201103
- When resizing views that use autolayout, Xcode applies constraints to the descendants of the view being resized, but not to its siblings and ancestors. 9450655
- Xcode doesn’t allow constraints with negative values. 9717632
- When you create a user constraint, Xcode removes redundant constrains, which is not always desirable. 9794979
- You cannot add width and height constraints to top-level views. 9877773

#### Building

- Xcode imports incorrect header in projects containing targets that produce different header files with the same name. 8201103
- A build may hang if Xcode encounters a build error and the “Continue building after errors” option in general preferences is turned on. 10642885

### Known Issues

#### General

- The App Store app cannot install Xcode in the `/Applications` directory because there are beta releases of Xcode in that directory.

  Do not install beta releases of Xcode in the `/Applications` directory. 10824869

#### iOS SDK Support

- Xcode cannot launch your app on a device for debugging after you install the iOS 3.x device debugging support component.

  Unplug and plug-in your device to your Mac, and ensure that you build your app for the armv6 architecture. 10538662

#### Editing Source Code

- Xcode doesn’t show code-completion suggestions when there are mismatched braces.

  Turn on the “Automatically insert closing "}"” option in text editing preferences to reduce the number of mismatched braces. 10775381

#### Debugging

- Some debugger commands and log expressions in breakpoints fail when using the LLDB debugger because Xcode uses the wrong frame when executing the debugger command or evaluating the log expression.

  If you know what thread the the debugger command or log expression must run relative to, add a breakpoint action that sets the current frame to the appropriate one before the breakpoint action with the problem. 10426977

#### Debugging: LLDB

- The variables pane in the debug area does’t display correctly the child values of variables with dynamic types (Objective-C object pointers and virtual C++ pointers).

  Use the console pane in the debug area: enter the commands `frame variable *self` or `frame variable *this` to the values.10658091
- LLDB cannot be used to debug apps on devices running iOS 3.x or iOS 4.x.

  Set GDB instead of LLDB as the debugger in the scheme that builds your app. 10776590

#### Performance Measurement and Analysis

- When there are more than one Xcode releases installed on your Mac, Xcode 4.3 may not find your app’s symbols when displaying crash reports and the trace data for instruments.

  To enable Instruments to find your app’s symbols when displaying trace data:

  1. In Instruments, choose File > Re-symbolicate Document.
  2. Search for you app’s name, and locate it in your app’s build directory, such as `~/Library/Developer/Xcode/DerivedData/<MyApp>`. 10552213
- You cannot run System Time Profile from the Instruments icon in the Dock by Control-clicking the icon and choosing System Time Profile.

  Control-click the Instruments icon in the Dock, and select the Allow Tracing of Any Process option. 10755622

#### Source Control and Snapshots

- When Xcode attempts to authenticate Subversion repositories that require approval of a server certificate, one or more `svn` processes hangs.

  Authenticate the server in Terminal. 10042297

## Xcode 4.2 Release Notes

### Installation

- You can install Xcode 4.2 for OS X v10.6 Snow Leopard only if you have purchased an earlier release of Xcode.

  Install or update Xcode through the Purchases or Updates panes.
- If you purchased Xcode from the Mac App Store, the Install Xcode app is on the volume on which you installed Xcode.

  To install Xcode 4.2 on another volume, you must delete all copies of the Install Xcode app from your file system.

### Xcode

- In Xcode 4.2 with iOS 5, support for running and debugging applications in the iOS 4.3 Simulator and on devices with iOS versions older than 4.2 is optional and installed only on demand. In addition, this support is no longer shipped as part of the core tools packaging, and is instead made available for download and installation through the "Downloads" pane of the Xcode Preferences panel. A valid iOS developer ADC account is required to obtain this content.

  To obtain the iOS 4.3 Simulator, choose More Simulators from the Run Destinations popup in the main toolbar. This item presents the Downloads pane of the Preferences and includes UI to initiate the installation of the simulator.

  To obtain iOS device support for pre-iOS 4.2 devices, connect a device and activate it for development in the Organizer. Xcode prompts you to initiate the download of the device support components.

  If Xcode 4.2 in iOS 5 is installed over a previous Xcode 4.2 beta or over Xcode 4.1, the iOS 4.3 Simulator and device support from the previous install will already be present, and the additional components will display as "Installed" in the Downloads pane of the Xcode Preferences.

  The installation packages for the downloaded components are stored in `~Library/Developer/Xcode`. When a new version of Xcode (beta or GM) is installed, subsequent requests to install these components use the local packages without requiring a new download.
- In some cases, Xcode 4.2 Organizer does not display a device that is in restore mode. As a workaround you can use iTunes to restore.
- In iOS 5, iOS Simulator is not compatible with previous releases of the iCloud Developer Seed for OS X. It is highly recommended that you update to the latest iCloud Developer Seed to ensure compatibility.
- The iOS 5 SDK supports both iOS 4.3 and iOS 5.0 simulators.
- Be sure to quit any running Xcode before starting the uninstall-devtools script.
- The Network Link Conditioner daemon cannot be launched after installing the Networking Link Conditioner preference pane without first rebooting the system. As a result, the tool will not function without a system reboot.

  If you do not want to reboot the system, you can issue the following command from Terminal instead: `sudo launchctl load /system/library/launchdaemons/com.apple.networklinkconditioner.plist`
- If you are using multiple tabs in Xcode 4.2, some behaviors that are dependent on the Run Generates Output and Run Completes events may not get triggered. This bug will be fixed in future versions.

### Interface Builder

- When initiating a refactoring rename operation from the declaration of a property, any Interface Builder files that refer to that property will not be updated correctly. Instead, perform the rename operation on a usage of the property, or an associated `@synthesize` statement.
- In Xcode 4.2, when copying views (either a single view or multiple views), both the user defined constraints on the selected view and the user defined constraints between the views are copied to the pasteboard.
- When developing Mac apps, changing the segment style of an `NSSegmentedControl` object to Automatic might crash in documents using Cocoa Auto Layout. To workaround the issue use an explicit segment style such as Round or Textured, and at runtime, change the segment style to automatic using the `setSegmentStyle:` method.

### Instruments

- There is a known issue with the Profile action from Xcode 4.2. After a build in which no source files have changed, Instruments will be unable to gather symbols for the target application.

  This affects projects where both:

  1. The Release configuration is selected for the Profile action. (default)
  2. The Strip Linked Product build setting is set to "Yes”, or a custom Run Script build phase strips the product. (non-default)

  The workaround is to do any one of the following:

  1. Perform a "Clean" on the product before initiating the Profile action.
  2. Do a Clean of the product and temporarily set the Strip Linked Product build setting to "No" while Profiling.
  3. Set the configuration of the Profile action to Debug.
  4. Run successive profiles directly from within Instruments when you do not need to rebuild.
- When developing Mac apps, using the GC Monitor template in Instruments may cause Instruments to crash. To workaround the problem please consider migrating your application to ARC.

### iOS Simulator

- When running Mac OS 10.7, Location Services are not functional in iOS simulator when simulating iOS 4.3 and earlier. This issue is not present when running Mac OS 10.6 or when simulating iOS 5.0.

## Xcode 4.1 Developer Preview 1 Release Notes

### New Features

#### Editing Nib Files

- You can create and edit view-based `NSTableView` instances.

  Just drag an `NSView` subclass (usually `NSTableCellView`) from the Object library into each table column. After connecting the datasource and delegate outlets, implement at least these methods:

  - `– (NSInteger)numberOfRowsInTableView:(NSTableView *)tableView`
  - `– (id)tableView:(NSTableView *)tableView objectValueForTableColumn:(NSTableColumn *)tableColumn row:(NSInteger)row`

  You can bind the `objectValue` property of an `NSTableCellView` instance in Interface Builder. You can also make action connections from a cell to the cell’s owner, which is usually the table view’s delegate.

  By assigning identifiers to the view cells, you can use the `NSTableView` method `–makeViewForIdentifier:owner:` in the implementation of the table-view delegate method `–viewForTableColumn:row:`. 7465869

### Enhancements

#### General

- If Xcode or `xcodebuild` fail to launch:

  - Hold down Shift while launching Xcode
  - Use the `xcodebuild -clearPlugInCache` option. 9013457

#### Editing Nib Files

- Building products that require Interface Builder 3 plug-ins may fail because the `ibtool` command-line tool is unable to locate the required `ibplugin` plug-in.

  If you have the Xcode 3 toolset installed on your computer, load the plug-in using the Interface Builder 3 preferences window. Otherwise, use this command:

  ```
  defaults write com.apple.InterfaceBuilder3 "IBKnownPluginPaths.3.2.7" -dict-add "<plug.in.identifier.string>" "<path_to_ibplugin>"
  ```

  8920581

### Changes

#### Building: xcodebuild

- The `xcodebuild -activetarget` option is not supported. 8361726

#### Performance Measurement and Analysis

- MallocDebug is replaced by the Allocations and Leaks instruments, and the `libgmalloc` (GuardMalloc) and `leaks` command-line tools. 4388187

### New Issues

#### Performance Measurement and Analysis

- When using the OS X Core Data template, Instruments may hang or stop tracing. 9031942
- When you profile an application running in iOS Simulator, Instruments collects no data.

  To have Instruments collect data, click the Instruments icon in the Dock after it starts recording. 8909180

### Known Issues

#### General

- Nib files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the nib file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406

#### Editing Nib Files

- Xcode disallows dragging objects in the Interface Builder canvas to the Object library. 8656363

#### Unit Testing

- Projects that use the Xcode 3 unit-testing tools cannot use the Xcode 4 unit-testing infrastructure.

  To use unit testing in your Xcode 3 projects, set the Test After Build build setting to No. 8803198

## Xcode 4.0 GM Seed Release Notes

### Resolved Issues

#### Editing Nib Files

- __Refactoring:__ Xcode refactors Cocoa bindings. 8423815

#### Source Control and Snapshots

- On a project with no snapshots, new snapshots appear in the projects organizer. 8774085

#### Performance Measurement and Analysis

- Xcode 4.0 Developer Preview 6 installs a set of kernel extension with a version number of 9999, which hinders their upgrade.

  Before installing Xcode 4.0 GM Seed, perform these actions:

  - In Terminal, execute these commands:

    ```
    sudo rm -rf /System/Library/Extensions/AppleProfileFamily.kext/Contents/PlugIns/AppleIntelPenrynProfile.kext
    sudo rm -rf /System/Library/Extensions/AppleProfileFamily.kext/Contents/PlugIns/AppleIntelNehalemProfile.kext
    sudo touch /System/Library/Extensions
    ```
  - Install Xcode.
  - Restart your computer. 8844127

### New Issues

#### Editing Nib Files

- Xcode disallows dragging objects in the Interface Builder canvas to the Object library. 8656363

#### Unit Testing

- The unit-test command-line tools in `/Developer/Tools` are deprecated.

  To use unit testing in your Xcode 3 projects, set the Test After Build build setting to `NO`. 8803198

### Known Issues

#### General

- Interface Builder files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the Interface Builder file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406
- The task log viewer is empty when you select the last build task of a project or workspace in the log navigator and the viewer is set to show only recent operations.

  Set the task log viewer to show all operations. 8350930

#### Editing Nib Files

- Xcode cannot edit OS X–type Interface Builder documents comprised of objects from frameworks other than AppKit.

  You can compile and run these documents, however. 7470836

## Xcode 4.0 Developer Preview 6 Release Notes

### New Features

#### Performance Measurement and Analysis

- There is new command-line tool for measuring an application’s performance without launching the Instruments application: `iprofiler`. After making the measurements, you can analyze them with Instruments. A new framework, DTPerformanceSession (located in `/Library/Developer/4.0/Instruments/Frameworks`) allows your application to create performance measurements of itself or other applications. 7773305

### Enhancements

#### General

- In the Manage Schemes dialog you can specify whether to create schemes automatically with the “Autocreate schemes” option. You may want to turn off automatic scheme creation in a large workspace, where automatic scheme creation produces too many schemes. This setting is shared with all the users of the workspace.

  You can have Xcode create schemes with the Autocreate Schemes Now button. 7952053
- You can add an Xcode archive file (`.xcarchive`) to the archives organizer by double-clicking it in the Finder. 8791305
- You can use a workspace-relative location for derived data. 8242521

#### Task Information and Alerts

- Enhancements to the execution of alert scripts:

  - The scripts can access the Xcode user environment variables.
  - The value of the PWD environment variable is a path to the directory that contains the current project or workspace.
  - The new `XcodeAlertAffectedPaths` environment variable contains a colon-separated list of full paths to the affected files. This variable replaces the `IDEAlertAffectedURLs` environment variable. 8748528

### Resolved Issues

#### General

- Xcode doesn’t strip newline characters from the scripts in Run Script scheme actions. 8230045
- Duplicating a scheme doesn’t result in a new scheme with broken target references. 8335950
- When the active scheme is a unit-test scheme, clicking Run in the toolbar doesn’t produce an unknown error dialog. 8642393

#### Refactoring

- __Editing nib files:__ The Rename transformation renames action methods in Interface Builder documents when the action’s target is the first responder or the method is declared in a category, protocol, or a superclass of the given class. 8500272
- __Source Control and Snapshots:__ Xcode creates a snapshot of your workspace before performing a refactoring transformation. 7816256

#### Comparing Versions of a File

- After you create a branch and switch to it in the repositories organizer, using the commit dialog or the version editor doesn’t cause an assertion failure. 8383245

#### Source Control and Snapshots

- Xcode recognize SCP-based URLs (such as `git@example.com:/myrepositoryname.git`) for Git repositories in the repositories organizer. 8044145

#### Building

- After you change General preferences > Build Location, Xcode uses the new build location. 7965261

### New Issues

#### Performance Measurement and Analysis

- Multicore and Dispatch templates are not working. 8717719
- Time Profiler and System Trace don’t work after installing Xcode 4.0 Developer Preview 6.

  Restart your computer. 8829655
- If your computer contains more than one release of Xcode, the Dock time profiler doesn’t work correctly.

  Add the Instruments application in the appropriate Xcode release to the Dock and restart your computer. 8830062

### Known Issues

#### General

- Interface Builder files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the Interface Builder file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406
- The task log viewer is empty when you select the last build task of a project or workspace in the log navigator and the viewer is set to show only recent operations.

  Set the task log viewer to show all operations. 8350930

#### Editing Nib Files

- Xcode cannot edit OS X–type Interface Builder documents comprised of objects from frameworks other than AppKit.

  You can compile and run these documents, however. 7470836
- __Refactoring:__ Xcode does not refactor Cocoa bindings. 8423815

#### Searching

- __Search navigator:__ Xcode may crash in the replace preview dialog of the search navigator when all the found instances are selected and you click Replace. 8091532

## Xcode 4.0 Developer Preview 5 Release Notes

### New Features

#### General

- The build action in the scheme dialog allows you to choose which targets should be built for each scheme action. 8025069
- Each scheme action specifies the build configuration to use when Xcode performs that action as part of a build. Setting up a scheme with scheme actions that use particular build configurations allows you to, for example, set up a scheme that runs the product with the Debug configuration but profiles it with the Release configuration. 8090845
- The Build and Archive command archives the products of the targets selected in the active scheme for archival, including their dSYM files. You submit your products to iTunes Connect using these archives. You can also use them to symbolicate crash logs. 7696041
- The post-action scripts of archive scheme actions have access to information about the just-built archive in their environment:

  - `ARCHIVE_PATH`: The path to the archive.
  - `ARCHIVE_PRODUCTS_PATH`: The installation location for the archived product.
  - `ARCHIVE_DSYMS_PATH`: The path to the product’s dSYM files. 8423449
- Xcode detects and enforces implicit build dependencies between targets when you build a scheme. You can turn this off per scheme in a scheme’s build action. 7879553
- When the active scheme is a unit-test scheme, clicking Run in the toolbar produces an unknown error dialog.

  To run unit tests, choose Product > Test. 8642393
- Fix-it is not supported in iOS application projects created using the new project dialog. The iOS project templates have the compiler set to LLVM-GCC, which does not support Fix-it.

  After creating an iOS project, set the compiler to LLVM 2.0. 8607314

#### Editing Core Data Models

- You can create `NSManagedObject` subclasses from entities in a Core Data data model. 7484772

#### Refactoring

- The Extract transformation is supported. 7711619

#### Compiling: LLVM 2.0

- __Blocks:__`Goto` statements within blocks are allowed when the target is within the block. 7549164
- __Objective-C:__ Fixes bugs in exception handling present in LLVM 1.5. 8160285
- You can declare instance variables in class implementations and extensions (iOS and 64-bit OS X). 7538989

#### Analyzing OpenGL ES Performance

- The OpenGL ES Performance Detective identifies graphics bottlenecks in your iOS applications. It is located in `<Xcode>/Applications/Graphics Tools`. 8208239
- Runs of the OpenGL ES Analyzer instrument can be saved in Instruments traces. 7993423
- The OpenGL ES Analyzer instrument supports extended filtering of the OpenGL ES trace. 7976717
- The OpenGL ES Analyzer instrument provides single-frame navigation, which allows you to focus all instruments on a specific OpenGL frame, and to step backward and forward in the trace frame by frame. 8552970

### Enhancements

#### General

- You can access the values of the build settings of the target being built through environment variables and launch arguments. When you create custom executables (by changing the value of the Executable setting in Run and Profile scheme actions), you can specify the target against which to expand the environment variables and launch arguments. 7546808

#### Editing Nib Files

- Xcode suggests key path completions in the bindings inspector as you type. To take advantage of this feature, specify the class of object being managed by your controller in the attributes inspector.

  Xcode uses the project’s symbol index to generate the key path completions. 8176168

#### Editing Source Code

- There’s an additional gesture to jump to a symbol definition in the source editor: holding down the Command key. When you hold down Command, Xcode represents the symbol under the pointer as a hyperlink; you can move the pointer between symbols until Xcode highlights the one you want to act on. You can then click the symbol to jump to its definition. Other modifies keys behave as expected. 8459719

#### Task Information and Alerts

- The activity viewer presents more detailed information about scheme-related tasks, such as building a product. 7982481

### Changes

#### Editing Nib Files

- Hidden views are invisible in the Interface Builder canvas (they used to be partially visible in Interface Builder 3, part of Xcode 3).

  To work with these views, select them in the jump bar or the outline view. 8059339

#### Building: xcodebuild

- The `xcodebuild -activetarget` option is no longer supported. 8361726

### Resolved Issues

#### General

- In General preferences, you can specify that Xcode ask you where to open a file you click or double-click while holding down an modifier key in a navigator. 8476034
- Xcode automatically creates schemes for all targets in a project when you open an Xcode 3.x–based project. It doesn’t skip targets that other targets depend on.

  You can delete or hide schemes you don’t need in the manage schemes dialog. 8016676
- Setting General preferences > Build Location > “Shared subfolder” to an absolute path doesn’t generate an assertion failure when opening projects. 8368913

#### Editing Nib Files

- Many performance problems with making connections are resolved. In particular, the performance of connecting to the First Responder has been drastically improved. 8280101
- You can create an Interface Builder–to–source connection even the target source code is folded. 8472539

#### Editing Core Data Model Files

- When you create `NSManagedObject` subclasses from entities in a Core Data data model, Xcode ask for confirmation before overwriting existing files. 8506607

#### Editing Source Code

- Breakpoints and message bubbles appear in the source editor even when code is folded above them. 7192871

#### Compiling: LLVM 2.0

- __C++:__ Several bugs related to using blocks are fixed. 6182276

#### Analyzing OpenGL ES Performance

- API statistics in the OpenGL ES Analyzer instrument are computed correctly. 8549379

#### Help and Documentation Content

- The list of help topics in a help book appears, as expected, when accessing help books in the documentation organizer. 8430699

### New Issues

#### Comparing Versions of a File

- After you create a branch and switch to it in the repositories organizer, using the commit dialog or the version editor causes an assertion failure.

  Restart Xcode after creating a branch and switching to it. 8383245

### Known Issues

#### General

- Interface Builder files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the Interface Builder file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406
- The task log viewer is empty when you select the last build task of a project or workspace in the log navigator and the viewer is set to show only recent operations.

  Set the task log viewer to show all operations. 8350930

#### Editing Nib Files

- Xcode cannot edit OS X–type Interface Builder documents comprised of objects from frameworks other than AppKit.

  You can compile and run these documents, however. 7470836
- __Refactoring:__ Xcode does not refactor Cocoa bindings. 8423815

#### Searching

- __Search navigator:__ Xcode may crash in the replace preview dialog of the search navigator when all the found instances are selected and you click Replace. 8091532

#### Refactoring

- Xcode does not create a snapshot of your workspace before performing a refactoring transformation.

  Create manual snapshots before performing refactoring transformations. 7816256
- __Editing nib files:__ The Rename transformation may not work properly action methods in Interface Builder documents when the action’s target is the first responder or the method is declared in a category, protocol, or a superclass of the given class. 8500272

#### Source Control and Snapshots

- Xcode doesn’t recognize SCP-based URLs for Git repositories in the Repositories organizer.

  Use the SSH-based URLs. For example, instead of `git@example.com:/myrepositoryname.git` use `ssh://git@example.com/myrepositoryname.git`. 8044145

#### Building

- Xcode doesn’t use a new build location after you change General preferences > Build Location.

  Close and reopen open projects and workspaces after changing the build location. 7965261

#### Help and Documentation Content

- These help books are not listed on the Xcode Application Help page (Help > Xcode Application Help): _Interface Builder Help_, _Task and Session Log Viewer Help_, _Symbol Navigator Help_, and _Xcode Concepts_.

  Search for these titles in the Help menu or in the search navigator in the documentation organizer. 8481951,8518802

## Xcode 4.0 Developer Preview 4 Release Notes

### New Features

#### General

- There is no distinction between “launch” schemes and “distribution” schemes. All schemes are capable of launching and archiving a product. 8429398
- The project navigator identifies read-only files with a lock icon. Click the lock to unlock the file. Xcode can unlock files with no “write” permission and files locked from the Finder. You can also invoke a custom script to unlock files through the “Unlocking file” alert in Alerts preferences. 8135771

#### Source Control and Snapshots

- You can preview the files modified in a snapshot before restoring it using the version editor. 7494111
- When using Git as as your source control repository, you can discard changes to project packages (`.xcodeproj` files) through the Source Control item in the project navigator’s shortcut menu. 7480525
- Xcode offers to place new projects under source control in a local Git repository in the project directory. 8407608

#### Accessing Help and Documentation

- You can access Quick Help for a suggested completion from the code completion list. To display Quick Help for the selected suggestion, click the question mark icon on the suggestion or choose Help > Quick Help. 8172782

#### Compiling: LLVM2.0

- __Objective-C:__ Adds support for instance variables in class implementations and class extensions (iOS and 64-bit OS X).
- __Objective-C:__ Adds default automatic synthesis of properties (iOS and 64-bit OS X). You don’t need the `@synthesize` directive in the implementation sections for the compiler to synthesize accessors for declared properties.

  However, to access such properties in `dealloc` and `finalize` methods, you must use the dot notation; for example: `self.property`. 7885001

### Resolved Issues

#### Editing Nib Files

- When inserting an outlet or action with Connect to Source Code, Xcode adds the counterparts for the connection:

  For actions:

  - When dragging to a header file: Xcode adds the implementation and interface.
  - When dragging to an implementation file: Xcode adds the implementation.

  For outlets:

  - When dragging to a header file to insert a property outlet: Xcode adds the instance variable declaration, the `@synthesize` directive, and the `release` call in the `dealloc` method.
  - When dragging to a header file to insert an instance variable outlet, Xcode adds the instance variable declaration, and the `release` call in the `dealloc` method. 8082047

#### Editing Source Code

- Xcode shows a preview of the suggested completion in the code completion list. To accept the entire completion, press Return. To accept only the highlighted part of the completion (identified with a dotted underline), press Tab. 8321987

#### Refactoring

- You can refactor Interface Builder and Core Data model files. 7474053
- After selecting an entire word in the source editor, Xcode was not always able to perform refactoring transformations. 8349889
- You can perform refactoring transformations on key-value coding and Core Data methods. 8224495
- You can rename classes, protocols, and other top-level constructs only when the new name is not in use by another construct of the same type. 8313803
- Xcode notifies you of refactoring errors and warnings in the workspace window. 8128957

#### Compiling

- Catching exceptions in optimized fragile-ABI Objective-C code no longer resets modifications to local variables. 8160285
- Eliminated crash in Objective-C exception rethrow. 8144203
- Fixed bugs in blocks in C++ and Objective-C++ code.

### Known Issues

#### General

- Interface Builder files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the Interface Builder file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406
- Absolute paths in General preferences > Build Location > “Shared subfolder” generate an assertion failure when opening projects.

  Specify a relative path for “Shared subfolder” in General preferences, or set Build Location to the recommended value. 8368913
- The task log viewer is empty when you select the last build task of a project or workspace in the log navigator and the viewer is set to show only recent operations.

  Set the task log viewer to show all operations. 8350930
- The Extract transformation is not supported. 7711619

#### Searching

- __Search navigator:__ Xcode may crash in the replace preview dialog of the search navigator when all the found instances are selected and you click Replace. 8091532

#### Editing Core Data Model Files

- When you create `NSManagedObject` subclasses from entities in a Core Data data model, Xcode overwrites existing files without a confirmation dialog. 8506607

#### Editing Nib Files

- __Refactoring:__ Xcode does not refactor Cocoa bindings. 8423815
- Xcode cannot edit OS X–type Interface Builder documents comprised of objects from frameworks other than AppKit.

  You can compile and run these documents, however. 7470836
- Hidden views are invisible in the Interface Builder canvas.

  To work with these views, select them in the jump bar or the outline view. 8059339

#### Refactoring

- Xcode does not create a snapshot of your workspace before performing a refactoring transformation.

  Create manual snapshots before performing refactoring transformations. 7816256
- __Editing nib files:__ The Rename transformation may not work properly action methods in Interface Builder documents when the action’s target is the first responder or the method is declared in a category, protocol, or a superclass of the given class. 8500272

#### Building

- Xcode doesn’t use a new build location after you change General preferences > Build Location.

  Close and reopen open projects and workspaces after changing the build location. 7965261

#### Source Control and Snapshots

- Xcode doesn’t recognize SCP-based URLs for Git repositories in the Repositories organizer.

  Use the SSH-based URLs. For example, instead of `git@example.com:/myrepositoryname.git` use `ssh://git@example.com/myrepositoryname.git`. 8044145

#### Help and Documentation Content

- These help books are not listed on the Xcode Application Help page (Help > Xcode Application Help): _Interface Builder Help_, _Task and Session Log Viewer Help_, _Symbol Navigator Help_, and _Xcode Concepts_.

  Search for these titles in the Help menu or in the search navigator in the documentation organizer. 8481951,8518802
- The list of help topics in a help book doesn’t appear when accessing help books in the documentation organizer, instead the book’s first help topic appears.

  Use the jump bar to navigate to the other help topics in the book. 8430699

## Xcode 4.0 Developer Preview 3 Release Notes

### About Xcode 4 Developer Preview 3

#### Supported Configurations

Xcode 4 developer preview 3 requires OS X v10.6.4. It does not install or run on earlier versions of OS X.

Xcode supports universal development for iOS 4.1 and 3.2 and OS X v10.5 and later. It does not support development for iOS 3.1 or earlier or OS X v10.4 or earlier.

#### Installation

Xcode 4 developer preview 3 is installed by default into the `/Xcode4` directory and does not conflict with an existing installation of Xcode 3.2.

__Important:__ Several features of Xcode 4, such as the Snapshot mechanism, support for the Git SCM system, and System Trace instrumentation in Instruments, require tools that are installed by the System Tools package. This package is installed by default in Xcode 4 developer preview 3.

The installer optionally installs Unix tools into `/usr`, so conventional makefile-based and config-based builds operate correctly. Use the `xcode-select` command-line utility to set the default toolset for command-line builds. If you choose this option when installing Xcode 4, Xcode 4 Unix tools replace the Xcode 3.2 Unix tools in `/usr`. This does not effect the functionality of any Xcode 3.2 installations.

#### Project File Format Compatibility and Versioning

Xcode 4 reads and builds projects created in Xcode 2.1 through 3.2.3. Projects created and edited with Xcode 4 can be opened and built on Xcode 3.2 through 3.2.3.

__Important:__ Once a project or workspace has been opened with Xcode 4 developer preview 3, do not use that project or workspace with previous Xcode 4 developer previews.

#### Technical Support and Learning Resources

Apple offers a number of resources where you can get Xcode development support:

- [http://developer.apple.com](https://developer.apple.com): The Apple Developer website is the best source for up-to-date technical documentation on iOS and OS X.
- [http://developer.apple.com/technologies/tools/](https://developer.apple.com/technologies/tools/): The Xcode home page on the Apple Developer website provides information on the developer tools.
- [https://forums.developer.apple.com/](https://forums.developer.apple.com/): The Apple Developer Forums feature a dedicated Developer Forum for Xcode 4 Developer Previews.

Use [http://bugreport.apple.com](http://bugreport.apple.com) to communicate issues with Apple. Include detailed information of the issue, including the system and developer tools version information, and any relevant crash logs or console messages.

To send comments or feedback on the Xcode Tools suite to Apple, use [xcode-feedback@group.apple.com](mailto:xcode-feedback@group.apple.com).

### New Features

**__Viewing all Xcode 4 activity__ (7966729)**
: When using Xcode 4, there are times when multiple activities may be active. When this happens, the activity view displays the number of activities in a badge. Clicking on the badge shows the full list of activities currently active.

**__Code completion redesign__ (7764985)**
: The user interface and interaction of code completion has been redesigned to be responsive, predictable, and less intrusive with a refreshed appearance.

**__Using jump bar menus from the keyboard__ (6964063)**
: All the primary menus in the jump bar are accessible via control-# key combinations, where the number increases following UI elements from the left to the right.

| Jump bar item | Key combination |
| --- | --- |
| Related files | Control-1 |
| Previous history | Control-2 |
| Next history | Control-3 |
| First item of path control | Control-4 |
| Files item of path control | Control-5 |
| Symbols item of path control | Control-6 |
| Jump bar Issue navigator, if present | Control-7 |

**__Key combinations for navigation between Assistant editor panes__ (8273438)**
: Xcode 4 developer preview 3 features new commands for moving keyboard focus between top level areas or the user interface:

- To move focus to the next area in the window (clockwise), use command-option-K
- To move focus to the previous area in the window (counter-clockwise), use command-option-shift-K

**__Text manipulation commands available for source editor__ (7854915)**
: Two new text manipulation commands have now been added to the Editor > Structure menu: Move line up/down and Comment/Uncomment lines.

**__Running a process using a custom UI scale__ (8135779)**
: You can now set a scheme to launch its executable using a custom UI scale.

**__Preferences for controlling build products location__ (8281332)**
: Preferences for specifying where build products should be placed by default have been added. A shared subfolder can now be specified to make all projects place their build products in the same directory. These preferences can be overridden for a project or workspace in File > Project Settings/Workspace Settings.

**__Editing IB documents that include objects from frameworks outside of App Kit__ (7493346)**
: With Xcode 4 developer preview 3, you can edit documents that contain objects from frameworks outside of App Kit. Note that editing documents containing Automator objects is not currently supported.

**__Effects attributes of objects in IB editor__ (7470883)**
: Properties modified using the Effects inspector in Interface Builder 3 are now editable in the IB editor in Xcode 4.

**__Preliminary support for the Rename refactoring transformation__ (8372774)**
: The Rename refactoring transformation is now available. It is invoked via the Edit menu or the contextual menu in the source editor.

Support for Refactoring operations in Xcode 4 developer preview 3 is preliminary. These issues are outstanding:

- Transformations other than Rename are not supported. (7711619)
- Errors and warnings generated by the refactoring engine are not visible in the UI. (8128957)
- Refactoring does not yet work with nib and Core Data model files. Changes to these files must be made manually. (7474053)
- Xcode does not yet take a snapshot of your workspace before refactoring source files. These must be created manually, if desired. (7816256)
- Renaming KVC/Core Data methods and related files is not yet available. Such changes must be made manually, if desired. (8224495)
- The refactoring engine does not yet disallow renaming classes, protocols, and other top-level constructs if the requested name is already used by a construct of the same type. (8313803)
- Selecting a file in the jump bar that is not one of the files being changed by refactoring leads to a crash. (8337919)

### Known issues in Xcode 4 Developer Preview 3

Xcode 4 developer preview 3 is pre-release software. File bugs at [http://bugreport.apple.com](http://bugreport.apple.com) for performance and stability issues, data loss or file corruption, missing or unimplemented features, behavioral or aesthetic issues, and feature and enhancement requests. Provide as much context as possible, especially crash logs or samples, detailed Steps to Reproduce, and projects or workspaces when possible.

These problems are already known in this release:

**__Documentation organizer requires updated documentation__ (8354991)**
: After installing Xcode 4 developer preview 3 over a previous Xcode 4 developer preview, the Documentation organizer may not show the documentation you are looking for.

Workaround: In the Documentation preferences, press the Get button next to Xcode 4.0 Developer Tools Library. This downloads the latest version of that documentation set.

**__Connect to source code from IB documents does not insert counterparts__ (8082047)**
: When inserting an outlet or action using connect to source code in IB documents, the counterparts for the connection are not added.

- Actions: When dragging to a header file, the implementation is not inserted.
- Outlets: When dragging to a header to insert a property outlet, the needed instance variable, @synthesize, and release call in dealloc are not added.

**__Warnings when building after editing a IB document__ (8131479)**
: If you edit an IB document and then build a project, false-positive warnings may appear for the IB document.

Workaround: Make sure the project has finished indexing before saving IB documents to avoid these warnings. Re-save any files that have warnings after the project has finished indexing to remove the warnings.

**__Hidden property makes views disappear in IB editor__ (8059339)**
: Views marked as hidden are completely invisible in the Interface Builder editor.

Workaround: To work with these views, selected them in the Jump Bar or document outline view.

**__Syntax coloring and code sense features can fail in some files__ (8360261)**
: Some source files may not get full syntax coloring, code completion, and fix-it hints. Also, Jump to Definition may not work.

Workaround: Save the file to index it.

**__IB documents appear as source__ (8028406)**
: IB documents with explicit Xcode 3 file types open in the Source editor instead of the Interface Builder editor.

Workaround: Set the file type for the selected file in the Type and Identity inspector's File Type field to Default, then close and re-open the document.

**__Last build log restored from previous session appears empty__ (8350930)**
: When you open a workspace or project that has been built before, the information about the last build is shown in the Log navigator. If you load this log, it may appear empty if you have the log viewer's scope bar set to show Recent log entries only.

Workaround: Switch to showing All log content.

**__Shared build location preference requires a path relative to the derived data location__ (8368913)**
: If you choose to have all projects and workspaces build into a common subfolder using the Build Location setting in General preferences, you must specify a relative subpath within the derived data folder. Specifying an absolute path is not a valid choice, but the UI does not signal this as an error. Instead, when you open projects, Xcode shows an assertion failure.

Workaround: specify a relative path for the build location or to change back to the default settings.

**__Editing IB documents with objects from plugins__ (7470836)**
: Xcode 4 supports iOS-type IB documents and OS X-type IB documents composed of App Kit objects. OS X-type documents composed of objects from other frameworks, such as Address Book, Automator, and 3rd party IB plugins, are not supported in the IB editor. Although these documents cannot be edited with the IB editor, they can be compiled, built, and run.

**__SCP-style URLs for Git repositories are not supported__ (8044145)**
: The Repositories organizer does not support SCP-style URLs when configuring Git repositories. Use the ssh:// style of URL to refer to a repository you wish to clone.

For example, the URL `git@example.com:/myrepositoryname.git` should be provided as `ssh://git@example.com/myrepositoryname.git`.

**__Crash when replacing all search results.__ (8091532)**
: In the Search Navigator's Preview sheet, replacing results when all search results are selected can cause Xcode to crash.

**__Changes to the build products location do not take effect while a project is open.__ (7965261)**
: After changing the location where build products are placed, any open projects or workspaces must be closed and re-opened before the change takes effect.

### Issues Resolved in Xcode 4 Developer Preview 3

These issues where present in Xcode 4 developer preview 2 or earlier and have been resolved in Xcode 4 developer preview 3.

**__iOS applications run with Instruments launch in iPad Simulator__ (8203761)**
: Running an iOS 4 application with Instruments in the iOS simulator now results in the Simulator launching in iPhone device mode.

**__Out-of-sync selections in data model files__ (8289611)**
: Adding entities and attributes to data model files no longer leads to selection becoming out-of-sync until the document was reloaded.

**__Data models edited in previous Xcode 4 developer preview__ (8320417)**
: Data models edited with previous Xcode 4 developer previews need to revert changes due to possible data corruption.

**__Console output from iOS Simulator applications__ (8201210)**
: Console output to standard out from iOS applications running in the iOS simulator appear as expected.

**__Deleting top level objects in IB documents__ (8114740)**
: Top level objects in IB documents can now be directly deleted from the canvas and dock.

**__Changing object attributes doesn't properly resize objects to fit__ (7600085)**
: An object changes size automatically when modifying an attribute that requires the change. Using Editor > Size to Fit to workaround is no longer needed.

**__Connect to source code for IB documents now supports outlet collections__ (8045078)**
: When making connections to source code in IB documents, connecting to outlet collections is now supported.

**__Support for editing accessibility values for iOS objects__ (7986412)**
: The IB editor now supports editing accessibility values for iOS objects.

**__Navigator filter results don't update as the items to filter changed__ (7722840)**
: Filtering in navigators now produces live results. For example, when filtering the contents of the Project navigator by SCM status, the list of items updates as the SCM status of individual files changes.

**__Workspace window and tab state lost if Xcode is force quit or quits unexpectedly.__ (7773437)**
: The layout of a workspace window including the open tabs, navigator and inspector positioning and visibility, selected navigator rows, current document, and editor mode are normally all saved when Xcode 4 quits or the workspace is closed. In Xcode 4 developer preview 3, state is also be saved periodically while you work and navigate between files.

**__Projects claim to use multiple SDKs__ (8128405)**
: The project navigator no longer claims projects with multiple targets use multiple SDKs when all targets use the same SDK.

**__Issues opening projects with cyclic references__ (8226072)**
: An issue with opening projects with cyclic references (A->B, B->A) has been resolved.

**__Persistence of IB editor's object dock mode__ (8232638)**
: The IB editor's dock now persists its mode when switching between documents.

**__Textual filter settings in navigators stuck__ (8183815)**
: The text for navigator filtering stays cleared.

**__Version editor jump bar out of sync with file shown__ (8198690)**
: At times the jump bar in the Version editor was out of sync with the document shown.

**__The source editor shows a full contextual menu__ (7473795)**
: Some items that had been missing from the source editor contextual menu have now been added.

**__Syntax coloring of shell scripts and xcconfig files__ (7600899)**
: Shell scripts and `xcconfig` files support syntax coloring in Xcode's source code editor.

### Issues Resolved in Xcode 4 Developer Preview 2

These issues where present in Xcode 4 developer preview and have been resolved in Xcode 4 developer preview 2.

**__Snapshots available as alert action__ (7945417)**
: Snapshot creation is available as an alert action in Alerts preferences.

**__Default build directory for all projects and workspaces__ (8073463)**
: General preferences includes settings for the default locations to use for derived data (such as build results, logs and indices), snapshots, and archives. Settings made in the Project or Workspace Settings of individual projects or workspaces override the app-level setting.

**__Broken file references__ (8085921)**
: A number of issues were resolved that allow Xcode 4 to resolve references that were previously broken.

**__Issues identifying appropriate run destinations for targets__ (8165363)**
: Issues that caused some iOS targets to appear as Mac targets with "Intel 32-bit" as its run destination and some multi-architecture Mac OS targets to only be offered as "Intel 32-bit" have been resolved.

**__Indexing issues on case sensitive file systems__ (7950730)**
: A situation where IB documents blocked indexing in case sensitive file systems has been resolved.

**__IB editor crash with table view image cells__ (8118050)**
: A crash within the IB editor when loading an IB document with a table view containing a image cell column has been resolved.

**__Filtering objects in IB document outline view__ (7880130)**
: The filter field in the IB editor's document outline view filters objects in the Objects outline view based upon their label.

**__Speed improvements when dragging objects in IB documents__ (8088222)**
: Dragging objects in Interface Builder documents is improved and does not pause.

**__Options when connecting to source code from IB documents__ (8095283)**
: When connecting to source code to insert an outlet or action, the configuration panel includes options for outlets and actions, such as retain/assign for property outlets.

**__IB editor requires IBAction return type__**
: Previous releases of Interface Builder accepted many method signatures as valid actions. The IB editor in Xcode 4 strictly identifies IBActions and only accepts methods with return types explicitly tagged as `- (IBAction)`.

**__Manually defined actions and outlets need to be defined in source__**
: Actions and outlets defined manually in previous releases of Interface Builder's inspectors and library but not redefined in source code are not recognized by Xcode 4.

### Functionality No Longer Supported in Xcode

The following features and functionality have been removed from Xcode. When substitute functionality is available, it is noted.

- Layout modes
- Class Browser. Use the Symbol Navigator and Class Navigation menu in the Editor.
- Active Target/Configuration/Architecture/SDK/Executable toolbar items and Project menu entries. Configure a Launch Scheme for a particular combination of target/configuration/architecture/SDK/executable that is useful to you using the Scheme toolbar popup.
- Bookmarks
- Favorites bar
- Detail views
- Class model
- Touch an individual file
- Recent Files menu item in the File menu. The Navigation buttons have a list of recent files. Also, use the filter in the Project Navigator to show all recently-viewed files in the project or workspace.
- Support for External Editors
- Worksheet (Control-R) execution of shell script commands in text documents
- Predictive Compilation (generally replaced by Fix-It Hints)
- Fix and Continue
- Breakpoint navigation menu in Navigator bar
- Editing and compiling AppleScript .scpt files
- Perforce and CVS source code management
- Dock Icon Menu of open Xcode windows (in Snow Leopard, press and hold on the Dock tile to see all Xcode windows)
- Editing Carbon nib files. Xcode 4 supports building Carbon xib and nib files; use Interface Builder 3.2 to edit them.

## Xcode 4.0 Developer Preview 2 Release Notes

### About Xcode 4 Developer Preview 2

#### Supported Configurations

Xcode 4 Developer Preview 2 requires OS X v10.6.4. It does not install or run on earlier versions of OS X.

Xcode supports universal development for iOS 4 and 3.2 and OS X v10.5 and later. It does not support development for iOS 3.1 or earlier or OS X v10.4 or earlier.

#### Installation

Xcode 4 Developer Preview 2 is installed by default into the `/Xcode4` directory and does not conflict with an existing installation of Xcode 3.2.

__Important:__ Several features of Xcode 4, such as the Snapshot mechanism, support for the Git SCM system, and System Trace instrumentation in Instruments, require tools that are installed by the System Tools package. You must check the __System Tools__ check box when installing Xcode 4 in order to use the these features. It is recommended that you restart your Mac after installing System Tools.

The installer optionally installs Unix tools into `/usr`, so conventional makefile-based and config-based builds operate correctly. Use the `xcode-select` command-line utility to set the default toolset for command-line builds. If you choose this option when installing Xcode 4, Xcode 4 Unix tools replace the Xcode 3.2 Unix tools in `/usr`. This does not effect the functionality of any Xcode 3.2 installations.

#### Project File Format Compatibility and Versioning

Xcode 4 reads and builds projects created in Xcode 2.1 through 3.2.3. Projects created with Xcode 4 can be opened and built on Xcode 3.2 through 3.2.3.

Opening and building a project in Xcode 4 does not upgrade or alter it. Changes you make to a project in Xcode 4 are compatible with earlier versions of Xcode.

#### Technical Support and Learning Resources

Apple offers a number of resources where you can get Xcode development support:

- [http://developer.apple.com](https://developer.apple.com): The Apple Developer website is the best source for up-to-date technical documentation on iOS and OS X.
- [http://developer.apple.com/technologies/tools/](https://developer.apple.com/technologies/tools/): The Xcode home page on the Apple Developer website provides information on the developer tools.
- [https://forums.developer.apple.com/](https://forums.developer.apple.com/): The Apple Developer Forums feature a dedicated Developer Forum for Xcode 4 Developer Previews.

Use [http://bugreport.apple.com](http://bugreport.apple.com) to communicate issues with Apple. Include detailed information of the issue, including the system and developer tools version information, and any relevant crash logs or console messages.

To send comments or feedback on the Xcode Tools suite to Apple, use [xcode-feedback@group.apple.com](mailto:xcode-feedback@group.apple.com).

### Known issues in Xcode 4 Developer Preview 2

Xcode 4 Developer Preview is pre-release software. File bugs at [http://bugreport.apple.com](http://bugreport.apple.com) for performance and stability issues, data loss or file corruption, missing or unimplemented features, behavioral or aesthetic issues, and feature and enhancement requests. Provide as much context as possible, especially crash logs or samples, detailed Steps to Reproduce, and projects or workspaces when possible.

These problems are already known in this release:

**__Installer packages visible on Xcode 4 Developer Preview 2 disk image__ (8209023)**
: When mounting the Xcode 4 Developer Preview 2 disk image, a `Packages` folder is visible. Installing packages from within this folder is not supported. Use the `Xcode and iOS SDK` package to install Xcode 4 Developer Preview 2.

**__iOS applications run with Instruments launch in iPad Simulator__ (8203761)**
: Running an iOS 4 application with Instruments in the iOS simulator results in the Simulator launching in iPad device mode instead of iPhone device mode.

**__Console output from iOS Simulator applications__ (8201210)**
: Console output to standard out from iOS applications running in the iOS simulator does not appear until each call is new-line terminated or the application is quit.

**__SCP-style URLs for Git repositories are not supported__ (8044145)**
: The Repositories organizer does not support SCP-style URLs when configuring Git repositories. Use the ssh:// style of URL to refer to a repository you wish to clone.

For example, the URL `git@mycompanyname.beanstalkapp.com:/myrepositoryname.git` should be provided as `ssh://git@mycompanyname.beanstalkapp.com/myrepositoryname.git`.

**__Version editor Jump Bar out of sync with file shown__ (8198690)**
: At times the Jump Bar in the Version editor is out of sync with the document shown.

Workaround: Navigate away from and back to the file in the Version editor to refresh the data.

**__Documentation organizer requires updated documentation__ (8205933)**
: Documentation viewed in the organizer may be missing its table of contents or its contents are not navigable via the Jump Bar.

Workaround: Download the latest documentation, go to the Documentation preferences and click Check and Install Now.

**__Crash when making connections using connections HUD__ (8197402)**
: Control-clicking an element and attempting to drag a connection crashes Xcode then next time any file is saved.

Workaround: Use the connections inspector or connect-to-code with the Assistant editor to make connections.

**__Effects attributes of objects in IB editor__ (7470883)**
: Properties modified using the Effects inspector in Interface Builder 3 are not editable in Xcode 4.

**__Attributes on objects in IB documents require size-to-fit__ (7600085)**
: Some changes to attributes of objects in IB files require that the object is properly sized-to-fit after making the change, but these objects do not automatically size-to-fit.

Workaround: Select the control in the design canvas and choose Editor > Size to Fit.

**__Outlet collections for connect to source code from IB documents__ (8045078)**
: When making connections to source code in Interface Builder documents, connecting to outlet collections is not supported.

**__Connect to source code from IB documents does not insert counterparts__ (8082047)**
: When inserting an outlet or action using connect to source code in IB documents, the counterparts for the connection are not added.

- Actions: When dragging to a header file, the implementation is not inserted.
- Outlets: When dragging to a header to insert a property outlet, the needed instance variable, `@synthesize`, and release call in dealloc are not added.

**__Hidden property makes views disappear in IB editor__ (8059339)**
: Views marked as hidden are completely invisible in the Interface Builder editor.

Workaround: To work with these views, selected them in the Jump Bar or document outline view.

**__IB documents appear as source__ (8028406)**
: IB documents with explicit Xcode 3 file types open in the Source editor instead of the Interface Builder editor.

Workaround: Reset the file type for the selected file in the "Type and Identity" file inspector's "File Type" pop up button to "Default," then close and re-open the document.

**__Editing IB documents with objects from plugins__ (7470836)**
: Xcode 4 supports iOS-type IB documents and OS X-type IB documents composed of App Kit objects. OS X-type documents composed of objects from other frameworks, such as Address Book, Automator, and 3rd party IB plugins, are not supported in the IB editor. Although these documents cannot be edited with the IB editor, they can be compiled, built, and run.

**__Warnings when building after editing a IB document__ (8131479)**
: If you edit an IB document and then build a project, warnings may appear for the IB document. Most likely, these warnings are false-positives.

Workaround: Make sure the project has finished indexing before saving IB documents to avoid these warnings. Re-save any files that have warnings after the project has finished indexing to remove the warnings.

### Issues Resolved in Xcode 4 Developer Preview 2

These issues where present in Xcode 4 Developer Preview and have been resolved in Xcode 4 Developer Preview 2.

**__Snapshots available as alert action__ (7945417)**
: Snapshot creation is available as an alert action in Alerts preferences.

**__Default build directory for all projects and workspaces__ (8073463)**
: General preferences includes settings for the default locations to use for derived data (such as build results, logs and indices), snapshots, and archives. Settings made in the Project or Workspace Settings of individual projects or workspaces override the app-level setting.

**__Broken file references__ (8085921)**
: A number of issues were resolved that allow Xcode 4 to resolve references that were previously broken.

**__Issues identifying appropriate run destinations for targets__ (8165363)**
: Issues that caused some iOS targets to appear as Mac targets with "Intel 32-bit" as its run destination and some multi-architecture Mac OS targets to only be offered as "Intel 32-bit" have been resolved.

**__Indexing issues on case sensitive file systems__ (7950730)**
: A situation where IB documents blocked indexing in case sensitive file systems has been resolved.

**__IB editor crash with table view image cells__ (8118050)**
: A crash within the IB editor when loading an IB document with a table view containing a image cell column has been resolved.

**__Filtering objects in IB document outline view__ (7880130)**
: The filter field in the IB editor's document outline view filters objects in the Objects outline view based upon their label.

**__Speed improvements when dragging objects in IB documents__ (8088222)**
: Dragging objects in Interface Builder documents is improved and does not pause.

**__Options when connecting to source code from IB documents__ (8095283)**
: When connecting to source code to insert an outlet or action, the configuration panel includes options for outlets and actions, such as retain/assign for property outlets.

**__IB editor requires IBAction return type__**
: Previous releases of Interface Builder accepted many method signatures as valid actions. The IB editor in Xcode 4 strictly identifies IBActions and only accepts methods with return types explicitly tagged as `- (IBAction)`.

**__Manually defined actions and outlets need to be defined in source__**
: Actions and outlets defined manually in previous releases of Interface Builder's inspectors and library but not redefined in source code are not recognized by Xcode 4.

### Functionality No Longer Supported in Xcode

The following features and functionality have been removed from Xcode. When substitute functionality is available, it is noted.

- Layout modes
- Class Browser. Use the Symbol Navigator and Class Navigation menu in the Editor.
- Active Target/Configuration/Architecture/SDK/Executable toolbar items and Project menu entries. Configure a Launch Scheme for a particular combination of target/configuration/architecture/SDK/executable that is useful to you using the Scheme toolbar popup.
- Bookmarks
- Favorites bar
- Detail views
- Class model
- Touch an individual file
- Recent Files menu item in the File menu. The Navigation buttons have a list of recent files. Also, use the filter in the Project Navigator to show all recently-viewed files in the project or workspace.
- Support for External Editors
- Worksheet (Control-R) execution of shell script commands in text documents
- Predictive Compilation (generally replaced by Fix-It Hints)
- Fix and Continue
- Breakpoint navigation menu in Navigator bar
- Editing and compiling AppleScript .scpt files
- Perforce and CVS source code management
- Dock Icon Menu of open Xcode windows (in Snow Leopard, press and hold on the Dock tile to see all Xcode windows)
- Editing Carbon nib files. Xcode 4 supports building Carbon xib and nib files; use Interface Builder 3.2 to edit them.

## Xcode 4.0 Developer Preview 1 Release Notes

Xcode 4 is a major version of the Xcode toolset. It requires OS X v10.6.3 and does not run on previous versions of OS X.

__Important:__ These Release Notes cover important information for transitioning from Xcode 3.2 to Xcode 4. To learn more about changes in the development workflow, read Xcode 4 User Guide.

The following Release Notes pertain to the WWDC 2010 Developer Preview of Xcode 4 only.

### General

- _Supported Configurations_

  Xcode 4 runs on OS X v10.6.3. It does not install or run on earlier versions of OS X. Xcode supports universal development for iPhone OS 4 and 3.2 and OS X v10.4 and later. It does not support development for OS X v10.3 or earlier or iPhone OS 3.1 or earlier.
- _Xcode Installation_

  Xcode 4 Developer Preview is installed by default into the `/Xcode4` directory and does not conflict with an existing installation of Xcode 3.2.

  __Important:__ Several features of Xcode 4, such as the Snapshot mechanism, support for the git SCM system, and System Trace instrumentation in Instruments require tools that are installed by the System Tools package. You must check the __System Tools__ check box when installing Xcode 4 in order to use the these features. It is recommended that you restart your Mac after installing System Tools.

  The installer optionally installs Unix tools into `/usr`, so conventional makefile-based and config-based builds operate correctly. Use the `xcode-select` command-line utility to set the default toolset for command-line builds. If you choose this option when installing Xcode 4, Xcode 4 Unix tools replace the Xcode 3.2 Unix tools in `/usr`. This does not effect the functionality of any Xcode 3.2 installations.
- _Project File Format Compatibility and Versioning_

  Xcode 4 reads and builds projects created in Xcode 2.1 through 3.2.3. Projects created with Xcode 4 can be opened and built on Xcode 3.2 through 3.2.3.

  Opening and building a project in Xcode 4 does not upgrade or alter it. Changes you make to a project in Xcode 4 are compatible with earlier versions of Xcode.

  User-specific project information for Xcode 4 is stored in new files in the `.xcodeproj` project wrapper. Xcode 4 ignores and rarely alters the information in Xcode 3.2’s per-user `.pbxuser` files.
- _User Preferences from Xcode 3.2_

  For the most part, Xcode 4 neither migrates nor interferes with your user settings from Xcode 3.2, with some exceptions.

  General, Code Sense, Building, Distributed Builds, Debugging, Key Bindings, File Types, Source Trees, and Documentation preferences from Xcode 3.3 are ignored; similar Xcode 4 functionality starts with Xcode 4 defaults. Changing settings in Xcode 4 does not affect your continued use of Xcode 3.2.

  Text Editing, Fonts and Colors, Indentation, and SCM preferences are copied from Xcode 3.2 preferences. Changes made to these preferences with Xcode 4 are not copied back to Xcode 3.2.

### Major Changes in Xcode 4

- _Workflow_

  The Default, Compact, and All-in-One layouts have been replaced by a single Xcode window layout that accommodates everything from a single source file to a multiple interrelated project workspace. Source files, Xcode projects, Interface Builder xibs & nibs, data models, and other files are viewed and edited in the Editor area of the window.

  The left side of the Xcode 4 window shows one of several navigators. The project aviator contains a list of files or projects, and functions like the Groups and Files tree of an Xcode 3.2 project. Other navigators show lists of project symbols; current issues, such as build errors and warnings; results of cross-file Find operations; logs from operations such as building, debugging, or SCM transactions; current breakpoints set in code; or the debug information for the current process. You select an item from the navigator to show its contents for viewing or editing in the Editor.

  Most navigators have a Filter area at the bottom of the navigator that lets you narrow down the contents it displays. This resembles the function of the Filter field in Xcode 3.2’s Detail view. In the project navigator, additional scope buttons allow you to show only recently–accessed files, only currently–modified files, or only files that have interesting SCM status.

  A Utility area on the right shows information about items selected in the navigator or current editor. The top portion of the Utility area features inspectors for the selected item in the navigator or editor. There may be several separate inspectors. The leftmost one usually shows the information about the selected file, while others may show information about the selection within that file. At the bottom of the Utility area is a Library with parts that can be added to a project or file, including file templates, text macros, Interface Builder objects, and media files.

  The navigator and utility areas are opened with the editor in the middle or closed to allow the editor to occupy the entire window.

  The Xcode window supports _window tabs_, which span the navigator, editor, and Utility areas. Create new tabs for editing different files, or have separate tabs for file navigation, searching, and debugging if you choose.

  You can show multiple editors at the same time, stacked vertically or horizontally. The Assistant editor automatically associates the contents of two editors; for example, the Assistant editor can always show the header file when editing a source file or the source files when browsing through a build log.

  The same project or workspace can be open in multiple windows simultaneously.
- _Workspaces_

  The main Xcode window contains a workspace. A workspace can be as simple as a single text file or as complex as several dozen interrelated projects. If you open a single project in Xcode 4, it opens as its own workspace. You can create a dedicated workspace that contains multiple files and projects and store its workspace configuration in a separate `.xcworkspace` file.

  Each workspace manages editing, navigation, building and launching, indexing, snapshots, and SCM for the files and projects in it. In most cases these Xcode 4 workspace functions supersede the behavior of the same project in Xcode 3.2. In some cases, the settings of the Xcode 3.2 project are copied into the Xcode 4 workspace. Changes you make to those settings are isolated to that workspace and do not interfere when the same project is opened in another workspace or in Xcode 3.2.
- _Project Management and Editing_

  Projects are displayed and edited in the project navigator. The project navigator contains any number or projects, files, or folder references. Add new projects to a workspace with the + button in the Filter area at the bottom of the navigator.

  Within a project, files, groups, and folder references behave just as in Xcode 3.2. Add files to a project with File > New > New File..., with the + button in the Filter area, or by dragging them into the project navigator from the Finder or the Library.

  Project Settings that are found in the Project Inspector in Xcode 3.2 are now located in the Project editor in Xcode 4. The Info tab sets project-wide information (add or delete configurations and localizations, set Deployment Target defaults for all targets) and the Build Settings tab lets you set Project-level Build Settings.

  Targets are not displayed in the project navigator, but instead are available in the project editor. Add or delete targets here, as well as edit target contents. The tabs in the Target Editor are similar to the tabs in the Target Inspector in Xcode 3.2. The Info tab lets you see and change the contents of the target’s Info.plist file visually; the Build tab edits the target’s Build Settings; and the Build Rules tab edits the Build Rules for the target. Add, rearrange, and delete Build Phases, and add or remove target members from Build Phases with drag and drop. Target Dependencies are set in the Build Dependencies build phase. Per-file Compile Flags are set in a column in the Compile Sources build phase. Header Role (project, public, private) is set by dragging header files into subdivisions of the Copy Headers build phase.

  Structural commands on the Project—adding targets, configurations, build phases, localizations—are now located in the Editor menu instead of the Project menu as in Xcode 3.2.

  The Build Settings tabs for both the Project and Target editors are significantly improved from Xcode 3.2. The Build Settings grid now essentially treats Configuration as a build setting condition, so you see values in all configurations simultaneously. The Levels mode also shows Default, Project, and Target settings in columns, so you see exactly where a build setting value comes from. Select multiple targets and see the settings in those targets side-by-side.

  The Build Settings grid has a Basic scope, which shows only the most commonly used settings for a project or target (along with all settings defined at that level). The All scope shows all settings. The filter field filters the build setting list. Build setting names and values are returned as Find Results in the search navigator.

  Changes made in the project editor are stored in the project, not in the workspace. They take effect in any workspace that has that project as a member and also take effect if the project is reopened in Xcode 3.2.
- _Navigation_

  The Jump Bar across the top of the Editor shows the logical path to the item in the editor. Each part of the path is a pull-down menu to navigate to any other item at that level; the rightmost part allows navigation within the Editor. For source files, for example, this replaces the function pop-up in Xcode 3.2.

  The Navigation popup menu button at the left of the Navigation Arrows allows direct navigation to other files. Its submenus list Recent Files, Unsaved Files, Counterparts, class relationships including Superclass, Siblings, Subclasses, and Categories, and Includes and Included By. These take the place of the buttons in the editor Navigation Bar in Xcode 3.2.

  A split-button control in the toolbar switches among Standard Editor, Assistant Editor, and Version Editor in the Editor area. The Standard Editor shows one editor. The Assistant Editor shows an editor split between two different files; change whether this is horizontal or vertically split with View >Editor > Change Split Orientation (command-shift-0).

  Holding down the option key when navigating to a different file using the Standard Editor’s Jump Bar opens both the current and the selected file in the Assistant Editor.

  The second view in the Assistant Editor tracks the file or selection in the main view. For source files, the second view shows the main counterpart (header or source file) for the file in the main view. For the Log Editor, the second view shows the source file location corresponding to the selected error or warning. For Interface Builder files, the second view shows the header file for the objects selected in the main view.

  The first item in the Jump Bar for an Assistant Editor shows a list of Assistant Categories that lets you control how it tracks the main editor. Choosing Manual allows you to disengage the split editor to show any file, even a different part of the same file.

  The Open Quickly command allows you to open any known file by name, or to the file that defines the given symbol. If a filename is selected, Open Quickly enters that filename so that pressing Enter jumps directly there. Typing the initial letters (or just the capital letters in) a file name or symbol lists all matches; use the arrow keys or mouse to select a file to open.

  Within a file, the Navigate menu in the main menu bar provides navigation commands specific to the editor’s document type.
- _Editors_

  Xcode 4 includes editors for project files, source code, Interface Builder files, Property List files, Data Model files, Scripting Definitions, and Rich Text files. PDF files are viewable but not editable. HTML and XML files can be edited as text; there is no HTML viewer. All other documents are displayed as previews as in the Finder. In addition, a context menu on every file reference allows it to be opened using a Hex Editor to view and edit the raw file contents.

  Editors for different document types each have custom commands in the Navigate and Editor menus to act on the information in that document type. The terminal item of the Jump Bar allows you to navigate within the document.
- _Editing Source Code_

  The Source Code Editor supports the major editor functionality of the Xcode 3.2 editor: automatic indenting and formatting, Code Sense code completion with text macro support, code folding, and Code Focus block highlighting. Navigation features in the Source Editor are generally unchanged from Xcode 3.2: command-double click jumps to the symbol’s definition, option-double click shows the Quick Help for a function, etc.

  When your target is set to use the LLVM compiler, the source code editor scans your source text as you type. Syntax errors are marked with a wavy red underscore or a caret at the position of the error, and a symbol in the gutter. Clicking the symbol advises you on the potential syntax error and in many cases offer to repair it automatically.

  Similarly, Edit All in Scope uses information from the LLVM compiler to correctly determine the scope of identifiers to mass-replace.
- _Editing Interface Files_

  Interface Builder xib and nib files are edited directly in the Xcode editor—the Interface Builder application has been completely integrated into Xcode. When you select an Interface Builder file, the file’s objects appear in a sidebar in the editor, and the objects themselves appear on a canvas when selected. The Interface Builder inspectors and Library are available in the Utility area to the right of the canvas. Instantiate new objects in your IB file by dragging them directly from the Library in the Utility Area onto the canvas.

  Interface Builder files are automatically associated with the project that contains them, so there is no need to synchronize these files and projects between Xcode and IB. Connections are made in the usual way, by using the connections inspector or by control-dragging from one object to another.

  When editing an Interface Builder file with the Assistant Editor, selecting an object opens the object’s corresponding class header in the second pane. Drag connections directly from the object to declarations in the header file.

  Xib/nib-wide properties are edited in the File Inspector for the nib.
- _Editing Data Models_

  Data model files are edited directly in the Xcode editor. The sidebar shows the list of elements in the model. Using buttons at the bottom of the main editor, choose to display the model in graphic form (as in Xcode 3.2) or in a table view that you sort, search, and filter.

  Attributes of selected data model objects are edited using the Model tab of the Inspector in the Utility Area to the right of the Editor.
- _Editing Property Lists_

  Property list files are edited directly in the Xcode editor, just as in Xcode 3.2. For known property list types, the Key panel shows a descriptive name of the key instead of the key’s literal text; toggle this view using the Show Raw Keys/Values item in the Editor menu. The raw key value is also available in the QuickHelp inspector.
- _Building_

  The separate Build and Run menus in Xcode 3.2 have been consolidated into a single Product menu. There are separate commands for Build, Analyze, and Test. The Run command builds if necessary, then executes; Run without Building runs the last built product even if there are unbuilt changes.

  The Active Target, Configuration, SDK, Architecture, and Executable concepts have been consolidated and their individual menu and toolbar items removed. Xcode 4 manages building and launching with _schemes_. When you open a project, Xcode automatically creates schemes based on the targets, build configurations, and executables in your project. Schemes are used by Xcode 4 and are ignored by Xcode 3.2.

  A _launch scheme_ contains instructions for building one or more targets and its dependencies, then either running tests against the build products or launching an executable. This allows you to encapsulate the logic of your development cycle in a single package and invoke it simply by clicking Run, rather than having to set several different switches in the Overview menu every time you shift development modes.

  All schemes are listed in the Schemes popup in the toolbar (in place of the Overview popup in Xcode 3.2). To build and run, you choose a scheme (and, optionally, a destination that specifies a particular device or architecture supported by that scheme), choose to Enable or Disable Breakpoints, and then click Run. Xcode builds the targets of the scheme in the Build Configuration designated by that scheme, optionally runs Unit Tests on the results, then launches a designated executable with or without breakpoints enabled in order to execute the build product. To build for a different SDK or device, to launch with a different set of environment variables or command-line arguments, or to build a different configuration or different set of targets requires only picking a different scheme from the same menu.

  The Edit Active Scheme item in the Schemes popup allows you to set the attributes of the Build Action of the scheme (configuration and target list), the Test Action (which targets to build and execute for unit testing), and the Launch Action (what debugger to run, under which performance tool, with what runtime settings). The Manage Schemes menu item allows you to create new schemes, remove unused ones, and reorder schemes in the menu. If a scheme is not relevant to your workflow, delete it or uncheck it and it is longer shown in the menu.

  All schemes are stored on a per-user basis in the project or workspace unless the Shared box is checked. Shared schemes are made available to all users of that project or workspace. Use the Container popup to determine which project or workspace the scheme is saved in.

  Once Xcode has determined the targets and dependencies, the build configuration, the architecture and SDK from the choice of Launch Scheme and Destination, building proceeds normally. Xcode builds the designated targets in dependency order, using the build settings determined by the build configuration, for the architectures supported by the destination. It processes the build phases of each target to copy resources, compile sources, link binaries with frameworks, and run shell scripts as needed.

  The progress of the build is shown in the Activity View in the Xcode 4 toolbar and build steps are recorded in a Build Log in the log navigator. Xcode 4 keeps a progressive record of build logs so you can see the results of previous builds. Selecting a build log in the log navigator opens the log in the Standard Editor, where you expand, search, or filter its results using the scope bar and filter buttons. Selecting a build step or issue in the log and switching to the assistant editor shows the corresponding build file in the assistant pane.

  If you care only about build issues and not about the build steps, show the issue navigator. It shows a concise phrasing of each issue, and selecting it navigates the primary editor to the location of the issue. The Filter field is used to show only specific types of issues. Use the jump bar the top right of the editor pane to navigate among current issues.
- _Build Locations_

  Xcode 4 does not have application-level settings for build directories (that contain intermediate files and build products). Instead, each project or workspace has a Build Location that sets a common directory for all the projects it contains. By default the build location is a unique directory in `~/Library/Developer/Xcode/DerivedData/` and each project in the workspace has a separate folder in that directory. This means that when you build projects with the same name in two different workspaces (for example, a branch and trunk of the same project), its precompiled headers, indexes, and build products do not conflict with one another.

  Set the Build Locations in the sheet invoked by Project Settings or Workspace Settings in the File menu. The paths set in the Settings sheet control the default values for `$(OBJROOT)` and `$(SYMROOT)` (Build Products Path and Intermediate Build Files Path, respectively) when building projects. Any build settings derived from these are affected by the workspace-wide Build Location.

  The common Precompiled Headers Cache Path `$(CACHE_ROOT)` is now within the project or workspace Build Locations. When using LLVM compiler 2.0, the size of precompiled headers is significantly smaller, and the size and speed advantages of sharing them are less significant.
- _Build Tools_

  Xcode 4 contains an updated version of the LLVM compiler (LLVM compiler 2.0) which directly supports compilation of C++ and Objective-C++ code without falling back to llvm-gcc. New projects created in Xcode 4 are configured to use LLVM compiler 2.0.

  In this Developer Preview, C++ support in the LLVM compiler 2.0 is not available for iPhone OS.

  llvm-gcc4.2 is now the default system compiler in Xcode 4. Existing projects that don’t have an explicit Compiler Version set and thus build with gcc4.2 on Xcode 3.2 build with llvm-gcc4.2 on Xcode 4.

  GCC 4.0 has been removed from Xcode 4. If your project has an explicit Compiler Version of gcc 4.0, you need to change it in order to build with Xcode 4.
- _Running and Debugging_

  The active Scheme controls what happens when you choose Run from the Products menu or click the Run button. With a Launch scheme, the Build and Launch actions of the scheme are performed; for a Distribution scheme, the Build and Archive actions are performed. Choose to Build (without Running), Run (without Building), or Build and Test with the menu items in the Product menu.

  As in Xcode 3.2, Xcode always launches executable code by attaching a debugger to it. When you choose to launch with breakpoints deactivated, this adds negligible launch time and no measurable performance impact until the program is interrupted or traps into the debugger. Deactivate breakpoints with the Product menu item, with the button in the toolbar, or as a default in the Scheme Editor.

  In Xcode 4, the `gdb` debugger and the new `lldb` debugger are available.

  Additional tabs in the Launch step of the Launch Action allow you to designate launch arguments and environment variables to be used when launching, as well as a set of diagnostic controls for memory management and logging. For example, create a launch action that always runs your executable under Malloc Debug by checking the appropriate check box.

  Launching a process reveals the Debugger Area under the Editor. Show or hide this at any time from the View menu. The Debugger Area has a Variables view and a Console view.

  The Variables view has a Filter bar with a popup to choose to show all symbols, only symbols in the local scope, or an Auto mode that shows values relevant at the current program location. A filter field allows you to narrow down to specific symbols of interest.

  Values are shown in outline form with the identifier, type, raw value, and formatted value in a single line, rather than a multicolumn display. During execution, updated values are displayed in blue. A contextual menu on each value allows you to control its display, print its value to the Console, or open the backing memory for it in a hex editor.

  The Console shows interaction with the debugger or the program’s Standard Input and/or Standard Output. Transcripts of debug sessions are stored in the log navigator and is shown in the main editor area. Xcode 4 keeps a record of debug logs so you can see the proceedings of previous debug sessions.

  The Debugger Bar at the top of the panel has the step controls for program execution, as well as a path control showing the context of the current program counter by thread and stack frame. Stack frames are identified with distinctive icons to identify user, system, framework, and kernel code.

  The Breakpoints navigator shows all breakpoints set in all projects in the workspace. Breakpoints are imported from project user files in Xcode projects added to the workspace, but are stored in workspace user files in Xcode 4. Changes you make to breakpoints in Xcode 4 are not available to other users or workspaces and do not appear when the project is opened in Xcode 3.2.

  Click the breakpoint symbol in the breakpoint navigator to enable or disable it; double-click it to set the breakpoint condition, action, and options.

  The debug navigator shows all active threads in the process. The Stack Compression slider at the bottom reveals or hides redundant or irrelevant stack frames in all threads; the Σ button hides running threads with no frames in your code. Any Memory Viewers you have opened on locations or variables also appear in the debug navigator.

  Breakpoints, the Program Counter bar, Data Tips, and In-Editor Controls appear in the source editor while debugging just as in Xcode 3.2.
- _Debugging Tools_

  The `lldb` debugger is new in Xcode 4 and is still under development. While it offers basic functionality in this Developer Preview, it is not fully featured. See the LLVM project page at [http://lldb.llvm.org](http://lldb.llvm.org) for more information on `lldb`.
- _Packaging and Distribution_

  Similar to Launch Schemes, a Distribution Scheme is a plan for building one or more targets and running unit tests, but instead of executing the build product, a Distribution Scheme designates an operation for archiving and distributing it. You generally use a Distribution Scheme at milestones in product development, such as posting a nightly build, seeding a preview copy, or shipping your final release.

  A Distribution Scheme has Build and Test actions just like a Launch Scheme, but also has an Archive action that packages the build products in a designated manner. Like Launch Schemes, each action has pre-action and post-action scripts to perform useful tasks at that phase of the operation.

  The Archive step of a Distribution Scheme allows you to choose to archive an application alone, or to package all build products for the scheme into a single disk image (.dmg) file.
- _Indexing_

  Xcode 4 has an entirely new mechanism for indexing files in a workspace. An index is created for the entire workspace, so references across projects are resolved.

  The indexer now uses the LLVM compiler 2.0 to parse source files. This results in improved performance and higher accuracy; most importantly, the interpretation of symbols for indexing more closely matches the interpretation of syntax at compile time.

  The index is stored in the Index subdirectory of the workspace’s unique directory in `~/Library/Developer/Xcode/DerivedData`. Manage this information (including deleting the index and other derived data of an orphaned project) in the Organizer.

  Indexing is done in the background; the Activity View indicates when indexing is being performed. Until the index is ready, some functions that require the index may not be available (for example, Open Quickly); others may have degraded performance (for example, syntax coloring of system symbols). When the index is complete these features become available immediately.
- _Snapshots_

  The Snapshots feature has been reimplemented to be faster and more reliable. Note that you must install the System Tools in the Xcode 4 installer in order to use snapshots.

  Create a snapshot manually or automatically before a Find and Replace operation. The Settings sheet (File > Project Settings) allows you to designate the storage location of the snapshot backing store.
- _SCM_

  Configuration of SCM repositories is done in the Organizer instead of a preference pane. If you open a project or workspace that was checked out of an SCM system using the command line or another tool, Xcode automatically configures the SCM repository support for that project or workspace.

  Support for git has been added and support for Subversion has been enhanced to support annotations. The git tools are installed when you check the System Tools check box in the Xcode 4 installer. Perforce and CVS Source Code Management systems are no longer supported.

  SCM status is shown as a badge in the project navigator, using the conventional set of mnemonics (U for updated in repository, M for locally modified, A for locally added, D for locally deleted, I for ignored, R for replaced in the Repository). Badges propagate up to the highest container so you see the SCM status of the whole workspace regardless of the disclosure level. An asterisk badge on a container means its contents have mixed status. Detailed SCM status is also available in the SCM area of the File Inspector.

  Selecting any file under SCM control and clicking the Version Editor brings up that file in a side-by-side view. Clicking the Timeline icon in the center column shows a visual timeline of all repository versions; use the sliders to control which side shows which version. If one side is your working copy, you merge changes to it from any repository version using the Version Editor. In Xcode 4, the working copy of a file is on the left.

  Buttons under the Version Editor allow you to show a file comparison and timeline; change logs for the file; or individual change annotations (“blame”) for each line of the file.

  SCM commands are now in the Source Control submenu of the File menu, rather than in a separate SCM menu. The SCM sheet allows you to select individual files for a given SCM action, and preview the differences before you confirm the action.

  Update and commit operations are recorded in the log navigator. By selecting a log you see the individual steps of that operation in the Log Editor.
- _Searching_

  The find navigator searches the entire workspace. It shows Find Results in text files, property lists, data models, and build settings in projects and targets.

  The magnifying glass icon in the Search field reveals a list of recent searches. Choose Show Find Options to set Textual or Regular Expression search style, whether the search result must contain or match exactly the search term, whether to match or ignore case, and what subset of the workspace or project to search.
- _Status and Activity_

  An Activity View in the center of the toolbar shows a progress indicator for ongoing activities, and the names of background activities (indexing, checking SCM status) that are also being performed. The Activity View displays “Welcome to Xcode” when Xcode is idle.
- _Alerts_

  The Alerts preference pane allows you to specify actions that occur when certain operations are initiated or completed. You use this to tailor your workflow, for example, to always show the latest Build Log when you start a build. Triggers include starting and stopping building, testing, launching, searching, or restoring a device; actions include playing sounds, bouncing the dock icon, or executing a script.
- _Organizer_

  The Xcode Organizer is no longer an arbitrary container for files and folders; that functionality has been moved to the Workspace. It is still the window where you manage iPhone, iPod Touch, and iPad devices. In addition, SCM Repository Management has moved from the Preferences pane to the Organizer, and Developer Documentation has moved from its own window into the Organizer.

  The Organizer also has a new section for Archives, which provides access to the archived applications and disk images created by Distribution Schemes.
- _Key Bindings_

  Because Xcode 4 has a different menu structure, many Xcode 3.2 menu commands no longer exist in Xcode 4. Some of their menu key bindings have been reassigned to new functions in Xcode 4, and the key bindings of other menu items have been changed to be consistent.

  |  |  |  |
  | --- | --- | --- |
  | __Key Binding__ | __Xcode 3.2 Meaning__ | __Xcode 4 Meaning__ |
  | ⌘⌥B | Show Breakpoints | Edit and Build Scheme |
  | ⌃⌘B | Show Model Browser | Build and Analyze |
  | ⌘⌥C | Copy Style | Commit |
  | ⌘D | Add Bookmark | Duplicate |
  | ⌘⇧D | Open Quickly (now ⌘⇧O) | Jump to Definition (equivalent of ⌘-double-click) |
  | ⌘⇧⌥D | Open This Quickly (now ⌃⌘O) | Unassigned |
  | ⌘⇧E | Toggle Editor | Use Selection for Replace (was ⌃⌘E) |
  | ⌃⌘E | Use Selection for Replace (now ⌘⇧E) | Edit All In Scope (was ⌃⌘T) |
  | ⌘⌥F | Find in Detail | Find and Replace |
  | ⌘I | Get Info/Show Inspector (now ⌘⌥1) | Step Into (was ⌘⇧I) |
  | ⌘⇧J | Refactor | Jump to Line (was ⌘L) |
  | ⌘L | Go to Line (moved to ⌘⇧J) | Reveal in Navigator |
  | ⌃⌘N | New Empty File | New Workspace |
  | ⌘⇧O | Step Over (now ⌘P) | Open Quickly (was ⌘⇧D) |
  | ⌃⌘O | Organizer (now ⌘⇧2) | Open This Quickly (was ⌘⇧⌥D) |
  | ⌘P | Print | Step Out (was ⌘⇧T) |
  | ⌘⇧R | Console | Run without Building (was ⌘⌥R) |
  | ⌘⇧⌥R | Clear Console | Edit Scheme and Run |
  | ⌘T | Show Fonts | Test |
  | ⌘⇧T | Step Out (now ⌘P) | Test Without Building |
  | ⌘⌥U | Ungroup | Update |
  | ⌘⌥V | Paste Style | Special Paste |
  | ⌃⌘W | Close Project | Close Current File (was ⌘⇧W) |
  | ⌘Y | Build and Debug – Breakpoints On | Enable/Disable Breakpoints (was ⌃⌘\) |
  | ⌃⌘Y | Debug – Breakpoints On | Pause (was ⌘⌥P) |
  | ⌘0 | Project | Hide Navigator |

### Known Missing Functionality in This Release

This Developer Release of Xcode 4 does not implement the following features.

- New Untitled File
- Compile, Preprocess, Show Assembly Code
- Distributed Builds
- Refactoring
- Specific functionality for Test action in Launch Schemes and Distribution Schemes
- Replace in Selected Text
- Duplicate for files, folders, and targets
- Key binding sets for other editors
- User Script menu or editor
- xed
- Target editing for External (makefile) targets
- Editing .nib or .xib files that require custom plug-ins at build time
- Target Membership inspector
- Connections to custom actions and outlets in iPad interface builder files. Use the Connect to Source Code feature to make these connections.
- Searching in Interface Builder files
- Creating custom or placeholder objects in iPad Interface Builder documents. Copy and paste an existing placeholder from another document.
- Debugging with `lldb` works with iPhone and iPad apps in the simulator, but not on the device

### Known Problems in This Release

Xcode 4 Developer Preview is pre-release software. Please file bugs at [http://bugreport.apple.com](http://bugreport.apple.com) for performance and stability issues, data loss or file corruption, missing or unimplemented features, behavioral or aesthetic issues, and feature and enhancement requests. Provide as much context as possible, especially crash logs or samples, detailed Steps to Reproduce, and projects or workspaces when possible.

These problems are already known in this release:

- Duplicating a Localization in the project editor may not work if the project is under SCM control.
- Following a link in the Documentation Viewer may cause a crash if the linked document is expected to be in the local documentation set but is missing. 8017277
- Clicking a Find Result of a build setting opens the containing project or target, but does not scroll to and select the actual found setting. 7749874
- Canceling a build may leave the spinning Progress indicator in the Build item in the log navigator. 7735752
- Reveal in Navigator selects the file in the project navigator, but may not scroll it into view. 8003741
- Most definitions in Xcode’s scripting dictionary are currently unimplemented. 7948823
- The Editor > Add Build Phase menu items are not enabled unless you select a file in a current build phase. Use the Add Build Phase button in the editor.
- The Relative to Build Folder, Relative to Developer Folder, Relative to Build Products, and Relative to Path (source tree) reference styles are not shown correctly in the File Inspector and cannot be set in the File Inspector. Values set correctly in existing projects work correctly. Dragging build products between projects in a workspace may not create build product references correctly.
- Locked files are generally not handled. The File Inspector usually gives an indication of file locked state, but no attempt is made to prevent or warn about operations on locked files. 7338327
- Adding or moving files in a project may not add them to the correct build phase. After adding a file, you should check the target build phase to ensure the file is built by the desired target(s) correctly.
- Build files in the Compile Sources phase are displayed in alphabetical order and you cannot change the order. If you add a new file, the build files are saved to the project file in alphabetical order and built in that order. If order is important to building or linking that target, this may cause the build to fail.
- “Open These Results As Transcript Text File” is not working. 8041039
- Disk images created by a Distribution Scheme are not showing up in the Organizer.
- Deleting projects from a workspace may not correctly update schemes that rely on that project’s targets. You may wish to delete and recreate schemes after deleting projects from a workspace. 7901251
- In certain circumstances, opening a workspace opens it in two independent windows. 7336838
- Arguments and environment variables for a Launch action cannot be reordered. 7909498
- If you see XML text instead of the Interface Builder editor for an Interface Builder file, open the Inspector area and set the File Type to “Default,” then close and re-open the document.
- Interface Builder objects are not automatically resized to fit their containers after certain operations. Choose Size to Fit from the Editor menu to ensure objects are the correct size.
- Views marked “hidden” in an Interface Builder document are not shown in the Interface Builder editor. Choose them from the Jump Bar or Document Outline view.

### Functionality No Longer Supported in Xcode

The following features and functionality have been removed from Xcode. When substitute functionality is available, it is noted.

- Layout modes
- Class Browser. Use the symbol navigator and Class Navigation menu in the Editor.
- Active Target/Configuration/Architecture/SDK/Executable toolbar items and Project menu entries. Configure a Launch Scheme for a particular combination of target/configuration/architecture/SDK/executable that is useful to you using the Scheme toolbar popup.
- Bookmarks
- Favorites bar
- Detail views
- Class model
- Touch an individual file
- Recent Files menu item in the File menu. The Navigation buttons have a list of recent files. Also, use the filter in the project navigator to show all recently-viewed files in the project or workspace.
- Support for External Editors
- Worksheet (Control-R) execution of shell script commands in text documents
- Predictive Compilation (generally replaced by Fix-It Hints)
- Fix and Continue
- Breakpoint navigation menu in the jump bar
- Editing and compiling AppleScript .scpt files
- Perforce and CVS source code management
- Dock Icon Menu of open Xcode windows (in Snow Leopard, press and hold on the Dock tile to see all Xcode windows)
- Editing Carbon nib files. Xcode 4 supports building Carbon xib and nib files; use Interface Builder 3.2 to edit them.

[Next](Document%20Revision%20History.md)[Previous](Xcode%205%20Release%20Notes.md)

