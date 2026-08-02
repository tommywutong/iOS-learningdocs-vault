---
title: Xcode Release Notes — Archive
apple_id: TP40016994
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/RN-Xcode-Archive/Chapters/xc6_release_notes.html
archived_at: '2026-07-26T19:54:16.450944Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Release Notes — Archive](Xcode%20Release%20Notes%20%E2%80%94%20Archive.md)


[Next](Xcode%205%20Release%20Notes.md)[Previous](Xcode%207%20Release%20Notes.md)

# Xcode 6 Release Notes

## Xcode 6.4 Release Notes

### New Features

- Xcode 6.4 includes the iOS 8.4 SDK to support development for iOS 8.4 apps.

### Known Issues

#### Instruments

- Shortly after the first build and run cycle in Xcode, Instruments may disable profiling, indicate that an iOS device is offline, and offer to open Xcode to enable the device for development.

  Quit Instruments, open Xcode, choose Window > Devices, and select the iOS device. If any tasks are listed as in progress, wait for them to complete and close the Devices window. Build and run the app from Xcode, then click Stop. Wait approximately one minute, then press Command-I to launch Instruments. The device should no longer appear offline and profiling should be enabled. (21412937)

## Xcode 6.3.2 Release Notes

### Swift Compiler

- Swift projects now compile quickly, fixing a speed regression in Xcode 6.3.1.

  In Xcode 6.3.1, the Swift “Merge” compile phase could appear to hang for some targets. You no longer need to enable Whole Module Optimization in order to avoid this issue. (20638611)

## Xcode 6.3.1 Release Notes

### Resolved Issues

#### Swift

- Using Open Quickly, symbols from SDKs are available in projects and workspaces that use Swift. (20349540)

#### Playgrounds

- Playgrounds with an invalid target platform value do not crash Xcode. (20327968)
- Immediately selecting Undo upon opening a Playground does not set an invalid target platform value. (20327880)

#### Interface Builder

- Using custom fonts in Storyboard and xib files does not cause Xcode to hang. (20476377)
- When auto-layout is disabled, `NSTextView` nib restoration works correctly. (20523924)

#### Debugger

- The Xcode debugger variables view does not omit values for the current frame when the current function comes from a Swift framework. (20380047)

#### Testing

- Swift tests are automatically discovered by Xcode. (20373533)

#### General

- Archiving a project or workspace that is not under source control but that contains contents under source control does not crash Xcode. (20521089)
- The Command Line Tools product includes the `__debug` header. (20523314)
- Localized files can be renamed. (20490808)
- Devices previously listed as "ineligible for running” erroneously are listed correctly. (20121178)

## Xcode 6.3 Release Notes

### New Features

#### Crashes Organizer for App Store and TestFlight Users

Xcode 6.3 includes a new feature to help opted-in App Store users and TestFlight users collect and analyze crash log data for your apps.

Crash reports gathered from opted-in App Store users and TestFlight users can be displayed in the Crashes Organizer:

- To view crash reports for your apps, first enter your developer accounts in Xcode Preferences “Accounts” pane. Crash reports for the iOS apps associated with your developer accounts are displayed in the Xcode Organizer window.
- Crash reports are only available for apps that were uploaded to iTunes Connect with symbol information.
- Xcode provides a list of the top crashes for each of your apps.
- The crash reports are fully symbolicated and aggregated on Apple's servers.
- Xcode provides workflows for managing your crash reports and viewing backtraces directly beside your project’s source code.

For more information, see Crashes Organizer Help in the Xcode documentation. (14995491)

#### Xcode Playground

Playgrounds have been enhanced with documentation authoring using inline marked-up comments, inline playground results, the ability to view and edit resources embedded in playgrounds, and the ability to integrate auxiliary source files into Playgrounds. These features enable the creation of rich new experiences in playgrounds.

These enhancements are detailed in the [Playground Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknltcmi) section below.

#### Swift 1.2

Xcode 6.3 includes a new version of the Swift language, Swift 1.2, with significant changes, fixes, and enhancements. See the following sections of these release notes for details:

- [Swift Language Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknltg)
- [Swift Language Fixes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknlto)
- [Swift Language Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknltm)
- [Swift Performance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknlti)
- [Swift Standard Library Enhancements and Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknltk)

#### Swift Migrator from Swift 1.1 to Swift 1.2

A source migrator tool has been provided to help update your Swift source code from Swift 1.1 (Xcode 6.2) to Swift 1.2 (Xcode 6.3.)

In Xcode, select `Edit > Convert > To Latest Swift Syntax`.

#### Objective-C

Objective-C code has been enhanced to improve interoperability between Swift and Objective-C code. For detailed information, see the [Objective-C Language Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknlts) section in these release notes.

#### Debugger

LLDB has been enhanced to improve the support for modules in C-based languages as well as provide overall improvements in Swift debugging support. For more details, see the [Debugger Enhancements](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknltcma) section.

#### Apple LLVM Compiler Version 6.1

The Apple LLVM compiler has been updated to version 6.1.0.

