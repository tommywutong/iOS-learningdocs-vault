---
title: 'Emerge Tools Blog | Dead Code Detection With Reaper'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:79e63ec6fe284050'
translated: false
---

> 原文：[Emerge Tools Blog | Dead Code Detection With Reaper](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper)　·　Emerge Tools Blog

# Dead Code Detection with Reaper

August 10, 2023 by

[Noah Martin](https://twitter.com/sond813)

iOSPerformanceFeatured

![Dead code detection with reaper](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog16.23dcecf1.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Dead code is all around us.

Maybe a bit dramatic, but I don't think it would be far from the truth to say that all apps have some dead code. There are quite a few benefits to removing this code. Unsurprisingly, dead code can affect app size and compile time, but excessive dead code also introduces complexity to a codebase and slows developer productivity.

Let's say you're updating a function and need to modify all call sites to work with the new function signature. This time is wasted if the call sites are dead. Dead code inherently increases the line count of a codebase, which is correlated to the [number of bugs](https://www.openrefactory.com/intelligent-code-repair-icr/#:~:text=On%20average%2C%20a%20developer%20creates,writing%20a%20line%20of%20code).

There are even performance implications for having dead code take up memory in your iOS app, which I've mentioned in articles about [fixups](https://www.emergetools.com/blog/posts/SwiftReferenceTypes) and [order files](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles). Emerge helps reduce the complexity of apps and infrastructure, including by finding dead code such as [protocols without any conformances](https://docs.emergetools.com/docs/unused-protocols). This is done with static analysis.

[Reaper](https://docs.emergetools.com/docs/reaper), Emerge's new iOS framework, goes beyond static analysis by detecting unused code at runtime. This extra dead code detection helps to build better, simpler apps.

In this post, we'll look at what dead code is and how runtime detection expands the amount we can find.

## [The kinds of dead code](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#the-kinds-of-dead-code)

Dead code refers to a few things. The following four categories are not exhaustive, but are good examples of what we commonly see.

### [1. Unreachable code](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#unreachable-code)

In the compiler/linker sense, it means unreachable code, which you can statically determine will never be called. This code gets automatically removed from the app binary during the build process. You can see dead code in [linkmaps](https://docs.emergetools.com/docs/linkmaps), each symbol that gets removed by the linker gets a separate line:

```basic
<<dead>> 	0x00000010	[ 16] _$s9EpoxyBars12BarStackViewC20didUpdateCoordinatoryAA03AnyC12Coordinating_pcSgvpMV
<<dead>> 	0x00000070	[ 16] _$s9EpoxyBars12BarStackViewC6ZOrderOWV
<<dead>> 	0x00000008	[ 16] _$s9EpoxyBars12BarStackViewC6ZOrderOMf
<<dead>> 	0x00000010	[ 16] _$s9EpoxyBars12BarStackViewC6ZOrderON
```

Emerge helps with this kind of dead code by suggesting build flags that maximize the amount of dead code found (and removed). For example, the flag [`-internalize-at-link`](https://github.com/apple/swift/blob/main/include/swift/Option/FrontendOptions.td#L654) allows stripping `public` Swift code, which can significantly decrease app size.

![Insight to strip public Swift code.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog16%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

### [2. Reachable but impossible at runtime](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#reachable-but-impossible-at-runtime)

Dead code can also be reachable. One example comes from [Swift protocols](https://www.emergetools.com/glossary/swift-protocols). You might have a protocol in your code that is reached through a cast like `myVar as? MyProtocol`. If there are no types in your code that conform to `MyProtocol` the protocol is dead code, but the type definition and any code related to checks for conformance stay in the binary. These conformance checks are guaranteed to fail because you can never create an instance that conforms to the protocol.

For example, in the following Swift code, the entire `if let` statement can be removed if we know no types conform to MyProtocol.

```swift
protocol MyProtocol { func foo() }

func bar(input: Any) {
if let castInput = input as? MyProtocol {
  castInput.foo()
} else {
  print("Input was not MyProtocol")
  fallback()
}
}
```

Emerge helps with this kind of dead code by [reporting unused protocols](https://docs.emergetools.com/docs/unused-protocols) so you can delete them.

### [3. Dynamically reachable](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#dynamically-reachable)

A less obvious source of reachable dead code is any class types for Objective-C and Swift. Even if you don't reference a class directly in source code, that class can still be used through some dynamic runtime features.

[Metadata](https://www.emergetools.com/blog/posts/SwiftReferenceTypes) about each class is included in the app binary and used by the objc runtime (even for Swift classes without @objc). This is needed because of the dynamic nature of the objc runtime with functions like `NSClassFromString()`. The compiler doesn't know if you use a class at runtime like this, so the class is not stripped.

### [4. Server controlled](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#server-controlled)

Similar to the dynamic nature of the runtime, your own code is usually very dynamic. For example, you may have code that references a class, but is itself dead due to being behind a feature flag. Feature flags commonly create large "islands" of dead code powering disabled features. Many of you are probably familiar with the experience of needing to update old code to work with a refactor, and then struggling to test it because the feature flag is not straightforward to enable. This is a big enough problem that Uber has even developed a tool specifically for deleting dead feature flags: [Piranha](https://www.uber.com/blog/piranha/).

Reaper can detect these last three categories of unused code automatically, with only one line of code added to your app.

## [Identifying dead code with Reaper](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#identifying-dead-code-with-reaper)

Reaper can do this because it leverages initialization in the Objective-C runtime. In Objective-C, all classes are sent an `+initialize` method the first time they are used.

However, Swift doesn't require this [since Swift 3.1](https://github.com/apple/swift/blob/main/CHANGELOG.md#swift-31) which poses a challenge for Reaper — it needs to work with Swift. We work around this with an initial measurement to determine which Swift classes require initialization. The measurement is done once in the Emerge infrastructure, never on user devices. After the initial measurement, supported classes can be tracked using the runtime state. Based on our measurements, many classes in popular Swift apps are still initialized and included in the Reaper report.

## [Implementation](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#implementation)

Using Reaper is straightforward. Just include the SDK in your app, the framework will report on class usage, and Emerge will aggregate the results and display them in our web app.

To include the SDK, just link the XCFramework and initialize it like this:

```swift
import Reaper

...

EMGReaper.sharedInstance().start(withAPIKey: "myKey")
```

The easiest place to put this initialization is in didFinishLaunching. It takes less than 1ms to run this line, and the SDK adds less than 20kb to your app. The SDK has no initializers, and will not run any code if you don't explicitly initialize it. Initialization is also synchronous, so you can measure how long it takes.

## [Efficiently reporting on dead code](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#efficiently-reporting-on-dead-code)

The SDK doesn't swizzle `+initialize`, in fact after calling `start` the SDK does nothing until the app is backgrounded or closed. At this point, Reaper calculates which classes were used, and makes an API request to report this. The request is compressed to reduce bandwidth consumption, and subsequent requests are deduped with already uploaded data to further reduce the impact of this network request.

## [Reaper in use](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#reaper-in-use)

We have an example of how Reaper was able to delete code from Lottie, an open source repo for animations. One of our beta users has Lottie in their app and Reaper detected `NullHapticGenerator` as being unused. This turned out to be due to `#available` checks that would always evaluate to true. My [pull request](https://github.com/airbnb/lottie-ios/pull/2111) removes the dead code so now every iOS app using Lottie can have one less class.

![Example report showing dead code found by Reaper](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog16%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Example report showing dead code found by Reaper

## [Beyond dead code](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#beyond-dead-code)

Dead code is not the only use case for Reaper. Reaper determines every time a class gets used during a user session (while the app process is running). So it also knows what % of sessions use each class. One reason you might want to know this is for launched experiments. A common practice is to fetch experiment data on app launch. If the network connection is down the app might default to assuming the experiment is not launched leading some users to still get the unlaunched experience in your app. This creates a whole new set of possible bugs due to fragmented experiences, but also makes code you would think is dead actually used. Reaper can detect classes like these with percentage usage. This feature is currently experimental, and if you have an app that would benefit from it please get in touch to tell us more about your use case.

## [Join the beta](https://www.emergetools.com/blog/posts/dead-code-detection-with-reaper#join-the-beta)

We are already piloting Reaper in several apps and serve over 20M requests per day. We're still looking for more apps to try it out with. If you're interested in trying it in your app, please get in touch!
