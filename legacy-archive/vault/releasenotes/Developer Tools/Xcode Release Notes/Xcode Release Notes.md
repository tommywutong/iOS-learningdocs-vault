---
title: Xcode Release Notes
apple_id: TP40001051
resource_type: Release Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2018-06-13'
source_url: https://developer.apple.com/library/archive/releasenotes/DeveloperTools/RN-Xcode/Chapters/Introduction.html
archived_at: '2026-07-18T02:50:27.282798Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md)


[Next](Document%20Revision%20History.md)

# Xcode Release Notes

You obtain Xcode 9.4.1 from the Mac App Store. It is a free download that installs directly into the Applications folder.

The Apple Developer Program provides everything you need to build and distribute your apps on the App Store for iPhone, iPad, Mac, and Apple Watch. Membership includes access to beta OS releases, advanced app capabilities, and tools to develop, test, and distribute apps and Safari extensions. For more information, visit [Apple Developer Program](https://developer.apple.com/programs/).

Apple provides the following resources to support development with Xcode:

- Developer documentation is available both on the [Apple Developer website](https://developer.apple.com/documentation) and from Xcode by choosing Help > Developer Documentation.
- [Apple Developer Forums](https://forums.developer.apple.com/). Participate in discussions about developing for Apple platforms and using developer tools.
- [Bug Reporter](http://bugreport.apple.com/). Report issues, enhancement requests, and feedback to Apple. Provide detailed information, including the system and developer tools version information, and any relevant crash logs or console messages.
- [Apple Developer](https://developer.apple.com/) website. Get the latest development information as well as technical documentation for Xcode.
- [Xcode homepage](https://developer.apple.com/xcode/). Get high-level information about the latest release of Xcode. Download current and beta Xcode releases.
- For help with using Xcode, Simulator, or Instruments, choose Help > _app name_ Help.

For issues not mentioned in [Xcode Release Notes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltc), please file bugs through the Apple Developer website [https://developer.apple.com/bug-reporting/](https://developer.apple.com/bug-reporting/).

When filing a bug, please include the full version number in the bug title and in the description. To find the version number, choose Xcode > About Xcode, the full version number including the part in parenthesis is in the window that appears. The full version number looks like _9.4.1 (9Fxxx)_.

Additionally, you may discuss these issues in the Apple Developer Forums: [https://forums.developer.apple.com/welcome](https://forums.developer.apple.com/welcome). To get more information about iCloud for Developers, go to [https://developer.apple.com/icloud](https://developer.apple.com/icloud).

_Xcode Release Notes_ is sometimes updated after a release is distributed. Please check this document for updates.

_Revision: XC941 - XRN1_

- Xcode 9 requires a Mac running macOS 10.13.2 or later.
- Xcode 9 includes SDKs for iOS 11.4, watchOS 4.3, macOS 10.13, and tvOS 11.4.

- Updated Git to version 2.15.2 to address CVE-2018-11233 and CVE-2018-11235. (40631597)

- Asset catalogs with ARKit assets can compile if the deployment version is less than 11.3. (39218934)
- Resolved an issue that could cause a crash when dragging a `.gif` image into a Sticker Pack in an Asset Catalog. (38820366)
- Resolved an issue that could cause progress to get stuck while editing AR assets in an Asset Catalog. (38393995)

- Xcode 9.4 adds support for developing apps with ClassKit.

- Adding a fetch request to a Core Data model containing a UUID or URI attribute will not crash Xcode. (39470899)

- Fixed navigation of items with extensions in the Find navigator. (39601956)

- Resolved an issue where loading a saved trace could result in an empty Symbols panel. (38813311)

- Fixed an issue where exporting an app using Ad Hoc distribution would fail with an error about missing the `beta-reports-active` entitlement. (39462609)

- In some situations, the compiler may crash during code generation for generic enumerations with multiple payloads inside generic functions where there are redundant protocol requirements or same-type constraints. In the crash log backtrace, this will show up as a crash inside `MultiPayloadEnumImplStrategy::emitIndirectInitialize`. (39040680)

  _Workaround_: Make the affected enumeration an `indirect` enumeration.
- Defining a private class nested inside an extension constrained with same-type constraints may lead to a runtime crash when the class is initialized. (39208961)

  For example:

```
extension Optional where Wrapped == NSData {
    private class Foo {}
}

let x = Optional<NSData>.Foo()
```

  _Workaround_: Move the class definition out of nested position, and nest a type alias to the class instead:

```
private class _Optional_NSData_Foo {}

extension Optional where Wrapped == NSData {
  typealias Foo = _Optional_NSData_Foo
}

let x = Optional<NSData>.Foo()
```


- Fixed an issue causing the user to have to log in with their Apple ID repeatedly. (39573406)

- Addressed an issue that would cause Xcode to hang when using Playgrounds. (37822125)

Developers can use a new 64-bit testing mode in macOS 10.13.4 to test software for 64-bit compatibility.

To enable the 64-bit testing mode:

1. Boot to Recovery OS by restarting your machine and holding down the Command and R keys at startup.
2. Launch Terminal
3. Execute the following command: `nvram boot-args="-no32exec"`
4. Restart the machine

The 64-bit testing mode prevents 32-bit processes from launching. Launching an app that depends on 32-bit software results in a notification that the application can't be opened. Other types of software may fail silently, such as 32-bit versions of Dashboard and WebKit plugins, preference panes, and background processes.

Disable the test mode once the software is updated to work in 64-bit.

To disable the 64-bit testing mode:

1. Boot to Recovery OS by restarting your machine and holding down the Command and R keys at startup.
2. Launch Terminal
3. Execute the following command: `nvram boot-args=""`
4. Restart the machine

In future releases, the 64-bit testing mode may provide additional information for the developer to help test and qualify software.

- Removed the 32-bit option from the Architectures build settings UI. (35517385)
- Building for 32-bit architecture on macOS now emits a warning. (35709244)

- The Core Animation instrument and template have been deprecated in Instruments. The functionality previously under "Debug Options" has moved to Xcode, under "Debug > View Debugging > Rendering". (22971414)
- The OpenGL ES Analyzer Instrument is no longer supported. It has been replaced by the GPU Frame Debugger in Xcode and will be removed in a future version of Instruments. (35104029)

- The new [Energy organizer](http://help.apple.com/xcode/mac/current/#/dev36a5a9141) shows logs generated when your app or app extension exceeds a reasonable CPU threshold in the foreground or background causing battery drain on your user's device. (28640769)

  The [Energy organizer](http://help.apple.com/xcode/mac/current/#/dev36a5a9141) features include:

  - Energy logs are reported for your app when distributed on TestFlight or the App Store.
  - Server-side symbolication when uploading symbol information to Apple.
  - Automatic client-side symbolication when symbol information is saved locally.
  - CPU sample reports that are generated when your process is terminated for high CPU usage while the app is in the background.
  - Grouping logs with similar backtraces in energy reports.
  - Viewing the heaviest backtrace of CPU sample logs in the Debug navigator.
  - Compressing log stack frames by non-user stack frames and low sample count stack frames.
- Code coverage can now select the targets to include in a code coverage report. (27752500)

  To configure the targets to include:

  1. Open the Scheme editor.
  2. Select the Test action.
  3. Show the Options pane.
  4. In the pane, enable Code Coverage.
  5. In the pop-up menu, choose "some targets."
  6. Select the targets for the code coverage report.
- Text in the Code Snippets library filter bar now includes code completion shortcuts. (8147546)
- User-defined code snippets now appear at the top of the library, rather than the bottom. (8901028)

- Users may have to log in with their Apple ID repeatedly. (39347493)

  _Workaround_: Set this user default in Terminal:

  `defaults write com.apple.dt.Xcode DVTDeveloperAccountUseKeychainService -bool NO`

  Then quit and relaunch Xcode. You may need to authenticate your Apple ID once more.

- Xcode 9.3 adds a new `IDEWorkspaceChecks.plist` file to a workspace's shared data, to store the state of necessary workspace checks. Committing this file to source control will prevent unnecessary rerunning of those checks for each user opening the workspace. (37293167)
- Resolved a performance issue when switching away from Issue Navigator into other Navigators, especially the Find Navigator. (35363603)
- The source editor find and replace control now supports Full Keyboard Access. (33666790)

- A class and instance method with the same selector on an Objective-C protocol are both callable on a class that implements that protocol. (34596043)

- Dragging an image from Finder to an empty sticker pack is rejected. Xcode crashes when dragging an image in the Project navigator to an empty Sticker pack. (38509180)

  _Workaround_: Create a new sticker in the empty sticker pack, then drag the image from Finder or Project navigator into the new sticker well.
- App Icon set in Asset Catalog in a new watchOS template app does not include the App store icon. (37480050)

  _Workaround_: Select watchOS 1.0 and later in the Attributes Inspector, this will generate the App store icon, set it back to watchOS 2.0 and later if only watchOS 2.0 is supported.

- Xcode now runs more Swift build tasks in parallel with other commands. This may improve build times for Swift projects, but may also increase memory use during the build. This feature can be disabled from Terminal by setting a user default with `defaults write com.apple.dt.Xcode BuildSystemScheduleInherentlyParallelCommandsSerially -bool YES`. (35551983)
- Added an option to optimizing by size (`-Osize`) to the Optimization Level for the Swift compiler to the Build Settings pane of the Project editor. When this mode is selected the Swift compiler minimizes the size of compiled code. (36887476)

  The choice for compiling Swift code by file or by module moved from the Optimization Level setting to Compilation Mode, which is a new setting for the Swift compiler in the Build Settings pane of the Project editor. Previously this choice was combined with others in the Optimization Level setting. Compiling by file enables building only the files that changed, enabling faster builds. Compiling by module enables better optimization. (36887476)

- When an .xcconfig file contains multiple assignments of the same build setting, later assignments using `$(inherited)` will inherit from earlier assignments when using the new build system. The old build system discards all except the last assignment. This can cause the evaluated result to be different if `$(inherited)` is used in the value. You can enable a setting to emit a warning if any of these cases are found by running `defaults write com.apple.dt.XCBuild EnableCompatibilityWarningsForXCBuildTransition YES`. (37833468)
- When the new build system is enabled, changing the `Info.plist` file doesn’t cause Xcode to re-sign your app. This may cause your app to crash on launch after an incremental build. (34016924)

  _Workaround_: After changing the `Info.plist` file, make a change to your app’s source code to trigger recompilation and re-signing, or perform a clean rebuild.

- The new build system now supports all of the Product > Perform Action > Compile, Analyze, Preprocess, or Assemble operations for single-files. (31072405)
- Improved new build system rebuild times for configurations which have the "DWARF with dSYM File" build setting enabled by performing only the necessary work for dSYM generation during incremental rebuilds. (30668974)
- Prevented Spotlight from indexing the module cache folder for builds, by renaming the folder to `ModuleCache.noindex` which results in an improvement in overall build performance. (35212165)
- Fixed an issue in which the Clean Build Folder command could fail to complete. (36117298)
- When using the new build system, navigating from a build issue to a header now correctly opens the header in the project source instead of the copy built into the product. (29060887)
- Fixed a bug which would sometimes cause the `-showBuildSettings` option to `xcodebuild` to hang. (33881306)
- Single file actions in the new build system use the active run destination. (23767795)
- Fixed several issues which could cause Convert to Current Swift Syntax not to work when using the new build system. (36265451)
- Fixed an issue in the new build system that incorrectly rebuilt files on the next build after a build error. (35319783)
- "Build system information" errors from the new build system now appear in both the Issue Navigator and in the build logs. (34873210)
- Fixed an issue in which using Build and Analyze with the new build system could cause Xcode to crash. (32920792)

- Fixed a problem with code completion on a line containing emoji or non-ASCII characters. (24906321)

- In the Core Data editor, property settings for `NSFetchRequest` are now included in the compiled data model. (13432055)

- Memory graph debugging now uses a cleaner, more compact layout for non-cycle graphs. (36987034)
- Added new Core Animation debug options for iOS and tvOS devices that were previously available only in the Core Animation Instrument. Choose Debug > View Debugging > Rendering to access the options. (27976406)

- Enhanced the performance of the `po` command when printing Objective-C objects in the console. (34197161)
- NSLayoutConstraints listed for a selected view when debugging an app’s view hierarchy now show their identifier in the inspector. (34736382)

- The Connect via Network checkbox may become unchecked when first enabling network development for a device. (36797900)

  _Workaround_: Check the checkbox again.

- The Activity view no longer displays "Untitled" instead of the progress of a device operation, such as an app install. (35620763)
- Xcode may fail to capture a screen shot from an attached device. (36632000)

- Documentation for the HealthKit framework is missing from the Developer Documentation window. (39005708)

  _Workaround_: Read [the HealthKit framework documentation](https://developer.apple.com/documentation/healthkit) on the web.

- The "Import Sampler Data..." menu item has been removed from Instruments. Open the sample text output by selecting through the normal "Open..." panel. (36866911)
- The Cocoa Layout template has been removed. The instrument is still available in the Library palette. To use the Cocoa Layout instrument, open the Library palette, create a document using the Blank template, and drag in the Cocoa Layout instrument from the library to the new document. (21963317)

- The "Energy Log" instrument doesn't work for iPhone X and iPhone 8. (36569629)
- The SceneKit instrument shows a warning icon on the right of the target selection with messages “view settings could not be restored”. The SceneKit Instrument still works correctly and the warning can be safely ignored. (38081921)
- Profiling iOS framework unit tests works only for the Release configuration. (26883826)

  _Workaround_: Modify the scheme's Test option to use the Release build configuration.

  1. Product -> Scheme -> Edit Scheme…
  2. Select the Test tab.
  3. Change the Build Configuration to be Release.
  4. Attempt to profile the framework unit test again.

- Using a color from an asset catalog in the large title text attributes of a UINavigationBar results in a runtime exception. (35645022)
- SKView from the object library does not behave correctly in Mac documents. (37127877)

  _Workaround_: Drag out a custom view and set its class to SKView.

- Toolbars or multiline labels in stack views no longer result in an Auto Layout misalignment on the canvas. This issue resulted in problems such as zero width multi-line labels, or in extra tall toolbars when an iPhone X was selected in the device bar. (35377301)
- Placeholder text for `UITextField` now appears correctly on the Interface Builder canvas. (35909580)
- Changing a segue from "Show Detail" to "Show" no longer keeps the action selector for Show Detail. This default action will be automatically restored when compiling or saving a storyboard with Xcode 9.3 or later. (23505175)
- Removed spurious warnings for using `NSImageNameTouchBar*` constants in Touch Bar. (35773248)
- System-provided fonts are no longer archived in the `<customFonts>` XML element for iOS and tvOS documents. This resolves exceptions in `libFontParser.dylib` when launching apps. (35126633)
- Fixed an issue compiling macOS storyboards that resulted in incorrectly logging: "Unknown Window class (null) in Interface Builder file, creating generic Window instead." (34994636)
- Increased the helpfulness of the VoiceOver descriptions and tooltips for control and text alignment items in the Attributes inspector. (29782636)

- Added the LOCALIZED_STRING_MACRO_NAMES build setting for adding custom localized string macros in addition to the default `NSLocalizedString` and `CFLocalizedString` families of macros. Each entry in the build setting is the base name for a set of four localization macros. For example, adding `MyErrorString` to the list enables using `MyErrorString()`, `MyErrorStringFromTable()`, `MyErrorStringFromTableInBundle()`, and `MyErrorStringWithDefaultValue()` to localize strings in your project. (14842118)

- Resolved a crash that could occur when selecting a log in the Crashes organizer. (34869501)
- Resolved a crash that could occur when selecting the app version in the Crashes organizer. (35786034)
- Resolved an issue that resulted in the incorrect error message "No accounts with iTunes Connect access have been found [...]" when uploading an app to the App Store. (18369136)
- Improved the performance of the Organizer window when scrolling and resizing, and when loading many archives or many iTunes Connect apps. (18978906)

- Selecting text contained in rendered markup in the Find Navigator may not work as expected. (36382602)

  _Workaround_: Choose "Editor > Show Raw Markup" before selecting the text.

- Playgrounds with nested functions run correctly when using a custom toolchain from swift.org. (28784059)
- tvOS playgrounds now display their live views at the correct size. (35951627)
- Find Navigator now correctly searches all playground page content. (35751178)
- Fixed a crash that occurred when deleting text in a playground page that is displayed in multiple tabs. (34364618)

- Projects created in Xcode 9.3 use a new project format that is incompatible with earlier versions of Xcode. To open projects in earlier versions, change the project format by selecting the project in the Project navigator, opening the Document inspector, and selecting the desired format from the Project Format pop-up menu. (35207662)

- When adding a framework to a target, Xcode also checks that the path of the directory containing the added framework doesn't already exist in SYSTEM_FRAMEWORK_SEARCH_PATHS before adding that path to FRAMEWORK_SEARCH_PATHS. (29851042)

- Xcode provides a new quick look preview generator for provisioning profiles. The preview includes the app identifier, expiration date, certificates, device identifiers, and entitlements encoded within the profile. (37042581)

- Fixed a problem where a "Rename Failed" error would occur the second time you used the Refactor > Rename command. (36304316)

- Updated the Report navigator for Xcode Server integrations to show repository commits, logs, and sub-nodes for test and coverage results. (34493798)
- The debugger on macOS now requires the entitlement `com.apple.security.get-task-allow` to attach to apps built for macOS or for iOS, tvOS or watchOS apps built for Simulator. Xcode automatically injects this entitlement to your builds. The entitlement is stripped from apps distributed using the Organizer window. (34638816)

  To disable Xcode injecting the entitlement, set `CODE_SIGN_INJECT_BASE_ENTITLEMENTS` to `NO` in the build settings for the target or app. (34638816)

- When starting Xcode Server, an alert may appear asking to provide the passphrase to access the xcsd keychain. (37795722)

  _Workaround_: Enter the passphrase which is stored in /Library/Developer/XcodeServer/SharedSecrets/XCSDKeychainSharedSecret.

- Resolves an issue that would cause Xcode to sign with entitlements from a different build configuration. (37324488)
- Resolves an issue where modifying your entitlements file sometimes did not trigger code signing to occur during your next build. (36882851)

- On macOS 10.13.4, booting iOS 11 and later in the Simulator may take several minutes the first time. (35628711)

- Improved the visual quality of scaled simulated iOS devices resulting in fewer visual artifacts. To get the best results, turn off Optimize Rendering in the Debug menu. (35295090)

- The Comparison View of the Version Editor has been redesigned with improved scrolling and visual styling. (35254006)
- Renamed user interface elements to clarify the information presented. In the Version editor "Blame View" is now "Authors View" and in the Source editor "Show Blame For Line" is now "Show Last Change For Line." (35031446)

- Reverting changes in the Comparison View now restores the original whitespace even if it doesn't match the current formatting options. (35009545)
- Git checkout operations no longer require committing changes to files that are unaffected by the operation. (35837784)
- Tagging a branch in Git now tags the most recent available revision of that branch. (35250057)

- Added Callers to the Structured Selection Action Popover. You can now command-click on functions, methods, and properties and quickly navigate to their callers. (32587508)
- Text anti-aliasing can be disabled in the source editor by opening Terminal and running the following command:

  `defaults write com.apple.dt.Xcode SourceEditorDisableAntialiasing -bool YES`

  Set the default to `NO` to turn anti-aliasing on. (31378200)
- Compiler notes can now be viewed in the source editor by clicking on the diagnostic icon. (35898603)
- Enhanced Jump to Definition to show the file and line number for each result to help distinguish similar results. (32020190)

- Fixed a problem where Undoing would not cancel an Edit All in Scope session when undoing past changes made with Edit All in Scope. (31906590)
- Code coverage highlighting in a group of lines in the source editor now works correctly when a group contains multiple subranges with different highlighting. (34802960)
- Fixed a problem with Edit All in Scope where typing was not coalesced into a single undo group. (31364117)
- Significantly improved performance editing and navigating large, multi-megabyte files. (31689732)
- Fixed a problem where printing would cut off the right and bottom edges of each page. (35427028)
- Fixed a problem where scrolling by a page using Option-Page Up or Option-Page Down would scroll too far. (34873829)
- Fixed a problem where copying text would not always preserve the syntax coloring when pasted into Keynote. (32823164)
- Live issues no longer remain in the source editor after a build succeeds. (35810806)
- Improved the reliability of Command-Click in the source editor. (35937969)
- The source editor page guide is now positioned correctly when line wrapping is disabled and the editor is horizontally scrolled. (32699889)
- Improved the accessibility of breakpoints, test statuses, issues, and warnings in the source editor. (33593039)
- Fixed a problem where the source editor did not respect the "Reduce Motion" System Preference when folding code. (35474751)
- Code coverage highlights in the source editor are no longer shown in the incorrect columns. (33040660)
- Resolved an issue where breakpoints may appear on the incorrect line when code is folded. (38082660)
- Improved the scroll bar accuracy for scrolling in large files. (32473788)
- The code coverage ribbon now shows correctly when line wrapping is disabled in the source editor. (20928769)
- Copying and pasting the contents of entire documents no longer adds an additional trailing newline. (36042915)
- Fixed a problem where Quick Help, Find Call Hierarchy, Reveal in Symbol Navigator, and Copy Symbol Name would give information for the wrong symbol. (31889593)

- Implicitly unwrapped optionals may be used only as a top level type for properties, function parameters, function return values, and variables. Nesting them inside other types is deprecated and results in a warning. This will change to an error in a later version of Swift. ([SR-3023](https://bugs.swift.org/browse/SR-3023), [SE-0054](https://github.com/apple/swift-evolution/blob/master/proposals/0054-abolish-iuo.md))
- Swift now consistently enforces that you can’t override a computed property with a stored property, even when the overridden property is marked as `lazy`. If you need to use a stored value when overriding a property, define a separate property as backing storage and make it available through your override. (35870371)
- The type checker now resolves a function overload as ambiguous when there is an overload that returns an optional type, another overload that returns a function type, and the function is called in a context where either overload's return type could be used. For example, on the last line of the the code example below, the type checker can't resolve which version of `f` to call because `result` has no explicit type information. (36892416)

```swift
struct S<T> {}

func f<T>(_: S<T>) -> T? { … }
func f<T>(_: S<T>) -> (T) -> Int { … }

let s = S<String>()
let result = f(s)    // now correctly reports the ambiguity as an error
```
- Passing different kinds of optionals (`?` or `!`) to a function as `inout` no longer requires overriding that function. (36913150)

  For example, the following code is now correct:

```swift
func takesOptional(i: inout Int?) { … }
var x: Int! = 1
takesOptional(&x)
```
- Swift now supports conditional compilation based on available modules using `canImport()` with an argument that is the name of a module that may not be present on all platforms. This condition tests whether it's possible to import the module, but doesn't actually import it. If the module is present, the platform condition returns true; otherwise, it returns false. ([SE-0075](https://github.com/apple/swift-evolution/blob/master/proposals/0075-import-test.md))

```
#if canImport(UIKit)
<#module-specific code#>
#endif
```
- When `swiftc` is run from the command line, the default deployment target is set to the version of the currently running OS. (29948658)
- Use of ownership keywords `weak` and `unowned` for property declarations in protocols now result in a warning ([SE-0186](https://github.com/apple/swift-evolution/blob/master/proposals/0186-remove-ownership-keyword-support-in-protocols.md)). However, as noted in ([SR-7182](https://bugs.swift.org/browse/SR-7182)), ownership keywords still have an effect when defining a protocol marked `@objc`, because they control the interface presented in the generated Objective-C header. No warnings will be issued if the protocol is marked `@objc`.
- Overriding a function when the only difference in the signature is the kind of optional (`?` or `!`) for an `inout` parameter is deprecated in all versions of Swift and results in a compiler warning. This will change to an error in a future version of Swift. ([SR-6685](https://bugs.swift.org/browse/SR-6685))
- Swift supports a new platform condition `targetEnvironment` with a single valid argument `simulator`. Conditional compilation of the form `#if targetEnvironment(simulator)` can now be used to detect when the build target is a simulator. The Swift compiler will attempt to detect, warn, and suggest the use of `targetEnvironment(simulator)` when evaluating platform conditions that appear to be testing for simulator environments indirectly, via the existing `os()` and `arch()` platform conditions. ([SE-0190](https://github.com/apple/swift-evolution/blob/master/proposals/0190-target-environment-platform-condition.md))
- The compiler now warns for more cases of non-exclusive memory access. These are shown as warnings in the Swift 4.1 compiler and may become errors for all language modes in future versions of the compiler.

  Examples of the new warnings include: an access to memory inside a nonescaping closure conflicting with an access that is already in progress, and a conflict in a closure with a non-generic type that is passed to a function expecting a generic closure. ([SR-6103](https://bugs.swift.org/browse/SR-6103))

  For example, the compiler now warns about overlapping accesses to the variable `value`:

```
var value = 7
withUnsafeMutablePointer(to: &value) {
  $0.pointee = value + 1
}
```

  One way to avoid the warning is to make a copy of the local variable before passing it as `inout`:

```
var value = 7
let valueCopy = value
withUnsafeMutablePointer(to: &value) {
  $0.pointee = valueCopy + 1
}
```

  Another way is to refer to the variable using a closure parameter instead of capturing it:

```
var value = 7
withUnsafeMutablePointer(to: &value) {
  $0.pointee = $0.pointee + 1
}
```
- Calls to unavailable functions are permitted if the calling context is also marked unavailable. This simplifies writing code that can be compiled with and without application extension restrictions enabled. (34949130)

- When a class conforms to a `private` or `fileprivate` protocol in one file, and the class is subclassed in another file or target, the compiler crashes with the messages "DESERIALIZATION FAILURE" and "top-level value not found." (22672176)

  _Workaround_: Change the protocol to `internal` instead of `private` or `fileprivate`, or set the Optimization Level build setting to Whole Module Optimization (`-O -whole-module-optimization`.)
- If a nested type in a codable type has the same name as a property of the codable type, the compiler will crash. (37570349)

  _Workaround_: Rename either the nested type or the property.
- A crash can occur during runtime whenever there is a generic class or a subclass of a generic class with a stored protocol metatype property. (38394640)

  Example:

```swift
protocol P { }
class Generic<T> {
  let protocolMetatype: P.Type
}
```

  _Workaround_: Box the metatype in a class.

```swift
class BoxedType {
  let p: P.Type
  init(_ type: P.Type) {
    p = type
  }
}

class Generic<T> {
  let boxedProtocolMetatype: BoxedType
}
```
- In circumstances where protocol methods or base class methods defined in Objective-C claim to take non-null arguments of type `id` in their headers, but get invoked with `nil` values at runtime, Swift code compiled by Xcode 9.3 that overrides those methods may crash when the Swift implementations are invoked. (38675815)

  _Workaround_: Change the Swift override to take a value of type `Any?`. For example, if you implement the `UIApplicationDelegate` protocol's `application(_:open:sourceApplication:annotation:)` method:

```swift
class AppDelegate: UIApplicationDelegate {
    func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any) -> Bool {
        return true
    }
}
```

  The program may crash when passed `nil` as the annotation argument. Avoid the crash by making the `annotation` argument have type `Any?`:

```swift
class AppDelegate: UIApplicationDelegate {
      func application(_ application: UIApplication, open url: URL, sourceApplication: String?, annotation: Any?) -> Bool {
        return true
    }
}
```
- Conditional conformances are unsupported when performing a dynamic cast (with `is` or `as`). ([SE-0143](https://github.com/apple/swift-evolution/blob/master/proposals/0143-conditional-conformances.md))

  For example:

```
print([1, 2, 3] is Codable) // Prints "false", but [Int]
                            // instances really are Codable.
try JSONEncoder().encode([1, 2, 3]) // Successfully encodes
                                    // the array as JSON.
```

  Arrays only conform to `Codable` when their elements are also `Codable`, but checking for this conformance isn't supported at runtime.

  While performing the `is` cast, the Swift runtime warns that it can't evaluate the conditional conformance:

  `warning: Swift runtime does not yet support dynamically querying conditional conformance ('Swift.Array<Swift.Int>': 'Swift.Decodable')`

- Generated headers for Swift content can be imported when a macro named `any` is defined. (34168022)
- Assigning a Swift closure expression into a global block variable that is declared in Objective-C now works correctly. (36843476)
- In a Swift class that is exposed to Objective-C, if `init()` is not supported then the `+new` method is marked as unavailable. (32405588)
- Objective-C methods with selectors that start with `add` or `remove` are now named consistently when imported into Swift. Previously, each occurrence of the same selector could be nondeterministically named by using or not using the portion of the name after `add` or `remove`, such as importing `addThing:` as either `add(_:)` or `addThing(_:)`. (33836975)

- A synthesized implementation of `==` is automatically added to a structure or enumeration that declares a conformance to `Equatable`. This requires that all stored properties of a structure or all enumeration cases with associated values are `Equatable`.

  Similarly, a synthesized implementation of `hashValue` is added when declaring a conformance to `Hashable`. This requires that all stored properties of a `struct` or all `enum` cases with associated values are `Hashable`.

  Providing your own implementation of `==` or `hashValue` overrides the one synthesized by the compiler. ([SE-0185](https://github.com/apple/swift-evolution/blob/master/proposals/0185-synthesize-equatable-hashable.md))
- If an extension adds an initializer to a structure that was declared in another module, the new initializer can't access `self` until it calls an initializer from the defining module. Attempting to access `self` before calling such an initializer results in a warning in Swift 4 and may result in an error in Swift 5. The requirement prevents an app from accidentally depending on the implementation details of a library. It also matches the existing requirement that cross-module initializers must be convenience initializers.

  Code that extends a struct imported from C is most likely to be impacted. However, most imported C structs are given a zeroing no-argument initializer that can be called as `self.init()` before modifying specific properties.

  Swift library authors who wish to continue allowing initialization on a per-member basis should explicitly declare a public memberwise initializer for clients that are in other modules. ([SE-0189](https://github.com/apple/swift-evolution/blob/master/proposals/0189-restrict-cross-module-struct-initializers.md))
- New _recursive_ constraints require that the associated type conform to the enclosing protocol. The standard library protocols have been updated to use recursive constraints including:

  - The `Indices` associated type has the same traversal requirements as the enclosing protocol, for example `Collection.Indices` conforms to `Collection`.
  - Requiring that `Numeric.Magnitude` conform to `Numeric`.
  - Using more efficient `SubSequence` types for lazy filter and map.
  - Eliminating the `*Indexable` protocols.

  ([SE-0157](https://github.com/apple/swift-evolution/blob/master/proposals/0157-recursive-protocol-constraints.md))

  For example, the `SubSequence` associated type of `Sequence` follows the enclosing protocol:

```
protocol Sequence {
  associatedtype Element
  associatedtype SubSequence: Sequence
  where SubSequence.Element == Element,
  SubSequence.SubSequence == SubSequence
  // ...
}

protocol Collection: Sequence where Self.SubSequence: Collection {
  // ...
}
```
- Access control is enforced for subclasses of generic classes. A `public` class may not subclass an `internal` class. For source compatibility, these new diagnostics are warnings in Swift 4.1. (35119972)
- KeyPaths now support subscript, optional chaining, and optional force-unwrapping components. (31768715)

- Performance of the dependency resolution algorithm has been significantly improved when there are shared dependencies in a package graph. Up to a 12X improvement has been observed in certain cases (36777215).

- When compiling jobs in parallel, the package manager determines the number of CPUs to use instead of using a hardcoded value. (35042923)
- In a package graph that uses different URL schemes, such as `ssh` and `http`, dependencies are now resolved correctly by the package manager. (27573226)
- The package manager now warns if a dependency is declared but not used. (35174605)
- The package manager now displays an error when there are two products with the same name. (34494792)
- Compiler warnings in Package.swift no longer prevent a build from completing successfully. (36324891)
- The `build` command in Swift package manager now works correctly when products of type `automatic` are used with the `--product` option. (36509350)
- The `edit` command for a package now finds a dependency correctly when the base name of the URL for the package and the name of the package in `Package.swift` don't match. ([SR-6758](https://bugs.swift.org/browse/SR-6758))

- `Encodable` and `Decodable` are now conditional conformances of `Optional`, `Array`, `Dictionary`, and `Set` that are available only when the type parameters conform to `Encodable` or `Decodable`. ([SE-0143](https://github.com/apple/swift-evolution/blob/master/proposals/0143-conditional-conformances.md), [SE-0166](https://github.com/apple/swift-evolution/blob/master/proposals/0166-swift-archival-serialization.md))
- `Optional`, `Array`, and `Dictionary` now conform to the `Equatable` protocol if their element types conform to `Equatable` enabling the comparison of two values of composed types, such as `[Int: [Int?]?]`. ([SE-0143](https://github.com/apple/swift-evolution/blob/master/proposals/0143-conditional-conformances.md))
- Index types for most standard library collections now conform to `Hashable` enabling the indices to be used in key-path subscripts and in hashed collections. ([SE-0188](https://github.com/apple/swift-evolution/blob/master/proposals/0188-stdlib-index-types-hashable.md))

  For example:

```
let s = "Hashable"
let p = \String.[s.startIndex]
s[keyPath: p] // "H"
```
- The variant of `Sequence.flatMap(_:)` that accepts a closure returning an `Optional` value has been deprecated. Other variants of `flatMap(_:)` on both `Sequence` and `Optional` remain as is. ([SE-0187](https://github.com/apple/swift-evolution/blob/master/proposals/0187-introduce-filtermap.md))
- Instances of `IndexDistance` associated type in the Swift standard library have been replaced by the concrete type `Int`. Algorithms that currently constrain `IndexDistance` to `Int` in their `where` clause, and algorithms that use `IndexDistance` within the body of a method, are supported by a deprecated type alias for `IndexDistance` in an extension on `Collection`. ([SE-0191](https://github.com/apple/swift-evolution/blob/master/proposals/0191-eliminate-indexdistance.md))

- Reconciled APIs between the multiple forms of unsafe pointers: `UnsafePointer`, `UnsafeMutablePointer`, `UnsafeRawPointer`, `UnsafeMutableRawPointer`, `UnsafeBufferPointer`, `UnsafeMutableBufferPointer`, `UnsafeRawBufferPointer`, and `UnsafeMutableRawBufferPointer`. Functionality previously only available in some interfaces are now available in all the relevant interfaces. ([SE-0184](https://github.com/apple/swift-evolution/blob/master/proposals/0184-unsafe-pointers-add-missing.md))

  The changes are additive with the following exceptions:

  - `deallocate(capacity:)` and `deallocate(bytes:alignedTo:)` are replaced by `deallocate()`. Simply removing the `capacity` argument or the `bytes` and `alignedTo` arguments preserves the behavior of the code.
  - `UnsafeMutableRawBufferPointer.allocate(count:)` is replaced by `UnsafeMutableRawBufferPointer.allocate(byteCount:alignment:)`. The behavior of the code can be preserved by adding an `alignment` argument, `MemoryLayout<UInt>.alignment`, to specify alignment on word boundaries.
  - `initializeMemory<T>(as:at:count:to:)`, is replaced by `initializeMemory<T>(as:repeating:count:)`. The `at` parameter is removed. Initializing at an offset can be achieved by multiplying the element index by `MemoryLayout<T>.stride` and adding to the raw pointer base.
- Some groups of collection types in the standard library, including slices and lazy collection wrappers, are now collapsed into single types using conditional conformance. The old types are available as deprecated type aliases for source compatibility. For more information on conditional conformance, see [https://swift.org/blog/conditional-conformance/](https://swift.org/blog/conditional-conformance/). (21935030)

- `xccov` is a new command-line utility for inspecting the contents of Xcode coverage reports. It can be used to view coverage data in both human-readable and machine parseable format. To learn more, enter `man xccov` in Terminal. (37172926)

- Classes that inherit from subclasses of `XCTestCase` now show inherited test methods in the Test navigator correctly. (34838443)
- The code coverage line execution counts for block literals are now correct. (22581085)
- Fixed an issue that could result in a code coverage report missing header files and any code in those header files. (28915357)
- Code coverage data is now captured for applications that are the target of UI tests when tests are run with xcodebuild. (23913271)
- Fixed an issue that resulted in the coverage report incorrectly displaying the "No Coverage Data" message. (36040075)
- Fixed several performance bottlenecks with code coverage including generating coverage reports and loading coverage reports in the Reports Navigator. In addition, navigating between files in the source editor while viewing code coverage no longer results in the spinning cursor. (33353328)
- Running tests on an iOS device with code coverage enabled no longer results in temporary freezes of the UI while downloading the code coverage profiles. (29681809)
- An issue that could cause `-[XCUIApplication launch]` and `-[XCUIApplication terminate]` to fail if code coverage is enabled and the debugger is disabled has been resolved. (36590025)
- The code coverage report now contains correct counts for static inline functions. (22520187)
- XCTest UI interruption monitors now work correctly on devices and simulators running iOS 10. (33278282)

- `NSFileProviderExtension` now works on iOS 9 and iOS 10 when the minimum supported OS version of the project is iOS 8.0 or earlier. (34828118)
- A workspace containing many cross-project references no longer experiences significant user interface lag shortly after opening. (14558737)

- When using Xcode 9.2 to create apps that deploy to iOS 8 and later, images in the asset catalog may be corrupted when viewed on devices running iOS 8.3 and earlier. (35379713)

  _Workaround_: Build the app using Xcode 9.1, or use Xcode 9.2 and set the deployment target to iOS 8.4 or later.

- Xcode now correctly compiles code that contains a `std::function` variable with an incomplete return type. (34010071)
- When `_POSIX_C_SOURCE` is defined, including libc++ headers that depend on `__threading_support`, such as `thread` or `mutex` no longer results in an error. (31263056)

- An experimental opt-in feature increases the number of concurrent build tasks that are run for Swift projects. This may improve build times for Swift projects, but may also increase memory use during the build. (35326759)

  To enable this feature, open the Terminal and enter the following command:

  `defaults write com.apple.dt.Xcode BuildSystemScheduleInherentlyParallelCommandsExclusively -bool NO`

  To disable the feature, delete the preference by entering the command:

  `defaults delete com.apple.dt.Xcode BuildSystemScheduleInherentlyParallelCommandsExclusively`

- The build system no longer produces inconsistent header maps while indexing. This resolves an issue with debugging Swift code using lldb. (34716477)

- The generated Objective-C `@property` declaration for a UUID attribute now always includes the `nullable` and `copy` annotations. (35273724)

- Added support for the `.mlmodel` specification version 2 which includes `float16` weights and custom layers in neural network models.
- Updated the Model viewer to show custom layer dependencies.

- Specifying a section inset reference point for a `UICollectionView`, such as relative to the Safe Area, is now supported in the Size inspector. (34812768)

- Fixed a performance issue that resulted in frequent rebuilds when editing an `IBDesignable` view. (28360728)
- Resolved a canvas rendering issue that sometimes occurred when switching the device configuration to iPhone X. (34424852)
- Localization warnings are no longer reported for a `UISegmentedControl` containing only images and no text. (34601808)
- Resolved a layout ambiguity with image-based `UIToolbar` buttons that resulted in a hang and in high CPU usage. (34057302)
- Localization warnings are no longer reported for a `UILabel` with `numberOfLines` set to `0`, or for any single-character text strings. (34767956)
- Resolved a canvas responsiveness issue when rendering a Storyboard containing a `UITextField`. (34808049)
- A layer-backed `IBDesignable` view no longer draws upside-down on the IB canvas. (34758240)
- Resolved a crash that occurred when trying to change the font for a localization comment in the Identity inspector for iOS, tvOS, and watchOS documents. (26097921)
- Device Bar labels are more concise when displayed as popup buttons. In addition, VoiceOver navigation is improved for groups around related mutually-exclusive buttons. (27480768)

- When the device configuration is set to an iPhone X, the height of the `UIToolbar` shown on the canvas may be too large. The iOS runtime is not affected.

  _Workaround_: Use a different device for editing on the canvas, or connect the scene to a navigation controller that contains a toolbar.

- Xcode no longer crashes when navigating between pages in a playground. (34821667)
- The Render Documentation checkbox now behaves correctly. (34627634)

- In Simulator, apps with the audio background capability now continue playing audio when switched to the background. (34591587)
- A watchOS app using Swift now runs on a simulated watchOS 2 device. (35063043)
- iCloud Drive now syncs on a simulated device running iOS 11.2 or later. (34669593)
- Swiping up to unlock a simulated iPhone X now works correctly. (33390776)

- When both Xcode 9.0 and 9.1 are installed, Simulator in Xcode 9.1 may not show devices for iOS 11.0, tvOS 11.0, or watchOS 4.0 in the Hardware > Device menu. (34761843)

  _Workaround_: Use Xcode 9.0 to build and run the app in Simulator on the desired device.
- Use of some 3rd party firewall tools that install kexts may cause problems launching apps in Simulator. (34829500)

  _Workaround_: Unload the problematic kexts using the `kextunload` command in the terminal. Disabling rules in the firewall application may not solve the problem.

- A thrown Swift Error object with an assertion message greater than 255 characters that is not caught may result in Xcode crashing. (35487430)

- UTF–16 string indices now increment correctly when there is a limiting index resulting in expressions such as `Range(NSRange(location: 1, length: 0), in: "")` returning `nil` instead of crashing. (34551055)

- Opening the Swift Migration Assistant when a workspace or project contains a Swift Playground no longer crashes. (35175054)

- `MTKMesh.newMeshes(asset:device:)` now populates the `MDLMesh` array in the return value correctly. (34624659)

- Fixed a bug that resulted in some uses of key path literals with optional chaining (`?`) components that either crash with the error message "pointer with negative count", or in memory corruption at runtime. (35367114)

- The `XCUIElementType` enumeration is now imported into Swift 4 as `XCUIElement.ElementType`, allowing the type name to be referenced in code. (34772051)

- The new build system properly respects localizations for all files when copying them into the Resources folder. (34025522)

- The Xcode debugger now displays improved error descriptions for most Swift fatal errors. (33365646)

- Display of Swift fatal errors in the debugger is enabled only when the main executable is using Swift. (35163654)

- Setting the Spring Loaded checkbox for drag and drop in the Interface Builder Attributes inspector now sets [isSpringLoaded](https://developer.apple.com/documentation/uikit/uispringloadedinteractionsupporting/2897189-springloaded) at runtime. (34284258)
- Setting the large title text attributes of [UINavigationBar](https://developer.apple.com/documentation/uikit/uinavigationbar) now works correctly. (33979437)
- When the Size simulated metric of a view controller is set to Freeform, Interface Builder now uses the freeform size for downstream view controllers with the Size metric set to Inferred. (33872052)
- Setting a `UITableView` in a XIB file to Grouped style with automatic row heights no longer hangs Xcode. (33483932)
- New checkbox and radio buttons added from the object library now have a default Vertical Content Hugging Priority that matches other `NSButton` objects. Priority values for existing objects remain unchanged. (21574446)
- Dragging a row within the user-defined runtime attributes table no longer discards the dragged attributes. (18444777)
- Clicking outside the text field when editing the key path of a user defined runtime attribute now works as expected. (12406749)

- Mirroring the user interface now works correctly when running a macOS app using a scheme that sets the Application Language to Right-to-Left Pseudolanguage With Right-to-Left Strings. (33923833)
- Reduced the number of false positive Auto Layout warnings for localized projects. (33849087)
- The `-importLocalizations` option of the `xcodebuild` command now adds files from the XLIFF to the project. (17305567)
- The `Info.plist` keys `NSLocationAlwaysAndWhenInUseUsageDescription` and `NSFaceIDUsageDescription` are now localizable for XLIFF export and import. (34589189, 34866053)

- Uploading In-App Purchase content from the Xcode Organizer window now works correctly. (33951562)

- Using a networked device for testing in Xcode Server currently requires that the user account for running integrations is logged in and that Xcode Server is the frontmost app. For information on setting up Xcode Server, see Perform Continuous Integration > Configure Xcode Server in [Xcode Help](https://help.apple.com/xcode/mac/current/#/dev399fc6efa). (33904987)

- In Simulator, the video in an [AVPlayerViewController](https://developer.apple.com/documentation/avkit/avplayerviewcontroller) no longer appears outside the safe area on the iPhone X. (34339660)
- Improved the rendering quality of Simulator on 2016 and 2017 MacBook Pros. (33998687)
- Reducing the sized of an iPhone X in Simulator by dragging no longer results in a edge swipe on the simulated device. (33974533)
- Choosing Window -> Scale -> Actual Size in Simulator now sets an iPhone X to the correct size. (33908038)
- Fixed an issue in Simulator's OpenGL that could cause SceneKit apps to run slowly and the CPU to hit 100% when attempting to pan in an MKMapView.
- In Simulator, panning an `MKMapView` in a SceneKit app now works correctly. (33664759)
- watchOS apps that use Swift may fail to run on a simulated device running any version of watchOS 2. (35063043)

  _Workaround_: Test watchOS 2 apps on a device, or test in Simulator on watchOS 3 or later.

- Xcode now supports using a Git worktree as a working copy. (24745300)
- The source control history editor now updates correctly when updating the local working copy. (33919644)

- The following ARKit and Metal symbols are now available for Swift on iOS. (34642200)

  ARKit:

  - `ARFaceGeometry.verticies`
  - `ARFaceGeometry.textureCoordinates`
  - `ARFaceGeometry.triangleIndices`

  Metal:

  - `MTLRenderCommandEncoder.setTileBuffers(_:offsets:range:)`
  - `MTLRenderCommandEncoder.setTileTextures(_:range:)`
  - `MTLRenderCommandEncoder.setTileSamplerStates(_:range:)`
  - `MTLRenderCommandEncoder.setTileSamplerStates(_:lodMinClamps:lodMaxClamps:range:)`

- When running a test action which involves multiple bundles, the `xcodebuild` command line tool no longer intermittently shuts down simulated devices. (33983007)
- Testing no longer intermittently fails at the end of a successful test run with the error “DTXProxyChannel error 1.” (33948901)

- When using Swift 4, referring to the nested enumeration type `XCUIElement.Type` by name is not possible. This can result in a compile time error in other places in your code when working with the type of an `XCUIElement.Type`. Using a value of the nested enumeration works correctly.

  The issue doesn't occur in Swift 3 code because the enumeration is named `XCUIElementType`. (34772051)

  _Workaround_: Add a type definition to your bridging header, such as:

```objc
#import <XCTest/XCTest.h>

typedef XCUIElementType FIX_XCUIElementDotTypeWorkaround;
```


- Updated Simulator to use the iOS runtime used on iPhone X.

- In the Editor > Resolve Auto Layout Issues submenu, Add Missing Constraints and Reset to Suggested Constraints now create the correct constraints for a view that is in a view controller that is downstream of a navigation controller. (34603925)

- Moving localized files in the structure editor no longer causes Xcode to crash. (34551605)
- Adding files to a project now adds them to the selected targets. (34551617)
- Reordering items in a group in the Project navigator no longer results in Xcode consuming excess CPU. (34551671)

- In Simulator, the Settings app crashes the first time it is opened. Subsequent launches work correctly. (34522196)

- Swift apps using generic casting and reflection now run correctly on macOS 10.9 and iOS 7. (34595478)

- The following AVFoundation symbols are now correctly marked as public:

  - `AVCaptureDevice.Format.supportedColorSpaces`
  - `AVCapturePhotoOutput.supportedFlashModes`
  - `AVCapturePhotoOutput.availablePhotoPixelFormatTypes`
  - `AVCapturePhotoOutput.availableRawPhotoPixelFormatTypes`
  - `AVCapturePhotoSettings.availablePreviewPhotoPixelFormatTypes`

  (34538928)

- Added `Test` and `Tests` as suffixes for determining file counterparts used in navigation and in the Assistant Editor. (28981734)
- Added `-runFirstLaunch`, a new `xcodebuild` flag that checks the status of the license agreement and installs any packages required for launching Xcode. (23529342)
- Core NFC can now be enabled via the Capabilities tab in Xcode. (32520707)
- Added support for running multiple versions of the Xcode app at the same time, and of any associated tools such as Simulator. Xcode 9.0 can't be run at the same time as earlier versions. (23140937)

- Fixed an issue causing App Store uploads to fail with error code –22421. (25068558)

- On OS X 10.9 or iOS 7, running a Swift app that uses generic casting or reflection may result in an error that includes the wording `object_isClass symbol not found`. (33872748)
- Uploading In-App Purchase content from Organizer window fails with the error message `The archive contains nothing that can be signed`. (33951562)

  _Workaround:_ Use Transporter to upload In-App Purchase content. For more information, see [https://help.apple.com/itc/appsspec](https://help.apple.com/itc/appsspec).
- When exporting an ad-hoc or enterprise IPA, Swift symbol stripping requires enabling app thinning or Rebuild from Bitcode. For more information, see [Distribution options](https://help.apple.com/xcode/mac/current/#/devde46df08a) in Xcode Help. (31737836)

  _Workaround:_ Enable app thinning or Rebuild from Bitcode when exporting the app.

- Apps with a deployment target of iOS 11 no longer build a 32-bit slice. To build and include a 32-bit slice, set the deployment target to an earlier version of iOS. (32163517)

- Added a check for using the memory for a variable that is out of scope. (32308829)
- Added "Detect use of stack after return", an optional check for using the memory for a local function variable after the function has returned. Turn on the option in the Diagnostics pane of the Scheme editor. (32308829)
- Address Sanitizer is now compatible with Malloc Scribble. (32359908)

- Increased the performance of incremental link-time optimization. (22867330)
- Added a warning for calls to `performSelector` where the method referred to by the selector may return a structure, union, or vector type. (12056271)
- Updated `-Wstrict-prototypes` to warn about nonprototype functions, block declarations, and types in C and in Objective-C. (15060615)
- Updated how the `expected identifier` error handles C++ keywords in Objective-C++ code. Identifiers that are valid in Objective-C but invalid in Objective-C++ have a more specific error message. An example of the new error is: `error: expected identifier; 'new' is a keyword in Objective-C++ @protocol new ^`. The parser has better recovery after this error, to improve error reporting in the rest of the file. (20626062)
- Added `-iframeworkwithsysroot`, a command line option that prepends the system root path (`-isysroot`) to the path of the provided framework. (21316352)
- Added `-Wunguarded-availability`, a new compiler flag that warns of an unguarded use of an Objective-C API that was introduced in a version of the OS that is later than the deployment target version.

  To guard the use of new APIs, use an `if` statement combined with `@available`, a new Objective-C expression that checks the system version. For example:

```
if (@available(macOS 10.13, iOS 11, *)) {
   // The compiler will not warn about uses of APIs from macOS 10.13
   // or iOS 11 here
}
```

  C or C++ code can use `__builtin_available`, a new builtin whose semantics are equivalent to `@available`.

  The `-Wunguarded-availability` flag is off by default to prevent unexpected warnings in existing projects. `-Wunguarded-availability-new`, a less strict version of the compiler flag that warns about unguarded uses of APIs only when they were introduced in macOS 10.13 or later, iOS 11 or later, tvOS 11 or later, or watchOS 4 or later. The `-Wunguarded-availability-new` flag is on by default. (7184689)
- The placeholder for a block parameter that uses a `typedef` instead of specifying the block type directly now expands to the block declaration when using code completion for setters of block properties. (21981862)
- Xcode provides code-completion results for missing C++11 constructs and keywords. The following constructs are included in the code-completion results:

  - `static_assert`
  - `alignas`

  The following keywords and special identifiers are included in the code-completion results:

  - `constexpr`
  - `final`
  - `noexcept`
  - `override`
  - `thread_local`

  The `__auto_type` keyword is included in code-completion results for code that uses C or Objective-C. (29219185)
- Xcode provides code-completion results for members from dependent classes. For example:

```
template<typename T>
void appendIfTrue(std::vector<T> &dest, const T &value) {
   dest. // Xcode will now show relevant completion results after '.'
}
```

  Note that code-completion results won’t be provided when the member expression includes a dependent base. For example:

```
template<typename T>
void appendIfTrue(std::vector<std::vector<T>> &dest, const T &value) {
   dest.at(0). // Xcode *will not* have the relevant completion results
               // for the members of std::vector here
}
```

  (29818301)
- The state of the `#pragma pack` directive in an included precompiled header is now preserved. (21359084)
- Warnings for incomplete umbrella headers in module maps now trigger even when the umbrella header is part of a submodule. (22623686)
- A redefinition error caused by the repeated inclusion of a nonmodular header now shows the include file stack leading to the repeated include. (24116019)

- When the `-E` flag in Clang is used for preprocessing, the `editor placeholder in source file` error is no longer shown. (32718000)

- Xcode fails to compile code that contains a `std::function` variable with an incomplete return type. For example, the following code below doesn't conform to the C++ standard. (34010071).

```
class Continuation {
   std::function<Continuation ()> m_next;
};
```
- When the Symbols Hidden by Default build setting is enabled (`-fvisibility=hidden`) and a symbol declaration includes an availability attribute with a macOS availability such as `API_AVAILABLE(macos(10.12), ios(10))`, then the symbol’s visibility is set to `default` instead of `hidden`. (33655115)

  _Workaround:_ Use `__attribute__((visibility("hidden")))` in addition to `API_AVAILABLE` to hide a declarations.

- Vector parameter return values for an Objective-C method with a target earlier than macOS 10.11 or iOS 9 are no longer valid. (21662309)

- Asset catalogs now support named colors that can be used in source files and Interface Builder. (28900538)
- Asset catalogs now support high-efficiency image formats, including files with the `.avci`, `.heic`, and `.heif` file extensions. (29959599)

- WatchKit App Store icons in the asset catalog are not uploaded when using Xcode to submit an app to the App Store. (33383969)

  _Workaround:_ Use the iTunes Connect web app to upload WatchKit App Store icons.
- App store icons for tvOS include an unused slot for a 2x version of the icon. Any images in this slot are ignored. (33800909)
- Apple TV 4K apps must include a 2x launch image to run at the higher resolution. (33968521)

- Xcode 9 includes a new build system written from scratch in Swift. It is designed for higher reliability, and it catches project configuration problems that the standard build system does not. The performance of the build system (not including compilers, linkers, and other build tools) has been dramatically improved. This new build system is built on top of the Swift open source [llbuild project](https://github.com/apple/swift-llbuild).

  In Xcode 9.0, the new build system is disabled by default. To enable the new build system, choose File > Project Settings or File > Workspace Settings, and then choose New Builds System for the Build System option in the menu. For a command-line build, pass the `-UseNewBuildSystem=YES` flag to `xcodebuild`. The new build system will become the default build system in a future version of Xcode. (19209225)

  Although the new build system is highly compatible with existing projects, some projects may require changes due to the following:

  - The new build system has stricter checks for cycles between elements in the build in order to prevent unnecessary rebuilds. To resolve the issue, make sure that any generated files are produced before they are required. For example, if a target both produces an output and depends on other targets that use the output, move the production of the output into its own target and run that target earlier in the build.
  - It is an error for any individual file in the build to be produced by more than one build command. For example, if two targets each declare the same output file from a shell script phase, factor out the declaration of the output file into a single target.
  - If an output file which is generated by a shell script is used as an input elsewhere in the build (for example, to another shell script), then that output must be declared as an explicit output by the script that generates it; otherwise the build system may attempt to search for the file before it has been generated, causing the build to fail.
  - The traditional header map that was generated when the Always Search User Paths (`ALWAYS_SEARCH_USER_PATHS`) setting was `YES` is not supported by the new build system. Instead, set `ALWAYS_SEARCH_USER_PATHS` to `NO` and migrate to using modern header include syntax.

    - Add any needed header files that are in the project repository to the Xcode project to ensure they are available for use in `#include` (via the project wide header map).
    - Use quote-style include ("`foo.h`") for project headers, and reserve angle-bracket include (<`foo.h`>) for system headers.
  - The new build system passes `undefined_arch` as the value for the `ARCH` environment variable when running shell script build phases. The value was previously not well defined. Any shell scripts depending on this value must behave correctly for all defined architectures being built, available via the `ARCHS` environment variable.
  - The new build system supports the “clean build folder” behavior. The standard “clean” behavior is not supported.
- For a target containing Swift and defining a module, the generated `module.modulemap` file now includes `requires objc` so it can be used by languages other than Objective-C (such as C++). (28650820)
- The new Strip Swift Symbols (`STRIP_SWIFT_SYMBOLS`) build setting is enabled by default. It adjusts the level of symbol stripping so that when the linked product of the build is stripped, all Swift symbols are removed. This significantly reduces the size of Swift frameworks. If the lack of Swift symbols causes problems, such as when using `dladdr()`, this setting can be disabled. To view the exported symbols from file that has been stripped, use `xcrun dyldinfo -export` instead of `nm`. (31306055)
- A scheme with code coverage enabled for the test action now enables code coverage for the run and analyze actions, reducing the need to build multiple versions of the application. To turn off code coverage for all actions other than test, use a separate scheme for those actions with code coverage disabled. (31848014)
- Added Precompile Bridging Header (`SWIFT_PRECOMPILE_BRIDGING_HEADER`), a new build setting for the Swift compiler. This setting is enabled by default and adds a new optional step in mixed-source builds called `PrecompileSwiftBridgingHeader`, that improves overall build time. If unexpected errors occur during this step, disable this build setting to omit the optional step. (31851450)
- Added Swift 3 @objc Inference (`SWIFT_SWIFT3_OBJC_INFERENCE`), a new build setting that controls how the Swift compiler infers `@objc` for declarations. By default the compiler uses the declared Swift version in the target to perform the inference. The new setting can be used to explicitly direct the Swift compiler to use either Swift 3 to Swift 4 inference rules. (32121595)
- An autocreated scheme is saved to disk only if it has been edited. This helps prevent the accumulation of schemes for targets which were deleted, or are added to other schemes. (30266825)
- For targets that use automatic signing, `xcodebuild` can now communicate with the Apple developer website to create and update provisioning profiles, signing certificates, and app IDs. To enable this behavior, choose Xcode > Preferences and add your Apple ID in the Accounts pane, and then pass the `-allowProvisioningUpdates` flag to `xcodebuild` when building your target. (27572834)
- Added `CODE_SIGN_STYLE`, a build setting used to override a target’s signing style to Automatic or Manual when using `xcodebuild`. (28077832)

- When a project is opened, Xcode may create a Recovered References group in the Project navigator. This group contains files that are referenced in a target but aren't referenced in the group tree of the project. If the group appears, move each file to the proper location in the project as appropriate. (22924751)
- Changed the name of the build intermediates folder to `Intermediates.noindex`. This improves build times by preventing Spotlight from indexing the folder. (29336306)
- Xcode supports static library targets which contain Swift code. Debugging applications that use Swift static libraries may require a complete set of build artifacts that are in their original location. (33297067)

- When using the new build system, it is not possible to use the clean action in a project or workspace that uses the legacy or custom locations for derived data. (32296417)
- Products built with code coverage enabled should not be submitted to the app store. Code coverage is disabled automatically when performing the `archive` scheme action. It is not recommended to distribute or submit apps built with the `run` action; if your workflow involves submitting a product built with the `run` action, you should switch to submitting the product of the `archive` action. The `run` action is the default action performed by `xcodebuild` when `-scheme` is passed with no explicit verb, or with the `build` verb; use the `archive` verb to build with the `archive` action. (32870905)
- The new build system may not define all of the environment variables that the standard build system defines when launching shell scripts. If the new build system is not supplying an environment variable that your scripts use, please file a bug at https://bugreporter.apple.com with the name of the environment variable, the expected value in the old build system, and a brief explanation about what you are using the variable for. (24541618)
- When using the new build system and using DWARF with dSYM File debugging information, the build may do unnecessary work to extract the dSYM on each build iteration, degrading build performance. (30668974)

  _Workaround:_ Enable DWARF with dSYM File only for the Release configuration.
- With the new build system, switching between building the Debug and Release configuration of a project may result in unnecessary content rebuilding. (30924058)
- For single files, the new build system does not yet support the Compile, Analyze, Preprocess, or Assemble operations of the Product > Perform Action submenu. (31072405)
- When using the new build system, Interface Builder live views use the old build system. (31433718)
- Projects using on-demand resources are not currently supported by the new build system. (31508570)
- When using the new build system, the total number of build tasks reported in the activity area may not be computed correctly, and will continue to increase during the build. (31855141)

- The build setting Separate Strip (`SEPARATE_STRIP`) is no longer supported nor is it displayed in the build settings editor. Xcode always strips binaries in a separate task and no longer instructs the linker to perform the strip. (31584192)

- Data models generated in projects that use Swift 4 use Swift structures when possible. Data models generated in projects using Swift 3 are unchanged. (27512827)
- Updated the model editor to present a unified interface for Core Data’s fetch indexes, property index, and entity compound indexes. Older data models are translated into fetch index form, and saved to the old file format when necessary. Compiling a data model for a target lower than iOS 11, watchOS 4, macOS 10.13, or tvOS 11 continues to generate a compatible model. (30843153)
- Added a flag to the model editor for marking an attribute as preserved after deletion, to support persistent history tracking. (31204966)
- Added support to the model editor for setting an entity's Core Spotlight display name expression. (31619747)
- Added support to the model editor for creating fetch indexes from attributes, expressions, and relationships. (32407895)

- The Crashes Organizer symbolicates unsymbolicated logs, if they are selected using a local .dSYM indexed by Spotlight. (22550064)

- Added a number of fixes to increase the stability, reliability, presentation, performance, of the Crashes Organizer. (29500046)

- Added wireless debugging for iOS and AppleTV. (10968305)
- Added support for SpriteKit and SceneKit to the visual hierarchy debugger. SpriteKit nodes appear as views. SceneKit views open a snapshot in the SceneKit editor. Changes made to the editor can be saved and don't change the app. (29169315)
- Added allocation backtraces to saved memory graph files exported by Xcode or generated by the `leaks` command line tool. Saving backtraces requires that malloc stack logging is enabled for the target. (25399716)

- The Xcode Memory Debugger, Leaks instrument, and `leaks` command line tool should no longer report false positive leaks of small malloc blocks related to the use of weak references in process that use Swift. (29780048)

- GPU performance counters are not available on devices with A7 or A8 processors. (32982421)
- Removing a wireless development pairing from a device requires resetting the network settings by choosing Settings > General > Reset > Reset Network Settings. (31626631)
- In the GPU Frame Debugger, argument encoders created before the start of a frame capture result in the app crashing while capturing. (32415645)

  _Workaround:_ Create argument encoders within the captured workload, or release them before capturing.

- In the Devices pane of the Devices and Simulators window, the button to show the debug console for a paired Apple Watch now shows correctly when an iPhone with a paired watch is selected. (32365458)

- Instruments can’t wake a sleeping device over a network. (33384362)

  _Workaround:_ Wake the device manually or by building and running the app.
- After installing Xcode, the first time an app is run in Simulator the memory graph debugger and Instruments display no data. (34172871)

  _Workaround:_ Reboot the Mac.

- Added the Layout Margins option in the Size inspector to enable specifying custom margins. For more information, see [Positioning Content Within Layout Margins](https://developer.apple.com/documentation/uikit/uiview/positioning_content_within_layout_margins). (30086042)
- Added support for the vertical baseline-to-baseline constraint added in iOS 11. (30086144)
- Safe Area layout guides can be enabled for any subview and for XIB files. (32956031)
- Interface Builder renders navigation bars, tab bars, and toolbars on the canvas as they appear on a device at runtime. (30983209)
- To use the new `usesAutomaticRowHeights` property of `NSTableView` in Interface Builder, choose Automatic (Auto Layout) from the Size inspector, and then set a value for Row Height. This value is used by AppKit as part of the auto layout calculation. (29511510)
- Added estimated row, header, and footer heights to the Size inspector in Interface Builder. These properties are used by UIKit to create self-sizing table cells by setting the estimated height to a value other than zero. (17995201)
- Files created with Interface Builder files use the new safe area layout guide instead of top and bottom layout guides. Constraints that use the safe area are automatically converted to use top and bottom guides when deployed to a version of iOS or tvOS that doesn't support the new safe area guide. To enable the safe area guide in existing files, select the view controller or view, open the File inspector, and enable Use Safe Area Layout Guides. (29323293)
- Interface Builder allows configuring the column sizing properties of `UISplitViewController`. (18359423)
- Interface Builder supports setting `textContentType` on classes conforming to the `UITextInputTraits` protocol. On iOS 11, this improves the ability of AutoFill to populate with appropriate data including the Username and Password. (25019432)

- When landscape is chosen from the Device configuration pane, Interface Builder now shows the correct height for the status, top, and bottom bars. In addition, `IBDesignable` views receive the the correct values for the current trait collection. (6799670)
- When Vary for Traits mode is active, choosing Clear Constraints and Reset to Suggested Constraints affects only the active configuration. (27407689)
- Fixed drawing issues that occurred when resizing the Interface Builder document outline view. (32137309)
- Connecting outlets and actions to a Swift protocol-typed class now works correctly. (17023935)
- Outlets, actions, and inspectable properties declared in classes that have a Swift protocol extensions now work correctly. (22201035)
- Objective-C annotations such as `NS_REFINED_FOR_SWIFT` no longer prevent using `IBInspectable` with a property. (30509152)
- Compiling a macOS storyboard with an `NSTableView` that uses Cocoa Bindings, no longer results in `ibtool` hanging. (18867270)

- Using a Swift image literal within `prepareForInterfaceBuilder()` causes `IBDesignablesAgentCocoaTouch` to crash because live views are compiled in a different bundle. (28676479)

  _Workaround:_ Use `UIImage(named:inBundle:compatibleWithTraitCollection:)` for all image lookups, and use `Bundle(for: type(of: self))` to find the bundle for the live view class.
- The navigation bar doesn't shrink when scrolling view content if Prefers Large Titles is set for the navigation controller's navigation bar, or is set on the storyboard. (33229609)

  _Workaround:_ Add the following to the root view controller’s `awakeFromNib` method:

```
self.navigationController?.navigationBar.prefersLargeTitles = false
self.navigationController?.navigationBar.prefersLargeTitles = true
```

```
self.navigationController.navigationBar.prefersLargeTitles = NO;
self.navigationController.navigationBar.prefersLargeTitles = YES;
```


- Interface Builder no longer compiles for targets targeting iOS 6 or earlier. Opening an Interface Builder document with an older deployment target converts them to iOS 7 and later. (28726486)

- Added support to XLIFF for exporting and importing `stringsdict` files, including support for using the correct per-language plural variants. (16785521)
- Added support for XLIFF export of encodings other than UTF-8. (18944510)
- Xcode no longer exports localizations for test targets that don't contain their own localized resources. (16813531)

- Exporting a localization that contains a localized resource that is a duplicated in more than one target no longer results in an error. The duplicated resource is exported only once. (19059103)
- Xcode now uses `\n` and `\t` to represent newline and tab characters in generated strings files. (22981479)
- Strings files with line endings other than the standard linefeed character now work correctly for both import and export. (30552675)

- Added Main Thread Checker, a new runtime tool that finds calls to APIs in AppKit, UIKit, and WebKit that must be made from the main thread, but are made on other threads. These calls are reported as runtime issues. Main Thread Checker is automatically enabled during debugging and can be disabled in the Diagnostics tab of the Scheme editor. (29951764)

- macOS playground execution may hang in the Running state with no results produced. This is more prevalent when changing pages. (32429211)

  _Workaround:_ Stop playground execution and rerun. If issue persists, close and reopen Xcode.
- The `liveTouchBar` property of `PlaygroundSupport` is not supported. (31073754)

- Groups in the Project Navigator are now more closely associated with directories in the file system. (28612132)

  - Dragging files between groups in the Project Navigator moves the files in the filesystem and updates any associated SCM working copies.
  - When a group is connected to folder in the filesystem, creating, renaming, and deleting groups updates the corresponding files and folders in the the filesystem.
  - To remove a connection between a group and a folder in the filesystem, select the group, and then open the File inspector and click on the on the Clear path button (X).
  - To add or update an association from a file or a folder in the filesystem to a file or a group in the project, select the file or group, open the File inspector, and drag the corresponding file or folder onto the Location section in the File inspector.

- Renaming files no longer results in the error alert `The file has been saved by another application`. (31968242)

- Dragging a file into a project from the Finder may move or copy the file in the Finder. (31042020)

  _Workaround:_ Create a reference to the file by Command-Option dragging the file into the project.

- Adding protocol stubs by applying the Fix for “Do you want to add protocol stubs?” may not insert all the parts of a complex protocol such as `Swift.Collection`. (31078629)

  _Workaround:_ Use the Fix button and then add any missing protocol stubs.
- Constructors for locally defined types, such as a structure defined inside a function body, cannot be refactored. (31695776)
- When extracting a code snippet that uses a locally defined type the extracted function may use that locally defined type as a parameter, resulting in code that does not compile. An example of a locally defined type, is an enumeration defined in a function body. (32288968)
- Renaming does not affect symbols found inside macro expansions. (31989492)
- Renaming Swift enumeration cases with associated values doesn't rename their argument labels. (32126363)
- Renaming a Swift class or protocol exported to Objective-C doesn't rename any references that use a forward `@class` declaration in a source file that doesn't include the generated `MODULE-Swift.h` header. (32275117)

  _Workaround:_ `#include` the generated `MODULE-Swift.h` header in your `.m` file.
- Renaming a call or reference to a member-wise initializer does not rename the corresponding member properties. (32383812)

  _Workaround:_ Manually rename member properties from their definition or references.
- Undo does not work while renaming. (32429491)

  _Workaround:_ Manually edit the new name, or use Cancel.

- Revised the distribution workflows. (29054761)

  When a new distribution signing certificate is required, Xcode prompts for permission. Signing certificates can be exported for sharing with other team members. Revoking distribution signing certificates is no longer supported by the distribution workflow. Specifying a team is no longer required when the app is signed when the archive is built.

  Added manual signing support to the Xcode distribution methods. You can now specify manual signing assets when exporting or uploading your app. Profiles that are created manually are not modified by Xcode or `xcodebuild`.

  In Xcode, exporting an app now exports a distribution summary property list file, a packaging log, and an export options property list file. The distribution summary property list file describes the content of the exported app, including signature information, symbol and bitcode settings, and the embedded content. The package log contains all of the commands used to transform the archived application into a distributable packaged app.

  The export options property list file includes all of the choices made during the distribution workflow and can be passed to `xcodebuild` using the `-exportOptionsPlist` flag. The property list file includes new properties (`signingStyle`, `signingCertificate`, and `provisioningProfiles`) for specifying manual signing. See `xcodebuild -help` for the full list of supported `ExportOptions` keys.

  Added support for automatic signing to `xcodebuild` using the `-allowProvisioningUpdates` and `-allowProvisioningDeviceRegistration` flags.

  Added development and distribution signing flows to continuous integration. Bots can development-sign apps to run on multiple connected devices. For automatic signing, bots can register connected devices and update Xcode-managed profiles but not create distribution certificates.
- Enabling code coverage for the Test action of a scheme also enables it for the Run action. This results in saving the build intermediates and products from both actions in the location used by the Run action. (32079317)
- Added a Strip Swift Symbols option that controls stripping Swift symbols from the Swift standard library. For more information, see New Features in Building and Linking and the Strip Swift symbols topic in Xcode Help. (31669406)

- Added face-up and face-down orientations for supported devices. (11393667)
- Updated Simulator to save screenshots to the system screenshot directory instead of always saving screenshots to the desktop. (26127809)
- Added the ability to attach to a simulated device started from the command line and to close a simulated device window without shutting down simulator. To leave a device running, hold down the Control key when closing a window or quitting the app, and then click the Keep Running button in the dialog that appears. Select the checkbox to make this the default action when closing or quitting. (31004084)
- Add a Share Extension for importing items into simulators:

  - Photos and videos are imported into the photo library of a device.
  - Locations or pins from Maps.app set the device’s simulated location.
  - App bundles are installed.
  - URLs are opened in Safari.

  Choose All Simulators to install the item to all open simulators. (31150602)
- Added support for selecting the macOS audio input and output device for each simulated device by using the Hardware > Audio Input and Hardware > Audio Output menus. To use the Mac input or output device selected in System Preferences, choose System from the menu.

  Selecting Bluetooth headphones may decrease the audio quality by placing the headphones in call mode. If that occurs, select a different device. (32337249)
- Added support for starting multiple simultaneous devices to Simulator and remove the separate Simulator (Watch) app. (5687722)
- Added a bezel to simulated devices. The buttons on the bezel send the appropriate event to the simulated device. The bezel supports moving the simulated device window and device gestures originating at the edge of the screen. Clicking and dragging away from the simulated screen moves the the window. Moving towards the simulated screen performs a gesture. (14020158, 31558767, 32061265, 32118310)
- Added redirection of keyboard shortcuts to a simulated device. Choose Hardware > Keyboard> Send Menu Keyboard Shortcuts to toggle sending shortcuts to the frontmost device. The setting can be different for each device. For more information, choose Help > Simulator Help and navigate to Interact with devices > Redirect keyboard shortcuts. (31990219)
- Updated Simulator runtimes for iOS 11 and later, tvOS 11 and later, and watchOS 4 and later to treat the filesystem as case sensitive to better simulate physical device behavior. (18609452)
- Updated Simulator to enforce background execution policies to more closely match physical devices. A backgrounded app is scheduled for execution only if it has appropriate `UIBackgroundTasks`, has a plist background mode, or receives a notification. (16532261)

- Simulator captures the output from a Siri remote paired with your Mac when there is at least one simulated Apple TV device. When the frontmost simulated device is an Apple TV, the output from the Siri remote is directed to the device, otherwise the output is ignored. Quitting Simulator returns control of the Siri remote to the Mac. (29960775)
- When launching Simulator, if an older version of Simulator is currently running, the older version hands off any running simulated devices to the newer version and then quits. (32384840)

- Running several simulators simultaneously may exceed the maximum number of processes or maximum open file limits. When this happens starting a new process, opening a new simulated device, or opening a file results in an error. Closing one or more simulated devices or closing open programs may resolve the issue.

  macOS 10.13 and later automatically scales these limits based on available system memory. The limits are fixed values on earlier versions of macOS. The limits can be increased by using `launchctl`. For more information, choose Help > Simulator Help and navigate to Troubleshoot Simulator > Insufficient resources. (31179087)
- Launching many simulated devices in rapid succession may prevent new process from spawning by using all the system resources. There may be no warning when this occurs. (31723508)

  _Workaround:_ Close Simulator windows or quit Simulator to shutdown devices for immediate recovery. Do not Force Quit Simulator as that does not shutdown the devices. For more information, choose Help > Simulator Help and navigate to Troubleshoot Simulator > Insufficient resources.
- Reducing the size of an iPhone X simulated device by dragging the bezel may trigger an edge swipe instead of resizing the device. (33974533)

  _Workaround:_ Start by increasing the window size, and then decreasing to the desired size.
- Choosing Window -> Scale -> Actual Size for a simulated iPhone X doesn't set the size correctly. (33908038)

  _Workaround:_ Manually resize the window to the correct size.
- Using `xcrun simctl uninstall` to uninstall an app in Simulator results in a failure and hangs Simulator. (30586964)

  _Workaround:_ Use `xcrun simctl erase` to reset the device to its initial state, or delete the app from the device’s home screen in Simulator.
- When using `AVPlayerViewController` in an iPhone X simulated device, video may appear outside of the safe area and be obscured by the sensor housing or rounded corners. (34339660)

- The Source Control pane in Preferences now supports configuring Git author information, Git ignore file lists, and SVN ignore file lists. (10544339)
- Updated the Accounts pane in Preferences to support integration with GitHub. As part of this update, repositories added in previous versions of Xcode are no longer available. Use Source Control > Clone to access a repository. Repositories for GitHub and GitHub Enterprise accounts registered in Xcode appear in the clone window. Other repositories can be accessed by entering the repository URL. (30191709)
- Added support for configuring two-factor authentication and an SSH key to GitHub accounts to the Accounts pane in preferences. The credentials are used when performing source control operations. (28775680)
- Added a Clone window that integrates directly with GitHub to show you the favorite, private, personal and organizational repositories for all of your accounts. Each repository, shows the metadata, project readme, and an option to create a local clone of the repository. (30960520)
- Added a new Source Control navigator for viewing the working copies in the project or workspace. The navigator lists branches, tags, and remotes as well as push and pull counts. (29054970)

  The contextual menu in the navigator includes the ability to:

  - Create branches and tags.
  - Configure remotes.
  - Checkout a revision number.
  - Merge changes between branches.
- Added a history editor for viewing the full history of a branch or tag. Each commit includes the author, commit comments, and any branches or tags that are part of the commit. Clicking on a branch or tag in the Source Control navigator to show the history. (29054970)
- Added a review files editor to show the changes made to the files in a commit. (29054970)
- Added a Source Control inspector to show more details of a commit. (29054970)
- Updated Xcode to fetch remote tracking branches automatically, mark updated files in the project navigator, and show push and pull counts in the Source Control navigator. (31839384)
- github.com added support for one-click clone to Xcode from a repository in a web browser. (32294826)

- When performing certain source control operations, such as a pull, the latest updates may not appear in the history view. (33919644)

  _Workaround:_ With the history view open, choose the Editor > Refresh History.
- Removing the keychain credentials for a GitHub account added in Xcode using a tool other than Xcode prevents Xcode showing an authentication error. (33898250)

  _Workaround:_ Delete the GitHub account in Xcode and then add it.

- Subversion integration will be deprecated in a future release. (33041914)

- Command-plus (+) and Command-minus (-) now increase and decrease the size of the font in the source editor. (21423189)
- Typing a opening delimiter in selected text adds a matching closing delimiter at the end of the selection. Auto-matched delimiters include double-quotes (`"`), parenthesis ("`(`" and "`)`"), square brackets (`[` and `]`), and braces (`{` and `}`). (29164633)
- The comment and uncomment functionality now works correctly with languages that support nesting block comments, such as Swift, and with others that don't, such as C. This results in more accurate commenting and uncommenting. (32193940)

- Using VoiceOver to drag a connection from Interface Builder to the source editor sometimes fails to create the connection. (33198923)

  _Workaround:_ Declare the `IBAction` or `IBOutlet` in the source editor, and then drag the connection from the source editor to Interface Builder.

- Updated Xcode to support both Swift 4.0 and Swift 3.2. The language mode is controlled by the Swift Language Version build setting. These two language modes are implemented using the same compiler and standard library, which enables linking targets using Swift 3 with targets using Swift 4 so that, in most cases, migration from Swift 3.2 to Swift 4 can be done on a target-by-target basis.

  Although Swift 3.2 and Swift 4.0 are intended to be compatible, the differences in how they access Cocoa and Cocoa Touch APIs can lead to inconsistencies, which may limit how a library built with one version can be used by a client target built with the other. The most common issue is a member being absent from a type; in certain situations the client may be forbidden from subclassing certain classes or adopting certain protocols.

  Swift 3.2 and Swift 4.0 do not support linking with targets compiled with versions of Swift earlier than 3.2.

  As usual, if the compiler or SourceKit crashes, please file a bug report with your project and sources attached. If you are mixing Swift 3 and Swift 4 in your project, please mention that in the description of the issue. (31104045)
- It is now an error to perform a second access to a variable while it is being modified. Such accesses lead to code that is hard both for programmers and the compiler to understand. In general, you need to rearrange your code (for example, by making a local copy) to prevent conflicting accesses.

  For example, the following code attempts to read from the variable array while the `sort()` method is mutating it.

```
var array: [Int] = ...
array.sort { $0 < array[0] }  // Error
```

  This rule is enforced by a combination of compile-time and run-time checks.

  Static checks are used for most local variables, constants, and parameters. In Swift 4 mode, static failures are compile-time errors. In Swift 3 mode, static failures are a warning, but this will be strengthened to an error in a future release of Swift, so you should fix these warnings.

  Dynamic checks are used for global variables, static type properties, class instance properties, and local variables that have been captured in an `@escaping` closure. In Swift 4 mode, failing a dynamic check causes a trap at runtime, much like integer overflow does. In Swift 3 mode, failing a dynamic check causes a warning to be printed to stderr.

  The compile-time and runtime checks enforce the rule for accesses that occur within the same thread. Thread Sanitizer can catch most (but not all) violations that occur from different threads.

  The common idiom of exchanging two elements of a collection using swap violates this rule. To support this pattern, there is now a `swapAt(_:_:)` method on all mutable collections. ([SE–0176](https://github.com/apple/swift-evolution/blob/master/proposals/0176-enforce-exclusive-access-to-memory.md))
- In Swift 4.0, extensions that are in the same file and that extend the same type share an access control scope. If the type that they extend is also in the same file, they share its access control scope. This means that private members declared in the type’s declaration can be accessed from extensions, and private members declared in one extension can be accessed from other extensions and from the type’s declaration. ([SE–0169](https://github.com/apple/swift-evolution/blob/master/proposals/0169-improve-interaction-between-private-declarations-and-extensions.md))
- You can now write multiline string literals. A `"""` followed by a new line starts the literal, and a `"""` on a new line ends it. Every line after the initial quote must start with the same whitespace as the closing quote, which will be stripped out on compilation. ([SE–0168](https://github.com/apple/swift-evolution/blob/master/proposals/0168-multi-line-string-literals.md))
- SQLite APIs can now be imported into Swift under the module name `SQLite3`. (18640410)
- In Swift 4.0, if an Objective-C class has a designated initializer that can’t be imported into Swift, any Swift subclasses of that class will not inherit any convenience initializers. (31563662)
- All Core Foundation types implicitly conform to the `Equatable` and `Hashable` protocols in Swift 3.2 and 4.0. ([SR–2388](https://bugs.swift.org/browse/SR-2388))

  If you were previously adding these conformances in an extension, conditionalize the extension by using the following pattern:

```swift
#if swift(>=3.2)
   // Equatable and Hashable are provided by Swift.
#else
   extension TheCFTypeICareAbout: Hashable {
      static func ==(left: TheCFTypeICareAbout, right:
         TheCFTypeICareAbout) -> Bool {
            return CFEqual(left, right)
         }
         var hashValue: Int {
            return CFHash(self)
         }
      }
#endif
```
- Subscript declarations can now be defined to have generic parameter lists. ([SE–0148](https://github.com/apple/swift-evolution/blob/master/proposals/0148-generic-subscripts.md))

```
extension MyContainer {
   subscript<T: MyKeyConvertible>(key: T) { ... }
}
```
- Protocol composition types can now contain one or more class type terms, forming a class-constrained protocol composition. ([SE–0156](https://github.com/apple/swift-evolution/blob/master/proposals/0156-subclass-existentials.md))

```swift
protocol Paintable {
   func paint()
}

class Canvas {
   var origin: CGPoint
}

class Wall : Canvas, Paintable {
   func paint() { ... }
}

func render(_: Canvas & Paintable) { ... }

render(Wall())
```

  Class-constrained protocol compositions can be written and used in both Swift 3 and Swift 4 mode.

  Generated headers for Swift APIs map class-constrained protocol compositions to Objective-C protocol-qualified class types in both Swift 3 and Swift 4 mode — for example, `NSSomeClass & SomeProtocol & OtherProtocol` in Swift becomes `NSSomeClass <SomeProtocol, OtherProtocol>` in Objective-C. Similarly `UIViewController<UITableViewDataSource, UITableViewDelegate>` in Objective-C becomes `UIViewController & UITableViewDataSource & UITableViewDelegate` in Swift.

  Objective-C APIs that use protocol-qualified class types differ in behavior when imported by a module compiled in Swift 3 mode and Swift 4 mode. In Swift 3 mode, these APIs will continue to import as protocol compositions without a class constraint — for example `SomeProtocol & OtherProtocol`. In Swift 4 mode, protocol-qualified class types import as class-constrained protocol compositions, for a more accurate mapping of APIs from Objective-C to Swift.

  The current implementation of class-constrained protocol compositions lacks three features outlined in the Swift evolution proposal:

  - In the evolution proposal, a class-constrained protocol composition is permitted to contain two different classes as long as one is a superclass of the other. The current implementation only allows multiple classes to appear in the composition if they are identical.
  - In the evolution proposal, associated type and class inheritance clauses are generalized to allow class-constrained protocol compositions. The current implementation does not allow this.
  - In the evolution proposal, protocol inheritance clauses are allowed to contain a class, placing a requirement that all conforming types are a subclass of the given class. The current implementation does not allow this.

  These missing aspects of the proposal can be introduced in a future release without breaking source compatibility with existing code.
- A new family of integer protocols enables more generic algorithms:

  - `Numeric`, types that support arithmetic operators
  - `BinaryInteger`, integer types that have a binary representation and support bitwise operations
  - `FixedWidthInteger`, integer types that use a fixed size and support the concept of arithmetic operations that report overflow

  Heterogeneous comparisons are now allowed, eliminating the need for `numericCast(_:)` in comparisons. For example, `(42 as UInt) > (0 as Int)` works.

  With the introduction of smart shifts, it’s possible to shift a value by a negative amount, or to shift by a value of a different integer type without calling `numericCast(_:)`. The result type is the type of the shifted value.

  `toIntMax()` and `init(_:IntMax)` have been deprecated – `numericCast` converts directly between different integer types without going through the maximum width integer. ([SE–0104](https://github.com/apple/swift-evolution/blob/master/proposals/0104-improved-integers.md))
- `Sequence` has an associated type `Element` that is equivalent to `Iterator.Element`. The value of this associated type can be inferred from existing `Sequence` conformance. Code that already declares a type of `Element` may need to be altered to resolve conflicts. (32186094)
- Slicing a raw buffer no longer results in the same raw buffer type. Specifically, `UnsafeBufferPointer.SubSequence` now has type `RandomAccessSlice<UnsafeRawBufferPointer>` with the same changes for the mutable version. Therefore, indexing into a raw buffer slice is no longer zero-based. This is required for raw buffers to fully conform to generic `Collection`. ([SE–0138](https://github.com/apple/swift-evolution/blob/master/proposals/0138-unsaferawbufferpointer.md))

  Passing a region within a buffer to another function that takes a buffer can no longer be done via subscript. This now requires explicit initialization, using a `rebasing:` initializer, which converts from a slice to a zero-based `Unsafe[Mutable]RawBufferPointer`:

```
takesRawBuffer(buffer[i..<j])  // Incorrect
takesRawBuffer(UnsafeRawBufferPointer(rebasing: buffer[i..<j]))  // Correct
```

  Subscript assignment can no longer be done directly from a buffer. This now requires creation of a slice from the complete source buffer:

```
buffer[n..<m] = smaller_buffer  // Incorrect
buffer[n..<m] = smaller_buffer.[0...]  // Correct
```

  The slice type of `UnsafeRawBufferPointer` no longer has a nonmutating subscript setter. So assigning into a mutable `let` buffer no longer compiles. The assigned buffer slice now needs to be a `var`.

```
// Incorrect
let slice = buffer[n..<m]
slice[i..<j] = buffer[k..<l]

// Correct
var slice = buffer[n..<m]
slice[i..<j] = buffer[k..<l]
```
- A dictionary can be created from a sequence of keys and values, and can merge keys and values into an existing dictionary. ([SE–0165](https://github.com/apple/swift-evolution/blob/master/proposals/0165-dict.md))

```
let asciiTable = Dictionary(uniqueKeysWithValues: zip("abcdefghijklmnopqrstuvwxyz", 97...))
// ["w": 119, "n": 110, "u": 117, "v": 118, "x": 120, "q": 113, ...]

let vegetables = ["tomato", "carrot", "onion", "onion", "carrot", "onion"]
var vegetableCounts = Dictionary(zip(vegetables, repeatElement(1, count: Int.max)), uniquingKeysWith: +)
vegetableCounts.merge([("tomato", 1)], uniquingKeysWith: +)
// ["tomato": 2, "carrot": 2, "onion": 3]
```
- Filtering a set of a dictionary produces a result with the same type as the receiver. To transform the values of a dictionary, keeping the same keys, use the `mapValues(_:)` method. ([SE–0165](https://github.com/apple/swift-evolution/blob/master/proposals/0165-dict.md))

```swift
let vowels: Set<Character> = ["a", "e", "i", "o", "u"]
let asciiVowels = asciiTable.filter({ vowels.contains($0.key) })
asciiVowels["a"]  // 97
asciiVowels["b"]  // nil

let asciiHexTable = asciiTable.mapValues({ "0x" + String($0, radix: 16) })
// ["w": "0x77", "n": "0x6e", "u": "0x75", "v": "0x76",  "x": "0x78", ...]
```
- When using a key as a dictionary subscript, a default value to be returned can be supplied if the key is not present in the dictionary. ([SE–0165](https://github.com/apple/swift-evolution/blob/master/proposals/0165-dict.md))

```
for veg in ["tomato", "cauliflower"] {
    vegetableCounts[veg, default: 0] += 1
}
// ["tomato": 3, "carrot": 2, "onion": 3, "cauliflower": 1]
```
- Added an `init(grouping:by:)` initializer to `Dictionary` that converts an array or other sequence into a dictionary, grouped by a particular trait. ([SE–0165](https://github.com/apple/swift-evolution/blob/master/proposals/0165-dict.md))

```
let buttons = ...  // an array of button instances
let buttonsByStatus = Dictionary(grouping: buttons, by: { $0.isEnabled })
// How many buttons are enabled?
print("Enabled:", buttonsByStatus[true]?.count ?? 0)
```
- `Dictionary` and `Set` have a visible `capacity` property and a `reserveCapacity(_:)` method similar to `Array`, and a dictionary’s keys and values properties are represented by specialized collections. ([SE–0165](https://github.com/apple/swift-evolution/blob/master/proposals/0165-dict.md))
- Added a new `Substring` type to Swift 4 that is returned when slicing a `String`. ([SE-0163](https://github.com/apple/swift-evolution/blob/master/proposals/0163-string-revision-1.md))

  In Swift 3.2, slicing a `String` continues to return a `String`, but you can provide type context to get a `Substring` — for example, `myString[i...] as Substring`.

  `Substring` presents an almost-identical API as that of `String`. A new protocol, `StringProtocol`, is available to write generic code that applies to either `String` or `Substring`.
- `String` now conforms to `BidirectionalCollection` and `RangeReplaceableCollection`. ([SE-0163](https://github.com/apple/swift-evolution/blob/master/proposals/0163-string-revision-1.md))
- A new `RangeExpression` protocol is now used to unify all range types (such as `CountableRange` and `ClosedRange`), and new one-sided ranges (such as `PartialRangeUpTo`) have been added. ([SE-0172](https://github.com/apple/swift-evolution/blob/master/proposals/0172-one-sided-ranges.md))

  Any type that conforms to `RangeExpression` can now be used to slice a collection.

```
let numbers = [10, 20, 30, 40, 50, 60]
if let i = numbers.index(of: 40) {
    print(numbers[..<i])
}
// Prints "[10, 20, 30]"
```

  Countable partial ranges can be used as sequences.

```
let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
let asciiTable = zip(65..., alphabet)
for (code, letter) in asciiTable {
    print(code, letter)
}
// "65 A"
// "66 B"
// "67 C"
// ...
// "89 Y"
// "90 Z"
```
- `NSNumber` is stricter about the result of bridging some of its values to corresponding Swift value types.

  Specifically, using an `as?` cast returns `nil` if the value stored by `NSNumber` does not fit into the requested Swift value type. For example, `NSNumber(2) as? Bool` returns `nil`, but `NSNumber(1) as? Bool` returns `true`.

  To ignore this behavior and force a cast, use the appropriate conversion method on `NSNumber` instead. For example, `myNumber.boolValue`. ([SE–0170](https://github.com/apple/swift-evolution/blob/master/proposals/0170-nsnumber_bridge.md))
- The archival and serialization API is built in to Swift, with a focus on type-safe conversions from external formats directly into native Swift types, and interoperability with common formats like JSON and property list. The `Encodable` and `Decodable` protocols (along with `Codable`, which implies both), allow types to participate in encoding and decoding mechanisms. ([SE–0166](https://github.com/apple/swift-evolution/blob/master/proposals/0166-swift-archival-serialization.md))

  Many of the basic data types conform to `Codable`. Custom data types whose members all conform to `Codable` can use a compiler-generated implementation of these protocols by declaring protocol conformance.

```swift
public struct Person: Codable {
    let name: String
    let email: String
}
```
- Updated `Encoder` and `Decoder` for type-safe conversion to and from the JSON and property list formats. Combined with the default `Codable` implementation, many types can natively convert to and from these formats, with no additional encoding or decoding work. ([SE–0167](https://github.com/apple/swift-evolution/blob/master/proposals/0167-swift-encoders.md))

```
import Foundation

let johnny = Person(name: "Johnny Appleseed", email: "johnny_appleseed@apple.com")
let encoder = JSONEncoder()
let data = try encoder.encode(johnny)
// data is {"name": "Johnny Appleseed", "email": "johnny_appleseed@apple.com"}

let decoder = JSONDecoder()
let person = try decoder.decode(Person.self, from: data)
print(person.name)
// Prints "Johnny Appleseed"
```
- Swift 4 adds support for type-safe key path literals. They are formed using syntax that looks like this: `\BaseType.propertyName`. The backslash is important: it disambiguates between a key path to a property, and simply accessing the property. When the base type can be inferred, it can be elided producing expressions that look like: `\.propertyName`. Key path expressions produce instances from the hierarchy of `KeyPath` types listed below, where `BaseType` is the dynamic type of the base, and `PropertyType` the type of named property:

  - `KeyPath<BaseType, PropertyType>` – readonly key path
  - `WritableKeyPath<BaseType, PropertyType>` – read/write key path that can mutate a value type directly, similar to `inout` and `mutating`
  - `ReferenceWritablePath<BaseType, PropertyType>` – read/write key path that can mutate reference types

  These new key paths exist alongside the existing string `#keyPath` expressions introduced last year. `#keyPath` remains available for use with legacy `String`-based API. ([SE–0161](https://github.com/apple/swift-evolution/blob/master/proposals/0161-key-paths.md))
- In Swift 4 mode, the type system properly distinguishes between functions that take one tuple argument, and functions that take multiple arguments. ([[SE-0110](https://github.com/apple/swift-evolution/blob/master/proposals/0110-distingish-single-tuple-arg.md)])

- In Swift 4 mode, a declaration is inferred to be `@objc` where it is required for semantic consistency of the programming model. Specifically, it is inferred in the following cases:

  - The declaration is an override of an `@objc` declaration
  - The declaration satisfies a requirement in an `@objc` protocol
  - The declaration has one of the following attributes: `@IBAction`, `@IBOutlet`, `@IBInspectable`, `@GKInspectable`, or `@NSManaged`

  Additionally, in Swift 4 mode, dynamic declarations that don’t have `@objc` inferred based on the rules above will need to be explicitly marked `@objc`.
  Swift 3.2 retains the more permissive Swift 3 rules for inference of `@objc` within subclasses of `NSObject`. However, the compiler emits warnings about places where the Objective-C entry points for these inference cases are used, such as in a `#selector` or `#keyPath` expression, via messaging through `AnyObject`, or direct uses in Objective-C code within a mixed Swift and Objective-C project. The warnings can be silenced by adding an explicit `@objc`. Uses of these entry points that are not statically visible to the compiler can be diagnosed at runtime by setting the environment variable `SWIFT_DEBUG_IMPLICIT_OBJC_ENTRYPOINT` to a value between 1 and 3, and then testing the application. ([SE–0160](https://github.com/apple/swift-evolution/blob/master/proposals/0160-objc-inference.md))
- The Swift compiler diagnoses attempts to use `NSCoding` with a class that doesn’t have a simple Objective-C runtime name. The names of these classes may be affected by unrelated changes. For example, the runtime name of a private class depends on the name of the containing source file. Alternatively, use the `@objc` attribute to explicitly specify a runtime name. If you archive the class under its current “mangled” name, the compiler provides a fix-it to use it. (32314195)
- Protocols and associated types can now contain `where` clauses that provide additional restrictions on associated types. ([SE–0142](https://github.com/apple/swift-evolution/blob/master/proposals/0142-associated-types-constraints.md))

```
protocol StringRepresentable: RawRepresentable where RawValue == String {}
protocol RawStringWrapper {
    associatedtype Wrapped: RawRepresentable where Wrapper.RawValue == String
}
```
- The Swift compiler now lazily and implicitly imports outer modules when importing a submodule after Swift finishes parsing the bridging header. This is a behavior change from previous releases where the import happened eagerly. As a result, some bridging headers that might have relied on the eager implicit import (such as by directly using a type defined in the outer module) will no longer compile; they will need to either forward-declare such definitions or explicitly import the outer module. (30615193)
- In order for default argument expressions to be inlined into the caller in a future version of Swift, they must not reference any declarations that have less access than the enclosing function. (32189807)

```swift
// Before
private func computeTheBestInteger() -> Int {
    return 4
}
public func useAnInteger(_ x: Int = computeTheBestInteger().absoluteValue) {
    print(x)
}
```

  There are multiple ways to modify existing code to satisfy this condition:

  - Change the non-public reference to be public.

```swift
public func computeTheBestInteger() -> Int {
    return 4
}
public func useAnInteger(_ x: Int = computeTheBestInteger().absoluteValue) {
    print(x)
}
```
  - Add a helper function.

```swift
private func computeTheBestInteger() -> Int {
    return 4
}
public func defaultXForUseAnInteger() -> Int {
    return computeTheBestInteger().absoluteValue
}
public func useAnInteger(_ x: Int = computeTheBestInteger().absoluteValue) {
    print(x)
}
```
  - Use a sentinel value.

```swift
private func computeTheBestInteger() -> Int {
    return 4
}
public func useAnInteger(_ xOrNil: Int? = nil) {
    let x = xOrNil ?? (computeTheBestInteger().absoluteValue)
    print(x)
}
```
- The compiler can now warn about individual expressions that take a long time to type check.

  To enable this warning, go the Build Settings, Swift Compiler - Custom Flags, Other Swift Flags, and add the `-Xfrontend -warn-long-expression-type-checking=<limit>` flag, where _<limit>_ is the lower limit of the number of milliseconds that an expression must take to type check in order for the warning to be emitted.

  This allows users to identify those expressions that are contributing significantly to build times and rework them by splitting them up or adding type annotations to attempt to reduce the time spent on those expressions. (32619658)

- Swift integer values can be used as an index in a bridged `NSDictionary` with `NSNumber` keys. ([SR–3172](https://bugs.swift.org/browse/SR-3172))
- When assigning nil to a lazy property with an `ImplicitlyUnwrappedOptional` type, the value is correctly set to `nil`. (32778003)
- Covariant method overrides in classes are now fully supported, fixing many crashes and compile-time assertions when defining or calling such methods. ([SR–1529](https://bugs.swift.org/browse/SR-1529))

```swift
class Bed {}
class Nook: Bed {}

class Cat<T> {
    func eat(snack: T) {}
    func play(game: String) {}
    func sleep(where: Nook) {}
}

class Dog: Cat<(Int, Int)> {
    // 'T' becomes concrete
    override func eat(snack: (Int, Int)) {}

    // 'game' becomes optional
    override func play(game: String?) {}

    // 'where' becomes a superclass
    override func sleep(where: Bed) {}
}
```


- When the Precompile Bridging Header build setting is on, some configurations of headers in Framework targets can cause the compiler to mistakenly read a header twice, both as part of a module and as an independent, non-modular header. This can lead to warnings about duplicate Objective-C definitions, and ultimately compilation failures or compiler crashes due to incorrect cross-references between Swift module files. (33837253)

  _Workaround:_ Change the Precompile Bridging Header build setting to No for the affected target.
- If a Swift class uses a type that is newer than its deployment target in a method exposed to Objective-C, the generated `MyApp-Swift.h` header will have warnings in it about the type being “partial,” due to the Swift compiler not including availability information. (33313703)

  _Workaround:_ Turn off the `-Wunguarded-availability-new` warning whenever the generated header is included.

```c
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunguarded-availability-new"
#include "MyApp-Swift.h"
#pragma clang diagnostic pop
```
- The Swift compiler doesn't produce warnings when a method in a subclass is intended to match an optional method in a protocol adopted by the superclass. For example, if the superclass conforms to `UITableViewDelegate`, and the subclass declares a method incorrectly named `tableView(_:editingStyleForRowAtIndexPath:)` instead of `tableView(_:editingStyleForRowAt:)`, the compiler will not warn about it. Additionally, if Swift 3 style inference of `@objc` is turned off the method will not be called at run time. Make sure to check any such methods carefully. (30489065, [SR–3943](https://bugs.swift.org/browse/SR-3943))
- When the Precompile Bridging Header build setting is on, the Swift compiler will no longer automatically read a module map file that is in the same directory as the bridging header. This may lead to errors of the form `module ‘TheModule’ not found`. (32810754)

  _Workaround:_ If reading a module map from this directory is needed, add it as an explicit search path under the User Header Search Paths build setting.
- Attempting to use the Accelerate framework from Swift may generate linker errors about missing simd symbols such as `error: Couldn't lookup symbols: __T04simd6float4VN` (32457742)

  _Workaround:_ Add `import simd` to the Swift file.
- Image literals result in an immediate run-time exit when used outside the main application target. (26873717)

  _Workaround:_ Continue using `NSImage` or `UIImage` APIs to create images in non-application targets.

- The package manifest API used in a package's `Package.swift` file has been improved. Create a new package or use the package manager command `swift package tools-version --set-current` to opt into the new API. Packages can still use the previous manifest format. ([SE–0158](https://github.com/apple/swift-evolution/blob/master/proposals/0158-package-manager-manifest-api-redesign.md), [SR-3949](https://bugs.swift.org/browse/SR-3949))
- Added support for custom directory layouts for the source files in a package. Each target in a package can specify the path of the directory that contains the source files for that target. ([SE–0162](https://github.com/apple/swift-evolution/blob/master/proposals/0162-package-manager-custom-target-layouts.md), [SR–29](https://bugs.swift.org/browse/SR-29))
- Changed the default linking for C targets to static linking. Linking options are controlled in the package manifest by passing the `.static` or `.dynamic` case when specifying the type of a library product. (29730882)
- Added support for a package to explicitly declare the products that the package vends to clients. Previously, the products were inferred based on the targets in the package. ([SE–0146](https://github.com/apple/swift-evolution/blob/master/proposals/0146-package-manager-product-definitions.md), [SR–3606](https://bugs.swift.org/browse/SR-3606))
- Updated the error messages for many package manager issues to be clearer and more informative. (29772725)
- Updated the `swift package edit` command to detect dependency resolution errors before making changes by resolving package dependencies before placing the package into edit mode. (29772779)
- Package dependencies can now refer to a branch name instead of a tagged version. Use a named branch as a package dependency only when the package is closely coupled with all of its clients. Tagged versions of a package must not depend on any branches. ([SE–0150](https://github.com/apple/swift-evolution/blob/master/proposals/0150-package-manager-branch-support.md), [SR–666](https://bugs.swift.org/browse/SR-666))
- Added the `--path` option to the `swift package edit` command to support "top-of-tree" development of a related set of packages by suspending the automatic checkout management of the remote package. This enables iterating on a package and several of its dependencies without having to commit and tag those changes to see the holistic result. ([SE–0149](https://github.com/apple/swift-evolution/blob/master/proposals/0149-package-manager-top-of-tree.md), [SR–3709](https://bugs.swift.org/browse/SR-3709))
- Changed the `--branch` option of the `swift package edit` command to be optional. If no branch is provided, the Git repository is put into a "detached HEAD" state. (30120243)
- A package can declare the required minimum version of the Swift tools needed to use the package. ([SE–0152](https://github.com/apple/swift-evolution/blob/master/proposals/0152-package-manager-tools-version.md))
- Building a package on macOS only requires that the Command Line Developer Tools are installed. Previously, Xcode needed to be installed. Running unit tests still requires Xcode. (30813768)
- Updated Xcode projects generated by the package manager to use stable and readable object identifiers for objects such as targets, allowing Xcode schemes to continue referencing the same objects even when the project is regenerated with modified contents. (31019219)
- Updated the error message for unsatisfiable package dependencies to explain the dependency requirements that are in conflict. ([SR–4072](https://bugs.swift.org/browse/SR-4072), [SR–4237](https://bugs.swift.org/browse/SR-4237))
- Updated package manifest interpretation and package builds on macOS to use a sandbox, which prevents network access and file system modification. This helps mitigate the effect of maliciously crafted manifests. (31107213)
- Updated newly cloned package dependencies on macOS to use read-only file permissions, reducing the risk of unintentional changes. When a package is put into edit mode, write permission is added for the files in that package. (31286403)
- Updated the support of custom directory layouts on Linux by searching for `LinuxMain.swift` in all directory hierarchies contain a test target directory. The search continues to the package root directory. (31585721)
- Updated dependency resolution by replacing the `Package.pins` file with the new `Package.resolved` file. The new file contains resolved dependency versions enabling dependency re-resolution to occur automatically in more cases. Commit the file with the package to use the new method of dependency resolution. In addition, the `resolve` command for `swift package` replaces the `fetch` command. ([SE–0175](https://github.com/apple/swift-evolution/blob/master/proposals/0175-package-manager-revised-dependency-resolution.md))
- Added a prerelease semantic versioning component to package version tags. ([SR–1039](https://bugs.swift.org/browse/SR-1039))
- Package dependencies are now cloned in parallel by default. (32286386)
- Added the `cLanguageStandard` and `cxxLanguageStandard` properties to packages for specifying which language standard to use when compiling C and C++ targets. ([SE–0181](https://github.com/apple/swift-evolution/blob/master/proposals/0181-package-manager-cpp-language-version.md))

- Code completion now works when editing the `Package.swift` manifest in an Xcode project generated from a Swift package. (33284557)

- Creating static executables using the new option `--static-swift-stdlib` does not function correctly. (33861492)

  _Workaround:_ Build the package using the following command: `swift build -Xswiftc -static-stdlib`.

- Changed `NSFastEnumerationIterator` from a `class` to a `struct`. Existing code that works directly with `NSFastEnumerationIterator` may have to switch to using a `var` instead of a `let`. (30905263)

- Swift apps that transitively import the ModelIO framework but that do not use it will launch correctly on OS versions that do not contain the framework. (33471433)

- The following AVFoundation APIs are temporarily unavailable (34378539):

  - `AVCaptureDevice.Format.supportedColorSpaces`
  - `AVCaptureDevice.supportedFlashModes`
  - `AVCapturePhotoOutput.availablePhotoPixelFormatTypes`
  - `AVCapturePhotoOutput.availableRawPhotoPixelFormatTypes`
  - `AVCapturePhotoSettings.availablePreviewPhotoPixelFormatTypes`

- Some APIs have changed to accept `[NSAttributeKey: Any]` dictionaries instead of `[String: Any]`, such as `NSString.size(withAttributes:)` and `NSString.draw(at:withAttributes:)`. These changes may produce errors after migration is completed. (32431618)

  _Workaround:_ Change the type to match the expected parameters in the variable declaration.
- When a `Dictionary` that has an `NSAttributedStringKey` as key uses a `String` as an index, the compiler may return an error of the form: `error: ambiguous reference to member 'subscript'`. (32432013)

  _Workaround:_ Wrap the key object with `NSAttributedStringKey(rawValue: ... )`
- The migrator does not properly handle cases where an API changes nullability and the right side of an `if let` statement becomes non-optional. This will produce errors such as: error: `initializer for conditional binding must have Optional type, not '<TYPE>'`. (32476453)

  _Workaround:_ Change the `if let` statement to make it an assignment with `let` instead.

- Updated template macro expansion for new files. Improvements include:

  - Added `FILEHEADER`, a new macro for the content of a standard file header comment.
  - The contents of a macros can be defined using other macros. For example, the `FILEHEADER` macro is defined using other macros such as `FILENAME` and `COPYRIGHT`, and `COPYRIGHT` is defined using `ORGANIZATIONNAME` and `YEAR`.
  - Macro expansions can include modifiers.
  - It is possible override the default macros and to provide custom ones.

  For more information, choose Help > Xcode Help and navigate to Appendixes > Text Macros. (5775785)

- `xcodebuild` no longer launches Simulator when running tests. (27385435)
- Added a teardown block API to XCTest for cleaning up the test state after it completes. (28097197)
- Added an API to XCTest to wait on for an `XCUIElement` to exist before proceeding. (28483267)
- Added support to XCTest for targeting multiple applications in a single UI test. This includes monitoring application state and making a backgrounded application the frontmost application. (28948745)
- XCTest types that are closely associated with a particular class such as `XCUIElement.Type` are available as nested types in Swift 4. (29000570)
- Added `XCTActivity`, a new API for grouping UI test activity together in test reports and logging. (30401267)
- Added `XCTAttachment`, a new API for bundling diagnostic test resources, such as rich logging, with your test results. (30478677)
- `xcodebuild` tests on multiple destinations simultaneously by default. Use the `-disable-concurrent-testing` command line argument to disable concurrent testing. (31964004)
- Updated the save format for automatic captured screenshots to JPG. (32719585)
- Added new APIs to XCTest for managing screenshots including scheme-level configuration options for disabling automatic screenshots, and for capturing screenshots of partial, individual or multiple displays. (21327915)
- Updated UI testing to support targeting LSUIElements-based applications. (21344280)
- Increased the performance of UI testing when the application is built and installed by Xcode. Also added `firstMatch` for restricting query execution in UI tests. (29544176, 22980005)
- Added language and region specific configuration for tests the Xcode schemes. (28897796)

- `NSUInteger` in XCTest APIs is imported into Swift 4 as `Int` rather than `UInt`, bringing it into alignment with other system frameworks. (29589664)
- A test assertion during a UI test always results in XCTest capturing a screenshot. (28853076)

- Xcode does not show correct file and line information for some test failures when the tests are run in the Simulator. (33810627)
- `xcodebuild test` can intermittently fail with errors. (32881403, 32836473, 29122169, 32354498, 32852527).

  The errors include:

  - `Launch session expired before checking in`
  - `Early unexpected exit, operation never finished bootstrapping - no restart will be attempted`
  - `App accessibility isn't loaded`
  - `Domain=XCTestManagerErrorDomain Code=12 "Failed to get main window after 30 retries"`
  - `Error Domain=DTServiceHubClient Code=–11 "unable to contact local DTServiceHub to bless simulator connection"`
  - `Test runner failed to initialize for UI testing but did not provide any additional details`

  _Workaround:_ Try running the test again.
- When running a parallel test on macOS High Sierra, `xcodebuild test` can sometimes become unresponsive. (33206730)

  _Workaround:_ Cancel the test using Control-C and retry the test. Alternatively, disable parallel testing by using the `-disable-concurrent-testing` flag.
- `testmanagerd` exiting unexpectedly with an error of `Assertion failed: (staticHeader.header_magic == DTX_MESSAGE_MAGIC)` results in a running `xcodebuild test` failing. (33470538)

  _Workaround:_ Try the test again.

- Updated Thread Sanitizer to catch higher-level races on Objective-C and Swift collections, such as writing to a mutable array from different threads without using proper synchronization. (26798589)
- Updated Thread Sanitizer to catch more cross-thread violations of the Swift rule that requires exclusive access to memory. For example, when multiple threads call mutating methods on the same structure without synchronization. (30455576)

- The new build system no longer runs a shell script build phase with the legacy `COMMAND_MODE`. This results in utility programs, such as `echo`, conforming to Version 3 of the Single UNIX Specification. (33875525)

- Added Undefined Behavior Sanitizer, a new low overhead runtime tool that finds several types of undefined behavior in C languages, such as integer overflows, invalid casts, and alignment violations. Undefined Behavior Sanitizer is enabled in the Diagnostics tab of the Scheme editor and is compatible with all other sanitizers. (15425728)
- Added optional detection of nullability annotation violations at runtime. The feature is enabled in the Undefined Behavior Sanitizer section of Build Settings by setting Enable Nullability Annotation Checks to Yes. (30619298)

- Added support for running tests in parallel on multiple devices and simulators to Xcode Server and `xcodebuild`. Bots can be configured to enable or disable parallel testing on devices and default to parallel testing. The output produced by `xcodebuild` when running tests in parallel has been updated and any automated tooling relying on the format of the output may need to be updated. (14254639)
- Added support for automatic and manual provisioning configurations. Servers can be added from the updated bot editor by an agent or admin of the developer team. A scheme that requires manually specified certificates or profiles can shared with the server from the new Signing tab in the bot editor. (15437174)
- Updated Xcode Server to support configuring additional arguments that are passed to `xcodebuild` when integrations are run. (23578597)
- Added two-factor authentication to Xcode server. This can be used when joining your server to your development team, and eliminates the need for an app-specific password. (27002415)
- Added sending an “all clear” email notification when all issues that are tracked by a bot have been resolved. (26179348)
- Xcode Server no longer requires the macOS Server app. Configure your server and bots in the Server & Bots tab of Xcode Preferences. (28211693)
- Updated bots to run tests in a specific language and region. (30382604)
- Updated bot configuration to include an optional Export Options Plist that is to configure the export of an installable product from an archive. (31895193)

- Copy, paste, and cmd+F now work as expected in the logs tab of an integration report. (14140192)
- Xcode Server logs now support copy and paste. (26605066)
- When an upgrade integration runs after installing a new version of Xcode, Xcode Server correctly indicates any changes in SDK versions. (30983641)

- Testing on networked devices using Xcode Server doesn't work when Xcode Server is initialized with a different build service user account. (33904987)

  _Workaround:_ Select the main user account for the build service user when initializing Xcode Server.
- Removing Server.app after configuring Xcode Server with Xcode 9 will stop the Xcode Server service. (31820819)

  _Workaround:_ Do not remove Server.app, or after removing start Xcode Server again from the Server & Bots preference pane or using the `xcscontrol` command-line tool.
- Attempting to edit an Xcode Server bot may incorrectly display the error `does not match this workspace` even when it does. (31957021)

  _Workaround:_ Dismiss the dialog.
- Screenshots may not always be captured during UI testing when Xcode Server is configured to perform integrations using a background user account. (34213968)

- Xcode Server no longer includes hosting Git repositories. To continue using repositories that were set up in macOS Server, configure a new remote Git server and push your code to that remote. After upgrading to Xcode 9, any existing repositories are archived in `/Library/Developer/XcodeServer/HostedRepositories`. (31243129)

- Xcode 8.3.3 requires a Mac running macOS 10.12 or later.
- Xcode 8.3.3 includes SDKs for iOS 10.3.1, watchOS 3.2, macOS 10.12.4, and tvOS 10.2. To develop apps targeting prior OS versions, see [About SDKs and Simulator](../../What%27s%20New%20in%20Xcode%204.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmmzvfvjvomq) in What's New in Xcode, or when running Xcode, select Help > What's New in Xcode.

- Added a 3GB memory class for graphics configurations to Asset Catalog. (30814729)

- Fixed issues with Xcode Server that caused excessive CPU usage. (31874759)
- Fixed issue with Xcode Server so that a bot can switch back to a previously used branch. (31721307)

- Fixed an issue where valid C++ code involving a nested `struct`, `enum`, or `lambda` would fail to compile in C++1z mode. (31385254)

- Xcode no longer produces an Update Signing report for targets that use manual signing. (31276851)

- Fixed an issue preventing output without newlines from being printed in the Xcode Debug Console until there is more output. This issue prevented interactive programs from working with the Xcode Debug console, causing prompts to appear only after a user entered text with a newline. (31465525)

- Interface Builder documents for iOS that contain a color based on an image pattern no longer result in a compiler error. Image pattern colors are not supported, and are now always converted to black when compiled. (31342191)
- Fixed an issue that caused text to be hidden in Interface Builder documents that use a System size font. (31503323)

- Fixed an issue preventing user interaction events being sent from inside the live view of an iOS playground that is running on a device with a non-Retina display, or on a device with a connected non-Retina display. (31445684)

- Resolves an issue where variables in entitlements files were always expanded using the Debug build configuration instead of the active build configuration. (31456053)

- Xcode now schedules Swift whole-module optimization jobs in parallel, enabling better utilization of multiple cores for building projects. (31478013)

- Fixed an issue where the Swift 3 Migrator would not apply compiler fix-it items. (30984612)

- Due to the resolved app archives issue listed below, we will soon be deprecating Xcode 8.3, at which time app archives built with Xcode 8.3 will no longer be accepted by the App Store.

- Fixed an issue that could produce app archives that were larger than necessary. Support for app archives built in Xcode 8.3 will be deprecated. (31302382)

- Xcode 8.3 no longer supports Swift 2.3. Please migrate your projects containing Swift 2.3 code to Swift 3 syntax by opening the project and choosing Edit > Convert > To Current Swift Syntax.
- OS X 10.11 was the last major release of macOS that supported the previously deprecated garbage collection runtime. Applications or features that depend upon garbage collection may not function properly or will not launch in macOS Sierra. Developers should use Automatic Reference Counting (ARC) or manual retain/release for memory management instead. (20589595)
- The Automation instrument has been removed from Instruments. Use Xcode’s UI Testing in its place. (26761665)
- The "Always Search User Paths" build setting is deprecated and may not be supported by a future version of Xcode. Projects which are relying on this feature should migrate to separate user vs. system header include semantics and set this build setting to "No". (16364329)
- 3rd party docset support is now deprecated and will no longer be supported in a future release of Xcode. (30584489)
- The `-exportFormat` parameter of the `-exportArchive` option for `xcodebuild` has been removed. To set the export format, use the `-exportOptionsPlist` parameter to specify an export plist file with the `method` key set to the desired format. For more information on the keys and values for the export plist, run `xcodebuild -help` on the command line.

- Intents Extensions are available on watchOS. (28372004)

- Fixed a problem which would cause Xcode to crash when removing certain file or framework references from certain projects. (29118448)
- Fixed an issue which caused the “update to recommended settings” warning to remain after updating to the recommended settings. (28447448)

- The Apple LLVM compiler now supports nullability annotations on function and method parameters with an array type, and provides additional warnings for incomplete and suspicious nullability annotations. (25846421)

- The compiler properly completes type information for forward-declared classes from C++ precompiled headers. (30173654)

- When building a framework that has module maps in both the source and the install directories that define the same module, the compiler will show a redefinition message. (28638816)

  _Workaround_: Rename the module map file in the source directory to a non-default name (the default name is `module.modulemap` or `module.map`), and set the Module Map File build setting to the renamed module map.

- Scheme pre-action and post-action scripts now set the environment variable `TARGET_DEVICE_IDENTIFIER` to the UDID of the selected run destination device. (28078704)

- Using `xcodebuild -exportLocalizations` or `xcodebuild -importLocalization` to export or import localizations from a project, no longer hangs after the operation is complete. (25857436)
- When copying files the build system now preserves the extended attributes (`xattrs`) used by `codesign` for signing standalone files. (29453501)
- The Mac will no longer sleep when a build is in progress. (29256278)
- Xcode no longer crashes when the build system copies a file with an invalid code signature. (29656173)
- Changes to `xcconfig` files no longer require restarting Xcode to take effect. (29805284)
- Build issues from targets that are implicit dependencies of the active scheme are now shown in the issue navigator. (28719580)
- `xcodebuild` no longer hangs when invoked with a project or workspace containing no schemes. (20450296)

- After opening a project, an Update Signing report may be visible in the Reports Navigator for targets that use manual signing. No signing certificates, app IDs, or provisioning profiles are modified when this occurs. (31209546)

- In the data model editor, changes to an entity’s Code Generation, Compound Indexes, and Uniqueness Constraints are now undoable and autosaved. (21205277)
- When manually generating code for Core Data entities, generated Objective-C code properly uses `«ClassName»+CoreDataClass.h` rather than just `ClassName.h` in `#import` directives. (30343106)
- Passing `-showBuildSettings` to `xcodebuild` for a project containing a Core Data model should no longer result in `xcodebuild` hanging. (26749142)

- The view debugger now shows creation backtraces for many objects in the Object inspector. To show the backtraces, enable Malloc with the option “All Allocation and Free History” logging in the Diagnostics tab of the Manage Schemes dialog. (28715704)
- Autocompletion is supported in Breakpoint navigator text fields. Completions for a file breakpoint are generated using information in the referenced file. Other breakpoint completions use general indexing information and may be slower. (28268983)
- The Scheme editor now contains a text field to add an Intents Extension query instead of issuing an utterance vocally. (26456789)
- Added the ability to visually debug the view hierarchy of an iOS iMessage extension running on iOS 10.3 or later. (28838632)

- LLDB no longer hangs or prints incorrect values when evaluating Swift enumerations defined as an `indirect enum`. (29953436)
- Running a watchOS Intents extension will automatically trigger Siri for a voice command. (29714417)
- Activity and trace messages normally visible in LLDB thread summaries and thread detailed information are available when debugging processes running on beta versions of macOS, iOS, tvOS, or watchOS. (26370425)

- When debugging a watchOS Intent extension using Watch Simulator, the session can end after about 30 seconds with the error message “Program ended with exit code: 0”. (30923914)

  _Workaround_: In the iPhone simulator, open Settings > Siri > App Support and disable Siri for app.
- The first time you run a Complication from Xcode in Simulator it may continually exit when you configure that Complication. (29858029)

  _Workaround_: Re-run the scheme from Xcode.
- Debugged processes may hang on launch if the console option for the scheme is set to “Use Terminal”. (29760580)

  _Workaround_: Select “Use Xcode” for the console option of the scheme.

- The FileMerge application now uses the same text infrastructure as Xcode. File navigation and syntax coloring are more consistent with Xcode. (8838481)

- Updated the Instruments user interface. (28503173)

  _Inspector Refresh_

  Instruments previously contained three inspector panes: Record Settings, Display Settings, and Extended Detail. There are now two inspector panes: Extended Detail and Run Info. Extended Detail remains unchanged and continues to provide additional information about selected data in the detail pane. The new Run Info inspector pane displays information about the currently selected run, including the recording device information and recording settings when the run was taken.

  Record Settings are now located in a Recording Options window. To display this window, choose File > Recording Options, press Option-Command-R, or click-and-hold the Record button in the toolbar and choose Recording Options from the menu that appears. The Recording Options window includes global and instrument-specific recording options.

  The Display Settings inspector pane was previously used to change the graphing style of the timeline pane and to perform filtering in the detail pane. These features have been moved to new locations. If an instrument supports multiple graphing options, a down arrow now appears beside the instrument's icon when the pointer is positioned above the instrument in the timeline pane. Click the instrument's icon to open a popover containing editable graphing options. The down arrow appears only for instruments that have graphing options. Detail pane filtering options, including the text filter field previously located in the navigation bar of the detail pane, are now found at the bottom of the detail pane.

  _Visual Run Comparison_

  The ability to view graphs for multiple runs at the same time in the timeline pane has been removed. To switch between runs, choose Previous Run or Next Run from the Instruments menu, or click a navigation arrow in the activity viewer in the toolbar.

  For more information, see Instruments Help. Open help by choosing Help > Instruments Help.

- Interface Builder supports setting `adjustsFontForContentSizeCategory` to automatically adjust the size of text as the Dynamic Type setting changes. (25543597)

- `NSTextField` objects created in Interface Builder now have `allowsCharacterPickerTouchBarItem` turned off by default. (29223278)
- Auto layout issue buttons in the Interface Builder document outline are no longer clipped under the right margin. (14485840)
- Swift `@IBOutlet` declarations that have a nullability type annotation are now detected. (29983196)
- Setting an `NSMenuItem`'s identifier in Interface Builder is supported on macOS 10.12 and higher. (23945473)
- An `NSDatePicker` now uses `NSDate` instead of `NSCalendarDate` when added from the object library. (29639832)
- Adding a `UILabel` to a tvOS Interface Builder document now uses the correct default font, `UIFontTextStyleHeadline`. (24172228)
- Typing in the Model Key Path field for a Cocoa binding no longer hangs Xcode. (26487347)
- The top of the library content no longer gets shifted under the header bar, which previously resulted in clipping. (27601428)
- Connecting `@IBAction` methods from Interface Builder to Swift code now works when the sender parameter type is `Any`. (29639217)
- Using `NSColorPickerTouchBarItem` in Interface Builder no longer creates a Touch Bar item that is disabled at runtime. (28670596)
- Fixed a bug that prevented setting inspector checkboxes that correspond to bitmask properties, such as `NSWindow.styleMask`, `UIAccessibility.accessibilityTraits`, and `UIPopoverPresentationController.permittedArrowDirections`. (26613034)
- Update frames for views with constraints now works with ambiguous views that have an unambiguous horizontal or vertical axis. (16019988)
- Option for “Follow Readable Width” has been restored to the view controller Size inspector. (28246180)

- Incremental Link-Time Optimization works properly with bitcode-enabled apps. (30109087)
- Improved overall incremental Link-Time Optimization performance, including fixing an issue that was creating duplicate cache files. (29526668)

- The Xcode Organizer now supports exporting tvOS apps for Enterprise distribution. (30000839)

- Speed improvements have been made to the Organizer window. Opening the Organizer with many Archives and many iTunes Connect Products should open quickly. (28722427)

- Under some configurations, iOS and tvOS Playgrounds may hang with no indication of completion. (30085996)

  _Workaround_: If this occurs, rerun the Playground.
- Xcode may crash while you are interacting with a playground's Project Navigator. (29741774)

- Fixed an issue which caused Xcode to warn about Swift 2.3 deprecation even when the "Use Legacy Swift Language Version" setting is set to `NO`. (29655628)

- Changed the user interface for managing signing certificates and provisioning profiles. Certificates are managed from the Accounts preferences pane by selecting a team and clicking Manage Certificates. Automatically managing signing is recommended, however if your app requires manually signing provisioning profiles are managed in the General tab of the project editor. Use the Provisioning Profile dropdown to import or download profiles. In addition it displays profiles that match the current signing configuration of the target. For more information, see Xcode Help. (28641027)

- The `simctl get_app_container` command can now return the path of an app's data container or App Group containers. (30224453)
- The `simctl` tool of the `xcrun` command line tool has two new commands that provide additional information for filing bug reports.

  - `simctl logverbose` enables verbose logging on the specified device.
  - `simctl diagnose` collects all relevant Simulator logs on the host and on the device, and then packages them into an archive that can be attached to bug reports.

  For more information, see the help for each command by running `xcrun simctl <tool name> help` on the command line. (21001891)
- You can invoke Siri using Hardware > Siri after enabling Siri in the Settings app on Simulator. (25176537)

- Resolved an issue where Siri on a simulated watchOS device did not respond the first time Siri was enabled on a simulated iOS device. (29708878)
- Launching an application or executing tests should no longer generate "Application <bundle> is installing or uninstalling, and cannot be launched" errors in Simulator. (30172453)
- Videos recorded by the `simctl` tool of the `xcrun` command line tool now support scrubbing and import into video editors correctly. (29654098)

- Recording a video with the `simctl` command line tool requires Metal-capable hardware. (29688949)
- `AVAssetExportSession` may not return any presets on the iPad Pro (12.9 inch) Simulator. (30698677)

  _Workaround_: Use a different Simulator.

- Xcode Source Editor Extensions will now assert if you try to create a command with an identifier containing invalid characters (characters outside the range `0-9`, `A-Z`, `a-z`, `-`, or `.`). (26615933)

- Added a check for synthesized copy properties of mutable types, such as `NSMutableArray`. Calling the setter for these properties will store an immutable copy of the value. (21022397)
- Added a check for calls to `dispatch_once()` that use an Objective-C instance variable as the predicate. Using an instance variable as a predicate may result in the passed-in block being executed multiple times or not at all. These calls should be rewritten to use either a lock, or to store the predicate in a global or static variable. (23390767)
- Added a check for unintended comparisons between scalar values and `NSNumber`, `CFNumberRef`, and other number objects. (10228523)

- Swift now warns when an `NSObject` subclass attempts to override the `initialize` class method, because Swift can't guarantee that the Objective-C method will be called. (28954946)
- C functions that "return twice" are no longer imported into Swift and attempting to reference such a function will result in a compilation error.

  Examples of functions that "return twice" include `vfork` and `setjmp`. These functions change the control flow of a program in ways that that are not supported in Swift. For example, definitive initialization of variables, a core Swift language feature, can not be guaranteed when these functions are used. Although this could be considered a source-breaking change, it's important to note that any use of these functions will most likely crash at runtime. ([SR-2394](https://bugs.swift.org/browse/SR-2394))
- Indirect fields from C structures and unions are now always imported. Previously they weren't imported when they belonged to a union. This is done by naming anonymous fields, for example:

```
typedef struct foo_t {
   union {
      int a;
      double b;
   };
} foo_t;
```

  Is imported as:

```swift
struct foo_t {
   struct __Unnamed_union___Anonymous_field0 {
      var a : Int { get set }
      var b : Double { get set }
   }
   var __Anonymous_field0 : foo_t.__Unnamed_union___Anonymous_field0

   // a and b are computed properties accessing the content of __Anonymous_field0
   var a : Int { get set }
   var b : Double { get set }
}
```

  Since new symbols are exposed from imported structure/unions, this may conflict with existing code that extended C types in order to provide their own accessors to the indirect fields. (30221279, [PR-6531](https://github.com/apple/swift/pull/6531), [PR-6816](https://github.com/apple/swift/pull/6816))

- Swift REPL and interpreted scripts correctly determine the version of the OS that they are running on. (29433205)
- `#keyPath` respects the original name of properties imported from Objective-C. (28543037)
- The generated header for a mixed-source Swift target will now correctly reference Dispatch framework types using the usual typedefs (`dispatch_queue_t`) rather than their implementation details. (29790636)
- Properties that satisfy requirements in Objective-C protocols work properly when they are declared with a `willSet` or `didSet` observing accessor. (30101703)
- The LLVM and Swift compilers now emit correct diagnostics when using a custom module map that contains system headers. Examples include a module map with paths into the macOS SDK while building for iOS, or headers from `/usr/include`. (26866326)
- The Swift compiler now raises an error when a let property or a variable of a protocol type is modified after initialization. Code that successfully compiled in previous releases may fail after upgrading. For example, the following code that compiled in previous versions now raises an error:

```swift
protocol P {
   mutating func f()
}

extension Int: P {
   mutating func f() { self += 1 }
}

func foo(x: Int) {
   let y: P
   y = x
   y.f()
}
```

  (29716016)
- Swift 3.1 includes a new warning of the form "implicit import of bridging header … via module … is deprecated and will be removed in a later version of Swift". This warning is no longer reported too frequently in contexts where it may not be easy to correct. (30202509)

- Extending the `Sequence` or `Collection` protocols to add a `typealias` named `Element` can result in the Swift compiler crashing. More generally, this issue can occur when name collisions are encountered among type aliases within nested associated types. (30702721)

  _Workaround_: Use a different name for the `typealias`, or write the type out explicitly, such as `Iterator.Element`.
- AppKit's NSView.animator() method claims to return the Self type but really returns a proxy object. When called on a Swift subclass, this may lead to runtime crashes when trying to reference animatable properties of the view that were overridden in Swift:

```swift
public class MyView: NSView {
   public override var frame: NSRect {
      didSet {
         Swift.print(self.frame)
      }
   }

let view = MyView()

// The following line crashes
view.animator().frame = NSMakeRect(0.0, 0.0, 120.0, 120.0)
```

  (27655718)

  _Workaround_: Cast the result of view.animator() to AnyObject, then do method dispatch on the AnyObject value to ensure that the animator proxy is invoked with Objective-C messaging instead of Swift messaging. For example:

```
(view.animator() as AnyObject).setFrame(NSMakeRect(0.0, 0.0, 120.0, 120.0))
```
- The Swift compiler may crash when an Objective-C category extends a system class, and that category adopts a protocol requiring a method matching the getter or setter of a property that is declared using `@property`.

  For example, the `MyLengthModifying` protocol includes a method that matches the setter for the `length` property, and the protocol is part of the `MyAdditions` category extension to the `NSMutableData` system class:

```objc
@protocol MyLengthModifying
   - (void)setLength:(NSUInteger)length;
@end

@interface NSMutableData (MyAdditions) <MyLengthModifying>
@end
```

  ([SR-4022](https://bugs.swift.org/browse/SR-4022))

  _Workaround_: Use a `@property` in your protocol instead of a method, even if the only important requirement is the setter.
- `withoutActuallyEscaping` will fail to compile when given an `@autoclosure` argument. ([SR-4188](https://bugs.swift.org/browse/SR-4188))

  _Workaround_: Pass the autoclosure down to another function as a regular closure argument. For example:

```swift
func allValues(in array: [Int], smallerThan: @autoclosure () -> Int) -> Bool {
   func allValuesImpl(in array: [Int], smallerThan: () -> Int) -> Bool {
      return withoutActuallyEscaping(smallerThan) {
         escapableF in array.lazy.filter {$0 >= escapableF() }.isEmpty
      }
   }
   return allValuesImpl(in: array, smallerThan: smallerThan)
}
```


- A new family of failable conversion initializers to all numeric types either completes successfully without loss of information, or returns `nil`. ([SE-0080](https://github.com/apple/swift-evolution/blob/master/proposals/0080-failable-numeric-initializers.md))
- Extended the `@available` attribute to include varying API availability by Swift language version. An annotated API is compiled as usual and added to the library, but is made available only to a client built with a matching compiler version or a matching `-swift-version` when built for version compatibility. ([SE-0141](https://github.com/apple/swift-evolution/blob/master/proposals/0141-available-by-swift-version.md), [SR-2709](https://bugs.swift.org/browse/SR-2709))
- The `Sequence` protocol adds two new members, `prefix(while:)` and `drop(while:)`. `prefix(while:)` requests the longest subsequence satisfying a predicate. `drop(while:)` requests the remaining subsequence after dropping the longest subsequence satisfying a predicate. ([SE-0045](https://github.com/apple/swift-evolution/blob/master/proposals/0045-scan-takewhile-dropwhile.md))
- Constrained extensions allow same-type constraints between generic parameters and concrete types. For example, the following code defines an extension on `Array` with `Int` elements:

```
extension Array where Element == Int { }
```

  ([SR-1009](https://bugs.swift.org/browse/SR-1009))
- Nested types may now appear inside generic types, and nested types may have their own generic parameters:

```
struct OuterNonGeneric {
   struct InnerGeneric<T> {}
}
struct OuterGeneric<T> {
   struct InnerNonGeneric {}
   struct InnerGeneric<T> {}
}
extension OuterNonGeneric.InnerGeneric {}
extension OuterGeneric.InnerNonGeneric {}
extension OuterGeneric.InnerGeneric {}
```

  ([SR-1446](https://bugs.swift.org/browse/SR-1446))

- The Swift compiler no longer incorrectly reports a version of Swift 3.0. (30081411)

- String interpolations that do not use fully qualified names when referencing members of type extensions can fail in this release. This includes cases that worked in Swift 3. (30885036)

  _Workaround_: Use a fully qualified name. For example, the following code worked in Swift 3, but results an error of “error: expression type 'String' is ambiguous without more context” in the current version:

```
extension Bool {
   static let yes = true
}

print("\(.yes)")
```

  To fix the error use the fully qualified name in the `print` statement:

```
print("\(Bool.yes)")
```


- The package manager no longer uses the auto-linking feature of module maps for C language targets. Packages which use custom module maps for their C language targets should remove the link statement from the module map. The package manager will automatically add the link flag if required.

  For example, the following custom module map:

```
module MyCLib {
   header "foo.h"
   link "MyCLib"
   export *
}
```

  Should be changed to:

```
module MyCLib {
   header "foo.h"
   export *
}
```

  (30016942)
- The Swift Package Manager now supports an edit mode for a package's dependencies. Putting a dependency in edit mode moves it from the managed dependency location to a local Packages directory and omits it from swift package update and related commands. This allows the user to manually manage checkout of the dependency, for example by committing fixes that are required only locally. By default, dependencies are no longer stored in the Packages directory unless they are in edit mode. A package can be put in edit mode with the `swift package edit` command, and can leave edit mode with the `swift package unedit` command. ([SE-0082](https://github.com/apple/swift-evolution/blob/master/proposals/0082-swiftpm-package-edit.md))
- The Swift Package Manager now supports pinning a dependency to a specific version so that in a clean build, it resolves only to the pinned version. The swift build command will automatically record the version that is used for every dependency in a `Package.pins` file, unless autopinning is disabled with `swift package pin --disable-autopin`. Commit the `Package.pins` file to source control when you expect your package to use specific dependency versions without requiring those versions in your `Package.swift` manifest. The `Package.pins` file is used during initial dependency resolution to determine which dependency versions to use; `swift package update` will update all dependency versions and repin those dependencies to the new versions. If autopinning is off, pass the `--repin` flag to swift package update to override any manually-pinned versions. Pinning can be further controlled with the `swift package pin` and `swift package unpin` commands. ([SE-0145](https://github.com/apple/swift-evolution/blob/master/proposals/0145-package-manager-version-pinning.md))
- Replaced the `swift package clean=dist` command with `swift package reset` which resets a package back to a clean state, with no dependencies checked out or build artifacts present. (28384606)
- The `swift package test` command has a new `--parallel` option which executes tests in parallel. This mode of testing may cause problems for tests which are not written to be able to safely run in parallel. (28402178)

- When a dependency of a package is in edit mode, operations which trigger dependency resolution, such as `swift package update`, will fail. (29944464)
- Rebuilding a package in Swift Package Manager now avoids performing unnecessary work. (28037508)
- `swift package update` incrementally updates dependencies instead of re-cloning them from the beginning. In addition, complex dependencies are resolved correctly. (26371453)

- Earlier versions of the Swift compiler would sometimes accept single-element labeled tuples as values, even though these types weren't supported by the language. The Swift 3.1 compiler now more reliably rejects these types. Code that used unsupported single-element tuples can remove the tuple label. For example, this code will now be rejected:

```swift
func foo(x: ((y: Int)) ->; Int)
```

  To fix, remove the tuple label such as:

```swift
func foo(x: (Int) ->; Int)
```

  ([SR-3788](https://bugs.swift.org/browse/SR-3788))

- Added the `XCUISiriService` class to `XCTest` used for writing tests which activate Siri with a voice recognition string, and for queries for elements in the Siri UI. Use the class to write UI tests for Intents and Intents UI extensions. (29958123)
- Added `XCUIKeyModifierCapsLock` as a preferred alternative for `XCUIKeyModifierAlphaShift`. This is consistent with the addition of `NSEventModifierFlagCapsLock` in macOS 10.12, as a preferred alternative for `NSAlphaShiftKeyMask`. (27375799)
- `XCTest` adds new APIs to simplify writing asynchronous tests.

  - A new class, `XCTWaiter`, is used to wait for an `XCTestExpectation` object independent of any `XCTestCase` instance, making it possible to wait inside helper functions and to test support libraries.
  - New subclasses of `XCTestExpectation` are used for tests that wait for `NSNotifications`, Key Value Observation, `NSPredicate` evaluations, and Darwin notifications.
  - `XCTestExpectation` has a new writable description property to simplify failure diagnosis in asynchronous tests.
  - `XCTestExpectation` adds two new behaviors. Set `.inverted` to `true` to fail if the expectation is fulfilled. Set `.expectedFulfillmentCount` to specify the required number of calls to `fulfill()`.

  See documentation in `XCTWaiter.h`, `XCTestExpectation.h`, `XCTNSPredicateExpectation.h`, `XCTNSNotificationExpectation.h`, `XCTKVOExpectation.h`, and `XCTDarwinNotificationExpectation.h` for more details. (22539853)
- The Test navigator now includes test classes and methods located in static libraries that are linked into test bundles. Note that it may be necessary to activate the test navigator before test diamonds for these tests appear in the source editor. (28173131)

- Fixed a bug in the handling of `XCTestExpectations` that waited on predicates evaluated against `XCUIElements`. As a result, some tests which were previously succeeding despite ambiguous (incorrect) queries will start to fail. For instance, if your UI test now fails because of "Multiple matches found" and the element in question is the subject of a predicate expectation earlier in the test, your test is failing because of this fix and the element query will need to be updated to correct the ambiguity that is leading to multiple matches. (28139563)

- Profile-Guided Optimization does not work when using the Test action. (30769613)

- Fixed an issue that could cause building a project to fail with the error message “"Use Legacy Swift Language Version" (SWIFT_VERSION) is required to be configured correctly for targets which use Swift” when using a supported version of Swift. (29667880)
- Xcode no longer warns about using deprecated Swift 2.3 code when the active scheme does not reference targets using Swift 2.3 code. (29671741)

- "Convert to Current Swift Syntax" only converts targets referenced by the active scheme. (13997108)

- Xcode 8.2 offers more Touch Bar actions and allows customizing the Touch Bar controls of the following editors and debuggers: source editor, Playground editor, Interface Builder, view debugger, and memory graph debugger. To customize the Touch Bar, open the desired editor and then choose View > Customize Touch Bar. (28462580)
- Touch Bar API is available for macOS 10.12.2 or later. (28785230, 28785231)

- Builds of iOS, tvOS, and watchOS targets may hang during `CompileAssetCatalog`, `CompileStoryboard`, or `CompileXIB` when running on OS X El Capitan. (28422833)

  Workaround: Rebuild the target.

- Using `.xcconfig` files will not cause projects to prompt about changes on disk when switching git branches. (28794807)

- Command Line Tools (OS X 10.11) for Xcode 8.2 are available and support Swift 3.0 development from the command line on OS X El Capitan. (28234439)

- Opening a data model with a minimum tools version earlier than Xcode 8.0 will not reset the code generation language to Objective-C. (29032095)

- The Memory Debugger for macOS and the iOS Simulator fixes reporting of false memory leaks for Swift classes containing either fields of type `enum`, or classes that inherit from certain Objective-C framework classes. (27932061)

  False reporting can still occur for iOS, watchOS, and tvOS applications. See (29335813) in Known Issues, below.

- The Memory Debugger for iOS, watchOS, and tvOS applications can report false memory leaks when debugging Swift classes containing either fields of type `enum`, or classes that inherit from certain Objective-C framework classes. (29335813)

- A `UITabBarController` correctly displays content instead of blue boxes. (27881406)
- Fixed a crash on macOS 10.12 when a P3 color space other than the system default is installed. (26178719)
- The `supportsPressAndHold` property works when using popover Touch Bar items from Interface Builder. (28701667)

- Dragging an app onto a Simulator window installs the app. (23387069)
- You can take videos and screenshots of Simulator using the `xcrun` Xcode command-line utility. To take a screenshot, run the command `xcrun simctl io booted screenshot`. To take a video, run the command `xcrun simctl io booted recordVideo <filename>.<file extension>.` (9887264)

- Dragging a Live Photo resource into the Simulator imports the Live Photo instead of importing a photo and a video. (27906875)
- Simulator renders the screen correctly when using iOS 9.1 or earlier. (27996364)
- Keychain APIs work correctly in Simulator. (28338972)

- Simulator can crash when saving a screenshot when running on OS X El Capitan. (29182710)

  The crash does not occur on macOS Sierra.

- Extensions which make imported Objective-C generic classes conform to protocols defined in Swift are compiled correctly. (28873860)
- Objective-C generic types show as defined in generated headers with a suffix of `-Swift.h`. (28738008)
- Type inference will properly unwrap optionals when used with generics and implicitly-unwrapped optionals. (28621624)
- NSFileManager's `enumerate(at:includingPropertiesForKeys:options:errorHandler:)` method passes valid URLs to the error handler in code compiled with Swift 3.0.2.

  There may still be some Objective-C methods in the SDKs that incorrectly annotate or assume a type to be nonnull rather than nullable. If the type is one that Swift treats as a struct, such as `NSURL (Foundation.URL)` or `NSDate (Foundation.Date)`, this can lead to a run-time crash in a method with a name like `bridgeFromObjectiveC`; in other cases, it can lead to crashes or undefined behavior in user code. If you identify such a method, please file a report at [bugreport.apple.com](https://bugreport.apple.com/). For reference, the (now unnecessary) workaround for the newly-fixed NSFileManager API is shown below; it can be adapted for whichever API you want to call.

```
static inline NSDirectoryEnumerator<NSURL *> * _Nullable
fileManagerEnumeratorAtURL(NSFileManager *fileManager, NSURL * _Nonnull url,
                           NSArray<NSURLResourceKey> * _Nullable keys,
                           NSDirectoryEnumerationOptions options,
                           BOOL (^ _Nullable errorHandler)
                           (NSURL * _Nullable errorURL, NSError * _Nonnull error)) {
                                return [fileManager enumeratorAtURL:url
                                         includingPropertiesForKeys:keys
                                                            options:options
                           errorHandler:^(NSURL * _Nonnull errorURL, NSError * _Nonnull error) {
                               return errorHandler(errorURL, error);
                           }];
}
```

  This function can be included in your bridging header (for an app or test target) or umbrella header (for a framework target). (27749845)

- The Swift compiler may crash if a nested computed get-only property is defined and accessed within a generic function, a method of a protocol extension, or a method of a generic type. (28933116)

  For example:

```swift
protocol Runcible {}

extension Runcible {
   func runce() -> Int {
      // Property definition crashes the compiler
      var localProperty: Int {
         print(self)
         return 0
      }
      return localProperty
   }
}
```

  Workaround: Redefine the property as a nested function or provide a setter.
- The Swift compiler may crash when an array of tuples is converted to add or remove element labels. (28425149)

  For example:

```swift
typealias Foo = (x: Int, y: Int)
let foos = [(0, 0), (1, 1)] // has inferred type [(Int, Int)]

func getFoos() -> [Foo] {
   // Attempts implicit conversion from [(Int, Int)] to [(x: Int, y: Int)]
   return foos
}
```

  Workaround: Avoid mixing array types of labeled tuples with arrays of unlabeled tuples.
- The Swift compiler may crash if a method of a nested type refers to a nested function in the same scope. (28015090)

  For example:

```swift
do {
   func foo() {}

   class Bar {
      init() {
         //the following line crashes the compiler
         foo()
      }
   }
}
```

  Workaround: Move the function to the top level to avoid the crash.

  For example, the following code shows the workaround for the example given above:

```swift
// Move the function to the top level
func foo() {}

do {
   class Bar {
      init() {
         foo()
      }
   }
}
```
- When an `NSDictionary` is bridged into Swift as a `Dictionary` with `AnyHashable` keys, then using Swift integer values to index the dictionary may fail to find objects inside the dictionary. (29026017)

  For example:

```
NSDictionary *makeDict() {
   return @{@(NSOrderedAscending): @"ascending"};
}
```

```
let dict = makeDict()
// Fails to find key in dictionary
dict[NSComparisonResult.orderedAscending.rawValue]
```

  Workaround: Explicitly construct an `NSNumber` instance for the dictionary lookup key.

  For example, the following code shows the workaround for the example given above:

```
dict[NSNumber(value: NSComparisonResult.orderedAscending.rawValue)]
```


- Xcode 8.2 is the last release that will support Swift 2.3. Please migrate your projects to Swift 2.3 code to Swift 3 syntax by opening the project and choosing Edit > Convert > To Current Swift Syntax.

- The Touch Bar simulator window can interfere with mouse events during macOS UI tests.

  Workaround: As a temporary workaround, set the `IDETestingDisableTouchBarSimulatorWindowBehavior` user default to a `YES` to prevent the window from appearing during testing. (28531281, 28802822)

  1. Quit Xcode if it's running.
  2. Open the Terminal and enter the following command:

     `defaults write com.apple.dt.xcode IDETestingDisableTouchBarSimulatorWindowBehavior -bool YES`

- Xcode 8.1 supports Touch Bar for Macs that include it, and supports adding Touch Bar functionality to your app. (28859277)

  Before using Touch Bar functionality in your app, confirm that the app is running on a macOS version that includes support for Touch Bar using a runtime check.

  - For example, the following Objective-C code performs a runtime check to make sure NSTouchBar is available:

```
NSClassFromString(@"NSTouchBar") != nil
```
  - In Swift code, do an availability check for macOS 10.12.1, and a runtime check for Touch Bar class availability. For example:

```
NSClassFromString("NSTouchBar") != nil
```


- When an Xcode project is stored in iCloud Drive, Xcode does not automatically detect iCloud Drive sync conflicts for projects or for files involved in the build. Note that the Documents and Desktop folders can be stored in iCloud Drive on macOS 10.12. (18161353)
- Opening Xcode projects and workspaces stored in iCloud Drive, or changing source control branches for an open workspace or project stored in iCloud Drive, may sometimes cause Xcode to hang. Note that in macOS 10.12, your Documents and Desktop folders may optionally be iCloud Drive locations. (28212905)

- OS X 10.11 was the last major release of macOS that supported the previously deprecated garbage collection runtime. Applications or features that depend upon garbage collection may not function properly or will not launch in macOS Sierra. Developers should use Automatic Reference Counting (ARC) or manual retain/release for memory management instead. (20589595)

- The `simctl``launch` subcommand in `xcrun` now supports directing the app’s standard out and standard error to a file or to the local terminal. (27636817)

- There is no Command Line Tools (OS X 10.11) for Xcode 8.1 beta 2 package. Xcode 8.1 beta 2 contains SDKs that are incompatible with earlier toolchains. Developers who want to make use of the Xcode 8 beta 2 SDKs from the command line must choose the SDK with `xcode-select`. Developers on OS X El Capitan who have installed versions of the Command Line Tools (OS X 10.11) for Xcode 8.1 beta 2 should install Command Line Tools (OS X 10.11) for Xcode 7.3.1. (28234439)

- Adding a new entity to an Xcode 8 or later Core Data model sets the entity name and the class name to the same value. Changing the entity name changes the class name, unless the class name is different than the entity name. (27896843)

- When using Core Data automatic code generation, changes made to a data model are now available after the model is saved or autosaved. (25789848)

- In the Core Data editor, setting the module of a Swift `NSManagedObject` subclass to Current Product Module can cause Swift code generation to use an incorrect filename for the generated code, and to generate an empty `import` statement for other `NSManagedObject` subclasses. (26898508)

  As a workaround, set the contents of the Module field for the desired entity to the default value:

  1. In the Core Data editor, highlight the contents of the Module field for the desired entity.
  2. Press the Delete key.

     The Module field now shows the default value, "Global namespace," in light gray.

- Starting with macOS Sierra 10.12.1, Xcode 8.1 is required to debug processes that call `exec()` on themselves. For earlier Xcode versions, re-attach the debugger to the target process after the `exec()`] call. (28476369)

- The Xcode debug button in the Touch Bar can sometimes remain in the Control Strip after a debug session has ended resulting in a button with no icon. The debug icon will re-appear in the button when starting a new debug session. (28776047)
- Anonymous closure arguments in Swift cannot be used in LLDB expressions. For example, `po $0` is not supported.

  The values can be inspected in the LLDB command frame variable in Xcode’s Variables View. For example, `fr va $0` displays the current value of the first argument. (28611943)
- A Top Shelf extension is not automatically triggered when you debug a tvOS app from Xcode. As a workaround, use the remote to select a different Top Shelf item and then go back to the one you want to debug. (26131040)
- Evaluating expressions in the Xcode Debug Console attached to an Apple Watch can cause the process to be suspended. This occurs when debugging a Notification before the user interface is displayed, for example, during the -init method. As a workaround, manually launch the Watch app on the device to resume the process. To avoid suspending the process, you can use logging instead of a breakpoint. (27459900)
- Xcode Debugger cannot debug apps written in Objective-C only but that link against frameworks written in Swift only. (28312362)
- The first time you debug a Today extension on a device, it is not offered as an extension to run. As a workaround, stop the process, then run and debug it again. (26427188)
- watchOS 1 apps may fail to finish launching on Apple Watch devices. (27724931)

- `Debugger()` and `DebugStr()` are deprecated and the scheme editor no longer provides the option to enable these functions. If your project uses these functions, enable them by setting the environment variable `USERBREAK` with a value of 1. (24631170)

- Quick Help shows “Symbol not found” message for Objective-C user defined symbols. (28061632)

  Use HeaderDoc documentation tags to add Quick Help comments to your symbols. The following comment block shows the general format for documenting a method:

```
/**
   @method myMethod:withTwoParameters:
   @abstract A short description for the QuickHelp popover
   @description A longer description for the QuickHelp pane
   @param paramName1 A description of the parameter
   @param paramName2 Another parameter description
   @return Description for the return value
*/
```


- The Automation instrument has been removed from Instruments. Use Xcode’s UI Testing instead. (26761665)

- Added Custom Gesture Recognizer to the object library. Use it for custom subclasses of `UIGestureRecognizer` or `NSGestureRecognizer` instead of a plain `NSObject`. This resolves an issue where a combination of stock and custom gesture recognizers on a `UIView` fails to compile. (27838954)
- There is a new Update Frames button at the bottom of the canvas. Click the button to update the frames of the selected objects and their children on the Interface Builder canvas. (27818991)
- The Pin button at the bottom of the canvas has been renamed to Add New Constraints. (27819014)

- Dragging content into static `UITableView` cell on the canvas works again. (28026179)
- Fixed auto layout performance issue with `NSStackView` using Gravity Areas distribution. (27910320)
- Xcode 8.0 did not always restore view frames from storyboards and xibs when layouts were ambiguous. Xcode 8.1 fixes several of these issues. If you have encountered these issues, resolve the ambiguity in the Auto Layout issues and update frames. Xcode 8.1 will persist them correctly. (28221021, 28244619)
- Resolved a layout hang when selecting Landscape orientation in the Device Bar on non-Retina displays when running on OS X 10.11. (27251685)
- Xcode Debug Console no longer shows extra logging from system frameworks when debugging applications in the Simulator. (26652255, 27331147)
- When using Swift 2.3, creating `IBAction` connections no longer inserts `WithSender` in the selector name. (25220368)

- `supportsPressAndHold` does not work when using popover Touch Bar items from Interface Builder. (28701667)

  To work around this, add an outlet to the popover item in code and call `popoverItem.pressAndHoldTouchBar = popoverItem.popoverTouchBar`.
- Using `NSColorPickerTouchBarItem` in Interface Builder results in a Touch Bar item that is disabled at runtime. (28670596)

  To enable the Touch Bar at runtime, add an outlet to the color picker item in code and call `colorPickerItem.isEnabled = true`.
- Using `NSSharingServicePickerTouchBarItem` in Interface Builder results in a disabled Touch Bar item with a blank image. (28716331)

  To set the image and enable the service picker at runtime, add an outlet to the service picker and set the image by calling `servicePicker.buttonImage = NSImage(named: NSImageNameTouchBarShareTemplate)`. Then enable the service picker by calling `servicePicker.isEnabled = true`.
- Creating an `IBAction` connection by control-dragging when using Swift 2.3 incorrectly includes `WithSender` in the selector, causing the application to crash at runtime. `WithSender` is added when control-dragging from a `.swift` file to the Interface Builder canvas, or when control-dragging from the canvas to the document outline. As a workaround, create the action connection by dragging from Interface Builder to the Swift source, or use Find > Find and Replace to manually remove `WithSender`. (27410040)
- Interface Builder does not show correct bar heights (status bar, top bar, bottom bar) when picking landscape for a device in the device configuration bar. (6799670)

- Objective-C now supports ARC-style weak references in files using manual reference counting (MRC). This behavior must be manually enabled in your project settings. `__weak` was previously accepted and ignored in MRC files; to avoid silently changing the behavior of code, if weak references are not enabled, the compiler will now warn on such uses of `__weak`. (28694859)
- Manual reference counting (MRC) weak references are fully supported on macOS 10.12 Sierra, iOS 10.0, watchOS 3.0, and tvOS 10.0.

  MRC weak references are partially supported on macOS Lion 10.7 through macOS El Capitan 10.11, iOS 5.0 through 9.0, watchOS 1.0 and 2.0, and tvOS 9.0. These versions do not support runtime metadata for `__weak` instance variables in classes whose `@implementation` is defined in MRC. Also `NSCopyObject()` will not work, and direct access to `ivars` by Key-Value Coding and Interface Builder will not work. To work around this, use KVC and `IBOutlet` on accessor methods or properties. (9674298)

- The “Use Asset Catalog…” button in the Project Editor’s General tab does not immediately refresh after selecting an asset catalog. To work around this, after selecting an asset catalog, navigate away from the General tab and then back. (26381374)

- SceneKit views (`SCNView`) do not render in Quick Look inside the Xcode Debugger when the current camera (`SCNCamera`) uses new effects such as color grading, color fringe, or saturation and contrast. (27653505)

- When manually signing, Xcode requires your provisioning profile to contain all entitlements used by your default build configuration’s entitlements file. (28377448)

- Inspector tooltips in Interface Builder are not available. (26664452)
- The Xcode automatic signing system may fail to sign your app if you add your account or change your password while your project is open. As a workaround, close and reopen the project. (25627172)
- When opening a project, Xcode only migrates the deprecated `PROVISIONING_PROFILE` setting to `PROVISIONING_PROFILE_SPECIFIER` when the setting is empty. (26281413)
- Downloading profiles using the Download All Profiles button intermittently skips some profiles. As a workaround, use the developer website to download any missing profiles. (26412212)
- Xcode may require a watch paired to your phone to be registered on the developer website even when developing an iOS only app. As a workaround, turn off your watch while developing, or develop using a different phone. (26885780)
- Free provisioning accounts may experience issues launching apps on the watch for the first time. As a workaround, launch the app manually on the device and click Trust when the security sheet appears. (26629630)
- Messages extensions signed with a personal team may fail to run on a device. As a workaround, on the device, go to Settings > General > Profiles & Device Management, tap on the profile name that authorized the app, and tap Trust. (26359174)

- Sticker Pack apps can be used in 32-bit simulators (iPhone 5, iPad Retina) in Xcode. (27830469)
- Simulator no longer leaks memory when a simulated device is booted, rotated, or the scale is changed. (27673601)

- The GameKit framework is missing from the SDK for the watchOS simulator. To work around this issue, develop for GameKit using a watchOS device which does include the framework. (27899791)
- All connected host controllers are seen as the same controller for tvOS in Simulator. As a workaround, test multiple controller functionality on an AppleTV. (27511145)
- There is no way to trigger Siri from Simulator even though Siri APIs are available in Simulator runtimes. Use an Apple TV to test usage of the Siri APIs. (25957692)
- Keychain APIs may fail to work in the Simulator if your entitlements file doesn’t contain a value for the application-identifier entitlement. To work around this issue, add a user-defined build setting to your target named `ENTITLEMENTS_REQUIRED` and set the value to `YES`. This will cause Xcode to automatically insert an application-identifier entitlement when building. (28338972)

- Xcode features provided via extensions now work more reliably. (28341722)
- In Xcode 8.1, an `XCSourceTextRange` is half-open: It includes the character at the start position, and excludes the character at the end position. Previous versions of Xcode were inconsistent when translating from the internal format to an `XCSourceTextRange` instance. All Xcode Source Editor Extensions built against Xcode 8.0 will continue to get the previous inconsistent behavior for binary compatibility.

  An Xcode Source Editor Extension built against Xcode 8.1 that also needs to run in Xcode 8.0 can check the version of Xcode by comparing `XCXcodeKitVersionNumber` against the version listed in _XcodeKit/XcodeKitDefines.h_. (28131743)

- Xcode Source Editor extensions don’t support adding Objective-C categories to XcodeKit classes. (26432410)

- When Optional values are bridged to Objective-C objects, such as when an `Optional` is passed to an Objective-C API that takes `nonnull` id or when a `[T?]` array is bridged to an `NSArray`, the Swift runtime will now bridge the wrapped value if there is one. If a `nil` value is bridged, and the API does not accept a `nil` pointer, Swift will use `NSNull` to represent the `nil` value. ([SE-0140](https://github.com/apple/swift-evolution/blob/master/proposals/0140-bridge-optional-to-nsnull.md))
- All of Swift's standard number types now bridge to Objective-C as `NSNumber` instances. Structs such as `CGRect`, for which the `NSValue` class provides factory methods, now bridge to Objective-C as `NSValue` instances. ([SE-0139](https://github.com/apple/swift-evolution/blob/master/proposals/0139-bridge-nsnumber-and-nsvalue.md))
- Two types have been added to the Swift standard library: `UnsafeRawBufferPointer` and `UnsafeMutableRawBufferPointer`. They represent a non-owning view over a fixed region of memory (a buffer). They expose the underlying buffer as a `Collection` of `UInt8` bytes, independent of the type of values held in that memory. This helps developers migrate to the UnsafePointer changes in Swift 3.0. For background, see the [UnsafeRawPointer Migration Guide](https://swift.org/migration-guide/se-0107-migrate.html). In some cases, `UnsafeRawBufferPointer` provides a safe replacement for `UnsafeBufferPointer<UInt8>`. This is particularly useful for code that works with binary file formats and streaming I/O.

  A new `withUnsafeBytes(of:)` function exposes a value's in-memory representation as an `UnsafeRawBufferPointer`. This example copies a heterogenous struct into a homogeneous array of bytes:

```swift
struct Header {
   var x: Int
   var y: Float
}

var header = Header(x: 0, y: 0.0)
var byteBuffer = [UInt8]()

withUnsafeBytes(of: &header) {
   (bytes: UnsafeRawBufferPointer) in byteBuffer += bytes
}
```

  A new `Array.withUnsafeBytes` method exposes an array's underlying buffer as an `UnsafeRawBufferPointer`. This example copies an array of integers into an array of bytes:

```
let intArray = [1, 2, 3]
var byteBuffer = [UInt8]()

intArray.withUnsafeBytes {
   (bytes: UnsafeRawBufferPointer) in byteBuffer += bytes
}
```

  ([SE-0138](https://github.com/apple/swift-evolution/blob/master/proposals/0138-unsaferawbufferpointer.md))
- The macro `__swift__` will be defined when importing C and Objective-C code into Swift. The value of this macro will have the form `XYYZZ`, where `X` is the major version of the language, `YY` is the minor version of the language (always two digits), and `ZZ` is the “patch” version (also two digits). For example, in Swift 3.0.1, `__swift__` will have the value `30001`. Note that this macro is not defined in the legacy Swift 2.3 compiler, nor was it defined in the initial release of Swift 3. (26921435)

- An issue with `@NSManaged` properties being used to satisfy protocol requirements has been fixed. ([SR-2673](https://bugs.swift.org/browse/SR-2673))
- Linking LTO files compiled with Xcode 8 to LTO files compiled with a previous Xcode release will now work even if Objective-C class properties are in use. (28017126)
- The C attribute `swift_error(zero_result)` is now handled correctly. (27985744)
- Access checking for overrides and for members that satisfy protocol requirements has been fixed to more closely match the Swift language proposal that introduced `private` and `fileprivate` ([SE-0025](https://github.com/apple/swift-evolution/blob/master/proposals/0025-scoped-access-level.md).) This resolves some crashes, but can result in errors for code that was accepted in Xcode 8.0. To keep Swift 3 code compatible with Xcode 8.0, use `private` for top-level classes and structs instead of `fileprivate`. (27820665)
- Swift Evolution proposal [SE-0107](https://github.com/apple/swift-evolution/blob/master/proposals/0137-avoiding-lock-in.md) states that `UnsafePointer.withMemoryRebound(to:capacity:)`
  should produce a `const UnsafePointer`, but in Swift 3.0 it produces an `UnsafeMutablePointer`. As a result, Swift 3.0 incorrectly accepts code in this form:

```swift
let ptr: UnsafePointer<Int>
ptr.withMemoryRebound(to: UInt.self, capacity: 1) {
   takesUInt($0) // this implicitly converts to a mutable pointer
}
```

  For Swift 3.0.1, change the code to:

```
ptr.withMemoryRebound(to: UInt.self, capacity: 1) {
   takesUInt(UnsafeMutablePointer(mutating: $0))
}
```

  (28409842)

- Extensions which make imported Objective-C generic classes conform to a Swift protocol can be miscompiled. This can result in a runtime crash in `objc_retain` or `objc_msgSend` when a class method is called generically through the protocol. (28873860)

  As a workaround, declare the protocol as `@objc` or wrap the class instance in a generic struct that implements the protocol.
- When using generics and implicitly-unwrapped optionals, type inference can fail to unwrap the optional, leading to compiler errors for valid code. (28621624)

  As a workaround, explicitly unwrap the optional. For example, in the following valid code, the compiler gives an error because `u` is implicitly-unwrapped in the `return` statement.

```swift
func compare<T: Comparable>(v: T, u: T!) -> Bool {
   return v < u
}
```

  Work around the error by explicitly unwrapping `u`:

```swift
func compare<T: Comparable>(v: T, u: T!) -> Bool {
   return v < u!
}
```
- Objective-C methods with empty selector pieces (i.e. a colon with no name before it) may cause the Swift 3 compiler to crash. As a workaround, rename the methods or remove them from the bridging header includes. If neither of those alternatives are possible, guard the method declaration. For example:

```
#if !defined(__swift__) || __swift__ > 30001
```

  (28448188)
- Lazy initialization using a constructor with defaulted parameters can fail with the message “type of expression is ambiguous without more context”. As a workaround, wrap the call to the constructor into a separate function if you want to use the defaulted parameters such as:

```swift
struct Value {
   init(first: Int, second: Int? = 10) {}
}

class Test {
   static func createValue(first: Int) -> Value {
      return Value(first: first)
   }

   lazy var theValue = createValue(first: 5)
}
```

  Calling the constructor without any of the parameters defaulted works as well. (28313602)
- Some Objective-C methods in the SDKs may incorrectly annotate or assume a type to be `nonnull` rather than `nullable`. A type that Swift treats as a struct, such as `NSURL` (`Foundation.URL`) or `NSDate` (`Foundation.Date`), results in a run-time crash in a method with a name like `bridgeFromObjectiveC`; in other cases, it can lead to crashes or undefined behavior in user code. If you identify such a method, please file a report at [bugreport.apple.com](http://bugreport.apple.com/).
  As a workaround, add a trampoline function in Objective-C with the correct nullability annotations. For example, the following function will allow you to call `FileManager's``enumerator(at:includingPropertiesForKeys:options:errorHandler:)` method with an error handler that accepts `nil` URLs:

```
static inline NSDirectoryEnumerator<NSURL *> * _Nullable

fileManagerEnumeratorAtURL(NSFileManager *fileManager, NSURL * _Nonnull url, NSArray<NSURLResourceKey> * _Nullable keys, NSDirectoryEnumerationOptions options, BOOL (^ _Nullable errorHandler)(NSURL * _Nullable errorURL, NSError * _Nonnull error)) {
     return [fileManager enumeratorAtURL:url includingPropertiesForKeys:keys options:options errorHandler:^(NSURL * _Nonnull errorURL, NSError * _Nonnull error) {
      return errorHandler(errorURL, error);
   }];
}
```

  This function can be included in your bridging header (for an app or test target) or umbrella header (for a framework target). (27749845)

- UI Recording in the Touch Bar only records tap interactions. (28500819, 28454674)

  To work around this, record the test and then change the generated code for the test to the desired type of interaction. For example, replace the call to `tap` with `doubleTap` to change from a single-tap to a double-tap. For possible interactions, see the documentation for [XCUIElement](https://developer.apple.com/documentation/xctest/xcuielement).
- UI tests may fail to run for apps written with Swift 2.3. (26680406)
- Keystroke events issued by Xcode UI tests may be dropped if `TextExpander` is enabled. (25203671)

- Xcode Server reports the error “Verifying that Xcode is accessible” when Xcode is installed in a non-world-readable location other than /Applications. Since the service makes use of role accounts to run various service daemons, those role accounts need to be able to read Xcode. As a workaround, place Xcode in the /Applications folder. (26920334)

- The clang static analyzer now checks for improper cleanup of synthesized instance variables in `-dealloc` methods. (6927496)
- The indexing component has moved out of the Xcode process to an XPC service, providing the benefit of process isolation and accurate resource usage attribution. (24330820)
- A fast scanner for unit tests is now available. The scanner will populate the Test navigator shortly after opening a project for the first time, eliminating the need to wait for indexing to parse all the unit test source files. It supports both Swift and Objective-C unit tests. (25716884)

- Opening Xcode projects and workspaces stored in iCloud Drive, or changing source control branches for an open workspace or project stored in iCloud Drive, may sometimes cause Xcode to hang. Note that in macOS 10.12, your Documents and Desktop folders may optionally be iCloud Drive locations. (28212905)

- On macOS 10.12, Xcode removes its custom motion animations from the user interface when the Reduce Motion setting is selected in System Preferences > Accessibility > Display. (26973957)

- Address Sanitizer is supported in Swift and can catch memory corruption errors that get triggered by using types such as `UnsafeMutablePointer`. (21888114)
- The new thread sanitizer feature combines compiler instrumentation and runtime monitoring to help find and understand data races and other concurrency bugs in Swift and Objective-C. Thread sanitizer is supported on 64-bit macOS and 64-bit simulators. (19432893)

- Using a custom module map that contains system headers (directly or indirectly) can result in crashes of the LLVM or Swift compiler. For example, this can occur when using a module map with paths into the macOS SDK while building for iOS, or when using headers from the system `/usr/include` while building with any Xcode SDK.

  To work around this issue, make sure the system headers mentioned in the module map or included by custom headers are always found in the current target's `SDKROOT`. (26866326)
- Older versions of libobjc cannot fully handle the runtime metadata provided by the compiler for class properties. Therefore, if your deployment target is older than OS X 10.11 or iOS 9, some of this metadata will be absent. It is still safe to use class properties in projects deploying to newer OS versions, and the accessor methods will still show up in the runtime metadata. If you aren't using the Objective-C runtime to get information about class properties, you don't need to worry about this issue. (25616128)
- Trying to link with LTO files compiled with Xcode 8 and files compiled with a previous Xcode release may fail if Objective-C class properties are in use. (28017126)
- Activity and trace messages normally visible in LLDB thread summaries and thread detailed information is absent when debugging processes running on beta versions of macOS, iOS, tvOS, or watchOS. (26370425)
- If any Swift code contains a `private func ==` definition, LLDB fails to evaluate expressions in a Swift context with the error: `binary operator '==' cannot be applied to two 'Int' operands`. To work around this issue, make any `==` overloads in your program non-private. (27015195)
- The new LLVM-based `otool(1)` exits non-zero on the first error it encounters for the files on the command line. This includes treating non-object files as errors. This differs from the old `otool(1)`, available as `otool-classic(1)`, which processes all files on the command line even if some have errors and does not treat non-object files as an error but as a warning. (26828015)

- Applications compiled with Xcode 8 and a deployment target of iOS 7 may crash at launch with the following assertion:

```
Assertion failed: (maxCountIncludingZeroTerminator > 0 && tokenCount < maxCountIncludingZeroTerminator), function CUIRenditionKeyCopy, file /SourceCache/CoreUI/CoreUI-232.4/CoreTheme/ThemeStorage/CUIThemeRendition.m, line 185.
```

  To work around this issue, update the deployment target to iOS 8.0 or later, or add a single image to the asset catalog that has at least five attributes specified across the image set, such as:

  - scale (1x, 2x, 3x)
  - idiom (add iPad,iPhone, and a universal asset)
  - direction (left to right, right to left)
  - width/height class (any & compact, and so forth)
  - memory (add a 1 GB asset)
  - graphics (add a Metal 1v2 asset)

  It is not necessary to use the image in your code or to add all of these attributes. (27852391)

- The PNG compression build settings `Compress PNG Files` and `Remove Text Metadata From PNG Files` are available for macOS in addition to iOS, watchOS, and tvOS. For macOS, both settings are off by default. (24638927)
- The build setting `ENABLE_ADDRESS_SANITIZER` controls whether the address sanitizer is enabled across both the clang and swiftc compilers. Previously only `CLANG_USE_ADDRESS_SANITIZER` existed; that setting is now subordinate to `ENABLE_ADDRESS_SANITIZER` and should not be used by itself. If a project was previously using `CLANG_USE_ADDRESS_SANITIZER` as a build setting to enable the address sanitizer separate from the scheme option, then `ENABLE_ADDRESS_SANITIZER` should now be used instead. (24912445)
- Xcode takes build settings set in xcconfig files into account when suggesting updates to your build settings. (13433596)
- xcconfig files support conditional inclusion of other xcconfig files, using the syntax `#include?` instead of the usual `#include` (which still generates a warning, as before, if the file is missing). (11003005)
- The static analyzer check for nullability violations now supports both aggressive and less aggressive levels of checking. The more-aggressive level checks for nullability violations in all calls and is enabled by default for new projects. The less-aggressive level checks for nullability violations in calls to project headers but not system headers. The less-aggressive level is enabled by default for existing projects. To turn on the more-aggressive level for existing projects, select "Yes (Aggressive)" for "Misuse of ‘nonnull’" in the Static Analyzer - General Issues section of the target build settings. (25120516)
- The development team used for signing is now stored in a new build setting, `DEVELOPMENT_TEAM`. This allows overriding the development team using xcconfig files. As a result, the format of the new `PROVISIONING_PROFILE_SPECIFIER` build setting has changed. The old format, which included a team ID, is still supported, but it now needs to contain only a provisioning profile name. (27082795)
- If your `CODE_SIGN_ENTITLEMENTS` value is conditionalized per SDK, add a setting for the appropriate simulator SDK(s) explicitly. Previous versions of Xcode fell back to the iOS SDK’s value; this is no longer the case. (26923346)
- When the `Enable Testability` build setting is enabled, Xcode 8 will pass `-export_dynamic` to the linker to preserve all global symbols for testing. This effectively overrides dead code stripping, which can expose link failures from unused functions that reference undefined symbols. If necessary, disabling testability will allow the link to proceed without source changes. (27684883)
- xcodebuild now supports a `-quiet` flag to suppress output other than errors and warnings. (5732994)
- In macOS 10.12 and later, Xcode cleans up stale derived data, precompiled headers, and module caches. (23282174)

- In Developer ID provisioning profiles, the value of the com.apple.developer.icloud-container-environment entitlement has changed from an array to a string. (26722546)
- When exporting an app with Developer ID, Xcode will automatically generate Developer ID provisioning profiles for any bundles embedded in the app. (26827710)

- Developer ID apps using profiles will not work on versions of OS X prior to 10.10. You can work around this issue by explicitly installing the profile before running the app. (26013718)
- Xcode 8 does not automatically copy the aps-environment entitlement from provisioning profiles at build time. This behavior is intentional. To use this entitlement, either enable Push Notifications in the project editor’s Capabilities pane, or manually add the entitlement to your entitlements file. (28076333)

- Xcode does not require code signing for iOS frameworks, and will skip signing a framework if a team is not specified. Frameworks should be signed when copied into the hosting product (using the Code Sign on Copy flag in a Copy Files build phase). (26892618)

- Fixed a crash opening documents using a pattern color with `NSPatternColorSpace`. (26964970)

- The Swift Package Manager tool for managing the distribution of Swift code is available on the command line. Help for the Swift Package Manager can be found by running `swift package --help` in Terminal. (25582703)

- Xcode automatically generates classes or class extensions for the entities and properties in a Core Data data model. Automatic code generation is enabled and disabled on an entity by entity basis, and is enabled for all entities in new models that use the Xcode 8 file format. This feature is available for any data model that has been upgraded to the Xcode 8 format. You specify whether Xcode generates Swift or Objective-C code for a data model using the data model’s file inspector.

  When automatic code generation is enabled for an entity, Xcode creates either a class or class extension for the entity as specified in the entity's inspector: the specified class name is used and the sources are placed in the project’s Derived Data. For both Swift and Objective-C, these classes are directly usable from the project’s code. For Objective-C, an additional header file is created for all generated entities in your model. The header file name conforms to the naming convention “DataModelName+CoreDataModel.h”.

  The Xcode attribute inspector also allows a choice of whether to generate scalar or object properties. New attributes default to generating scalar properties where appropriate. For attributes that previously relied on filling in class information after code was manually generated (for example, transformable attributes and transient attributes with an undefined attribute type), specify the class to use in the attribute’s declaration directly in the attribute inspector. (22223273)

- Debugging mixed Objective-C and Swift projects has been improved by displaying Swift instance variables even when showing Objective-C references to Swift types. (24083219)
- Memory graph debugging is available for WatchKit extensions. (26563396)
- In addition to the Xcode console, Terminal can be used for macOS process input and output while debugging. Open the scheme editor to edit your scheme’s Run action and then select the Use Terminal option in the Options tab. (23565724)
- LLDB fully supports the Swift 3 language and includes numerous quality improvements to make Swift debugging more accurate and reliable. Note that when debugging Swift 2.3 code an earlier version of LLDB will be used, and most new LLDB features will not be available. (22509661)
- Stepping into a specific function in a complex line of code is much easier. Consider the following example:

```
Resolved Issues(bar(), baz())
```

  Previously, stepping into `Resolved Issues()` required stepping into and out of `bar()` and `baz()`. Now the `sif` alias makes this easy. The command `sif Resolved Issues` will step through other functions until it reaches the named target. If the expected target isn’t reached, it provides a safeguard by stopping after returning from the current scope. (24528770)
- Xcode 8 now isolates LLDB as a distinct process. This is largely transparent but has the following implications:

  - In the event of an unrecoverable failure while debugging, Xcode will be unaffected aside from closing the debug session.
  - Multiple debugger versions can be used simultaneously. Projects containing Swift 2.3 code will use an earlier corresponding LLDB, and when working with an open source Swift toolchain, the included LLDB will be used.

  (23418627)
- LLDB now supports and correctly displays the value of thread-local variables. (7796742)
- LLDB documentation has been significantly updated:

  - A new _[LLDB Debugging Guide](../../../documentation/General/LLDB%20Debugging%20Guide/About%20LLDB%20and%20Debugging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3domjx)_ is available in Xcode help.
  - LLDB’s built-in help text has been overhauled for clarity and consistency.
  - When no help is available via `help <topic>` in LLDB, alternative suggestions are displayed.
  - Command aliases can now have custom help text, and several of the key built-in aliases take advantage of this facility.

  (24868841)
- Expressions that can be trivially corrected using compiler fix-its are automatically fixed and executed. This ensures that LLDB doesn’t get in your way for something as simple as a missing semicolon or the wrong style of indirection in Objective-C; or the need to unwrap a value in Swift. (25351938)
- Expressions in LLDB support an even wider array of scenarios. Declaring and capturing Objective-C blocks and C++ lambdas now works as expected, and declaring C and C++ functions is now possible using the new `--top-level` (or `-p`) option on the `expression` command. (22509903)
- Two new command aliases make it easy to examine C-style arrays. The commands `parray` and `poarray` behave like their counterparts `p` and `po` when formatting each element of the specified array. The length of the array must be specified first, followed by a pointer to the array. The usual LLDB conveniences for specifying arguments using the result of expressions can be used for the length—for example, `` parray `argc` argv `` when stopped in a C, C++, or Objective-C main function. (12691162)
- Processes built with thread sanitizer enabled will display relevant information when issues are detected while debugging with LLDB. (23956680)

- Debugging a Notification extension works with the normal extension debugging workflow in Xcode. (23487932)
- Debugging with address sanitizer does not result in a runtime error regarding dyld inserting the ASan library. (23805032)
- Fixed a crash for macOS apps running with thread sanitizer when profiling from the Memory gauge. (26275485)
- The view debugger shows the debug description for views in the inspector. (23976841)
- The view debugger shows the frame for views in the size inspector. (24314615)
- The view debugger functions normally when debugging on the iOS 8 simulator. (25802025)
- Resolved an issue where view debugging could fail when not using auto layout, due to an unhandled assertion in an underlying system framework. (25311044)
- Resolved stability issues with debugging extensions or watch apps in the simulator. (25338888)

- `Debugger()` and `DebugStr()` are deprecated and the scheme editor no longer provides the option to enable these functions. If your project uses these functions, enable them by setting the environment variable `USERBREAK` with a value of 1. (24631170)

- You must unlock devices when first connecting them to Xcode in order to use them for development. (25771635)

- Instruments can't find the symbols downloaded for Apple Watch. As a workaround, find the device support folder for your Apple Watch version (it will be inside `~/Library/Developer/Xcode/watchOS DeviceSupport/`), create an empty `Info.plist` file inside this folder, and restart Instruments. (27996340)
- The Instruments Leaks template fails to report data against Swift apps with a Release configuration, because this configuration enables Whole Module Optimization by default. To work around this issue: if you're targeting a Swift app, temporarily turn off Whole Module Optimization when using either the Leaks template in Instruments or the Memory Graph Debugger in Xcode. (27906876)

- The Automation instrument has been removed from Instruments. Use Xcode’s UI Testing instead. (26761665)

- Interface Builder makes it easier to migrate to auto layout by no longer generating implicit constraints for views without constraints. (13728545, 24274870)
- The size inspector now displays frame coordinates with greater precision, and can accept fractional point values on Retina displays for iOS. (8895377)
- Storyboard and xib files support smooth zooming across iOS, tvOS, and watchOS, as well as editing at any zoom level. When using a mouse, operating the scroll wheel while holding down the option key allows you to zoom in and out. (5215027, 9635866, 11579591, 15011038, 21256576, 23379420)
- A completely redesigned workflow for working with trait variations (for example, size classes), supports designing UI in terms of a real device size rather than by using intentionally abstract rectangles. Combined with a new mode for quickly introducing variations, it’s easier than ever to see what your UI looks like across multiple devices, orientations, and adaptations like Slide Over and Split View on iPad. (16901225, 23804474, 24012599)
- Creating an `@IBAction` method by control-dragging from Interface Builder to a Swift 3 source file includes an underscore before the `sender` parameter, causing the corresponding Objective-C selector to match Swift 2 behavior. Converting to Swift 3 syntax modifies `@IBAction` methods by adding an underscore, preserving connections in existing IB documents. (26120871)
- The Notes field in the Identity inspector now has "Comment For Localizer" placeholder text to more clearly indicate that it is included in an XLIFF export. (26802029)
- Xcode 8 removes the ability to configure views without constraints with frame varying per size class. Views without constraints may look different after compiling with Xcode 8 when switching size classes at runtime. Going forward, use constraints and autoresizing masks with the device bar to achieve the desired layout. (25894544)
- The canvas in Interface Builder renders visual interactions between iOS views as they appear at runtime, including accurate compositing of `UIVisualEffectView`. Designable views can now visually interact with their subviews. Rendering performance is significantly improved for tvOS documents. (21922006)
- Interface Builder supports customizing UI elements for Dark interface style on tvOS and previewing in the assistant editor. This support is enabled by default for new xib and storyboard files; it can be enabled for existing documents by selecting the Uses Trait Variations option in the Identity inspector. (23343849)
- Interface Builder supports colors in the Display P3 color space. In the system color panel, select RGB or HSB sliders, click the gear menu to the right of the popup button, and choose Display P3 from the list. (23612133)
- The UI for customizing inspector properties for iOS size classes is improved, and defaults to the configuration that is currently active in the canvas. (26123851)
- Xcode 8 provides numerous accessibility improvements, including VoiceOver enhancements to the design canvas, inspectors, document outline, and object library. (5306382)
- While the canvas is varying for traits (indicated by a blue bottom bar) and has focus, the Delete key uninstalls the selected objects only for the current configuration. If the document outline has focus, or when the canvas is not in varying mode, the Delete key removes the selected objects from the document, affecting all configurations. (26153578)
- Color values in Interface Builder documents correctly use color space during rendering and compilation. Earlier versions of Xcode mishandled color spaces saved in iOS and tvOS documents. Xcode 8 converts existing colors in a way that preserves their perceptual appearance on a device, and updates either the color space or component values in the source document as appropriate. (7645087)

- Constraint constants with fractional (non-integer) values can now be configured in Interface Builder. (15963933)
- Constraints to a view are now preserved when the view is embedded in a new view, or dragged to within a new superview. (9666331)
- Storyboard and xib files can be scrolled while dragging objects or scenes, and during control-dragging to create connections. Dragging to the edge of the canvas activates autoscrolling. (25221374, 25631320)
- Interface Builder's design canvas draws correctly when layer-backing is enabled in macOS xib and storyboard documents. This includes canvas decorations such as resize knobs, selection indicators, bounds rectangles, constraints, and segue arrows. (5565950)
- Fixed a crash when navigating away from an Interface Builder document that uses custom fonts and designable views. (17237787)
- `NSBox` properties that are inapplicable for custom box and separator lines are excluded from inspectors, warnings, and saved documents. This includes a localizable title for separator lines that was unintentionally included in XLIFF output. (5081354, 9939692, 14994467, 23877301)
- Using a custom font in `UILabel`, `UITextField`, or `UITextView` with size classes enabled now correctly encodes the font for use at runtime. (18535469)
- Xcode records custom font names once per document, rather than once for each use in a document. (18389741)

- Inspector tooltips in Interface Builder are not available.

- For projects with localizations in more than one language, Xcode automatically turns on the static analyzer check for missing localizability. (22807459)

- XLIFF export no longer includes `accessibilityIdentifier` strings configured in Interface Builder. (24548071)

- Logging for simulated key presses includes the glyph representations for modifier keys, as well as the glyph and symbol name for constants starting with `XCUIKeyboardKey`. (27374182)

- Unified Logging is now supported for apps uploading to TestFlight and the App Store. (27794355)

- A new target type for Metal libraries enables creating new projects, or new targets in existing projects, for platforms that support Metal. Targets of this type only compile Metal source files and produce Metal libraries. A Metal library produced in this manner can be added to the Copy Bundle Resources build phase of another target to make the Metal content available to that target's products. (17877026)

- Objective-C now supports class properties, which interoperate with Swift type properties. They are declared as `@property (class) NSString *someStringProperty`;, and are never synthesized. (23891898)
- C++ now supports the `thread_local` keyword, which declares thread-local storage (TLS) and supports C++ classes with non-trivial constructors and destructors. (9001553)
- Incremental Link-Time Optimization (LTO) has been added and is a major redesign of the existing monolithic LTO mode. Incremental LTO addresses the three main limitations of monolithic LTO by making it parallel, memory lean, and incremental. (22252706)

- The playground video tag now supports remote URLs. (24886083)

- The first link included in a playground markup comment does not have its hit target reduced to the beginning of the linked text. (24920637)
- Live views for iOS playgrounds display retina views on Macs with retina displays. (26945081)
- The editor's Add Documentation command is enabled when editing a playground. (27395238)

- Xcode 8 contains a project template for a cross-platform SpriteKit game. When you create a project from this template, you can choose which platforms should be supported (iOS, macOS, tvOS, watchOS). The resulting project will contain a target for each selected platform and will factor out content that is appropriate to be shared between all platforms. Shared content includes the primary `SKScene` subclass, sks files, and the main asset catalog. Platform-specific content is created for each supported platform including app delegates, view controllers, and so forth. (26543360)

- The "Embed Binaries" section of the target editor correctly adds new embedded binaries. (27631378)
- Xcode correctly embeds or links frameworks across projects without requiring you to set up a direct reference between the project that produces the framework and the project that embeds or links it. (27631386)
- Changes made to projects from outside Xcode (for instance, from Git) do not cause Xcode to select a different active scheme. (16762297)

- Xcode 8 provides completely rewritten AppleScript support. A new scripting dictionary provides the ability to automate Xcode workflows. New functionality includes, for example, the ability to perform "run" and "test" actions. Some previous functionality, such as manipulating files and groups in a workspace, has been curtailed for enhanced reliability. Open Script Editor.app and select File > Open Dictionary to access the Xcode scripting library.

  Xcode scripts can be used in Automator workflows with the Run Script command. (22819339)

- The signing system has been rewritten to include a new mode for automatically managing signing assets, in addition to a dedicated manual mode where the profiles for the target must be explicitly selected. When automatically managing signing assets, Xcode will create signing certificates, update app IDs, and create provisioning profiles. For manual mode, only custom created profiles can be selected and Xcode will not modify or create any signing assets.

  Xcode now encodes profiles in the target using the `PROVISIONING_PROFILE_SPECIFIER` build setting. This setting allows specifying both the team ID and the name or identifier of the profile. (23992778)

- `UIContentSizeCategoryDidChangeNotification` is delivered as expected in the iOS 10.0 Simulator runtime. (25303105)
- `SKVideoNode` is usable in the iOS and tvOS Simulator Runtimes. (26433285)

- The GameKit framework is missing from the SDK for the watchOS simulator. However, the framework is present for watchOS devices, so you can still do development of GameKit apps for watchOS on devices. (27899791)

- Xcode now assumes that Git repositories with “core.precomposeunicode” unset or set to false are using macOS canonical decomposition normalization for Unicode filenames. This may cause repositories that have this unset or set to false to have trouble with some Unicode file names if the filename normalization in the repository was done on another platform. (26861162)

  To work around this issue, make sure the configuration for Git repositories has “core.precomposeunicode” set to true. This will be the case for any repository created with the Git tools that ship with Xcode. Only leave it unset or set to false for compatibility with repositories that have Unicode filenames using macOS canonical decomposition normalization.

- Xcode 8 adds support for Xcode source editor extensions. Application extensions provide additional commands in the Xcode Editor menu. These extensions can manipulate both text and selections. To create them, use the new Xcode Source Editor Extension target template in the macOS Application Extensions section when creating a project. (23194974)

- To use the Editor's Comment/Uncomment Selection and Add Documentation commands—as well as other installed Xcode Extensions—on OS X 10.11, launch Xcode and install additional system components, then restart your Mac. (26106213)

- The version of Swift 2 (2.3) used in Xcode 8 is very close to the version used in Xcode 7.3.1. However, it has been updated for the newer SDKs, and therefore is not compatible with Swift frameworks compiled in Xcode 7.3.1. Distributing binary Swift frameworks remains unsupported in Xcode 8. (25680392)
- For information on migrating from Swift 2 to Swift 3, see the [Swift Migration Guide.](https://swift.org/migration-guide/)
- When a Swift program traps at runtime due to an unexpected null value, the error message reports the source location of the `!` operator or implicit unwrapping in the user's source code. (26919123)
- Argument labels have been removed from Swift function types. Instead, they are part of the name of a function, subscript, or initializer. Calls to a function or initializer, or uses of a subscript, still require argument labels, as they always have:

```swift
func doSomething(x: Int, y: Int) {}
doSomething(x: 0, y: 0) // argument labels are required
```

  However, unapplied references to functions or initializers no longer carry argument labels. For example:

```swift
 let f = doSomething(x:y:)   // inferred type is now (Int, Int) -> Void
```

  Additionally, explicitly-written function types can no longer carry argument labels, although one can still provide a parameter name for documentation purposes using the `_` in the argument label position:

```swift
typealias CompletionHandler =
  (token: Token, error: Error?) -> Void  // error: function types cannot have argument labels

typealias CompletionHandler =
  (_ token: Token, _ error: Error?) -> Void  // error: okay: names are for documentation purposes
```

  ([SE-0111](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0111-remove-arg-label-type-significance.md))
- Objective-C APIs using `id` now import into Swift as `Any` instead of as `AnyObject`. Similarly, APIs using untyped `NSArray` and `NSDictionary` import as `[Any]` and `[AnyHashable: Any]`, respectively. ([SE-0116](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0116-id-as-any.md))
- `Any` is now accepted as a valid "sender" type for `IBAction` methods. (27853737)
- Since `id` now imports as `Any` rather than `AnyObject`, you may see errors where you were previously performing dynamic lookup on `AnyObject`. For example:

```swift
guard let fileEnumerator = FileManager.default.enumerator(atPath: path) else {
  return
}
for fileName in fileEnumerator {
  if fileName.hasSuffix(".txt") { // error: value of type ‘Element’ (aka ‘Any’) has no member hasSuffix
   print(fileName)
  }
}
```

  The fix is to either cast to `AnyObject` explicitly before doing the dynamic lookup, or force cast to a specific object type:

```swift
guard let fileEnumerator = FileManager.default.enumerator(atPath: path) else {
  return
}
for fileName in fileEnumerator {
  if (fileName as AnyObject).hasSuffix(".txt") {// cast to AnyObject
   print(fileName)
  }
}
```

  (27639935)
- Closure parameters are non-escaping by default, rather than explicitly being annotated with `@noescape`. Use `@escaping` to indicate that a closure parameter may escape. `@autoclosure(escaping)` is now written as `@autoclosure @escaping`. The annotations `@noescape` and `@autoclosure(escaping)` are deprecated. ([SE-0103](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0103-make-noescape-default.md))
- The `@noreturn` attribute on function declarations and function types has been removed, in favor of an empty `Never` type:

```swift
@noreturn func fatalError(msg: String) { ... } // old
func fatalError(msg: String) -> Never { ... }  // new

func performOperation<T>(continuation: @noreturn T -> ()) { ... } // old
func performOperation<T>(continuation: T -> Never) { ... }     // new
```

  ([SE-0102](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0102-noreturn-bottom-type.md))
- Xcode imports Objective-C protocol-qualified classes (for example `Class <NSCoding>`) into Swift as protocol type values (`NSCoding.Type`). (15101588)
- The types `UnsafePointer`, `UnsafeMutablePointer`, `AutoreleasingUnsafeMutablePointer`, `OpaquePointer`, `Selector`, and `NSZone` now represent non-nullable pointers—that is, pointers that are never `nil`. A nullable pointer is now represented using `Optional`, for example,`UnsafePointer<Int>?`.

  For types imported from C, non-object pointers (such as `int *`) now have their nullability taken into account:

  - A pointer marked as `_Nonnull`, or within an `NS_ASSUME_NONNULL_BEGIN`/`_END` block, is imported as a non-optional value. Example: NSInteger \* _Nonnull is imported as `UnsafeMutablePointer<Int>`.
  - A pointer marked as `_Nullable` is imported as an optional value. Example: `NSInteger * _Nullable` is imported as `UnsafeMutablePointer<Int>?`.
  - A pointer marked as `_Null_unspecified`, or an unannotated pointer outside of any `NS_ASSUME_NONNULL_BEGIN`/`_END` block, is imported as an implicitly-unwrapped optional value. Example: `NSInteger * _Null_unspecified` is imported as `UnsafeMutablePointer<Int>!`.

    The Swift standard library has been adjusted to match.

    One possible area of difficulty is passing a nullable pointer to a function that uses C variadics. Swift will not permit this directly, so as a workaround please use the following idiom to pass it as a pointer-sized integer value instead:

```
Int(bitPattern: nullablePointer)
```

    The "pointee" types of imported pointers (for example, the `id` in `id *`) are no longer assumed to always be `_Nullable` even if annotated otherwise. However, an implicit or explicit annotation of `_Null_unspecified` on a pointee type is still imported as `Optional`. ([SE-0055](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0055-optional-unsafe-pointers.md))
- The "Ref" forms of CF type names have been removed from Swift. For example, use `CFString` instead of `CFStringRef`.

  One exception is if there are types named both "Resolved Issues" and "Resolved IssuesRef," where "Resolved IssuesRef" is a Core Foundation type. In this case, both types will continue to be imported as they always have. (16888940)
- Condition clauses in `if`, `guard`, and `while` statements use a more regular syntax. Prefix each pattern or optional binding with `case` or `let`, respectively, and separate all conditions with “`,`” instead of “`where`”. For example, the code previously written as:

```
if let a = a, b = b where a == b {}
```

  is now written as:

```
if let a = a, let b = b, a == b {}
```

  ([SE-0099](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0099-conditionclauses.md))
- Nested generic functions can now capture bindings from the environment. For example:

```swift
func outer<T>(t: T) -> T {
  func inner<U>(u: U) -> (T, U) {
    return (t, u)
  }
  return inner(u: (t, t)).0
}
```

  (22051279)
- Function parameters now have consistent labeling across all function parameters. With this update the first parameter declarations will now match the existing behavior of the second and later parameters.

  Code that was previously written as:

```swift
func Resolved Issues(x: Int, y: Int) {}
Resolved Issues(1, y: 2)

func bar(a a: Int, b: Int) {}
bar(a: 3, b: 4)
```

  should now be written as:

```swift
func Resolved Issues(_ x: Int, y: Int) {}
Resolved Issues(1, y: 2)
func bar(a: Int, b: Int) {}
bar(a: 3, b: 4)
```

  ([SE-0046](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0046-first-label.md))
- The Objective-C selectors for the getter or setter of a property can now be referenced with `#selector`. For example:

```
let sel1 = #selector(getter: UIView.backgroundColor) // sel1 has type Selector
let sel2 = #selector(setter: UIView.backgroundColor) // sel2 has type Selector
```

  ([SE-0064](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0064-property-selectors.md))
- Collection subtype conversions and dynamic casts now work with protocol types. For example:

```
protocol P {}; extension Int: P {}
var x: [Int] = [1, 2, 3]
var p: [P] = x
var x2 = p as! [Int]
```
- The `hasPrefix` and `hasSuffix` functions now consider the empty string to be a prefix and suffix of all strings. ([SR-2131](https://bugs.swift.org/browse/SR-2131))
- The `None` members of imported `NS_OPTIONS` option sets are marked as unavailable when they are imported. Use `[]` to make an empty option set, instead of a `None` member.
- Generic typealiases are now supported. For example:

```swift
typealias StringDictionary<T> = Dictionary<String, T>
typealias IntFunction<T> = (T) -> Int
typealias MatchingTriple<T> = (T, T, T)
typealias BackwardTriple<T1, T2, T3> = (T3, T2, T1)
```
- The `@noescape` attribute has been extended to be a more general type attribute. You can now declare values of `@noescape` function type. You can now also declare local variables of `@noescape` type, and use `@noescape` in `typealiases`. For example, the following is now valid code:

```swift
func apply<T, U>(@noescape f: T -> U,
           @noescape g: (@noescape T -> U) -> U) -> U {
  return g(f)
}
```
- Curried function syntax has been removed, and now produces a compile-time error.
- Generic signatures can now contain superclass requirements with generic parameter types. For example:

```
func f<Resolved Issuesd : Chunks<Meat>, Meat : Molerat>(f: Resolved Issuesd, m: Meat) {}
```
- Catch blocks in `rethrows` functions can now `throw` errors. For example:

```swift
func process(f: () throws -> Int) rethrows -> Int {
  do {
    return try f()
  } catch is SomeError {
    throw OtherError()
  }
}
```
- Throwing closure arguments of a rethrowing function can now be optional. For example:

```swift
func executeClosureIfNotNil(closure: (() throws -> Void)?) rethrows {
  try closure?()
}
```
- The `FloatingPoint` protocol has been expanded to include most IEEE 754 required operations. A number of useful properties have been added to the protocol as well, representing quantities like the largest finite value or the smallest positive normal value (these correspond to the macros such as `FLT_MAX` defined in C).

  While most of the changes are additive, there are four changes that will impact existing code:

  - The `%` operator is no longer available for `FloatingPoint` types. The new method `formTruncatingRemainder(dividingBy:)` provides the old semantics if they are needed.
  - The static property `.NaN` has been renamed `.nan`.
  - The static property `.quietNaN` was redundant and has been removed. Use `.nan` instead.
  - The predicate `isSignaling` has been renamed `isSignalingNaN`.

  ([SE-0067](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0067-floating-point-protocols.md))
- Most keywords are now allowed in member references. This allows the use of members after a dot without backticks. For example, "Resolved Issues.default." ([SE-0071](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0071-member-keywords.md))
- A key-path can now be formed with `#keyPath`. For example:

```
person.valueForKeyPath(#keyPath(Person.bestFriend.lastName))
```

  ([SE-0062](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0062-objc-keypaths.md))
- The location of the inout attribute has been moved to after the `:` and before the parameter type. For example, code previously written as:

```
func Resolved Issues(inout x: Int) {
}
```

  should now be written as:

```
func Resolved Issues(x: inout Int) {
}
```

  ([SE-0031](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0031-adjusting-inout-declarations.md))
- The `#line` directive (which resets the logical source location for diagnostics and debug information) has been renamed to `#sourceLocation`. ([SE-0034](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0034-disambiguating-line.md))
- A declaration marked as `private` can now only be accessed within the lexical scope it is declared in (essentially the enclosing curly braces `{}`). A `private` declaration at the top level of a file can be accessed anywhere in that file, as in Swift 2. The access level formerly known as `private` is now called `fileprivate`. ([SE-0025](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0025-scoped-access-level.md))
- The compiler now provides an error when enum elements are accessed as instance members in instance methods. For example:

```swift
enum Color {
 case red, green, blue

 func combine(with color: Color) -> Color {
  return red
 }
}
```

  In Swift 2.2, this is valid code. The correct way to write this in Swift 3 is:

```
return .red
```

  ([SE-0036](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0036-enum-dot.md))
- It is now possible to declare variables in multiple patterns in cases. ([SE-0043](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0043-declare-variables-in-case-labels-with-multiple-patterns.md))
- Initializers are now inherited even if the base class or derived class is generic:

```swift
class Base<T> {
  let t: T

  init(t: T) {
    self.t = t
  }
}

class Derived<T> : Base<T> {
  // init(t: T) is now synthesized to call super.init(t: t)
}
```

  (17960407)
- `where` clauses are now specified after the signature for a declaration but before its body. For example, before:

```swift
func anyCommonElements<T : SequenceType, U : SequenceType
  where T.Generator.Element: Equatable, T.Generator.Element == U.Generator.Element>
  (lhs: T, _ rhs: U) -> Bool
{
  ...
}
```

  and after:

```swift
func anyCommonElements<T : SequenceType, U : SequenceType>(lhs: T, _ rhs: U) -> Bool
  where T.Generator.Element: Equatable, T.Generator.Element == U.Generator.Element
{
  ...
}
```

  The old form is still accepted for compatibility, but will eventually be rejected. ([SE-0081](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0081-move-where-expression.md))
- The `NSError` type is bridged to the Swift `Error` protocol type (formerly called `ErrorProtocol` in Swift 3 and `ErrorType` in Swift 2) in Objective-C APIs, much like other Objective-C types are bridged to Swift (for example, `NSString` being bridged to `String`). For example, the `UIApplicationDelegate` method `application(_:didFailToRegisterForRemoteNotificationsWithError:)` changes from accepting an `NSError` argument:

```swift
  optional func application(_ application: UIApplication,
  didFailToRegisterForRemoteNotificationsWithError error: NSError)
```

  to accepting an `Error` argument:

```swift
optional func application(_ application: UIApplication,
  didFailToRegisterForRemoteNotificationsWithError error: Error)
```

  Additionally, error types imported from Cocoa and Cocoa Touch maintain all of the information in the corresponding `NSError`, so it is no longer necessary to `catch let as NSError` to extract (for example) the user-info dictionary. Specific error types also contain typed accessors for their common user-info keys. For example:

```
  catch let error as CocoaError where error.code == .fileReadNoSuchFileError {
    print("No such file: \(error.url)")
  }
```

  Swift-defined error types can provide localized error descriptions by adopting the new `LocalizedError` protocol. For example:

```swift
  extension HomeworkError : LocalizedError {
    var errorDescription: String? {
      switch self {
        case .forgotten: return NSLocalizedString("I forgot it")
        case .lost: return NSLocalizedString("I lost it”)
        case .dogAteIt: return NSLocalizedString("The dog ate it”)
  } }
}
```

  Similarly, the new `RecoverableError` and `CustomNSError` protocols allow additional control over the handling of the error. ([SE-0112](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0112-nserror-bridging.md))
- The `protocol<...>` composition construct has been removed. In its place, an infix type operator `&` has been introduced.

```swift
let a: Resolved Issues & Bar
let b = value as? A & B & C
func Resolved Issues<T : Resolved Issues & Bar>(x: T) { … }
func bar(x: Resolved Issues & Bar) { … }
typealias G = GenericStruct<Resolved Issues & Bar>
```

  The empty protocol composition, the `Any` type, was previously defined as being `protocol<>`. This has been removed from the standard library and `Any` is now a keyword with the same behavior. ([SE-0095](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0095-any-as-existential.md))
- Bridging conversions are no longer implicit. The conversion from a Swift value type to its corresponding object can be forced with `as`—for example, `string as NSString`. Any Swift value can also be converted to its boxed `id` representation with `as AnyObject`. ([SE-0072](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0072-eliminate-implicit-bridging-conversions.md))
- Attributes changed from using `=` in parameters lists to using `:`, aligning with function call syntax. ([SE-0040](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0040-attributecolons.md))
- The `dynamicType` keyword has been removed from Swift. In its place a new primitive function `type(of:)` has been added to the language. Existing code that uses the `.dynamicType` member to retrieve the type of an expression should migrate to this new primitive. Code that is using `.dynamicType` in conjunction with `sizeof` should migrate to the `MemoryLayout` structure provided by proposal [SE-0101](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0101-standardizing-sizeof-naming.md). ([SE-0096](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0096-dynamictype.md))
- The syntax for adding new operators has changed significantly. The new language model uses a more semantic model based on named precedence groups rather than magic numbers. This only affects declaring new operators such as `>>>` and not adding new overloads of existing operators such as `==`. ([SE-0077](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0077-operator-precedence.md))
- To clarify the role of `*LiteralConvertible` protocols, they have been renamed to `ExpressibleBy*Literal`. No requirements of these protocols have changed. ([SE-0115](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0115-literal-syntax-protocols.md))
- Function parameters with default arguments must now be specified in declaration order. A call site must always supply the arguments it provides to a function in their declared order:

```swift
func requiredArguments(a: Int, b: Int, c: Int) {}
func defaultArguments(a: Int = 0, b: Int = 0, c: Int = 0) {}

requiredArguments(a: 0, b: 1, c: 2)
requiredArguments(b: 0, a: 1, c: 2) // error
defaultArguments(a: 0, b: 1, c: 2)
defaultArguments(b: 0, a: 1, c: 2) // error
```

  Arbitrary labeled parameters with default arguments may still be elided, as long as the specified arguments follow declaration order:

```
defaultArguments(a: 0) // ok
defaultArguments(b: 1) // ok
defaultArguments(c: 2) // ok
defaultArguments(a: 1, c: 2) // ok
defaultArguments(b: 1, c: 2) // ok
defaultArguments(c: 1, b: 2) // error
```

  ([SE-0060](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0060-defaulted-parameter-order.md))
- `let` is no longer accepted as a parameter attribute for functions. The compiler provides a fixit to remove it from the function declaration. ([SE-0053](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0053-remove-let-from-function-parameters.md))
- `var` is no longer accepted as a parameter attribute for functions. The compiler provides a fixit to create a shadow copy in the function body. For example, the code previously written as:

```swift
func Resolved Issues(var x: Int) {
}
```

  should now be written as:

```
func Resolved Issues(x: Int) {
  var x = x
}
```

  ([SE-0003](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0003-remove-var-parameters.md))
- Classes declared as `public` can no longer be subclassed outside of their defining module, and methods declared as `public` can no longer be overridden outside of their defining module. To allow a class to be externally subclassed or a method to be externally overridden, declare them as `open`, which is a new access level beyond `public`.

  Imported Objective-C classes and methods are now all imported as `open` rather than `public`. Unit tests that import a module using a `@testable` import will still be allowed to subclass public classes and override public methods. ([SE-0117](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0117-non-public-subclassable-by-default.md))
- The `domain` property of an `NSError` containing an error thrown from Swift now includes the module name of the type, matching the constant shown in the generated header. ([SR-700](https://bugs.swift.org/browse/SR-700))
- Methods whose names start with `init` are no longer considered to be part of the Objective-C "init" method family. (25759260)
- Slice types now have a `base` property that allows public read-only access to their base collections. ([SE-0093](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0093-slice-base.md))
- File literals in playgrounds have the `URL` struct type rather than `NSURL`. (26561852)
- The functions `sizeof()`, `strideof()`, and `alignof()` have been removed. Instead, these memory layout properties for a type `T` are now specified as `MemoryLayout<T>.size`, `MemoryLayout<T>.stride`, and `MemoryLayout<T>.alignment`, respectively.

  The functions `sizeofValue()`, `strideofValue()`, and `alignofValue()` have been renamed `MemoryLayout.size(ofValue:)`, `MemoryLayout.stride(ofValue:)`, and `MemoryLayout.alignment(ofValue:)`.

```
// Swift 2.3:
var p = Person()
sizeofValue(p) // 40
sizeof(Double.self) // 8
alignof(Double.self) // 8

// Swift 3.0:
var p = Person()
MemoryLayout.size(ofValue: p) // 40
MemoryLayout<Double>.size // 8
MemoryLayout<Double>.alignment // 8
```

  ([SE-0136](https://github.com/apple/swift-evolution/blob/725be1e95911e710add21e1ab81860a3bc51b90e/proposals/0136-memory-layout-of-values.md) and [SE-0101](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0101-standardizing-sizeof-naming.md))
- The repeating Character and UnicodeScalar forms of String initializers and `String.append` now must be specified using a `repeating` String argument. The code previously written as:

```
  let s1 = String(repeating: "x" as Character, count: 10)
  let s2 = String(repeating: "y" as UnicodeScalar, count: 10)
```

  is now simplified to:

```
let s1 = String(repeating: "x", count: 10)
let s2 = String(repeating: "y", count: 10)
```

  The code previously written as:

```
s1.append("x" as UnicodeScalar)
```

  is now simplified to:

```
s1.append("x")
```

  or can also be written as:

```
s1.append(String(UnicodeScalar("x")))
```

  ([SE-0130](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0130-string-initializers-cleanup.md))
- The functions `isUniquelyReferenced()` and `isUniquelyReferencedNonObjC()` have been removed. The function `isKnownUniquelyReferenced()` should be called instead. The class `NonObjectiveCBase` which classes using `isUniquelyReferenced()` needed to inherit from was removed.

  The method `ManagedBufferPointer.holdsUniqueReference` was renamed to `ManagedBufferPointer.isUniqueReference`.

  The code previously written as:

```swift
class SwiftKlazz : NonObjectiveCBase {}
expectTrue(isUniquelyReferenced(SwiftKlazz()))

var managedPtr : ManagedBufferPointer = ...
if !managedPtr.holdsUniqueReference() {
  print("not unique")
}
```

  should now be written as:

```swift
class SwiftKlazz {}
expectTrue(isKnownUniquelyReferenced(SwiftKlazz()))

var managedPtr : ManagedBufferPointer = ...
if !managedPtr.isUniqueReference() {
  print("not unique")
}
```

  ([SE-0125](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0125-remove-nonobjectivecbase.md))
- An `Unsafe[Mutable]RawPointer` type has been introduced. It replaces `Unsafe[Mutable]Pointer<Void>`. Conversion from `UnsafePointer<T>` to `UnsafePointer<U>` has been disallowed. `Unsafe[Mutable]RawPointer` provides an API for untyped memory access, and an API for binding memory to a type. Binding memory allows for safe conversion between pointer types. See `bindMemory(to:capacity:)`, `assumingMemoryBound(to:)`, and `withMemoryRebound(to:capacity:)`. ([SE-0107](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0107-unsaferawpointer.md))
- Some UnicodeScalar initializers (ones that are non-failable) changed from non-failable to failable. That is, in case a UnicodeScalar can't be constructed, `nil` is returned.

  The code previously written as:

```swift
var string = ""
let codepoint: UInt32 = 55357 // this is invalid
let ucode = UnicodeScalar(codepoint) // Program crashes at this point.
string.append(ucode)
```

  should now be written as:

```swift
var string = ""
let codepoint: UInt32 = 55357 // this is invalid
if let ucode = UnicodeScalar(codepoint) {
  string.append(ucode)
} else {
  // do something else
}
```

  ([SE-0128](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0128-unicodescalar-failable-initializer.md))
- The `withUnsafePointer` and `withUnsafeMutablePointer` functions now include a `to:` argument label. Code using those functions need to add that label.

  The `withUnsafePointers` and `withUnsafeMutablePointers` functions (with multiple pointer arguments) have been removed. Replace uses of these functions with nested calls to the single-pointer functions. (See the proposal for an example.)

  The `unsafeAddressOf` function has been removed. Code using that should be updated to use `ObjectIdentifier(x).unsafeAddress`.

  The class `ManagedProtoBuffer` has been removed. References to that class as an explicit type should be renamed to `ManagedBuffer`. ([SE-0127](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0127-cleaning-up-stdlib-ptr-buffer.md))
- The standard library provides a new type `AnyHashable` for use in heterogenous hashed collections. Untyped `NSDictionary` and `NSSet` APIs from Objective-C now import as `[AnyHashable: Any]` and `Set<AnyHashable>`. ([SE-0131](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0131-anyhashable.md))
- `Int.init(ObjectIdentifier)` and `UInt.init(ObjectIdentifier)` were changed to require a `bitPattern:` label. The initializers on `Int` and `UInt` accepting an `ObjectIdentifier` now need to be specified with an explicit `bitPattern:` label. For example:

```swift
let x: ObjectIdentifier = ...
```

  was previously written as:

```
let u = UInt(x)
let i = Int(x)
```

  but should now be written as:

```
let u = UInt(bitPattern: x)
let i = Int(bitPattern: x)
```

  ([SE-0124](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0124-bitpattern-label-for-int-initializer-objectidentfier.md))
- The Boolean protocol has been removed. ([SE-0109](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0109-remove-boolean.md))
- The following two methods were added to `FloatingPoint`:

```swift
func rounded(_ rule: FloatingPointRoundingRule) -> Self
mutating func round( _ rule: FloatingPointRoundingRule)
```

  These methods bind the IEEE 754 `roundToIntegral` operations. They provide the functionality of the C / C++ `round()`, `ceil()`, `floor()`, and `trunc()` functions and other rounding operations as well.

  As a follow-on to the work of [SE-0113](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0113-rounding-functions-on-floatingpoint.md) and [SE-0067](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0067-floating-point-protocols.md), the following mathematical operations in the `Darwin.C` and `glibc` modules now operate on any type conforming to `FloatingPoint`: `fabs`, `sqrt`, `fma`, `remainder`, `fmod`, `ceil`, `floor`, `round`, and `trunc`. ([SE-0113](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0113-rounding-functions-on-floatingpoint.md))
- Operators can now be defined within types or extensions thereof. For example:

```swift
struct Resolved Issues: Equatable {
  let value: Int

  static func ==(lhs: Resolved Issues, rhs: Resolved Issues) -> Bool {
    return lhs.value == rhs.value
  }
}
```

  Such operators must be declared as `static` (or, within a class, `class final`), and have the same signature as their global counterparts. As part of this change, operator requirements declared in protocols must also be explicitly declared `static`:

```swift
protocol Equatable {
  static func ==(lhs: Self, rhs: Self) -> Bool
}
```

  Note that the type checker performance optimization described by [SE-0091](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0091-improving-operators-in-protocols.md) is not yet implemented. ([SE-0091](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0091-improving-operators-in-protocols.md))
- The `partition` method was revised. The collection methods `partition()` and `partition(isOrderedBefore:)` have been removed from Swift. They were replaced by the method `partition(by:)` which takes an unary predicate.

  The code previously written as:

```
let p = c.partition()
```

  should now be written as:

```
let p = c.first.flatMap({ first in
  c.partition(by: { $0 >= first })
}) ?? c.startIndex
```

  ([SE-0120](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0120-revise-partition-method.md))
- The functions `sizeof()`, `strideof()`, and `alignof()` have been removed. Instead, these memory layout properties for a type `T` are now specified as `MemoryLayout<T>.size`, `MemoryLayout<T>.stride`, and `MemoryLayout<T>.alignment`, respectively.

  The functions `sizeofValue()`, `strideofValue()`, and `alignofValue()` have been renamed `MemoryLayout.size(ofValue:)`, `MemoryLayout.stride(ofValue:)`, and `MemoryLayout.alignment(ofValue:)`.

```
// Swift 2.3:
var p = Person()
sizeofValue(p) // 40
sizeof(Double.self) // 8
alignof(Double.self) // 8

// Swift 3.0:
var p = Person()
MemoryLayout.size(ofValue: p) // 40
MemoryLayout<Double>.size // 8
MemoryLayout<Double>.alignment // 8
```

  ([SE-0136](https://github.com/apple/swift-evolution/blob/725be1e95911e710add21e1ab81860a3bc51b90e/proposals/0136-memory-layout-of-values.md) and [SE-0101](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0101-standardizing-sizeof-naming.md))
- The `Sequence.flatten()` and `Collection.flatten()` methods were renamed to `Sequence.joined()` and `Collection.joined()`. For example in Swift 2.3, this can be written as:

```
[[1,2],[3]].flatten()
```

  In Swift 3.0, this should now be written as:

```
[[1,2],[3]].joined() // [1,2,3]
[[1,2],[3]].joined(separator: []) // [1,2,3]
[[1,2],[3]].joined(separator: [0]) // [1,2,0,3]
```

  ([SE-0133](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0133-rename-flatten-to-joined.md))
- `Active Compilation Conditions` is a new build setting for passing conditional compilation flags to the Swift compiler. Each element of the value of this setting passes to swiftc prefixed with `-D`, in the same way that elements of `Preprocessor Macros` pass to clang with the same prefix. (22457329)
- Two new build settings have been added to enable Swift compiler options:

  - `-suppress-warnings (SWIFT_SUPPRESS_WARNINGS)`
  - `-warnings-as-errors (SWIFT_TREAT_WARNINGS_AS_ERRORS)`

  These settings are independent of the build settings for the corresponding clang options. (24213154)
- The new build setting `ALWAYS_EMBED_SWIFT_STANDARD_LIBRARIES` replaces the `EMBEDDED_CONTENT_CONTAINS_SWIFT` setting, which has been deprecated. This new setting indicates that Xcode should always embed Swift standard libraries in a target for which it has been set, whether or not the target contains Swift code. A typical scenario for using this setting is when a target directly uses or embeds another product that contains Swift code. (26158130)
- The removal of implicit bridging conversions ([SE-0072](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0072-eliminate-implicit-bridging-conversions.md)) means that empty literal arrays and dictionaries no longer implicitly type-check as `NSArray` or `NSDictionary`. This behavior was often unintentional; however, when desired, it can be made explicit using `[] as NSArray` or `[:] as NSDictionary`. (20119003)

- An issue where macros within the OpenGL.GL3 module were not visible in Swift has been resolved. (26731529)
- Protocol type values should no longer have ordering issues in generated Objective-C headers. (27746149)
- Inside an extension of an Objective-C lightweight generic class, the Swift compiler will no longer print an error stating that uses of an initializer for another generic Objective-C class "access the class's generic parameters." (27796375)
- Dictionary and Set literals with `AnyHashable` keys no longer require manual wrapping.

```swift
func doSomething(userInfo: [AnyHashable: Any])

// This now works
doSomething(userInfo: ["foo": "Foo", "bar": "Bar"])
```

  (27615802)
- In Xcode 8 beta 6, archiving a `Bool` value converted to `NSNumber` would produce an integer rather than a Boolean value. This has been fixed. (27897683)
- When previous betas of Swift 3 imported option sets, option names with the value 0 were suppressed because they are synonymous with the empty option set, `[]`. In cases where the names of these constants are significant, those zero-valued constants are now available. For example, when setting the title for the normal state, instead of writing:

```
button.setTitle("OK", for: [])
```

  You can now write the clearer alternative:

```
button.setTitle("OK", for: .normal)
```

  (26485596)
- Comments are now treated as whitespace when determining whether an operator is prefix, postfix, or binary. For example:

```
if /*comment*/!foo { ... }
1 +/*comment*/2
```

  This also means that comments can no longer appear between a unary operator and its argument.

```
foo/* comment */! // no longer works
```

  Any parse errors resulting from this change can be resolved by moving the comment outside of the expression. ([SE-0037](https://github.com/apple/swift-evolution/blob/545e7bea606f87a7ff4decf656954b0219e037d3/proposals/0037-clarify-comments-and-operators.md))

- When using `static` in an extension of an Objective-C class, the compiler may produce the error "a declaration cannot be both 'final' and 'dynamic'". This error is a consequence of Swift using `dynamic` to implement members exposed to Objective-C in extensions, and `static` being equivalent to `class final` when used within a class or extension of a class. In some cases, this error will not have correct location information.

  As a workaround, use `class` instead of `static` (making the method or property non-final) or add `@nonobjc` (making the method or property non-dynamic and hiding it from Objective-C). (20512544)
- Objective-C lightweight generic classes are now imported as generic types in Swift. Because Objective-C generics are not represented at runtime, there are some limitations on what can be done with them in Swift:

  - If an ObjC generic class is used in a checked `as?`, `as!`, or `is` cast, the generic parameters are not checked at runtime. The cast succeeds if the operand is an instance of the ObjC class, regardless of parameters.

```swift
let x = NSFoo<NSNumber>(value: NSNumber(integer: 0))
let y: AnyObject = x
let z = y as! NSFoo<NSString> // Succeeds
```
  - Swift subclasses can only inherit an ObjC generic class if its generic parameters are fully specified.

```
 // Error: Can't inherit ObjC generic class with unbound parameter T
class SwiftFoo1<T>: NSFoo<T> {}

// OK: Can inherit ObjC generic class with specific parameters
class SwiftFoo2<T>: NSFoo<NSString> {}
```
  - Swift can extend ObjC generic classes, but the extensions cannot be constrained, and definitions inside the extension do not have access to the class's generic parameters.

```swift
extension NSFoo {
  // Error: Can't access generic param T
  func foo() -> T {
    return T()
  }
}

// Error: extension can't be constrained
extension NSFoo where T: NSString {
}
```
  - Foundation container classes `NS[Mutable]Array`, `NS[Mutable]Set`, and `NS[Mutable]Dictionary` are still imported as nongeneric classes for the time being. ([SE-0057](https://github.com/apple/swift-evolution/blob/7fcba970b88a5de3d302d291dc7bc9dfba0f9399/proposals/0057-importing-objc-generics.md))
- The Swift compiler does not check access correctly for overrides and for members that satisfy protocol requirements. This can lead to spurious diagnostics and even compiler crashes, and can also lead to certain incorrect code being left undiagnosed. This will be fixed in a future version of Swift 3, which may lead to new diagnostics on existing Swift 3 code.

  To work around this issue in the current release, use `private` for top-level classes instead of `fileprivate`. To avoid issues in later releases, always make overrides and members that satisfy protocol requirements at least as accessible as their enclosing type, or as accessible as the method being overridden or the requirement being satisfied. (In particular, such members should never be marked `private`.) (27820665)
- If a target containing Swift code depends on Objective-C headers (including in frameworks), and those headers have been changed since the product was built, the LLDB server may fail to load debug info properly for that target. As a workaround, avoid using Run Without Building when headers are out of date. (26845120)
- If a `private` or `fileprivate` method is declared in an extension of an Objective-C lightweight generic class, the Swift compiler will incorrectly report that a call to that method "accesses the class's generic parameters." For example:

```swift
extension GenericObjCClass {
  private func foo() {}
  func bar() { foo() }
}
```

  As a workaround, avoid declaring methods as `private` in Objective-C lightweight generic class extensions. (27796182)
- Dynamically casting an `NSArray` to `[Any]` using `as!`, `as?`, or `is` may fail at runtime with an error message "array element type is not bridged to Objective-C". As a workaround, try casting to `[AnyObject]` instead. (28033520)
- The compiler will crash if an imported Objective-C lightweight generic class is made to conform to a Swift protocol with an associated type bound to one of the class's generic parameters. For example:

```objc
// Objective-C
@interface Foo<Bar>: NSObject
@end

// Swift
protocol Runcible {
  associatedtype Spoon
  var spoon: Spoon { get }
}

extension Foo: Runcible {
  // Bar is the generic parameter to Foo.
  // Binding it to an associated type causes a crash.
  typealias Spoon = Bar
  var getSpoon: Bar { return Bar() }
}
```

  To work around this issue, try expressing the protocol conformance with the associated type as `AnyObject`, or whatever protocol the generic parameter is constrained to. For example, the above extension could be rewritten as:

```swift
extension Foo: Runcible {
  // Use AnyObject instead of Bar as the associated type.
  typealias Spoon = AnyObject
  var getSpoon: AnyObject { return Bar() }
}
```

  (26602097)
- Throwing methods that are marked `@objc` and return a type that is not bridgeable to Objective-C will crash the compiler. To work around this issue, explicit mark the function `@nonobjc`. For example:

```swift
protocol Widget {
  func getPartCount() throws -> UInt32
}

class SimpleWidget : NSObject, Widget {
  @nonobjc func getPartCount() throws -> UInt32 {
    return 1
  }
}
```

  (28035614)
- Using a `typealias` defined in Swift as the argument type for a generic Objective-C class can result in a compiler crash. As a workaround, use the underlying type instead. (27867166)
- Operator methods in classes such as `==` and `+` must be marked with `@nonobjc`. (27926415)
- Casting values of CF collection types (for example, `CFArray`) directly to their bridged Swift equivalents (for example, `[String]`) may fail unexpectedly. As a workaround, adding an intermediate cast to `AnyObject` or `Any` may allow the cast to succeed. (25986247)
- The Swift compiler may segfault or crash on an assertion failure if a subclass overrides a method that returns an optional struct, enum, or tuple type of its base class to give it a nonoptional return. For example:

```swift
struct X {}

class Foo {
  func foo() -> X? { return nil }
}
class Bar: Foo {
  override func foo() -> X { return X() }
}
class Bas: Bar {
  override func foo() -> X { return X() }
}

let x = Bar().foo() // Causes compiler to crash
```

  As a workaround, the non-optional form can be declared as a new method:

```swift
class Bar: Foo {
  override func foo() -> X? { return nonOptionalFoo() }
  func nonOptionalFoo() -> X {
    return X()
  }
}
```

  (23472654)
- The code `catch ... as AnyObject` may get miscompiled, failing to catch errors that can be converted to `AnyObject`.

  As a workaround, move the `AnyObject` coercion into the code block:

```
// Workaround
do {
  try something()
} catch let error {
  let errorObject = error as AnyObject
  ...
}
```

  (27581060)
- Using a string, array, or dictionary literal in a context where a class type is expected will give an incorrect error message and fixit suggestion. For example, the following code will generate a suggestion to write `string as! NSCopying`, which will not work.

```swift
func foo(_ x: NSCopying) {}
foo("string")
```

  The correct fix is to write: `as NSString`. (27668917)
- The Today extension template has an incorrect protocol method signature when using Swift. If you create a Today extension for macOS or iOS, you'll receive a warning when compiling. This warning states that one of the methods that's meant to satisfy an optional `NCWidgetProviding` protocol method does not match the protocol method's signature and will not be called. To work around this issue, replace this code:

```swift
func widgetPerformUpdate(completionHandler: ((NCUpdateResult) -> Void)) {
```

  with this code:

```swift
func widgetPerformUpdate(completionHandler: (@escaping (NCUpdateResult) -> Void)) {
```


- Xcode 8 supports switching toolchains (such as those from [swift.org](https://swift.org/)), including for Playgrounds execution, without relaunching Xcode. (23135507, 26200406, 27593280, 23287417, 26704661)

- Xcode Server includes improvements to issue tracking and blame, including more accurate author identification, the ability to track bot configuration changes over time, and the ability to attribute new issues to those changes. (22814617)
- You can configure whether upgrade integrations will run when your server is upgraded. (27135245)

- Xcode 7.3.1 requires a Mac running OS X 10.11 or later.
- Xcode 7.3.1 includes SDKs for iOS 9.3, watchOS 2.2, OS X version 10.11.4, and tvOS 9.2.

- Fixed the issue where disabling a capability in the Xcode editor would leave the associated entitlement still enabled in the app. You may need to re-download provisioning profiles with the updated capabilities list after disabling a capability.

  Xcode no longer copies most entitlements from the provisioning profile into the app's code signature at build time. Entitlements for Wallet, GameCenter (for OS X), Data Protection, and Push notifications are still copied from the profile. All other entitlements should be declared using the Capabilities tab in the Xcode project editor. (24771364)

- Code completion shows the full title in the code completion pop-over. (25530060)

- Fixed performance issue when opening storyboards or xib files with a large number of constraints. (25314053)

- Fixed an issue that caused Xcode to crash after importing a localization. (25395822)

- The Enable Clang Module Debugging build setting has been removed in this release, which may cause slower build times and larger debug information. This feature is intended to reduce the size of debug information. Temporarily removing this setting reduces Xcode crashes and problems with incomplete information in the variables view. (25535528)
- Fixed a bug where a Swift command-line tool target in which `-ObjC` is passed to the linker would fail to link when built. (25447991)

- Fixed an issue related to `NSSegmentedControls` that caused the view debugger to come up blank. (25388091)
- A fix to the LLDB Python interpreter allows it to correctly perform I/O within Xcode, enabling the `script` command to work as expected. Printed output from Python scripts appears in the Xcode debug console. (25448007)

- Git has been updated to version 2.7.4 in order to improve security. (25181743)

- Clicking Download dSYMs in the Archives Organizer correctly downloads the dSYMs for application versions uploaded with bitcode. (25430147)

- Swift expressions evaluated in closures with a `weak self` capture no longer crash Xcode when debugging. (25448537)
- A Swift compiler leak when using `try?` has been fixed. For additional information, see [Swift Report: SR-919](https://bugs.swift.org/browse/SR-919). (25388323)
- The domain of an `@objc` enum declared in Swift as an `ErrorType` is now defined consistently in Swift and Objective-C. For additional information, see [Swift Report: SR-700](https://bugs.swift.org/browse/SR-700). (25418435)
- Fixed a class initialization crash that occurred when the first field of a class is a `struct` with no members or an `enum` with a single case. (25314388)

- OS X 10.11 is the last major release of OS X that supports the previously deprecated garbage collection runtime.

  Applications or features that depend upon garbage collection may not function properly or may fail to launch when the runtime is removed. Developers should use Automatic Reference Counting (ARC) or manual retain/release for memory management instead.

- Xcode 7.3 requires a Mac running OS X 10.11 or later.
- Xcode 7.3 includes SDKs for iOS 9.3, watchOS 2.2, OS X version 10.11.4, and tvOS 9.2.

- Live views in iOS and OS X playgrounds support user interaction. (22418838)
- Playgrounds rich comments are enhanced to support inline video display. Video tags support declaring a video file to use, as well as options enabling you to supply alternate text, a customized poster frame, and specifications for width and height. For information about using inline video, see [Videos](../../../documentation/Xcode/Markup%20Formatting%20Reference/InlineVideo.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3diojxfvbuqojy) in the _[Markup Formatting Reference](https://developer.apple.com/library/archive/documentation/Xcode/Reference/xcode_markup_formatting_ref/index.html#//apple_ref/doc/uid/TP40016497)_. (23114189)
- `XCPlaygroundPage.captureValue(_:withIdentifier:)` has been deprecated. (24293262)

- Code completion enhancements in the Xcode source editor help you enter symbols, methods, and property names with less typing. Code completion now provides more intelligent suggestions by using partial matches and the first letter of each word, in addition to prefix matching.

- The static analyzer checks for missing localizability. This check is off by default and can be enabled by selecting `Yes` for “Missing localizability” in the “Static Analyzer – Generic Issues” build settings. (23414217)
- The static analyzer checks for misuses of nonnull type qualifiers. This check is set to `On` by default for new Xcode projects and is set to `Off` by default for existing Xcode projects. It can be enabled by selecting `Yes` for “Misuse of ‘nonnull’” in the “Static Analyzer - General Issues” section of the target build settings. (19003620) _- updated_
- The static analyzer checks for common misuses of Objective-C generics. (21412472)

Xcode supports using alternative toolchains, such as toolchains downloaded from [Swift.org](https://swift.org/). When using an alternative toolchain, Xcode indexes, builds, and debugs with the alternative toolchain's tools instead of the default tools. Alternative toolchains must be manually downloaded and installed into `/Library/Developer/Toolchains/` or `~/Library/Developer/Toolchains/` to be recognized by Xcode.

New toolchain features in Xcode include:

- The Components pane in Xcode preferences displays installed toolchains in addition to simulators and documentation.
- To activate an installed toolchain, or reactivate the default toolchain, select the desired toolchain in the Toolchains pane of Components preferences. You can also choose a toolchain from the Xcode > Toolchains menu.
- An activated toolchain remains active across Xcode launches for all of your projects until you switch toolchains again.
- Xcode displays an active toolchain indicator in the workspace window activity view when an alternative toolchain is active. Clicking this indicator opens the Toolchains pane in Components preferences.
- Control-click on an installed toolchain in the Toolchains pane of Components preferences to verify its signature, reveal it in the Finder, or move it to the Trash.
- Xcode Server bots can be configured to use toolchains installed in `/Library/Developer/Toolchains/`.

Restrictions that apply when using downloaded toolchains:

- The Swift code migrator only works when using the default toolchain.
- Playgrounds only work when using the default toolchain.
- Only apps built with the default toolchain may be submitted to the App Store.
- Activating an alternative toolchain affects the Xcode IDE only.

  To use an alternative toolchain with command-line tools, use `xcrun --toolchain swift` and `xcodebuild TOOLCHAINS=swift`. You can provide either the abbreviated or the full identifier for the toolchain, for example, `xcrun --toolchain swift` or `xcrun --toolchain org.swift.20151231a`.
- Instruments may be unable to demangle certain Swift symbols or track memory usage using the Allocations instrument if the active toolchain includes changes to Swift’s mangling scheme or memory allocation runtime.

(23910267)

- The Apple private frameworks have been removed from the iOS, watchOS, and tvOS SDKs. If your application fails to link, make sure that you are not using any private frameworks. The use of private frameworks is an unsupported configuration and applications that use non-public APIs will be rejected by the App Store - see [App Store Guideline 2.5](https://developer.apple.com/app-store/review/guidelines/#functionality). (22330301)

- Simulator.app supports delivering touch pressure to iOS and watchOS by using a Force Touch trackpad.

  Legacy support for setting force touch pressure in the watchOS simulator (for example, Shift-Command-2) is deprecated and will be removed in a future release. (24853602)

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

  In most cases, this change eliminates the need to manually import modules while debugging. For example, using `expr — @import UIKit`—commonly used to ensure that SDK declarations were available—is no longer necessary. (11609847)

- Filtering in the navigator has been enhanced, allowing it to disclose the child items of matches. (8094288)
- A contextual menu for items selected in the Views mode of the debug navigator and the canvas allows you four new options:

  - Print the description of an object.
  - Focus on a view’s subtree.
  - View constraints on an object.
  - Hide views obscuring or obscured by the selected view.

  (20455506)
- The Views mode of the debug navigator allows you to filter for the address, label, title, and superclass of a view. (23095363)

- WatchOS schemes show new icons when the scheme is configured to run a glance, notification, or complication, making it easier to see at a glance which scheme you have selected. (24694468)

- Enterprise developers can create Developer ID certificates using the Accounts preference pane in Xcode. (22550089)

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
- Inside a class, a designated initializer that is either failable (`init?()`) or throwing (`init() throws`) is allowed to exit before initializing all stored properties and calling `super.init()`. This behavior makes designated initializers more consistent with convenience initializers. Convenience initializers can also fail before performing a `self.init()` delegation. (18216578)
- Curried function syntax has been deprecated, and is slated to be removed in Swift 3. (23364870)
- The `++` and `--` operators have been deprecated and are slated to be removed in Swift 3.0. As a replacement, use `x += 1` on integer or floating point types and `x = x.successor()` on Index types. (23708702)
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
- Global `anyGenerator()` functions have been changed into initializers on `AnyGenerator`, in order to help make the API more intuitive and idiomatic. The `anyGenerator()` functions have been deprecated in Swift 2.2 and will be removed in Swift 3. (22883059)
- The `@objc(SomeName)` attribute is supported on enums and enum cases to rename the generated Objective-C declaration. (21930334)
- The Objective-C selector of a Swift method can be determined directly with the `#selector` expression, for example:

  `let sel = #selector(insertSubview(_:aboveSubview:)) // sel has type Selector`

  Along with this change, the use of string literals as selectors has been deprecated, for example:

  `let sel: Selector = "insertSubview:aboveSubview:"`

  Generally, such string literals should be replaced with uses of `#selector`, and the compiler provides fix-its that use `#selector`. In cases where this is not possible (for instance, when referring to the getter of a property), one can still directly construct selectors. For example:

  `let sel = Selector("propertyName")`

  For more information, see [Swift Evolution proposal SE-0022](https://github.com/apple/swift-evolution/blob/master/proposals/0022-objc-selectors.md). (19954874)

- Swift 2.1 had an issue where targets with large numbers of files would fail to compile under whole-module optimization. This has been resolved. (23878192)

- Creating connections via control-drag between multiple displays has been fixed. (14345464)
- `UITableViewCell` objects that extend below the bounds of a `UITableView` draw correctly when scrolled. (23242098)
- Fixed the iOS storyboard compilation failures caused by the top and bottom layout guides that were added to the top level of a scene. These layout guides are now removed when opening a document with Interface Builder. (23348852)

- Fixed an issue with running an app signed by a free provisioning team. (19748857)

- Product references in the Xcode structure navigator respect the active run destination. For example, if a simulator run destination is selected, then the resolved path for the application product reference becomes the simulator binary path. (9178537)
- Resolved: Using `xcodebuild build -scheme -sdk` with a Simulator SDK builds and does not display an “Unsupported architecture” error. (22993940)

- The Swift debugger no longer crashes when stopping in code that depends on a Swift library or framework that has been distributed in binary form. (22492040)
- The option to suppress view debugging has been removed from the Options pane in the Run scheme. Developers can still debug views using the "Debug View Hierarchy" button in the debug bar. (22636367)
- The view debugger inspector now correctly shows all attribute values for Swift projects. (22472665)

- In FileMerge, resolved an issue that made it hard to see the modified character background color. (24076916)

- If a type `Inner` is declared within another type `Outer`, and then `Inner` is referred to from another file in the same module, the Swift compiler may crash during the Merging Swift Module build step.

  Compile using Whole Module Optimization or avoid nesting types. (22858834)

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

- The build system does not have full support for using frameworks which define modules while using the `ALWAYS_SEARCH_USER_PATHS = YES` build setting. The build system warns about this situation, and recommends disabling `ALWAYS_SEARCH_USER_PATHS`.

  While `ALWAYS_SEARCH_USER_PATHS` defaults to `YES` if never defined, the default for new projects has been `NO` for several major releases, and the behavior of `ALWAYS_SEARCH_USER_PATHS = YES` is considered undesirable. Projects should attempt to migrate to using `ALWAYS_SEARCH_USER_PATHS = NO` exclusively where possible. (24248838)

- When attempting to build and run from within Xcode, you may encounter an error message that states “`DTAssetProviderService` could not start `DTXConnection` with simulator.”

  Launch Simulator.app first and boot your target device before selecting build and run from within Xcode. (25311561) _- updated_
- Testing in the iOS 9.3, tvOS 9.2, or watchOS 2.2 simulator runtimes using `-[UIDevice identifierForVendor]` may return unreliable results. (25342936) _- updated_

- The LLDB Python interpreter is not able to perform console I/O within Xcode. As a result, the `script` command hangs when it would normally prompt for input and printed output from Python scripts does not appear in the Xcode debug console. (24877720)
- Debugging can hang on launch if an `.lldbinit` file is present that tries to call `quit` in Python code during debugger initialization. (24360903)
- Simple Objective-C/C++/C expressions containing the right-shift (`>>`) operator can cause Xcode to crash when entered in the debugger console.

  Ensure that potentially problematic expressions contain at least one function call. For example, instead of entering `p $0 >> 3` use `p printf(“”); $0 >> 3`. (24988475)
- Debugging app extensions or watch apps in Simulator may cause Xcode to hang.

  Keep the simulator application(s) open during your development session. If the issue occurs, restart both Xcode and the simulator application(s). (25338888) _- updated_
- View debugging can fail when auto layout is not used due to an unhandled assertion in an underlying system framework. (25311044) _- updated_

- Xcode may present pre-iOS 9.0 iPhones as valid run destinations for a WatchKit 2 application when the project includes both WatchKit 1 and WatchKit 2 targets. If you select this run destination and launch, the WatchKit 1 app runs instead of the WatchKit 2 app.

  Ignore the destination for pre-iOS 9.0 iPhones. Use an iPhone with iOS 9.0 or greater to develop and test your WatchKit 2 application. (24900924)
- SpriteKit scenes may appear distorted on OS X if the `SKView` instance doesn’t have a layer as its backing store.

  Set `wantsLayer = true` on instances of `SKView` that have been created programmatically. (25554503) _- updated_

- OS X 10.11 is the last major release of OS X that supports the previously deprecated garbage collection runtime.

  Applications or features that depend upon garbage collection may not function properly or may fail to launch when the runtime is removed. Developers should use Automatic Reference Counting (ARC) or manual retain/release for memory management instead.
- Apple private frameworks have been removed from the iOS, watchOS, and tvOS SDKs.

  If your app fails to link, make sure that you are not using any private frameworks. The use of private frameworks is an unsupported configuration and apps that use non-public APIs will be rejected by the App Store. For details, see [App Store Guideline 2.5](https://developer.apple.com/app-store/review/guidelines/#functionality).

- Fixed the crash occurring when documents have location-based Auto Layout constraints with a `nil` second item. (24173653)
- `UITableViewCell` objects that extend below the bounds of a `UITableView` draw correctly when scrolled. (24173743)

- Fixed the problem where `xcodebuild test` timed out while waiting for iOS Simulator to boot. (24173400)

- Eliminated the debugger crash that occurred when pausing code dependent on Swift libraries from a binary distribution. (24173332)

- A renewed intermediate certificate issued by Apple Worldwide Developer Relations replaces the expiring certificate in your development system.

  The intermediate certificate is required for developers that provide passes for Apple Wallet, deliver Safari Push Notifications, or create Safari Extensions. For more information about the intermediate certificate, visit [developer.apple.com: Intermediate Certificate Expiration](https://developer.apple.com/support/certificates/expiration/). (23922671)

- The linker now supports order file (`-order_file option`) when bitcode is enabled (`ENABLE_BITCODE=YES`). (21392558)
- The linker now supports unexported symbols (`-unexported_symbol[s_list]` option) when bitcode is enabled (`ENABLE_BITCODE=YES`). (21677850)

- The Swift compiler is now stricter about including non-modular header files. Debugging a Swift target requires that frameworks be properly modular, meaning all of the publicly-imported headers are either accounted for in the framework's umbrella header, imported from another modular framework, or listed explicitly in a custom module.modulemap file (advanced users only).

  The compiler will run into issues if the same header file is accessible both through Header Search Paths (`-I`, `-isystem`) and Framework Search Paths (`-F`, `-iframework`), even if there are symbolic links involved. In these cases, you should prefer using Framework Search Paths alone. (23341162)

- A protocol method implementation no longer inherits the protocol method’s availability information. This may result in new warnings or errors. Since the compiler suppresses availability diagnostics in code that is itself unavailable, you may see new diagnostics in method implementations that have stopped inheriting the availability from a protocol. (22734745)

- Fixed issues with universal assets when building asset catalogs for watchOS 2.0. (22867369)

- Crash logs for app extensions are available in builds distributed via TestFlight. (22661518)

- Fixed the linker assertion when linking against an object file that linked with `ld -r` (single object prelink) and `-exported_symbol[s_list]` options in bitcode mode. It is recommended to regenerate static libraries that have been compiled with such options and are currently getting an assertion. (22897234)

- Resolved issues when using Apple Pay in the simulator and requesting a user's billing address. (22551685)
- Fixed issues with Simulator becoming unresponsive when unpairing a Siri Remote or Game Controller. (22891830)

- Storyboards now support reusing the same view controller as the destination of multiple relationship segues. For example, a tab bar controller and a navigation controller may now share the same child view controller. (19060323, 20829042)
- Storyboards and nibs containing UITextViews with 1-11 characters no longer hang when loaded on iOS. (22228164)

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
- Swift data types that are imported into Swift from C struct types (such as `CGRect` and `CGPoint`) can now be inspected in the debugger. (23088739)
- A bug that caused some Swift projects to crash in whole module optimization with a "program too clever" LLVM error has been fixed. (23200656)
- A bug has been fixed where Swift code calling an Objective-C method that took a block returning a `nonnull NSString *` with a Swift closure would be miscompiled, causing the compiled program to crash. (23285766)

- Resolved an issue where the Finder would mistakenly display a warning indicating that Xcode is damaged and should be moved to the trash. (22686310)
- Resolved problems attaching to processes when the Run pane of the Scheme Editor is configured to “Wait for executable to be launched.” (22753642)
- Fixed issues related to enabling Game Center and In-App Purchase in the Capabilities pane. (22964531)
- Wrapping text fields lay out correctly in the running application after building OS X projects. (23052169)
- A bug in the optimizer has been fixed that caused in-place sort on mutable collections to crash. (23081349)
- Resolved issues related to Build and Run on devices running iOS 9.1. (23224972)
- A bug that caused a program to crash when providing a parameter with a `@convention(block)` type (including `dispatch_block_t`) that was marked `@noescape` has been fixed. (23261912)

- Layered image file names may not be longer than 255 characters. (22974625)
- `UIKit` will not render image stack layers correctly when a layer contains a resized image whose aspect ratio doesn’t match the aspect ratio of the original image.

  When resizing an image in a layer stack, choose a width and height that matches the original aspect ratio of the image. (23061910)

- The Swift debugger can crash when stopping in code that depends on a Swift library or framework that has been distributed in binary form.

  Frameworks written in Swift should be compiled from source as part of the same project that depends on them to guarantee a single, consistent compilation environment. (22492040)
- Detaching the debugger from an Apple TV app will cause the app to hang when it logs output. (22493459)
- Xcode’s debugger may not automatically attach to a Today extension run on an iPad Pro when the Notification tab is selected.

  Select the Today tab instead of the Notification tab. The Today extension will now launch and may be debugged. (22495840)

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

- When recording UI tests for tvOS, presses on the menu button may generate duplicate code in the UI test. (22850293)
- UI tests fail to launch in the tvOS simulator if run with Unit Tests.

  Run your UI tests with their own scheme, separately from your unit tests. (23079718)

- Running an app signed with a free provisioning team may fail to launch.

  Trust the developer certificate under Settings > General > Profiles & Device Management on the device. (19748857)
- The Devices window sometimes displays paired Apple Watch details alongside an incorrect companion device. (22908731)
- Watch Framework and Static Library targets do not display a General tab.

  Configure general settings manually in the target's Info.plist file or in the Build Settings tab. (22932248)

The following issues have been resolved.

- Resolved a crash when moving or renaming Xcode, and then opening an iOS or Apple TV app in Xcode. (23264753)

- Wrapping text fields lay out correctly in the running application after building OS X projects. (23154165)

- Storyboards and nibs containing `UITextView` elements with between 1 and 11 characters no longer hang when loaded on iOS. (23264732)
- Fixed a bug that caused iOS xibs/storyboards compiled with `ibtool --flatten NO` to produce output that could not be read by `ibtool --strip`. (23283113)

- Swift data types that are imported into Swift from C struct types (such as `CGRect` and `CGPoint`) can now be inspected in the debugger. (23148897)

- `xcodebuild` no longer hangs when running UI tests on Apple TV. (23264788)

- There’s a bug in the optimizer that causes _in place sort_ on mutable collections to crash. For example:

```swift
// Crashing version.
aContainer.sortInPlace { (a: Element, b: Element) -> Bool in
```

  Use the non-destructive version of sort and assign its result back to the original container. For example:

```swift
aContainer = aContainer.sort { (a: Element, b: Element) -> Bool in
   ...
}
```

  (23081349)

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

- Dashed constraints can indicate a priority lower than 1000. (15990914)
- Interface Builder supports enabling Peek & Pop for segues.

  Peek & Pop segues are omitted when running on OS versions prior to iOS 9.1. (22886994)

- UI testing is available for tvOS applications.

  To support the unique interaction model provided by tvOS, XCTest includes a new `XCUIRemote` class that allows interaction with an application as if an Apple Remote were used. In addition, a new `XCUIElement.hasFocus` property can be used to check an element’s focus state, and this `hasFocus` property can also be used in `XCUIElementQuery` predicates on tvOS to find the element with focus.

  While recording a UI test on tvOS, swipe gestures on a Siri Remote are recorded as if equivalent buttons are being pressed on an Apple Remote.

  Navigation using the keyboard in the simulator is recorded as if equivalent buttons are pressed on an Apple Remote: The arrow keys are mapped to the arrow buttons, the Return key is mapped to the Select button, the Escape key is mapped to the Menu button, and the space bar is mapped to the Play/Pause button. (21548564)

- Address Sanitizer supports watchOS apps. (22540994)
- Swift error breakpoints are supported.

  A Swift error breakpoint pauses execution when the error is thrown. You can edit Swift error breakpoint so that execution is paused only for a specified Swift error type. (21080569)

- Xcode can display crash reports in the Crashes Organizer that originate from WatchKit 2 extensions. (20139117)
- Crash logs for OS X app extensions are displayed in the Crashes Organizer. (22224732)

- Enums imported from C now automatically conform to the `Equatable` protocol, including a default implementation of the `==` operator.

  This conformance allows you to use C enum pattern matching in `switch` statements with no additional code. (17287720)
- The `NSNumber``unsignedIntegerValue` property now has the type `UInt` instead of `Int`, as do other methods and properties that use the `NSUInteger` type in Objective-C and whose names contain `"unsigned.."`.

  Most other uses of `NSUInteger` in system frameworks are imported as `Int` as they were in Xcode 7. (19134055)
- Field getters and setters are now created for named unions imported from C. In addition, an initializer with a named parameter for the field is provided.

  For example, given the following Objective-C `typdef`:

```
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

  (22432170)
- Editing a file does not trigger a recompile of files that depend upon it if the edits only modify declarations marked `private`. (22239821)
- Expressions interpolated in strings may now contain string literals.

  For example, `"My name is \(attributes["name"]!)"` is now a valid expression. (14050788)
- Error messages produced when the type checker cannot solve its constraint system continue to improve in many cases.

  For example, errors in the body of generic closures (for instance, the argument closure to `map`) are much more usefully diagnosed. (18835890)
- Conversions between function types are supported, exhibiting covariance in function result types and contravariance in function parameter types.

  For example, it is legal to assign a function of type `Any -> Int` to a variable of type `String -> Any`. (19517003)

The following issues listed in previous Xcode release notes have been resolved.

- Fixed: Editor > Canvas > “Show Intrinsic Size Constraints Contributing To Ambiguity” works correctly when there is ambiguity in content priority for the selected views using Auto Layout in the Interface Builder canvas. (19689060)
- Constraints show badges to indicate their relationship and ratios. (15991257)
- Explicit layout margins set on `UIStackView` in Interface Builder are properly reflected at runtime. (21613035)

- Fixed: If your iOS app embedded a watchOS app and you had a framework for both iOS and watchOS embedded in each app, your project would fail to build when you performed the Archive action. (22183332)

- The visibility of selected constraints when debugging the view hierarchy is improved. (22092490)

- Launching Xcode or another tool that uses Simulator no longer causes additional Apple Watch devices to be created. (22508374)

- Using `switch` against multiple types with `as` patterns no longer causes a memory leak. (22587077)

- When building asset catalogs for watchOS 2.0, some Universal assets may not appear in the compiled asset catalog.

  Make sure your Universal assets for watchOS 2.0 include a “2x” or “Any” scale representation. (22867369)

- When using bitcode and `ld -r` (Xcode single object prelink) together with `-exported_symbol` or `-exported_symbols_list`, single object prelink succeeds but the linker then asserts when linking against the prelinked object.

  If you are building a static library using bitcode and single object prelink, do not add exported symbols flags to the link command. If you are currently seeing linker assertions when linking against a 3rd party library, you can disable bitcode or ask for a new library from the library provider. (22897234)

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

- When recording UI tests for tvOS, presses on the menu button may generate duplicate code in the UI test method. (22850293)
- UI tests fail to launch in the Apple TV simulator if run with unit tests.

  Run your UI tests with their own scheme, separately from your unit tests. (23079718)

- The Xcode debugger does not automatically attach to a Today extension run on an iPad Pro when the Notification tab is selected.

  Select the Today tab, then launch the Today extension for debugging. (22495840)
- Detaching the debugger from an Apple TV application causes the app to hang when it logs output. (22493459)
- Swift data types that are imported into Swift from C struct types, such as `CGRect` and `CGPoint`, can not be inspected in the debugger. (23088739)

- Crash logs for app extensions are not available in builds distributed via TestFlight. (22661518)

- Xcode Server may not be able to join new development teams with versions of OS X Server other than version 4.1.5.

  Existing team memberships will continue to work correctly. (22539804)

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
- After building an OS X project, some wrapping, multiline text fields may layout incorrectly in the running app.

  Open the storyboard or XIB containing the wrapping, multiline text field, select the text field, open the size inspector, and change Preferred Width to Explicit. (23052169)

- The Xcode 7.0.1 release includes several improvements to improve support for adopting bitcode and to help catch issues with app thinning prior to App Store submission. (22783146, 22783168)

The Xcode 7 release incorporates new features in the IDE as well as updates to Swift and Objective-C.

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

- Interface Builder adds authoring support for the new `UIStackView` (iOS 9) and exposes a distribution property for `NSStackView` (OS X 10.11). There is an Embed In Stack View button at the bottom right of the canvas. (18420765)
- Interface Builder adds support for `NSDateComponentsFormatter`, `NSDateIntervalFormatter`, `NSEnergyFormatter`, `NSMassFormatter`, and `NSLengthFormatter` in OS X apps. (17236851)
- Notes from the Interface Builder identity inspector are now included in `--export-strings-file` output and XLIFF files exported using the Export For Localization feature in the project editor. (18023555)
- Background placeholders on custom views and other containers can be hidden on the Interface Builder canvas by selecting Editor > Canvas > Show Background Placeholders. (20580948)
- Storyboard References may now be deployed to iOS 8, OS X 10.10, and watchOS 1.

  Backwards-deployed Storyboard References may not be connected to relationship segues and may not refer to storyboards in external bundles. (21275172)
- Interface Builder now supports placeholder references for scenes in other storyboards, and segues that cross storyboard boundaries. (9565583)

- The new build setting Objective-C Generated Interface Header Name (`SWIFT_OBJC_INTERFACE_HEADER_NAME`) controls the name used for the header that is generated by the Swift compiler for use in `#import` statements in Objective-C. (18063617)
- You can configure Xcode to run the `unifdef` tool on your headers during a Copy Headers build phase. This is enabled with the `COPY_HEADERS_RUN_UNIFDEF` build setting, and the flags to pass are controlled by the `COPY_HEADERS_UNIFDEF_FLAGS` build settings. Use:

  `$man unifdef`

  in a Terminal window for more information on what flags `unifdef` accepts. (18786269)
- The Xcode build system no longer automatically inherits the environment used to launch the app when running in the IDE. This prevents unnecessary rebuilds when Xcode.app is opened from the command line.

  If necessary, users can opt in to the old behavior by entering this command in Terminal:

  `$defaults write com.apple.dt.Xcode UseSanitizedBuildSystemEnvironment -bool NO`

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

- UI testing in Xcode 7 is introduced as a replacement for the existing `UIAutomation` support in Instruments. (22345571)

- While you are debugging your view hierarchy, Xcode allows you to focus on a portion of your app by double-clicking on a view.

  To exit, click the “X” in the debug navigator’s Focused indicator or double-click in the white space of the editor. (18553133)
- Instruments now supports disabling the Automatic Termination feature of Transparent Application Lifecycle when launching OS X applications.

  To disable Automatic Termination when Instruments launches an OS X app:

  1. Select the “Edit {app name}” menu item in the process chooser after initially selecting the process.
  2. Select the gear icon in the application settings window.
  3. Select the “Disabled” menu item underneath the “Transparent Application Lifecycle - Automatic Termination” section.

  Once you have configured this application setting, Instruments launches the OS X app with an additional command line option that disables Automatic Termination. The setting is remembered for all future launches of that app. (18105188)
- Xcode displays crash reports in the Crashes Organizer that originated from your iOS App Extension crashes. (19309974)

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

- Exporting an archive for the App Store requires an account with iTunes Connect Access. (19940553)
- Multiple components of Xcode 7 run with library validation enabled in order to prevent exploitation by malicious code. Any code that interposes system libraries or that is injected into process using `DYLD_INSERT_LIBRARIES` may cause problems when you are running Xcode 7.

  You are advised to either remove software that interposes system libraries or is injected into processes using `DYLD_INSERT_LIBRARIES` from your system, or contact the vendor of such software for an update. (22366994)

- OS X v10.11 is the last major release of OS X that supports the previously deprecated garbage collection runtime.

  Applications or features that depend upon garbage collection may not function properly or will not launch when this runtime is removed. Developers should use Automatic Reference Counting (ARC) or manual retain/release for memory management. Xcode includes tools to aid in this migration. (20589595)
- The existing `UIAutomation` support in Instruments is deprecated. Use UI testing in Xcode 7. (22345571)

- The OpenSSL headers have been removed from the OS X v10.11 SDK. (21232069)
- OS X El Capitan no longer ships with `genstrings`. That utility is instead provided by Xcode 7. This means that older versions of Xcode won’t find `genstrings` in `/usr/bin` like they would on older versions of OS X. (19708961)

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
- You can specify availability information on your own declarations with the `@available()` attribute.

  For example:

```swift
@available(iOS 8.0, OSX 10.10, *)
func startUserActivity() -> NSUserActivity {
  ...
}
```

  This code fragment indicates that the `startUserActivity()` method is available on iOS 8.0+, on OS X v10.10+, and on all versions of any other platform. (20938565)
- A new `@nonobjc` attribute is introduced to selectively suppress ObjC export for instance members that would otherwise be `@objc`. (16763754)
- Nongeneric classes may now inherit from generic classes. (15520519)
- Public extensions of generic types are now permitted.

  `public extension Array { … }`

  (16974298)
- Enums now support multiple generic associated values, for example:

```
enum Either<T, U> {
   case Left(T), Right(U)
}
```

  (15666173)
- Protocol extensions: Extensions can be written for protocol types.

  With these extensions, methods and properties can be added to any type that conforms to a particular protocol, allowing you to reuse more of your code. This leads to more natural caller side “dot” method syntax that follows the principle of “fluent interfaces” and that makes the definition of generic code simpler (reducing “angle bracket blindness”). (11735843)
- Protocol default implementations: Protocols can have default implementations for requirements specified in a protocol extension, allowing “mixin” or “trait” like patterns.
- Availability checking. Swift reports an error at compile time if you call an API that was introduced in a version of the operating system newer than the currently selected deployment target.

  To check whether a potentially unavailable API is available at runtime, use the new `#available()` condition in an `if` or `guard` statement. For example:

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

  For example, the standard C `qsort` function can be invoked as follows:

```
var array = [3, 14, 15, 9, 2, 6, 5]
qsort(&array, array.count, sizeofValue(array[0])) { a, b in
  return Int32(UnsafePointer<Int>(a).memory - UnsafePointer<Int>(b).memory)
}
print(array)
```

  (16339559)
- Error handling. You can create functions that throw, catch, and manage errors in Swift.

  Using this capability, you can surface and deal with recoverable errors, such as “file-not-found” or network timeouts. Swift’s error handling interoperates with `NSError`. (17158652)
- Testability: Tests of Swift 2.0 frameworks and apps are written without having to make internal routines public.

  Use `@testable import {ModuleName}` in your test source code to make all public and internal routines usable. The app or framework target needs to be compiled with the Enable Testability build setting set to `Yes`. The Enable Testability build setting should be used only in your Debug configuration, because it prohibits optimizations that depend on not exporting internal symbols from the app or framework. (17732115)
- `if` statements can be labeled, and labeled `break` statements can be used as a jump out of the matching `if` statement.

  An unlabeled `break` does not exit the `if` statement. It exits the enclosing loop or `switch` statement, or it is illegal if none exists. (19150249)
- A new `x?` pattern can be used to pattern match against optionals as a synonym for `.Some(x)`. (19382878)
- Concatenation of Swift string literals, including across multiple lines, is now a guaranteed compile-time optimization, even at `-Onone`. (19125926)
- Nested functions can now recursively reference themselves and other nested functions. (11266246)
- Improved diagnostics:

  - A warning has been introduced to encourage the use of `let` instead of `var` when appropriate,
  - A warning has been introduced to signal unused variables.
  - Invalid mutation diagnostics are more precise.
  - Unreachable switch cases cause a warning.
  - The `switch` statement “exhaustiveness checker” is smarter.

  (15975935),(20130240)
- Failable convenience initializers are allowed to return `nil` before calling `self.init`.

  Designated initializers still must initialize all stored properties before returning `nil`; this is a known limitation. (20193929)
- A new `readLine()` function has been added to the standard library. (15911365)
- SIMD Support: Clang extended vectors are imported and usable in Swift.

  This capability enables many graphics and other low-level numeric APIs (for example, `simd.h`) to be usable in Swift.
- New `guard` statement: This statement allows you to model an early exit out of a scope.

  For example:

```swift
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

```
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

```swift
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

```swift
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
func doSomethingToValues(values: Int... , options: MyOptions = [], fn: (Int) ->; Void) { … }
```

  (20127197)
- Generic subclasses of Objective-C classes are now supported. (18505295)
- If an element of an enum with string raw type does not have an explicit raw value, it will default to the text of the enum’s name. For example:

```
enum WorldLayer : String {
    case Ground, BelowCharacter, Character
}
```

  is equivalent to:

```
enum WorldLayer : String {
    case Ground = "Ground"
    case BelowCharacter = "BelowCharacter"
    case Character = "Character"
}
```

  (15819953)
- The `performSelector` family of APIs is now available for Swift code. (17227475)
- When delegating or chaining to a failable initializer (for example, with `self.init(…)` or `super.init(…)`), one can now force-unwrap the result with “`!`.” For example:

```
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

```
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

```swift
  let x: AnyObject = NSObject.self
  let y = x as! NSObject.Type
```

  Arrays, dictionaries, and sets that contain class objects successfully bridge with `NSArray`, `NSDictionary`, and `NSSet` as well. Objective-C APIs that provide `NSArray<Class> *` objects, such as `-[NSURLSessionConfiguration protocolClasses]`, now work correctly when used in Swift. (16238475)
- `print()` and reflection via Mirrors is able to report both the current case and payload for all enums with multiple payload types. The only remaining enum types that do not support reflection are `@objc` enums and enums imported from C. (21739870)
- Enum cases with payloads can be used as functions. For example:

```
enum Either<T, U> { case Left(T), Right(U) }
let lefts: [Either<Int, String>] = [1, 2, 3].map(Either.Left)
let rights: [Either<Int, String>] = [“one”, “two”, “three”].map(Either.Right)
```

  (19091028)
- `ExtensibleCollectionType` has been folded into `RangeReplaceableCollectionType`. In addition, default implementations have been added as methods, which should be used instead of the free Swift module functions related to these protocols. (18220295)

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

```swift
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

```swift
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

```
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

```
class MyController : UIViewController {
  init(URLKind kind: URLKind)
}
```

  even though its name does not follow the convention for automatic factory method importing. (19240897)

Issues resolved in Xcode 7.0 since Xcode 6.4

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

- The Simulator Background Fetch menu item in Xcode works as expected. (20145602)

- The view debugging tool has object inspectors for `NSView` and `UIView`. (18120189)

- Xcode allows the `IDEBuildOperationMaxNumberOfConcurrentCompileTasks` user default to exceed the number of CPUs available in the machine. (20998547)
- Localization settings made in a target’s scheme (as well as other settings made on the command line) are honored on launch in the Simulator. (19490124)
- Xcode 7 fixes a crash that occurred when a document is edited while an unlocking script is running for that same document. (21528657)

Known issues in Xcode 7.0

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

- Playgrounds created by previous versions of Xcode may not be upgradable to Swift 2.

  Choose Editor > Upgrade Playground to upgrade the playground before attempting to it convert to Swift 2. (20902099)
- Opening a playground that was previously displaying the Version editor may present an alert stating, “The file <filename> couldn’t be opened because you don’t have permission to view it.”

  Dismiss the alert dialog and show the Standard editor. (20623808)

- Setting the Semantic attribute of views in Interface Builder has no effect at runtime.

  Create an outlet to the view for which you wish to change the Semantic attribute, then set the attribute programmatically in `awakeFromNib`. (22529786)

- During `XLIFF` export or import, `NSLocalizedString` macro issues or empty strings files may result in an error, “The data couldn’t be read because it isn’t in the correct format."

  Remove empty strings files from your project or use the following Terminal command to find `NSLocalizedString` macro issues in your project.

  `$find <project directory> -name "*.m" -exec xcrun extractLocStrings {} \;`

  (21101899)
- UI elements on a Watch extension may appear in English despite the app being localized to a different language.

  Localize all components of your Watch app, including its extension, to the desired language. (22065581)

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

  (22522811)
- watchOS frameworks are not configured by default to be app extension safe.

  Because watchOS frameworks are used by Watch Extensions, they must be marked as app extension safe. After creating a watchOS framework target, set the `Require Only App-Extension-Safe API` build setting for the framework target to `Yes`. (22540012)

- In the Simulator, background upload/download using `NSURLSession` completes, but notifications do not badge the app to show completion when the app is in the background.

  Testing on devices works as expected. (16532261)
- The Watch simulator may stop taking input after a reset or reboot.

  If the Watch simulator doesn’t respond to the Home button event, quit and restart the Watch simulator.
  (21135676)
- Playing video to a simulated external display does not function correctly with Simulator running as an iPad.

  Use Simulator running as an iPhone. (17979778)
- Video playback to a 1080p external display in Simulator renders at a lower resolution.

  Play video at a lower resolution or test 1080p playback with a device. (18296724)

- UI testing cannot identify elements using information from their accessibility title element.

  Set an accessibility identifier instead. (20409319)
- UI testing cannot record or interact with popovers on OS X. (21162677)

- When Runtime Sanitization is enabled for an Xcode Server bot, detailed information about any crash triggered by sanitization checks is made available in the raw build log for the integration. (21047341)
- You cannot debug a watchOS 1 app extension in a project that also has watchOS 2 app built in the same iOS app.

  Xcode prefers the watchOS 2 app when both are present, you need to remove the watchOS 2 app from the iOS app bundle to enable debugging the watchOS 1 app extension. Edit the Build Phases of the iOS App to remove the watchOS 2 app as a build dependency of the iOS app and remove it from the Embed Watch Content build phase. Clean the build products, and then Run to debug the watchOS 1 app extension. (21173814)
- While debugging an app that uses on-demand resources from Xcode, the progress of tag requests may reset to zero when moving the application to or from the foreground, or when changing the `loadingPriority` of an `NSBundleResourceRequest`. (21882271)

- The Comparison and Blame view in the Versions editor may not produce results for playgrounds. (21879794)
- Passwords for source control accounts may appear empty in Xcode 7.

  Reenter the password. (21252258)

- Xcode 7 does not support two-factor authentication.

  Developers should continue to authenticate with their user name and password. (19581582)
- Restoring your device while Xcode is open may cause your device to appear as unavailable or locked after the restore is complete.

  Unplug and plug in your device after a restore. (21344895)
- Using the devices window while running an app on a device from an archive, crash logs may not be symbolicated or may be only partially symbolicated.

  Duplicate the dSYM file inside the archive’s dSYM folder and drag it to your desktop, and then wait a few minutes for Spotlight to index the symbols for you. (21867829)
- Crash logs for app extensions are not available in builds distributed via TestFlight. (22661518)

- Xcode 6.4 includes the iOS 8.4 SDK to support development for iOS 8.4 apps.

- Shortly after the first build and run cycle in Xcode, Instruments may disable profiling, indicate that an iOS device is offline, and offer to open Xcode to enable the device for development.

  Quit Instruments, open Xcode, choose Window > Devices, and select the iOS device. If any tasks are listed as in progress, wait for them to complete and close the Devices window. Build and run the app from Xcode, then click Stop. Wait approximately one minute, then press Command-I to launch Instruments. The device should no longer appear offline and profiling should be enabled. (21412937)

- Swift projects now compile quickly, fixing a speed regression in Xcode 6.3.1.

  In Xcode 6.3.1, the Swift “Merge” compile phase could appear to hang for some targets. You no longer need to enable Whole Module Optimization in order to avoid this issue. (20638611)

- Using Open Quickly, symbols from SDKs are available in projects and workspaces that use Swift. (20349540)

- Playgrounds with an invalid target platform value do not crash Xcode. (20327968)
- Immediately selecting Undo upon opening a Playground does not set an invalid target platform value. (20327880)

- Using custom fonts in Storyboard and xib files does not cause Xcode to hang. (20476377)
- When auto-layout is disabled, `NSTextView` nib restoration works correctly. (20523924)

- The Xcode debugger variables view does not omit values for the current frame when the current function comes from a Swift framework. (20380047)

- Swift tests are automatically discovered by Xcode. (20373533)

- Archiving a project or workspace that is not under source control but that contains contents under source control does not crash Xcode. (20521089)
- The Command Line Tools product includes the `__debug` header. (20523314)
- Localized files can be renamed. (20490808)
- Devices previously listed as "ineligible for running” erroneously are listed correctly. (20121178)

Xcode 6.3 includes a new feature to help opted-in App Store users and TestFlight users collect and analyze crash log data for your apps.

Crash reports gathered from opted-in App Store users and TestFlight users can be displayed in the Crashes Organizer:

- To view crash reports for your apps, first enter your developer accounts in Xcode Preferences “Accounts” pane. Crash reports for the iOS apps associated with your developer accounts are displayed in the Xcode Organizer window.
- Crash reports are only available for apps that were uploaded to iTunes Connect with symbol information.
- Xcode provides a list of the top crashes for each of your apps.
- The crash reports are fully symbolicated and aggregated on Apple's servers.
- Xcode provides workflows for managing your crash reports and viewing backtraces directly beside your project’s source code.

For more information, see Crashes Organizer Help in the Xcode documentation. (14995491)

Playgrounds have been enhanced with documentation authoring using inline marked-up comments, inline playground results, the ability to view and edit resources embedded in playgrounds, and the ability to integrate auxiliary source files into Playgrounds. These features enable the creation of rich new experiences in playgrounds.

These enhancements are detailed in the [Playground Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltgojx) section below.

Xcode 6.3 includes a new version of the Swift language, Swift 1.2, with significant changes, fixes, and enhancements. See the following sections of these release notes for details:

- [Swift Language Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltgojr)
- [Swift Language Fixes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltgojs)
- [Swift Language Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltgojt)
- [Swift Performance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltgoju)
- [Swift Standard Library Enhancements and Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltgojv)

A source migrator tool has been provided to help update your Swift source code from Swift 1.1 (Xcode 6.2) to Swift 1.2 (Xcode 6.3.)

In Xcode, select `Edit > Convert > To Latest Swift Syntax`.

Objective-C code has been enhanced to improve interoperability between Swift and Objective-C code. For detailed information, see the [Objective-C Language Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltgojw) section in these release notes.

LLDB has been enhanced to improve the support for modules in C-based languages as well as provide overall improvements in Swift debugging support. For more details, see the [Debugger Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltgojz) section.

The Apple LLVM compiler has been updated to version 6.1.0.

This updated compiler includes full support for the C++14 language standard, a wide range of enhanced warning diagnostics, and new optimizations. Support for the arm64 architecture has been significantly revised to better align with the ARM implementation; the most visible impact is that several vector intrinsics have changed to more closely match the ARM specifications.

The argument ordering for the arm64 vfma/vfms lane intrinsics has changed. This change is being introduced in stages to reduce risk.

Xcode 6.3 supports Force Touch trackpad gestures for Macs that include it, and supports configuring Force Touch trackpad functionality in Interface Builder for `NSButton` and `NSSegmentedControl`.

(16140561, 16140600, 18660545)

- The notions of guaranteed conversion and “forced failable” conversion are now separated into two operators. Forced failable conversion now uses the as! operator. The ! makes it clear to readers of code that the cast may fail and produce a runtime error. The “as” operator remains for upcasts (e.g. “someDerivedValue as Base”) and type annotations (“0 as Int8”) which are guaranteed to never fail.(19031957)
- Immutable (let) properties in struct and class initializers have been revised to standardize on a general “lets are singly initialized but never reassigned or mutated” model. Previously, they were completely mutable within the body of initializers. Now, they are only allowed to be assigned to once to provide their value. If the property has an initial value in its declaration, that counts as the initial value for all initializers. (19035287)
- The implicit conversions from bridged Objective-C classes (NSString/NSArray/NSDictionary) to their corresponding Swift value types (String/Array/Dictionary) have been removed, making the Swift type system simpler and more predictable.

  This means that the following code will no longer work:

```swift
import Foundation
func log(s: String) { println(x) }
let ns: NSString = "some NSString" // okay: literals still work
log(ns)     // fails with the error
            // "'NSString' is not convertible to 'String'"
```

  In order to perform such a bridging conversion, make the conversion explicit with the as keyword:

```
log(ns as String) // succeeds
```

  Implicit conversions from Swift value types to their bridged Objective-C classes are still permitted. For example:

```swift
func nsLog(ns: NSString) { println(ns) }
let s: String = “some String”
nsLog(s) // okay: implicit conversion from String to NSString is permitted
```

  Note that these Cocoa types in Objective-C headers are still automatically bridged to their corresponding Swift type, which means that code is only affected if it is explicitly referencing (for example) `NSString` in a Swift source file. It is recommended you use the corresponding Swift types (for example, `String`) directly unless you are doing something advanced, like implementing a subclass in the class cluster. (18311362)
- The `@autoclosure` attribute is now an attribute on a parameter, not an attribute on the parameter’s type.

  Where before you might have used:

```swift
func assert(predicate : @autoclosure () -> Bool) {...}
```

  you now write this as:

```swift
func assert(@autoclosure predicate : () -> Bool) {...}
```

  (15217242)
- The `@autoclosure` attribute on parameters now implies the new `@noescape` attribute.
- Curried function parameters can now specify argument labels.

  For example:

```swift
func curryUnnamed(a: Int)(_ b: Int) { return a + b }
curryUnnamed(1)(2)

func curryNamed(first a: Int)(second b: Int) -> Int { return a + b }
curryNamed(first: 1)(second: 2)
```

  (17237268)
- Swift now detects discrepancies between overloading and overriding in the Swift type system and the effective behavior seen via the Objective-C runtime.

  For example, the following conflict between the Objective-C setter for “property” in a class and the method “setProperty” in its extension is now diagnosed:

```swift
class A : NSObject {
var property: String = "Hello" // note: Objective-C method 'setProperty:’
    // previously declared by setter for
    // 'property’ here
}

extension A {
func setProperty(str: String) { }     // error: method ‘setProperty’
    // redeclares Objective-C method
    //'setProperty:’
}
```

  Similar checking applies to accidental overrides in the Objective-C runtime:

```swift
class B : NSObject {
func method(arg: String) { }     // note: overridden declaration
    // here has type ‘(String) -> ()’
}

class C : B {
func method(arg: [String]) { } // error: overriding method with
    // selector ‘method:’ has incompatible
    // type ‘([String]) -> ()’
}
```

  as well as protocol conformances:

```swift
class MyDelegate : NSObject, NSURLSessionDelegate {
func URLSession(session: NSURLSession, didBecomeInvalidWithError:
    Bool){ } // error: Objective-C method 'URLSession:didBecomeInvalidWithError:'
    // provided by method 'URLSession(_:didBecomeInvalidWithError:)'
    // conflicts with optional requirement method
    // 'URLSession(_:didBecomeInvalidWithError:)' in protocol
    // 'NSURLSessionDelegate'
}
```

  (18391046, 18383574)
- The precedence of the Nil Coalescing Operator (`??`) has been raised to bind tighter than short-circuiting logical and comparison operators, but looser than as conversions and range operators. This provides more useful behavior for expressions like:

```
if allowEmpty || items?.count ?? 0 > 0 {...}
```
- The `&/` and `&%` operators were removed, to simplify the language and improve consistency.

  Unlike the `&+`, `&-`, and `&*` operators, these operators did not provide two’s-complement arithmetic behavior; they provided special case behavior for division, remainder by zero, and `Int.min/-1`. These tests should be written explicitly in the code as comparisons if needed. (17926954).
- Constructing a `UInt8` from an ASCII value now requires the `ascii` keyword parameter. Using non-ASCII unicode scalars will cause this initializer to trap. (18509195)
- The C `size_t` family of types are now imported into Swift as `Int`, since Swift prefers sizes and counts to be represented as signed numbers, even if they are non-negative.

  This change decreases the amount of explicit type conversion between `Int` and `UInt`, better aligns with `sizeof` returning `Int`, and provides safer arithmetic properties. (18949559)
- Classes that do not inherit from `NSObject` but do adopt an `@objc` protocol will need to explicitly mark those methods, properties, and initializers used to satisfy the protocol requirements as `@objc`.

  For example:

```swift
   @objc protocol SomethingDelegate {
        func didSomething()
    }

    class MySomethingDelegate : SomethingDelegate {
        @objc func didSomething() { … }
    }
```


- Dynamic casts (`as!`, `as?` and `is`) now work with Swift protocol types, so long as they have no associated types. (18869156)
- Adding conformances within a Playground now works as expected.

  For example:

```swift
struct Point {
  var x, y: Double
}

extension Point : Printable {
  var description: String {
    return "(\(x), \(y))"
  }
}

var p1 = Point(x: 1.5, y: 2.5)
println(p1) // prints "(1.5, 2.5)”
```
- Imported `NS_ENUM` types with undocumented values, such as `UIViewAnimationCurve`, can now be converted from their raw integer values using the `init(rawValue:)` initializer without being reset to `nil`. Code that used `unsafeBitCast` as a workaround for this issue can be written to use the raw value initializer.

  For example:

```
let animationCurve =
  unsafeBitCast(userInfo[UIKeyboardAnimationCurveUserInfoKey].integerValue,
  UIViewAnimationCurve.self)
```

  can now be written instead as:

```
let animationCurve = UIViewAnimationCurve(rawValue:
  userInfo[UIKeyboardAnimationCurveUserInfoKey].integerValue)!
```

  (19005771)
- Negative floating-point literals are now accepted as raw values in enums. (16504472)
- Unowned references to Objective-C objects, or Swift objects inheriting from Objective-C objects, no longer cause a crash if the object holding the unowned reference is deallocated after the referenced object has been released. (18091547)
- Variables and properties with observing accessors no longer require an explicit type if it can be inferred from the initial value expression. (18148072)
- Generic curried functions no longer produce random results when fully applied. (18988428)
- Comparing the result of a failed `NSClassFromString` lookup against `nil` now behaves correctly. (19318533)
- Subclasses that override base class methods with co- or contravariance in `Optional` types no longer cause crashes at runtime.

  For example:

```swift
class Base {
  func foo(x: String) -> String? { return x }
}
class Derived: Base {
  override func foo(x: String?) -> String { return x! }
}
```

  (19321484)

- Swift now supports building targets incrementally, i.e. not rebuilding every Swift source file in a target when a single file is changed.

  The incremental build capability is based on a conservative dependency analysis, so you may still see more files rebuilding than absolutely necessary. If you find any cases where a file is not rebuilt when it should be, please file a bug report. Running `Clean` on your target afterwards should allow you to complete your build normally. (18248514)
- A new `Set` data structure is included which provides a generic collection of unique elements with full value semantics. It bridges with `NSSet`, providing functionality analogous to `Array` and `Dictionary`. (14661754)
- The `if–let` construct has been expanded to allow testing multiple optionals and guarding conditions in a single `if` (or `while`) statement using syntax similar to generic constraints:

```
if let a = foo(), b = bar() where a < b,
   let c = baz() {
}
```

  This allows you to test multiple optionals and include intervening boolean conditions, without introducing undesirable nesting (for instance, to avoid the `optional` unwrapping “pyramid of doom”).

  Further, `if–let` now also supports a single leading boolean condition along with optional binding `let` clauses. For example:

```
if someValue > 42 && someOtherThing < 19,          let a = getOptionalThing() where a > someValue {
}
```

  (19797158), (19382942)
- The `if–let` syntax has been extended to support a single leading boolean condition along with optional binding `let` clauses.

  For example:

```
if someValue > 42 && someOtherThing < 19,          let a = getOptionalThing() where a > someValue {
}
```

  (19797158)
- let constants have been generalized to no longer require immediate initialization. The new rule is that a let constant must be initialized before use (like a var), and that it may only be initialized: not reassigned or mutated after initialization. This enables patterns such as:

```swift
let x: SomeThing
if condition {
  x = foo()
} else {
  x = bar()
}
use(x)
```

  which formerly required the use of a `var`, even though there is no mutation taking place. (16181314)
- “`static`” methods and properties are now allowed in classes (as an alias for `class final`). You are now allowed to declare static stored properties in classes, which have global storage and are lazily initialized on first access (like global variables). Protocols now declare type requirements as `static` requirements instead of declaring them as `class` requirements. (17198298)
- Type inference for single-expression closures has been improved in several ways:

  - Closures that are comprised of a single return statement are now type checked as single-expression closures.
  - Unannotated single-expression closures with non-Void return types can now be used in Void contexts.
  - Situations where a multi-statement closure’s type could not be inferred because of a missing return-type annotation are now properly diagnosed.
- Swift enums can now be exported to Objective-C using the `@objc` attribute. `@objc` enums must declare an integer raw type, and cannot be generic or use associated values. Because Objective-C enums are not namespaced, enum cases are imported into Objective-C as the concatenation of the enum name and case name.

  For example, this Swift declaration:

```
@objc
enum Bear: Int {
   case Black, Grizzly, Polar
}
```

  imports into Objective-C as:

```
typedef NS_ENUM(NSInteger, Bear) {
   BearBlack, BearGrizzly, BearPolar
};
```

  (16967385)
- Objective-C language extensions are now available to indicate the nullability of pointers and blocks in Objective-C APIs, allowing your Objective-C APIs to be imported without `ImplicitlyUnwrappedOptional`. _(See items below for more details.)_ (18868820)
- Swift can now partially import C aggregates containing unions, bitfields, SIMD vector types, and other C language features that are not natively supported in Swift. The unsupported fields will not be accessible from Swift, but C and Objective-C APIs that have arguments and return values of these types can be used in Swift. This includes the Foundation `NSDecimal` type and the GLKit `GLKVector` and `GLKMatrix` types, among others. (15951448)
- Imported C structs now have a default initializer in Swift that initializes all of the struct's fields to zero.

  For example:

```
import Darwin
var devNullStat = stat()
stat("/dev/null", &devNullStat)
```

  If a structure contains fields that cannot be correctly zero initialized (i.e. pointer fields marked with the new `__nonnull` modifier), this default initializer will be suppressed. (18338802)
- New APIs for converting among the Index types for `String`, `String.UnicodeScalarView`, `String.UTF16View`, and `String.UTF8View` are available, as well as APIs for converting each of the String views into Strings. (18018911)
- Type values now print as the full demangled type name when used with `println` or string interpolation.

```
toString(Int.self)          // prints “Swift.Int"
println([Float].self)       // prints "Swift.Array&lt;Swift.Float>;”
println((Int, String).self) // prints "(Swift.Int, Swift.String)"
```

  (18947381)
- A new `@noescape` attribute may be used on closure parameters to functions. This indicates that the parameter is only ever called (or passed as an `@noescape` parameter in a call), which means that it cannot outlive the lifetime of the call. This enables some minor performance optimizations, but more importantly disables the “`self.`” requirement in closure arguments. This enables control-flow-like functions to be more transparent about their behavior. In a future beta, the standard library will adopt this attribute in functions like `autoreleasepool()`.

```swift
func autoreleasepool(@noescape code: () -> ()) {
   pushAutoreleasePool()
   code()
   popAutoreleasePool()
}
```

  (16323038)
- Performance is substantially improved over Swift 1.1 in many cases. For example, multidimensional arrays are algorithmically faster in some cases, unoptimized code is much faster in many cases, and many other improvements have been made.
- The diagnostics emitted for expression type check errors are greatly improved in many cases. (18869019)
- Type checker performance for many common expression kinds has been greatly improved. This can significantly improve build times and reduces the number of “expression too complex” errors. (18868985)
- The `@autoclosure` attribute has a second form, @`autoclosure(escaping)`, that provides the same caller-side syntax as `@autoclosure` but allows the resulting closure to escape in the implementation.

  For example:

```swift
func lazyAssertion(@autoclosure(escaping) condition: () -> Bool,
                   message: String = "") {
  lazyAssertions.append(condition) // escapes
  }
lazyAssertion(1 == 2, message: "fail eventually")
```

  (19499207)

- A new compilation mode has been introduced for Swift called Whole Module Optimization. This option optimizes all of the files in a target together and enables better performance (at the cost of increased compile time). The new flag can be enabled in Xcode using the “`Whole Module Optimization`” build setting or by using the `swiftc` command line tool with the flag `-whole-module-optimization`. (18603795)

- `flatMap` was added to the standard library. `flatMap` is the function that maps a function over something and returns the result flattened one level. `flatMap` has many uses, such as to flatten an array:

```
[[1,2],[3,4]].flatMap { $0 }
```

  or to chain optionals with functions:

```
[[1,2], [3,4]].first.flatMap { find($0, 1) }
```

  (19881534)
- The function `zip` was added. It joins two sequences together into one sequence of tuples. (17292393)
- `utf16Count` is removed from `String`. Instead use `count` on the `UTF16` view of the `String`.

  For example:

```
count(string.utf16)
```

  (17627758)

- Objective-C APIs can now express the “nullability” of parameters, return types, properties, variables, etc. For example, here is the expression of nullability for several UITableView APIs:

```objc
-(void)registerNib:(nonnull UINib *)nib forCellReuseIdentifier:
                   (nonnull NSString *)identifier;
-(nullable UITableViewCell *)cellForRowAtIndexPath:
                   (nonnull NSIndexPath)indexPath;
@property (nonatomic, readwrite, retain, nullable) UIView *backgroundView;
```

  The nullability qualifiers affect the optionality of the Objective-C APIs when in Swift. Instead of being imported as implicitly-unwrapped optionals (e.g., UINib!), nonnull-qualified types are imported as non-optional (e.g., UINib) and nullable-qualified types are imported as optional (e.g., UITableViewCell?), so the above APIs will be seen in Swift as:

```swift
func registerNib(nib: UINib, forCellReuseIdentifier identifier: String)
func cellForRowAtIndexPath(indexPath: NSIndexPath) -> UITableViewCell?
var backgroundView: UIView?
```

  Nullability qualifiers can also be applied to arbitrary pointer types, including C pointers, block pointers, and C++ member pointers, using double-underscored versions of the nullability qualifiers. For example, consider a C API such as:

```
void enumerateStrings(__nonnull CFStringRef (^ __nullable callback)(void));
```

  Here, the callback itself is nullable and the result type of that callback is nonnull. This API will be usable from Swift as:

```swift
func enumerateStrings(callback: (() -> CFString)?)
```

  In all, there are three different kinds of nullability specifiers, which can be spelled with a double-underscore (on any pointer type) or without (for Objective-C properties, method result types, and method parameter types):

| Type qualifier spelling | Objective-C property/method spelling | Swift view | Meaning |
| --- | --- | --- | --- |
| `__nonnull` | `nonnull` | Non-optional, e.g., `UINib` | The value is never expected to be `nil` (except perhaps due to messaging `nil` in the argument). |
| `__nullable` | `nullable` | Optional, e.g., `UITableViewCell?` | The value can be `nil`. |
| `__null_unspecified` | `null_unspecified` | Implicitly-unwrapped optional, e.g., `NSDate!` | It is unknown whether the value can be `nil` (very rare). |

  Particularly in Objective-C APIs, many pointers tend to be nonnull. Therefore, Objective-C provides “audited” regions (via a new `#pragma`) that assume that unannotated pointers are nonnull. For example, the following example is equivalent to the first example, but uses audited regions to simplify the presentation:

```objc
NS_ASSUME_NONNULL_BEGIN
// …
-(void)registerNib:(UINib *)nib forCellReuseIdentifier:(NSString *)identifier;
-(nullable UITableViewCell *)cellForRowAtIndexPath:(NSIndexPath)indexPath;
@property (nonatomic, readwrite, retain, nullable) UIView *backgroundView;
// …
NS_ASSUME_NONNULL_END
```

  For consistency, we recommend using audited regions in all Objective-C headers that describe the nullability of their APIs, and to avoid `null_unspecified` except as a transitional tool while introducing nullability into existing headers.

  Adding nullability annotations to Objective-C APIs does not affect backward compatibility or the way in which the compiler generates code. For example, nonnull pointers can still end up being `nil` in some cases, such as when messaging a `nil` receiver. However, nullability annotations—in addition to improving the experience in Swift—provide new warnings in Objective-C if (for example) a `nil` argument is passed to a nonnull parameter, making Objective-C APIs more expressive and easier to use correctly. (18868820)
- Objective-C APIs can now express the nullability of properties whose setters allow `nil` (to “reset” the value to some default) but whose getters never produce `nil` (because they provide some default instead) using the `null_resettable` property attribute. One such property is `tintColor` in `UIView`, which substitutes a default system tint color when no tint color has been specified.

  For example:

```objc
@property (nonatomic, retain, null_resettable) UIColor *tintColor;
```

  Such APIs are imported into Swift via implicitly-unwrapped optionals, for example:

```swift
var tintColor: UIColor!
```

  (19051334)
- Parameters of C pointer type or block pointer type can be annotated with the new `noescape` attribute to indicate that pointer argument won’t “escape” the function or method it is being passed to.

  In such cases, it’s safe, for example, to pass the address of a local variable. `noescape` block pointer parameters will be imported into Swift as `@noescape` parameters:

```
void executeImmediately(__attribute__((noescape)) void (^callback)(void));
```

  is imported into Swift as:

```swift
func executeImmediately(@noescape callback: () -> Void)
```

  (19389222)

- Playgrounds now offer an easy way to create and edit rich documentation using marked-up text. Use the new `//:` or `/*: */` style comments to indicate when text should be shown as a rich comment. Change the viewing mode of a playground by using the “`Show Documentation as Rich Text`” and “`Show Documentation as Raw Text`” commands in the Editor menu.

  For more information, see _[Playground Reference](https://developer.apple.com/library/archive/documentation/Swift/Reference/Playground_Ref/Chapters/XCPlayground.html#//apple_ref/doc/uid/TP40014789)_ in the Xcode documentation. (19265300)
- Playground results are now shown inline, rather than in the timeline view. When there are multiple results on a line, you can toggle between viewing a single result and a listing of all the results. For result sets that are numbers, there is the added option of viewing as a graph. Results can be resized to show more or less information.

  For more information, see Playground Help in the Xcode documentation. (19259877)
- Playground scrolling and performance has been improved.
- Playgrounds can now be upgraded to the new format by selecting the `Editor > Upgrade Playground` menu item.

  (19938996)
- Playgrounds now expose their structure in the project navigator. To show the project navigator, select `View > Navigators > Show Project Navigator`. This allows you to use resources (for instance, images) from within your playground: twist open the playground to see the Resources folder and drag them in. (19115173)
- Playgrounds now let you provide auxiliary support source files, which are compiled into a module and automatically imported into your playground. To use the new supporting source files feature, twist open the playground in the project navigator to see the new Sources folder, which has a single file named `SupportCode.swift` by default. Add code to that file, or create new source files in this folder, which will all be automatically compiled into a module and automatically imported into your playground. (19460887)

- LLDB now includes a prototype for `printf()` by default when evaluating C, C++, and Objective-C expressions.

  This improves the expression evaluation experience on arm64 devices, but may conflict with user-defined expression prefixes in `.lldbinit` that have a conflicting declaration of `printf()`. If you see errors during expression evaluation this may be the root cause. (19024779)
- LLDB's Objective-C expression parser can now import modules. Any subsequent expression can rely on function and method prototypes defined in the module:

```
(lldb) p @import Foundation
(lldb) p NSPointFromString(@"{10.0, 20.0}");
(NSPoint) $1 = (x = 10, y = 20)
```

  Before Xcode 6.3, methods and functions without debug information required explicit typecasts to specify their return type. Importing modules allows a developer to avoid the more labor-intensive process of determining and specifying this information manually:

```
(lldb) p NSPointFromString(@"{10.0, 20.0}");
error: 'NSPointFromString' has unknown return type; cast the call to its declared return type
error: 1 errors parsing expression
(lldb) p (NSPoint)NSPointFromString(@"{10.0, 20.0}”);
(NSPoint) $0 = (x = 10, y = 20)
```

  Other benefits of importing modules include better error messages, access to variadic functions when running on 64-bit devices, and eliminating potentially incorrect inferred argument types.

  (18782288)
- Evaluating Swift expressions performance is improved especially when debugging code running on devices.

  This will be most noticeable in the Swift `REPL` and when issuing LLDB commands such as `p`, `po`, and `expression`. (19213054)
- Significant improvements in LLDB’s Swift support have addressed many known issues with the Swift debugging experience. (19656017)

The argument ordering for the arm64 vfma/vfms lane intrinsics has changed.

The change may not trigger compile-time errors but it will break code at runtime. To reduce risk, the transition to the new ordering is being completed in stages:

- By default, the compiler now warns about any use of the intrinsics but will retain the old behavior.
- As soon as possible, adopt the new behavior and define the `USE_CORRECT_VFMA_INTRINSICS` macro with value `1`.
- If you define the `USE_CORRECT_VFMA_INTRINSICS` macro value with value `0`, that silences the warnings and keeps the old behavior. However, do not leave your code in that state for long: support for the old behavior will be removed in a future release.

(17964959)

These issues, previously reported in prior releases of Xcode, have been resolved in Xcode 6.3.

- Apps containing a Watch extension may not deploy to the iOS Simulator for iOS versions earlier than 8.2. (20032374)
- Audio playback using `AudioServicesPlaySystemSound` does not function as expected in the iOS 8.1 and 8.2 simulator runtimes. (17911598)

- Xcode does not show a Watch as paired to its companion iPhone if the iPhone was rebooted and then connected to the host Mac without first being unlocked. (19864431)
- Sharing a scheme in an Apple Watch app project prevents the iOS and Apple Watch App schemes from being created. (18941832)
- App Store import will fail for Apple Watch apps that do not have the same version information as the containing app. (17812309)
- Xcode does not show a Watch as paired to its companion iPhone if the iPhone was rebooted and then connected to the host Mac without first being unlocked. (19864431)
- If the deployment target of an app containing an Apple Watch extension is configured for earlier than iOS 8.2, deployment of the app to devices running iOS 8.1.x or earlier may fail. (20032374)

- `Convert to Latest Swift` may generate build errors when run.

  These errors can be safely ignored and don’t affect the source changes that are produced. (19650497)
- When subclassing `UITableViewController`, if you try to create your own initializer you will see an error telling you "Initializer does not override a designated initializer from its superclass."

  To override the designated initializer `initWithNibName:bundle:` you will need to declare it as a designated initializer in a class extension in an Objective-C bridging header. The following steps will guide you through this process:

  1. In your Swift project, create a new empty iOS Objective-C file. This will trigger a sheet asking you "Would you like to configure an Objective-C bridging header?"
  2. Tap "Yes" to create a bridging header.
  3. Inside `[YOURPROJECTNAME]-Bridging-Header.h` add the following code:

```objc
@import UIKit;

@interface UITableViewController()
- (instancetype)initWithNibName:(NSString *)nibNameOrNil
   bundle:(NSBundle *)nibBundleOrNil NS_DESIGNATED_INITIALIZER;
@end
```
  4. Rebuild your project

  (19775924)
- Swift 1.2 is strict about checking type-based overloading of `@objc` methods and initializers, something not supported by Objective-C.

```swift
// Has the Objective-C selector "performOperation:".
func performOperation(op: NSOperation) { /* do something */ }
// Also has the selector "performOperation:".
func performOperation(fn: () -> Void) {
    self.performOperation(NSBlockOperation(block: fn))
}
```

  This code would work when invoked from Swift, but could easily crash if invoked from Objective-C.

  To solve this problem, use a type that is not supported by Objective-C to prevent the Swift compiler from exposing the member to the Objective-C runtime:

  - If it makes sense, mark the member as `private` to disable inference of `@objc`.
  - Otherwise, use a placeholder parameter with a default value, for example: `_ nonobjc: () = ()`.

  (19826275)
- Overrides of methods exposed to Objective-C in private subclasses are not inferred to be `@objc`, causing the Swift compiler to crash.

  Explicitly add the `@objc` attribute to any such overriding methods. (19935352)
- Symbols from SDKs are not available when using Open Quickly in a project or workspace that uses Swift. (20349540)

- Switching between `Raw Source` and `Rich Text` in a playground may cause the timeline to disappear.

  You can show the timeline by selecting it from the Assistant editor popup menu. (20091907)
- Opening a playground and immediately selecting `Undo` can set an invalid target platform.

  Either redo, select a valid platform, or, if you have already closed the document, edit the playground’s `contents.xcplayground` file to ensure that either `osx` or `ios` is specified for the `target-platform` property. (20327880)
- Xcode crashes if a playground has an invalid value target platform.

  Edit the playground’s `contents.xcplayground` file to ensure that either `osx` or `ios` is specified for the `target-platform` property. (20327968)

- When launching a WatchKit app on the iOS Simulator, the Watch Simulator may not automatically launch.

  Launch the Watch Simulator before launching the WatchKit app on the iOS Simulator. (19830540)
- Localization settings made in a target's scheme (as well as other settings made on the command line) will not be honored on launch in the iOS Simulator with iOS 8 runtimes.

  Choose the desired language in the Settings app. (19490124)

- When using the debugger, the variables view may omit values for the current frame if the current function comes from a Swift framework.

  Add `-Xfrontend -serialize-debugging-options` to the `Other Swift Options` build setting for the framework. (20380047)

- Swift tests are not automatically discovered in this release of Xcode. Test annotations in the source editor sidebar will not appear, and the test navigator and the table of tests in the Test action of the scheme sheet will be empty.

  You can run Swift tests by selecting `Product > Test`. Once tests have been run, they appear in the test navigator and the scheme sheet. The following limitations apply:

  - Tests discovered through execution in this manner provide limited interaction in the test navigator. For example, Run buttons do not appear and clicking on a test in the navigator does not jump to the source code except in the case of a test error.
  - Run buttons and test success/fail indicators will not appear in the source editor.

  (20373533)

- iOS extensions may need to be manually enabled before you can debug them. (18603937)
- The Xcode menu command `Simulator Background Fetch` does not work.

  Use the menu command in iOS Simulator instead. (20145602)
- Attached devices running earlier versions of iOS might show up as ineligible in the run destinations menu.

  To correct this problem, reconnect the devices one at a time. (20320586)

Xcode 6.2 adds support for iOS 8.2, including developing Apple Watch apps with the new WatchKit framework. Tools support for WatchKit includes:

- Design tools for building Apple Watch interfaces, glances, and notifications
- Debugging and profiling support
- Apple Watch support in iOS Simulator for testing apps, glances, and notifications

- Interface Builder sometimes fails to render a subclass of a designable class on the canvas, or fails to show inspectable properties inherited from a superclass.

  Add `IB_DESIGNABLE` or `@IBDesignable` to the subclass declaration. (19512849)

- When creating a new Apple Watch app target, the newly created asset catalog includes an "Unassigned" slot in the catalog's app icon.

  Select the "Unassigned" slot and delete it using the Delete key. (19978639)
- The long-look slot in an Apple Watch app asset catalog for 38mm devices is labeled incorrectly. The label reads:

  - `Apple Watch - Home Screen (All) - Long Look (42 mm) - 40pt`

  It should read:

  - `Apple Watch - Home Screen - Long Look (38 mm) - 40pt`

  This slot works correctly for 38 mm device icons.

  The long-look slot for 42 mm devices is labeled: `Apple Watch - Long Look - 44pt`. (19978648)

- iCloud accounts requiring two factor authentication are not supported in iOS Simulator.

  For development, create an account that doesn't use two factor authentication. (18522339)
- Running an iOS app and an Apple Watch app concurrently in the simulator is not supported.

  To debug an iOS app and an Apple Watch app:

  1. Build and run the Apple Watch app.
  2. Tap the iOS app's icon in the simulator home screen.
  3. Use `Debug > Attach to Process` to debug the iOS app in Xcode.

  (18559453)
- Apps containing an Apple Watch extension may not deploy to iOS Simulator for iOS 8.1.x or earlier.

  Add a `"MinimumOSVersion" = "8.2"` key pair to the `Info.plist` for the Apple Watch extension. (20032374)

- The UI Automation Instrument is not supported for WatchKit apps. (19152139)

- When stopped at a breakpoint in an Apple Watch app, tapping `Stop` doesn't stop the running app.

  Tap `Stop` twice. (18991746)

- Sharing a scheme in a project containing an Apple Watch app prevents iOS and Apple Watch app schemes from being created. (18941832)
- Icons for Apple Watch are not displayed in the Xcode Devices window when running on OS X 10.10.2 and earlier. (19986057)
- The Devices window does not show a warning when a connected iOS device requires user interaction to approve a Trust request.

  Use the connected iOS device to approve the Trust alert. (19944552)
- Xcode does not show an Apple Watch as paired if the companion iPhone was rebooted and then connected to the host Mac without first being unlocked.

  To resolve, reboot the iPhone and unlock it with a password before connecting it to the Mac. (19864431)
- The App Store import fails for Apple Watch apps that do not have the same version information as their containing app.

  To prevent this import failure, ensure that the `CFBundleVersion` and `CFBundleShortVersionString` entries in the Apple Watch app and the containing app are identical. (17812309)
- If the deployment target of an app containing an Apple Watch extension is configured for earlier than iOS 8.2, deployment of the app to devices running iOS 8.1.x or earlier may fail.

  Manually configure the deployment target of the Apple Watch extension for iOS 8.2. The Apple Watch extension will not run on iOS earlier than 8.2, but the app’s deployment will be allowed. (20032374)

- Many common causes of SourceKit crashes have been fixed, namely corrupted module caches and out of date derived data.
- Passing class objects for pure Swift class to `AnyObject` values no longer causes a crash. (18828226)
- Class methods and initializers that satisfy protocol requirements now properly invoke subclass overrides when called in generic contexts. For example:

```swift
  protocol P {
    class func foo()
  }

  class C: P {
    class func foo() { println("C!") }
  }

  class D: C {
    override class func foo() { println("D!") }
  }

  func foo<T: P>(x: T) {
    x.dynamicType.foo()
  }

  foo(C()) // Prints "C!"
  foo(D()) // Used to incorrectly print "C!", now prints "D!"
```

  (18828217)

- Fixed an issue where Interface Builder could not open or compile IB documents that have an image name containing a slash (‘`/`') character on Yosemite. This manifested as a range exception on `NSTaggedPointerString` when calling `+[NSImage imageNamed:]`. (18752260)

- Fixed an issue where choosing a new build of Xcode after configuring Xcode Server could cause permissions problems. (18819339)
- Fixed a crash in Xcode Server when the private portal keychain is replaced with a symlink to the system keychain. (18854423)
- Fixed an issue with startup when using a password policy. (18819348)
- Fixed an issue checking out sources in Xcode Server when connecting over SSH. (18819357)

- Data structures containing bitfields may display incorrectly in the debugger when referenced from Swift code. (17967427)

- If your project’s only assets are in an asset catalog, the build may fail with an error similar to: '`.../Contents/Resources` does not exist.’

  Add at least one non-asset catalog resource to your project. (17848595)

- The iOS Simulator will sometimes loose network connectivity when the host’s network configuration changes.

  Restart the simulated device to regain network connectivity. (17867038)
- When playing a video to the external display in the iOS Simulator, external display may be all black.

  Change the resolution of the external display while the video is playing and then change it back to the desired resolution. (17933514)
- After you install iOS 7.1 Simulator using the Downloads panel in Xcode Preferences, the iOS 7.1 simulator’s devices may not be available in the run destination menu.

  Log out and then log in again, or restart your computer. (19011252)

- Xcode 6.1 includes Swift 1.1. (18238390)
- A large number of AppKit APIs have been audited for optional conformance in addition to WebKit, Foundation, UIKit, CoreData, SceneKit, SpriteKit, and Metal APIs. As a result, a significant number of implicitly unwrapped optionals have been removed from their interfaces. These changes clarify the nullability of properties, arguments, and return values in the APIs. The audit effort is ongoing.

  The API changes replace `T!` with either `T?` or `T` depending on whether or not the value can be `null`, respectively.  If you find a case that is incorrect, file a bug at [http://bugreport.apple.com](http://bugreport.apple.com/) and include the tag “_#IUO_” in the subject line.

  If you encounter a method, property, or initializer for which the return value is incorrectly considered non-nullable, you can work around the problem by wrapping the result in an optional:

```swift
var fooOpt: NSFoo? = object.reallyMightReturnNil()
if let foo = fooOpt {...}
```

  Be sure to file a bug about these cases.
- Values of type `Any` can now contain values of function type. (16406907)
- Documentation for the standard library (displayed in quick help and in the synthesized header for the Swift module) is improved. (16462500)
- All of the `*LiteralConvertible` protocols now use initializers for their requirements rather than static methods starting with `convertFrom`. For example, `IntegerLiteralConvertible` now has the following initializer requirement:

```
init(integerLiteral value: IntegerLiteralType)
```

  Any type that previously conformed to one of these protocols needs to replace the `convertFromXXX` static methods with the corresponding initializer. (18154091)
- Xcode produces fixit hints to move code from the old-style “fromRaw()/toRaw()” enum APIs to the new style-initializer and “rawValue” property. (18216832)
- Class properties don't need to be marked final to avoid O(n) mutations on value semantic types. (17416120)
- Initializers can fail by returning `nil`. A failable initializer is declared with `init?` to return an explicit optional or `init!` to return an implicitly unwrapped optional.

  For example, `String.toInt` could be implemented as a failable initializer of `Int`:

```
extension Int {
  init?(fromString: String) {
    if let i = fromString.toInt() {
      // Initialize
      self = i
    } else {
      // Discard self and return 'nil'
      return nil
    }
  }
}
```

  The result of constructing a value using a failable initializer should be checked for `nil` as in this example.

```
if let twentytwo = Int(fromString: "22") {
  println("the number is \(twentytwo)")
} else {
  println("not a number")
}
```

  In the current implementation, structure and enumerator initializers can return `nil` at any point inside the initializer, but initializers of a class can only return `nil` after all of the stored properties of the object have been initialized and `self.init` or `super.init` has been called. If `self.init` or `super.init` is used to delegate to a failable initializer, then the `nil` return is implicitly propagated through the current initializer if the called initializer fails. (16480364)
- Objective-C `init` and factory methods are imported as failable initializers when they can return `nil`. In the absence of information about a potentially `nil` result, an Objective-C `init` or factory method will be imported as `init!`.

  As part of this change, factory methods that have `NSError**` parameters, such as `+[NSString stringWithContentsOfFile:encoding:error:]`, will now be imported as failable) initializers. For example:

```
init?(contentsOfFile path: String,
      encoding: NSStringEncoding,
      error: NSErrorPointer)
```

  (18232430)
- OS X apps can now apply the `@NSApplicationMain` attribute to their app delegate class in order to generate an implicit `main` for the app.

  This attribute works in the same way as the `@UIApplicationMain` attribute for iOS apps. (16904667)
- Casts can now be performed between CF types (such as `CFString`, `CGImage`, and `SecIdentity`) and `AnyObject`. Such casts will always succeed at run-time. For example:

  - `var cfStr: CFString = ...`
  - `var obj: AnyObject = cfStr as AnyObject`
  - `var cfStr = obj as CFString`

  (18088474)

- iOS Playgrounds now support displaying animated views with the `XCPShowView()``XCPlayground` API. This capability is disabled by default; it can be enabled by checking the "Run in Full Simulator" setting in the Playground Settings inspector.

  When the capability is enabled, running the playground causes the iOS Simulator application to launch and run the playground in the full simulator. This capability is also required for other functionality that fails without the full simulator, such as `NSURLConnection` http requests. Running in the full iOS Simulator is slower than running in the default mode. (18282806)

- Dead code stripping no longer removes public declarations that are needed to run tests from Swift application targets. (18173029)

- A weakly-linked symbol in a playground no longer causes a compilation error. (18000684)
- Using `NSView` subclasses in OS X playgrounds no longer results in execution failure. (18449054)

- Addressed an issue that could cause Xcode to become unresponsive while editing Swift code.

- Swift expressions like '`expr`', '`p`', and '`print`' that are evaluated from the LLDB prompt in the debugger console will now work on 32-bit iOS devices. (18249931)

- In the Swift REPL, attempts to inspect instances of classes defined in the REPL now produce properly formed data for stored properties. (18457336)

- Configuring Xcode Server on a system that had a pre-GM build of Xcode 6 now works. (18314522)

- Settings changed in the Settings app on iOS Simulator now persist as expected. (18238018)
- Deleting an app from iOS Simulator now deletes user defaults as expected. (18307910)

- Users upgrading Xcode, iOS Simulator, and documentation downloads from Xcode 5.1.1 to Xcode 6.1 may receive the error, “The digest is missing,” when building and running a master detail app on a device.

  Unplug the device and plug it back in. (18464963)

- By default, NSTableViews and NSOutlineViews have a white background, which may be incorrect when the control is shown with a dark appearance.

  To dynamically support both light and dark appearances, change the background of an `NSTableView` or `NSOutlineView` from “Default” to “Control Background Color”. (18075907)

- Simulated devices can get stuck in a “Creating” state in some circumstances. This problem can occur either when creating new devices or when resetting existing devices after having renamed `Xcode.app`.

  If this this problem occurs, reboot your system and reset the device from the command line by running `xcrun simctl erase <Device UDID>`. You can obtain the UDID of the device by checking the output of `xcrun simctl list`. (17042870)
- Localization and Keyboard settings, including 3rd party keyboards, are not correctly honored by Safari, Maps, and developer apps in the iOS 8.1 Simulator. `[NSLocale currentLocale]` returns `en_US` and only the English and Emoji keyboards are available. (18418630, 18512161)
- If an app is weak linked against frameworks new in iOS 8 SDK and OS X 10.10 SDK, it may fail to run if the run destination is an iOS Simulator for older iOS runtimes and the host system is running OS X Yosemite. (17807439)
- iOS Simulator does not support the use of network proxy servers that require authentication. (14889876)

- Debugging Today app extensions is not reliable after the first debug session.

  Dismiss Notification Center before starting the next debug session. (18051136)

- App Store submission issues encountered with the Xcode 6.0 GM seed have been resolved. (18444000)

Swift is a new object-oriented programming language for iOS development. Swift is modern, powerful, expressive, and easy to use.

- Access all of the Cocoa Touch frameworks with Swift.
- Swift code is compiled and optimized by the advanced LLVM compiler to create high-performance apps.
- Swift provides increased type safety with type inference, restricts direct access to pointers, and automatically manages memory using ARC to make it easy for you to use Swift and create secure, stable software. Other features related to language safety include mandatory variable initialization, automatic bounds checking to prevent overflows, conditionals that break by default, and elimination of pointers to direct memory by default.
- Write, debug, and maintain less code, with an easy to write and read syntax and no headers to maintain.
- Swift includes optionals, generics, closures, tuples, and other modern language features. Inspired by and improving upon Objective-C, Swift code feels natural to read and write.
- Use Swift interactively to experiment with your ideas and see instant results.
- Swift is a complete replacement for both the C and Objective-C languages. Swift provides full object-oriented features, and includes low-level language primitives such as types, flow control, and operators.

- Playgrounds are an interactive development environment allowing you to experiment with Swift for prototyping, testing ideas, and so forth. Some uses for playgrounds include:

  - Designing a new algorithm and watching its results every step of the way
  - Experimenting with new API or trying out new Swift syntax
  - Creating new tests and then verifying that they work before promoting them into your test suite
- You can open select documentation in a playground to learn from the tutorial in a graphically rich, interactive environment.
- The debugging console in Xcode includes an interactive version of the Swift language called the _read-eval-print loop (REPL)_ built into LLDB. Use Swift syntax to evaluate and interact with your running app, or write new code to see how it works in a script-like environment. REPL is available from within the Xcode console or by using LLDB from within Terminal when attached to a running process.
- The Xcode documentation viewer shows Quick Help or reference documentation in the language of your choice—Objective-C, Swift, or both.
- Xcode synthesizes a Swift view of the SDK API when using jump-to-definition for SDK content from Swift code. The synthesized interface shows how the API is imported into Swift, and it retains all the comments from the original SDK headers.

- The XCTest framework supports performance measurement capabilities enabling you to quantify each part of an application. Xcode runs your performance tests and allows you to define a baseline performance metric. Each subsequent test run compares performance and displays the change over time.
- New APIs in the XCTest framework allow testing code that executes asynchronously. You can now create tests for network operations, file I/O, and other system interactions that execute using asynchronous calls.

- Interface Builder uses live rendering to display your custom objects at design time exactly as they appear when your app is run. When you update the code for a custom view, the Interface Builder design canvas updates automatically with the new look you just typed into the source editor, with no need to build and run.
- Size classes for iOS 8 enable designing a single universal storyboard with customized layouts for both iPhone and iPad. With size classes you can define common views and constraints once, and then add variations for each supported form factor. iOS Simulator and asset catalogs fully support size classes as well.
- Interface Builder renders embedded custom iOS fonts during design time, giving a more accurate preview of how the finished app will look, with correct dimensions.
- Find and search is supported in `.xib` and `.storyboard` files when using Interface Builder.
- The preview editor includes the ability to present multiple previews and zooming.

- Size classes, JPEG, PDF, template images, and alignment rectangles are now supported by asset catalogs.

- Using the view debugger, a single button click pauses your running app and “explodes” the paused UI into a 3D rendering, separating each layer of a stack of views. Using the view debugger makes it easy to see why an image may be clipped and invisible, and the order of the graphical elements becomes clear. By selecting any view, you can inspect the details by jumping to the relevant code in the assistant editor source view. The view debugger also displays Auto Layout constraints, making areas where conflicts cause problems findable.
- The debug navigator queue debugger is enhanced to record and display recently executed blocks, as well as enqueued blocks. You can use it to see where your enqueued blocks are and to examine the details of what’s been set up to execute.
- Debug gauges provide at-a-glance information about resource usage while debugging, calling the developer’s attention to previously unknown problems.

  - Two new gauges, Network Activity and File Activity, visually highlight spikes in input/output activity while your app is running.
  - The iCloud gauge is updated with support for the new Documents in the Cloud and CloudKit features that provide access to files outside the app-specific container.

- Metal provides a new, low-overhead GPU graphics and compute API as well as a shading language for iOS. The Metal shader compiler adds support for precompiling Metal shaders in Xcode. The GPU frame debugger and shader profiler supports debugging and profiling Metal-based games and apps.

- The SpriteKit level designer enhances SpriteKit use and provides improved display of SpriteKit variables when debugging.
- SpriteKit and SceneKit are now enhanced to work together and are supported on iOS.

- You can add an extension target to any iOS or Mac app to expand your app’s functionality to other apps in the OS.
- iOS developers can now create dynamic frameworks.

- New iOS Simulator configurations allow you to keep data and configuration settings grouped together. Run one configuration for one version of an app, with its own data, and another configuration for a different app version.

- Xcode can package your localizable strings into the industry-standard XLIFF format for localization.
- Xcode automatically generates the base language `.strings` file directly from your source code.
- While designing in Interface Builder, the preview assistant can show how the interface appears in other languages.
- Xcode can use a locale to run your app in iOS Simulator or directly on devices, as it would appear to customers in other countries.

- Profile Guided Optimization (PGO) works with the LLVM optimizer and XCTest tests to profile the most actively used parts of your application. You can also exercise your app manually to generate an optimization profile. PGO uses the profile to further optimize your app, targeting the areas that most need optimization, improving performance beyond what setting optimization options alone can achieve.
- Developers can define modules for their own Objective-C code, which makes sharing frameworks across all their projects easier.

- The new Instruments user interface makes configuring your performance tuning session easier and improves control. The new template chooser allows you to choose your device and target as well as the starting point for your profiling session. The track view allows direct click-and-drag to set the time filter range. The toolbar takes up less space to let you focus on the task at hand. The tracks of recorded data are given more space, and configuration for how data is collected and viewed is managed in a unified inspector area.
- You can profile any test or test suite, which is useful for analyzing memory leaks in a functional test or time profiling a performance test to see why it has regressed.
- Simulator configurations are now treated like devices by Instruments, making it easy to launch or attach to processes in the simulator.
- Counters and Events instruments have been combined into a more powerful Counters instrument and made easier to configure. It can track individual CPU events, and you can specify formulas to measure event aggregates, ratios, and more. iOS developers on 64-bit devices can now use Counters to fine-tune apps.
- Instruments supports Swift, displaying Swift symbols in stack traces and Swift types in Allocations. You can also use Instruments to profile app extensions.

- Triggers allow you to make more complex integration scenarios by configuring server-side rules to launch custom scripts before or after the execution of an Xcode scheme.
- Xcode Server supports the new Xcode performance-testing features, making it easy for a team to share a group of devices and Macs for continual performance testing.
- Issues are now tracked per integration and allow delta tracking, so that you can see when an issue appeared or when it or was fixed, and by whom.
- Configuration options in Xcode Server give development teams greater control over the execution of bots. New settings for integration intervals, grouping of bots, and iOS Simulator configurations make Xcode bots more powerful. The new reports UI includes bot-level statistics, the number of successful integrations, and commit and test addition tracking.

- A future version of Xcode to be released along with OS X Yosemite will add Swift support for OS X, including playgrounds and REPL. Xcode 6.0 only supports Swift for iOS projects and playgrounds. A beta release of Xcode with Swift support for both OS X and iOS is available at [developer.apple.com/xcode/downloads/](https://developer.apple.com/xcode/downloads/)

- If you encounter an API method for which the return value is incorrectly considered non-nullable, or a property that is incorrectly considered non-nullable, please file a radar and include the tag “#IUO” in the subject line. You can work around the problem by immediately wrapping the result in an optional:

```swift
var fooOpt: NSFoo? = object.reallyMightReturnNil()
if let foo = fooOpt { … }
```

  Please be sure to file bugs about these cases. Please do not file feature requests about APIs that are still marked as T!, we know about them.

- Refactoring for Swift is not available.

- The `libc++` headers in Xcode 6 include a change to make `std::pair` have a trivial constructor. This fix is important for performance and compliance with the C++ standard, but it changes the ABI for C++ code using `std::pair`.

  This issue does not affect the `libc++` library installed on OS X and iOS systems because that library does not expose any uses of `std::pair` in its API. It is only a concern for your own code and any third-party libraries that you link with. As long as all of the code is built with the same version of `libc++`, there will be no problem.

  If you need to maintain binary compatibility with a previous version of `libc++`, you can opt into keeping the old ABI by building with the `_LIBCPP_TRIVIAL_PAIR_COPY_CTOR` macro defined to zero, that is, by adding `-D_LIBCPP_TRIVIAL_PAIR_COPY_CTOR=0` to the compiler options. (15474572)

- Xcode will no longer pass options in the build setting `OTHER_LDFLAGS` to `libtool` when building static libraries, nor will it pass options in `OTHER_LIBTOOLFLAGS` to the Mach-O linker when building any other kind of product. Previously all options in both settings would be passed to both tools. Make sure that options are in the correct build setting for the product type, static library, or other component being built. (4285249)
- Bundles (including frameworks, applications, and other bundles) which are added to a Copy Files build phase to embed the bundle in the current target's product will have their `Headers` and `PrivateHeaders` directories removed when they are copied. This is done to help ensure that header content in embedded bundles is not accidentally shipped to end users. This does not affect such items which are already in Copy Files build phases in existing projects. This change affects any file or directory inside the item being copied which is named exactly `Headers` or `PrivateHeaders`.

  To have a target opt out of this behavior, set the build setting `REMOVE_HEADERS_FROM_EMBEDDED_BUNDLES` to `YES`. To have an existing target opt in to this behavior, remove and then re-add the desired file references to the Copy Files build phase in question.

- When using a regular expression in the Find navigator, it is now possible for a match to span multiple lines. The metacharacter “.” still excludes newlines, but a character class may include every character, for example, “`[\D\d]`”. (11393323)
- When using a regular expression in the Find navigator, the “`\1`” syntax is no longer supported in the replacement string. To refer to a captured group, use the syntax “`$123`”.

  With this change, you can now insert a digit after the tenth captured group and beyond by escaping the digit, for example, “`$10\2`.” Likewise, when finding text using patterns, you can insert a digit after the tenth pattern. (11836632)

- XIBs and Storyboards can now be used as launch screens. Applications take advantage of this feature to provide a single launch screen that adapts to different screen sizes using constraints and size classes. These launch screens are supported on iOS 8.0 and later.

  Applications targeting iOS 7.x or prior releases need to also supply traditional launch PNGs via an asset catalog. Without launch PNGs for iOS 7 and earlier, applications will run in the retina 3.5” compatibility mode on retina 4” displays. (18000959)

- Embedded frameworks and dylibs are supported only on iOS 8 and later.

  If your app deploys to prior iOS releases, turn off auto-linking. Load the frameworks or dylibs using `dlopen()` after performing an OS version check. (18140501)

- The _Hardware IO Tools for Xcode_ package, available at [developer.apple.com](https://developer.apple.com/), now includes the following apps:

  - Printer Simulator
  - HomeKit Accessory Simulator

  (17014426, 17014426, 17738621)
- These three apps have been removed from the _Hardware IO Tools for Xcode_ package download for this release:

  - Apple Bluetooth Guidelines Validation
  - Bluetooth Explorer
  - PacketLogger

   (18162817)

- Xcode can now configure bots to authenticate with source control repositories using SSH keys. (16512381)
- Xcode Server prunes older integration data based on available disk space. (16535845)

- `xcodebuild` now supports the `id` option for iOS simulator destination specifiers. In Xcode 5 this option was only available for iOS device destination specifiers. (17398965)

- Xcode 6.0 GM seed may encounter issues when submitting to the App Store. These issues to be resolved in a subsequent release of Xcode. (18344000)

- The relational operator `==` may not work on `enum` values if the `enum` is declared in another file.

  Use `!(x != .Value)` instead of `(x == .Value)`. (18073705)
- Properties of values typed as AnyObject may not be directly assigned to.

  Cast the value of type '`AnyObject`' to the intended type, store it in a separate value, then assign it directly to the properties of that value. For example:

```swift
var mc: MyClass = someAnyObject as MyClass
mc.foo = “reassign"
```

  (15233922)
- Swift does not support object initializers that fail by returning null.

  If there is a factory method, use it instead. Otherwise, capture the result in an optional. For example:

```swift
let url: NSURL? = NSURL(string: "not a url")
```

  (16480364)
- Private entities with the same name and same type will conflict even if defined in different files within the same module. (17632175)
- Nested functions that recursively reference themselves or other functions nested in the same outer function will crash the compiler. For example:

```swift
func foo() {
   func bar() { bar() }

  func zim() { zang() }
  func zang() { zim() }
}
```

  Move recursive functions to the outer type or module context. (11266246)
- A generic class can define a stored property with a generic type, as long as the generic class is not made available to Objective-C—that is, the generic class is not marked as `@objc` or subclassed from an Objective-C class. For example, this is valid:

```swift
class Box<T> {
   // "value" is a stored property whose type is the generic type parameter T
   let value: T
   init(value: T) {
     self.value = value
   }
}
```

  If you need to make such a class available to Objective-C, use an array for storage:

```swift
@objc class ObjCBox<T> {
   let _value: T[]
   var value: T { return _value[0] }
}
```

  (16737510)
- Using a Swift `Dictionary` with `Int64` or `UInt64` types as keys will cause traps on 32-bit platforms when attempting to insert a key whose value is not representable by an `Int32`.

  Use `NSNumber` as the key type. (18113807)

- In Playgrounds, `println()` ignores the `Printable` conformance of user-defined types. (16562388)
- iOS playgrounds do not support displaying animated views with the `XCPShowView()``XCPlayground` API. (17848651)

- `ARM` and `ARM64` code that uses the `float16_t` type may fail when trying to link C++ code compiled with an older compiler. In previous versions of the compiler, `float16_t` was defined as `uint16_t`. `float16_t` is now defined as `__fp16`. (15506420)

- View Memory for Swift data structures in the debugger may show memory location zero.

  Pass the structure to a function expecting a reference to an `UnsafePointer<Void>`, and print it within the function. Enter this address as the memory location to view. (17818703)

- If you set a Swift subclass of `NSValueTransformer` as a binding’s value transformer, the XIB or storyboard will contain an invalid reference to the class and the binding will not work properly at runtime.

  Either enter a mangled class name into the `Value Transformer` field, or add the `@objc(…)` attribute to the `NSValueTransformer` subclass. (17495784)
- Interface Builder does not support connecting to an outlet in a Swift file when the outlet type is a protocol.

  Declare the outlet type as `AnyObject` or `NSObject`, connect objects to the outlet using Interface Builder, then change the outlet type back to the protocol. (17023935)
- After porting a custom class from Objective-C to Swift, any references to the class in a XIB or storyboard needs to be updated manually.

  Select each reference, clear the `Class` field in the Custom Class inspector, save, and reenter the class name. (17153630)
- The implementation of `UICollectionViewCell` content view sizing has changed in iOS 8. When deploying collection view cells built with Xcode 6 to iOS 7, a cell’s content view has no autoresizing mask. This can result in undesirable layouts.

  You must conditionally set the autoresizing mask for proper deployment of collection views on versions of iOS prior to iOS 8. The sample code below demonstrates how to implement this workaround on a custom subclass of `UICollectionViewCell`.

```objc
- (void)commonInit_MyCollectionViewCell {
    if ([[[UIDevice currentDevice] systemVersion] compare:@"8.0" options:NSNumericSearch] == NSOrderedDescending) {
        [[self contentView] setAutoresizingMask:UIViewAutoresizingFlexibleWidth | UIViewAutoresizingFlexibleHeight];
    }
}

- (id)initWithCoder:(NSCoder *)coder {
    if (self = [super initWithCoder:coder]) {
        [self commonInit_MyCollectionViewCell];
    }
    return self;
}

- (id)initWithFrame:(CGRect)frame {
    if (self = [super initWithFrame:frame]) {
        [self commonInit_MyCollectionViewCell];
    }
    return self;
}
```

  (18338361)
- Interface Builder only shows custom geometry overrides (for example, `-intrinsicContentSize`) in a designable subclass in iOS documents. (17024838)

- A storyboard or XIB will not localize correctly if all of the following three conditions are true:

  - The storyboard or XIB uses size classes.
  - The base localization and the build target are set to `Universal`.
  - The build targets iOS 7.0.

  You can work around this issue by adding a `~iphone` and a `~ipad` variant of each strings file used by the affected storyboards and XIBs. Automate this operation with a build phase by doing the following.

  1. Select the application target in the project editor, then go to the Build Phases tab.
  2. Add a new Run Script phase with the following contents:

```
# Go to the app bundle.
cd "${BUILT_PRODUCTS_DIR}/${UNLOCALIZED_RESOURCES_FOLDER_PATH}"

for f in "$PWD"/*.lproj/*.strings; do
    # If the .strings file name doesn't already specify a device...
    name=$(basename "$f" .strings)
    if [[ "${name%%~iphone}" == "$name" && "${name%%~ipad}" == "$name" ]]; then
        # If there is a corresponding .nib in Base.lproj...
        if [[ -e "Base.lproj/$name~iphone.nib" ]]; then
            # Symlink the device-qualified file name to the unqualified file.
            ln -sf "$f" "${f/%.strings/~iphone.strings}"
        fi
        # Do likewise for iPad.
        if [[ -e "Base.lproj/$name~ipad.nib" ]]; then
            ln -sf "$f" "${f/%.strings/~ipad.strings}"
        fi
    fi
done
```

  (18087788)

- Signed OS X App Extensions may emit `dyld` warnings and fail to launch.

  Ensure that the same team ID is set for both the app extension and the containing app. (17711503)
- Creating an iOS Document Picker extension with the File Provider enabled does not add the containing app to the resulting app group.

  Add the containing app to the app group manually. (16871267)

- If a build target’s only asset is an asset catalog, building fails with the error “`.../Contents/Resources" does not exist`.”

  Add at least one non-asset catalog resource to the build target. (17848595)

- The refactoring engine does not detect when an Objective-C class has a Swift subclass.

  When doing Objective-C refactoring, any changes needed in Swift subclasses will need to be made by hand. (16465974)

- Incremental builds of app extensions that use Swift fail with a code signing error.

  Choose Product > Clean and then build again to workaround this issue. (17589793)
- A mixed Swift and Objective-C project may not rebuild fully after a header is changed.

  Choose Product > Clean and then build again to workaround this issue. (17963128)

- The build step which embeds the Swift standard libraries in a bundle only runs for application product types, and only if the application itself, independent of any embedded content, contains Swift source files.

  When building an application that does not contain Swift source files but embeds other content (like frameworks, XPC services, app extensions, and so on) that does contain Swift code, you must set the build setting _Embedded Content Contains Swift Code_ (`EMBEDDED_CONTENT_CONTAINS_SWIFT`). That way the Swift libraries will be included in the application. (17757566)

- After upgrading to Xcode 6, users need to rejoin their ADC development team in OS X Server. (17789478)

- Renaming Xcode.app after running any of the Xcode tools in that bundle may cause iOS simulator to be no longer be available.

  Either rename Xcode.app back to what it was when first launched or restart your Mac. (16646772)
- Testing on iOS simulator may produce an error indicating that the application could not be installed or launched.

  Re-run testing or start another integration. (17733855)
- Settings changed in the Settings app on iOS Simulator may not persist. (18238018)
- Deleting an app from iOS Simulator doesn’t delete user defaults. (18307910)

- Opening the Source Control menu in Xcode when a project references a working copy that is not checked out sometimes causes crashes.

  Delete the `.xccheckout` file within the project. (17905354)
- When updating a Subversion working copy with local modifications and an incoming change modifies the open project file (project.pbxproj), the status icons for the files modified before the update may not appear until Xcode is relaunched.

  Restart Xcode. (18122757)

- The XCTest class file template allows creation of a test class using Swift as the implementation language for OS X projects. However, Xcode version 6.0 does not support Swift development for OS X. Attempting to build a Swift test class in an OS X test target with Xcode 6.0 results in a compiler error. (18107068)
- Dead code stripping may remove public declarations needed for test class implementations from Swift application targets.

  Turn off dead code stripping in configurations where you are building tests. (18173029)
- XCTest test classes written in Objective-C cannot import the Swift generated interfaces header (`$(PRODUCT_MODULE_NAME)-Swift.h`) for application targets, and cannot be used to test code that requires this header.

  Write test classes for Swift code with Swift. Test classes written in Objective-C for framework targets can access the Swift generated interfaces by importing the framework module using `@import FrameworkName;`. (16931027)

- Tools that support Carbon development are deprecated with Xcode 6. These include: BuildStrings, GetFileInfo, SplitForks, ResMerger, UnRezWack, MergePef, RezWack, SetFile, RezDet, CpMac, DeRez, MvMac, and Rez. (10344338)

- OCUnit and the SenTestingKit framework are deprecated and will be removed from a future release of Xcode. Source code using OCUnit will generate warnings while being compiled. Developers should migrate to XCTest by using Edit > Refactor > Convert to XCTest. For more information, see _[Testing with Xcode](../../../documentation/Developer%20Tools/Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_.

- Updated compiler options logic allows "Enforce Strict Aliasing" to be set to off with the `-Ofast` flag (16368909)
- Errors when using `xcodebuild -parallelizeTargets` option or equivalent Xcode build setting (16420957)

- Crash in compiled code when using ARC and C++ (16368824)
- Compiler error when using the `-fsanitize=undefined-trap` and `-fsanitize-undefined-trap-on-error` options (16387418)
- Crash in compiled code when targeting iOS 5.1.1 (16485980)
- Compiler crashes when compiling C++ initializers and other situations (16438726, 16368865)

- Crashes and errors in the linker related to LTO, dead stripping, and branch out of range (16368534, 16368564, 16368631)

- Xcode crash when debugging (16369101)
- Issue where some objects would not display in the Quick Look display on the first try (16368930)
- Inconsistent behaviors in the `UIView` Quick Look display (16368999)
- Problem with Quick Look for `UIImageView` (16489265)
- Xcode crash with multiple debugging sessions (16369025)

- Compiler error after converting a project from OCUnit to XCTest (16387456)

- Issue where Xcode Server sometimes incorrectly claims that the version of OS X Server is incompatible (16436893)

- Quick Look can be implemented for developer defined classes

  When an instance of a custom class is viewed with Quick Look in the debugger variables view or a data tip, the debugger presents it using a method named `-debugQuickLookObject` defined in the class implementation. For details on how to use this capability, see _[Quick Look for Custom Types in the Xcode Debugger](../../../documentation/IDEs/Quick%20Look%20for%20Custom%20Types%20in%20the%20Xcode%20Debugger/About%20Variables%20Quick%20Look%20for%20Custom%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dambr)_. (12723736)
- Log breakpoint actions now print out the logical value of expressions.

  For example, a log breakpoint action such as `"myString = @myString@"` now prints the value of `myString`, rather than the pointer value. (13211695)

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

- Instruments now finds symbols much more reliably.

  If symbols aren't showing up automatically, try the following:

  - When Spotlight indexing is disabled for Xcode derived data, such as when using `/tmp`, add a global list of additional search paths configured in the Instruments preferences.
  - The context menu for an address now includes the option “Symbolicate with DSYM” to add a specific symbol file.
  - Use the File menu Symbols command to see a more detailed list of the state of individual executables and libraries.

    - Green lights indicate the presence of symbols and source information.
    - Yellow lights indicate libraries with some symbols but can still benefit from locating a dSYM.
    - Red lights indicate situations that prevented symbolication. (14269449)
- The `instruments` command-line tool now supports specifying the simulator SDK and device type using the `-w` flag. To see a list of the supported simulator configurations as well as attached devices, execute `instruments -s devices` in a Terminal window. (14996865)

- Installing Device Support

  Run from the command-line, Xcode.app takes the new command-line argument, `-installComponents`. When Xcode is run from a command-line script with this option, it installs the required device support packages and then quits. (15127411)

- Emoji and other Unicode surrogate pairs are supported in scheme settings and in project files. (14837623, 13827044)

- Arm64 is now included in the “Standard architectures” setting.

  Xcode 5.0 introduced support for building 64-bit iOS applications but it was not enabled by default. To enable the option of building 64-bit in Xcode 5.0, an architectures setting was provided: “Standard Architectures Including 64-Bit” (`ARCHS_STANDARD_INCLUDING_64_BIT`).

  With the introduction of Xcode 5.1, arm64 is included in the default "Standard architecture” build setting. This results in projects using the default setting automatically building for arm64 along with the standard 32-bit architectures.
- Projects configured to use ”Standard Architectures Including 64-bit” will be converted to “Standard Architectures `$(ARCHS_STANDARD)`.

- As of Apple LLVM compiler version 5.1 (clang-502) and later, the optimization level `-O4` no longer implies link time optimization (LTO). In order to build with LTO explicitly use the `-flto` option in addition to the optimization level flag. (15633276)
- The Apple LLVM compiler in Xcode 5.1 treats unrecognized command-line options as errors. This issue has been seen when building both Python native extensions and Ruby Gems, where some invalid compiler options are currently specified.

  Projects using invalid compiler options will need to be changed to remove those options. To help ease that transition, the compiler will temporarily accept an option to downgrade the error to a warning:

  `-Wno-error=unused-command-line-argument-hard-error-in-future`

  To workaround this issue, set the `ARCHFLAGS` environment variable to downgrade the error to a warning. For example, you can install a Python native extension with:

  `$ ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future easy_install ExtensionName`

  Similarly, you can install a Ruby Gem with:

  `$ ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future gem install GemName` (16214764)

- The `gcov` tool for code coverage testing has been reimplemented. The new version uses the `llvm-cov` tool from the LLVM project. It is functionally equivalent to the old version for all significant features. The location of `gcov` within Xcode has also moved, use xcrun to invoke it. If you find problems, please file bug reports. For this release, you can still use the old version of `gcov` from GCC, which is available as `gcov-4.2`. (11919694)

- Custom views added to a stack view in Interface Builder can get stuck in a “misplaced views” (inconsistent) state.

  As a workaround, set a placeholder intrinsic size for the custom view with appropriate content hugging and compression resistance priorities. (15778653)

- Automated tests run in iOS Simulator may fail with an error similar to this:

  `Test target [test name] encountered an error (Test process exited with code -1)`

  Attempt recovery by quitting and restarting the simulator. (15929053)

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

- Performance issues can arise when running apps within the iOS Simulator on OS X Mavericks with a simulated OS version of iOS 6.1 or earlier.

  A workaround is to disable timer coalescing while using the iOS 6.1 or earlier simulator by executing the following command in a Terminal window:

  `sudo sysctl -w kern.timer.coalescing_enabled=0` (15501929)
- iOS Simulator sometimes stops responding to hardware keyboard.

  Quitting and relaunching the simulator usually corrects this. (14642684)

- Quick Look for `UIView` and `UIColor` variable types may not always work correctly.

  You can capture variables of these types as `id` rather than `UIView` or `UIColor`. 16065049

- When validating multiple applications in sequence using the Xcode Organizer, erroneous warnings about bundle IDs may be emitted.

  If these warnings occur, quit & relaunch Xcode in between validations. (15113664)
- Executables created by Xcode 5.1 may crash on OS X v10.5. (15852259)

- The `XCTAssertEqual` macro (formerly `STAssertEquals` using OCUnit) correctly compares scalar values of different types without casting, for example, `int` and `NSInteger`. It can no longer accept nonscalar types, such as structs, for comparison. (14435933)

- OS X apps that require a provisioning profile, such as those using iCloud, now build, are code-signed correctly, and launch. (15841159)

- OCUnit and the SenTestingKit framework are deprecated and will be removed from a future release of Xcode. Source code using OCUnit generates warnings while being compiled in Xcode 5.1.

  Migrate to XCTest by using the “Edit > Refactor > Convert to XCTest…” menu command. .
- The ATS framework is deprecated. Source code using ATS APIs will generate warnings while being compiled. For version 10.8, there will be no loss of functionality but there could be areas where performance will suffer.

  Replace all ATS code (including `ATSUI`) with `CoreText`. ATS functionality will be removed in future OS X releases.
  More information about this change is available in _[Core Text Programming Guide](../../../documentation/Strings%20Text%20Fonts/Core%20Text%20Programming%20Guide/About%20Core%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzt)_.

The following known issues are noted for Xcode 5.0.2 in addition to what has been listed for Xcode 5.0.1.

- In iOS 7 Interface Builder documents, when a vertical spacing constraint is created between a view that is flush with the top or bottom layout guide, a constraint between the guide’s top edge and the view’s bottom edge may be created instead of from the guide’s bottom edge to the view’s top edge.

  Move the view 1pt down (if to the top layout guide) or up (if to the bottom layout guide), create the vertical spacing constraint, then change the constraint’s constant from 1 to 0. 14627548

- The message “Could Not Start Script : Target app is not frontmost” may be displayed when attempting to capture a UI Automation script in Instruments against the iOS 7 Simulator.

  If this occurs, close the trace document and create a new one. 15387075

- LLDB now correctly displays structs in simulator processes. 14496092
- Debugging an application on a device running iOS 6.x caused the application to crash with EXC_BAD_ACCESS. 15310896

- After installation of Xcode, the iOS 7.0.3 simulator would hang on first launch for a period of time (eventually launching). 15368009
- Running UIAutomation from the Instruments GUI or from the `/usr/bin/instruments` command line would hang. 15367995

- Launching a 64-bit application on a device from Xcode multiple times caused the device to stop responding (and required a soft-reset). 15338361

- The documentation window now has a navigator area that contains a library browser and the bookmarks list. You can show the current document in the library browser using either the Editor > “Reveal in Library” menu item or by selecting the contextual menu "Reveal in Library.” 12116524

- New application targets created in Xcode 5 will crash on launch on iOS 5.

  Turn off Base Localization if your app targets iOS 5. 13979280
- Building a project from inside VMWare that is accessible via a VMWare shared folder can cause the compiler to crash.

  Use AFP to share files instead. 14251948

- Communicating with a remote SVN repository over HTTPS can fail with an error similar to “Error validating server certificate for _server name_.”

  Edit the file `/Library/Server/Xcode/Config/xcsbuildd.plist` and change the `TrustSelfSignedSSLCertificates` key from `false` to `true`.

  Then, from a Terminal window, run: `sudo killall xcsbuildd`. 14639890
- SSH access permissions for remote repositories created from within Xcode are limited to only the user that created them, by default. The permissions for these hosted repositories cannot be changed from within Xcode.

  The permissions can be changed for a hosted repository in Server.app by visiting the Xcode service—under the repositories tab, double click the repository and change the access settings. 15193716

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

- In some cases the “Update Frames” command does not resize top-level views or windows.

  Use the “Update All Frames” menu item. 13716892
- Constraints owned by the clip view of a scroll view in Interface Builder, where the document view is a custom view, are removed at runtime.

  Create outlets to each of the constraints you want to keep and re-add them to the clip view at runtime. 15115315

- After importing images from a project into an image catalog, storyboards and xib files have broken image file references.

  The image names in Interface Builder are listed as `image-name.png` and should be shortened to `image-name` to repair the broken reference. 14042186

- Projects and targets which have only `strings` files as localized resources cannot be converted to use Base Localization. (The behavior you observe is that after checking the “Use Base Localization” checkbox in the project editor, the conversion sheet does not present any files to be converted and clicking the Finish button results in the checkbox becoming unchecked.)

  To convert to using Base Localization, a project or target must contain one non-`strings` resource enabled for localization. In the project navigator, select a resource you intend to localize (for example, an Interface Builder document or an image), then open the file inspector. In the Localization slice, click the Localize button and select the localization to add. Once complete, the conversion workflow displays the file and enables the checkbox. 15160454

- In the 32-bit iOS 7.0 simulator, manually calling `objc_msgSend_stret()` with a `nil` receiver can corrupt the stack pointer.

  Ensure that the receiver is non-`nil` before calling `objc_msgSend_stret()`. 14753273

- Watchpoints set on a variable from Xcode’s UI using the contextual menu in the variables view don’t work for some variables—for example, `self`. When this is the case you’ll notice that the watchpoint is not being hit when you would expect.

  To work around this issue, use the console in Xcode to create a watchpoint at the `lldb>` prompt with the command `watchpoint set variable <variable-name>`. 12658775
- When ending the debug session of an app on an iOS 5 device, the error message “Lost Connection” may be displayed.

  Dismiss the error pop-up. It is spurious and does not indicate any problem debugging your app or connecting to the device. 14871460
- If an application on an iOS device is paused in the debugger within the method `-application:didFinishLaunchingWithOptions:`, the debugging session must be stopped before building and relaunching the same application with a different build configuration.

  If the application is not stopped first, the device can enter a state where it will no longer launch applications. If the device enters this state, it must be rebooted in order to be used for development again. 14851115
- If an iOS app running in the simulator is detached, a relaunch of the same app from Xcode will result in a black screen in iOS Simulator even though the new instance of the app is launched.

  Terminate the app in the simulator, or relaunch it a second time. 14648784

- The OpenGL ES frame debugger fails to display texture mip-levels for textures that are not texture-complete. 14852587

- The Allocations instrument can only attach to processes on devices running iOS 7.

  Processes must be started by Instruments for earlier versions of iOS. 14065257
- When attaching with the Allocations instrument to a process running on an iOS 7 device, the target process may crash and the recording in the Allocations instrument then stops immediately. When attaching with Allocations to a process on an iOS 6 or earlier device, the target process should continue to run but no data will be collected in Allocations.

  Launch with Xcode and then attach with Instruments or transfer to Instruments by clicking “Profile in Instruments,” using the memory gauge in the debug navigator. 14828459

- XCTest does not support iOS 6 destinations.

  Xcode does not prevent you from using XCTest with iOS 6 destinations, resulting in undefined behavior. 14075515

- Sometimes after requesting a signing identity from the Member Center, Xcode does not install the corresponding certificate in the keychain.

  To work around this issue, perform the following steps:

  1. View the Accounts section of Xcode’s preferences
  2. Select the account or team that corresponds to the signing identity
  3. Click “View Details”
  4. Click the Refresh button at the lower-left of the details sheet 14197131

- Xcode may have trouble connecting to repositories if credential information has changed after the repository was added in the Accounts preferences. In certain cases, Xcode displays a failure when connecting to a repository while it is actually attempting to connect in the background.

  If you encounter a repository connection problem, remove and re-add the repository with the updated credential information. This will restore access to the repository. 13955597

- After switching the minimum deployment target of an application from iOS 7.0 to a release prior to iOS 7.0, building and running the application may fail with the message “iOS Simulator failed to install the application.”

  To resolve this issue go to the iOS Simulator home screen. Remove the application by clicking and holding the application icon, and then choosing to delete the application by tapping the hovering “X” button. 13917023
- The Mac hardware keyboard may not function for iOS Simulator when first launched.

  Relaunch the simulator. 13315258
- StoreKit (In-App purchases) will not work in the Simulator. 13962338

- When playing video via the Quicklook framework on an iPhone simulator, the video view appears black, but audio continues to play fine. 13871109

- Views without an autoresizing mask in Interface Builder documents did not open correctly. 14969450
- When loading nibs at runtime with scroll views built with Xcode 5, constraints between the clip view and its document view were not handled properly. 14097019

- Creating distribution signing assets caused Xcode to crash. 13956010

- Launching an app using OpenGL on more than a single device failed. 14836639

- Subversion URLs caused errors with variable username usage. 14825641
- Using HTTPS and a git repository with a self-signed certificate failed. 14060992

  If you are interacting with a hosted git repository on OS X Server using HTTPS and are presented with a certificate dialog, to use the git repository:

  1. Click “Show Certificate” on the bottom-left of the dialog
  2. Check the “Always Trust” checkbox
  3. Click “Continue”

  You are now able to use the git repository in Xcode.

- Xcode 5 does not support downloading additional doc sets. Additional doc sets can be added manually by installing them at `~/Library/Developer/Shared/Documentation/DocSets/`.

  Once installed, doc sets are found and loaded by Xcode 5. If Xcode is running while the doc set is installed, quit and relaunch Xcode. 14930443

- iOS 64-bit compatible applications are only supported with a minimum deployment target of iOS 5.1.1 or above. 15190445

- The provisioning profiles list in the Organizer is now located in the Accounts tab of Xcode's preferences. To view them, select the relevant Apple ID account and tap View Details. 13950944

- Xcode 5 does not support use of the LLVM-GCC compiler and the GDB debugger. 14857582
- Garbage collection is a deprecated technology in OS X Mountain Lion and later. Xcode 5 is scheduled to be the last release of the Xcode developer tools to support building, debugging, or profiling Mac apps that use garbage collection.

  It is recommended that any projects using GC employ Xcode’s migration tool to convert to ARC (Automatic Reference Counting). For more information about transitioning to ARC, see _[Transitioning to ARC Release Notes](../../Objective%20C/Transitioning%20to%20ARC%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrw)_. 14406894
- The CVS and RCS source control tools have been removed from Xcode 5. 11968433
- The CPlusTest unit testing framework has been removed from Xcode 5. To write unit tests for C++ code, use the new XCTest framework and create Objective-C++ (.mm) test case subclasses. 8273037
- `SenTestingKit` and `OCUnit` are deprecated. Use the migrator to move to XCTest. 14857574

- To ensure that OS X Server is configured to use Xcode 5.0.1, follow these steps to install Xcode:

  1. Open the App Store and update OS X Mavericks
  2. Download Xcode 5.0.1 and OS X Server
  3. Quit Xcode and Server
  4. Install Xcode 5.0.1
  5. Install OS X Server
  6. Open Server
  7. Select the Xcode service, then click Choose and select Xcode 5.0.1

- When reporting a Continuous Integration bug, enter the following command in Terminal, then attach the output to the bug report.

  `sudo /Applications/Server.app/Contents/ServerRoot/usr/sbin/serverloggather`

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

- Command line shims are included with OS X Mavericks. If Xcode is installed, the shims use the tools within Xcode. Otherwise, the tools delivered in the Command Line Developer Tools package are used. The Command Line Developer Tools package can be installed on demand using `xcode-select --install` or by trying to use any command line developer tool in Terminal.

  On OS X Mavericks, Command Line Developer Tools are updated using Software Update. On OS X Mountain Lion, continue to use the Downloads preferences in Xcode to update the Command Line Developer Tools.

  On OS X Mavericks, `xcode-select` provides the `--reset` flag to revert to using the default search paths.

  The Command Line Developer tools package has been updated to include `xcrun`. `xcrun` adds support for the following:

  1. The `--show-sdk-path` option queries SDK paths
  2. Improved `xcrun` performance
  3. More robust support for the `DEVELOPER_DIR` environment variable

     Set `DEVELOPER_DIR` to either a copy of Xcode or `/Library/Developer CommandLineTools` when Command Line Tools for OS X Mavericks is installed
  4. `xcrun` passes the SDK provided to subcommands in the `SDKROOT` environment variable when used with --sdk. 15190491

- Building a project from inside VMWare that is accessible via a VMWare shared folder can cause the compiler to crash.

  - Use AFP to share files instead. 14251948
- In the 32-bit iOS 7.0 simulator, manually calling `objc_msgSend_stret()` with a `nil` receiver can corrupt the stack pointer.

  - Ensure that the receiver is non-`nil` before calling `objc_msgSend_stret()`. 14753273

- New application targets created in Xcode 5 will crash on launch on iOS 5.

  - Turn off base localization if your app targets iOS 5. 13979280

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

- In some cases “Update Frames” will not resize top level views or windows.

  - Use the “Update All Frames” menu item. 13716892
- Sometimes when editing UITableViews in Auto Layout documents set to open in Xcode 4.6, you get an error message saying “Failed to automatically update constraints.”

  - Upgrade your document to the Xcode 5 format using the “Opens in” option in the File inspector. After performing the desired edits, you can downgrade back to the Xcode 4.6 format if necessary. 14680132

- Scripts running under the Automation instrument sometime fail to detect applications running inside the iOS 6 simulator environment.

  - Relaunch the simulator application and run the script again. 14447965
- The Allocations instrument can only attach to processes on devices running iOS 7. Processes must be started by Instruments on iOS versions prior to iOS 7. 14065257
- When attaching to a process running on an iOS 7 device with the Allocations instrument, the process may crash and the recording in the Allocations instrument then stops immediately. When attaching to a process on an iOS 6 or earlier device with the Allocations instrument, the process continues to run but no data will be collected in Allocations.

  - Launch with Xcode and then attach with Instruments. Alternatively, transfer to Instruments by clicking “Profile in Instruments” in the debug memory gauge. 14828459

- When ending the debug session of an app on an iOS 5 device, the error message, "lost connection" may be displayed.

  - Dismiss the error pop-up: It does not indicate any problem debugging your app or connecting to the device. 14871460
- Watchpoints set from the Xcode UI using the contextual menu on a variable in the variables view don’t work for some variables , for instance `'self'`. When this is the case, the watchpoint won’t be hit when you expect.

  - To work around this issue, use the console in Xcode to create a watchpoint at the lldb prompt with the command `'watchpoint set variable <variable-name>'`. 12658775

- The OpenGL ES frame debugger does not display texture mip-levels for textures that are not texture-complete. 14852587
- Simultaneously launching an iOS app which uses OpenGL from Xcode on more than a single device may not work.

  - Launch on one device at a time. 14836639

- XCTest does not support iOS 6 destinations. Xcode does not prevent you from using XCTest with iOS 6 destinations, resulting in undefined behavior. 14075515

- Xcode may have trouble connecting to repositories if credential information has changed after the repository was added in Accounts preferences. In certain cases, Xcode displays a failure when connecting to a repository while it is attempting to connect in the background.

  - If you encounter a repository connection problem, remove and re-add the repository with the updated credential information. This will restore access to the repository. 13955597
- Xcode 5 requires consistent usage of Subversion URLs: Either always include the (same) username or do not include one for a given repository. 14825641

- If an iOS app is detached, relaunching the same app from Xcode will result in a black screen in the Simulator even though the new app is launched.

  - Terminate the app in the Simulator or relaunch it for the second time. 14648784
- After switching the minimum deployment target of an application from iOS 7.0 to a release prior to iOS 7.0, building and running the application may fail with the message “iOS Simulator failed to install the application.”

  - Go to the iOS home screen, click and hold the application icon, then tap the hovering “X” button to delete the application. 13917023
- StoreKit (In-App purchases) will not work in the Simulator. 13962338
- When playing video via the Quicklook framework on an iPhone simulator, the video view appears black, but audio continues to play fine. 13871109
- The Mac hardware keyboard may not work for iOS Simulator on first launch.

  - Relaunch the simulator. 13315258

- Xcode sometimes crashes if you request to create distribution signing assets during distribution of a Mac app.

  - Create the distribution signing assets using the Member Center. 13956010
- Xcode sometimes does not install the corresponding certificate in the Keychain after requesting a signing identity from the Member Center.

  Workaround:

  1. View the Accounts section of Xcode’s preferences.
  2. Select the account/team that corresponds to the signing identity.
  3. Click “View Details.”
  4. Click the Refresh button at the lower-left of the details sheet. 14197131

- The provisioning profiles list in the Organizer is now located in the Accounts tab of Xcode's preferences. To view them, select the relevant Apple ID account and click View Details. 13950944
- 64-bit compatible applications are only supported with a minimum deployment target of iOS 6 or later. 14730546
- Xcode 5 does not support using the LLVM-GCC compiler or the GDB debugger. 14857582

- The CPlusTest unit testing framework has been removed from Xcode 5. To write unit tests for C++ code, use the new XCTest framework and create Objective-C++ (.mm) test case subclasses. 8273037
- SenTestingKit and OCUnit are deprecated. Use the migrator to move to XCTest. 14857574

- The CVS and RCS source control tools have been removed from Xcode 5. 11968433

- Xcode 5 does not support downloading additional doc sets.

  Additional doc sets can be added manually by installing them at `~/Library/Developer/Shared/ Documentation/DocSets/`

  Once installed, doc sets are found and loaded by Xcode 5. If Xcode is running while the doc set is installed, quit and relaunch Xcode. 14930443

- Xcode 5 ending support for OS X garbage collection.

  Garbage collection is a deprecated technology in OS X Mountain Lion and later. Xcode 5 is scheduled to be the last release of the Xcode developer tools to support building, debugging, or profiling Mac apps that use garbage collection. It is recommended that any projects using GC employ the Xcode migration tool to convert to ARC (Automatic Reference Counting.) More information about transitioning to ARC is available at: _[Transitioning to ARC Release Notes](../../Objective%20C/Transitioning%20to%20ARC%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytemrw)_. 14406894

- Continuous integration features (bots) require OS X Server for OS X Mavericks. Mac Developer Program members can download the latest developer preview of OS X Mavericks from the Mac Dev Center. 14949282

- Hang when debugging in iOS Simulator on OS X 10.8.4. 13722320

- Kernel extensions (kexts) built with Xcode 4.6.1 and 4.6.2 fail to load on OS X 10.6 and 10.7, and this error message appears in the console:

```
kernel: kxld: The Mach-O file is malformed: Invalid segment type in MH_KEXT_BUNDLE kext: 42
```

To build kexts that load on OS X 10.6 and 10.7, on the targets that build the kexts, set the OS X Deployment Target build setting to OS X 10.6. 13645170

- Implemented stability fixes. 13518419, 13518436, 13518436, 13518526, 13611415

- If you build code signed kexts on OS X 10.8.3 (you turn on code signing in the target that builds the kext), that kext fails to load on OS X 10.7.x and earlier, and this error message appears in the console:

```
kernel: kxld: The Mach-O file is malformed: Invalid segment type in MH_KEXT_BUNDLE kext: 29
```

  Workarounds:

  - To build an unsigned kext that loads in OS X 10.7.x and earlier, in the target that builds the kext, set the Code Signing Identity build setting to Don’t Code Sign.

    If you need to build signed and unsigned versions of the kext, you can have in your project separate targets that build the same kext, one configured to code sign the kext and the other configured not to sign it.
  - To build a signed kext that loads in OS X 10.7.x and earlier, code sign the kext on a Mac running OS X 10.8.2 or earlier. 13428950

- When building a product previously built with Xcode 4.6.1 or earlier, the build fails with an error similar to this one:

```
PCH file built from a different branch ((clang-425.0.27)) than the compiler ((clang-425.0.28))
```

  To address this issue, choose Product > Clean before building your product. 13663167

- SDKs:

  OS X SDK 10.8.3 (13130441)

- Crash on launch on OS X v10.6 with apps using ARC built with Xcode 4.6. (13129783)

- Documentation doc set update fails with the message:

```
Install path <path_1> points to a different documentation package <path_2> than expected <path_3>
```

  13292012.

- More than one Xcode doc set listed in the Documentation organizer. 13207501

To address this issue delete any Xcode doc set whose version number is earlier than 509.12 from Documentation preferences:

1. Open the Xcode preferences window, and click the Downloads button to display Downloads preferences.
2. Click the Documentation button.
3. Select an Xcode doc set (titled “Xcode ...”).
4. Reveal the doc set info by clicking the Show Doc Set Info button (to the left of the + button).
5. If the version of the doc set is earlier than 509.12, delete the doc set by clicking the Remove (–) button.

- SDKs:

  - OS X SDK 10.8
  - iOS SDK 6.1
- Device support (added):

  - iPad mini
  - iPad with Retina display (4th generation)

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

- Xcode UI: Inspects elements of [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray) and [NSDictionary](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDictionaryClassClstr/Description.html#//apple_ref/occ/cl/NSDictionary) objects.
- LLDB: Reads metadata from the Objective-C runtime.
- LLDB: Improves support for stepping over inlined functions.
- LLDB: Prints function argument information in backtraces by default.
- LLDB: Supports “thread return,” the `temporary breakpoint` command, and a variety of aliases to add common GDB shortcuts.

- DEPRECATED: LLVM-GCC compiler and GDB debugger.

  Xcode 4.6 is the last release to include the LLVM-GCC compiler and the GDB debugger.

  Use the LLVM compiler and the LLDB debugger, and file reports at [https://bugreport.apple.com](https://bugreport.apple.com/) for issues that require the use of LLVM-GCC or GDB.
- DEPRECATED: Package Maker app.

  Use the `productbuild` command to create installer packages
- DEPRECATED: ATS.framework (OS X SDK 10.8).

  The use of the ATS API produces compilation warnings.

  In OS X v10.8 there is no loss of functionality, but there could be areas where performance degrades.

  Replace ATS code (including ATSUI) with Core Text calls (see _[Core Text Programming Guide](../../../documentation/Strings%20Text%20Fonts/Core%20Text%20Programming%20Guide/About%20Core%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmzt)_ for details).

- Fixed Xcode app and LLDB debugger crashes reported on Xcode 4.5. 12482521, 12482518, 12481393, 12481829, 12481363, 12481302, 12481396, 12482364, 12514294, 12364375, 12481322, 12481370, 12481398, 12481373, 12489094, 12483605, 12481863, 12482083, 12482540, 12481426, 12482542, 12481390, 12482362, 12481885

- Improved stability when editing storyboards and using Auto Layout. 12482514, 12482536, 12482526, 12482548

- Fixed an LLDB memory leak. 12483722
- Improved behavior when quitting iOS Simulator directly. 12481405

- Fixed occasional Xcode hang when submitting an app to the iOS App Store. 12482847

- Improved the responsiveness of the Open Quickly dialog. 12251666
- Improved performance switching between tabs in the Xcode app. 12364395

- Improved stability and responsiveness running apps on a simulator. 12388056, 12364385, 12364295

- Crashes while editing user interface documents. 12364019, 12389062, 12388854, 12389040, 10261299

- Issues adding keys to property list files. 12377407

- Debug console doesn’t display all input characters. 12364400

- Issues interacting with working copies known by the Xcode app. 12364258, 12389205, 12389198

- The Interface Builder canvas includes a new button to toggle between iPhone screen layouts. When you click the button, Xcode resizes full-screen views to match the selected iPhone screen size. When the top level views are resized, Xcode uses the resizing rules specified by layout constraints or springs and struts in the size inspector to reflow the contained views. 12290237

  Use this button to toggle between layouts and ensure that the resizing rules you define work as expected on both the new Retina 4 screen and previous screen sizes.

- Storyboards now support view controller containment. You can add child view controllers to a parent view controller in a storyboard. At runtime, when the [viewDidLoad](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621495-viewdidload) method is called on the parent controller, its view hierarchy (composed of the view hierarchies of its child controllers) is already loaded. 9630246

  To add a view controller as the child of another view controller:

  1. Add a container view from the Object library.
  2. Connect the container view to the child view controller with an embed segue.

- When Xcode autocreates schemes, it now adds the new schemes in project order (within the workspace) and target order (within each project). 7996506

- You can now specify that modal segues be presented without animation. 10384049
- You can now create unwind segues that allow transitioning to existing instances of scenes in a storyboard. 9211697.

  With earlier releases of Xcode, you may have implemented unwind segues programmatically. See [iOS SDK Usage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanjrfvbuqmjnknltmnjq) for details.

- When your app runs on iOS 6.0 or later, in the [shouldPerformSegueWithIdentifier:sender:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621502-shouldperformseguewithidentifier) method of your [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller) subclass, you can decide whether to trigger a segue with a specific identifier, which you set in the segue’s Attributes inspector. 9447109

- When you update your Subversion-managed project, Xcode now automatically applies the update if there are no conflicts. 11913482

  To see changes from the repository before applying them, choose File > Source Control > Update while holding down the Control key.

- This version of Xcode does not generate armv6 binaries. 12282156
- The minimum deployment target is iOS 4.3. 12282166
- In this Xcode release, Auto Layout is turned on for new user interface documents (storyboards and nib files). Because Auto Layout requires iOS 6.0, using such user interface documents on earlier iOS releases results in a crash or other undefined behavior. 12289644

  For your app to run on earlier iOS releases, turn off Auto Layout in its user interface documents.

- This release of Xcode doesn’t allow submitting to the App Store apps with iOS Deployment Target set to iOS releases earlier than iOS 4.3. The validation process fails with the message “This bundle is invalid. The key UIRequiredDeviceCapabilities in the Info.plist may not contain values that would prevent this application from running on devices that were supported by previous versions.” 12309358

  Set the app’s iOS Deployment Target to iOS 4.3 or later.

- Projects created using this Xcode release use the new libc++ implementation of the standard C++ library. The libc++ library is available only on iOS 5.0 and later and OS X 10.7 and later. 12221787

  To enable deployment on earlier releases of iOS and OS X in your project, set the C++ Standard Library build setting to libstdc++ (Gnu C++ standard library).

- Uploading app data files to an iOS device works correctly on OS X v10.7 and v10.8. 12017933

- RCS and CVS are deprecated in this Xcode release. 12252058

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
  3. Open a new shell window, and verify that `MANPATH` lists the paths to the `Xcode.app` package you’re using.
  4. Index the man pages by executing this shell command:

```
sudo /usr/libexec/makewhatis
```


- When you add a gesture recognizer in a storyboard, it mistakenly overrides the system-supplied gesture recognizers for the target view. For example, adding a tap gesture recognizer to a table view results in a table view that does not scroll. 12200238

  Disconnect the gesture recognizer in the storyboard, and apply it in code.

- A UI automation script being run with a simulator target in Instruments fails if your Mac contains multiple copies of Xcode and the Xcode install path is not set up correctly. 12288632

  Determine the path to the running Xcode instance by executing this shell command:

```
$ xcode-select --print-path
```

  If the returned path doesn’t point to the running Xcode instance, execute this shell command:

```
$ xcode-select -switch <path_to_the_Xcode_package>
```

  - In the command, `<path_to_the_Xcode_package>` is the path to the `Xcode.app` package you’re using—for example, `/Applications/Xcode.app`.

- Xcode may not show any windows when it’s launched. This happens when you download Xcode from [https://developer.apple.com](https://developer.apple.com/) and the “Close windows when quitting an application” preference in System Preferences is unselected. 11865559

  Switch to another app and relaunch Xcode.

- MobileMe syncing support is deprecated. However, the `syncable` property is still set to `YES` by default in the User Info Dictionary for entities and properties, but the model editor doesn’t show this setting. 10787672

  To explicitly set `syncable` to `NO` for an entity or a property, add a key-value pair in your User Info Dictionary:

  1. Select the entity or property for which you want to turn off synching on a model file.
  2. In the User Info section in the Data Model inspector, add this key-value pair:

|  |  |
| --- | --- |
| key | `"com.apple.syncservices.Syncable"` |
| value | `"NO"` |

- Text and font rendering on OS X v10.8 is optimized for Retina display. On a non–Retina display running OS X v10.8, some font configurations can appear blurry in Xcode. 11486875

  Switch back to non–Retina display optimized text and font appearance in Xcode by entering this command in Terminal:

```
defaults write com.apple.dt.Xcode NSFontDefaultScreenFontSubstitutionEnabled -bool YES
```


- When you select the Use Base Internationalization option in the project editor, Xcode generates strings files for each your project’s user interface documents. 11462724

  To resynchronize your strings files with new content from your user interface documents, use the `--generate-strings-file` option of the `ibtool` command to produce new strings files. Then, manually merge the new files into your existing localized strings.

- At runtime, when adding subviews to a split view while loading both views from nib files, you may see log messages about unsatisfiable constraints because of autoresizing mask constraints on the split view panes. These are benign log messages because a split view automatically fixes the problem after adding the subview. 11614767

  In your code, before adding the subview to the split view, send `setTranslatesAutoresizingMaskIntoConstraints:NO` to the subview.

- The `po`, `print`, and `expression` commands cannot access enumerators directly. You must use the name of the enumeration. 11485295

  For example, if your code contains `enum MyEnum { e1, e2 };`, LLDB emits an error if you type `print e1`. Instead, type `print MyEnum::e1`.

- Xcode no longer preserves an app’s designated requirements when you submit it to the App Store. 12006125

  Some apps where prevented from submission because of designated requirements.

- After quitting iOS Simulator directly, Xcode continues to show the process launched on the simulator as running. 11998376

- Xcode doesn’t offer code completion in Objective-C++ files. 12006547

- The LLDB debugger gets the wrong address for some variables. 12006552
- When compiling an Objective-C++ file in C++11 with vectors under automatic reference counting (ARC), the LLVM compiler generates incorrect code. 12006560
- Objective-C code compiled under ARC and optimized for size may crash at runtime. 12006567

- Xcode becomes unresponsive while running unit tests. 12017975

- Uploading app data files to an iOS device may not work. 12017933

  - On OS X v10.8, duplicate the `.xcappdata` file, and upload the duplicate.
  - On OS X v10.7 there is no workaround to this issue.

- You can drag file, directory, and group icons from the jump bar to the project navigator, a Finder window, and other apps. 7452760
- The Use Base Internationalization setting in the project editor works only on Mac products for deployment on OS X v.10.8 and later. Xcode must also be running on OS X v.10.8 or later. This setting is not supported on iOS projects. 11712855

- The source editor can remove trailing whitespace at the end of a line after you have edited it. You control this behavior with the “Automatically trim trailing whitespace” option in Text Editing preferences. 2535591
- When the “Automatically insert closing braces” option in Text Editing preference is turned on, as you type an opening parenthesis, brace, or quotation mark, the source editor adds the corresponding closing character. When the “Enable type-over completions” option is turned on, the editor adds the closing character in a state in which you can type over the character. This feature reduces the appearance of duplicate closing characters, such as when you type both the open and close characters quickly. 3780948

  Press Tab to jump over the closing character.

- __LLVM integrated assembler for ARM.__ This new assembler improves compilation times for iOS products, and provides better user level diagnostics for ARM assembly code. This assembler uses only Unified Assembly Language (UAL) assembly code; therefore, you may need to update projects that use manually generated assembly code. 9136376

  Use the `clang``-no-integrated-as` command-line option in projects with substantial Divided Syntax assembly code while transitioning to UAL.

- During a code completion interaction, Xcode gives higher priority to completions you have used recently. 9790948

- You can view and modify the root object of a custom property list file. 8635494

- When creating a project, you can choose whether to add it to a workspace or create a standalone project. 8032086

- When you hold down Option and place the pointer over views in the canvas, the distance values are not obscured by other elements, such as the resizing handles. 8204499

- You can rename a file just by changing the case of one of the letters in its filename, even on a case-insensitive file system. 7846036

- A failure to rebuild precompiled header (PCH) files causes syntax highlighting, code completion, and Command+click navigation to behave incorrectly. 11538640

  Delete the PCH index folder.
- Xcode may not show any windows when it’s launched. This happens when you download Xcode from [https://developer.apple.com](https://developer.apple.com/) and the “Close windows when quitting an application” preference in System Preferences is unselected. 11865559

  Switch to another app and relaunch Xcode.

- Text and font rendering on OS X v10.8 is optimized for Retina display. On a non–Retina display running OS X v.10.8, some font configurations can appear blurry in Xcode. 11486875

  Switch back to non–Retina display optimized text and font appearance in Xcode by entering this command in Terminal:

```
defaults write com.apple.dt.Xcode NSFontDefaultScreenFontSubstitutionEnabled -bool YES
```


- MobileMe syncing support is deprecated. However, the `syncable` property is still set to `YES` by default in the User Info Dictionary for entities and properties, but the model editor doesn’t show this setting. 10787672

  To explicitly set `syncable` to `NO` for an entity or a property, add a key/value pair in your User Info Dictionary:

  1. Select the entity or property for which you want to turn off synching on a model file.
  2. In the User Info section in the Data Model inspector, add this key/value pair:

|  |  |
| --- | --- |
| key | `"com.apple.syncservices.Syncable"` |
| value | `"NO"` |

- When you select the Use Base Internationalization option in the project editor, Xcode generates strings files for each your project’s user interface documents. 11462724

  To resynchronize your strings files with new content from your user interface documents, use the `--generate-strings-file` option of the `ibtool` command to produce new strings files. Then, manually merge the new files into your existing localized strings.

- The `po`, `print`, and `expression` commands cannot access enumerators directly. You must use the name of the enumeration. 11485295

  For example, if your code contains `enum MyEnum { e1, e2 };`, LLDB emits an error if you type `print e1`. Instead type, `print MyEnum::e1`.

- At runtime, when adding subviews to a split view while loading both views from nib files, you may see log messages about unsatisfiable constraints because of autoresizing mask constraints on the split view panes. These are benign log messages because a split view automatically fixes the problem after adding the subview. 11614767

  In your code, before adding the subview to the split view, send `setTranslatesAutoresizingMaskIntoConstraints:NO` to the subview.

- Xcode crashes when dragging tabs in full-screen mode. 9987358
- Xcode crashes when opening multiple workspaces that contain the same folder reference (blue folder). 10079252

- Installing Xcode on OS X v10.7.3 or later breaks the Xcode 4.3 Instruments app. 10619572

- After enabling autolayout in a nib file, the wrong constraints are applied. 8201103
- When resizing views that use autolayout, Xcode applies constraints to the descendants of the view being resized, but not to its siblings and ancestors. 9450655
- Xcode doesn’t allow constraints with negative values. 9717632
- When you create a user constraint, Xcode removes redundant constrains, which is not always desirable. 9794979
- You cannot add width and height constraints to top-level views. 9877773

- Xcode imports incorrect header in projects containing targets that produce different header files with the same name. 8201103
- A build may hang if Xcode encounters a build error and the “Continue building after errors” option in general preferences is turned on. 10642885

- The App Store app cannot install Xcode in the `/Applications` directory because there are beta releases of Xcode in that directory.

  Do not install beta releases of Xcode in the `/Applications` directory. 10824869

- Xcode cannot launch your app on a device for debugging after you install the iOS 3.x device debugging support component.

  Unplug and plug-in your device to your Mac, and ensure that you build your app for the armv6 architecture. 10538662

- Xcode doesn’t show code-completion suggestions when there are mismatched braces.

  Turn on the “Automatically insert closing "}"” option in text editing preferences to reduce the number of mismatched braces. 10775381

- Some debugger commands and log expressions in breakpoints fail when using the LLDB debugger because Xcode uses the wrong frame when executing the debugger command or evaluating the log expression.

  If you know what thread the the debugger command or log expression must run relative to, add a breakpoint action that sets the current frame to the appropriate one before the breakpoint action with the problem. 10426977

- The variables pane in the debug area does’t display correctly the child values of variables with dynamic types (Objective-C object pointers and virtual C++ pointers).

  Use the console pane in the debug area: enter the commands `frame variable *self` or `frame variable *this` to the values.10658091
- LLDB cannot be used to debug apps on devices running iOS 3.x or iOS 4.x.

  Set GDB instead of LLDB as the debugger in the scheme that builds your app. 10776590

- When there are more than one Xcode releases installed on your Mac, Xcode 4.3 may not find your app’s symbols when displaying crash reports and the trace data for instruments.

  To enable Instruments to find your app’s symbols when displaying trace data:

  1. In Instruments, choose File > Re-symbolicate Document.
  2. Search for you app’s name, and locate it in your app’s build directory, such as `~/Library/Developer/Xcode/DerivedData/<MyApp>`. 10552213
- You cannot run System Time Profile from the Instruments icon in the Dock by Control-clicking the icon and choosing System Time Profile.

  Control-click the Instruments icon in the Dock, and select the Allow Tracing of Any Process option. 10755622

- When Xcode attempts to authenticate Subversion repositories that require approval of a server certificate, one or more `svn` processes hangs.

  Authenticate the server in Terminal. 10042297

- You can install Xcode 4.2 for OS X v10.6 Snow Leopard only if you have purchased an earlier release of Xcode.

  Install or update Xcode through the Purchases or Updates panes.
- If you purchased Xcode from the Mac App Store, the Install Xcode app is on the volume on which you installed Xcode.

  To install Xcode 4.2 on another volume, you must delete all copies of the Install Xcode app from your file system.

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

- When initiating a refactoring rename operation from the declaration of a property, any Interface Builder files that refer to that property will not be updated correctly. Instead, perform the rename operation on a usage of the property, or an associated `@synthesize` statement.
- In Xcode 4.2, when copying views (either a single view or multiple views), both the user defined constraints on the selected view and the user defined constraints between the views are copied to the pasteboard.
- When developing Mac apps, changing the segment style of an `NSSegmentedControl` object to Automatic might crash in documents using Cocoa Auto Layout. To workaround the issue use an explicit segment style such as Round or Textured, and at runtime, change the segment style to automatic using the `setSegmentStyle:` method.

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

- When running Mac OS 10.7, Location Services are not functional in iOS simulator when simulating iOS 4.3 and earlier. This issue is not present when running Mac OS 10.6 or when simulating iOS 5.0.

- You can create and edit view-based `NSTableView` instances.

  Just drag an `NSView` subclass (usually `NSTableCellView`) from the Object library into each table column. After connecting the datasource and delegate outlets, implement at least these methods:

  - `– (NSInteger)numberOfRowsInTableView:(NSTableView *)tableView`
  - `– (id)tableView:(NSTableView *)tableView objectValueForTableColumn:(NSTableColumn *)tableColumn row:(NSInteger)row`

  You can bind the `objectValue` property of an `NSTableCellView` instance in Interface Builder. You can also make action connections from a cell to the cell’s owner, which is usually the table view’s delegate.

  By assigning identifiers to the view cells, you can use the `NSTableView` method `–makeViewForIdentifier:owner:` in the implementation of the table-view delegate method `–viewForTableColumn:row:`. 7465869

- If Xcode or `xcodebuild` fail to launch:

  - Hold down Shift while launching Xcode
  - Use the `xcodebuild -clearPlugInCache` option. 9013457

- Building products that require Interface Builder 3 plug-ins may fail because the `ibtool` command-line tool is unable to locate the required `ibplugin` plug-in.

  If you have the Xcode 3 toolset installed on your computer, load the plug-in using the Interface Builder 3 preferences window. Otherwise, use this command:

```
defaults write com.apple.InterfaceBuilder3 "IBKnownPluginPaths.3.2.7" -dict-add "<plug.in.identifier.string>" "<path_to_ibplugin>"
```

  8920581

- The `xcodebuild -activetarget` option is not supported. 8361726

- MallocDebug is replaced by the Allocations and Leaks instruments, and the `libgmalloc` (GuardMalloc) and `leaks` command-line tools. 4388187

- When using the OS X Core Data template, Instruments may hang or stop tracing. 9031942
- When you profile an application running in iOS Simulator, Instruments collects no data.

  To have Instruments collect data, click the Instruments icon in the Dock after it starts recording. 8909180

- Nib files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the nib file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406

- Xcode disallows dragging objects in the Interface Builder canvas to the Object library. 8656363

- Projects that use the Xcode 3 unit-testing tools cannot use the Xcode 4 unit-testing infrastructure.

  To use unit testing in your Xcode 3 projects, set the Test After Build build setting to No. 8803198

- __Refactoring:__ Xcode refactors Cocoa bindings. 8423815

- On a project with no snapshots, new snapshots appear in the projects organizer. 8774085

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

- Xcode disallows dragging objects in the Interface Builder canvas to the Object library. 8656363

- The unit-test command-line tools in `/Developer/Tools` are deprecated.

  To use unit testing in your Xcode 3 projects, set the Test After Build build setting to `NO`. 8803198

- Interface Builder files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the Interface Builder file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406
- The task log viewer is empty when you select the last build task of a project or workspace in the log navigator and the viewer is set to show only recent operations.

  Set the task log viewer to show all operations. 8350930

- Xcode cannot edit OS X–type Interface Builder documents comprised of objects from frameworks other than AppKit.

  You can compile and run these documents, however. 7470836

- There is new command-line tool for measuring an application’s performance without launching the Instruments application: `iprofiler`. After making the measurements, you can analyze them with Instruments. A new framework, DTPerformanceSession (located in `/Library/Developer/4.0/Instruments/Frameworks`) allows your application to create performance measurements of itself or other applications. 7773305

- In the Manage Schemes dialog you can specify whether to create schemes automatically with the “Autocreate schemes” option. You may want to turn off automatic scheme creation in a large workspace, where automatic scheme creation produces too many schemes. This setting is shared with all the users of the workspace.

  You can have Xcode create schemes with the Autocreate Schemes Now button. 7952053
- You can add an Xcode archive file (`.xcarchive`) to the archives organizer by double-clicking it in the Finder. 8791305
- You can use a workspace-relative location for derived data. 8242521

- Enhancements to the execution of alert scripts:

  - The scripts can access the Xcode user environment variables.
  - The value of the PWD environment variable is a path to the directory that contains the current project or workspace.
  - The new `XcodeAlertAffectedPaths` environment variable contains a colon-separated list of full paths to the affected files. This variable replaces the `IDEAlertAffectedURLs` environment variable. 8748528

- Xcode doesn’t strip newline characters from the scripts in Run Script scheme actions. 8230045
- Duplicating a scheme doesn’t result in a new scheme with broken target references. 8335950
- When the active scheme is a unit-test scheme, clicking Run in the toolbar doesn’t produce an unknown error dialog. 8642393

- __Editing nib files:__ The Rename transformation renames action methods in Interface Builder documents when the action’s target is the first responder or the method is declared in a category, protocol, or a superclass of the given class. 8500272
- __Source Control and Snapshots:__ Xcode creates a snapshot of your workspace before performing a refactoring transformation. 7816256

- After you create a branch and switch to it in the repositories organizer, using the commit dialog or the version editor doesn’t cause an assertion failure. 8383245

- Xcode recognize SCP-based URLs (such as `git@example.com:/myrepositoryname.git`) for Git repositories in the repositories organizer. 8044145

- After you change General preferences > Build Location, Xcode uses the new build location. 7965261

- Multicore and Dispatch templates are not working. 8717719
- Time Profiler and System Trace don’t work after installing Xcode 4.0 Developer Preview 6.

  Restart your computer. 8829655
- If your computer contains more than one release of Xcode, the Dock time profiler doesn’t work correctly.

  Add the Instruments application in the appropriate Xcode release to the Dock and restart your computer. 8830062

- Interface Builder files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the Interface Builder file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406
- The task log viewer is empty when you select the last build task of a project or workspace in the log navigator and the viewer is set to show only recent operations.

  Set the task log viewer to show all operations. 8350930

- Xcode cannot edit OS X–type Interface Builder documents comprised of objects from frameworks other than AppKit.

  You can compile and run these documents, however. 7470836
- __Refactoring:__ Xcode does not refactor Cocoa bindings. 8423815

- __Search navigator:__ Xcode may crash in the replace preview dialog of the search navigator when all the found instances are selected and you click Replace. 8091532

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

- You can create `NSManagedObject` subclasses from entities in a Core Data data model. 7484772

- The Extract transformation is supported. 7711619

- __Blocks:__`Goto` statements within blocks are allowed when the target is within the block. 7549164
- __Objective-C:__ Fixes bugs in exception handling present in LLVM 1.5. 8160285
- You can declare instance variables in class implementations and extensions (iOS and 64-bit OS X). 7538989

- The OpenGL ES Performance Detective identifies graphics bottlenecks in your iOS applications. It is located in `<Xcode>/Applications/Graphics Tools`. 8208239
- Runs of the OpenGL ES Analyzer instrument can be saved in Instruments traces. 7993423
- The OpenGL ES Analyzer instrument supports extended filtering of the OpenGL ES trace. 7976717
- The OpenGL ES Analyzer instrument provides single-frame navigation, which allows you to focus all instruments on a specific OpenGL frame, and to step backward and forward in the trace frame by frame. 8552970

- You can access the values of the build settings of the target being built through environment variables and launch arguments. When you create custom executables (by changing the value of the Executable setting in Run and Profile scheme actions), you can specify the target against which to expand the environment variables and launch arguments. 7546808

- Xcode suggests key path completions in the bindings inspector as you type. To take advantage of this feature, specify the class of object being managed by your controller in the attributes inspector.

  Xcode uses the project’s symbol index to generate the key path completions. 8176168

- There’s an additional gesture to jump to a symbol definition in the source editor: holding down the Command key. When you hold down Command, Xcode represents the symbol under the pointer as a hyperlink; you can move the pointer between symbols until Xcode highlights the one you want to act on. You can then click the symbol to jump to its definition. Other modifies keys behave as expected. 8459719

- The activity viewer presents more detailed information about scheme-related tasks, such as building a product. 7982481

- Hidden views are invisible in the Interface Builder canvas (they used to be partially visible in Interface Builder 3, part of Xcode 3).

  To work with these views, select them in the jump bar or the outline view. 8059339

- The `xcodebuild -activetarget` option is no longer supported. 8361726

- In General preferences, you can specify that Xcode ask you where to open a file you click or double-click while holding down an modifier key in a navigator. 8476034
- Xcode automatically creates schemes for all targets in a project when you open an Xcode 3.x–based project. It doesn’t skip targets that other targets depend on.

  You can delete or hide schemes you don’t need in the manage schemes dialog. 8016676
- Setting General preferences > Build Location > “Shared subfolder” to an absolute path doesn’t generate an assertion failure when opening projects. 8368913

- Many performance problems with making connections are resolved. In particular, the performance of connecting to the First Responder has been drastically improved. 8280101
- You can create an Interface Builder–to–source connection even the target source code is folded. 8472539

- When you create `NSManagedObject` subclasses from entities in a Core Data data model, Xcode ask for confirmation before overwriting existing files. 8506607

- Breakpoints and message bubbles appear in the source editor even when code is folded above them. 7192871

- __C++:__ Several bugs related to using blocks are fixed. 6182276

- API statistics in the OpenGL ES Analyzer instrument are computed correctly. 8549379

- The list of help topics in a help book appears, as expected, when accessing help books in the documentation organizer. 8430699

- After you create a branch and switch to it in the repositories organizer, using the commit dialog or the version editor causes an assertion failure.

  Restart Xcode after creating a branch and switching to it. 8383245

- Interface Builder files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the Interface Builder file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406
- The task log viewer is empty when you select the last build task of a project or workspace in the log navigator and the viewer is set to show only recent operations.

  Set the task log viewer to show all operations. 8350930

- Xcode cannot edit OS X–type Interface Builder documents comprised of objects from frameworks other than AppKit.

  You can compile and run these documents, however. 7470836
- __Refactoring:__ Xcode does not refactor Cocoa bindings. 8423815

- __Search navigator:__ Xcode may crash in the replace preview dialog of the search navigator when all the found instances are selected and you click Replace. 8091532

- Xcode does not create a snapshot of your workspace before performing a refactoring transformation.

  Create manual snapshots before performing refactoring transformations. 7816256
- __Editing nib files:__ The Rename transformation may not work properly action methods in Interface Builder documents when the action’s target is the first responder or the method is declared in a category, protocol, or a superclass of the given class. 8500272

- Xcode doesn’t recognize SCP-based URLs for Git repositories in the Repositories organizer.

  Use the SSH-based URLs. For example, instead of `git@example.com:/myrepositoryname.git` use `ssh://git@example.com/myrepositoryname.git`. 8044145

- Xcode doesn’t use a new build location after you change General preferences > Build Location.

  Close and reopen open projects and workspaces after changing the build location. 7965261

- These help books are not listed on the Xcode Application Help page (Help > Xcode Application Help): _Interface Builder Help_, _Task and Session Log Viewer Help_, _Symbol Navigator Help_, and _Xcode Concepts_.

  Search for these titles in the Help menu or in the search navigator in the documentation organizer. 8481951,8518802

- There is no distinction between “launch” schemes and “distribution” schemes. All schemes are capable of launching and archiving a product. 8429398
- The project navigator identifies read-only files with a lock icon. Click the lock to unlock the file. Xcode can unlock files with no “write” permission and files locked from the Finder. You can also invoke a custom script to unlock files through the “Unlocking file” alert in Alerts preferences. 8135771

- You can preview the files modified in a snapshot before restoring it using the version editor. 7494111
- When using Git as as your source control repository, you can discard changes to project packages (`.xcodeproj` files) through the Source Control item in the project navigator’s shortcut menu. 7480525
- Xcode offers to place new projects under source control in a local Git repository in the project directory. 8407608

- You can access Quick Help for a suggested completion from the code completion list. To display Quick Help for the selected suggestion, click the question mark icon on the suggestion or choose Help > Quick Help. 8172782

- __Objective-C:__ Adds support for instance variables in class implementations and class extensions (iOS and 64-bit OS X).
- __Objective-C:__ Adds default automatic synthesis of properties (iOS and 64-bit OS X). You don’t need the `@synthesize` directive in the implementation sections for the compiler to synthesize accessors for declared properties.

  However, to access such properties in `dealloc` and `finalize` methods, you must use the dot notation; for example: `self.property`. 7885001

- When inserting an outlet or action with Connect to Source Code, Xcode adds the counterparts for the connection:

  For actions:

  - When dragging to a header file: Xcode adds the implementation and interface.
  - When dragging to an implementation file: Xcode adds the implementation.

  For outlets:

  - When dragging to a header file to insert a property outlet: Xcode adds the instance variable declaration, the `@synthesize` directive, and the `release` call in the `dealloc` method.
  - When dragging to a header file to insert an instance variable outlet, Xcode adds the instance variable declaration, and the `release` call in the `dealloc` method. 8082047

- Xcode shows a preview of the suggested completion in the code completion list. To accept the entire completion, press Return. To accept only the highlighted part of the completion (identified with a dotted underline), press Tab. 8321987

- You can refactor Interface Builder and Core Data model files. 7474053
- After selecting an entire word in the source editor, Xcode was not always able to perform refactoring transformations. 8349889
- You can perform refactoring transformations on key-value coding and Core Data methods. 8224495
- You can rename classes, protocols, and other top-level constructs only when the new name is not in use by another construct of the same type. 8313803
- Xcode notifies you of refactoring errors and warnings in the workspace window. 8128957

- Catching exceptions in optimized fragile-ABI Objective-C code no longer resets modifications to local variables. 8160285
- Eliminated crash in Objective-C exception rethrow. 8144203
- Fixed bugs in blocks in C++ and Objective-C++ code.

- Interface Builder files with explicit Xcode 3 file types open in the source editor instead of in Interface Builder.

  Set the file type of the Interface Builder file in the Identity and Type inspector to “Default,” deselect it in the project navigator, and select it again. 8028406
- Absolute paths in General preferences > Build Location > “Shared subfolder” generate an assertion failure when opening projects.

  Specify a relative path for “Shared subfolder” in General preferences, or set Build Location to the recommended value. 8368913
- The task log viewer is empty when you select the last build task of a project or workspace in the log navigator and the viewer is set to show only recent operations.

  Set the task log viewer to show all operations. 8350930
- The Extract transformation is not supported. 7711619

- __Search navigator:__ Xcode may crash in the replace preview dialog of the search navigator when all the found instances are selected and you click Replace. 8091532

- When you create `NSManagedObject` subclasses from entities in a Core Data data model, Xcode overwrites existing files without a confirmation dialog. 8506607

- __Refactoring:__ Xcode does not refactor Cocoa bindings. 8423815
- Xcode cannot edit OS X–type Interface Builder documents comprised of objects from frameworks other than AppKit.

  You can compile and run these documents, however. 7470836
- Hidden views are invisible in the Interface Builder canvas.

  To work with these views, select them in the jump bar or the outline view. 8059339

- Xcode does not create a snapshot of your workspace before performing a refactoring transformation.

  Create manual snapshots before performing refactoring transformations. 7816256
- __Editing nib files:__ The Rename transformation may not work properly action methods in Interface Builder documents when the action’s target is the first responder or the method is declared in a category, protocol, or a superclass of the given class. 8500272

- Xcode doesn’t use a new build location after you change General preferences > Build Location.

  Close and reopen open projects and workspaces after changing the build location. 7965261

- Xcode doesn’t recognize SCP-based URLs for Git repositories in the Repositories organizer.

  Use the SSH-based URLs. For example, instead of `git@example.com:/myrepositoryname.git` use `ssh://git@example.com/myrepositoryname.git`. 8044145

- These help books are not listed on the Xcode Application Help page (Help > Xcode Application Help): _Interface Builder Help_, _Task and Session Log Viewer Help_, _Symbol Navigator Help_, and _Xcode Concepts_.

  Search for these titles in the Help menu or in the search navigator in the documentation organizer. 8481951,8518802
- The list of help topics in a help book doesn’t appear when accessing help books in the documentation organizer, instead the book’s first help topic appears.

  Use the jump bar to navigate to the other help topics in the book. 8430699

Xcode 4 developer preview 3 requires OS X v10.6.4. It does not install or run on earlier versions of OS X.

Xcode supports universal development for iOS 4.1 and 3.2 and OS X v10.5 and later. It does not support development for iOS 3.1 or earlier or OS X v10.4 or earlier.

Xcode 4 developer preview 3 is installed by default into the `/Xcode4` directory and does not conflict with an existing installation of Xcode 3.2.

The installer optionally installs Unix tools into `/usr`, so conventional makefile-based and config-based builds operate correctly. Use the `xcode-select` command-line utility to set the default toolset for command-line builds. If you choose this option when installing Xcode 4, Xcode 4 Unix tools replace the Xcode 3.2 Unix tools in `/usr`. This does not effect the functionality of any Xcode 3.2 installations.

Xcode 4 reads and builds projects created in Xcode 2.1 through 3.2.3. Projects created and edited with Xcode 4 can be opened and built on Xcode 3.2 through 3.2.3.

Apple offers a number of resources where you can get Xcode development support:

- [http://developer.apple.com](https://developer.apple.com/): The Apple Developer website is the best source for up-to-date technical documentation on iOS and OS X.
- [http://developer.apple.com/technologies/tools/](https://developer.apple.com/technologies/tools/): The Xcode home page on the Apple Developer website provides information on the developer tools.
- [https://forums.developer.apple.com/](https://forums.developer.apple.com/): The Apple Developer Forums feature a dedicated Developer Forum for Xcode 4 Developer Previews.

Use [http://bugreport.apple.com](http://bugreport.apple.com/) to communicate issues with Apple. Include detailed information of the issue, including the system and developer tools version information, and any relevant crash logs or console messages.

To send comments or feedback on the Xcode Tools suite to Apple, use [xcode-feedback@group.apple.com](mailto:xcode-feedback@group.apple.com).

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

Xcode 4 developer preview 3 is pre-release software. File bugs at [http://bugreport.apple.com](http://bugreport.apple.com/) for performance and stability issues, data loss or file corruption, missing or unimplemented features, behavioral or aesthetic issues, and feature and enhancement requests. Provide as much context as possible, especially crash logs or samples, detailed Steps to Reproduce, and projects or workspaces when possible.

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

**__Support for editing accessibility values for iOS objects__  (7986412)**
: The IB editor now supports editing accessibility values for iOS objects.

**__Navigator filter results don't update as the items to filter changed__ (7722840)**
: Filtering in navigators now produces live results. For example, when filtering the contents of the Project navigator by SCM status, the list of items updates as the SCM status of individual files changes.

**__Workspace window and tab state lost if Xcode is force quit or quits unexpectedly.__  (7773437)**
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

Xcode 4 Developer Preview 2 requires OS X v10.6.4. It does not install or run on earlier versions of OS X.

Xcode supports universal development for iOS 4 and 3.2 and OS X v10.5 and later. It does not support development for iOS 3.1 or earlier or OS X v10.4 or earlier.

Xcode 4 Developer Preview 2 is installed by default into the `/Xcode4` directory and does not conflict with an existing installation of Xcode 3.2.

The installer optionally installs Unix tools into `/usr`, so conventional makefile-based and config-based builds operate correctly. Use the `xcode-select` command-line utility to set the default toolset for command-line builds. If you choose this option when installing Xcode 4, Xcode 4 Unix tools replace the Xcode 3.2 Unix tools in `/usr`. This does not effect the functionality of any Xcode 3.2 installations.

Xcode 4 reads and builds projects created in Xcode 2.1 through 3.2.3. Projects created with Xcode 4 can be opened and built on Xcode 3.2 through 3.2.3.

Opening and building a project in Xcode 4 does not upgrade or alter it. Changes you make to a project in Xcode 4 are compatible with earlier versions of Xcode.

Apple offers a number of resources where you can get Xcode development support:

- [http://developer.apple.com](https://developer.apple.com/): The Apple Developer website is the best source for up-to-date technical documentation on iOS and OS X.
- [http://developer.apple.com/technologies/tools/](https://developer.apple.com/technologies/tools/): The Xcode home page on the Apple Developer website provides information on the developer tools.
- [https://forums.developer.apple.com/](https://forums.developer.apple.com/): The Apple Developer Forums feature a dedicated Developer Forum for Xcode 4 Developer Previews.

Use [http://bugreport.apple.com](http://bugreport.apple.com/) to communicate issues with Apple. Include detailed information of the issue, including the system and developer tools version information, and any relevant crash logs or console messages.

To send comments or feedback on the Xcode Tools suite to Apple, use [xcode-feedback@group.apple.com](mailto:xcode-feedback@group.apple.com).

Xcode 4 Developer Preview is pre-release software. File bugs at [http://bugreport.apple.com](http://bugreport.apple.com/) for performance and stability issues, data loss or file corruption, missing or unimplemented features, behavioral or aesthetic issues, and feature and enhancement requests. Provide as much context as possible, especially crash logs or samples, detailed Steps to Reproduce, and projects or workspaces when possible.

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

Xcode 4 is a major version of the Xcode toolset. It requires OS X v10.6.3 and does not run on previous versions of OS X.

- _Supported Configurations_

  Xcode 4 runs on OS X v10.6.3. It does not install or run on earlier versions of OS X. Xcode supports universal development for iPhone OS 4 and 3.2 and OS X v10.4 and later. It does not support development for OS X v10.3 or earlier or iPhone OS 3.1 or earlier.
- _Xcode Installation_

  Xcode 4 Developer Preview is installed by default into the `/Xcode4` directory and does not conflict with an existing installation of Xcode 3.2.

  The installer optionally installs Unix tools into `/usr`, so conventional makefile-based and config-based builds operate correctly. Use the `xcode-select` command-line utility to set the default toolset for command-line builds. If you choose this option when installing Xcode 4, Xcode 4 Unix tools replace the Xcode 3.2 Unix tools in `/usr`. This does not effect the functionality of any Xcode 3.2 installations.
- _Project File Format Compatibility and Versioning_

  Xcode 4 reads and builds projects created in Xcode 2.1 through 3.2.3. Projects created with Xcode 4 can be opened and built on Xcode 3.2 through 3.2.3.

  Opening and building a project in Xcode 4 does not upgrade or alter it. Changes you make to a project in Xcode 4 are compatible with earlier versions of Xcode.

  User-specific project information for Xcode 4 is stored in new files in the `.xcodeproj` project wrapper. Xcode 4 ignores and rarely alters the information in Xcode 3.2’s per-user `.pbxuser` files.
- _User Preferences from Xcode 3.2_

  For the most part, Xcode 4 neither migrates nor interferes with your user settings from Xcode 3.2, with some exceptions.

  General, Code Sense, Building, Distributed Builds, Debugging, Key Bindings, File Types, Source Trees, and Documentation preferences from Xcode 3.3 are ignored; similar Xcode 4 functionality starts with Xcode 4 defaults. Changing settings in Xcode 4 does not affect your continued use of Xcode 3.2.

  Text Editing, Fonts and Colors, Indentation, and SCM preferences are copied from Xcode 3.2 preferences. Changes made to these preferences with Xcode 4 are not copied back to Xcode 3.2.

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

  The `lldb` debugger is new in Xcode 4 and is still under development. While it offers basic functionality in this Developer Preview, it is not fully featured. See the LLVM project page at [http://lldb.llvm.org](http://lldb.llvm.org/) for more information on `lldb`.
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

Xcode 4 Developer Preview is pre-release software. Please file bugs at [http://bugreport.apple.com](http://bugreport.apple.com/) for performance and stability issues, data loss or file corruption, missing or unimplemented features, behavioral or aesthetic issues, and feature and enhancement requests. Provide as much context as possible, especially crash logs or samples, detailed Steps to Reproduce, and projects or workspaces when possible.

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

[Next](Document%20Revision%20History.md)