This updated compiler includes full support for the C++14 language standard, a wide range of enhanced warning diagnostics, and new optimizations. Support for the arm64 architecture has been significantly revised to better align with the ARM implementation; the most visible impact is that several vector intrinsics have changed to more closely match the ARM specifications.

#### ARM64 Intrinsics

The argument ordering for the arm64 vfma/vfms lane intrinsics has changed. This change is being introduced in stages to reduce risk.

__Important:__ See "[ARM64 Intrinsics Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknltcmq)" for details.

#### Force Touch

Xcode 6.3 supports Force Touch trackpad gestures for Macs that include it, and supports configuring Force Touch trackpad functionality in Interface Builder for `NSButton` and `NSSegmentedControl`.

__Note:__ Adopting Force Touch in Interface Builder requires running Xcode on OS X Yosemite version 10.10.3.

(16140561, 16140600, 18660545)

### Changes, Enhancements, and Notes

#### Swift Language Changes

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

#### Swift Language Fixes

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

#### Swift Language Enhancements

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

  ```
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

  ```swift
  @objc
  enum Bear: Int {
     case Black, Grizzly, Polar
  }
  ```

  imports into Objective-C as:

  ```c
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
  println([Float].self)       // prints "Swift.Array&lt;Swift.Float&gt;”
  println((Int, String).self) // prints "(Swift.Int, Swift.String)"
  ```

  (18947381)
- A new `@noescape` attribute may be used on closure parameters to functions. This indicates that the parameter is only ever called (or passed as an `@noescape` parameter in a call), which means that it cannot outlive the lifetime of the call. This enables some minor performance optimizations, but more importantly disables the “`self.`” requirement in closure arguments. This enables control-flow-like functions to be more transparent about their behavior. In a future beta, the standard library will adopt this attribute in functions like `autoreleasepool()`.

  ```
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

#### Swift Performance

- A new compilation mode has been introduced for Swift called Whole Module Optimization. This option optimizes all of the files in a target together and enables better performance (at the cost of increased compile time). The new flag can be enabled in Xcode using the “`Whole Module Optimization`” build setting or by using the `swiftc` command line tool with the flag `-whole-module-optimization`. (18603795)

#### Swift Standard Library Enhancements and Changes

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

