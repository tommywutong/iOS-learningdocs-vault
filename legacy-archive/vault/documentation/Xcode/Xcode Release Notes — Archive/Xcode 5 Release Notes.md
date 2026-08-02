---
title: Xcode Release Notes — Archive
apple_id: TP40016994
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/xc5_release_notes.html
archived_at: '2026-07-26T19:54:16.494274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Release Notes — Archive](Xcode%20Release%20Notes%20%E2%80%94%20Archive.md)


[Next](Xcode%204%20Release%20Notes.md)[Previous](Xcode%206%20Release%20Notes.md)

# Xcode 5 Release Notes

## Xcode 5.1.1 Release Notes

### Resolved Issues

#### Build System

- Updated compiler options logic allows "Enforce Strict Aliasing" to be set to off with the `-Ofast` flag (16368909)
- Errors when using `xcodebuild -parallelizeTargets` option or equivalent Xcode build setting (16420957)

#### Compiler

- Crash in compiled code when using ARC and C++ (16368824)
- Compiler error when using the `-fsanitize=undefined-trap` and `-fsanitize-undefined-trap-on-error` options (16387418)
- Crash in compiled code when targeting iOS 5.1.1 (16485980)
- Compiler crashes when compiling C++ initializers and other situations (16438726, 16368865)

#### Linker

- Crashes and errors in the linker related to LTO, dead stripping, and branch out of range (16368534, 16368564, 16368631)

#### Debugging

- Xcode crash when debugging (16369101)
- Issue where some objects would not display in the Quick Look display on the first try (16368930)
- Inconsistent behaviors in the `UIView` Quick Look display (16368999)
- Problem with Quick Look for `UIImageView` (16489265)
- Xcode crash with multiple debugging sessions (16369025)

#### Testing

- Compiler error after converting a project from OCUnit to XCTest (16387456)

#### Xcode Server

- Issue where Xcode Server sometimes incorrectly claims that the version of OS X Server is incompatible (16436893)

## Xcode 5.1 Release Notes

### New Features

#### Debugging

- Quick Look can be implemented for developer defined classes

  When an instance of a custom class is viewed with Quick Look in the debugger variables view or a data tip, the debugger presents it using a method named `-debugQuickLookObject` defined in the class implementation. For details on how to use this capability, see _[Quick Look for Custom Types in the Xcode Debugger](../../IDEs/Quick%20Look%20for%20Custom%20Types%20in%20the%20Xcode%20Debugger/About%20Variables%20Quick%20Look%20for%20Custom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dambr)_. (12723736)
- Log breakpoint actions now print out the logical value of expressions.

  For example, a log breakpoint action such as `"myString = @myString@"` now prints the value of `myString`, rather than the pointer value. (13211695)

#### Editing User Interfaces

- Interface Builder documents can contain specific information about new features they use and the OS versions they require, allowing previous versions of Xcode to display better warning messages when trying to open such documents. (7659982)
- Building interfaces in Interface Builder using auto layout offers the full suite of possible constraint types: aspect ratios, proportional sizes and positions, cross attribute alignments, and a new constraint inspector with features for editing nearly all properties of a constraint.
- The Interface Builder constraint Attributes inspector shows a constraint's items and attributes and allows editing of the attributes. This feature enables the ability to create cross-attribute constraints such as `view1.centerY = view2.bottom`. (13739009)
- You can use Interface Builder to edit the relation of any type of constraint, including alignment constraints (for instance, `view1.leading <= view2.leading`) and equal size constraints (for instance, `view1.width >= view2.width`). (14721954)
- You can create aspect ratio and proportional sizing constraints and edit the multiplier of constraints in Interface Builder. The multiplier can be a decimal number (for example, `0.5`), a fraction (for example, `1/2`), or an aspect ratio (for example, `1:2`). (11935843)
- Constraints attached to ambiguous views in Interface Builder are drawn orange only in the axis with ambiguity. This makes it faster to identify a potential problem in the canvas. (15114120)
- The Interface Builder canvas now displays overlay scrollers when appropriate, based on the “Show scroll bar” setting in the General pane in System Preferences. (10069033)
- The Interface Builder inspector now has support for:

  - `NSTableView` - `floatsGroupRows` property (9617000)
  - `UISegmentedControl` - `apportionsSegmentWidthsByContent` property (9950528)
  - `UITableView` - `sectionIndexBackgroundColor` property (14776025)
  - Setting “Detail” button type for prototype `UITableViewCell` - `editingAccessoryType` property (15039987)

