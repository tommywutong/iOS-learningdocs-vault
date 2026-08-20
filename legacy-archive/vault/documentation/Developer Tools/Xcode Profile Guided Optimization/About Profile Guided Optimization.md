---
title: Xcode Profile Guided Optimization
apple_id: TP40014459
resource_type: Guide
platform: watchOS|Xcode Developer Tools
topic: Xcode
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/xcode_profile_guided_optimization/Introduction/Introduction.html
archived_at: '2026-07-15T07:30:56.125881Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Quick%20Start.md)

# About Profile Guided Optimization

Profile Guided Optimization (PGO) is a means to improve compiler optimization of an app. PGO utilizes a specially instrumented build of the app to generate profile information about the most commonly used code paths and methods. The compiler then uses this profile information to focus optimization efforts on the most frequently used code, taking advantage of the extra information about how the program typically behaves to do a better job of optimization.

Profile Guided Optimization provides a way to obtain more performance than you can get by using compiler options alone. Profiling gives the compiler detailed information about the most used code paths in the app.

You can automate the collection of profiles for PGO by using the Xcode testing framework, XCTest, for functional and performance measuring tests. Using tests to exercise the app when collecting the profile provides consistency and repeatability when you’ve constructed a good suite of tests for this purpose.

For information on how to create tests using the XCTest framework for your development projects, see _[Testing with Xcode](../Testing%20with%20Xcode/About%20Testing%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dcmzs)_.

[Next](Quick%20Start.md)

