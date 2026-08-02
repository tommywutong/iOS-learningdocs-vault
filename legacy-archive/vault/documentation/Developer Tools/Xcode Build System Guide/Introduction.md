---
title: Xcode Build System Guide
apple_id: TP40006904
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeBuildSystem/000-Introduction/Introduction.html
archived_at: '2026-07-15T07:27:18.908444Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Targets.md)

# Introduction

The _build system_ is the part of the Xcode that is responsible for transforming the components of a project into one or more finished products. The build system takes a number of inputs and performs operations such as compiling, linking, copying files and so forth to produce an output—usually an application or other type software.

Xcode includes a powerful build system that can create a wide variety of Mac OS X and iOS products, such as frameworks, libraries, applications, command-line tools and more. Using Xcode’s predefined project and target templates you can build these products right out of the box. However, the Xcode build system is also flexible enough to allow you to customize the build process—to tailor it to meet the special needs of your projects or support your preferred workflow.

You should read this document if you need to have a deep understanding of the Xcode build system to customize the building of your product or to use advanced features of the build system to speed up the build process.

The following chapters show how to build a product in Xcode, describe targets and the build system inputs that they organize, and show how to take advantage of build phases, build settings, and build configurations to customize the build process. These chapters also describe a number of Xcode features that you can take advantage of to shorten the edit-build-debug cycle. These features include distributed builds, precompiled prefix headers, and predictive compilation.

This document contains the following chapters:

- [Targets](Targets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmobzfvbusscfjbcugry) describes Xcode targets and how to manage them.
- [Build Phases](Build%20Phases.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojqfvbuuqkhirceqsi) provides an overview of build phases, explains how Xcode determines the order in which build phases are processed to build a product.
- [Build Settings](Build%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojrfvbecq2jizauiry) explains how build settings are implemented and how you can take advantage of them to communicate with the build system.
- [Build Configurations](Build%20Configurations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojsfvjvony) provides a general explanation of build configurations, describes the predefined build configurations you get when you create a target or project in Xcode, and explains how to modify and define your own build configurations.
- [Linking](Linking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojufvjvonq) provides details about how Xcode links code together into images and how you can customize this task.
- [Reducing Build Times](Reducing%20Build%20Times.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojvfvbuescciveuusq) describes the Xcode features that help reduce build times: precompiled headers, predictive compilation, and distributed builds.

This document also has a revision history.

[Next](Targets.md)

