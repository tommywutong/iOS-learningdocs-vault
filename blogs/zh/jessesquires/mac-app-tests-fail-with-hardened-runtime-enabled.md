---
title: 启用强化运行时后 Mac App 测试失败
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2020/02/23/mac-app-tests-fail-with-hardened-runtime/'
original_language: en
published: 2020-02-23
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fd322c0d39e0ae02'
translated: true
---

> 原文：[Mac app tests fail with hardened runtime enabled](https://www.jessesquires.com/blog/2020/02/23/mac-app-tests-fail-with-hardened-runtime/)　·　Jesse Squires

我最近发现，如果为 macOS Xcode 项目启用了[强化运行时（hardened runtime）](https://developer.apple.com/documentation/security/hardened_runtime)，单元测试和 UI 测试会因模糊的错误信息而失败。我花了好一会儿才意识到问题的真正根源，因为这些错误信息把我引向了错误的方向。希望这篇文章能帮你节省一些时间。

我有一个典型的 macOS Xcode 项目，用来开发一个小型 Mac App。它存放在 GitHub 的私有仓库中，我想为它配置 [GitHub Actions](https://github.com/features/actions) 作为 CI。为了简化这个过程，我在项目设置中禁用了所有代码签名（code signing），并将项目设置为“本地运行签名（Sign to Run Locally）”。关闭代码签名后，我无需任何额外配置就可以在 GitHub 的 CI 环境中运行测试。然而，在某次操作中我可能不小心更改了强化运行时的设置。

当为单元测试和 UI 测试启用强化运行时，Xcode 会失败并显示一些模糊的错误信息。问题的根源似乎是 Xcode 在这种情况下无法加载 `XCTest` bundle。重现这个问题很容易：创建一个新的空 macOS App 项目，为所有 target 启用强化运行时，然后运行测试。

UI 测试失败时显示以下信息：

```
not valid for use in process using Library Validation: mapped file has no Team ID and is not a platform binary (signed with custom identity or adhoc?)
```

完整的 UI 测试日志（路径已脱敏）：

```
dyld: Library not loaded: @rpath/XCTest.framework/Versions/A/XCTest
  Referenced from: <PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyAppUITests-Runner.app/Contents/MacOS/MyAppUITests-Runner
  Reason: no suitable image found.  Did find:
    <PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyAppUITests-Runner.app/Contents/MacOS/../Frameworks/XCTest.framework/Versions/A/XCTest:
    code signature in (<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyAppUITests-Runner.app/Contents/MacOS/../Frameworks/XCTest.framework/Versions/A/XCTest)
    not valid for use in process using Library Validation: mapped file has no Team ID and is not a platform binary (signed with custom identity or adhoc?)
```

单元测试也出现了类似的失败，并附带一些额外信息（尽管没有帮助）。

```
Error Domain=NSCocoaErrorDomain Code=3587

NSLocalizedFailureReason=The bundle is damaged or missing necessary resources.

NSLocalizedRecoverySuggestion=Try reinstalling the bundle.
```

完整的单元测试日志（路径已脱敏）：

```
MyApp[9030:262077] Launching with XCTest injected. Preparing to run tests.

MyApp[9030:262077] Failed to load test bundle from file://<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/

MyApp.app/Contents/PlugIns/MyAppTests.xctest/:
Error Domain=NSCocoaErrorDomain Code=3587 "dlopen_preflight(<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests):

    no suitable image found.  Did find:
    <PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests:
    code signature in (<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests)
    not valid for use in process using Library Validation: mapped file has no Team ID and is not a platform binary (signed with custom identity or adhoc?)"

    UserInfo={NSLocalizedFailureReason=The bundle is damaged or missing necessary resources.,

    NSLocalizedRecoverySuggestion=Try reinstalling the bundle.,

    NSFilePath=<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests,

    NSDebugDescription=dlopen_preflight(<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests):

    no suitable image found.  Did find:
    <PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests:
    code signature in (<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests)
    not valid for use in process using Library Validation: mapped file has no Team ID and is not a platform binary (signed with custom identity or adhoc?),

    NSBundlePath=<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest,

    NSLocalizedDescription=The bundle “MyAppTests” couldn’t be loaded because it is damaged or missing necessary resources.}

MyApp[9030:262077] Waiting to run tests until the app finishes launching.

MyApp[9030:262077] ApplePersistenceIgnoreState: Existing state will not be touched. New state will be written to (null)

MyApp[9030:262077] The bundle “MyAppTests” couldn’t be loaded because it is damaged or missing necessary resources. Try reinstalling the bundle.

MyApp[9030:262077] (dlopen_preflight(<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests): no suitable image found.  Did find:
    <PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests:
    code signature in (<PATH>/Xcode/DerivedData/MyApp-gqrupcoqijumllennrlrjosdynzy/Build/Products/Debug/MyApp.app/Contents/PlugIns/MyAppTests.xctest/Contents/MacOS/MyAppTests)
    not valid for use in process using Library Validation: mapped file has no Team ID and is not a platform binary (signed with custom identity or adhoc?))
```

考虑到我是为了在 CI 上运行测试而特意修改代码签名设置的，你可以理解为什么关于缺少 Team ID、自定义签名身份（custom signing identity）以及 bundle 损坏的错误信息会让人感到困惑。

解决这个问题的方法是把强化运行时仅用于发布版本（release），并在调试版本（debug）中禁用它。