#### Instruments and Symbolication

- Instruments now finds symbols much more reliably.

  If symbols aren't showing up automatically, try the following:

  - When Spotlight indexing is disabled for Xcode derived data, such as when using `/tmp`, add a global list of additional search paths configured in the Instruments preferences.
  - The context menu for an address now includes the option “Symbolicate with DSYM” to add a specific symbol file.
  - Use the File menu Symbols command to see a more detailed list of the state of individual executables and libraries.

    - Green lights indicate the presence of symbols and source information.
    - Yellow lights indicate libraries with some symbols but can still benefit from locating a dSYM.
    - Red lights indicate situations that prevented symbolication. (14269449)
- The `instruments` command-line tool now supports specifying the simulator SDK and device type using the `-w` flag. To see a list of the supported simulator configurations as well as attached devices, execute `instruments -s devices` in a Terminal window. (14996865)

#### Scripted installation

- Installing Device Support

  Run from the command-line, Xcode.app takes the new command-line argument, `-installComponents`. When Xcode is run from a command-line script with this option, it installs the required device support packages and then quits. (15127411)

#### General

- Emoji and other Unicode surrogate pairs are supported in scheme settings and in project files. (14837623, 13827044)

### Changes

#### Building

- Arm64 is now included in the “Standard architectures” setting.

  Xcode 5.0 introduced support for building 64-bit iOS applications but it was not enabled by default. To enable the option of building 64-bit in Xcode 5.0, an architectures setting was provided: “Standard Architectures Including 64-Bit” (`ARCHS_STANDARD_INCLUDING_64_BIT`).

  With the introduction of Xcode 5.1, arm64 is included in the default "Standard architecture” build setting. This results in projects using the default setting automatically building for arm64 along with the standard 32-bit architectures.

  __Note:__ Be aware of the following architectures issues when opening your existing projects in Xcode 5.1:

  - When building for all architectures, remove any explicit architectures setting and use the default Standard Architectures setting. For projects that were previously opted-in using “Standard Architectures Including 64-Bit”, switch back to the “Standard architectures” setting.
  - When opening an existing project for the first time, Xcode 5.1 may display a warning about the use of the Xcode 5.0 architectures setting. Selecting the warning provides a workflow to revise the setting.
  - Projects not able to support 64-bit need to specifically set the architectures build setting to $(ARCHS_STANDARD_32_BIT).
- Projects configured to use ”Standard Architectures Including 64-bit” will be converted to “Standard Architectures `$(ARCHS_STANDARD)`.

#### Compiler

- As of Apple LLVM compiler version 5.1 (clang-502) and later, the optimization level `-O4` no longer implies link time optimization (LTO). In order to build with LTO explicitly use the `-flto` option in addition to the optimization level flag. (15633276)
- The Apple LLVM compiler in Xcode 5.1 treats unrecognized command-line options as errors. This issue has been seen when building both Python native extensions and Ruby Gems, where some invalid compiler options are currently specified.

  Projects using invalid compiler options will need to be changed to remove those options. To help ease that transition, the compiler will temporarily accept an option to downgrade the error to a warning:

  `-Wno-error=unused-command-line-argument-hard-error-in-future`

  __Note:__ This option will not be supported in the future.

  To workaround this issue, set the `ARCHFLAGS` environment variable to downgrade the error to a warning. For example, you can install a Python native extension with:

  `$ ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future easy_install ExtensionName`

  Similarly, you can install a Ruby Gem with:

  `$ ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future gem install GemName` (16214764)

#### Testing

- The `gcov` tool for code coverage testing has been reimplemented. The new version uses the `llvm-cov` tool from the LLVM project. It is functionally equivalent to the old version for all significant features. The location of `gcov` within Xcode has also moved, use xcrun to invoke it. If you find problems, please file bug reports. For this release, you can still use the old version of `gcov` from GCC, which is available as `gcov-4.2`. (11919694)

### Known Issues

#### Editing User Interfaces

- Custom views added to a stack view in Interface Builder can get stuck in a “misplaced views” (inconsistent) state.

  As a workaround, set a placeholder intrinsic size for the custom view with appropriate content hugging and compression resistance priorities. (15778653)

