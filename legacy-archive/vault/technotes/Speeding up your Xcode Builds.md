---
title: Speeding up your Xcode Builds
apple_id: DTS10004305
resource_type: Technical Note
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2007-08-14'
source_url: https://developer.apple.com/library/archive/technotes/tn2190/_index.html
archived_at: '2026-07-26T19:54:09.170832Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2190

# Speeding up your Xcode Builds

Speed up your Xcode builds by normalizing your build settings, sharing your precompiled prefix files and specifying separate preprocessor macros for your prefix files and your targets.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzqguwugsbrfvke4vcbi4yq)[Normalize Your Build Settings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzqguwugsbrfvke4vcbi4za)[Share Your Precompiled Prefix Files](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzqguwugsbrfvke4vcbi4zq)[Separate Your Preprocessor Macros](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzqguwugsbrfvke4vcbi42a)[Additional Reading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzqguwugsbrfvauircjkreu6tsbjrpverkbireu4ry)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimzqguwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Many developers rarely modify the projects they instantiate from Xcode's templates. Tweaking a project's settings is a great way to learn Xcode in depth. Also, it is a great way to apply optimizations to your projects, ensuring they build as fast as possible.

To that end, here are some simple tips that you can apply to your projects right now to get them building faster.

[Back to Top](#)

## Normalize Your Build Settings

Projects and targets in Xcode have `Build Configurations` — collections of build settings that influence how a target is built. The `Debug` configuration, for example, will typically specify the compiler `Optimization Level` build setting with as low a value as possible. The `Release` configuration, on the other hand, will typically specify a relatively high value for the `Optimization Level` build setting.

When you create a new project from one of Xcode's templates, the principal target in that project will typically have a number of build settings customized in its configurations. The project itself, on the other hand, won't have very many customized build settings. For the one-target-per-project case this doesn't matter much. However, if you create a project with multiple targets, you can wind up with a number of targets that specify the same (or subtly different) information.

Instead of leaving your project this way, you can normalize your build settings such that build settings you want to specify for every target in the project — for example, that compiler optimization should be off for the Debug configuration — are specified at the project level rather than at the target level. This takes advantage of the fact that build settings are inherited in Xcode - if a build setting is not customized in a target, the value specified in the project is used.

__Note:__ A build setting that has had the value cleared by the user is a customized build setting. Although it contains no current value, the act of changing the value alters the setting. This is different than a build setting that has never been customized. This is an important concept, as the Xcode build system treats customized and non-customized build settings differently.

What does this buy you? It ensures that you have a single, consistent collection of settings that are passed to the compilers, linkers, and other tools that are used to build your software. Therefore, you will avoid subtle bugs like code built with the `Enable C++ Runtime Types` setting active calling a plug-in built with the same setting turned off. Normalizing your build settings also allows you to optimize your project's build process. This optimization can have a significant impact on the build speed of large projects with multiple targets.

[Back to Top](#)

## Share Your Precompiled Prefix Files

Xcode, like many other IDEs, supports prefix files — header files that are included implicitly by every one of your source files when they are built. Normally these files are specified in each of your project's target build settings. The text in the prefix file that is copied out of Xcode's templates even mentions that it is associated with a specific target. However, it is possible to share the prefix files within your project.

Prefix files get precompiled for performance, so they can simply be loaded by the compiler rather than recomputed for every file you build. Precompiling a prefix file takes quite a bit of time though, especially if you use multiple languages in your project (such as C, Objective-C, and C++) because each language needs a separate precompiled prefix due to differences in how they'll treat "the same" code.

However, just because precompiled prefix files can't be shared between languages doesn't mean they can't be shared between targets. In fact, for performance, Xcode automates this sharing for you — if you meet it halfway. The critical thing that you need to do is to ensure that your prefix files are:

- Named the same
- Built using the same compiler-related build settings

These criteria can be easily met by having your build settings normalized for your targets at the project level. You can even promote your prefix file related build settings to your project settings instead of within each targets. This will ensure that they share the same name.

In fact, if they meet the criteria that Xcode uses to determine whether precompiled prefix files should be shared, even multiple projects will wind up sharing them!

The pause between builds of a target's dependent targets to generate a new precompiled prefix file is like a pipeline stall: An unwelcome hiccup that holds everything else up until it is over. If Xcode can precompile a single set of prefix files at the start of your build and then re-use them for the rest of the process, it will stream past as quickly as possible with only the occasional pause for linking. For large projects with many dependent targets this can make a big difference in build completion time.

[Back to Top](#)

## Separate Your Preprocessor Macros

Another optimization technique is to specify separate preprocessor macros for your prefix files and targets . This works even when your project has target-specific preprocessor macros - as long as you don't need them in your prefix files, you can set them in the `Preprocessor Macros Not Used in Precompiled Headers` build setting. These will be passed to the compiler when your sources are compiled, just like the regular preprocessor macros will, but they won't be passed when precompiling a prefix file.

Of course, there are macros that you do want to set in your precompiled prefix headers, because they change the behavior. Macros like `NDEBUG` to turn off C `assert` or `NS_BLOCK_ASSERTIONS` to turn off Foundation's `NSAssert` are important to specify for your precompiled prefix files. Fortunately these types of macros typically differ only by configuration, and also remain consistent across targets and projects, allowing you to specify them at the project level rather than the target level.

[Back to Top](#)

## Additional Reading

While this document has tried to shepherd your through the process of accelerating your Xcode project's build performance, there have been concepts introduced that you may wish to explore further. Here are some links to helpful documentation that will explain in detail the [anatomy of Xcode projects](https://developer.apple.com/tools/xcode/xcodeprojects.html), how to work with the [Xcode build settings system](https://developer.apple.com/tools/xcode/xcodebuildsettings.html) and [working with precompiled prefix headers](https://developer.apple.com/documentation/DeveloperTools/Conceptual/XcodeUserGuide/Contents/Resources/en.lproj/05_09_bs_speed_up_build/chapter_36_section_2.html).

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-08-14 | New document that speed up your Xcode builds by leveraging the power of the Xcode build system |

