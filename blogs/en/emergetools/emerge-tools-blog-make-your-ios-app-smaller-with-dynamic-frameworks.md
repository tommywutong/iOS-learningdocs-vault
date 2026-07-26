---
title: 'Emerge Tools Blog | Make Your iOS App Smaller with Dynamic Frameworks'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:b435d57a2aa7ed2a'
translated: false
---

> 原文：[Emerge Tools Blog | Make Your iOS App Smaller with Dynamic Frameworks](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks)　·　Emerge Tools Blog

# Make Your iOS App Smaller with Dynamic Frameworks

March 20, 2024 by

Jacob Bartlett

iOSApp sizeGuest post

![Make Your iOS App Smaller with Dynamic Frameworks](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.5104431f.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Every fresh-faced junior knows the cardinal software sin:

_**D.R.Y.** _(don't repeat yourself)__

However, some of the biggest iOS apps on the App Store commit the deadliest form of this sin: needless replication of entire _modules_.

Here's a typical example: the [MyHyundai app](https://www.emergetools.com/app/example/ios/myhyundai-asset-duplicates), which allows drivers to easily access their vehicle's service history and receive roadside assistance.

![MyHyundai X-Ray analysis](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fmyhyundai-xray.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Look at the large red blocks in our size analysis - these show duplication of the assets directory, which is copied into the app bundle _three times_.

![Many clones of Homer Simpson falling out of a truck](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fthree-times.gif&w=1080&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

This isn't just because the good people at Hyundai love `.car` files. It's because iOS extensions such as widgets (`MyHyundaiWidget`) and share extensions (`MyHyundaiSharePoi`) are sandboxed separately from the app itself.

Therefore, unless you're very mindful of your architecture, it's easy to make the same mistake we see in MyHyundai: _statically linking a shared UI library with each of your targets_.

Static libraries, despite ostensibly being shared code, are packaged separately in the compiled binary of each target (here, that's 1 app plus 2 extensions), which can lead to unnecessary duplication.

![Evil aliens attempting to duplicate humans](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fbio-duplication.gif&w=1080&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The textbook solution is straightforward: for modules shared between targets, link them as **[dynamic frameworks](https://www.emergetools.com/glossary/dynamic-frameworks)** instead of [static libraries](https://www.emergetools.com/glossary/static-frameworks).

Instead of embedding a copy of the module into each target, frameworks live independently inside the `Frameworks/` folder of the `.app` bundle, and [dyld](https://www.emergetools.com/glossary/dyld) links them to your app (or extension) at launch.

If you're unfamiliar with static libraries, dynamic frameworks, or dyld, get a primer on some theory with our article: _[Static vs Dynamic Frameworks on iOS - a discussion with ChatGPT](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt)_.

![A robot talking to an iPhone](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fchat-gpt-robot.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

In practice - particularly when your app is rolling a modern multi-module architecture with Swift Package Manager - it's not obvious how to link your modules dynamically.

Let's change that.

We'll work through a simple open-source tutorial project, [EmergeMotors](https://github.com/jacobsapps/EmergeMotors). We'll start in the slightly problematic `Before/` folder and pair-program together; improving the architecture until it matches `After/`. We'll analyse the app size impact of our changes as we go.

## Enter EmergeMotors

Inspired by MyHyundai, **EmergeMotors** is the hot new app for... looking at photographs of cars. It's complete with a share extension and a widget extension which both, naturally, also display cars.

![The app, share extension, and widget for EmergeMotors](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Femerge-motors-targets.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Like many modern apps, EmergeMotors has a dedicated UI library, `EmergeUI`, which contains common components and assets. This is imported into all 3 targets: the app, the share extension, and the widget extension.

By _sheer coincidence_, EmergeMotors [presents with the same architectural problem](https://www.emergetools.com/app/example/ios/emerge-motors-before) as MyHyundai: a tripled-up UI bundle in the binary.

![EmergeMotors architecture with duplication](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fbefore-xray.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

As well as assets, the `EmergeUI` view code and Lottie sub-dependency are also bundled individually with each binary.

As mentioned above, the textbook solution to this copy-pasted conundrum is to convert the statically-linked `EmergeUI` library into a dynamic framework.

## [Making a Dynamic Framework with SwiftPM](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#making-a-dynamic-framework-with-swiftpm)

By default, Xcode chooses whether to link a Swift package statically or dynamically. In practice, it always bundles your packages as static libraries.

You can tell Xcode to link your Swift Package dynamically by specifying the library type of your package as `.dynamic`:

```swift
// EmergeUI/Package.swift

let package = Package(
    name: "EmergeUI",
    platforms: [.iOS(.v16)],
    products: [
        .library(
            name: "EmergeUI",
            type: .dynamic,
            targets: ["EmergeUI"]),
    ],
    dependencies: [
        .package(url: "https://github.com/airbnb/lottie-ios.git", .upToNextMajor(from: "4.4.1")),
    ],
    targets: [
        .target(
            name: "EmergeUI",
            dependencies: [.product(name: "Lottie", package: "lottie-ios")]
        )
    ]
)
```

Hey presto! The library is now dynamic!

![Ralph Wiggum saying hey, presto!](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fhey-presto.gif&w=1080&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

You can check this has worked by looking at your main project in Xcode.

With a static library, there is no option associated with your module under "Embed" in _Frameworks, Libraries, and Embedded Content_. Once you set the library type as dynamic, a dropdown menu appears, where you can specify how to embed the framework (if this still doesn't show up, force a refresh via _File, Packages, Reset Package Caches_).

![Selecting Embed And Sign in Xcode](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fembed-and-sign.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Make sure that your main app target has the framework set to _**Embed & Sign**_, which ensures the framework is copied into the app bundle and code-signed with your profile & certificate.

Your extension targets should use the option _**Do Not Embed**_ to avoid making additional copies in the app bundle.

![Selecting Do Not Embed in Xcode](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fdo-not-embed.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

### [Umbrella Frameworks](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#umbrella-frameworks)

Your Swift Package is now a dynamic framework.

As well as wrapping the code defined in the package, sub-dependencies (including third-party libraries) are now a part of the dynamically-linked framework, even if the sub-dependency is static.

With this technique, you can even wrap many libraries in an _umbrella framework_ and expose a unified public interface to consumers as if they're importing a single module.

Apple uses umbrella frameworks all the time (`import Foundation`, `import UIKit`, `import AVKit`...), but it's generally recommended to avoid this heavy-handed approach unless you know what you're doing.

### [Early Results](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#early-results)

Now that we have our dynamic framework defined in `Package.swift`, and told Xcode how to link it for each target (in Frameworks, Libraries, and Embedded content), we can archive EmergeMotors and see how it looks.

![Emerge Tools X-Ray of the partially-optimised app](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fmiddle-xray.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Hmm... It looks like we still have a long way to go.

While our shared `EmergeUI` library code and third-party Lottie dependency are both happily packaged as a framework, the heaviest component - the `EmergeUI.bundle` - is still bundled into each target.

Inspecting our `xcarchive` file directly, we can look inside the `.app` bundle (right click + Show Package Contents) and check out `EmergeUI.bundle` itself.

![File inspection of EmergeUI.bundle](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fbundle-file.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Both the asset catalog and the Lottie JSON are packaged into a bundle and statically linked to each target. For an asset-heavy module, this negates most of the benefits of using a framework.

Now, if your shared module is mostly code - for instance, a wrapper for third-party dependencies, internal SDKs, or an umbrella for a few sub-modules - then job well done. The default SwiftPM approach to creating dynamic frameworks works fantastically.

Unfortunately, if your shared code has lots of assets, we've bumped up against a serious limitation of Swift Package Manager.

## [Deduplicating Assets](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#deduplicating-assets)

It's possible to fix this problem. It's even possible to do so using SwiftPM. However, it requires desecrating your beautifully crafted package architecture.

If you're a SwiftUI veteran, you'll be used to dipping your toes into UIKit to access more complex functionality. The technique I'm about to show you is essentially the same thing, but for architecture geeks.

![A scientist enjoying himself](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fenjoy.gif&w=1080&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

__Disclaimer: this is a little annoying to set up, and introduces overhead every time you update your shared assets. Therefore, before you complicate your architecture, work out if you really need shared assets in each target. Alternatively, consider creating separate, minimal `Assets` modules for each target to minimize duplication.__

There are 4 steps to this secret asset normalization technique:

1. Create a new Xcode Framework and move the shared assets over.
2. Create a new Swift package with a binary target.
3. Build the framework for each architecture and wrap the build outputs in an `xcframework`, referenced by the above binary target.
4. Import the new package into your existing dynamic library.

### [Creating a Framework](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#creating-a-framework)

OGs will be pretty familiar with this approach. I created a new Xcode project called `EmergeAssets` and moved over my asset catalog & JSON resources (don't forget to check the target membership!).

![Create a Framework in Xcode](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fcreate-framework.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

For good measure, I created this vital helper function.

```swift
// EmergeAssets/EmergeAssets/BundleGetter.swift

public final class BundleGetter {    
    public static func get() -> Bundle {
        Bundle(for: BundleGetter.self)
    }
}
```

This allows us to reference the assets inside the `EmergeAssets` bundle from other modules:

```swift
// EmergeUI/Sources/EmergeUI/Car/Car.swift

import EmergeAssets

public struct Car {
    // ...
    public var image: Image {
        Image("(id)", bundle: EmergeAssets.BundleGetter.get())
    }
}
```

### [Importing a binary target](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#importing-a-binary-target)

Next, I created a new Swift Package, which I imaginatively coined `EmergeAssetsSPM`.

As a wrapper package, its structure is very simple:

```swift
// EmergeAssetsSPM/Package.swift

let package = Package(
    name: "EmergeAssetsSPM",
    products: [
        .library(
            name: "EmergeAssetsSPM",
            targets: ["EmergeAssetsSPM"]),
    ],
    targets: [
        .binaryTarget(
            name: "EmergeAssetsSPM",
            path: "EmergeAssets.xcframework"
        )
    ]
)
```

This `binaryTarget` is the key.

Binary targets are pre-compiled, ensuring that your assets bundle is already neatly packaged inside the framework. This means the compiler won't build it, and won't re-bundle it into each of your targets.

Initially, we have no files in the `EmergeAssetsSPM` package, other than `Package.swift` and this mysterious shell script: `generate_xcframework.sh`.

### [Building our XCFramework](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#building-our-xcframework)

We can use the `xcodebuild` command line tools to create a binary framework.

I wrote a shell script that builds the local `EmergeAssets` Framework and packages up the architecture variants I want (iOS + Simulator) into an `xcframework`, which can be imported as the binary target for `EmergeAssetsSPM`.

```plaintext
// EmergeAssetsSPM/generate_xcframework.sh

# /bin/bash!

# Build framework for iOS
xcodebuild -project ../EmergeAssets/EmergeAssets.xcodeproj -scheme EmergeAssets -configuration Release -sdk iphoneos BUILD_LIBRARY_FOR_DISTRIBUTION=YES SKIP_INSTALL=NO

# Build framework for Simulator
xcodebuild -project ../EmergeAssets/EmergeAssets.xcodeproj -scheme EmergeAssets -configuration Release -sdk iphonesimulator BUILD_LIBRARY_FOR_DISTRIBUTION=YES SKIP_INSTALL=NO

# To find the Build Products directory, you can either: 
# 1. Manually build the framework and look in Derived Data 
# 2. run `xcodebuild -project EmergeAssets.xcodeproj -scheme EmergeAssets -showBuildSettings` and search for BUILT_PRODUCTS_DIR
PRODUCTS_DIR=~/Library/Developer/Xcode/DerivedData/EmergeAssets-fuszllvjudzokhdzeyiixzajigdl/Build/Products

# Delete the old framework if it exists
rm -r EmergeAssets.xcframework 

# Generate xcframework from build products
xcodebuild -create-xcframework -framework $PRODUCTS_DIR/Release-iphoneos/EmergeAssets.framework -framework $PRODUCTS_DIR/Release-iphonesimulator/EmergeAssets.framework -output EmergeAssets.xcframework
```

To use this yourself, you need to take care to include SDKs for all your target platforms - make sure, if you support them, you include `macosx`, `appletvos`, `watchos`, and their corresponding simulators.

_While experimenting with this, debug builds worked fine even when I'd only built the release configurations, but your mileage may vary._

### [Importing our Assets Framework](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#importing-our-assets-framework)

Finally, our `EmergeUI` module can import our SwiftPM-wrapped framework as a regular local package dependency.

```swift
// EmergeUI/Package.swift

let package = Package(
    name: "EmergeUI",
    platforms: [.iOS(.v16)],
    products: [
        .library(
            name: "EmergeUI",
            type: .dynamic,
            targets: ["EmergeUI"]),
    ],
    dependencies: [
        .package(url: "https://github.com/airbnb/lottie-ios.git", .upToNextMajor(from: "4.4.1")),
        .package(path: "../EmergeAssetsSPM")
    ],
    targets: [
        .target(
            name: "EmergeUI",
            dependencies: ["EmergeAssetsSPM", .product(name: "Lottie", package: "lottie-ios")]
        ),
        .testTarget(
            name: "EmergeUITests",
            dependencies: ["EmergeUI"]),
    ]
)
```

## [The Results](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#the-results)

With this rather substantial architectural segue out of the way, our project builds. All 3 of our targets (app, share extension, and widget extension) work as expected.

Upon archiving and analysis, [we see a thing of beauty](https://www.emergetools.com/app/example/ios/emerge-motors-after).

![EmergeMotors architecture with no duplication](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fafter-xray.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The assets catalog (and Lottie JSON) live a happy, singular life, wrapped in `EmergeAssets.framework`. The `EmergeUI` framework is linked separately, and the two extension plugins are barely visible - they are pretty small when they're not copying all our assets!

Install size has dropped drastically from **32.3MB** to a breezy **13.7MB**.

![Homer Simpson reveling in his intelligence](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fsmart.gif&w=1080&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [Launch Speed](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#launch-speed)

I would be remiss to evangelise dynamic frameworks without explaining their downside: they can negatively impact app launch time.

In the pre-main phase of app launch, dyld links the necessary frameworks to the target, ensuring all executable code and assets are accessible.

I ran a quick Performance Analysis between builds to assess whether there was any impact, generating some nifty flame graphs in the process.

The `<early startup>` phase is where dyld is linking the dynamic frameworks at launch. As well as linking our own `EmergeUI` framework, dyld also links SwiftUI, Foundation, and Swift itself!

Below is the app launch profile for our original app from `Before/`.

![Before EmergeMotors launch performance flamegraph](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fflame-before.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Profile showing app launch for EmergeMotors before optimization

And here is the profile for our more storage-efficient app from `After/`.

![After EmergeMotors launch performance flamegraph](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fflame-after.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Profile showing app launch for EmergeMotors after optimization

In this instance, no statistically significant change was found, meaning the additional dynamic linking had a negligible impact on launch time. However, I strongly suggest you profile your own apps to ensure you are mindful about the trade-off you're making.

## [Conclusion](https://www.emergetools.com/blog/posts/make-your-ios-app-smaller-with-dynamic-frameworks#conclusion)

Apple doesn't like to make things easy for us, do they?

They created a wonderful first-party package ecosystem in Swift Package Manager, but didn't put much work into explaining how to make the most of it.

It's easy enough to package a dynamic framework, however you need to jump through many undocumented hoops to properly deduplicate assets and make your app lightweight.

But when you do get it working, you can achieve awesome results like **shedding 58% from your app binary size**. Take the time to work through the sample project, understand these clandestine techniques, and apply similar improvements to your own apps!

![Homer Simpson saying woohoo!](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog21%2Fwoohoo.gif&w=1080&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

🍺

This was an Emerge Tools guest post from **Jacob Bartlett**. If you want more of his content, you can [subscribe to Jacob's Tech Tavern](https://jacobbartlett.substack.com) to receive in-depth articles about iOS, Swift, tech, and indie projects every 2 weeks; or [follow him on Twitter](https://twitter.com/jacobs_handle).
