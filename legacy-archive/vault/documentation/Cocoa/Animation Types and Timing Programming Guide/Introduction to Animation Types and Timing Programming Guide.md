---
title: 动画类型与时间控制编程指南
apple_id: TP40006166
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2010-05-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Animation_Types_Timing/Introduction/Introduction.html
archived_at: '2026-07-15T05:25:28.403802Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Animation%20Class%20Roadmap.md)

# 动画类型与时间控制编程指南简介

本文档介绍与 Core Animation 配合使用的时间控制类和动画类所涉及的基本概念。Core Animation 是一个 Objective-C 框架，它把高性能的合成引擎与简单易用的动画编程接口结合在了一起。

如果你想理解如何在 Cocoa 应用程序中使用 Core Animation，就应该阅读本文档。应把 The Objective-C 2.0 Programming Language 视为阅读本文档的前提，因为 Core Animation 大量使用了 Objective-C 的属性（property）。你还应该熟悉 Key-Value Coding Programming Guide 中所描述的键值编码。熟悉 Quartz 2D Programming Guide 中介绍的 Quartz 2D 图像处理技术也会有帮助，但并非必需。

《动画类型与时间控制》包含以下文章：

- [动画类路线图](Animation%20Class%20Roadmap.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnrzfvjvomi) 概述了各个动画类以及时间控制协议。
- [时间控制、时间空间与 CAAnimation](Timing%2C%20Timespaces%2C%20and%20CAAnimation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnzqfvjvomi) 详细介绍 Core Animation 的时间控制模型以及抽象类 `CAAnimation`。
- [基于属性的动画](Property-Based%20Animations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnzsfvjvomi) 介绍基于属性的动画：`CABasicAnimation` 和 `CAKeyframeAnimation`。
- [过渡动画](Transition%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnzufvjvomi) 介绍过渡动画类 `CATransition`。

以下这些编程指南讨论了 Core Animation 所使用的部分技术：

- _[Animation Overview](../../Graphics%20Imaging/Animation%20Overview/Introduction%20to%20Animation%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsnjs)_ 介绍 OS X 上可用的各项动画技术。
- _[Core Animation Programming Guide](../Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_ 包含演示常见 Core Animation 任务的代码片段。
- _[Animation Programming Guide for Cocoa](../Animation%20Programming%20Guide%20for%20Cocoa/Introduction%20to%20Animation%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkojs)_ 介绍 Cocoa 应用程序可用的动画能力。
[下一页](Animation%20Class%20Roadmap.md)

