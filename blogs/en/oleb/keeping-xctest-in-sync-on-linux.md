---
title: Keeping XCTest in sync on Linux
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/03/keeping-xctest-in-sync/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fe8d37576a66d284'
translated: false
---

> 原文：[Keeping XCTest in sync on Linux](https://oleb.net/blog/2017/03/keeping-xctest-in-sync/)　·　Ole Begemann

# Keeping XCTest in sync on Linux

**Update:** [Swift 5.1 ships with automatic test discovery on non-Apple platforms](https://oleb.net/2020/swift-test-discovery/).

[Swift is cross-platform](https://swift.org/about/#platform-support), but it behaves differently on Apple platforms vs. all other operating systems, mainly for two reasons:

- The [Objective-C runtime](https://developer.apple.com/reference/objectivec/objective_c_runtime) is only available on Apple platforms.
- [Foundation](https://github.com/apple/swift-corelibs-foundation) and the other [core libraries](https://swift.org/core-libraries) have separate implementations for non-Apple OSes. This means some Foundation APIs may produce divergent results on macOS/iOS and Linux (though the stated goal is implementation parity), or they may simply not be fully implemented yet.

Therefore, when you write a library that doesn’t depend on any Apple-specific functionality, it’s a good idea to test your code on macOS/iOS _and_ Linux.

# Test discovery on Linux

Any unit testing framework must be able to find the tests it should run. On Apple platforms, the [XCTest framework](https://developer.apple.com/reference/xctest) uses the Objective-C runtime to enumerate all test suites and their methods in a test target. Since the Objective-C runtime is not available on Linux and the Swift runtime currently lacks equivalent functionality, XCTest on Linux [requires the developer to provide an explicit list](https://github.com/apple/swift-corelibs-xctest/blob/master/Documentation/Linux.md#additional-considerations-for-swift-on-linux) of tests to run.

## The `allTests` property

The way this works (by convention established by the [Swift Package Manager](https://swift.org/package-manager/)) is that you add an additional property named `allTests` to each of your [`XCTestCase`](https://developer.apple.com/reference/xctest/xctestcase) subclasses, which returns an array of test functions and their names. For example, a class containing a single test might look like this:

```
// Tests/BananaKitTests/BananaTests.swift
import XCTest
import BananaKit

class BananaTests: XCTestCase {
    static var allTests = [
        ("testYellowBananaIsRipe", testYellowBananaIsRipe),
    ]

    func testYellowBananaIsRipe() {
        let banana = Banana(color: .yellow)
        XCTAssertTrue(banana.isRipe)
    }
}
```

## `LinuxMain.swift`

The package manager creates another file named `LinuxMain.swift` that acts as the test runner on non-Apple platforms. It contains a call to `XCTMain(_:)` in which you must list all your test suites:

```
// Tests/LinuxMain.swift
import XCTest
@testable import BananaKitTests

XCTMain([
    testCase(BananaTests.allTests),
])
```

# Manual maintenance is easy to forget

This approach is obviously not ideal because it requires manual maintenance in two places:

1. Every time you add a new test, you must also add it to its class’s `allTests`.
2. Every time you create a new test suite, you must add it to the `XCTMain` call in `LinuxMain.swift`.

Both of these steps are easy to forget. Even worse, when you inevitably forget one of them it’s not at all obvious that something is wrong — your tests will still pass on Linux, and unless you manually compare the _number_ of executed tests on macOS vs. Linux you might not even notice that some tests didn’t run on Linux.

This happened to me numerous times, so I decided to do something about it.

## Swift 4.1 can update `allTests` for you

**UpdateMay 31, 2018:** Swift 4.1 includes [a new package manager command](https://github.com/apple/swift-package-manager/pull/1485) for keeping the list of tests for Linux up to date. You can invoke it like this:

```
> swift test --generate-linuxmain
```

This will build the test target and then generate the code for the required `__allTests` properties in a separate `XCTestManifests.swift` file. Note that the command internally still uses the Objective-C runtime for test discovery, so you have to run it on macOS.

And you have to automate this step as part of your build process — otherwise you run the risk of your Linux and Darwin tests running out of sync. Installing a safeguard that warns you when this happens is still a good idea. Therefore, I believe the rest of this article also applies to Swift 4.1, although you may have to adjust some names (Swift switched from `allTests` to `__allTests`).

# Safeguarding Linux tests against omissions

Let’s try to build a mechanism that automatically causes the test suite to fail when we forget one of the maintenance steps. We’re going to add the following test to each of our `XCTestCase` classes (and to their `allTests` arrays):

```
class BananaTests: XCTestCase {
    static var allTests = [
        ("testLinuxTestSuiteIncludesAllTests",
         testLinuxTestSuiteIncludesAllTests),
        // Your other tests here...
    ]

    func testLinuxTestSuiteIncludesAllTests() {
        #if os(macOS) || os(iOS) || os(tvOS) || os(watchOS)
            let thisClass = type(of: self)
            let linuxCount = thisClass.allTests.count
            #if swift(>=4.0)
                let darwinCount = thisClass
                    .defaultTestSuite.testCaseCount
            #else
                let darwinCount = Int(thisClass
                    .defaultTestSuite().testCaseCount)
            #endif
            XCTAssertEqual(linuxCount, darwinCount,
                "\(darwinCount - linuxCount) tests are missing from allTests")
        #endif
    }

    // Your other tests here...
}
```

This test compares the number of items in the `allTests` array to the number of tests discovered by the Objective-C runtime and will fail if it finds a discrepancy between the two, which is exactly what we want.

(The dependency on the Obj-C runtime means the test only works on Apple platforms — it won’t even compile on Linux, which is why we need to wrap it in the `#if os(macOS) ...` block.^[1](#fn:canImport))

## A failing test when you forget to add a test to `allTests`

To test this out, let’s add another test, this time “forgetting” to update `allTests`:

```
import XCTest
import BananaKit

class BananaTests: XCTestCase {
    static var allTests = [
        ("testLinuxTestSuiteIncludesAllTests",
         testLinuxTestSuiteIncludesAllTests),
        ("testYellowBananaIsRipe", testYellowBananaIsRipe),
        // testGreenBananaIsNotRipe is missing!
    ]

    // ...

    func testGreenBananaIsNotRipe() {
        let banana = Banana(color: .green)
        XCTAssertFalse(banana.isRipe)
    }
}
```

When we now run the tests on macOS, our safeguard test will fail:

[![Xcode showing the failing test](https://oleb.net/media/xcode-xctest-linux-safeguard-1550px.png)](https://oleb.net/media/xcode-xctest-linux-safeguard-1550px.png)

<sub>The safeguard test is failing because we forgot to add one test to the `allTests` array.</sub>

I really like this. Obviously, it only works if you _want_ the `allTests` array to contain every test, i.e. you’ll have to wrap any Darwin- or Linux-specific tests in conditional compilation blocks as we did above. I believe this is an acceptable limitation for most code bases.

## Safeguarding `LinuxMain.swift`

What about the other problem, verifying that `LinuxMain.swift` is complete? This is harder. `LinuxMain.swift` is not (and cannot be) part of the actual test target, so you can’t easily verify what gets passed into `XCTMain`.

[![Xcode showing build errors when you add LinuxMain.swift to the test target.](https://oleb.net/media/xcode-adding-LinuxMain-to-test-target-1400px.png)](https://oleb.net/media/xcode-adding-LinuxMain-to-test-target-1400px.png)

<sub>The errors you get when you try to add `LinuxMain.swift` to the test target.</sub>

The only solution I can see would be to add a _Run Script_ build phase to your test target and have the script parse the code in `LinuxMain.swift` and somehow compare the number of items in the array to the number of test suites in the test target. I haven’t tried it, but it sounds quite complicated.

**Update:** See the [appendix](#appendix-code-generation-with-sourcery) for a possible solution using code generation.

# Conclusion

Even with the new test, things are far from perfect since there are still two things you can potentially forget. Every time you create a new `XCTestCase` class, you must:

1. Copy and paste the `testLinuxTestSuiteIncludesAllTests` test into the new class.
2. Update `LinuxMain.swift`.

Still, I think this is considerably better than the status quo because the new test covers the most common case — adding a single test to an existing test suite and forgetting to update the `allTests` array.

I can’t wait for Swift’s reflection capabilities to become more powerful^[2](#fn:bug), making all this unnecessary.

# Appendix: Code generation with Sourcery

In what seems to be a recurring theme lately, [Krzysztof Zabłocki](http://merowing.info) pointed out that his excellent code generation tool [Sourcery](https://github.com/krzysztofzablocki/Sourcery) can also maintain the Linux test infrastructure for you. This is a great alternative and fairly easy to set up. Here’s how:

1. **[Install Sourcery](https://github.com/krzysztofzablocki/Sourcery#installing.).** Adding it as a Swift Package Manager dependency didn’t work for me (build failed), but I suspect that’s a temporary problem related to Swift 3.1 being brand new. I ended up downloading [the latest release](https://github.com/krzysztofzablocki/Sourcery/releases) and running the binary directly.
2. **Create a file named `LinuxMain.stencil`** with the following contents. Save it in a convenient place inside your project folder — I put mine in a `sourcery/` subdirectory:

  ```
  // sourcery:file:Tests/LinuxMain.swift
  import XCTest
  {{ argument.testimports }}

  {% for type in types.classes|based:"XCTestCase" %}
  {% if not type.annotations.disableTests %}extension {{ type.name }} {
    static var allTests = [
    {% for method in type.methods %}{% if method.parameters.count == 0 and method.shortName|hasPrefix:"test" %}  ("{{ method.shortName }}", {{ method.shortName }}),
    {% endif %}{% endfor %}]
  }

  {% endif %}{% endfor %}

  XCTMain([
  {% for type in types.classes|based:"XCTestCase" %}{% if not type.annotations.disableTests %}  testCase({{ type.name }}.allTests),
  {% endif %}{% endfor %}])
  // sourcery:end
  ```

  This is based on [a template](https://github.com/krzysztofzablocki/Sourcery/blob/master/Templates/LinuxMain.stencil) written by [Ilya Puchka](http://ilya.puchka.me). I just added the `// sourcery:...` annotations in the first and last lines, which determine the path of the generated file (requires Sourcery 0.5.9).

  As you can see, this is Swift code mixed with [a templating language](https://stencil.fuller.li). When you invoke Sourcery, it will parse the types in your projects source code and use them to generate code according to the template(s) you pass in. For example, the loop beginning with `{% for type in types.classes|based:"XCTestCase" %}` will iterate over all classes that inherit from `XCTestCase` and generate an extension containing the `allTests` property for them.
3. **Delete the existing definitions for `allTests` from your test classes.** We’ll generate them with Sourcery in the next step. If you’ve already added `testLinuxTestSuiteIncludesAllTests` methods, you can delete them too or choose to leave them in. They don’t hurt and may still detect issues, e.g. when you don’t run Sourcery again after adding a test, but they aren’t strictly necessary anymore.
4. **Run Sourcery** from your project directory:

  ```
  $ sourcery --sources Tests/ \
      --templates sourcery/LinuxMain.stencil \
      --args testimports='@testable import BananaKitTests'
  Scanning sources...
  Found 1 types.
  Loading templates...
  Loaded 1 templates.
  Generating code...
  Finished.
  Processing time 0.0301569700241089 seconds
  ```

  This will overwrite the existing `Tests/LinuxMain.swift` file with this generated code:

  ```
  // Generated using Sourcery 0.5.9 — https://github.com/krzysztofzablocki/Sourcery
  // DO NOT EDIT

  import XCTest
  @testable import BananaKitTests

  extension BananaTests {
    static var allTests = [
      ("testYellowBananaIsRipe", testYellowBananaIsRipe),
      ("testGreenBananaIsNotRipe", testGreenBananaIsNotRipe),
    ]
  }

  XCTMain([
    testCase(BananaTests.allTests),
  ])
  ```

  In our minimal example there’s only a single class with two tests, but this will also work for multiple test classes.

And that’s it. Add the command that invokes Sourcery to a script that you run on every build and your Linux tests will always be up to date. Very cool!

1. I don’t know of a more concise way than this for checking that we’re on an Apple platform. Once [SE-0075](https://github.com/apple/swift-evolution/blob/master/proposals/0075-import-test.md) (accepted but not implemented yet) lands, we should be able to replace this with `#if canImport(Darwin)`. [↩︎](#fnref:canImport)
2. Reflection (i.e. test discovery at runtime) is not the only way to tackle this problem. The bug tracking test discovery on Linux is [SR-710](https://bugs.swift.org/browse/SR-710), and after thorough discussion in the spring of 2016 [it was decided](https://forums.swift.org/t/sr-710-rfc-automatically-detecting-xctest-test-methods-on-linux-reflection-sourcekit/2050/12) to rely on [SourceKit](https://github.com/apple/swift/tree/master/tools/SourceKit) (i.e. source code parsing) for finding test methods. [Porting SourceKit to Linux](https://bugs.swift.org/browse/SR-1676) was and is a huge task, but as far as I can tell major progress has been made recently, so maybe the situation around testing on Linux will improve in Swift 4. [↩︎](#fnref:bug)
