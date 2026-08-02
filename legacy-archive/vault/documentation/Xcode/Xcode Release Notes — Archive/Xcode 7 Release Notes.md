---
title: Xcode Release Notes — Archive
apple_id: TP40016994
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/xc7_release_notes.html
archived_at: '2026-07-26T19:54:16.360814Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Release Notes — Archive](Xcode%20Release%20Notes%20%E2%80%94%20Archive.md)


[Next](Xcode%206%20Release%20Notes.md)[Previous](Xcode%20Release%20Notes%20%E2%80%94%20Archive.md)

# Xcode 7 Release Notes

## Xcode 7.3.1 Release Notes

### Compatibility

- Xcode 7.3.1 requires a Mac running OS X 10.11 or later.
- Xcode 7.3.1 includes SDKs for iOS 9.3, watchOS 2.2, OS X version 10.11.4, and tvOS 9.2.

### Resolved Issues

#### Provisioning

- Fixed the issue where disabling a capability in the Xcode editor would leave the associated entitlement still enabled in the app. You may need to re-download provisioning profiles with the updated capabilities list after disabling a capability.

  Xcode no longer copies most entitlements from the provisioning profile into the app's code signature at build time. Entitlements for Wallet, GameCenter (for OS X), Data Protection, and Push notifications are still copied from the profile. All other entitlements should be declared using the Capabilities tab in the Xcode project editor. (24771364)

  __Note:__ If your app configuration is not yet compatible with the corrected entitlements behavior you can temporarily disable the new behavior using:

  `defaults write com.apple.dt.Xcode WantsExtraKeysFor25642247 -bool NO`

#### Code Completion

- Code completion shows the full title in the code completion pop-over. (25530060)

#### Interface Builder

- Fixed performance issue when opening storyboards or xib files with a large number of constraints. (25314053)

#### Localization

- Fixed an issue that caused Xcode to crash after importing a localization. (25395822)

#### Build System

- The Enable Clang Module Debugging build setting has been removed in this release, which may cause slower build times and larger debug information. This feature is intended to reduce the size of debug information. Temporarily removing this setting reduces Xcode crashes and problems with incomplete information in the variables view. (25535528)

  __Note:__ The Enable Clang Module Debugging setting had been enabled by default. If you had previously disabled it, it now appears as a user-defined build setting named `CLANG_ENABLE_MODULE_DEBUGGING`, which can be removed.
- Fixed a bug where a Swift command-line tool target in which `-ObjC` is passed to the linker would fail to link when built. (25447991)

#### Debugger

- Fixed an issue related to `NSSegmentedControls` that caused the view debugger to come up blank. (25388091)
- A fix to the LLDB Python interpreter allows it to correctly perform I/O within Xcode, enabling the `script` command to work as expected. Printed output from Python scripts appears in the Xcode debug console. (25448007)

#### Source Control Management

- Git has been updated to version 2.7.4 in order to improve security. (25181743)

#### Archives Organizer

- Clicking Download dSYMs in the Archives Organizer correctly downloads the dSYMs for application versions uploaded with bitcode. (25430147)

#### Swift

- Swift expressions evaluated in closures with a `weak self` capture no longer crash Xcode when debugging. (25448537)

  __Note:__ Inside such closures, the value of `self` cannot be used in debugger expressions. Assigning `self` to another variable within the original closure source enables the value to be referenced in expressions.