#### Testing

- Automated tests run in iOS Simulator may fail with an error similar to this:

  `Test target [test name] encountered an error (Test process exited with code -1)`

  Attempt recovery by quitting and restarting the simulator. (15929053)

#### Xcode Server

- Continuous integration features (bots) of Xcode 5.1 require OS X Server v3.1 (or a version of OS X Server 3.1 beta) or later. (16225068)
- If there are old copies of Xcode on the server host, Xcode Server sometimes shows all the simulators. Only attempt to use simulators appropriate for use with Xcode 5.1. (15465692, 15153869)
- Xcode Server will offer All Devices or All Simulators even if there are none that fit the criteria for the project. If you select an inappropriate device or simulator, you may get an error similar to:

  `xcodebuild: error: No destinations were specified with the -destination flag which were valid for the specified scheme <scheme_name>.`

  To prevent this from happening, specify only valid devices or simulators for your project. (15465222)
- Sometimes when you’re attempting to create a new local repository on OS X Server through Xcode, Xcode may display an error message similar to:

  `xcode-select: note: no developer tools were found at '/Applications/Xcode.app', requesting install. Choose an option in the dialog to download the command line developer tools.`

  To resolve this problem, follow the prompts in the dialog displayed on the OS X Server host system. (15475078 & 15486464)
- Sometimes after upgrading to Xcode 5.1 and OS X Server 3.1, the first time you add a server you may see an error similar to:

  `“<Server> is running a version of OS X Server that cannot be used with this version of Xcode.”`

  Quit and restart Xcode one time to clear this message. (16217715)

#### iOS Simulator

- Performance issues can arise when running apps within the iOS Simulator on OS X Mavericks with a simulated OS version of iOS 6.1 or earlier.

  A workaround is to disable timer coalescing while using the iOS 6.1 or earlier simulator by executing the following command in a Terminal window:

  `sudo sysctl -w kern.timer.coalescing_enabled=0` (15501929)
- iOS Simulator sometimes stops responding to hardware keyboard.

  Quitting and relaunching the simulator usually corrects this. (14642684)

#### Debugger

- Quick Look for `UIView` and `UIColor` variable types may not always work correctly.

  You can capture variables of these types as `id` rather than `UIView` or `UIColor`. 16065049

#### General

- When validating multiple applications in sequence using the Xcode Organizer, erroneous warnings about bundle IDs may be emitted.

  If these warnings occur, quit & relaunch Xcode in between validations. (15113664)
- Executables created by Xcode 5.1 may crash on OS X v10.5. (15852259)

### Resolved Issues

#### Testing

- The `XCTAssertEqual` macro (formerly `STAssertEquals` using OCUnit) correctly compares scalar values of different types without casting, for example, `int` and `NSInteger`. It can no longer accept nonscalar types, such as structs, for comparison. (14435933)

#### General

- OS X apps that require a provisioning profile, such as those using iCloud, now build, are code-signed correctly, and launch. (15841159)

### Deprecations

- OCUnit and the SenTestingKit framework are deprecated and will be removed from a future release of Xcode. Source code using OCUnit generates warnings while being compiled in Xcode 5.1.

  Migrate to XCTest by using the “Edit > Refactor > Convert to XCTest…” menu command. .
- The ATS framework is deprecated. Source code using ATS APIs will generate warnings while being compiled. For version 10.8, there will be no loss of functionality but there could be areas where performance will suffer.

  Replace all ATS code (including `ATSUI`) with `CoreText`. ATS functionality will be removed in future OS X releases.
  More information about this change is available in _[Core Text Programming Guide](../../Strings%20Text%20Fonts/Core%20Text%20Programming%20Guide/About%20Core%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzt)_.

## Xcode 5.0.2 Release Notes

### Known Issues

The following known issues are noted for Xcode 5.0.2 in addition to what has been listed for Xcode 5.0.1.

#### Editing User Interfaces

- In iOS 7 Interface Builder documents, when a vertical spacing constraint is created between a view that is flush with the top or bottom layout guide, a constraint between the guide’s top edge and the view’s bottom edge may be created instead of from the guide’s bottom edge to the view’s top edge.

  Move the view 1pt down (if to the top layout guide) or up (if to the bottom layout guide), create the vertical spacing constraint, then change the constraint’s constant from 1 to 0. 14627548

