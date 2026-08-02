---
title: SDK Compatibility Guide
apple_id: 10000163i
resource_type: Guide
platform: Xcode Developer Tools
topic: General
technology: null
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/cross_development/Introduction/Introduction.html
archived_at: '2026-07-15T07:30:33.208077Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20SDK-Based%20Development.md)

# Introduction

Xcode includes software development kits (SDKs) that enable you to create applications that run on specific versions of iOS or OS X—including versions different from the one you are developing on. This technology lets you build a single binary that takes advantage of new features when running on a system that supports them, and gracefully degrades when running on an older system. Some Apple frameworks automatically modify their behavior based on the SDK an application is built against for improved compatibility.

Read this document if you want your application to target a specific version or multiple versions of iOS or OS X.

This document contains the following chapters:

- [Overview of SDK-Based Development](Overview%20of%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaydclkcifbekqshinda) describes how SDK-based development works.
- [Configuring a Project for SDK-Based Development](Configuring%20a%20Project%20for%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3dg2jninedclktk4za) describes how to set up your project to use an SDK.
- [Using SDK-Based Development](Using%20SDK-Based%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgaydalktk43a) explains how to use weakly linked classes, methods, and functions, how to weakly link an entire framework, how to compile conditionally for different SDKs, and how to find uses of deprecated APIs in your code.

[Next](Overview%20of%20SDK-Based%20Development.md)

