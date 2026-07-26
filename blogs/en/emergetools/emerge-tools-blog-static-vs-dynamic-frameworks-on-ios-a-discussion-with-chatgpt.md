---
title: 'Emerge Tools Blog | Static vs Dynamic Frameworks on iOS — a discussion with ChatGPT'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:abcba2e08291e79e'
translated: false
---

> 原文：[Emerge Tools Blog | Static vs Dynamic Frameworks on iOS — a discussion with ChatGPT](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt)　·　Emerge Tools Blog

# Static vs Dynamic Frameworks on iOS — a discussion with ChatGPT

December 14, 2022 by

Trevor Elkins & Max Topolsky

iOSSwiftApp size

![static-vs-dynamic-frameworks-ios-discussion-chat-gpt](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog-hero.ff152de3.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

## [Static vs dynamic frameworks](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#static-vs-dynamic)

Like most people in the tech world, we've been playing around with ChatGPT and wanted to see how it would do with low-level technical details. We asked ChatGPT to write a blog on Static vs. Dynamic Frameworks in iOS — here's its response, along with what it got right and what it got wrong.

**Prompt: I am a software engineer working on iOS apps. Can you write a blog post summarizing the differences between static and dynamic frameworks on iOS and how they affect app size and performance.**

### [Intro](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#intro)

_As an iOS developer, you may have come across the terms "static" and "dynamic" frameworks and wondered what the differences are between the two. In this blog post, we will explore the key differences between static and dynamic frameworks on iOS and how they affect app size and performance.First, let's define what a framework is. A framework is a collection of pre-compiled code, resources, and APIs that developers can use to build their own applications. iOS frameworks provide a standardized structure for organizing and accessing code and resources, making it easier for developers to reuse code and build complex applications.There are two types of frameworks on iOS: static and dynamic.Static frameworks are pre-compiled libraries that are linked to your app during the build process. This means that the framework code is included in the final app binary and cannot be updated or changed at runtime.Dynamic frameworks, on the other hand, are compiled libraries that are loaded at runtime. This means that the framework code is not included in the app binary and can be updated or changed at runtime.Now, let's explore the key differences between static and dynamic frameworks and how they affect app size and performance._

Not bad! It knows that static frameworks are linked during build time and dynamic frameworks are linked at runtime. There is one important distinction to make for dynamic frameworks.

First, let me clarify that an app bundle (eg the `.ipa` file you download) is different from an app binary (a Mach-O executable within the app bundle). These are often used interchangeably which can be confusing.

Here, we're showing the app bundle and then highlighting the main app binary. In addition to the main executable binary, each unique framework and extension will have its own binary.

![GIF highlighting the main executable binary](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog11%2Fapp-binary.gif&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Highlighting the main executable binary

What ChatGPT says is partially true. Dynamic frameworks provided by the system – like the Swift runtime now that it has a [stable ABI](https://www.swift.org/blog/abi-stability-and-more/) – can be updated independently from your app. However, user-provided dynamic frameworks have to be embedded within your app bundle and can't be updated in the same way.

Let's say you're using the Stripe SDK to process payments. ChatGPT's answer suggests that if the Stripe SDK is updated to include new functionality, your iOS app can leverage the newer version without any changes. In reality, that is not how it works. The code needs to be updated and the app rebuilt for the new version to be included in the app bundle.

We'll use version 2022.1201.1015 of the [LinkedIn iOS app](https://www.emergetools.com/app/example/ios/linkedin-static-vs-dynamic-frameworks) to illustrate how dynamic frameworks are included in the app bundle.

![Emerge Size Analysis X-Ray for 2022.1201.1015 of the LinkedIn iOS App](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog11%2Flinkedin-treemap.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Size Analysis X-Ray of the LinkedIn app

# X-Ray

Search

BinariesLocalizationsFontsAsset CatalogsVideosCoreML Models

We can see all the dynamic frameworks grouped under "Frameworks", a few being:

- `VoyagerLibs`
- `AzureCommunicatingCalling`
- `AgoraRTCKit`

Using `otool`, we can see what libraries the main app binary is using.

The `@rpath` declaration means that the LinkedIn binary is linking to a dynamic framework based on configured runpath search settings, whereas the Swift libraries are linked with absolute system paths. The main app binary is using the dynamic frameworks included in the app bundle. Yes, dynamic frameworks are "loaded at runtime", but it's the version in the bundle that is loaded and can not be "updated or changed" without rebuilding the bundle.

### [Effect on app size](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#effect-on-app-size)

_App Size:One of the main differences between static and dynamic frameworks is their impact on app size. Because static frameworks are linked to the app binary, they increase the size of the final app package. This can be a disadvantage for developers who are trying to minimize the size of their app to improve download and installation times.Dynamic frameworks, on the other hand, do not increase the size of the app package because the framework code is not included in the app binary. Instead, the framework is downloaded and installed on the device when the app is launched. This can be a significant advantage for developers who are trying to reduce app size._

Again, what ChatGPT says is generally true for frameworks — if you were building an app for macOS, the response would be ok. But **this isn't accurate** for the iOS runtime environment.

#### [Static frameworks and size](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#static-frameworks-and-size)

The answer ChatGPT provides here isn't completely wrong, but it misses some nuance of static frameworks.

One of the primary benefits of static frameworks is that the linker can often support dead stripping of executables. You can enable this feature in Xcode and allow the linker to analyze which symbols are used, resulting in potential size savings.

We built a sample Swift app to help demonstrate this. One [build](https://www.emergetools.com/app/example/ios/static-example-static-vs-dynamic-frameworks) of the app uses static frameworks and another [build](https://www.emergetools.com/app/example/ios/dynamic-example-static-vs-dynamic-frameworks) uses the same frameworks linked dynamically. There was no other change besides switching frameworks from static to dynamic.

Comparing the two builds, we see that install size is 2.7 MB smaller in the build that uses the frameworks statically.

![Comparison between two builds showing a size decrease in the version using static frameworks](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog11%2Fstatic-vs-dynamic-size-comp.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Comparison between two builds showing a size decrease in the version using static frameworks

#### [Dynamic frameworks and size](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#dynamic-frameworks-and-size)

As we showed above, dynamic frameworks are embedded somewhere inside the final app bundle and will increase the overall app bundle size. ChatGPT saying dynamic frameworks "do not increase the size of the app package" is flat out wrong.

This does not mean that there aren't size advantages to using dynamic frameworks. Depending on your app configuration, multiple binaries within your app bundle can use the same dynamic framework. This is common when you want to share code between the main app binary and an app extension.

To demonstrate how dynamic frameworks can share code, we'll again use the [LinkedIn iOS app](https://www.emergetools.com/app/example/ios/linkedin-static-vs-dynamic-frameworks) and examine its plugins.

![Emerge Size Analysis X-Ray for v22.36.1 of the Nike iOS App](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog11%2Flinkedin-treemap-plugins.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Size Analysis X-Ray showing LinkedIn Plugins

# X-Ray

Search

BinariesLocalizationsFontsAsset CatalogsVideosCoreML Models

LinkedIn has five different plugins:

- `NotificationServiceExtension_extension`
- `ShareExtension_extension`
- `WVMPTodayExtension_extension`
- `NewsModuleExtension_extension`
- `ShareExtension_extension`

Here's the `otool -L` command to see which shared frameworks each plugin is using.

Similar to the main app binary, three of the app plugins are linking to the framework `VoyagerLibs` and can access all of its resources.

Looking a little deeper we see a 7.4 MB `ArtDecoIconsResources.bundle` in the plugin `NotificationServiceExtension_extension`. This file also exists in `VoyagerLibs`, but `NotificationServiceExtension` doesn't link to `VoyagerLibs`. This is seemingly an oversight by LinkedIn, causing a substantial file to be duplicated.

![Treemap showing a duplicated file across a framework and a plugin](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog11%2Flinkedin-duplicate-files.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

ArtDecoIconsResources (red) is uneccessarily duplicated in a plugin

### [Effect on performance](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#effect-on-performance)

_Performance:Another key difference between static and dynamic frameworks is their impact on app performance. Because static frameworks are linked to the app binary, they are loaded into memory when the app is launched. This means that the app will use more memory and may have slower launch times because it has to load the framework code into memory.Dynamic frameworks, on the other hand, are loaded on demand at runtime. This means that the app only loads the framework code into memory when it is needed, which can improve app performance and reduce memory usage._

ChatGPT's answer gets a few things wrong here. First, the claim that static frameworks have slower launch times is incorrect (we'll come back to this point later).

ChatGPT also oversimplifies its explanation of dynamic frameworks on app launch. While it is technically possible to load a dylib later on using `dlopen()`, we don't particularly recommend using this feature for iOS apps and it's not what developers consider when deciding between static vs. dynamic frameworks. In practice, iOS apps load all of their dynamic frameworks up front during app launch with the dynamic linker [`dyld`](https://www.emergetools.com/glossary/dyld) (you can our read deep dives into `dyld` [here](https://www.emergetools.com/blog/posts/iOS15LaunchTime) and [here](https://www.emergetools.com/blog/posts/iOS16LaunchTime)).

Now, some considerations to be aware of for each approach.

#### [Static frameworks and performance](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#static-frameworks-and-performance)

Static frameworks will always load faster than dynamic frameworks, that is part of the trade-off you make when linking during build time — faster startup, slower build times. You can read this [blog post](https://acecilia.medium.com/static-vs-dynamic-frameworks-in-swift-an-in-depth-analysis-ff61a77eec65) for a detailed comparison on the effects of static vs. dynamic frameworks for performance.

A nice side-effect of using static frameworks is that larger binaries make [order files](https://docs.emergetools.com/docs/launch-booster-ios#what-is-an-order-file) more efficient. When the system goes to load symbols from your binary into memory during app launch, it does so by triggering [page faults](https://www.emergetools.com/blog/posts/FasterAppStartupOrderFiles#pages). If these symbols are not packed closely together, say they are spread loosely across one or many binaries, this will cause a lot of extra memory to be unnecessarily paged in.

To illustrate this, we'll look at the page faults in the [Robinhood app](https://www.emergetools.com/app/example/ios/robinhood-static-vs-dynamic-frameworks) (version 2022.48), which has an 86.5 MB main executable binary and uses 1559 pages during startup. Each blue grid represents a page that is used during startup.

![Page faults during app launch for Robinhood iOS app](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog11%2Frobinhood-order-files.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Page faults for Robinhood iOS app

Notice how the pages used on the left portion of the chart is scattered around the binary. This means that during app launch the entire file is going to be read from the file system, then into memory, and eventually to the CPU. This is slow because the binary is such a big file.

Order files are similar to defragmenting a hard drive on an old windows computer. It moves all the functions used during startup to be close together in the binary, so the whole file isn’t read in. Here's an example of page faults when using an optimized Order File.

![Image of optimized page faults using order files.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog11%2Foptimized-order-file.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Example of optimized page faults

#### [Dynamic frameworks and performance](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#dynamic-frameworks-and-performance)

Apple has provided guidance over the years as to how many dynamic frameworks should be loaded during app startup. This continually changes as they make improvements to DYLD with each release of iOS, and it's important for you to do your own profiling. I **highly recommend** you check out Apple's latest [WWDC2022 talk](https://developer.apple.com/videos/play/wwdc2022/110362/) on the subject!

Above we mentioned that `dyld` will load all dynamic libraries during app launch. This means that the more dynamic frameworks we add, the longer this process takes. Let's go back to our sample Swift app to demonstrate. Reminder — we have a [build](https://www.emergetools.com/app/example/ios/static-example-static-vs-dynamic-frameworks) _almost_ exclusively using static frameworks and a [build](https://www.emergetools.com/app/example/ios/dynamic-example-static-vs-dynamic-frameworks) using the same frameworks linked dynamically.

Before getting into comparing the app launch for both approaches, it's important to understand the role of `dyld` in startup — what ChatGPT got wrong. Here is an app launch flamegraph for our sample app when it is using static frameworks. Before any app launch code executes, `dyld` loads in **_all_** dynamic frameworks, which we characterize as `<early startup>`.

![App launch flamegraph showing `dyld` in startup path](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog11%2Fstatic-framework-app-launch.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

App launch flamegraph showing `dyld` in startup path

Now here's what happens to startup when we switch the app to use dynamic frameworks. Changing the frameworks to be dynamically link caused a **8.7% regression** in app launch.

![App launch comparison showing a regression in build with dynamic frameworks](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog11%2Fstatic-vs-dynamic-app-launch.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

App launch comparison showing a regression in build with dynamic frameworks

Yes, this is a very simple app and the actual change in startup is quite small. However, this change does represent that the more dynamically linked frameworks you have, the more work `dyld` has to do.

In this case, dynamic frameworks went from 2.6 MB to 12.7 MB and still caused a sizeable regression. Dynamic framework app bloat is very common and many devs don't realize the real effects sloppy management of dynamic frameworks can have on app startup.

(If you're interested, here's the [app launch comparison](https://www.emergetools.com/app/example/ios/dynamic-example-static-vs-dynamic-frameworks?buildContent=comparison) along with a [full list of dependencies](https://gist.github.com/mtopo27/c828e8f9ffe52fd1aae848de4f8d0535) we used in the sample app – we pretty much copied what Signal uses).

### [Summary](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#summary)

_In summary, static and dynamic frameworks are two types of pre-compiled libraries that iOS developers can use to build their applications. The main differences between the two are their impact on app size and performance. Static frameworks increase app size but provide faster launch times, while dynamic frameworks do not increase app size but may have slower launch times. Ultimately, the decision to use a static or dynamic framework will depend on the specific needs of your app and your development goals._

ChatGPT is already properly trained to know the answer is often “it depends”. 😂

Sadly, we see ChatGPT start to contradict itself regarding performance. Earlier it said that static frameworks "may have slower launch times" but now confidently says they "provide faster launch times".

Overall, it looks like ChatGPT understands there are differences but has trouble applying it to the context of iOS. To recap, our advice is to:

1. Start with a static framework when possible

    - Make sure Dead Code Stripping is enabled to ensure they have the smallest size footprint
    - You can use Order Files to optimize your launch performance
2. Explore dynamic frameworks if there is an opportunity to share code/resource duplication between binaries

    - Carefully measure the effect this has on your app launch performance and app bundle size
    - One pattern we see is having a single dynamic framework statically link all third-party dependencies. You can chat with us to learn more approaches!
    - Be aware that with either approach, bloat has an effect on app launch

### [Test driving](https://www.emergetools.com/blog/posts/static-vs-dynamic-frameworks-ios-discussion-chat-gpt#test-driving)

For fun I wanted to see what else ChatGPT is capable of. I've been exploring some Mach-O formats lately, so maybe it can help.

**Prompt: Write me a Swift program that extracts the LOAD_COMMANDs from a Mach-O executable**

Amazing! This _almost_ compiles, I needed to convert `$0.baseAddress` to `UnsafeMutableRawPointer.init(mutating: $0.baseAddress)`, but that was it. I also had to update it to use `mach_header_64()`, but that was my fault for not asking.

Testing this out:

We can see it matches the output of `otool -l AmazingApp`:

Pretty Neat. 😎