#### Performance Measurement and Analysis

- The message “Could Not Start Script : Target app is not frontmost” may be displayed when attempting to capture a UI Automation script in Instruments against the iOS 7 Simulator.

  If this occurs, close the trace document and create a new one. 15387075

### Resolved Issues

#### Debugging

- LLDB now correctly displays structs in simulator processes. 14496092
- Debugging an application on a device running iOS 6.x caused the application to crash with EXC_BAD_ACCESS. 15310896

#### iOS Simulator

- After installation of Xcode, the iOS 7.0.3 simulator would hang on first launch for a period of time (eventually launching). 15368009
- Running UIAutomation from the Instruments GUI or from the `/usr/bin/instruments` command line would hang. 15367995

#### General

- Launching a 64-bit application on a device from Xcode multiple times caused the device to stop responding (and required a soft-reset). 15338361

## Xcode 5.0.1 Release Notes

### New Features

#### Accessing Help and Documentation

- The documentation window now has a navigator area that contains a library browser and the bookmarks list. You can show the current document in the library browser using either the Editor > “Reveal in Library” menu item or by selecting the contextual menu "Reveal in Library.” 12116524

### Known Issues

#### Building

- New application targets created in Xcode 5 will crash on launch on iOS 5.

  Turn off Base Localization if your app targets iOS 5. 13979280
- Building a project from inside VMWare that is accessible via a VMWare shared folder can cause the compiler to crash.

  Use AFP to share files instead. 14251948

#### Continuous Integration with OS X Server

- Communicating with a remote SVN repository over HTTPS can fail with an error similar to “Error validating server certificate for _server name_.”

  Edit the file `/Library/Server/Xcode/Config/xcsbuildd.plist` and change the `TrustSelfSignedSSLCertificates` key from `false` to `true`.

  Then, from a Terminal window, run: `sudo killall xcsbuildd`. 14639890
- SSH access permissions for remote repositories created from within Xcode are limited to only the user that created them, by default. The permissions for these hosted repositories cannot be changed from within Xcode.

  The permissions can be changed for a hosted repository in Server.app by visiting the Xcode service—under the repositories tab, double click the repository and change the access settings. 15193716

#### Editing User Interfaces

- If you open a read-only xib or storyboard file that was last saved with an older version of Xcode, you might not be able to quit Xcode.

  You must first close the xib or storyboard file using control+command+W or by using the File > Close _filename_ menu command. 14715366
- You cannot drag a placeholder object from the Interface Builder object library into the outline.

  Drag the placeholder object into the canvas background. 13731313
- Sometimes when editing UITableViews in Auto Layout documents set to open in Xcode 4.6, an error message is displayed which says “Failed to automatically update constraints.”

  Upgrade your document to Xcode 5 format using the “Opens in” option in the file inspector. After performing the desired edits, you can downgrade back to the Xcode 4.6 format if necessary. 14680132
- In some instances, number formatters created in Interface Builder with “Currency” style will not display the localized currency symbol at runtime.

  In Interface Builder, switch the number formatter’s “Behavior” from `OS X 10.4+ Default` to `OS X 10.4+ Custom`, then back to `OS X 10.4+ Default`. 14378988
- Xib files containing an instance of QCView from Quartz Composer fail to build, and cannot be processed by ibtool.

  Replace the instance of QCView on the canvas with an instance of custom view from the library and set its custom class to “QCView” in the identity inspector. 14991302
- The UIAAlert `defaultButton` and `cancelButton` functions will fail for some two-button alerts when targeting iOS 7. 14649998

#### Auto Layout: Runtime

- In some cases the “Update Frames” command does not resize top-level views or windows.

  Use the “Update All Frames” menu item. 13716892
- Constraints owned by the clip view of a scroll view in Interface Builder, where the document view is a custom view, are removed at runtime.

  Create outlets to each of the constraints you want to keep and re-add them to the clip view at runtime. 15115315

#### Asset Catalog

- After importing images from a project into an image catalog, storyboards and xib files have broken image file references.

  The image names in Interface Builder are listed as `image-name.png` and should be shortened to `image-name` to repair the broken reference. 14042186

#### Localization

