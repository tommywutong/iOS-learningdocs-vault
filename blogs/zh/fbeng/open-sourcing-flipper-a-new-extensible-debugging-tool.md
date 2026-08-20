---
title: '开源 Flipper：一款全新的可扩展调试工具'
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2018/06/11/android/flipper/'
original_language: en
published: 2018-06-11
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0836e21239f5c4c5'
translated: true
---

> 原文：[Open-sourcing Flipper: a new extensible debugging tool](https://engineering.fb.com/2018/06/11/android/flipper/)　·　Meta Engineering — iOS

许多工程师在大型 App 上协作开发时面临的一个挑战是，通常没有哪个人单独了解每个模块的工作原理。这种知识与专业技能的分割，可能使开发新功能、排查 bug 或优化性能变得困难。为了帮助 Facebook 的工程师管理这种复杂性，我们构建了 Flipper，一个可扩展的跨平台调试工具。Flipper 为我们提供了一个界面，让框架专家和开发者能在此向框架使用者传达重要信息。现在，我们在增加功能的同时，[将 Flipper 作为开源项目分享](https://fbflipper.com/)，帮助其他人加速 App 开发过程。借助 Flipper，工程师可以用一种高度灵活、直观的方式检查和理解其 iOS 及 Android 应用的结构与行为。我们相信，Flipper 改进了现有工具，因为它提供了更直观、更具交互性的体验，并且可以扩展以满足工程师的特定需求。

这项计划始于三年多前 Stetho 的发布，Stetho 是一个基于 Chrome 开发者工具构建的 Android 调试桥接。通过 Flipper，我们希望在 Stetho 经验的基础上，设计一款更易于扩展新功能、拥有更丰富用户体验，且同时适用于 iOS 和 Android 的工具。随着[今日 Flipper 的发布](https://github.com/facebook/flipper)，我们正与开源社区分享这项工作。对于未来大多数用例，我们建议使用 Flipper 代替 Stetho。当工程师需要 Flipper 尚未实现的特定功能时（例如基于 dumpers 的命令行工具），仍可继续使用 Stetho。

## Flipper 中的扩展

Flipper 让 Facebook 工程师能够更轻松地检查我们应用的行为。它已在许多项目中使用，一些示例用例包括：

- 通过显示 Litho 和 ComponentKit 组件，让我们的工程师能够访问一个更准确地反映他们所处理功能和特性的视图层级结构（view hierarchy）。
- 呈现 GraphQL 请求流，而非原始网络事件。
- 实时追踪性能标记，使开发者能更轻松地调查性能问题。

Flipper 的设计以可扩展性为核心，因此工程师已构建了广泛的插件，覆盖通用和 Facebook 特定的用例。我们正与 Flipper 平台一起，开源我们认为对开源社区最广泛有用的插件。随着今日发布，工程师将能够检查其 App 的布局（layout），无论这些 App 是使用标准 Android/iOS 视图（view）还是 Litho/ComponentKit 组件构建的，还能同时检查来自其应用的网络流量和系统日志。

从一开始就与 Facebook 内部框架和产品开发者密切合作，我们得以确保插件 API 足够强大，能够构建各种工具。事实上，Flipper 中包含的所有工具本身都是插件；Flipper 核心只提供一组 UI 组件，并管理设备间的连接。这意味着任何人都可以构建同样强大的工具，作为自定义插件。

## 开源架构

Flipper 由两部分组成：一个桌面客户端和一个移动 SDK。Flipper 用户与桌面客户端交互。移动 SDK 安装在工程师要调试的 Android 或 iOS 应用中，然后将数据传输到 Flipper 桌面客户端。桌面客户端构建于 Electron 和 Facebook 开源项目之上，这些项目包括 React.js、Flow、Metro、RSocket 和 Yarn。移动 SDK 也大量使用了 Facebook 的开源项目，例如 Folly 和 RSocket。

要通过插件扩展 Flipper，工程师需要编写一个用来渲染 UI 的桌面客户端插件，以及一个用来暴露数据的移动 SDK 插件。对于桌面客户端插件，工程师只需创建一个继承客户端基础插件类的 React 组件。这个 React 组件负责与移动 SDK 插件通信，并渲染其传递的所有数据。桌面客户端插件也可以向移动 SDK 插件发送命令。移动 SDK 插件使用其运行平台的原生语言开发，可以是 iOS 上的 Swift/Objective-C 或 Android 上的 Java/Kotlin。移动 SDK 插件会注册一组处理程序并定义其响应，这与工程师通常构建处理客户端请求的服务器应用程序类似。

凭借这种双向套接字连接和基于 React 的 UI，我们已经能够创建种类繁多的工具，为 Facebook 工程师赋能。下图展示了正在工作中的布局检查器。属性（property）检查器显示在右侧，你可以在其中即时编辑 View 属性，从而快速测试不同设计和配置，无需重新编译。布局检查器本身也是可扩展的，Litho 团队已利用它，为通过 Flipper 检查的 Litho 组件带来了同样的实时更新能力。

![](https://scontent.xx.fbcdn.net/v/t39.2365-6/34181549_194884184473295_2201517085362749440_n.png?_nc_cat=0&_nc_log=1&oh=82a07d0dca365dd1faf1c31075f65f7e&oe=5BB21209)

## 面向开源社区的工具

我们希望将 Flipper 及配套插件开源，能为其他从事移动应用开发的工程师提供一个有用的工具。这些插件可以通过 Flipper 的 SDK，[仅用几行代码](https://l.facebook.com/l.php?u=https%3A%2F%2Ffbsonar.com%2Fdocs%2Fgetting-started.html%23setup&h=ATN-sZH2Q8W99l7w7IoUVOY5SRSf1uM3Dyll9DdfwFQo8498nBSe1Wj3BhhqvK_D4BCziQyt6XMaPF-_LcI2F5ETm5z0ef1c8RcIdrMa4qvrhDPcOYKQJhlUs_KZx8bU74gHNA)轻松集成到现有 App 中。

正如我们已经在 Facebook 内部见证了 Flipper 的价值，我们相信 Flipper 的 API 将帮助其他工程师构建出色的新体验，以改进他们的工作流程（workflow）。我们期待看到社区将创造什么，并在未来几个月里继续改进 Flipper 核心，扩展供插件开发者使用的 API 范围。

## 更新：

**自 2018 年 7 月 31 日起，我们已将开源的可扩展调试工具的名称从 Sonar 更改为 Flipper。**
