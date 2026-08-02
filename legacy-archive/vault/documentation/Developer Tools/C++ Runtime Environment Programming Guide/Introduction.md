---
title: C++ Runtime Environment Programming Guide
apple_id: TP40001666
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2009-10-09'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/CPPRuntimeEnv.html
archived_at: '2026-07-15T07:24:22.612061Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview%20of%20the%20C%2B%2B%20Runtime%20Environment.md)

# Introduction

All nontrivial C++ programs must be linked with the standard C++ library, also known as the C++ runtime. This library includes the implementations for components such as I/O streams, STL container classes, the low-level exception handling runtime, and other low-level types and classes.

This document provides background information about the C++ runtime that you may find useful if you are developing C++ programs. It also offers information about Apple’s C++ support and offers tips on how to write more compatible C++ libraries and programs.

Information about the C++ runtime environment is provided in the following articles:

- [Overview of the C++ Runtime Environment](Overview%20of%20the%20C%2B%2B%20Runtime%20Environment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnrxfvbegskgjbbuqqi) describes the state of the C++ runtime environment, including issues surrounding binary compatibility and general support.
- [Deploying Applications With the C++ Runtime](Deploying%20Applications%20With%20the%20C%2B%2B%20Runtime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnryfvjvomq) provides guidelines for deploying applications using either the static or dynamic C++ standard library.
- [Creating Compatible Libraries](Creating%20Compatible%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnrzfvbeeq2fjjbekry) provides tips on how to make sure your own dynamic shared libraries retain their binary compatibility even when changes occur to the C++ runtime.
- [Controlling Symbol Visibility](Controlling%20Symbol%20Visibility.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnzqfvbuuqshijeeksq) describes new tools and techniques for controlling the symbols exported by your C++ code.

[Next](Overview%20of%20the%20C%2B%2B%20Runtime%20Environment.md)

