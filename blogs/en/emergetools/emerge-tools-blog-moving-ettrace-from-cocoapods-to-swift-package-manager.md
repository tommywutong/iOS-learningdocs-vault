---
title: 'Emerge Tools Blog | Moving ETTrace from CocoaPods to Swift Package Manager'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/moving-from-cocoapods-to-swift-package-manager'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:4102b477b38b2f2c'
translated: false
---

> 原文：[Emerge Tools Blog | Moving ETTrace from CocoaPods to Swift Package Manager](https://www.emergetools.com/blog/posts/moving-from-cocoapods-to-swift-package-manager)　·　Emerge Tools Blog

# Moving ETTrace from CocoaPods to Swift Package Manager

June 29, 2023 by

Itay Brenner & Noah Martin

iOSSwift

![Graphic logo announcing ETTrace using Swift Package Manager](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog15.75f96d6c.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

When we first launched ETTrace it was built with Xcode projects and CocoaPods. This worked well for our development and allowed easy integration of our dependencies, which were C and Objective-C projects that had been around since before Swift.

However, we always wanted to try making ETTrace available through Swift Package Manager (SPM), knowing this is the Apple supported way to manage frameworks for iOS. Now, we’re excited to announce that it is available through SPM! This post will cover how we made the transition, including a few benefits and pitfalls.

## [SPM vs. Cocoapods](https://www.emergetools.com/blog/posts/moving-from-cocoapods-to-swift-package-manager#spm-vs-cocoapods)

A quick overview:

**CocoaPods** is a widely adopted dependency manager for iOS development. It supports Objective-C and Swift projects, handling complex dependencies and multi-platform targets effectively. CocoaPods operates outside of Xcode's built-in systems, by generating additional workspace files.

**Swift Package Manager (SPM)** is Apple's official tool for managing package dependencies. Designed to integrate directly with Swift and Xcode, it does not need separate workspace files, allowing for more widespread adoption.

## [Resolving bugs](https://www.emergetools.com/blog/posts/moving-from-cocoapods-to-swift-package-manager#resolving-bugs)

The first few issues opened on ETTrace were related to our Xcode project and CocoaPods configuration. One was due to the [project file structure](https://github.com/EmergeTools/ETTrace/issues/23) and [another](https://github.com/EmergeTools/ETTrace/issues/26) was from a dummy class added by CocoaPods that confliced with class names in the app ETTrace was included in. Both of these could be fixed, but we were able to avoid needing to patch them by moving to SPM.

We found the transition to SPM to reduce the overall complexity of our build, because instead of difficult to maintain project files we just had Package.swift files. This meant no difficult git conflicts and just easily reviewable Swift code, eliminating the entire class of bugs related to project files. However, SPM isn't without its own bugs, we also had an [issue](https://github.com/EmergeTools/ETTrace/issues/27) opened related to the inconvenience of mixing https and ssh links.

## [Managing SPM dependencies](https://www.emergetools.com/blog/posts/moving-from-cocoapods-to-swift-package-manager#managing-spm-dependencies)

The ETTrace xcframework has two dependencies, Crashlytics for stack unwinding and PeerTalk for device communication. We had previously linked these with CocoaPods, and needed a new way to include them with SPM. We already had a fork of Crashlytics since we only needed a small subset of its functionality. We were easily able to wrap this as a new product in our package

```swift
.target(
  name: "Unwinding",
  dependencies: [],
  path: "Unwinding/Crashlytics",
  exclude: [
      "LICENSE",
      "README.md"
  ],
  publicHeadersPath: "Public"
),
```

Supporting PeerTalk was more complicated. This project hadn’t been updated to support Swift Package Manager yet, so we had to create a fork in a new repo and [add the support ourselves](https://github.com/EmergeTools/peertalk/commit/1b905a7abe36b1f7f32288552866f0ad9d8cd0b1). A major challenge with SPM is that any dependency not already supporting SPM has to be updated manually. Hopefully this will continue to be less of burden as more frameworks update!

## [Mixing Swift and Objective-C](https://www.emergetools.com/blog/posts/moving-from-cocoapods-to-swift-package-manager#mixing-swift-and-objective-c)

Another challenge with SPM is that Swift packages can’t contain both Swift and Objective-C in a single target. We found it easiest to describe the structures sent over PeerTalk using C structs and enums, and had a single header file in the xcode project for this. So to migrate this to SPM, this one file needed to be in a target of it's own, which was added as a dependency of both the iOS framework and macOS runner.

```swift
.target(
  name: "CommunicationFrame",
  path: "ETTrace/CommunicationFrame",
  publicHeadersPath: "Public"
),
```

However, we found another issue with this approach which is that SPM does not support targets with only header files. To fix, we added a dummy Objective-C class `EMGDummyEmptyClass` to the target. This limition isn't ideal, but was similar to the dummy class added by CocoaPods before we switched to Swift Package Manager.

## [Mixed macOS and iOS products](https://www.emergetools.com/blog/posts/moving-from-cocoapods-to-swift-package-manager#mixed-macos-and-ios-products)

ETTrace consists of two products: an xcframework for iOS, and a CLI for macOS. This means our Package needs to include both iOS and macOS as valid platforms. However, when opening Package.swift in Xcode, all targets are available to build for both platforms. If you select the wrong combination, the build won’t compile.

We ran into this problem when first submitting to the [Swift Package Index](https://swiftpackageindex.com) and found our build failed. Luckily, the index has prepared for such cases. With a [custom .spi.yml](https://github.com/EmergeTools/ETTrace/blob/main/.spi.yml), you can specify the correct target/platform combination.

## [Signing and distribution](https://www.emergetools.com/blog/posts/moving-from-cocoapods-to-swift-package-manager#signing-and-distribution)

To ensure that using ETTrace is as simple as possible for everyone, we focused on finding the best distribution method. As mentioned earlier, we offer the option of building from source using SPM, which provides flexibility for users. However, we also recognize that sometimes a straightforward drag-and-drop framework is the easiest way to get started. This led us to create an xcframework alongside each release.

To automate the process, we leverage the power of GitHub Actions. Whenever a new tag is released, a trigger is set in motion, initiating our release workflow. Here's an example of the workflow configuration:

```shell
name: Release Workflow

on:
push:
  tags:
    - 'v*'
```

Within this workflow, the creation of the xcframework involves two main steps: building each target and merging them to form the xcframework.

```shell
xcodebuild archive -scheme ETTrace -archivePath ./iphonesimulator -sdk iphonesimulator ...
xcodebuild archive -scheme ETTrace -archivePath ./iphoneos -sdk iphoneos ...

xcodebuild -create-xcframework -framework ./simulator/PATH_TO/ETTrace.framework -framework ./iphoneos/PATH_TO/ETTrace.framework -output ./ETTrace.xcframework
```

Although we use SPM, we rely on xcodebuild to generate the xcframework because SPM does not provide built-in support for creating xcframeworks. Xcode remains the recommended approach for binary distribution in the Apple ecosystem.

Moving on to ETTraceRunner, our CLI tool, we understand the importance of signing it to ensure users can trust our distribution and verify its authenticity. Once again, this process is specific to Apple's platform and requires Xcode. To handle this on CI, we utilize a widely-used GitHub Action called [`import-codesign-certs`](https://github.com/Apple-Actions/import-codesign-certs). This action allows us to import our team's distribution certificate, which is encoded in Base64 and encrypted with a password (leveraging environment variables to prevent any leakage).

With the necessary certificates imported, we can proceed with building and signing ETTraceRunner:

```shell
xcodebuild archive -scheme ETTraceRunner -archivePath ./ETTraceRunner.xcarchive -sdk macosx -destination 'generic/platform=macOS' SKIP_INSTALL=NO

codesign --entitlements ./ETTrace/ETTraceRunner/ETTraceRunner.entitlements -f -s $SIGNING_IDENTITY ETTraceRunner.xcarchive/Products/usr/local/bin/ETTraceRunner
```

While it would have been possible to use `swift build` for this task, leveraging xcodebuild simplifies the process. Additionally, since Xcode has supported building SPM packages since Xcode 12, we encountered no issues in adopting this approach.

Once these steps are complete, we can effortlessly attach the generated ETTrace.xcframework and ETTraceRunner to the corresponding release in GitHub. This ensures that users can easily access and integrate ETTrace into their projects with confidence.

---

Overall, we found the Swift Package Manager version of ETTrace to be easier to maintain, even though there were a couple of rough edges during set up. For development purposes CocoaPods and Xcode project files served us very well and allowed quick experimentation without having to worry about the details of packaging.