- A Swift compiler leak when using `try?` has been fixed. For additional information, see [Swift Report: SR-919](https://bugs.swift.org/browse/SR-919). (25388323)
- The domain of an `@objc` enum declared in Swift as an `ErrorType` is now defined consistently in Swift and Objective-C. For additional information, see [Swift Report: SR-700](https://bugs.swift.org/browse/SR-700). (25418435)
- Fixed a class initialization crash that occurred when the first field of a class is a `struct` with no members or an `enum` with a single case. (25314388)

### Deprecations and Removals Notice

- OS X 10.11 is the last major release of OS X that supports the previously deprecated garbage collection runtime.

  Applications or features that depend upon garbage collection may not function properly or may fail to launch when the runtime is removed. Developers should use Automatic Reference Counting (ARC) or manual retain/release for memory management instead.

## Xcode 7.3 Release Notes

### Compatibility

- Xcode 7.3 requires a Mac running OS X 10.11 or later.
- Xcode 7.3 includes SDKs for iOS 9.3, watchOS 2.2, OS X version 10.11.4, and tvOS 9.2.

### New Features

#### Playgrounds

- Live views in iOS and OS X playgrounds support user interaction. (22418838)
- Playgrounds rich comments are enhanced to support inline video display. Video tags support declaring a video file to use, as well as options enabling you to supply alternate text, a customized poster frame, and specifications for width and height. For information about using inline video, see [Videos](../Markup%20Formatting%20Reference/InlineVideo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqojy) in the _[Markup Formatting Reference](../Markup%20Formatting%20Reference/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojx)_. (23114189)
- `XCPlaygroundPage.captureValue(_:withIdentifier:)` has been deprecated. (24293262)

#### Editor

- Code completion enhancements in the Xcode source editor help you enter symbols, methods, and property names with less typing. Code completion now provides more intelligent suggestions by using partial matches and the first letter of each word, in addition to prefix matching.

#### Static Analyzer

- The static analyzer checks for missing localizability. This check is off by default and can be enabled by selecting `Yes` for “Missing localizability” in the “Static Analyzer – Generic Issues” build settings. (23414217)
- The static analyzer checks for misuses of nonnull type qualifiers. This check is set to `On` by default for new Xcode projects and is set to `Off` by default for existing Xcode projects. It can be enabled by selecting `Yes` for “Misuse of ‘nonnull’” in the “Static Analyzer - General Issues” section of the target build settings. (19003620) _- updated_
- The static analyzer checks for common misuses of Objective-C generics. (21412472)

#### Alternative Toolchain Support

Xcode supports using alternative toolchains, such as toolchains downloaded from [Swift.org](https://swift.org). When using an alternative toolchain, Xcode indexes, builds, and debugs with the alternative toolchain's tools instead of the default tools. Alternative toolchains must be manually downloaded and installed into `/Library/Developer/Toolchains/` or `~/Library/Developer/Toolchains/` to be recognized by Xcode.

New toolchain features in Xcode include:

- The Components pane in Xcode preferences displays installed toolchains in addition to simulators and documentation.
- To activate an installed toolchain, or reactivate the default toolchain, select the desired toolchain in the Toolchains pane of Components preferences. You can also choose a toolchain from the Xcode > Toolchains menu.

  __Note:__ The Xcode > Toolchains menu, and the Toolchains pane are only available in Xcode after you have installed alternative toolchains.

  Xcode must be relaunched after switching toolchains.
- An activated toolchain remains active across Xcode launches for all of your projects until you switch toolchains again.
- Xcode displays an active toolchain indicator in the workspace window activity view when an alternative toolchain is active. Clicking this indicator opens the Toolchains pane in Components preferences.
- Control-click on an installed toolchain in the Toolchains pane of Components preferences to verify its signature, reveal it in the Finder, or move it to the Trash.
- Xcode Server bots can be configured to use toolchains installed in `/Library/Developer/Toolchains/`.

Restrictions that apply when using downloaded toolchains:

- The Swift code migrator only works when using the default toolchain.
- Playgrounds only work when using the default toolchain.
- Only apps built with the default toolchain may be submitted to the App Store.
- Activating an alternative toolchain affects the Xcode IDE only.

  To use an alternative toolchain with command-line tools, use `xcrun --toolchain swift` and `xcodebuild TOOLCHAINS=swift`. You can provide either the abbreviated or the full identifier for the toolchain, for example, `xcrun --toolchain swift` or `xcrun --toolchain org.swift.20151231a`.
- Instruments may be unable to demangle certain Swift symbols or track memory usage using the Allocations instrument if the active toolchain includes changes to Swift’s mangling scheme or memory allocation runtime.

(23910267)

#### Linker

- The Apple private frameworks have been removed from the iOS, watchOS, and tvOS SDKs. If your application fails to link, make sure that you are not using any private frameworks. The use of private frameworks is an unsupported configuration and applications that use non-public APIs will be rejected by the App Store - see [App Store Guideline 2.5](https://developer.apple.com/app-store/review/guidelines/#functionality). (22330301)

#### Simulator

- Simulator.app supports delivering touch pressure to iOS and watchOS by using a Force Touch trackpad.

  Legacy support for setting force touch pressure in the watchOS simulator (for example, Shift-Command-2) is deprecated and will be removed in a future release. (24853602)

#### Debugger

- Constraint badges in the view debugger present values as ratios for better readability when applicable. (22535224)
- The view debugger inspector shows referenced views, attributes, and values for a selected constraint. (22266966)
- The view debugger shows `NSWindow` size information in the inspector. (18284986)
- The view debugger has additional options for the assistant editor. The implementation file of data sources, delegates, and the target of controls can be viewed side by side with the 3D canvas of app views. (15777861)
- Improved 3D rotation behavior in the view debugger. (18313502)
- When inspecting a view in the debugger, objects with properties whose values represent classes such as Target, Delegate, and Data Source show a navigational arrow in the inspector. Click the arrow to open the implementation file of that class. Pressing the Option key while clicking performs the requested navigation in the assistant editor, instead of replacing the contents of the view debugger canvas. (15884626)
- GPU frame debugger supports shader profiling for OpenGL ES apps using secondary contexts for resource loading. (19538945)
- Address sanitizer no longer checks for C++ container overflows by default.

  To perform this check requires the entire application to be built with Address Sanitizer otherwise it may report false positives. To turn this check on, set “Enable C++ Container Overflow Checks for Address Sanitizer” in your target’s build settings to `Yes`. (24515599)
- Stepping performance has been improved when connected to devices over slower communication channels. This improvement is most noticeable when debugging code running on an Apple Watch. (22509498)
- When using LLDB, Objective-C expression evaluation implicitly imports all modules that were imported in the source context where execution takes place in order to provide a much higher fidelity debugging experience.

  In most cases, this change eliminates the need to manually import modules while debugging. For example, using `expr — @import UIKit`—commonly used to ensure that SDK declarations were available—is no longer necessary.  (11609847)

#### Debug Navigator

- Filtering in the navigator has been enhanced, allowing it to disclose the child items of matches. (8094288)
- A contextual menu for items selected in the Views mode of the debug navigator and the canvas allows you four new options:

  - Print the description of an object.
  - Focus on a view’s subtree.
  - View constraints on an object.
  - Hide views obscuring or obscured by the selected view.

  (20455506)
- The Views mode of the debug navigator allows you to filter for the address, label, title, and superclass of a view. (23095363)

#### Build System

- WatchOS schemes show new icons when the scheme is configured to run a glance, notification, or complication, making it easier to see at a glance which scheme you have selected. (24694468)

#### General

- Enterprise developers can create Developer ID certificates using the Accounts preference pane in Xcode. (22550089)

#### Swift

- You can guard statements and declarations with a new `#if swift(>=x.y)` build configuration: if the Swift language version is at least “`x.y`”, code in the active branch will compile. Code in the inactive branches won’t be parsed or emit syntax diagnostics, so you can mix source code for different versions of Swift in the same file.

  Example:

  ```
  #if swift(>=2.2)
    print(“Hello!”)
  #elseif swift(1.0)
    println(“Hello!”)
  #else
    This code will not parse or emit diagnostics
  #endif
  ```

  For more information, see [Swift Evolution proposal SE-0020](https://github.com/apple/swift-evolution/blob/master/proposals/0020-if-swift-version.md). (19823607)
- All slice types have `removeFirst()` and `removeLast()` methods. Additionally, `ArraySlice.removeFirst()` preserves element indices. (22536664)
- Anonymous structs from C are imported as nested struct types in Swift. (21683348)
- Three new doc comment fields allow Swift users to cooperate with code completion engine to deliver more effective code completion results:

  - `- keyword:` specifies concepts that are not fully manifested in declaration names.
  - `- recommended:` indicates other declarations are preferred to the one decorated.
  - `- recommendedover:` indicates the decorated declaration is preferred to those declarations whose names are specified.

  (23101030)
- Inside a class, a designated initializer that is either failable (`init?()`) or throwing (`init() throws`) is allowed to exit before initializing all stored properties and calling `super.init()`. This behavior makes designated initializers more consistent with convenience initializers. Convenience initializers can also fail before performing a `self.init()` delegation.  (18216578)
- Curried function syntax has been deprecated, and is slated to be removed in Swift 3. (23364870)
- The `++` and `--` operators have been deprecated and are slated to be removed in Swift 3.0.  As a replacement, use `x += 1` on integer or floating point types and `x = x.successor()` on Index types. (23708702)
- Associated types in protocols can be specified with a new `associatedtype` declaration, to replace the use of `typealias`:

  ```
  protocol P {
    associatedtype Ty
  }
  ```

  The `typealias` keyword is still allowed in Swift 2.2, although it is deprecated and produces a warning. This warning will become an error in Swift 3.

  For more information, see [Swift Evolution proposal SE-0011](https://github.com/apple/swift-evolution/blob/master/proposals/0011-replace-typealias-associated.md). (24159196)
- When referencing a function or initializer, one can provide the complete name, including argument labels. For example:

  ```
  let fn1 = someView.insertSubview(_:at:)
  let fn2 = someView.insertSubview(_:aboveSubview:)
  let buttonFactory = UIButton.init(type:)
  ```

  For more information, see [Swift Evolution proposal SE-0021](https://github.com/apple/swift-evolution/blob/master/proposals/0021-generalized-naming.md). (24270055)
- New `#file`, `#line`, `#column`, and `#function` expressions replace the existing `__FILE__`, `__LINE__`, `__COLUMN__`, and `__FUNCTION__` symbols. The `__FILE__`-style symbols have been deprecated, and will be removed in Swift 3.

  For more information, see [Swift Evolution proposal SE-0028](https://github.com/apple/swift-evolution/blob/master/proposals/0028-modernizing-debug-identifiers.md). (24637902)
- Global `anyGenerator()` functions have been changed into initializers on `AnyGenerator`, in order to help make the API more intuitive and idiomatic. The `anyGenerator()` functions have been deprecated in Swift 2.2 and will be removed in Swift 3. (22883059)
- The `@objc(SomeName)` attribute is supported on enums and enum cases to rename the generated Objective-C declaration. (21930334)
- The Objective-C selector of a Swift method can be determined directly with the `#selector` expression, for example:

  `let sel = #selector(insertSubview(_:aboveSubview:)) // sel has type Selector`

  Along with this change, the use of string literals as selectors has been deprecated, for example:

  `let sel: Selector = "insertSubview:aboveSubview:"`

  Generally, such string literals should be replaced with uses of `#selector`, and the compiler provides fix-its that use `#selector`. In cases where this is not possible (for instance, when referring to the getter of a property), one can still directly construct selectors. For example:

  `let sel = Selector("propertyName")`

  __Note:__ The compiler is checking the string literals used to construct Selectors to ensure that they are well-formed Objective-C selectors and that there is an `@objc` method with that selector.

  For more information, see [Swift Evolution proposal SE-0022](https://github.com/apple/swift-evolution/blob/master/proposals/0022-objc-selectors.md). (19954874)

### Resolved Issues

#### Swift

- Swift 2.1 had an issue where targets with large numbers of files would fail to compile under whole-module optimization. This has been resolved. (23878192)

#### Interface Builder

- Creating connections via control-drag between multiple displays has been fixed. (14345464)
- `UITableViewCell` objects that extend below the bounds of a `UITableView` draw correctly when scrolled. (23242098)
- Fixed the iOS storyboard compilation failures caused by the top and bottom layout guides that were added to the top level of a scene. These layout guides are now removed when opening a document with Interface Builder. (23348852)

#### Code Signing

- Fixed an issue with running an app signed by a free provisioning team. (19748857)

#### Build System

- Product references in the Xcode structure navigator respect the active run destination. For example, if a simulator run destination is selected, then the resolved path for the application product reference becomes the simulator binary path. (9178537)
- Resolved: Using `xcodebuild build -scheme -sdk` with a Simulator SDK builds and does not display an “Unsupported architecture” error. (22993940)

#### Debugger

- The Swift debugger no longer crashes when stopping in code that depends on a Swift library or framework that has been distributed in binary form. (22492040)
- The option to suppress view debugging has been removed from the Options pane in the Run scheme. Developers can still debug views using the "Debug View Hierarchy" button in the debug bar. (22636367)
- The view debugger inspector now correctly shows all attribute values for Swift projects. (22472665)

#### General

- In FileMerge, resolved an issue that made it hard to see the modified character background color. (24076916)

### Known Issues

#### Swift

- If a type `Inner` is declared within another type `Outer`, and then `Inner` is referred to from another file in the same module, the Swift compiler may crash during the Merging Swift Module build step.

  Compile using Whole Module Optimization or avoid nesting types. (22858834)

#### Playgrounds

- The hit target of the first link included in a playground markup comment is limited to the very start of the linked text; the hit target may be as small as a single character.

  Subsequent links in the markup comment are not affected. (24920637)
- The first line of a single-line style Swift documentation comment (a code line prefixed with “`///`”) is ignored by Quick Help if the declaration is directly preceded by a multiline-style documentation comment that is not associated with a symbol.

  For example:

  ```swift
  /**
  An unattached comment
  */

  /// First line
  /// Second line

  func test() { }
  ```

  In this example, only `Second line` appears as part of the abstract for `test()`. (25134233)
- Block quotes in playground markup comments, delimited by prefixing a line with “`>`”, are implicitly rendered as “Note” callouts. (25011787)
- Code blocks in playground markup comments, delimited by prefixing each line with a minimum of four spaces, are implicitly rendered as “Example” callouts. (25012454)

#### Build System

- The build system does not have full support for using frameworks which define modules while using the `ALWAYS_SEARCH_USER_PATHS = YES` build setting. The build system warns about this situation, and recommends disabling `ALWAYS_SEARCH_USER_PATHS`.

  While `ALWAYS_SEARCH_USER_PATHS` defaults to `YES` if never defined, the default for new projects has been `NO` for several major releases, and the behavior of `ALWAYS_SEARCH_USER_PATHS = YES` is considered undesirable. Projects should attempt to migrate to using `ALWAYS_SEARCH_USER_PATHS = NO` exclusively where possible. (24248838)

#### Simulator

- When attempting to build and run from within Xcode, you may encounter an error message that states “`DTAssetProviderService` could not start `DTXConnection` with simulator.”

  Launch Simulator.app first and boot your target device before selecting build and run from within Xcode. (25311561) _- updated_
- Testing in the iOS 9.3, tvOS 9.2, or watchOS 2.2 simulator runtimes using `-[UIDevice identifierForVendor]` may return unreliable results. (25342936) _- updated_

#### Debugger

- The LLDB Python interpreter is not able to perform console I/O within Xcode. As a result, the `script` command hangs when it would normally prompt for input and printed output from Python scripts does not appear in the Xcode debug console. (24877720)
- Debugging can hang on launch if an `.lldbinit` file is present that tries to call `quit` in Python code during debugger initialization. (24360903)
- Simple Objective-C/C++/C expressions containing the right-shift (`>>`) operator can cause Xcode to crash when entered in the debugger console.

  Ensure that potentially problematic expressions contain at least one function call. For example, instead of entering `p $0 >> 3` use `p printf(“”); $0 >> 3`. (24988475)
- Debugging app extensions or watch apps in Simulator may cause Xcode to hang.

  Keep the simulator application(s) open during your development session. If the issue occurs, restart both Xcode and the simulator application(s). (25338888) _- updated_
- View debugging can fail when auto layout is not used due to an unhandled assertion in an underlying system framework. (25311044) _- updated_

#### General

- Xcode may present pre-iOS 9.0 iPhones as valid run destinations for a WatchKit 2 application when the project includes both WatchKit 1 and WatchKit 2 targets. If you select this run destination and launch, the WatchKit 1 app runs instead of the WatchKit 2 app.

  Ignore the destination for pre-iOS 9.0 iPhones. Use an iPhone with iOS 9.0 or greater to develop and test your WatchKit 2 application. (24900924)
- SpriteKit scenes may appear distorted on OS X if the `SKView` instance doesn’t have a layer as its backing store.

  Set `wantsLayer = true` on instances of `SKView` that have been created programmatically. (25554503) _- updated_

### Deprecations and Removals Notice

- OS X 10.11 is the last major release of OS X that supports the previously deprecated garbage collection runtime.

  Applications or features that depend upon garbage collection may not function properly or may fail to launch when the runtime is removed. Developers should use Automatic Reference Counting (ARC) or manual retain/release for memory management instead.
- Apple private frameworks have been removed from the iOS, watchOS, and tvOS SDKs.

  If your app fails to link, make sure that you are not using any private frameworks. The use of private frameworks is an unsupported configuration and apps that use non-public APIs will be rejected by the App Store. For details, see [App Store Guideline 2.5](https://developer.apple.com/app-store/review/guidelines/#functionality).

## Xcode 7.2.1 Release Notes

### Resolved Issues

#### Interface Builder

- Fixed the crash occurring when documents have location-based Auto Layout constraints with a `nil` second item. (24173653)
- `UITableViewCell` objects that extend below the bounds of a `UITableView` draw correctly when scrolled. (24173743)

#### Testing

- Fixed the problem where `xcodebuild test` timed out while waiting for iOS Simulator to boot. (24173400)

#### Debugging

- Eliminated the debugger crash that occurred when pausing code dependent on Swift libraries from a binary distribution. (24173332)

#### General

- A renewed intermediate certificate issued by Apple Worldwide Developer Relations replaces the expiring certificate in your development system.

  The intermediate certificate is required for developers that provide passes for Apple Wallet, deliver Safari Push Notifications, or create Safari Extensions. For more information about the intermediate certificate, visit [developer.apple.com: Intermediate Certificate Expiration](https://developer.apple.com/support/certificates/expiration/). (23922671)

## Xcode 7.2 Release Notes

### New Features

#### Linker

- The linker now supports order file (`-order_file option`) when bitcode is enabled (`ENABLE_BITCODE=YES`). (21392558)
- The linker now supports unexported symbols (`-unexported_symbol[s_list]` option) when bitcode is enabled (`ENABLE_BITCODE=YES`). (21677850)

#### Swift

- The Swift compiler is now stricter about including non-modular header files. Debugging a Swift target requires that frameworks be properly modular, meaning all of the publicly-imported headers are either accounted for in the framework's umbrella header, imported from another modular framework, or listed explicitly in a custom module.modulemap file (advanced users only).

  The compiler will run into issues if the same header file is accessible both through Header Search Paths (`-I`, `-isystem`) and Framework Search Paths (`-F`, `-iframework`), even if there are symbolic links involved. In these cases, you should prefer using Framework Search Paths alone. (23341162)

  __Note:__ This invalid configuration may be generated by external systems, such as CocoaPods.

#### General

- A protocol method implementation no longer inherits the protocol method’s availability information. This may result in new warnings or errors. Since the compiler suppresses availability diagnostics in code that is itself unavailable, you may see new diagnostics in method implementations that have stopped inheriting the availability from a protocol. (22734745)

### Resolved Issues

#### Asset Catalogs

- Fixed issues with universal assets when building asset catalogs for watchOS 2.0. (22867369)

#### Crash Logs

- Crash logs for app extensions are available in builds distributed via TestFlight. (22661518)

#### Linker

- Fixed the linker assertion when linking against an object file that linked with `ld -r` (single object prelink) and `-exported_symbol[s_list]` options in bitcode mode. It is recommended to regenerate static libraries that have been compiled with such options and are currently getting an assertion. (22897234)

#### Simulator

- Resolved issues when using Apple Pay in the simulator and requesting a user's billing address. (22551685)
- Fixed issues with Simulator becoming unresponsive when unpairing a Siri Remote or Game Controller. (22891830)

#### Storyboards

- Storyboards now support reusing the same view controller as the destination of multiple relationship segues. For example, a tab bar controller and a navigation controller may now share the same child view controller. (19060323, 20829042)
- Storyboards and nibs containing UITextViews with 1-11 characters no longer hang when loaded on iOS. (22228164)

#### Swift

- In previous releases of Swift, if a type had a mutable property of protocol type, _chained_ accesses to properties of that property were always treated as mutations of the property, even if the second property was only read, not written. For example:

  ```swift
  protocol Countable {
      var count: Int { get }
  }
  class MyObject {
      var widgets : Countable {
          didSet { print("in didSet") }
      }
  }

  var obj : MyObject = ...
  let count = obj.widgets.count
  ```

  The example above would perform a spurious write back to the property `widgets`, causing `didSet` to unexpectedly fire. The workaround was to split the access into separate expressions. For example:

  ```
  let widgets = obj.widgets
  let count = widgets.count
  ```

  This bug has now been fixed. (22953072)
- Swift data types that are imported into Swift from C struct types (such as `CGRect` and `CGPoint`) can now be inspected in the debugger. (23088739)
- A bug that caused some Swift projects to crash in whole module optimization with a "program too clever" LLVM error has been fixed. (23200656)
- A bug has been fixed where Swift code calling an Objective-C method that took a block returning a `nonnull NSString *` with a Swift closure would be miscompiled, causing the compiled program to crash. (23285766)

#### General

- Resolved an issue where the Finder would mistakenly display a warning indicating that Xcode is damaged and should be moved to the trash. (22686310)
- Resolved problems attaching to processes when the Run pane of the Scheme Editor is configured to “Wait for executable to be launched.” (22753642)
- Fixed issues related to enabling Game Center and In-App Purchase in the Capabilities pane. (22964531)
- Wrapping text fields lay out correctly in the running application after building OS X projects. (23052169)
- A bug in the optimizer has been fixed that caused in-place sort on mutable collections to crash. (23081349)
- Resolved issues related to Build and Run on devices running iOS 9.1. (23224972)
- A bug that caused a program to crash when providing a parameter with a `@convention(block)` type (including `dispatch_block_t`) that was marked `@noescape` has been fixed. (23261912)

### Known Issues

#### Asset Catalog

- Layered image file names may not be longer than 255 characters. (22974625)
- `UIKit` will not render image stack layers correctly when a layer contains a resized image whose aspect ratio doesn’t match the aspect ratio of the original image.

  When resizing an image in a layer stack, choose a width and height that matches the original aspect ratio of the image. (23061910)

#### Debugger

- The Swift debugger can crash when stopping in code that depends on a Swift library or framework that has been distributed in binary form.

  Frameworks written in Swift should be compiled from source as part of the same project that depends on them to guarantee a single, consistent compilation environment. (22492040)
- Detaching the debugger from an Apple TV app will cause the app to hang when it logs output. (22493459)
- Xcode’s debugger may not automatically attach to a Today extension run on an iPad Pro when the Notification tab is selected.

  Select the Today tab instead of the Notification tab. The Today extension will now launch and may be debugged. (22495840)

#### Simulator

- Full support for the tvOS simulator runtime requires OS X 10.11 El Capitan or later. The runtime is supported on OS X Yosemite 10.10.5, but with limited capabilities. Developers running on Yosemite will be unable to pair the Apple TV Remote with the tvOS simulator runtime. (19070665
- When running in an iOS simulator for iOS versions 9.1 and earlier, an app may not communicate with TCP/IP services hosted locally by the Mac using the Mac’s local IP address.

  Connect via a loopback address, such as localhost or `127.0.0.1`. (22453539)
- A simulated iOS 9.0 device may boot to a black screen if Xcode is in a different location than when the device first booted.

  Choose Simulator > Reset Content and Settings. (22697818)
- To use a Siri Remote with the tvOS simulator, you may first need to unpair it from the Apple TV. To unpair a Siri Remote from an Apple TV, position the remote several meters away from the Apple TV and press and hold Menu and Volume Up (+) simultaneously for 2 seconds. If the Siri Remote immediately pairs with the Apple TV again, move further away and repeat this process. (22908351)
- When you download an iOS simulator from the Downloads preference pane in Xcode, you may be prompted to authenticate as an admin at the beginning of the first download and at the end of each additional download.

  All of these authentications are required to successfully install the selected iOS simulator. (22993731)
- When duplicating a simulator in the Devices window, the simulator may be listed with an identifier instead of a version number in simulator Run destinations. (23094167)
- Installing the iOS 9.0 Simulator Runtime from Xcode's Download Preferences can cause Interface Builder in Xcode 6 installs on the same machine to stop functioning.

  Either avoid installing the iOS 9.0 Simulator Runtime or move `/Library/Developer/CoreSimulator/Profiles/Runtimes/iOS\ 9.0.simruntime` to a backup location when switching to Xcode 6 and move it back for Xcode 7. (23230951)
- iPhone + Watch simulators for WatchKit 2.0 might not be visible in Xcode.

  Create an iPhone + Watch pair manually:

  1. Choose Window > Devices to open the Devices window.
  2. Click the Add (+) button in the lower left corner of the Devices window.
  3. Choose an iPhone device type, an iOS version, and a paired Apple Watch.
  4. Click the Create button.

  (23319184)
- Building and running may intermittently fail in the tvOS Simulator, producing the error “Failed to lookup process ID.”

  Try running your app again, or run the app on an Apple TV device. (23486651)

#### Testing

- When recording UI tests for tvOS, presses on the menu button may generate duplicate code in the UI test. (22850293)
- UI tests fail to launch in the tvOS simulator if run with Unit Tests.

  Run your UI tests with their own scheme, separately from your unit tests. (23079718)

#### General

- Running an app signed with a free provisioning team may fail to launch.

  Trust the developer certificate under Settings > General > Profiles & Device Management on the device. (19748857)
- The Devices window sometimes displays paired Apple Watch details alongside an incorrect companion device. (22908731)
- Watch Framework and Static Library targets do not display a General tab.

  Configure general settings manually in the target's Info.plist file or in the Build Settings tab. (22932248)

## Xcode 7.1.1 Release Notes

### Resolved Issues

The following issues have been resolved.

#### General

- Resolved a crash when moving or renaming Xcode, and then opening an iOS or Apple TV app in Xcode. (23264753)

#### Interface

- Wrapping text fields lay out correctly in the running application after building OS X projects. (23154165)

#### Storyboards

- Storyboards and nibs containing `UITextView` elements with between 1 and 11 characters no longer hang when loaded on iOS. (23264732)
- Fixed a bug that caused iOS xibs/storyboards compiled with `ibtool --flatten NO` to produce output that could not be read by `ibtool --strip`. (23283113)

#### Swift

- Swift data types that are imported into Swift from C struct types (such as `CGRect` and `CGPoint`) can now be inspected in the debugger. (23148897)

#### Testing

- `xcodebuild` no longer hangs when running UI tests on Apple TV. (23264788)

### Known Issues

#### General

- There’s a bug in the optimizer that causes _in place sort_ on mutable collections to crash. For example:

  ```
  // Crashing version.
  aContainer.sortInPlace { (a: Element, b: Element) -> Bool in
  ```

  Use the non-destructive version of sort and assign its result back to the original container. For example:

  ```
  aContainer = aContainer.sort { (a: Element, b: Element) -> Bool in
     ...
  }
  ```

  (23081349)

## Xcode 7.1 Release Notes

### New Features

#### Playgrounds

- Playgrounds support dragging files, images, and colors directly into the editor to create object literals.

  Object literals allow you to include visual representations of files, images, and colors within a playground, enabling a more expressive playground document. Literals behave similarly to their plain code counterparts but are rendered specially in the Xcode editor. (22099316)
- The API exposed by `XCPlayground` has been revised significantly. Instead of a collection of global functions, Xcode now exposes an `XCPlaygroundPage` class with methods for interacting with Xcode and the current playground page.

  `XCPlaygroundPage` exposes the following functionality:

  - Use `XCPlaygroundPage.currentPage` to obtain a reference to the current page.
  - Use `XCPlaygroundPage.captureValue(_:withIdentifier:)` to capture values into timeline items.
  - Set `XCPlaygroundPage.needsIndefiniteExecution` to indicate to Xcode that the playground page contains asynchronous code intended to execute indefinitely.
  - Set `XCPlaygroundPage.liveView` to tell Xcode to present a live view for the playground page

  `XCPlaygroundSharedDataDirectoryURL` has been defined as a new global constant; it exposes the shared playground data directory as an `NSURL`.

  As part of this API change, `XCPCaptureValue`, `XCPShowView`, `XCPSetExecutionShouldContinueIndefinitely`, `XCPExecutionShouldContinueIndefinitely`, and `XCPSharedDataDirectoryPath` have been deprecated; they may be removed in a future version of Xcode. (20783204)
- `XCPlayground` supports presenting view controllers as the live view for a playground page.

  To use this feature, set `XCPlaygroundPage.liveView` to your view controller of choice. When available, view controllers should be preferred but plain views may still be used as the live view for a playground page.

  Playground authors may also make custom types that can be presented as the live view for a playground page by conforming to the `XCPlaygroundLiveViewable` protocol, which allows an object or a value to return a view or view controller that should be used as its live view representation. (20783161)
- Playgrounds can programmatically stop execution by calling `XCPlaygroundPage.currentPage.finishExecution()`.

  This method instructs Xcode to stop executing the current playground page; it allows Xcode to clean up for exiting properly in ways that exiting directly does not. (22463694)

#### Interface Builder

- Dashed constraints can indicate a priority lower than 1000. (15990914)
- Interface Builder supports enabling Peek & Pop for segues.

  Peek & Pop segues are omitted when running on OS versions prior to iOS 9.1. (22886994)

#### Testing

- UI testing is available for tvOS applications.

  To support the unique interaction model provided by tvOS, XCTest includes a new `XCUIRemote` class that allows interaction with an application as if an Apple Remote were used. In addition, a new `XCUIElement.hasFocus` property can be used to check an element’s focus state, and this `hasFocus` property can also be used in `XCUIElementQuery` predicates on tvOS to find the element with focus.

  While recording a UI test on tvOS, swipe gestures on a Siri Remote are recorded as if equivalent buttons are being pressed on an Apple Remote.

  Navigation using the keyboard in the simulator is recorded as if equivalent buttons are pressed on an Apple Remote: The arrow keys are mapped to the arrow buttons, the Return key is mapped to the Select button, the Escape key is mapped to the Menu button, and the space bar is mapped to the Play/Pause button. (21548564)

#### Debugging

- Address Sanitizer supports watchOS apps. (22540994)
- Swift error breakpoints are supported.

  A Swift error breakpoint pauses execution when the error is thrown. You can edit Swift error breakpoint so that execution is paused only for a specified Swift error type. (21080569)

#### Crash Reports

- Xcode can display crash reports in the Crashes Organizer that originate from WatchKit 2 extensions. (20139117)
- Crash logs for OS X app extensions are displayed in the Crashes Organizer. (22224732)

#### Swift

- Enums imported from C now automatically conform to the `Equatable` protocol, including a default implementation of the `==` operator.

  This conformance allows you to use C enum pattern matching in `switch` statements with no additional code. (17287720)
- The `NSNumber``unsignedIntegerValue` property now has the type `UInt` instead of `Int`, as do other methods and properties that use the `NSUInteger` type in Objective-C and whose names contain `"unsigned.."`.

  Most other uses of `NSUInteger` in system frameworks are imported as `Int` as they were in Xcode 7. (19134055)
- Field getters and setters are now created for named unions imported from C. In addition, an initializer with a named parameter for the field is provided.

  For example, given the following Objective-C `typdef`:

  ```c
  typedef union IntOrFloat {
    int intField;
    float floatField;
  } IntOrFloat;
  ```

  Importing this `typedef` into Swift generates the following interface:

  ```swift
  struct IntOrFloat {
      var intField: Int { get set }
      init(intField: Int)

      var floatField: Float { get set }
      init(floatField: Float)
  }
  ```

  (19660119)
- Bitfield members of C structs are now imported into Swift. (21702107)
- The type `dispatch_block_t` now refers to the type `@convention(block) () -> Void`, as it did in Swift 1.2.

  This change allows programs using `dispatch_block_create` to work as expected, solving an issue that surfaced in Xcode 7.0 with Swift 2.0.

  __Note:__ Converting to a Swift closure value and back is not guaranteed to preserve the identity of a `dispatch_block_t`.

  (22432170)
- Editing a file does not trigger a recompile of files that depend upon it if the edits only modify declarations marked `private`. (22239821)
- Expressions interpolated in strings may now contain string literals.

  For example, `"My name is \(attributes["name"]!)"` is now a valid expression. (14050788)
- Error messages produced when the type checker cannot solve its constraint system continue to improve in many cases.

  For example, errors in the body of generic closures (for instance, the argument closure to `map`) are much more usefully diagnosed. (18835890)
- Conversions between function types are supported, exhibiting covariance in function result types and contravariance in function parameter types.

  For example, it is legal to assign a function of type `Any -> Int` to a variable of type `String -> Any`. (19517003)

### Resolved Issues

The following issues listed in previous Xcode release notes have been resolved.

#### Interface Builder

- Fixed: Editor > Canvas > “Show Intrinsic Size Constraints Contributing To Ambiguity” works correctly when there is ambiguity in content priority for the selected views using Auto Layout in the Interface Builder canvas. (19689060)
- Constraints show badges to indicate their relationship and ratios. (15991257)
- Explicit layout margins set on `UIStackView` in Interface Builder are properly reflected at runtime. (21613035)

#### Building

- Fixed: If your iOS app embedded a watchOS app and you had a framework for both iOS and watchOS embedded in each app, your project would fail to build when you performed the Archive action. (22183332)

#### Debugging

- The visibility of selected constraints when debugging the view hierarchy is improved. (22092490)

#### General

- Launching Xcode or another tool that uses Simulator no longer causes additional Apple Watch devices to be created. (22508374)

#### Swift

- Using `switch` against multiple types with `as` patterns no longer causes a memory leak. (22587077)

### Known Issues

#### Asset Catalog

- When building asset catalogs for watchOS 2.0, some Universal assets may not appear in the compiled asset catalog.

  Make sure your Universal assets for watchOS 2.0 include a “2x” or “Any” scale representation. (22867369)

#### Linker

- When using bitcode and `ld -r` (Xcode single object prelink) together with `-exported_symbol` or `-exported_symbols_list`, single object prelink succeeds but the linker then asserts when linking against the prelinked object.

  If you are building a static library using bitcode and single object prelink, do not add exported symbols flags to the link command. If you are currently seeing linker assertions when linking against a 3rd party library, you can disable bitcode or ask for a new library from the library provider. (22897234)

#### Simulator

- To use a Siri remote with the tvOS Simulator, you may need to first unpair it from the Apple TV.

  To unpair a Siri remote from an Apple TV, position the remote several meters away from the Apple TV, then press and hold MENU and + simultaneously for 2 seconds. If the Siri remote immediately re-pairs with the Apple TV, move further away and try again. (22908351)
- Simulator.app may become unresponsive when unpairing a Siri Remote or Game Controller.

  Force-quit Simulator.app and relaunch it. (22891830)
- When running in the Simulator, an app cannot communicate with TCP/IP services locally hosted by the Mac via the Mac’s local IP address.

  Connect via a loopback address, such as localhost or 127.0.0.1. (22453539)
- Simulated transactions using Apple Pay in Simulator do not complete if requesting a user's billing address. (22551685)
- For full support, the tvOS Simulator Runtime requires the final release of OS X v10.11 El Capitan or newer versions of OS X.

  The runtime is supported on OS X Yosemite 10.10.5 with limited capabilities. Running on OS X Yosemite is unable to pair the Apple TV Remote with the tvOS Simulator Runtime. (19070665)
- An iOS 9.0 simulator may boot to a black screen if Xcode.app is at a different path than when the device first booted.

  Reset the simulated device's contents and settings from the simulator menu. (22697818)
- When you download one or more Simulators from the Xcode Downloads preference panel, you are prompted for admin authorization at the beginning of the first download. You may also be prompted for admin authorization again at the end of each download. Responding to all of these prompts is required to successfully install the selected Simulators. (22993731)

#### Testing

- When recording UI tests for tvOS, presses on the menu button may generate duplicate code in the UI test method. (22850293)
- UI tests fail to launch in the Apple TV simulator if run with unit tests.

  Run your UI tests with their own scheme, separately from your unit tests. (23079718)

#### Debugging

- The Xcode debugger does not automatically attach to a Today extension run on an iPad Pro when the Notification tab is selected.

  Select the Today tab, then launch the Today extension for debugging. (22495840)
- Detaching the debugger from an Apple TV application causes the app to hang when it logs output. (22493459)
- Swift data types that are imported into Swift from C struct types, such as `CGRect` and `CGPoint`, can not be inspected in the debugger. (23088739)

#### Crash Reports

- Crash logs for app extensions are not available in builds distributed via TestFlight. (22661518)

#### Xcode Server

- Xcode Server may not be able to join new development teams with versions of OS X Server other than version 4.1.5.

  Existing team memberships will continue to work correctly. (22539804)

#### General

- When using “wait-for-launch” in the Run scheme action, Xcode shows “Running” instead of “Waiting to attach” in the Activity monitor even though it is waiting for the process to launch. If you don’t launch the process being waited for and switch to “launch automatically,” Xcode fails to attach to the app for each time this situation has occurred, after which it launches as expected. (22753642)
- The Devices window sometimes displays paired watch details alongside an incorrect companion device. (22908731)
- Watch Framework and Static Library targets do not have a General tab in the project editor.

  Configure settings manually via the target's `Info.plist` file or the Build Settings tab, as appropriate. (22932248)
- Running an app signed with a free provisioning team may fail to launch.

  Trust the developer certificate in the device Settings—Settings > General > Profiles & Device Management. (19748857)
- Apps signed with a free provisioning team may not run on a tvOS device. (22636412)
- The Finder may mistakenly give a warning that Xcode is damaged and should be moved to the trash.

  Reboot your Mac. If warnings persist after reboot, reinstall Xcode. (22686310)
- Certain capabilities, such as Game Center and In-App Purchase, cannot be enabled in the Capabilities pane of the Project Navigator.

  Enable and then disable the iCloud capability to restore the ability to enable the other capabilities. (22964531)
- After building an OS X project, some wrapping, multiline text fields may layout incorrectly in the running app.

  Open the storyboard or XIB containing the wrapping, multiline text field, select the text field, open the size inspector, and change Preferred Width to Explicit. (23052169)

## Xcode 7.0.1 Release Notes

### App Thinning

- The Xcode 7.0.1 release includes several improvements to improve support for adopting bitcode and to help catch issues with app thinning prior to App Store submission. (22783146, 22783168)

## Xcode 7.0 Release Notes

The Xcode 7 release incorporates new features in the IDE as well as updates to Swift and Objective-C.

### New Features

#### Playgrounds

- Playgrounds can now be set to run manually or automatically when changes are made, as well as stopped during execution. (18058289)
- Xcode 7 adds pages to playgrounds. You can add a new page to any playground by selecting File > New Playground Page. In the navigator and jump bar, you’ll see all pages in the playground. You can add navigation between pages with the new page navigation markup:

  - Navigation relative to the all pages in the playground:

    - [Go to First Page](@first)
    - [Go to Last Page](@last)
  - Navigation relative to the current page:

    - [Go to Next Page](@next)
    - [Go to Previous Page](@previous)
  - Navigation to a specific page:

    - [Go to Overview](Overview)
    - [Go to Sorting](Sorting)

  (20192277)

#### Interface Builder

- Interface Builder adds authoring support for the new `UIStackView` (iOS 9) and exposes a distribution property for `NSStackView` (OS X 10.11). There is an Embed In Stack View button at the bottom right of the canvas. (18420765)
- Interface Builder adds support for `NSDateComponentsFormatter`, `NSDateIntervalFormatter`, `NSEnergyFormatter`, `NSMassFormatter`, and `NSLengthFormatter` in OS X apps. (17236851)
- Notes from the Interface Builder identity inspector are now included in `--export-strings-file` output and XLIFF files exported using the Export For Localization feature in the project editor. (18023555)
- Background placeholders on custom views and other containers can be hidden on the Interface Builder canvas by selecting Editor > Canvas > Show Background Placeholders. (20580948)
- Storyboard References may now be deployed to iOS 8, OS X 10.10, and watchOS 1.

  Backwards-deployed Storyboard References may not be connected to relationship segues and may not refer to storyboards in external bundles. (21275172)
- Interface Builder now supports placeholder references for scenes in other storyboards, and segues that cross storyboard boundaries. (9565583)

#### Build System

- The new build setting Objective-C Generated Interface Header Name (`SWIFT_OBJC_INTERFACE_HEADER_NAME`) controls the name used for the header that is generated by the Swift compiler for use in `#import` statements in Objective-C. (18063617)
- You can configure Xcode to run the `unifdef` tool on your headers during a Copy Headers build phase. This is enabled with the `COPY_HEADERS_RUN_UNIFDEF` build setting, and the flags to pass are controlled by the `COPY_HEADERS_UNIFDEF_FLAGS` build settings. Use:

  `$man unifdef`

  in a Terminal window for more information on what flags `unifdef` accepts. (18786269)
- The Xcode build system no longer automatically inherits the environment used to launch the app when running in the IDE. This prevents unnecessary rebuilds when Xcode.app is opened from the command line.

  If necessary, users can opt in to the old behavior by entering this command in Terminal:

  `$defaults write com.apple.dt.Xcode UseSanitizedBuildSystemEnvironment -bool NO`

  __Note:__ For compatibility reasons, this behavior is not the default when running builds with `xcodebuild`. However, users who wish to interchange between building Xcode and building using xcodebuild can add the following argument:

  `-UseSanitizedBuildSystemEnvironment=YES`

  on the command line to also use a sanitized environment in `xcodebuild`.

  (20668232)
- The new build setting Product Bundle Identifier (`PRODUCT_BUNDLE_IDENTIFIER`) is the recommended place to set the Bundle Identifier for a target. The target’s `Info.plist` should be configured to use this build setting by referencing it as `$(PRODUCT_BUNDLE_IDENTIFIER)` in the value for the `CFBundleIdentifier` key.

  Xcode offers to configure this for you when you accept the “Upgrade to recommended settings” project modernization in the issue navigator, unless your target preprocesses its `Info.plist` file. In that case you will need to configure this setting manually. This change is backwards-compatible to older versions of Xcode.

  This change is required to make certain features work, such as On Demand Resources, if your target preprocesses its `Info.plist` file. (20887827)
- You can specify per-file compiler flags for derived source files in the Build Rules tab of the target editor. These flags will work in Xcode 6.3 as well, although they cannot be edited or viewed with any Xcode prior to Xcode 7. (5924168)
- During the build, Xcode populates build settings that describe the version of the SDK being built against.

  These settings are:

  - `SDK_VERSION`: x.y version of the SDK being used. For example, '10.10' for OS X 10.10, or '8.0' for iOS 8.
  - `SDK_VERSION_ACTUAL`: Single integer representing the SDK version. For example, 101000, or 80000.
  - `SDK_VERSION_MAJOR`: Single integer representing the major version of the SDK. For example, 101000 (which would be the value for 10.10.0 or 10.10.4), or 80000 (which would be the value for 8.0 or 8.3).
  - `SDK_VERSION_MINOR`: Single integer representing the minor version of the SDK. For example, 1000 or 1004 (for 10.10.0 or 10.10.4), or 0 or 300 (for 8.0 or 8.3).

  (20341285)

#### Testing

- UI testing in Xcode 7 is introduced as a replacement for the existing `UIAutomation` support in Instruments. (22345571)

#### Debugging

- While you are debugging your view hierarchy, Xcode allows you to focus on a portion of your app by double-clicking on a view.

  To exit, click the “X” in the debug navigator’s Focused indicator or double-click in the white space of the editor. (18553133)
- Instruments now supports disabling the Automatic Termination feature of Transparent Application Lifecycle when launching OS X applications.

  To disable Automatic Termination when Instruments launches an OS X app:

  1. Select the “Edit {app name}” menu item in the process chooser after initially selecting the process.
  2. Select the gear icon in the application settings window.
  3. Select the “Disabled” menu item underneath the “Transparent Application Lifecycle - Automatic Termination” section.

  Once you have configured this application setting, Instruments launches the OS X app with an additional command line option that disables Automatic Termination. The setting is remembered for all future launches of that app. (18105188)
- Xcode displays crash reports in the Crashes Organizer that originated from your iOS App Extension crashes. (19309974)

#### General

- Xcode 7 lets you find symbols choosing Find > “Find Selected Symbol in Project.” (15573153)
- The find navigator shows caller hierarchy. Select a function or method, and right-click to select “Find Call Hierarchy.” (15716883)
- The find navigator displays the language for `.strings` files containing matches. (18372154)
- The user defaults domain for `xcodebuild` has changed to `com.apple.dt.xcodebuild`.

  `xcodebuild` continues to read from the old user defaults domain (`xcodebuild`) at a lower priority than the new one. (20181486)
- `xcodebuild` supports a `-hideShellScriptEnvironment` option.

  This option causes Xcode to suppress listing the environment variables set for each Run Script build phase, significantly reducing build output verbosity for some projects. (20309279)
- The assistant editor can obtain a summary of the interface of your Swift classes.

  When viewing a Swift file in the primary editor, setting the assistant to the Counterparts mode shows a summarized version of the class that includes declarations (but not implementation) of the methods and functions in your file along with doc comments. (17684981)
- The assistant editor set to Generated Interface mode displays the Swift interface of an Objective-C header file. (19320817)

### Changes

- Exporting an archive for the App Store requires an account with iTunes Connect Access. (19940553)
- Multiple components of Xcode 7 run with library validation enabled in order to prevent exploitation by malicious code. Any code that interposes system libraries or that is injected into process using `DYLD_INSERT_LIBRARIES` may cause problems when you are running Xcode 7.

  You are advised to either remove software that interposes system libraries or is injected into processes using `DYLD_INSERT_LIBRARIES` from your system, or contact the vendor of such software for an update. (22366994)

### Deprecations

- OS X v10.11 is the last major release of OS X that supports the previously deprecated garbage collection runtime.

  Applications or features that depend upon garbage collection may not function properly or will not launch when this runtime is removed. Developers should use Automatic Reference Counting (ARC) or manual retain/release for memory management. Xcode includes tools to aid in this migration. (20589595)
- The existing `UIAutomation` support in Instruments is deprecated. Use UI testing in Xcode 7. (22345571)

### Notes

- The OpenSSL headers have been removed from the OS X v10.11 SDK. (21232069)
- OS X El Capitan no longer ships with `genstrings`. That utility is instead provided by Xcode 7. This means that older versions of Xcode won’t find `genstrings` in `/usr/bin` like they would on older versions of OS X. (19708961)

### Swift

#### Swift Language Features

- New defer statement. This statement runs cleanup code when the scope is exited, which is particularly useful in conjunction with the new error handling model. For example:

  ```swift
  func xyz() throws {
     let f = fopen("x.txt", "r")
     defer { fclose(f) }
     try foo(f)                    // f is closed if an error is propagated.
     let f2 = fopen("y.txt", "r")
     defer { fclose(f2) }
     try bar(f, f2)                // f2 is closed, then f is closed if an error is propagated.
  }                                // f2 is closed, then f is closed on a normal path
  ```

  (17302850)
- Printing values of certain enum types shows the enum case and payload, if any. This is not supported for `@objc` enums or certain enums with multiple payloads. (18334936)
- You can specify availability information on your own declarations with the `@available()` attribute.

  For example:

  ```swift
  @available(iOS 8.0, OSX 10.10, *)
  func startUserActivity() -> NSUserActivity {
    ...
  }
  ```

  This code fragment indicates that the `startUserActivity()` method is available on iOS 8.0+, on OS X v10.10+, and on all versions of any other platform. (20938565)
- A new `@nonobjc` attribute is introduced to selectively suppress ObjC export for instance members that would otherwise be `@objc`. (16763754)
- Nongeneric classes may now inherit from generic classes. (15520519)
- Public extensions of generic types are now permitted.

  `public extension Array { … }`

  (16974298)
- Enums now support multiple generic associated values, for example:

  ```swift
  enum Either<T, U> {
     case Left(T), Right(U)
  }
  ```

  (15666173)
- Protocol extensions: Extensions can be written for protocol types.

  With these extensions, methods and properties can be added to any type that conforms to a particular protocol, allowing you to reuse more of your code. This leads to more natural caller side “dot” method syntax that follows the principle of “fluent interfaces” and that makes the definition of generic code simpler (reducing “angle bracket blindness”). (11735843)
- Protocol default implementations: Protocols can have default implementations for requirements specified in a protocol extension, allowing “mixin” or “trait” like patterns.
- Availability checking. Swift reports an error at compile time if you call an API that was introduced in a version of the operating system newer than the currently selected deployment target.

  To check whether a potentially unavailable API is available at runtime, use the new `#available()` condition in an `if` or `guard` statement. For example:

  ```
  if #available(iOS 8.0, OSX 10.10, *) {
    // Use Handoff APIs when available.
    let activity =
      NSUserActivity(activityType:"com.example.ShoppingList.view")
    activity.becomeCurrent()
  } else {
    // Fall back when Handoff APIs not available.
  }
  ```

  (14586648)
- Native support for C function pointers: C functions that take function pointer arguments can be called using closures or global functions, with the restriction that the closure must not capture any of its local context.

  For example, the standard C `qsort` function can be invoked as follows:

  ```
  var array = [3, 14, 15, 9, 2, 6, 5]
  qsort(&array, array.count, sizeofValue(array[0])) { a, b in
    return Int32(UnsafePointer<Int>(a).memory - UnsafePointer<Int>(b).memory)
  }
  print(array)
  ```

  (16339559)
- Error handling. You can create functions that throw, catch, and manage errors in Swift.

  Using this capability, you can surface and deal with recoverable errors, such as “file-not-found” or network timeouts. Swift’s error handling interoperates with NSError. (17158652)
- Testability: Tests of Swift 2.0 frameworks and apps are written without having to make internal routines public.

  Use `@testable import {ModuleName}` in your test source code to make all public and internal routines usable. The app or framework target needs to be compiled with the Enable Testability build setting set to `Yes`. The Enable Testability build setting should be used only in your Debug configuration, because it prohibits optimizations that depend on not exporting internal symbols from the app or framework. (17732115)
- `if` statements can be labeled, and labeled `break` statements can be used as a jump out of the matching `if` statement.

  An unlabeled `break` does not exit the `if` statement. It exits the enclosing loop or `switch` statement, or it is illegal if none exists. (19150249)
- A new `x?` pattern can be used to pattern match against optionals as a synonym for `.Some(x)`. (19382878)
- Concatenation of Swift string literals, including across multiple lines, is now a guaranteed compile-time optimization, even at `-Onone`. (19125926)
- Nested functions can now recursively reference themselves and other nested functions. (11266246)
- Improved diagnostics:

  - A warning has been introduced to encourage the use of `let` instead of `var` when appropriate,
  - A warning has been introduced to signal unused variables.
  - Invalid mutation diagnostics are more precise.
  - Unreachable switch cases cause a warning.
  - The `switch` statement “exhaustiveness checker” is smarter.

  (15975935),(20130240)
- Failable convenience initializers are allowed to return `nil` before calling `self.init`.

  Designated initializers still must initialize all stored properties before returning `nil`; this is a known limitation. (20193929)
- A new `readLine()` function has been added to the standard library. (15911365)
- SIMD Support: Clang extended vectors are imported and usable in Swift.

  This capability enables many graphics and other low-level numeric APIs (for example, `simd.h`) to be usable in Swift.
- New `guard` statement: This statement allows you to model an early exit out of a scope.

  For example:

  ```
  guard let z = bar() else { return }
  use(z)
  ```

  The else block is required to exit the scope (for example, with `return`, `throw`, `break`, `continue`, and so forth) or end in a call to a `@noreturn` function. (20109722)
- Improved pattern matching: `switch/case` pattern matching is available to many new conditional control flow statements, including `if/case`, `while/case`, `guard/case`, and `for-in/case`. `for/in` statements can also have `where` clauses, which combine to support many of the features of list comprehensions in other languages.
- A new `do` statement allows scopes to be introduced with the `do` statement. For example:

  ```
  do {
      //new scope
      do {
          //another scope
      }
  }
  ```

#### Swift Enhancements and Changes

- The OS X v10.11, iOS 9, and watchOS 2 SDKs have adopted modern Objective-C features such as nullability, typed collections, and others to provide an improved Swift experience.
- A new keyword `try?` has been added to Swift.

  `try?` attempts to perform an operation that may throw. If the operation succeeds, the result is wrapped in an optional; if it fails (that is, if an error is thrown), the result is `nil` and the error is discarded. For example:

  ```swift
  func produceGizmoUsingTechnology() throws -> Gizmo { … }
  func produceGizmoUsingMagic() throws -> Gizmo { … }

  if let result = try? produceGizmoUsingTechnology() { return result }
  if let result = try? produceGizmoUsingMagic() { return result }
  print("warning: failed to produce a Gizmo in any way")
  return nil
  ```

  `try?` always adds an extra level of `Optional` to the result type of the expression being evaluated. If a throwing function’s normal return type is `Int?`, the result of calling it with `try?` will be `Int??`, or `Optional<Optional<Int>>`. (21692467)
- Type names and `enum` cases now `print` and convert to `String` without qualification by default. `debugPrint` or `String(reflecting:)` can still be used to get fully qualified names. For example:

  ```swift
  enum Fruit { case Apple, Banana, Strawberry }
  print(Fruit.Apple)      // “Apple”
  debugPrint(Fruit.Apple) // “MyApp.Fruit.Apple”)
  ```

  (21788604)
- C typedefs of block types are imported as typealiases for Swift closures.

  The primary result of this is that typedefs for blocks with a parameter of type `BOOL` are imported as closures with a parameter of type `Bool` (rather than `ObjCBool` as in the previous release). This matches the behavior of block parameters to imported Objective-C methods. (22013912)
- The type `Boolean` in MacTypes.h is imported as `Bool` in contexts that allow bridging between Swift and Objective-C types.

  In cases where the representation is significant, `Boolean` is imported as a distinct `DarwinBoolean` type, which is `BooleanLiteralConvertible` and can be used in conditions (much like the `ObjCBool` type). (19013551)
- Fields of C structs that are marked `__unsafe_unretained` are presented in Swift using `Unmanaged`.

  It is not possible for the Swift compiler to know if these references are really intended to be strong (+1) or unretained (+0). (19790608)
- The `NS_REFINED_FOR_SWIFT` macro can be used to move an Objective-C declaration aside to provide a better version of the same API in Swift, while still having the original implementation available. (For example, an Objective-C API that takes a `Class` could offer a more precise parameter type in Swift.)

  The `NS_REFINED_FOR_SWIFT` macro operates differently on different declarations:

  - Init methods will be imported with the resulting Swift initializer having “__” prepended to its first external parameter name.

    `- (instancetype)initWithClassName:(NSString *)name NS_REFINED_FOR_SWIFT;`

    `init(__className: String)`
  - Other methods will be imported with “__” prepended to their base name.

    `- (NSString *)displayNameForMode:(DisplayMode)mode NS_REFINED_FOR_SWIFT;`

    `func __displayNameForMode(mode: DisplayMode) -> String`
  - Subscript methods will be treated like any other methods and will not be imported as subscripts.
  - Other declarations will have “__” prepended to their name.

    `@property DisplayMode mode NS_REFINED_FOR_SWIFT;`

    `var __mode: DisplayMode { get set }`

  (20070465)
- Xcode provides context-sensitive code completions for enum elements and option sets when using the shorter dot syntax. (16659653)
- The `NSManaged` attribute can be used with methods as well as properties, for access to Core Data’s automatically generated Key-Value-Coding-compliant to-many accessors.

  ```
  @NSManaged var employees: NSSet

  @NSManaged func addEmployeesObject(employee: Employee)
  @NSManaged func removeEmployeesObject(employee: Employee)
  @NSManaged func addEmployees(employees: NSSet)
  @NSManaged func removeEmployees(employees: NSSet)
  ```

  These can be declared in your `NSManagedObject` subclass.
  (17583057)
- The grammar has been adjusted so that lines beginning with ‘.’ are always parsed as method or property lookups following the previous line, allowing for code formatted like this to work:

  ```
  foo
    .bar
    .bas = 68000
  ```

  It is no longer possible to begin a line with a contextual static member lookup (for example, to say `.staticVar = MyType()`). (20238557)
- Code generation for large struct and enum types has been improved to reduce code size. (20598289)
- Nonmutating methods of structs, enums, and protocols may now be partially applied to their `self` parameter:

  ```
  let a: Set<Int> = [1, 2, 3]
  let b: [Set<Int>] = [[1], [4]]
  b.map(a.union) // => [[1, 2, 3], [1, 2, 3, 4]]
  ```

  (21091944)
- Swift documentation comments recognize a new top-level list item:

  ```
  - Throws: ...
  ```

  This item is used to document what errors can be thrown and why. The documentation appears alongside parameters and return descriptions in Xcode QuickHelp. (21621679)
- Unnamed parameters now require an explicit `_:` to indicate that they are unnamed. For example, the following is now an error:

  `func f(Int) { }`

  and must be written as:

  `func f(_: Int) { }`

  This simplifies the argument label model and also clarifies why cases like `func f((a: Int, b: Int))` do not have parameters named “`a`” and “`b`.” (16737312)
- It is now possible to append a tuple to an array. (17875634)
- The ability to refer to the 0 element of a scalar value (producing the scalar value itself) has been removed. (17963034)
- Variadic parameters can now appear anywhere in the parameter list for a function or initializer. For example:

  ```swift
  func doSomethingToValues(values: Int... , options: MyOptions = [], fn: (Int) -&gt; Void) { … }
  ```

  (20127197)
- Generic subclasses of Objective-C classes are now supported. (18505295)
- If an element of an enum with string raw type does not have an explicit raw value, it will default to the text of the enum’s name. For example:

  ```swift
  enum WorldLayer : String {
      case Ground, BelowCharacter, Character
  }
  ```

  is equivalent to:

  ```swift
  enum WorldLayer : String {
      case Ground = "Ground"
      case BelowCharacter = "BelowCharacter"
      case Character = "Character"
  }
  ```

  (15819953)
- The `performSelector` family of APIs is now available for Swift code. (17227475)
- When delegating or chaining to a failable initializer (for example, with `self.init(…)` or `super.init(…)`), one can now force-unwrap the result with “`!`.” For example:

  ```swift
  extension UIImage {
    enum AssetIdentifier: String {
      case Isabella
      case William
      case Olivia
    }

    convenience init(assetIdentifier: AssetIdentifier) {
      self.init(named: assetIdentifier.rawValue)!
    }
  }
  ```

  (18497407)
- Initializers can now be referenced like static methods by referring to `.init` on a static type reference or type object. For example:

  ```
  let x = String.init(5)
  let stringType = String.self
  let y = stringType.init(5)

  let oneTwoThree = [1, 2, 3].map(String.init).reduce("”, combine: +)
  ```

  `.init` is still implicit when constructing using a static type, as in `String(5)`. `.init` is required when using dynamic type objects or when referring to the initializer as a function value. (21375845)
- Enums and cases can now be marked `indirect`, which causes the associated value for the enum to be stored indirectly, allowing for recursive data structures to be defined. For example:

  ```swift
  enum List<T> {
    case Nil
    indirect case Cons(head: T, tail: List<T>)
  }

  indirect enum Tree<T> {
    case Leaf(T)
    case Branch(left: Tree<T>, right: Tree<T>)
  }
  ```

  (21643855)
- Formatting for Swift expression results has changed significantly when using `po` or `expr -O`. Customization that was introduced has been refined in the following ways:

  - The formatted summary provided by either `debugDescription` or `description` methods will always be used for types that conform to `CustomDebugStringConvertible` or `CustomStringConvertible` respectively. When neither conformance is present, the type name is displayed and reference types also display the referenced address to more closely mimic existing behavior for Objective-C classes.
  - Value types such as enums, tuples, and structs display all members indented below the summary by default, while reference types will not. This behavior can be customized for all types by implementing `CustomReflectable`.

  These output customizations can be bypassed by using `p` or `expr` without the `-O` argument to provide a complete list of all fields and their values. (21463866)
- Properties and methods using `Unmanaged` can now be exposed to Objective-C. (16832080)
- Applying the `@objc` attribute to a class changes that class’s compile-time name in the target’s generated Objective-C header as well as changing its runtime name. This applies to protocols as well. For example:

  ```objc
  // Swift
  @objc(MyAppDelegate)
  class AppDelegate : NSObject, UIApplicationDelegate {
    // ...
  }

  // Objective-C
  @interface MyAppDelegate : NSObject <UIApplicationDelegate>
    // ...
  @end
  ```

  (17469485)
- Collections containing types that are not Objective-C compatible are no longer considered Objective-C compatible types themselves.

  For example, previously `Array<SwiftClassType>` was permitted as the type of a property marked `@objc`; this is no longer the case. (19787270)
- Generic subclasses of Objective-C classes, as well as nongeneric classes that inherit from such a class, require runtime metadata instantiation and cannot be directly named from Objective-C code.

  When support for generic subclasses of Objective-C classes was first added, the generated Objective-C bridging header erroneously listed such classes, which, when used, could lead to incorrect runtime behavior or compile-time errors. This has been fixed.

  The behavior of the `@objc` attribute on a class has been clarified such that applying `@objc` to a class which cannot appear in a bridging header is now an error.

  Note that this change does not result in a change of behavior with valid code because members of a class are implicitly `@objc` if any superclass of the class is an `@objc` class, and all `@objc` classes must inherit from `NSObject`. (21342574)
- The performance of `-Onone` (debug) builds has been improved by using prespecialized instances of generics in the standard library. It produces significantly faster executables in debug builds in many cases, without impacting compile time. (20486658)
- `AnyObject` and `NSObject` variables that refer to class objects can be cast back to class object types. For example, this code succeeds:

  ```
    let x: AnyObject = NSObject.self
    let y = x as! NSObject.Type
  ```

  Arrays, dictionaries, and sets that contain class objects successfully bridge with `NSArray`, `NSDictionary`, and `NSSet` as well. Objective-C APIs that provide `NSArray<Class> *` objects, such as `-[NSURLSessionConfiguration protocolClasses]`, now work correctly when used in Swift. (16238475)
- `print()` and reflection via Mirrors is able to report both the current case and payload for all enums with multiple payload types. The only remaining enum types that do not support reflection are `@objc` enums and enums imported from C. (21739870)
- Enum cases with payloads can be used as functions. For example:

  ```swift
  enum Either<T, U> { case Left(T), Right(U) }
  let lefts: [Either<Int, String>] = [1, 2, 3].map(Either.Left)
  let rights: [Either<Int, String>] = [“one”, “two”, “three”].map(Either.Right)
  ```

  (19091028)
- `ExtensibleCollectionType` has been folded into `RangeReplaceableCollectionType`. In addition, default implementations have been added as methods, which should be used instead of the free Swift module functions related to these protocols. (18220295)

#### Swift Standard Library

- The standard library moved many generic global functions (such as `map`, `filter`, and `sort`) to be methods written with protocol extensions. This allows those methods to be pervasively available on all sequence and collection types and allowed the removal of the global functions.
- Deprecated enum elements no longer affect the names of nondeprecated elements when an Objective-C enum is imported into Swift. This may cause the Swift names of some enum elements to change. (17686122)
- All enums imported from C are `RawRepresentable`, including those not declared with `NS_ENUM` or `NS_OPTIONS`. As part of this change, the value property of such enums has been renamed `rawValue`. (18702016)
- Swift documentation comments use a syntax based on the Markdown format, aligning them with rich comments in playgrounds.

  - Outermost list items are interpreted as special fields and are highlighted in Xcode QuickHelp.
  - There are two methods of documenting parameters: parameter outlines and separate parameter fields. You can mix and match these forms as you see fit in any order or continuity throughout the doc comment. Because these are parsed as list items, you can nest arbitrary content underneath them.
  - Parameter outline syntax:

    ```
    - Parameters:
      - x: ...
      - y: ...
    ```
  - Separate parameter fields:

    ```
    - parameter x: ...
    - parameter y: ...
    ```
  - Documenting return values:

    ```
    - returns: ...
    ```

  Other special fields are highlighted in QuickHelp, as well as rendering support for all of Markdown. (20180161)
- The `CFunctionPointer<T -> U>` type has been removed. C function types are specified using the new `@convention(c)` attribute. Like other function types, `@convention(c) T -> U` is not `nullable` unless made optional. The `@objc_block` attribute for specifying block types has also been removed and replaced with `@convention(block)`.
- Methods and functions have the same rules for parameter names. You can omit providing an external parameter name with “`_.`” To further simplify the model, the shorthand “`#`” for specifying a parameter name has been removed, as have the special rules for default arguments.

  ```swift
  Declaration
    func printFunction(str: String, newline: Bool)
    func printMethod(str: String, newline: Bool)
    func printFunctionOmitParameterName(str: String, _  newline: Bool)

  Call
    printFunction("hello", newline: true)
    printMethod("hello", newline: true)
    printFunctionOmitParameterName("hello", true)
  ```

  (17218256)
- `NS_OPTIONS` types get imported as conforming to the `OptionSetType` protocol, which presents a set-like interface for options. Instead of using bitwise operations such as:

  ```
  // Swift 1.2:
  object.invokeMethodWithOptions(.OptionA | .OptionB)
  object.invokeMethodWithOptions(nil)

  if options @ .OptionC == .OptionC {
    // .OptionC is set
  }
  ```

  Option sets support set literal syntax, and set-like methods such as `contains`:

  ```
  object.invokeMethodWithOptions([.OptionA, .OptionB])
  object.invokeMethodWithOptions([])

  if options.contains(.OptionC) {
    // .OptionC is set
  }
  ```

  A new option set type can be written in Swift as a struct that conforms to the `OptionSetType` protocol. If the type specifies a `rawValue` property and option constants as static `let` constants, the standard library will provide default implementations of the rest of the option set API:

  ```swift
  struct MyOptions: OptionSetType {
    let rawValue: Int

    static let TuringMachine  = MyOptions(rawValue: 1)
    static let LambdaCalculus = MyOptions(rawValue: 2)
    static let VonNeumann     = MyOptions(rawValue: 4)
  }

  let churchTuring: MyOptions = [.TuringMachine, .LambdaCalculus]
  ```

  (18069205)
- Type annotations are no longer allowed in patterns and are considered part of the outlying declaration. This means that code previously written as:

  `var (a : Int, b : Float) = foo()`

  needs to be written as:

  `var (a,b) : (Int, Float) = foo()`

  if an explicit type annotation is needed. The former syntax was ambiguous with tuple element labels. (20167393)
- The `do/while` loop is renamed to `repeat/while` to make it obvious whether a statement is a loop from its leading keyword.

  In Swift 1.2:

  ```
  do {
  ...
  } while <condition>
  ```

  In Swift 2.0:

  ```
  repeat {
  ...
  } while <condition>
  ```

  (20336424)
- `forEach` has been added to `SequenceType`. This lets you iterate over elements of a sequence, calling a body closure on each. For example:

  ```
  (0..<10).forEach {
    print($0)
  }
  ```

  This is very similar to the following:

  ```
  for x in 0..<10 {
    print(x)
  }
  ```

  But take note of the following differences:

  - Unlike `for-in` loops, you can’t use `break` or `continue` to exit the current call of the body closure or skip subsequent calls.
  - Also unlike `for-in` loops, using `return` in the body closure only exits from the current call to the closure, not any outer scope, and won’t skip subsequent calls.

  (18231840)
- The `Word` and `UWord` types have been removed from the standard library; use `Int` and `UInt` instead. (18693488)
- Most standard library APIs that take closures or `@autoclosure` parameters now use “rethrows.” This allows the closure parameters to methods like `map` and `filter` to throw errors, and allows short-circuiting operators like `&&`, `||`, and `??` to work with expressions that may produce errors. (21345565)
- SIMD improvements: Integer vector types in the `simd` module now only support unchecked arithmetic with wraparound semantics using the `&+`, `&-`, and `&*` operators, in order to better support the machine model for vectors. The `+`, `-`, and `*` operators are unavailable on integer vectors, and Xcode automatically suggests replacing them with the wrapping operators.

  Code generation for vector types in the `simd` module has been improved to better utilize vector hardware, leading to dramatically improved performance in many cases. (21574425)
- All `CollectionType` objects are now sliceable. `SequenceType` now has a notion of `SubSequence`, which is a type that represents only some of the values but in the same order. For example, the `Array``SubSequence` type is `ArraySlice`, which is an efficient view on the `Array` type’s buffer that avoids copying as long as it uniquely references the `Array` from which it came.

  The following free Swift functions for splitting/slicing sequences have been removed and replaced by method requirements on the `SequenceType` protocol with default implementations in protocol extensions. `CollectionType` has specialized implementations, where possible, to take advantage of efficient access of its elements.

  ```
  /// Returns the first `maxLength` elements of `self`,
  /// or all the elements if `self` has fewer than `maxLength` elements.
  prefix(maxLength: Int) -> SubSequence

  /// Returns the last `maxLength` elements of `self`,
  /// or all the elements if `self` has fewer than `maxLength` elements.
  suffix(maxLength: Int) -> SubSequence

  /// Returns all but the first `n` elements of `self`.
  dropFirst(n: Int) -> SubSequence

  /// Returns all but the last `n` elements of `self`.
  dropLast(n: Int) -> SubSequence

  /// Returns the maximal `SubSequence`s of `self`, in order, that
  /// don't contain elements satisfying the predicate `isSeparator`.
  split(maxSplits maxSplits: Int, allowEmptySlices: Bool, @noescape isSeparator: (Generator.Element) -> Bool) -> [SubSequence]
  ```

  The following convenience extension is provided for `split`:

  `split(separator: Generator.Element, maxSplit: Int, allowEmptySlices: Bool) -> [SubSequence]`

  Also, new protocol requirements and default implementations on `CollectionType` are now available:

  ```
  /// Returns `self[startIndex..<end]`
  prefixUpTo(end: Index) -> SubSequence

  /// Returns `self[start..<endIndex]`
  suffixFrom(start: Index) -> SubSequence

  /// Returns `prefixUpTo(position.successor())`
  prefixThrough(position: Index) -> SubSequence
  ```

  (21663830)
- The `print` and `debugPrint` functions are improved:

  - Both functions have become variadic, and you can print any number of items with a single call.
  - `separator: String = " "` was added so you can control how the items are separated.
  - `terminator: String = "\n"` replaced `appendNewline: bool = true`.  With this change,

    `print(x, appendNewline: false)` is expressed as `print(x, terminator: "")`.
  - For the variants that take an output stream, the argument label `toStream` was added to the stream argument.

  The `println` function from Swift 1.2 has been removed. (21788540)
- For consistency and better composition of generic code, `ArraySlice` indices are no longer always zero-based but map directly onto the indices of the collection they are slicing and maintain that mapping even after mutations.

  Before:

  ```
  var a = Array(0..<10)
  var s = a[5..<10]
  s.indices        // 0..<5
  s[0] = 111
  s                // [111, 6, 7, 8, 9]
  s.removeFirst()
  s.indices        // 1..<5
  ```

  After:

  ```
  var a = Array(0..<10)
  var s = a[5..<10]
  s.indices        // 5..<10
  s[5] = 99
  s                // [99, 6, 7, 8, 9]
  s.removeFirst()
  s.indices        // 6..<10
  ```

  Rather than define variants of collection algorithms that take explicit subrange arguments, such as `a.sortSubrangeInPlace(3..<7)`, the Swift standard library provides “slicing,” which composes well with algorithms. This enables you to write `a[3..<7].sortInPlace()`, for example. With most collections, these algorithms compose naturally.

  For example, before this change was incorporated:

  ```swift
  extension MyIntCollection {
    func prefixThroughFirstNegativeSubrange() -> SubSequence {
      // Find the first negative element
      let firstNegative = self.indexOf { $0 < 0 } ?? endIndex

      // Slice off non-negative prefix
      let startsWithNegative = self.suffixFrom(firstNegative)

      // Find the first non-negative position in the slice
      let end = startsWithNegative.indexOf { $0 >= 0 } ?? endIndex
      return self[startIndex..<end]
    }
  }
  ```

  The above code would work for any collection of `Ints` unless the collection is an `Array<Int>`. Unfortunately, when array slice indices are zero-based, the last two lines of the method need to change to:

  ```
  let end = startsWithNegative.indexOf { $0 >= 0 }
    ?? startsWithNegative.endIndex
  return self[startIndex..<end + firstNegative]
  ```

  These differences made working with slices awkward, error-prone, and nongeneric.

  After this change, Swift collections start to provide a guarantee that, at least until there is a mutation, slice indices are valid in the collection from which they were sliced, and refer to the same elements. (21866825)
- The method `RangeReplaceableCollectionType.extend()` was renamed to `appendContentsOf()`, and the `splice()` method was renamed to `insertContentsOf()`. (21972324)
- `find` has been renamed to `indexOf()`, `sort` has been renamed to `sortInPlace()`, and `sorted()` becomes `sort()`.
- `String.toInt()` has been renamed to a failable `Int(String)` initializer, since initialization syntax is the preferred style for type conversions.
- `String` no longer conforms to `SequenceType` in order to prevent non-Unicode correct sequence algorithms from being prominently available on `String`. To perform grapheme-cluster-based, UTF8-based, or UTF-16-based algorithms, use the `.characters`, `.utf8`, and `.utf16` projections respectively.
- Generic functions that declare type parameters not used within the generic function’s type produce a compiler error. For example:

  `func foo<T>() { } // error: generic parameter ’T’ is not used in function signature`
- The `Dictionary.removeAtIndex(_:)` method now returns the key-value pair being removed as a two-element tuple (rather than returning `Void`). Similarly, the `Set.removeAtIndex(_:)` method returns the element being removed. (20299881)
- Generic parameters on types in the Swift standard library have been renamed to reflect the role of the types in the API. For example, `Array<T>` became `Array<Element>`, `UnsafePointer<T>` became `UnsafePointer<Memory>`, and so forth. (21429126)
- The `SinkType` protocol and `SinkOf` struct have been removed from the standard library in favor of `(T) -> ()` closures. (21663799)

### Objective-C

#### Objective-C Language Changes

- C functions that return Core Foundation objects via out-parameters can now describe whether the object is returned at +0 or +1.

  ```
  OSStatus MyCFGetImportantValue(CFDictionaryRef data,
    CFStringRef __nullable * __nonnull CF_RETURNS_NOT_RETAINED outImportantValue);
  OSStatus MyCFCopyImportantValue(CFDictionaryRef data,
    CFStringRef __nullable * __nonnull CF_RETURNS_RETAINED outImportantValue);
  ```

  (18742441)
- A `__kindof` type has been introduced. Objects declared as `__kindof` types behave like a mix of `id` and a specific object type: They specify an upper bound (for example, must be `UIView` or a subclass thereof) but allow implicit downcasting to any subtype of that upper bound. For example, if we assume that

  `-[UIView subviewWithTag:]`

  produces a `__kindof` type `UIView *`, then:

  ```
  UIButton *button = [view subviewWithTag:0];       // okay: UIButton is a UIView
  [[view subviewWithTag:0] setTitle:@"Bounded" forState: UIControlStateNormal];
                                                    // okay: method found in UIButton
  UIResponder *responder = [view subviewWithTag:0]; // okay: UIView is a UIResponder
  NSString *string = [view subviewWithTag:0];       // error: UIView is unrelated to NSString
  ```

  (19589424)
- The double-underscored nullability qualifiers (`__nullable`, `__nonnull`, and `__null_unspecified`) have been renamed to use a single underscore with a capital letter:`_Nullable`, `_Nonnull`, and `_Null_unspecified`, respectively). The compiler predefines macros mapping from the old double-unspecified names to the new names for source compatibility. (21530726)
- Lightweight generics now allow you to specify type information for collection classes such as `NSArray`, `NSSet`, and `NSDictionary`. The type information improves Swift access when you bridge from Objective-C, and simplifies the code you have to write. For example:

  ```
  NSArray<UIImage *> *images;
  NSDictionary<NSString *, NSURL *> *resourcesByName;
  ```

  (6294649)
- The `NS_SWIFT_NAME` macro can be used to control the imports of enumerations whose constants don’t map cleanly to Swift. For example:

  ```c
  typedef NS_ENUM(NSInteger, DisplayMode) {
    DisplayMode256Colors NS_SWIFT_NAME(With256Colors),
    DisplayModeThousandsOfColors,
    DisplayModeMillionsOfColors
  };
  ```

  is imported into Swift as:

  ```
  @objc enum DisplayMode : Int {
    case With256Colors
    case ThousandsOfColors
    case MillionsOfColors
  }
  ```

  The macro can also be used to control whether factory methods are imported as initializers. For example:

  ```objc
  @interface MyController : UIViewController
  + (instancetype)standardControllerForURLKind:(URLKind)kind NS_SWIFT_NAME(init(URLKind:));
  @end
  ```

  will be imported into Swift as:

  ```swift
  class MyController : UIViewController {
    init(URLKind kind: URLKind)
  }
  ```

  even though its name does not follow the convention for automatic factory method importing. (19240897)

### Resolved Issues

Issues resolved in Xcode 7.0 since Xcode 6.4

#### Interface Builder

- You can create multiple storyboards for WatchKit interfaces. (19781408)
- Interface Builder allows subclassing all segue types. (19911504)
- Interface Builder enables setting the `accessiblityIdentifier` property of `AppKit` and `UIKit` views, via the Identity inspector. (8913778)
- `NSBox` now stores its content view in Interface Builder documents, which also enables alignment guides between the box and its subviews. (10726996)
- Interface Builder documents with a development target less than or equal to Xcode 4.6 are upgraded when opening. (12984639)
- Interface Builder allows setting an identifier for an auto layout constraint to assist in debugging unsatisfiable constraints. (13645911)
- Alignment and distribution commands in Interface Builder can be used without generating constraints. (19223827)
- Resize knobs for views on the canvas are able to be interacted with outside the canvas frame. (15864964)
- Interface Builder supports connecting actions from trigger points on the sender other than `action` (such as `doubleAction`) in OS X documents. Xcode 7 also changes how connected actions are displayed in the Connections inspector for OS X documents to match iOS, and enables showing multiple connected actions. (2161960)
- The template for Radio buttons in the Interface Builder object library is now implemented as individual `NSButton` objects, rather than the older `NSMatrix`, which is discouraged on OS X v10.8 and later. Radio buttons automatically act as a group (selecting one button will unselect all other related buttons) when they have the same superview and `-action` method. (16965941)
- `initWithNibName:bundle:` is set as a designated initializer for `UITableViewController` in the iOS 9 SDK. (19775924)

#### Building

- Run Script scheme actions take the run destination into account when passing environment variables, such as `SDKROOT`, that depend on the run destination. (19652312)
- It is possible to toggle all the checkboxes in a column in the Manage Schemes sheet by holding down the option key when toggling a checkbox. (8096575)
- A Copy Files build phase on a framework target with a destination of PlugIns copies its contents to the PlugIns directory in the framework rather than the Resources directory. (11488493)
- The `xcodebuild install` command, when used with `-scheme`, builds the target specified for the Archive action of that scheme rather than the Run action. (19391445)
- The Xcode build system supports stale file removal of some types of build artifacts that were produced in a previous build, but have since been removed from the project.

  - Stale files are removed when the next build detects that they are no longer needed.
  - Stale files appear in the build log navigator under a “Remove stale build products” section.
  - If removal of a stale file would cause its containing directory to become empty, the directory is removed as well.
  - The kinds of build artifacts which are currently handled by stale file removal are:

    - - Copied resources and header files
    - - On-demand resources in asset packs
    - - Module map specifications
    - - Swift generated API headers
  - Only build artifacts produced in the `OBJROOT`, `SYMROOT`, or `DSTROOT` are available for stale file removal.

  (19479602)
- Archive build operations use the `install` value for the `ACTION` build setting. Ramifications:

  - - Shell scripts can use this behavior to detect when Xcode is archiving versus building.
  - - Existing shell scripts which inspect the `ACTION` environment variable should be updated according.
  - - External build system targets are passed the `install` action instead of `build`, when archiving, and should be updated accordingly.
  - - External build system targets and aggregate targets with shell script build phases have the appropriate values of `TARGET_BUILD_DIR` and `BUILT_PRODUCTS_DIR` which point to appropriate installation location (and respect the `SKIP_INSTALL` build setting).

  (20192652)

#### Simulator

- The Simulator Background Fetch menu item in Xcode works as expected. (20145602)

#### Debugging

- The view debugging tool has object inspectors for `NSView` and `UIView`. (18120189)

#### General

- Xcode allows the `IDEBuildOperationMaxNumberOfConcurrentCompileTasks` user default to exceed the number of CPUs available in the machine. (20998547)
- Localization settings made in a target’s scheme (as well as other settings made on the command line) are honored on launch in the Simulator. (19490124)
- Xcode 7 fixes a crash that occurred when a document is edited while an unlocking script is running for that same document. (21528657)

### Known Issues

Known issues in Xcode 7.0

#### Swift

- Using `switch` against multiple types with `as` patterns may cause a memory leak. For example, avoid this kind of `switch` statement:

  ```
  switch x {
    case let a as A: ...
    case let b as B: ...
    case let c as C: ...
    default: ...
  }
  ```

  Rewrite the code to use `if let a = x as? A` statements instead of `switch`. This pattern performs type checks that avoid the memory leak. (22587077)

#### Playgrounds

- Playgrounds created by previous versions of Xcode may not be upgradable to Swift 2.

  Choose Editor > Upgrade Playground to upgrade the playground before attempting to it convert to Swift 2. (20902099)
- Opening a playground that was previously displaying the Version editor may present an alert stating, “The file <filename> couldn’t be opened because you don’t have permission to view it.”

  Dismiss the alert dialog and show the Standard editor. (20623808)

#### Interface Builder

- Setting the Semantic attribute of views in Interface Builder has no effect at runtime.

  Create an outlet to the view for which you wish to change the Semantic attribute, then set the attribute programmatically in `awakeFromNib`. (22529786)

#### Localization

- During `XLIFF` export or import, `NSLocalizedString` macro issues or empty strings files may result in an error, “The data couldn’t be read because it isn’t in the correct format."

  Remove empty strings files from your project or use the following Terminal command to find `NSLocalizedString` macro issues in your project.

  `$find <project directory> -name "*.m" -exec xcrun extractLocStrings {} \;`

  (21101899)
- UI elements on a Watch extension may appear in English despite the app being localized to a different language.

  Localize all components of your Watch app, including its extension, to the desired language. (22065581)

#### Bitcode

- Apps that include incorrectly-built bitcode in frameworks and libraries are rejected by the App Store.

  If you are a provider of framework and library products for iOS, watchOS, and tvOS platforms, your products must include full bitcode content. The Xcode 7 build system defaults include enabling the Enable Bitcode build setting, but standard Debug or Release builds do not include the full bitcode content in the built framework and library products.

  To build framework and library products for distribution and ensure that the full bitcode content is included, framework and library providers must:

  - Ensure that the Enable Bitcode build setting is correct (`ENABLE_BITCODE=YES`).
  - Perform either an Archive build or an Install build to produce framework and library products for distribution.

  (22483622)
- Framework and library providers need to include bitcode for Xcode 7 development, and Xcode 7 generates bitcode by default. However, bitcode-enabled framework and library products do not work well with Xcode 6. If you still need to support Xcode 6 development, you must produce an additional version of your products without bitcode.

  To build a library without bitcode, either use Xcode 7 with the build setting Enable Bitcode disabled (`ENABLE_BITCODE=NO`) or use Xcode 6. (22462511)
- If you use supplied framework or library products and need to support Xcode 6 development, be sure that you are using the correct products from your supplier. Frameworks and libraries include bitcode when built for Xcode 7 development, but bitcode-enabled libraries do not work well with Xcode 6. The issues and fixes differ based on whether you are using static libraries or dynamic libraries.

  __Static libraries.__ An attempt to use a bitcode-enabled static library with Xcode 6 generates linker errors about duplicate symbols such as `_llvm.embedded.module` and `_llvm.cmdline`.

  You need a version of the static library built without bitcode to use it with Xcode 6.

  __Dynamic libraries.__ An embedded framework with a dynamic library that contains bitcode does not lead to any errors with Xcode 6, but it increases the app size unnecessarily.

  To avoid this issue with an existing framework, use the `bitcode_strip` command from Xcode 7 to remove bitcode from a copy of the framework. Using a Terminal window:

  1. `cd` to the framework directory.
  2. Use `xcode-select` to choose Xcode 7 if you have multiple versions of Xcode installed.
  3. Enter the following commands, substituting the framework's name for `{Framework}`:

     ```shell
     $ xcrun bitcode_strip -r {Framework}.dylib -o tmp.dylib
     $ mv tmp.dylib {Framework}.dylib
     ```

  (22462511)

#### Building

- If your iOS app embeds a watchOS app and you have a framework for both iOS and watchOS embedded in each app, your project fails to build when you perform the Archive action.

  Use a different product name (using the `PRODUCT_NAME` build setting) for the watchOS version of your framework. (22183332)
- When you create a watchOS framework in Xcode 7.0, a Watch Application is set as the embedding destination. This fails to install on devices because watchOS frameworks must be embedded in a Watch Extension target.

  Remove the embedding of the framework into the Watch Application:

  1. Select your project in the project navigator to open the project editor.
  2. Select the Watch Application target.
  3. Select the framework in the “Linked Frameworks and Libraries” list.
  4. Click Delete (-) to remove the framework.

  After the framework has been removed from the Watch Application, configure it to be embedded into the Watch Extension:

  1. Select your project in the project navigator to open the project editor.
  2. Select the Watch Extension target.
  3. Click Add (+) in the “Linked Frameworks and Libraries” list.
  4. Select the framework from the displayed list.
  5. Click Add.

  __Note:__ You may have to remove the build folder to ensure a clean rebuild after you've completed this reconfiguration.

  1. Hold down the Option key.
  2. Choose Product > Clean Build Folder

  (22522811)
- watchOS frameworks are not configured by default to be app extension safe.

  Because watchOS frameworks are used by Watch Extensions, they must be marked as app extension safe. After creating a watchOS framework target, set the `Require Only App-Extension-Safe API` build setting for the framework target to `Yes`. (22540012)

#### Simulator

- In the Simulator, background upload/download using `NSURLSession` completes, but notifications do not badge the app to show completion when the app is in the background.

  Testing on devices works as expected. (16532261)
- The Watch simulator may stop taking input after a reset or reboot.

  If the Watch simulator doesn’t respond to the Home button event, quit and restart the Watch simulator.
  (21135676)
- Playing video to a simulated external display does not function correctly with Simulator running as an iPad.

  Use Simulator running as an iPhone. (17979778)
- Video playback to a 1080p external display in Simulator renders at a lower resolution.

  Play video at a lower resolution or test 1080p playback with a device. (18296724)

#### Testing

- UI testing cannot identify elements using information from their accessibility title element.

  Set an accessibility identifier instead. (20409319)
- UI testing cannot record or interact with popovers on OS X. (21162677)

#### Debugging

- When Runtime Sanitization is enabled for an Xcode Server bot, detailed information about any crash triggered by sanitization checks is made available in the raw build log for the integration. (21047341)
- You cannot debug a watchOS 1 app extension in a project that also has watchOS 2 app built in the same iOS app.

  Xcode prefers the watchOS 2 app when both are present, you need to remove the watchOS 2 app from the iOS app bundle to enable debugging the watchOS 1 app extension. Edit the Build Phases of the iOS App to remove the watchOS 2 app as a build dependency of the iOS app and remove it from the Embed Watch Content build phase. Clean the build products, and then Run to debug the watchOS 1 app extension. (21173814)
- While debugging an app that uses on-demand resources from Xcode, the progress of tag requests may reset to zero when moving the application to or from the foreground, or when changing the `loadingPriority` of an `NSBundleResourceRequest`. (21882271)

#### Source Control

- The Comparison and Blame view in the Versions editor may not produce results for playgrounds. (21879794)
- Passwords for source control accounts may appear empty in Xcode 7.

  Reenter the password. (21252258)

#### General

- Xcode 7 does not support two-factor authentication.

  Developers should continue to authenticate with their user name and password. (19581582)
- Restoring your device while Xcode is open may cause your device to appear as unavailable or locked after the restore is complete.

  Unplug and plug in your device after a restore. (21344895)
- Using the devices window while running an app on a device from an archive, crash logs may not be symbolicated or may be only partially symbolicated.

  Duplicate the dSYM file inside the archive’s dSYM folder and drag it to your desktop, and then wait a few minutes for Spotlight to index the symbols for you. (21867829)
- Crash logs for app extensions are not available in builds distributed via TestFlight. (22661518)

[Next](Xcode%206%20Release%20Notes.md)[Previous](Xcode%20Release%20Notes%20%E2%80%94%20Archive.md)