- Projects and targets which have only `strings` files as localized resources cannot be converted to use Base Localization. (The behavior you observe is that after checking the “Use Base Localization” checkbox in the project editor, the conversion sheet does not present any files to be converted and clicking the Finish button results in the checkbox becoming unchecked.)

  To convert to using Base Localization, a project or target must contain one non-`strings` resource enabled for localization. In the project navigator, select a resource you intend to localize (for example, an Interface Builder document or an image), then open the file inspector. In the Localization slice, click the Localize button and select the localization to add. Once complete, the conversion workflow displays the file and enables the checkbox. 15160454

#### Objective-C Runtime

- In the 32-bit iOS 7.0 simulator, manually calling `objc_msgSend_stret()` with a `nil` receiver can corrupt the stack pointer.

  Ensure that the receiver is non-`nil` before calling `objc_msgSend_stret()`. 14753273

#### Debugging

- Watchpoints set on a variable from Xcode’s UI using the contextual menu in the variables view don’t work for some variables—for example, `self`. When this is the case you’ll notice that the watchpoint is not being hit when you would expect.

  To work around this issue, use the console in Xcode to create a watchpoint at the `lldb>` prompt with the command `watchpoint set variable <variable-name>`. 12658775
- When ending the debug session of an app on an iOS 5 device, the error message “Lost Connection” may be displayed.

  Dismiss the error pop-up. It is spurious and does not indicate any problem debugging your app or connecting to the device. 14871460
- If an application on an iOS device is paused in the debugger within the method `-application:didFinishLaunchingWithOptions:`, the debugging session must be stopped before building and relaunching the same application with a different build configuration.

  If the application is not stopped first, the device can enter a state where it will no longer launch applications. If the device enters this state, it must be rebooted in order to be used for development again. 14851115
- If an iOS app running in the simulator is detached, a relaunch of the same app from Xcode will result in a black screen in iOS Simulator even though the new instance of the app is launched.

  Terminate the app in the simulator, or relaunch it a second time. 14648784

#### Debugging: Open GL

- The OpenGL ES frame debugger fails to display texture mip-levels for textures that are not texture-complete. 14852587

#### Performance Measurement and Analysis

- The Allocations instrument can only attach to processes on devices running iOS 7.

  Processes must be started by Instruments for earlier versions of iOS. 14065257
- When attaching with the Allocations instrument to a process running on an iOS 7 device, the target process may crash and the recording in the Allocations instrument then stops immediately. When attaching with Allocations to a process on an iOS 6 or earlier device, the target process should continue to run but no data will be collected in Allocations.

  Launch with Xcode and then attach with Instruments or transfer to Instruments by clicking “Profile in Instruments,” using the memory gauge in the debug navigator. 14828459

#### Testing

- XCTest does not support iOS 6 destinations.

  Xcode does not prevent you from using XCTest with iOS 6 destinations, resulting in undefined behavior. 14075515

#### Account Management

- Sometimes after requesting a signing identity from the Member Center, Xcode does not install the corresponding certificate in the keychain.

  To work around this issue, perform the following steps:

  1. View the Accounts section of Xcode’s preferences
  2. Select the account or team that corresponds to the signing identity
  3. Click “View Details”
  4. Click the Refresh button at the lower-left of the details sheet 14197131

#### Source Control

- Xcode may have trouble connecting to repositories if credential information has changed after the repository was added in the Accounts preferences. In certain cases, Xcode displays a failure when connecting to a repository while it is actually attempting to connect in the background.

  If you encounter a repository connection problem, remove and re-add the repository with the updated credential information. This will restore access to the repository. 13955597

#### iOS Simulator

- After switching the minimum deployment target of an application from iOS 7.0 to a release prior to iOS 7.0, building and running the application may fail with the message “iOS Simulator failed to install the application.”

  To resolve this issue go to the iOS Simulator home screen. Remove the application by clicking and holding the application icon, and then choosing to delete the application by tapping the hovering “X” button. 13917023
- The Mac hardware keyboard may not function for iOS Simulator when first launched.

  Relaunch the simulator. 13315258
- StoreKit (In-App purchases) will not work in the Simulator. 13962338

#### General

- When playing video via the Quicklook framework on an iPhone simulator, the video view appears black, but audio continues to play fine. 13871109

### Resolved Issues

#### Editing User Interfaces

