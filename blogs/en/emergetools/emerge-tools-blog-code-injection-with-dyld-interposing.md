---
title: 'Emerge Tools Blog | Code Injection with Dyld Interposing'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/DyldInterposing'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:bcda78ea532dd45f'
translated: false
---

> 原文：[Emerge Tools Blog | Code Injection with Dyld Interposing](https://www.emergetools.com/blog/posts/DyldInterposing)　·　Emerge Tools Blog

# Code Injection with Dyld Interposing

May 24, 2022 by

[Noah Martin](https://twitter.com/sond813)

iOSSwiftPerformance

![Code Injection with Dyld Interposing](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fblog7.f13166e1.jpg&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

The dynamic nature of the Objective-C runtime can be exploited for many purposes, including method swizzling. There are [many tutorials](https://nshipster.com/method-swizzling/) explaining how to use swizzling, and for many purposes it gets the job done. However, it can't always be used.

Swizzling handles Objective-C methods, but cannot be used for C/C++ functions. Non-Obj-C lower level calls can be useful for reverse engineering iOS apps, but sometimes you need to intercept them in an app that you don't have the source code for.

In this post we'll be looking at a lesser known technique for injecting code at a function call, one that works with C/C++ functions and with unmodified app binaries. These basic building blocks underpin many developer tools, including my work with Emerge Tools.

## [Example](https://www.emergetools.com/blog/posts/DyldInterposing#example)

Imagine you are trying to reverse engineer an app to understand how it uses the keychain. You know at some point the app calls [`SecItemCopyMatching`](https://developer.apple.com/documentation/security/1398306-secitemcopymatching), but are unsure what data is stored and what keys it is stored under. This function can't be swizzled because it is not Objective-C. You also can't modify the original source code, all you have is the compiled app.

In this post we'll implement a solution that prints all the data requested from the keychain to stdout as the app is running. The solution uses a framework that interposes `SecItemCopyMatching` and is loaded on launch with DYLD_INSERT_LIBRARIES.

## [DYLD_INSERT_LIBRARIES](https://www.emergetools.com/blog/posts/DyldInterposing#dyld-insert-libraries)

While not strictly necessary for interposing, inserted libraries are commonly combined with interposing and are a fantastic resource for anyone exploring iOS internals, so it's worth a quick overview.

DYLD_INSERT_LIBRARIES is an environment variable that allows you to add code to an app's process. The format is just a colon separated list of frameworks that will be linked on app launch. For example: `DYLD_INSERT_LIBRARIES=@executable_path/Frameworks/InterposingSample.framework/InterposingSample`. If you've ever used LD_PRELOAD on Linux/Android, this is the iOS equivalent.

This one environment variable[1] has a lot of potential, you can write a +load method to add any extra logic you want to app launch, including swizzling, responding to NSNotifications, or presenting an entirely new UI. This is even used by SwiftUI previews, inspecting a crash report from a preview reveals the line: `DYLD_INSERT_LIBRARIES=/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Library/Developer/CoreSimulator/Profiles/Runtimes/iOS.simruntime/Contents/Resources/RuntimeRoot//System/Library/PrivateFrameworks/PreviewsInjection.framework/PreviewsInjection`

## [DYLD_INTERPOSE](https://www.emergetools.com/blog/posts/DyldInterposing#dyld-interposing)

When you use [dyld](https://www.emergetools.com/glossary/dyld) interposing you don't even need to use an initializer such as +load, because it is a much more declarative API than swizzling. As [I've discussed before](https://www.emergetools.com/blog/posts/SwiftReferenceTypes), the first code that runs at app launch is dyld, not the code you write. One of dyld's responsibilities is to bind calls from one binary to another, such as from your app to Apple's frameworks. Interposing is a way to tell dyld to substitute one bound function for another.

### [Dyld Binding](https://www.emergetools.com/blog/posts/DyldInterposing#dyld-binding)

Embedded in your binary is a table of symbols that are referenced externally, I wrote about the new iOS 15 format of this data in a [previous blog post](https://www.emergetools.com/blog/posts/iOS15LaunchTime). Some of the symbols are bound lazily, only the first time they are used, through a function included in every app called `dyld_stub_helper`. Other symbols are bound right at app launch. Either of these methods allow dyld to have the final say in the address of any function defined in another binary, and luckily it gives you the opportunity to modify this address to point at your own function.

### [Interposing](https://www.emergetools.com/blog/posts/DyldInterposing#interposing)

![Diagram showing connections between images and interposed functions.](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog7%2F1.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Interposing SecItemCopyMatching with an inserted framework

Interposing works by adding a new Mach-O section (__DATA, __interpose) that contains a list of tuples holding the address to a replacement function and a replacee. If any library (including inserted ones) includes the Mach-O section (__DATA, __interpose) then dyld will use this list to replace any call to the replacee with the replacement, as long as the call is not coming from the binary containing the replacement function. **This means any call to the function you are trying to interpose in your inserted framework will still go to the original function.**

Looking at the source code for dyld, we can see exactly where these interposed addresses are loaded:

![Dyld source code](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog7%2F2.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

To make this new section in your binary Apple provides a [convenient macro](https://github.com/apple-opensource/dyld/blob/b6b86eb2db14440d373f6f7fd21be4a2bc0da897/include/mach-o/dyld-interposing.h):

![dyld_interpose macro](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog7%2F3.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Now putting this all together, we can see how to implement a framework that does what we wanted from our original example:

## [What can you do with this?](https://www.emergetools.com/blog/posts/DyldInterposing#what-can-you-do-with-this)

A lot! At [Emerge Tools](https://www.emergetools.com) we use this technique for all our runtime performance measurements such as order file generation and performance testing. With interposing you can hook into unmodified apps to measure app behavior, extract information, or completely change behavior. It's a powerful piece of the runtime for developer tools to take advantage of. Anytime you find yourself needing to swizzle a C/C++ function or anything that isn't part of Objective-C (so it can't be swizzled) it's good to be aware of interposing as an alternative you can turn to. One disclaimer: I haven't tried this in an app on the app store, but in general I would recommend it for local testing only!

## [Other Methods](https://www.emergetools.com/blog/posts/DyldInterposing#other-methods)

There are a few other ways to achieve code injection outside of the Objective-C runtime in iOS apps. [Fishhook](https://github.com/facebook/fishhook) is a popular one created by Facebook. Similar to dyld interposing it takes advantage of Mach-O symbol binding. With fishhook you don't need a separate dylib, which can be much more convenient if you have control of the apps source code. I prefer to use dyld interposing when possible because it's an entirely first-party solution, but fishhook is only a few hundred lines of C code and can be instructive to get a lower level view of how the symbol binding process works.

Intrepid readers might notice another feature in the dyld source: dynamic interposing with the function `dyld_dynamic_interpose`. This is just a way to tell dyld at runtime to start interposing a function. That's similar to how fishook works; you don't need to always interpose a function and can instead programmatically install a hook. At least one use case of this API was found by [Peter Steinberger in the Chrome source code](https://twitter.com/steipete/status/1258482647933870080?s=21). It looks like Chrome is overriding CoreAudio to modify it's behavior, interesting to see an example of interposing being used in production!

---

[1] If you're interested in other dyld environment variables, check out `man dyld`