#### Objective-C Language Enhancements

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

  ```
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

#### Playground Enhancements

- Playgrounds now offer an easy way to create and edit rich documentation using marked-up text. Use the new `//:` or `/*: */` style comments to indicate when text should be shown as a rich comment. Change the viewing mode of a playground by using the “`Show Documentation as Rich Text`” and “`Show Documentation as Raw Text`” commands in the Editor menu.

  For more information, see _[Playground Reference](https://developer.apple.com/library/archive/documentation/Swift/Reference/Playground_Ref/Chapters/XCPlayground.html#//apple_ref/doc/uid/TP40014789)_ in the Xcode documentation. (19265300)
- Playground results are now shown inline, rather than in the timeline view. When there are multiple results on a line, you can toggle between viewing a single result and a listing of all the results. For result sets that are numbers, there is the added option of viewing as a graph. Results can be resized to show more or less information.

  For more information, see Playground Help in the Xcode documentation. (19259877)
- Playground scrolling and performance has been improved.
- Playgrounds can now be upgraded to the new format by selecting the `Editor > Upgrade Playground` menu item.

  __Note:__ The rich comments and supporting source files features are only supported in playgrounds created with Xcode 6.3 or later.

  (19938996)
- Playgrounds now expose their structure in the project navigator. To show the project navigator, select `View > Navigators > Show Project Navigator`. This allows you to use resources (for instance, images) from within your playground: twist open the playground to see the Resources folder and drag them in. (19115173)
- Playgrounds now let you provide auxiliary support source files, which are compiled into a module and automatically imported into your playground. To use the new supporting source files feature, twist open the playground in the project navigator to see the new Sources folder, which has a single file named `SupportCode.swift` by default. Add code to that file, or create new source files in this folder, which will all be automatically compiled into a module and automatically imported into your playground. (19460887)

#### Debugger Enhancements

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

  __Note:__ In several cases, not having a proper function prototype could lead to unexpected failures.

  (18782288)
- Evaluating Swift expressions performance is improved especially when debugging code running on devices.

  This will be most noticeable in the Swift `REPL` and when issuing LLDB commands such as `p`, `po`, and `expression`. (19213054)
- Significant improvements in LLDB’s Swift support have addressed many known issues with the Swift debugging experience. (19656017)

#### ARM64 Intrinsics Changes

The argument ordering for the arm64 vfma/vfms lane intrinsics has changed.

The change may not trigger compile-time errors but it will break code at runtime. To reduce risk, the transition to the new ordering is being completed in stages:

- By default, the compiler now warns about any use of the intrinsics but will retain the old behavior.
- As soon as possible, adopt the new behavior and define the `USE_CORRECT_VFMA_INTRINSICS` macro with value `1`.
- If you define the `USE_CORRECT_VFMA_INTRINSICS` macro value with value `0`, that silences the warnings and keeps the old behavior. However, do not leave your code in that state for long: support for the old behavior will be removed in a future release.

(17964959)

### Resolved Issues

These issues, previously reported in prior releases of Xcode, have been resolved in Xcode 6.3.

#### iOS Simulator

- Apps containing a Watch extension may not deploy to the iOS Simulator for iOS versions earlier than 8.2. (20032374)
- Audio playback using `AudioServicesPlaySystemSound` does not function as expected in the iOS 8.1 and 8.2 simulator runtimes. (17911598)

#### General

- Xcode does not show a Watch as paired to its companion iPhone if the iPhone was rebooted and then connected to the host Mac without first being unlocked. (19864431)
- Sharing a scheme in an Apple Watch app project prevents the iOS and Apple Watch App schemes from being created. (18941832)
- App Store import will fail for Apple Watch apps that do not have the same version information as the containing app. (17812309)
- Xcode does not show a Watch as paired to its companion iPhone if the iPhone was rebooted and then connected to the host Mac without first being unlocked. (19864431)
- If the deployment target of an app containing an Apple Watch extension is configured for earlier than iOS 8.2, deployment of the app to devices running iOS 8.1.x or earlier may fail. (20032374)

### Known Issues

#### Swift

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
  - Otherwise, use a dummy parameter with a default value, for example: `_ nonobjc: () = ()`.

  (19826275)
- Overrides of methods exposed to Objective-C in private subclasses are not inferred to be `@objc`, causing the Swift compiler to crash.

  Explicitly add the `@objc` attribute to any such overriding methods. (19935352)
- Symbols from SDKs are not available when using Open Quickly in a project or workspace that uses Swift. (20349540)

#### Playgrounds

- Switching between `Raw Source` and `Rich Text` in a playground may cause the timeline to disappear.

  You can show the timeline by selecting it from the Assistant editor popup menu. (20091907)
- Opening a playground and immediately selecting `Undo` can set an invalid target platform.

  Either redo, select a valid platform, or, if you have already closed the document, edit the playground’s `contents.xcplayground` file to ensure that either `osx` or `ios` is specified for the `target-platform` property. (20327880)
- Xcode crashes if a playground has an invalid value target platform.

  Edit the playground’s `contents.xcplayground` file to ensure that either `osx` or `ios` is specified for the `target-platform` property. (20327968)

#### iOS Simulator

- When launching a WatchKit app on the iOS Simulator, the Watch Simulator may not automatically launch.

  Launch the Watch Simulator before launching the WatchKit app on the iOS Simulator. (19830540)
- Localization settings made in a target's scheme (as well as other settings made on the command line) will not be honored on launch in the iOS Simulator with iOS 8 runtimes.

  Choose the desired language in the Settings app. (19490124)

#### Debugger

- When using the debugger, the variables view may omit values for the current frame if the current function comes from a Swift framework.

  Add `-Xfrontend -serialize-debugging-options` to the `Other Swift Options` build setting for the framework. (20380047)

#### Testing

- Swift tests are not automatically discovered in this release of Xcode. Test annotations in the source editor sidebar will not appear, and the test navigator and the table of tests in the Test action of the scheme sheet will be empty.

  You can run Swift tests by selecting `Product > Test`. Once tests have been run, they appear in the test navigator and the scheme sheet. The following limitations apply:

  - Tests discovered through execution in this manner provide limited interaction in the test navigator. For example, Run buttons do not appear and clicking on a test in the navigator does not jump to the source code except in the case of a test error.
  - Run buttons and test success/fail indicators will not appear in the source editor.

  (20373533)

#### General

- iOS extensions may need to be manually enabled before you can debug them. (18603937)
- The Xcode menu command `Simulator Background Fetch` does not work.

  Use the menu command in iOS Simulator instead. (20145602)
- Attached devices running earlier versions of iOS might show up as ineligible in the run destinations menu.

  To correct this problem, reconnect the devices one at a time. (20320586)

## Xcode 6.2 Release Notes

### New Features

#### WatchKit Framework

Xcode 6.2 adds support for iOS 8.2, including developing Apple Watch apps with the new WatchKit framework. Tools support for WatchKit includes:

- Design tools for building Apple Watch interfaces, glances, and notifications
- Debugging and profiling support
- Apple Watch support in iOS Simulator for testing apps, glances, and notifications

### Known Issues

#### Interface Builder

- Interface Builder sometimes fails to render a subclass of a designable class on the canvas, or fails to show inspectable properties inherited from a superclass.

  Add `IB_DESIGNABLE` or `@IBDesignable` to the subclass declaration. (19512849)

#### Asset Catalog

- When creating a new Apple Watch app target, the newly created asset catalog includes an "Unassigned" slot in the catalog's app icon.

  Select the "Unassigned" slot and delete it using the Delete key. (19978639)
- The long-look slot in an Apple Watch app asset catalog for 38mm devices is labeled incorrectly. The label reads:

  - `Apple Watch - Home Screen (All) - Long Look (42 mm) - 40pt`

  It should read:

  - `Apple Watch - Home Screen - Long Look (38 mm) - 40pt`

  This slot works correctly for 38 mm device icons.

  The long-look slot for 42 mm devices is labeled: `Apple Watch - Long Look - 44pt`. (19978648)

#### iOS Simulator

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

#### Instruments

- The UI Automation Instrument is not supported for WatchKit apps. (19152139)

#### Debugging

- When stopped at a breakpoint in an Apple Watch app, tapping `Stop` doesn't stop the running app.

  Tap `Stop` twice. (18991746)

#### General

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

### Notes

__Important:__ Xcode 6.2 is the last release of Xcode that supports running on OS X Mavericks. (18673392)

## Xcode 6.1.1 Release Notes

### Resolved Issues

#### Swift Language

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

#### Interface Builder

- Fixed an issue where Interface Builder could not open or compile IB documents that have an image name containing a slash (‘`/`') character on Yosemite. This manifested as a range exception on `NSTaggedPointerString` when calling `+[NSImage imageNamed:]`. (18752260)

#### Xcode Server

- Fixed an issue where choosing a new build of Xcode after configuring Xcode Server could cause permissions problems. (18819339)
- Fixed a crash in Xcode Server when the private portal keychain is replaced with a symlink to the system keychain. (18854423)
- Fixed an issue with startup when using a password policy. (18819348)
- Fixed an issue checking out sources in Xcode Server when connecting over SSH. (18819357)

### Known Issues

#### Debugger

- Data structures containing bitfields may display incorrectly in the debugger when referenced from Swift code. (17967427)

#### Asset Catalogs

- If your project’s only assets are in an asset catalog, the build may fail with an error similar to: '`.../Contents/Resources` does not exist.’

  Add at least one non-asset catalog resource to your project. (17848595)

#### iOS Simulator

- The iOS Simulator will sometimes loose network connectivity when the host’s network configuration changes.

  Restart the simulated device to regain network connectivity. (17867038)
- When playing a video to the external display in the iOS Simulator, external display may be all black.

  Change the resolution of the external display while the video is playing and then change it back to the desired resolution. (17933514)
- After you install iOS 7.1 Simulator using the Downloads panel in Xcode Preferences, the iOS 7.1 simulator’s devices may not be available in the run destination menu.

  Log out and then log in again, or restart your computer. (19011252)

## Xcode 6.1 Release Notes

### New Features

#### Swift Language

- Xcode 6.1 includes Swift 1.1. (18238390)
- A large number of AppKit APIs have been audited for optional conformance in addition to WebKit, Foundation, UIKit, CoreData, SceneKit, SpriteKit, and Metal APIs. As a result, a significant number of implicitly unwrapped optionals have been removed from their interfaces. These changes clarify the nullability of properties, arguments, and return values in the APIs. The audit effort is ongoing.

  The API changes replace `T!` with either `T?` or `T` depending on whether or not the value can be `null`, respectively.  If you find a case that is incorrect, file a bug at [http://bugreport.apple.com](http://bugreport.apple.com) and include the tag “_#IUO_” in the subject line.

  If you encounter a method, property, or initializer for which the return value is incorrectly considered non-nullable, you can work around the problem by wrapping the result in an optional:

  ```
  var fooOpt: NSFoo? = object.reallyMightReturnNil()
  if let foo = fooOpt {...}
  ```

  Be sure to file a bug about these cases.

  __Note:__ Do not file bugs about APIs that are still marked as `T!`; we already know about them.
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

  ```swift
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

#### Playgrounds

- iOS Playgrounds now support displaying animated views with the `XCPShowView()` `XCPlayground` API. This capability is disabled by default; it can be enabled by checking the "Run in Full Simulator" setting in the Playground Settings inspector.

  When the capability is enabled, running the playground causes the iOS Simulator application to launch and run the playground in the full simulator. This capability is also required for other functionality that fails without the full simulator, such as `NSURLConnection` http requests. Running in the full iOS Simulator is slower than running in the default mode. (18282806)

#### Testing

- Dead code stripping no longer removes public declarations that are needed to run tests from Swift application targets. (18173029)

### Resolved Issues

#### Playgrounds

- A weakly-linked symbol in a playground no longer causes a compilation error. (18000684)
- Using `NSView` subclasses in OS X playgrounds no longer results in execution failure. (18449054)

#### Source Editor

- Addressed an issue that could cause Xcode to become unresponsive while editing Swift code.

#### Debugging

- Swift expressions like '`expr`', '`p`', and '`print`' that are evaluated from the LLDB prompt in the debugger console will now work on 32-bit iOS devices. (18249931)

#### REPL

- In the Swift REPL, attempts to inspect instances of classes defined in the REPL now produce properly formed data for stored properties. (18457336)

#### Xcode Server

- Configuring Xcode Server on a system that had a pre-GM build of Xcode 6 now works. (18314522)

#### iOS Simulator

- Settings changed in the Settings app on iOS Simulator now persist as expected. (18238018)
- Deleting an app from iOS Simulator now deletes user defaults as expected. (18307910)

### Known Issues

#### Templates

- Users upgrading Xcode, iOS Simulator, and documentation downloads from Xcode 5.1.1 to Xcode 6.1 may receive the error, “The digest is missing,” when building and running a master detail app on a device.

  Unplug the device and plug it back in. (18464963)

#### Interface Builder

- By default, NSTableViews and NSOutlineViews have a white background, which may be incorrect when the control is shown with a dark appearance.

  To dynamically support both light and dark appearances, change the background of an `NSTableView` or `NSOutlineView` from “Default” to “Control Background Color”. (18075907)

#### iOS Simulator

- Simulated devices can get stuck in a “Creating” state in some circumstances. This problem can occur either when creating new devices or when resetting existing devices after having renamed `Xcode.app`.

  If this this problem occurs, reboot your system and reset the device from the command line by running `xcrun simctl erase <Device UDID>`. You can obtain the UDID of the device by checking the output of `xcrun simctl list`. (17042870)
- Localization and Keyboard settings, including 3rd party keyboards, are not correctly honored by Safari, Maps, and developer apps in the iOS 8.1 Simulator. `[NSLocale currentLocale]` returns `en_US` and only the English and Emoji keyboards are available. (18418630, 18512161)
- If an app is weak linked against frameworks new in iOS 8 SDK and OS X 10.10 SDK, it may fail to run if the run destination is an iOS Simulator for older iOS runtimes and the host system is running OS X Yosemite. (17807439)
- iOS Simulator does not support the use of network proxy servers that require authentication. (14889876)

#### App Extensions

- Debugging Today app extensions is not reliable after the first debug session.

  Dismiss Notification Center before starting the next debug session. (18051136)

## Xcode 6.0.1 Release Notes

### Resolved Issues

#### App Submission

- App Store submission issues encountered with the Xcode 6.0 GM seed have been resolved. (18444000)

## Xcode 6.0 Release Notes

### New Features

#### Swift Language

Swift is a new object-oriented programming language for iOS development. Swift is modern, powerful, expressive, and easy to use.

__Note:__ Swift development for OS X requires the OS X version 10.10 SDK, available in beta at the time of this release. For more information, see [Swift Support for OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dsojufvbuqnbnknltcmjq).

- Access all of the Cocoa Touch frameworks with Swift.
- Swift code is compiled and optimized by the advanced LLVM compiler to create high-performance apps.
- Swift provides increased type safety with type inference, restricts direct access to pointers, and automatically manages memory using ARC to make it easy for you to use Swift and create secure, stable software. Other features related to language safety include mandatory variable initialization, automatic bounds checking to prevent overflows, conditionals that break by default, and elimination of pointers to direct memory by default.
- Write, debug, and maintain less code, with an easy to write and read syntax and no headers to maintain.
- Swift includes optionals, generics, closures, tuples, and other modern language features. Inspired by and improving upon Objective-C, Swift code feels natural to read and write.
- Use Swift interactively to experiment with your ideas and see instant results.
- Swift is a complete replacement for both the C and Objective-C languages. Swift provides full object-oriented features, and includes low-level language primitives such as types, flow control, and operators.

#### Xcode 6 Features supporting Swift

- Playgrounds are an interactive development environment allowing you to experiment with Swift for prototyping, testing ideas, and so forth. Some uses for playgrounds include:

  - Designing a new algorithm and watching its results every step of the way
  - Experimenting with new API or trying out new Swift syntax
  - Creating new tests and then verifying that they work before promoting them into your test suite
- You can open select documentation in a playground to learn from the tutorial in a graphically rich, interactive environment.
- The debugging console in Xcode includes an interactive version of the Swift language called the _read-eval-print loop (REPL)_ built into LLDB. Use Swift syntax to evaluate and interact with your running app, or write new code to see how it works in a script-like environment. REPL is available from within the Xcode console or by using LLDB from within Terminal when attached to a running process.
- The Xcode documentation viewer shows Quick Help or reference documentation in the language of your choice—Objective-C, Swift, or both.
- Xcode synthesizes a Swift view of the SDK API when using jump-to-definition for SDK content from Swift code. The synthesized interface shows how the API is imported into Swift, and it retains all the comments from the original SDK headers.

#### Additional Feature Enhancements for Xcode 6 IDE

#### Testing

- The XCTest framework supports performance measurement capabilities enabling you to quantify each part of an application. Xcode runs your performance tests and allows you to define a baseline performance metric. Each subsequent test run compares performance and displays the change over time.
- New APIs in the XCTest framework allow testing code that executes asynchronously. You can now create tests for network operations, file I/O, and other system interactions that execute using asynchronous calls.

#### Interface Builder

- Interface Builder uses live rendering to display your custom objects at design time exactly as they appear when your app is run. When you update the code for a custom view, the Interface Builder design canvas updates automatically with the new look you just typed into the source editor, with no need to build and run.
- Size classes for iOS 8 enable designing a single universal storyboard with customized layouts for both iPhone and iPad. With size classes you can define common views and constraints once, and then add variations for each supported form factor. iOS Simulator and asset catalogs fully support size classes as well.
- Interface Builder renders embedded custom iOS fonts during design time, giving a more accurate preview of how the finished app will look, with correct dimensions.
- Find and search is supported in `.xib` and `.storyboard` files when using Interface Builder.
- The preview editor includes the ability to present multiple previews and zooming.

#### Asset Catalogs

- Size classes, JPEG, PDF, template images, and alignment rectangles are now supported by asset catalogs.

#### Debugger

- Using the view debugger, a single button click pauses your running app and “explodes” the paused UI into a 3D rendering, separating each layer of a stack of views. Using the view debugger makes it easy to see why an image may be clipped and invisible, and the order of the graphical elements becomes clear. By selecting any view, you can inspect the details by jumping to the relevant code in the assistant editor source view. The view debugger also displays Auto Layout constraints, making areas where conflicts cause problems findable.
- The debug navigator queue debugger is enhanced to record and display recently executed blocks, as well as enqueued blocks. You can use it to see where your enqueued blocks are and to examine the details of what’s been set up to execute.
- Debug gauges provide at-a-glance information about resource usage while debugging, calling the developer’s attention to previously unknown problems.

  - Two new gauges, Network Activity and File Activity, visually highlight spikes in input/output activity while your app is running.
  - The iCloud gauge is updated with support for the new Documents in the Cloud and CloudKit features that provide access to files outside the app-specific container.

#### GPU Tools

- Metal provides a new, low-overhead GPU graphics and compute API as well as a shading language for iOS. The Metal shader compiler adds support for precompiling Metal shaders in Xcode. The GPU frame debugger and shader profiler supports debugging and profiling Metal-based games and apps.

#### SpriteKit

- The SpriteKit level designer enhances SpriteKit use and provides improved display of SpriteKit variables when debugging.
- SpriteKit and SceneKit are now enhanced to work together and are supported on iOS.

#### Extensions and Frameworks

- You can add an extension target to any iOS or Mac app to expand your app’s functionality to other apps in the OS.
- iOS developers can now create dynamic frameworks.

#### iOS Simulator

- New iOS Simulator configurations allow you to keep data and configuration settings grouped together. Run one configuration for one version of an app, with its own data, and another configuration for a different app version.

#### Localization

- Xcode can package your localizable strings into the industry-standard XLIFF format for localization.
- Xcode automatically generates the base language `.strings` file directly from your source code.
- While designing in Interface Builder, the preview assistant can show how the interface appears in other languages.
- Xcode can use a locale to run your app in iOS Simulator or directly on devices, as it would appear to customers in other countries.

#### Compiler

- Profile Guided Optimization (PGO) works with the LLVM optimizer and XCTest tests to profile the most actively used parts of your application. You can also exercise your app manually to generate an optimization profile. PGO uses the profile to further optimize your app, targeting the areas that most need optimization, improving performance beyond what setting optimization options alone can achieve.
- Developers can define modules for their own Objective-C code, which makes sharing frameworks across all their projects easier.

#### Instruments

- The new Instruments user interface makes configuring your performance tuning session easier and improves control. The new template chooser allows you to choose your device and target as well as the starting point for your profiling session. The track view allows direct click-and-drag to set the time filter range. The toolbar takes up less space to let you focus on the task at hand. The tracks of recorded data are given more space, and configuration for how data is collected and viewed is managed in a unified inspector area.
- You can profile any test or test suite, which is useful for analyzing memory leaks in a functional test or time profiling a performance test to see why it has regressed.
- Simulator configurations are now treated like devices by Instruments, making it easy to launch or attach to processes in the simulator.
- Counters and Events instruments have been combined into a more powerful Counters instrument and made easier to configure. It can track individual CPU events, and you can specify formulas to measure event aggregates, ratios, and more. iOS developers on 64-bit devices can now use Counters to fine-tune apps.
- Instruments supports Swift, displaying Swift symbols in stack traces and Swift types in Allocations. You can also use Instruments to profile app extensions.

#### Xcode Server

- Triggers allow you to make more complex integration scenarios by configuring server-side rules to launch custom scripts before or after the execution of an Xcode scheme.
- Xcode Server supports the new Xcode performance-testing features, making it easy for a team to share a group of devices and Macs for continual performance testing.
- Issues are now tracked per integration and allow delta tracking, so that you can see when an issue appeared or when it or was fixed, and by whom.
- Configuration options in Xcode Server give development teams greater control over the execution of bots. New settings for integration intervals, grouping of bots, and iOS Simulator configurations make Xcode bots more powerful. The new reports UI includes bot-level statistics, the number of successful integrations, and commit and test addition tracking.

### Notes

#### Swift Support for OS X

- A future version of Xcode to be released along with OS X Yosemite will add Swift support for OS X, including playgrounds and REPL. Xcode 6.0 only supports Swift for iOS projects and playgrounds. A beta release of Xcode with Swift support for both OS X and iOS is available at [developer.apple.com/xcode/downloads/](https://developer.apple.com/xcode/downloads/)

#### Swift Language

- If you encounter an API method for which the return value is incorrectly considered non-nullable, or a property that is incorrectly considered non-nullable, please file a radar and include the tag “#IUO” in the subject line. You can work around the problem by immediately wrapping the result in an optional:

  ```
  var fooOpt: NSFoo? = object.reallyMightReturnNil()
  if let foo = fooOpt { … }
  ```

  Please be sure to file bugs about these cases. Please do not file feature requests about APIs that are still marked as T!, we know about them.

#### Xcode Features for Swift

- Refactoring for Swift is not available.

#### Compiler

- The `libc++` headers in Xcode 6 include a change to make `std::pair` have a trivial constructor. This fix is important for performance and compliance with the C++ standard, but it changes the ABI for C++ code using `std::pair`.

  This issue does not affect the `libc++` library installed on OS X and iOS systems because that library does not expose any uses of `std::pair` in its API. It is only a concern for your own code and any third-party libraries that you link with. As long as all of the code is built with the same version of `libc++`, there will be no problem.

  If you need to maintain binary compatibility with a previous version of `libc++`, you can opt into keeping the old ABI by building with the `_LIBCPP_TRIVIAL_PAIR_COPY_CTOR` macro defined to zero, that is, by adding `-D_LIBCPP_TRIVIAL_PAIR_COPY_CTOR=0` to the compiler options. (15474572)

#### Build System

- Xcode will no longer pass options in the build setting `OTHER_LDFLAGS` to `libtool` when building static libraries, nor will it pass options in `OTHER_LIBTOOLFLAGS` to the Mach-O linker when building any other kind of product. Previously all options in both settings would be passed to both tools. Make sure that options are in the correct build setting for the product type, static library, or other component being built. (4285249)
- Bundles (including frameworks, applications, and other bundles) which are added to a Copy Files build phase to embed the bundle in the current target's product will have their `Headers` and `PrivateHeaders` directories removed when they are copied. This is done to help ensure that header content in embedded bundles is not accidentally shipped to end users. This does not affect such items which are already in Copy Files build phases in existing projects. This change affects any file or directory inside the item being copied which is named exactly `Headers` or `PrivateHeaders`.

  To have a target opt out of this behavior, set the build setting `REMOVE_HEADERS_FROM_EMBEDDED_BUNDLES` to `YES`. To have an existing target opt in to this behavior, remove and then re-add the desired file references to the Copy Files build phase in question.

#### Find Navigator

- When using a regular expression in the Find navigator, it is now possible for a match to span multiple lines. The metacharacter “.” still excludes newlines, but a character class may include every character, for example, “`[\D\d]`”. (11393323)
- When using a regular expression in the Find navigator, the “`\1`” syntax is no longer supported in the replacement string. To refer to a captured group, use the syntax “`$123`”.

  With this change, you can now insert a digit after the tenth captured group and beyond by escaping the digit, for example, “`$10\2`.” Likewise, when finding text using patterns, you can insert a digit after the tenth pattern. (11836632)

#### Launch Screens

- XIBs and Storyboards can now be used as launch screens. Applications take advantage of this feature to provide a single launch screen that adapts to different screen sizes using constraints and size classes. These launch screens are supported on iOS 8.0 and later.

  Applications targeting iOS 7.x or prior releases need to also supply traditional launch PNGs via an asset catalog. Without launch PNGs for iOS 7 and earlier, applications will run in the retina 3.5” compatibility mode on retina 4” displays. (18000959)

#### Frameworks on iOS

- Embedded frameworks and dylibs are supported only on iOS 8 and later.

  If your app deploys to prior iOS releases, turn off auto-linking. Load the frameworks or dylibs using `dlopen()` after performing an OS version check. (18140501)

#### Hardware IO Tools

- The _Hardware IO Tools for Xcode_ package, available at [developer.apple.com](https://developer.apple.com), now includes the following apps:

  - Printer Simulator
  - HomeKit Accessory Simulator

  (17014426, 17014426, 17738621)
- These three apps have been removed from the _Hardware IO Tools for Xcode_ package download for this release:

  - Apple Bluetooth Guidelines Validation
  - Bluetooth Explorer
  - PacketLogger

   (18162817)

#### Xcode Server

- Xcode can now configure bots to authenticate with source control repositories using SSH keys. (16512381)
- Xcode Server prunes older integration data based on available disk space. (16535845)

#### Xcodebuild

- `xcodebuild` now supports the `id` option for iOS simulator destination specifiers. In Xcode 5 this option was only available for iOS device destination specifiers. (17398965)

### Known Issues

#### App Submission

- Xcode 6.0 GM seed may encounter issues when submitting to the App Store. These issues to be resolved in a subsequent release of Xcode. (18344000)

#### Swift Language

- The relational operator `==` may not work on `enum` values if the `enum` is declared in another file.

  Use `!(x != .Value)` instead of `(x == .Value)`. (18073705)
- Properties of values typed as AnyObject may not be directly assigned to.

  Cast the value of type '`AnyObject`' to the intended type, store it in a separate value, then assign it directly to the properties of that value. For example:

  ```
  var mc: MyClass = someAnyObject as MyClass
  mc.foo = “reassign"
  ```

  (15233922)
- Swift does not support object initializers that fail by returning null.

  If there is a factory method, use it instead. Otherwise, capture the result in an optional. For example:

  ```
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

  ```
  @objc class ObjCBox<T> {
     let _value: T[]
     var value: T { return _value[0] }
  }
  ```

  (16737510)
- Using a Swift `Dictionary` with `Int64` or `UInt64` types as keys will cause traps on 32-bit platforms when attempting to insert a key whose value is not representable by an `Int32`.

  Use `NSNumber` as the key type. (18113807)

#### Playgrounds

- In Playgrounds, `println()` ignores the `Printable` conformance of user-defined types. (16562388)
- iOS playgrounds do not support displaying animated views with the `XCPShowView()``XCPlayground` API. (17848651)

#### Compiler

- `ARM` and `ARM64` code that uses the `float16_t` type may fail when trying to link C++ code compiled with an older compiler. In previous versions of the compiler, `float16_t` was defined as `uint16_t`. `float16_t` is now defined as `__fp16`. (15506420)

#### Debugger

- View Memory for Swift data structures in the debugger may show memory location zero.

  Pass the structure to a function expecting a reference to an `UnsafePointer<Void>`, and print it within the function. Enter this address as the memory location to view. (17818703)

#### Interface Builder

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

#### Localization

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

#### App Extensions

- Signed OS X App Extensions may emit `dyld` warnings and fail to launch.

  Ensure that the same team ID is set for both the app extension and the containing app. (17711503)
- Creating an iOS Document Picker extension with the File Provider enabled does not add the containing app to the resulting app group.

  Add the containing app to the app group manually. (16871267)

#### Asset Catalogs

- If a build target’s only asset is an asset catalog, building fails with the error “`.../Contents/Resources" does not exist`.”

  Add at least one non-asset catalog resource to the build target. (17848595)

#### Refactoring

- The refactoring engine does not detect when an Objective-C class has a Swift subclass.

  When doing Objective-C refactoring, any changes needed in Swift subclasses will need to be made by hand. (16465974)

#### Building

- Incremental builds of app extensions that use Swift fail with a code signing error.

  Choose Product > Clean and then build again to workaround this issue. (17589793)
- A mixed Swift and Objective-C project may not rebuild fully after a header is changed.

  Choose Product > Clean and then build again to workaround this issue. (17963128)

#### Build System

- The build step which embeds the Swift standard libraries in a bundle only runs for application product types, and only if the application itself, independent of any embedded content, contains Swift source files.

  When building an application that does not contain Swift source files but embeds other content (like frameworks, XPC services, app extensions, and so on) that does contain Swift code, you must set the build setting _Embedded Content Contains Swift Code_ (`EMBEDDED_CONTENT_CONTAINS_SWIFT`). That way the Swift libraries will be included in the application. (17757566)

#### Xcode Server

- After upgrading to Xcode 6, users need to rejoin their ADC development team in OS X Server. (17789478)

#### iOS Simulator

- Renaming Xcode.app after running any of the Xcode tools in that bundle may cause iOS simulator to be no longer be available.

  Either rename Xcode.app back to what it was when first launched or restart your Mac. (16646772)
- Testing on iOS simulator may produce an error indicating that the application could not be installed or launched.

  Re-run testing or start another integration. (17733855)
- Settings changed in the Settings app on iOS Simulator may not persist. (18238018)
- Deleting an app from iOS Simulator doesn’t delete user defaults. (18307910)

#### Source Control

- Opening the Source Control menu in Xcode when a project references a working copy that is not checked out sometimes causes crashes.

  Delete the `.xccheckout` file within the project. (17905354)
- When updating a Subversion working copy with local modifications and an incoming change modifies the open project file (project.pbxproj), the status icons for the files modified before the update may not appear until Xcode is relaunched.

  Restart Xcode. (18122757)

#### Testing

- The XCTest class file template allows creation of a test class using Swift as the implementation language for OS X projects. However, Xcode version 6.0 does not support Swift development for OS X. Attempting to build a Swift test class in an OS X test target with Xcode 6.0 results in a compiler error. (18107068)
- Dead code stripping may remove public declarations needed for test class implementations from Swift application targets.

  Turn off dead code stripping in configurations where you are building tests. (18173029)
- XCTest test classes written in Objective-C cannot import the Swift generated interfaces header (`$(PRODUCT_MODULE_NAME)-Swift.h`) for application targets, and cannot be used to test code that requires this header.

  Write test classes for Swift code with Swift. Test classes written in Objective-C for framework targets can access the Swift generated interfaces by importing the framework module using `@import FrameworkName;`. (16931027)

### Deprecations

#### Carbon Tools

- Tools that support Carbon development are deprecated with Xcode 6. These include: BuildStrings, GetFileInfo, SplitForks, ResMerger, UnRezWack, MergePef, RezWack, SetFile, RezDet, CpMac, DeRez, MvMac, and Rez. (10344338)

#### OCUnit and SenTestingKit.framework

- OCUnit and the SenTestingKit framework are deprecated and will be removed from a future release of Xcode. Source code using OCUnit will generate warnings while being compiled. Developers should migrate to XCTest by using Edit > Refactor > Convert to XCTest. For more information, see _[Testing with Xcode](../../Developer%20Tools/Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_.

[Next](Xcode%205%20Release%20Notes.md)[Previous](Xcode%207%20Release%20Notes.md)