- Views without an autoresizing mask in Interface Builder documents did not open correctly. 14969450
- When loading nibs at runtime with scroll views built with Xcode 5, constraints between the clip view and its document view were not handled properly. 14097019

#### Accounts

- Creating distribution signing assets caused Xcode to crash. 13956010

#### OpenGL

- Launching an app using OpenGL on more than a single device failed. 14836639

#### Source Control

- Subversion URLs caused errors with variable username usage. 14825641
- Using HTTPS and a git repository with a self-signed certificate failed. 14060992

  If you are interacting with a hosted git repository on OS X Server using HTTPS and are presented with a certificate dialog, to use the git repository:

  1. Click “Show Certificate” on the bottom-left of the dialog
  2. Check the “Always Trust” checkbox
  3. Click “Continue”

  You are now able to use the git repository in Xcode.

### Notes

#### Accessing Help and Documentation

- Xcode 5 does not support downloading additional doc sets. Additional doc sets can be added manually by installing them at `~/Library/Developer/Shared/Documentation/DocSets/`.

  Once installed, doc sets are found and loaded by Xcode 5. If Xcode is running while the doc set is installed, quit and relaunch Xcode. 14930443

#### Building: Deployment Compatibility

- iOS 64-bit compatible applications are only supported with a minimum deployment target of iOS 5.1.1 or above. 15190445

#### Account Management

- The provisioning profiles list in the Organizer is now located in the Accounts tab of Xcode's preferences. To view them, select the relevant Apple ID account and tap View Details. 13950944

#### Deprecations

- Xcode 5 does not support use of the LLVM-GCC compiler and the GDB debugger. 14857582
- Garbage collection is a deprecated technology in OS X Mountain Lion and later. Xcode 5 is scheduled to be the last release of the Xcode developer tools to support building, debugging, or profiling Mac apps that use garbage collection.

  It is recommended that any projects using GC employ Xcode’s migration tool to convert to ARC (Automatic Reference Counting). For more information about transitioning to ARC, see _[Transitioning to ARC Release Notes](../../../releasenotes/Objective%20C/Transitioning%20to%20ARC%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrw)_. 14406894
- The CVS and RCS source control tools have been removed from Xcode 5. 11968433
- The CPlusTest unit testing framework has been removed from Xcode 5. To write unit tests for C++ code, use the new XCTest framework and create Objective-C++ (.mm) test case subclasses. 8273037
- `SenTestingKit` and `OCUnit` are deprecated. Use the migrator to move to XCTest. 14857574

#### Continuous Integration with OS X Server

##### Installing Xcode on OS X Server

- To ensure that OS X Server is configured to use Xcode 5.0.1, follow these steps to install Xcode:

  1. Open the App Store and update OS X Mavericks
  2. Download Xcode 5.0.1 and OS X Server
  3. Quit Xcode and Server
  4. Install Xcode 5.0.1
  5. Install OS X Server
  6. Open Server
  7. Select the Xcode service, then click Choose and select Xcode 5.0.1

##### Reporting Bugs

- When reporting a Continuous Integration bug, enter the following command in Terminal, then attach the output to the bug report.

  `sudo /Applications/Server.app/Contents/ServerRoot/usr/sbin/serverloggather`

##### Communication between Xcode and Server

Communication between Xcode and the Xcode service is currently over HTTP port 80.

- For accessing local Git repositories hosted by the Xcode service:

  - Git+SSH: 22
  - HTTP: 80
  - HTTPS: 443
- For accessing remote SVN or Git repositories not hosted by the Xcode service:

  - Git: 9418
  - Git+SSH: 22
  - SVN: 3690 (anonymous access only)
  - SVN+SSH: 22
  - HTTP (Git + SVN): 80
  - HTTPS (Git + SVN): 443
- For joining a server to an Apple Developer Team:

  - HTTPS (SSL): 443

#### Command Line Tools

