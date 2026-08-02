---
title: Xcode Profile Guided Optimization
apple_id: TP40014459
resource_type: Guide
platform: watchOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/xcode_profile_guided_optimization/pgo-using/pgo-using.html
archived_at: '2026-07-15T07:30:58.551756Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Profile Guided Optimization](About%20Profile%20Guided%20Optimization.md)


[Next](Document%20Revision%20History.md)[Previous](Quick%20Start.md)

# Using Profile Guided Optimization

Profile Guided Optimization (PGO) is an advanced feature for wringing every last bit of performance out of your app. It is not hard to use but requires some extra build steps and some care to collect good profile information. Depending on the nature of your app’s code, PGO may improve performance by 5 to 10 percent, but not all applications will benefit from it. If you have performance-sensitive code that needs that extra optimization, PGO may be able to help.

The LLVM compiler already does a good job of optimization by default—PGO provides further improvement for highly performance sensitive code. PGO and other compiler optimizations are not a replacement for writing efficient code. By far the most important thing you can do to improve performance is to use the right algorithms and avoid inefficiencies in your code. After you have already done that, and when you want to try to obtain even more performance, that is the time to consider using PGO.

PGO assumes that your app behaves predictably, such that a representative profile can capture the future behavior for all the performance-sensitive aspects of the code. When you enable PGO, Xcode builds a specially instrumented version of your app and then runs it. You can either manually exercise the app or use your XCTest tests to exercise the app for you.

As the app runs, the number of times each statement executes is counted and recorded. Because those statement execution counts are generally the same in both Debug and Release build configurations, it does not matter which configuration you use when collecting the profile.

You want to collect a profile of typical app behavior when generating the optimization profile. PGO counts how many times each statement runs and creates a profile modeling that behavior. The LLVM compiler then uses that profile information to focus optimization efforts on the most important code, that is, the code that runs the most frequently in typical app behavior and use.

After you have collected the optimization profile, you can enable and disable its use for PGO with the Use Optimization Profile build setting. That setting is enabled by default for the Release build configuration when you first generate the profile, but you may want to experiment with different settings as you evaluate how much PGO helps your performance. For instance, you can compare the performance of the app—with the setting turned off and then on—with your suite of tests and look for improvement or regression.

As you modify your app, periodically regenerate the profile data. Because the profile data is associated with specific statements in your code, the compiler may not be able to use it when those statements change. The compiler issues build warnings when this happens to remind you to regenerate the profile.

Nothing catastrophic will happen if you ignore those warnings, but PGO becomes less effective as your app’s code diverges from the version that generated the old profile.

Xcode supports only a single profile for PGO. If your project builds for multiple architectures, you can still have only a single profile. For most code, the statement-level execution counts will be similar across different architectures and targets. If you have code that is customized for architecture-specific versions, the profile contains data only for the architecture where the profile was collected, and you may see warnings from the compiler about missing data when building for the other architectures. These warnings are harmless—collect the profile on the primary architecture so that the optimizations will work best there.

The burden is on you to make sure that the optimization profile collected by running the app manually or with your suite of tests reflects all the important behavior where performance matters. If the profile is not representative, you may see performance degrade with PGO, so be careful. For example, if some of the code is not exercised in the profile, it may be optimized in ways that make that code run slower, putting the priority on the code that was exercised in the profile. If you cannot figure out how to run your app in ways that match all the expected uses, PGO may not be right for you.

[Next](Document%20Revision%20History.md)[Previous](Quick%20Start.md)

