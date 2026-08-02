---
title: Core Data 实用工具教程
apple_id: TP40001800
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: CoreData
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataUtilityTutorial/Articles/01_introduction.html
archived_at: '2026-07-15T07:14:28.899625Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[下一页](Creating%20the%20Project.md)

# Core Data 实用工具教程简介

本教程将引导你逐步构建一个非常基础的、基于 Core Data 的命令行实用工具。教程演示了如何从零开始创建一个使用 Core Data 的应用程序，涵盖 Core Data 技术栈的方方面面、托管对象的实例化以及数据获取（fetching）——甚至还演示了如何用代码创建模型。

这个实用工具是一个命令行应用程序，它只是简单地记录该工具的运行日期及其进程 ID，并将运行历史打印到输出中。使用命令行应用程序有助于强化这样一个理念：Core Data 与平台无关，并不绑定于某个特定的用户界面框架或平台。

本教程的重点在于演示 Core Data 中的底层功能，而非代码的简洁性、可维护性或用户友好性。虽然文中对幕后发生的事情做了一些说明，但并未对 Core Data 基础架构进行深入分析。

如果你使用 Core Data [框架](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56)创建一个没有用户界面的实用工具，或者希望更深入地理解 Core Data 基础架构，你会发现本教程很有帮助。

如果你正在为 iOS 开发应用程序，在尝试本教程之前，先学习 _Core Data Tutorial for iOS_ 可能会对你有所帮助。_Core Data Tutorial for iOS_ 介绍了由 Xcode 模板创建的 Core Data 技术栈的架构。

[Creating the Project](Creating%20the%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrqgmwviubz) 介绍了如何在 Xcode 中创建 Foundation Tool 项目，以及如何链接 Core Data。

[Creating the Managed Object Model](Creating%20the%20Managed%20Object%20Model.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrrhewviubz) 介绍了如何用代码为该实用工具创建数据模型。

[The Application Log Directory](The%20Application%20Log%20Directory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrsg4wviubz) 演示了一种识别（并在必要时创建）目录的方法，用于保存该工具持久化存储所需的文件。

[Creating the Core Data Stack](Creating%20the%20Core%20Data%20Stack.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrtg4wviubz) 介绍了如何用代码创建并配置托管对象上下文和持久化存储协调器。

[The Custom Managed Object Class](The%20Custom%20Managed%20Object%20Class.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrtgqwviubz) 说明了 Run 实体，并介绍了如何实现自定义托管对象类。

[Listing Previous Runs](Listing%20Previous%20Runs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrtgawviubz) 介绍了如何从持久化存储中获取 Run 实例。

[Complete Source Listings](Complete%20Source%20Listings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbqfvbuqmrwgewvgvzr) 展示了该项目的完整源代码。

_[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ 从高层概览到深入描述，全面介绍了 Core Data 框架提供的功能。

[下一页](Creating%20the%20Project.md)