- Command line shims are included with OS X Mavericks. If Xcode is installed, the shims use the tools within Xcode. Otherwise, the tools delivered in the Command Line Developer Tools package are used. The Command Line Developer Tools package can be installed on demand using `xcode-select --install` or by trying to use any command line developer tool in Terminal.

  On OS X Mavericks, Command Line Developer Tools are updated using Software Update. On OS X Mountain Lion, continue to use the Downloads preferences in Xcode to update the Command Line Developer Tools.

  On OS X Mavericks, `xcode-select` provides the `--reset` flag to revert to using the default search paths.

  The Command Line Developer tools package has been updated to include `xcrun`. `xcrun` adds support for the following:

  1. The `--show-sdk-path` option queries SDK paths
  2. Improved `xcrun` performance
  3. More robust support for the `DEVELOPER_DIR` environment variable

     Set `DEVELOPER_DIR` to either a copy of Xcode or `/Library/Developer CommandLineTools` when Command Line Tools for OS X Mavericks is installed
  4. `xcrun` passes the SDK provided to subcommands in the `SDKROOT` environment variable when used with --sdk. 15190491

## Xcode 5.0 Release Notes

### Known Issues

#### Compiling: LLVM

- Building a project from inside VMWare that is accessible via a VMWare shared folder can cause the compiler to crash.

  - Use AFP to share files instead. 14251948
- In the 32-bit iOS 7.0 simulator, manually calling `objc_msgSend_stret()` with a `nil` receiver can corrupt the stack pointer.

  - Ensure that the receiver is non-`nil` before calling `objc_msgSend_stret()`. 14753273

#### Building

- New application targets created in Xcode 5 will crash on launch on iOS 5.

  - Turn off base localization if your app targets iOS 5. 13979280

#### Editing User Interfaces

- If you open a read-only xib or storyboard that was last saved with an older version of Xcode, you might not be able to quit Xcode.

  - You must first close the file using ctrl+cmd+w or by going to File > Close `<filename>`. 14715366
- In some instances, number formatters created in Interface Builder with “Currency” style will not display the localized currency symbol at runtime.

  - In IB, switch the number formatter's “Behavior” from “OS X 10.4+ Default” to “OS X 10.4+ Custom,” then back to “OS X 10.4+ Default.” 14378988
- When loading nibs at runtime using scroll views built with Xcode 5, constraints between the clip view and its document view will be removed. This only affects constraints between the clip view and the document view, which are usually constraints such as `H:|-[documentView]-|` and `V:|-[documentView]-|`.

  - Add the constraints at runtime. 14097019
- UIAAlert’s `defaultButton` and `cancelButton` functions will fail for some two button alerts when targeting iOS 7. 14649998
- After importing images from a project into a image catalog, storyboards and xib files have broken image references.

  - The image names in Interface Builder are listed as `image-name.png` and should be shortened to `image-name` to repair the broken reference. 14042186
- You cannot drag a Placeholder object from the library into the outline.

  - Drag the Placeholder object into the canvas background. 13731313

#### Autolayout: Runtime

- In some cases “Update Frames” will not resize top level views or windows.

  - Use the “Update All Frames” menu item. 13716892
- Sometimes when editing UITableViews in Auto Layout documents set to open in Xcode 4.6, you get an error message saying “Failed to automatically update constraints.”

  - Upgrade your document to the Xcode 5 format using the “Opens in” option in the File inspector. After performing the desired edits, you can downgrade back to the Xcode 4.6 format if necessary. 14680132

#### Performance Measurement and Analysis

- Scripts running under the Automation instrument sometime fail to detect applications running inside the iOS 6 simulator environment.

  - Relaunch the simulator application and run the script again. 14447965
- The Allocations instrument can only attach to processes on devices running iOS 7. Processes must be started by Instruments on iOS versions prior to iOS 7. 14065257
- When attaching to a process running on an iOS 7 device with the Allocations instrument, the process may crash and the recording in the Allocations instrument then stops immediately. When attaching to a process on an iOS 6 or earlier device with the Allocations instrument, the process continues to run but no data will be collected in Allocations.

  - Launch with Xcode and then attach with Instruments. Alternatively, transfer to Instruments by clicking “Profile in Instruments” in the debug memory gauge. 14828459

#### Debugging

- When ending the debug session of an app on an iOS 5 device, the error message, "lost connection" may be displayed.

  - Dismiss the error pop-up: It does not indicate any problem debugging your app or connecting to the device. 14871460
- Watchpoints set from the Xcode UI using the contextual menu on a variable in the variables view don’t work for some variables , for instance `'self'`. When this is the case, the watchpoint won’t be hit when you expect.

  - To work around this issue, use the console in Xcode to create a watchpoint at the lldb prompt with the command `'watchpoint set variable <variable-name>'`. 12658775

