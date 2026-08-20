---
title: Cocoa 基础指南
apple_id: TP40002974
resource_type: Guide
platform: iOS|macOS
topic: General
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaFundamentals/Introduction/Introduction.html
archived_at: '2026-07-15T07:13:04.276463Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](What%20Is%20Cocoa.md)

# 简介

对于刚刚接触 Cocoa 的开发者来说，Cocoa 可能像是一片广阔、未经勘探的技术新大陆。这个开发环境的特性、工具、概念、设计、术语，乃至编程语言本身，都可能是陌生的。_Cocoa 基础指南_ 让你更轻松地迈出通往 Cocoa 精通之路的第一步。它为 Cocoa 这片技术版图提供了一份导览，介绍了它的特性、基本概念、术语、架构以及底层的设计模式。

你可以为两个平台构建 Cocoa 应用程序：OS X 操作系统，以及面向 iPhone、iPad、iPod touch 等多点触控设备的 iOS 操作系统。_Cocoa 基础指南_ 涵盖了这两个平台相关的 Cocoa 信息，尽可能地将两者的信息整合到一起，并在必要时指出平台间的差异。其用意在于，当你熟悉了某一个平台的 Cocoa 之后，能更容易地将这些知识迁移到另一个平台的软件开发中。

_Cocoa 基础指南_ 的结构安排是循序渐进的，逐步带你建立起对 Cocoa 开发整体的理解。它从最基础的信息——Cocoa 由哪些组件和能力构成——讲起，最后以对其主要架构的考察收尾。每一章都建立在前面章节所讲内容的基础之上。每个小节都会给出某个主题的要点，但只在较高层面上进行描述。小节中经常会引导你去参阅另一份文档，以获取更全面的说明。

在 Cocoa 开发者文档体系中，_Cocoa 基础指南_ 是概念层面的入口文档。它是阅读其他重要 Cocoa 指南的前提，例如 _[Cocoa 绘图指南](../Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_、_[View 编程指南](../View%20Programming%20Guide/Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzy)_，以及 _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_。_Cocoa 基础指南_ 对预备知识的要求不多，但读者应该是熟练的 C 语言程序员，并且应该熟悉自己所要开发的平台的能力与技术。对于 OS X，你可以通过阅读 _[Mac 技术概览](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_ 来获得这些知识；对于 iOS，请阅读 _iOS Technology Overview_。

_Cocoa 基础指南_ 包含以下几章：

- [什么是 Cocoa？](What%20Is%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzufvbuqmznknltcnq) 从功能和总体架构的角度介绍 Cocoa，描述其特性、框架和开发环境。
- [Cocoa 对象](Cocoa%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzufvbuqnbnknltgmi) 说明了 Objective-C 的优势与基本用法，以及所有 Cocoa 对象共有的行为、接口和生命周期。
- [为 Cocoa 程序添加行为](Adding%20Behavior%20to%20a%20Cocoa%20Program.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzufvbuqnjnknltc) 描述了使用 Cocoa 框架编写程序是怎样一种体验，并说明了如何创建子类。
- [Cocoa 设计模式](Cocoa%20Design%20Patterns.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzufvbuqnrnknltm) 描述了 Cocoa 对设计模式的改造应用，尤其是 Model-View-Controller 和对象建模。
- [与对象通信](Communicating%20with%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzufvbuqnznknltcni) 讨论了 Cocoa 对象之间通信所用的编程接口和机制，包括委托机制、通知和绑定。

在技术类书店中，你可以找到不少优秀的第三方 Cocoa 入门书籍，可以用来补充你从 _Cocoa 基础指南_ 中学到的内容。此外，还有几份 Apple 出版物是你在初入 Cocoa 开发时应该阅读的：

- _[The Objective-C Programming Language](../The%20Objective-C%20Programming%20Language/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrt)_ 描述了 Objective-C 编程语言及其运行时环境。
- _Model Object Implementation Guide_ 讨论了子类设计与实现方面的基本问题。
- _Developing Cocoa Objective-C Applications: A Tutorial_ 向你展示了如何使用 Xcode 开发环境、Cocoa 框架和 Objective-C 为 OS X 构建一个简单的 Cocoa 应用程序。_Your First iOS App_ 则是一份教程，引导你创建一个简单的 iOS 应用程序，沿途展示 Xcode 开发环境、Objective-C 和 Cocoa 框架的基础知识。
- _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_ 提供了专门针对用于开发 iOS 设备应用程序的框架的相关信息。
[下一页](What%20Is%20Cocoa.md)

