---
title: 'Emerge Tools Blog | Are Android apps THAT much smaller than iOS?'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:479289212c4f8970'
translated: false
---

> 原文：[Emerge Tools Blog | Are Android apps THAT much smaller than iOS?](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios)　·　Emerge Tools Blog

# Are Android apps THAT much smaller than iOS?

October 10, 2024 by

Ryan Brooks & Trevor Elkins

AndroidiOSApp size

![Are Android apps THAT much smaller than iOS?](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.dc99580a.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

People ask why an app is large on Twitter and we at Emerge break it down. It's kind of become our bat signal.

![XXX](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Fgmail-tweet.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

![XXX](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Foralb-tweet.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Usually, we break down iOS apps, as iOS apps appear to be an order of magnitude larger than their Android counterparts. Almost always, someone points to Android's size vs. iOS.

![MEOW](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Fandroid-size-tweets.png&w=828&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

At face value, they're right! The size we see in the iOS App Store is almost always a multiple of the Android counterpart in the Google Play Store.

But what if I told you that Android app sizes are larger than they might immediately appear?

In this blog, we'll explain why Android apps are larger than people think, where size comes from on both platforms, and whether iOS apps are really that much bigger than Android.

## [The App Stores](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#the-app-stores)

Let's start from the top — what do the app stores show? We'll use Linear as an example, as it's a fully native* iOS & Android application.

_*there's one big index.html file for what is likely web-specific code meant to run in-app_

The iOS App Store (left) and the Google Play Store (right) give us wildly different numbers for size:

![Linear iOS App Store listing](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Flinear-app-store.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

![Linear Google Play Store listing](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Flinear-play-store.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

iOS shows a vague "size" number, while Android shows a "download size" number. At first glance, the difference is shocking.

iOS shows **88.3 MB** vs. Android's **9.52 MB** - meaning the Linear iOS app is **~9.25x larger** than its Android counterpart!

Did Linear mess something up on iOS? Not really.

Are iOS apps that much bigger than Android? Not **9.25x** bigger.

## [Install size vs. Download size](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#install-size-vs-download-size)

First, let's clarify iOS's "Size" number. The iOS App Store shows Install Size, whereas Google Play shows Download Size. From Spotify's [blog on app size](https://engineering.atspotify.com/2023/11/the-what-why-and-how-of-mastering-app-size/):

_**Download Size:** The size of the app when downloading the app from the user's app store, i.e., the amount of data transferred over the internet. To transfer as little as possible over the internet the app download size is compressed.**Install Size:** The size of the app directly after installation on a mobile device, i.e., the amount of data stored on disk after an app has been installed. To be able to use the application, the app install size is the content of the application in uncompressed form._

Comparing a screenshot of the respective app stores is not an apples-to-apples comparison. Install size will always be larger than download size, as download is compressed to optimize for bandwidth.

From Emerge's Size Analysis of Linear's [iOS app](https://www.emergetools.com/app/example/ios/examp_4SLJKiAf3wZp), we can pinpoint Linear's estimated download size as 33.6 MB*. But wait, **33.6 MB** (iOS) vs. **9.52 MB** (Android) is still **~3.5x larger**!? How is that possible?

_*Download size from public IPAs cannot be 100% accurate, but it provides a decent estimate_

## [The size Android is "hiding" from you](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#the-size-android-is-hiding-from-you)

Let's talk ART (Android runtime). Native Android apps are usually written in Kotlin or Java. Kotlin/Java compiles into bytecode, specifically Dex bytecode (dex) on Android and is optimized to run in constrained environments, like a phone or tablet.

Android can execute Dex directly, but not without paying some performance penalties. To avoid these penalties, ART pre-compiles parts of the code to speed up code execution. This mitigation comes at the cost of increasing app install size.

## [How code is executed](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#how-code-is-executed)

### [Native code](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#native-code)

Computers run native code, raw instructions that tell the CPU what to do, like loading something into memory or performing a calculation. Despite appearing like what one would call "native code" to the human eye, dex (and other bytecode) is not native code. Dex still needs to undergo another step to become native code.

In the snippet below, we have a simple Sort function that gives an illustration of the code we write (Kotlin) compared to the compiled dex bytecode and finally, the native code that the CPU executes:

![Code as bytecode vs. native code](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Fcompiler-explorer.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Left: Kotlin, Center: dex bytecode, Right: arm64 native code ([source](https://godbolt.org/z/Yx75qTxM5))

The important takeaway is that the Kotlin/Java code we write is not what's executed by Android. Even after it's "compiled" to dex bytecode, it still needs to become native code at some point so Android can run it.

And this compiled native code is quite large! Larger than our Kotlin source code and our dex bytecode.

### [Compilation vs. Interpretation](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#compilation-vs-interpretation)

A **compiled language** is directly transformed into native code by a compiler (C++ / Swift). Once compiled, the computer directly executes instructions. The drawback is that compiled native code only works on the platform the compiler built it for (e.g. x86, ARM64).

An **interpreted language** uses an interpreter to convert source code to native code one instruction at a time (Python / Javascript). Interpreted code doesn't rely on a compiler and offers more flexibility because it isn't pre-compiled to a specific platform. The drawback is a performance penalty due to the required "translation" from source to native code.

### [How Android executes code](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#how-android-executes-code)

Kotlin and Java don't fall into one category. They are "compiled" to dex on Android. If no optimizations are made, **dex is interpreted**, meaning each dex bytecode instruction is translated into native code one-at-a-time as the program runs.

Interpreting code is slow, particularly on constrained devices like lower-end Android phones. To speed up bytecode execution, ART uses tactics like just-in-time (JIT) & ahead-of-time (AOT) compilation. JIT happens during runtime and compiled code is not stored, meaning there is no impact on size.

#### [Ahead-of-time (AOT) compilation](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#ahead-of-time-compilation)

With AOT, ART pre-compiles dex to native code and stores the native code for later use.

Fully AOT compiling an app can have significant space (and time) ramifications. Enter profile-guided optimization.

#### [Profile-guided optimization (PGO)](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#profile-guided-optimization)

Profile-guided optimization uses profiles (statistics about the code) to determine commonly used code. These profiles are leveraged to AOT compile the most used code (rather than all dex), optimizing for both performance and disk space.

If you're an Android developer, you might have heard of baseline profiles before - baseline profiles are a form of PGO!

PGO speeds up code execution by compiling **the most used portions** of dex bytecode to native code and saving the native code for later (re)use. This improves performance at the optimal disk space expense, pre-compiling only the most important parts of the dex.

## [The price to pay: Install size](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#the-price-to-pay-install-size)

### [Android install size](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#android-install-size)

Since Android pre-compiles dex bytecode to native code, this compiled native code needs to be stored somewhere.

Let's go back to Linear.

We can force clear all native code using `adb shell cmd compile —reset app.linear` (left) and compare it vs. a fresh install (right) to see a noticeable difference:

![Linear Android app with no AOT](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Flinear-size-no-aot.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

![Linear Android app after fresh install](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Flinear-size.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The app with no pre-compiled native code is **17.86 MB**, while just after a fresh install, it's **25.81 MB**! Where did the ~8 MB come from? The answer is baseline profiles.

ART is leveraging PGO to pre-compile the most used portions of the code.

After checking on device, we can confirm this is AOT compiled `.odex`, which is our native code.

```shell
# /data/app/.../app.linear-.../oat/arm64
$ ls -l
-rw-r--r-- 1 system all_a6089       0 2024-09-20 16:10 base.art
-rw-r--r-- 1 system all_a6089 8064752 2024-09-20 16:10 base.odex
-rw-r--r-- 1 system all_a6089  273892 2024-09-20 16:10 base.vdex
```

This native code is generated by ART at install time using an on-device compiler called `dex2oat`. We won't go into too much detail here, but [here's further reading](https://source.android.com/docs/core/runtime/configure#how_art_works) if you're interested!

### [iOS install size](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#ios-install-size)

Native iOS apps, on the other hand, are compiled entirely to native code at build time. This means iOS gets the performance of running native code, but its binary size is larger than Android (where only a portion of code is compiled to native). There is no knob to turn for controlling how much code is compiled to machine code like there is for Android.

There are a few steps to go from Swift source code to machine code. First, the Swift compiler frontend converts your code into Swift Intermediate Language (SIL), which allows for some custom optimization passes to be done, among other things. SIL is then "lowered" into a more generic LLVM intermediate representation (IR), and from there, LLVM can generate machine code for various target architectures.

When you build your app in Xcode, you can see the exact commands being sent to the Swift compiler:

![Xcode build commands](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Fxcode.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

After digging through this gigantic build command, we eventually see where Xcode is outputting native code for the `arm64` architecture:

```plaintext
/Users/User/Library/Developer/Xcode/DerivedData/HackerNews-dzukkzbeqbfejeapaejefshbwqhx/Build/Intermediates.noindex/HackerNews.build/Debug-iphonesimulator/HackerNews.build/Objects-normal/arm64/
```

Opening that folder shows all the `.o` object files we'd expect per source file. These object files are then linked together into the final binary result that gets packaged to users. If you inspect the binary, you'll find most of the app's machine code in the `__TEXT` and `__DATA` segments.

## [Apples to apples - comparing Linear's "worst-case" Android install size vs. iOS's install size](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#apples-to-apples-comparing-linears-worst-case-android-install-size-vs-ioss-install-size)

On a "fresh install" of both apps, iOS is still ~3.5x bigger (87.6 MB vs. 25.1 MB). But what if we force Android to behave like iOS?

```shell
adb shell cmd package compile -m speed -f app.linear
```

Running this command fully AOT compiles the Linear Android app, generating all possible native code from the dex bytecode. It's worth noting that fully AOT compiling an Android app will likely never happen in the wild, but this is a fun exercise to compare iOS vs. Android.

Checking out our install size gives us results that are much closer together than our original App Store numbers:

![Linear iOS install size - 87.6 MB](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Fios-size.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

![Linear Android install size - 56.08 MB](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Fandroid-size.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

There we go, that's more like it. **87.6 MB** on iOS vs. Android's **56.08 MB** fully AOT compiled install size, only **~1.5x larger (31.5 MB)**.

Don't get me wrong, 1.5x is still a large gap! But let's remember where we started

| Source | iOS | Android | Difference |
|---|---|---|---|
| App store | 88.3 MB ("size") | 9.52 MB | ~9.25x (78.78 MB) |
| Download size (Emerge) | 33.6 MB | 9.52 MB | ~3.5x (23.94 MB) |
| On-device Install | 87.6 MB | 25.81 MB (normal install) | ~3.5x (61.59 MB) |
| On-device Install | 87.6 MB | 56.08 MB (fully AOT compiled) | ~1.5x (31.5 MB) |

## [What about that extra size gap?](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#what-about-that-extra-size-gap)

There's still a non-negligible ~**31.5 MB** size difference between the Linear iOS and Android apps. Let's look at some of the reasons why.

### [App bundle & Split APKs](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#app-bundle-split-apks)

Android employs even more size optimizations its app bundle (AAB) format. The AAB format splits the app into multiple smaller, modular APKs specific to a user's device rather than a single, universal APK containing all assets, architecture, and languages the app supports.

By doing this, Play is able to ship the minimal amount of languages, code, and resources to ensure the optimal download and install size.

Apple has a similar feature called "app thinning," which creates multiple variants of the app to send to users based on their device type. This means an image scaled for an iPad isn't downloaded to an iPhone.

While Apple has a mechanism to reduce the size of unused images, it does not optimize localizations. When downloaded, an iOS app contains all the localizations it supports, even though a user likely only uses a single localization. The Gmail iOS app has ~[130 MB of localizations](https://x.com/emergetools/status/1810790283216572822) on iOS, larger than the uncompressed size of the entire Gmail Android app 🤯.

### [Swift](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#swift)

Swift is a modern language with advanced features and memory safety. While we love Swift at Emerge, all of these features come at a cost in the generated output. Swift's binaries are inherently more bloated than (as an extreme example) a language like C where you manage your own memory.

Compiler synthesis for automatic type conformance is also getting popular for more and more features, now generalized with the addition of macros. This can lead to a surprising amount of code in some cases, like making a complicated type conform to `Codable` , and most of this generated code ends up in the final binary.

We recommend you play around with a tool like [Godbolt](https://godbolt.org/z/csna1zTqa) to see for yourself! This simple 6-line program generates 1936 lines of assembly:

```swift
import Foundation

struct JSONTest: Codable {
    let firstName: String
    let lastName: String
}
```

### [iOS can get tricky](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#ios-can-get-tricky)

If you follow us on Twitter, you're familiar that iOS apps have many sources of avoidable bloat. Even the "app thinning" feature we mentioned above can be done "wrong" by developers.

#### [Duplicate files](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#duplicate-files)

17% of the Linear iOS app size is from duplicate files.

![Linear iOS app duplicate files](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Flinear-duplicates.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

You could create a dynamic framework to share code and resources, however it is more difficult than it should be to correctly modularize and share code in an iOS app. While duplication can happen on Android, it is far from the scale of iOS.

#### [Binary symbol bloat](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#binary-symbol-bloat)

For the debugger to work with native code, the Swift compiler inserts various DWARF debugging symbols into the binary. When debugging code and a breakpoint is triggered, these symbols are how Xcode resolves function and variable memory addresses into human-readable names.

These symbols are only needed for development. Unfortunately it's very easy to include these by accident, and it's a common source of bloat in iOS apps. Debugging symbols similarly exist in Android's DEX files, but Android Studio is very good about removing them by default in release builds.

Here's how frequently this happens 👇

![Linear iOS app duplicate files](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Fsymbols-tweet.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

https://x.com/jazzychad/status/1842040535881596964

Funny enough, the Linear app is actually victim to a different type of iOS symbol bloat - unnecessary binary tries. This is 6.6 MB that can be shaved off through settings in Xcode.

![Tweet](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog27%2Fmetadata.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

[source](https://x.com/jazzychad/status/1842040535881596964)

The mere fact that iOS developers have multiple ways to introduce symbol bloat is unheard of for Android.

We could keep listing other iOS peculiarities, like how FedEx has [56 MB of comments and Unicode](https://x.com/emergetools/status/1689308029848576000) in their localizations or how the "levels" in [Candy Crush Saga](https://www.emergetools.com/deep-dives/candy-crush-saga) take up 30 MB more on iOS than Android because of the minimum file size allocation. But we'll stop here.

### [Other Size Differences](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#other-size-differences)

A quick look at other sources of size disparity

- **R8/Proguard Optimizations**: R8 & Proguard are tools used to minify the dex bytecode that Android apps contain. These tools employ many optimizations (like tree-shaking, obfuscation, etc) that go much further than any similar feature on iOS.
- **Dynamic Features (Android) vs. On-Demand Resources (iOS)**: Android supports dynamic features, allowing parts of an app to be downloaded on-demand, such as specific libraries or features. Apple's equivalent, On Demand Resources, only supports assets like videos or game files, not full app features.

## [Wrapping up](https://www.emergetools.com/blog/posts/are-android-apps-really-that-much-smaller-than-ios#wrapping-up)

Phew. App size can be complicated.

To summarize, Android apps **are bigger than you think**:

- The size number shown in Google Play is the **download size**. This is the compressed app, whereas Apple shows the **install size** (uncompressed app)
- Android pre-compiles a portion of its app to native code. This native code is stored alongside the app's dex bytecode, increasing our install size footprint.

BUT, iOS apps are still bigger than Android because:

- iOS apps are compiled as fully native vs. Android, which is only partially compiled
- Swift is a more verbose language than Kotlin and auto-generates more native code than Android
- Apple tooling makes it easier to introduce bloat than Android

Both platforms have a wide variety of mechanisms and features developers can use to reduce app size, which are tied to the history of the platforms. iOS, with tight control over both hardware and software, ships exactly the native code that will run on your iPhone. On the other hand Android, where OEMs can bring whatever hardware they want, evolved advanced split APK targeting to download only the bits of the app you need for the specific device.

Try [uploading your app](https://www.emergetools.com/) today to see what is behind the number.

Special thanks to Hector Dearman, Noah Martin and Max Topolsky for helping review!