#### Debugging: OpenGL

- The OpenGL ES frame debugger does not display texture mip-levels for textures that are not texture-complete. 14852587
- Simultaneously launching an iOS app which uses OpenGL from Xcode on more than a single device may not work.

  - Launch on one device at a time. 14836639

#### Unit Testing

- XCTest does not support iOS 6 destinations. Xcode does not prevent you from using XCTest with iOS 6 destinations, resulting in undefined behavior. 14075515

#### Source Control

- Xcode may have trouble connecting to repositories if credential information has changed after the repository was added in Accounts preferences. In certain cases, Xcode displays a failure when connecting to a repository while it is attempting to connect in the background.

  - If you encounter a repository connection problem, remove and re-add the repository with the updated credential information. This will restore access to the repository. 13955597
- Xcode 5 requires consistent usage of Subversion URLs: Either always include the (same) username or do not include one for a given repository. 14825641

#### iOS Simulator

- If an iOS app is detached, relaunching the same app from Xcode will result in a black screen in the Simulator even though the new app is launched.

  - Terminate the app in the Simulator or relaunch it for the second time. 14648784
- After switching the minimum deployment target of an application from iOS 7.0 to a release prior to iOS 7.0, building and running the application may fail with the message “iOS Simulator failed to install the application.”

  - Go to the iOS home screen, click and hold the application icon, then tap the hovering “X” button to delete the application. 13917023
- StoreKit (In-App purchases) will not work in the Simulator. 13962338
- When playing video via the Quicklook framework on an iPhone simulator, the video view appears black, but audio continues to play fine. 13871109
- The Mac hardware keyboard may not work for iOS Simulator on first launch.

  - Relaunch the simulator. 13315258

#### Account Management

- Xcode sometimes crashes if you request to create distribution signing assets during distribution of a Mac app.

  - Create the distribution signing assets using the Member Center. 13956010
- Xcode sometimes does not install the corresponding certificate in the Keychain after requesting a signing identity from the Member Center.

  Workaround:

  1. View the Accounts section of Xcode’s preferences.
  2. Select the account/team that corresponds to the signing identity.
  3. Click “View Details.”
  4. Click the Refresh button at the lower-left of the details sheet. 14197131

### Changes

#### General

- The provisioning profiles list in the Organizer is now located in the Accounts tab of Xcode's preferences. To view them, select the relevant Apple ID account and click View Details. 13950944
- 64-bit compatible applications are only supported with a minimum deployment target of iOS 6 or later. 14730546
- Xcode 5 does not support using the LLVM-GCC compiler or the GDB debugger. 14857582

#### Unit Testing

- The CPlusTest unit testing framework has been removed from Xcode 5. To write unit tests for C++ code, use the new XCTest framework and create Objective-C++ (.mm) test case subclasses. 8273037
- SenTestingKit and OCUnit are deprecated. Use the migrator to move to XCTest. 14857574

#### Source Control

- The CVS and RCS source control tools have been removed from Xcode 5. 11968433

### Notes

#### Doc Sets

- Xcode 5 does not support downloading additional doc sets.

  Additional doc sets can be added manually by installing them at `~/Library/Developer/Shared/ Documentation/DocSets/`

  Once installed, doc sets are found and loaded by Xcode 5. If Xcode is running while the doc set is installed, quit and relaunch Xcode. 14930443

#### Garbage Collection Support

- Xcode 5 ending support for OS X garbage collection.

  Garbage collection is a deprecated technology in OS X Mountain Lion and later. Xcode 5 is scheduled to be the last release of the Xcode developer tools to support building, debugging, or profiling Mac apps that use garbage collection. It is recommended that any projects using GC employ the Xcode migration tool to convert to ARC (Automatic Reference Counting.) More information about transitioning to ARC is available at: _[Transitioning to ARC Release Notes](../../../releasenotes/Objective%20C/Transitioning%20to%20ARC%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrw)_. 14406894

#### Continuous Integration Support

- Continuous integration features (bots) require OS X Server for OS X Mavericks. Mac Developer Program members can download the latest developer preview of OS X Mavericks from the Mac Dev Center. 14949282

[Next](Xcode%204%20Release%20Notes.md)[Previous](Xcode%206%20Release%20Notes.md)

