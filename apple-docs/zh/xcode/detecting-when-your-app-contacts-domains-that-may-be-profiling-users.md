---
title: 检测你的 App 何时联系可能构建用户画像的域
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/detecting-when-your-app-contacts-domains-that-may-be-profiling-users
source_url: 'https://developer.apple.com/documentation/xcode/detecting-when-your-app-contacts-domains-that-may-be-profiling-users'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/detecting-when-your-app-contacts-domains-that-may-be-profiling-users.json'
content_hash: 'sha256:ec642a59cedf7466'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md)

# 检测你的 App 何时联系可能构建用户画像的域

<sub>文章</sub>

使用 Instruments 评估你的 App 或其第三方 SDK 是否连接到可能为用户构建画像的域。

## 概述

操作系统维护着一份 DNS 域列表，其中的域可能跨多个 App 和网站跟踪用户，并将其活动合并成用户画像。请使用 Instruments 发现你的 App 是否会联系这些域——联系行为可能源自你编写的代码，也可能源自 App 所链接的第三方 SDK 中包含的代码——以便评估这些域的用途是否属于「App 跟踪透明度」框架所定义的跟踪。有关更多信息，请参阅[用户隐私与数据使用](https://developer.apple.com/app-store/user-privacy-and-data-use/)。

### 分析你的 App 的网络行为

Xcode 和 Instruments 提供了分析 App 网络连接所需的工具。具体来说，你可以使用 Instruments 记录 App 的出站和入站 HTTP 流量，然后分析其中是否存在任何意外活动。请按照以下步骤操作：

1. 在 Xcode 中打开你的 App 项目。
2. 选择「Product」\>「Profile」。Xcode 会构建 App 以进行性能分析，并在 Instruments 中打开它。
3. 在 Instruments 中选择「Network」模板。
4. 点按「Record」。
5. Instruments 会显示提醒，警告你记录 HTTP 流量可能会暴露敏感信息和个人信息。如果你接受此风险，请点按「Record Anyway」。Instruments 会启动你的 App 并开始性能分析。
6. 使用你的 App 的各项功能。
7. 完成后，切换回 Instruments 并点按「Stop」。

![Instruments 的屏幕截图，显示使用网络 instrument 记录 HTTP 流量时出现的对话框。](../../../attachments/c9cb8c9fd16af6de79f3aa1ecdeffa1e/detecting-potential-profiling-1@2x.png)

### 检查你的 App 与可能构建用户画像的域之间的连接

当你的 App 向操作系统 DNS 域列表中的某个域发出 HTTP 请求，而该域可能跨多个 App 和网站跟踪用户并将其活动合并成用户画像时，Points of Interest instrument 会记录此活动。时间线中 Points of Interest 轨道上的故障标记会显示你的 App 何时向该域发出请求。

在 Instruments 中，选择 Points of Interest 轨道。「Detail」区域会显示你的 App 向这些域发出 HTTP 请求的各个时刻。选择某个关注点（point of interest）在「Start」列中的条目，将时间指示头移动到该时刻。Instruments 会聚焦于 App 发出 HTTP 请求的时间，让你可以探索其他轨道，进一步了解 App 发出请求时的行为。有关使用 Instruments 分析 HTTP 流量的更多信息，请参阅[使用 Instruments 分析 HTTP 流量](../foundation/analyzing-http-traffic-with-instruments.md)。

![](../../../attachments/a43f4573c5bfbce5b7d5880c3e412063/detecting-potential-profiling-2@2x.png)

<sub>Instruments 的屏幕截图，时间线上显示多个关注点，表示 App 联系了可能跨多个 App 和网站跟踪用户并将其活动合并成用户画像的域。详细信息视图中选中了一个关注点。</sub>

### 在 App 的 privacy manifest 中声明跟踪域

如果你确定 App 连接的域正在使用 App 所发送的数据跟踪用户，请在 privacy manifest 中声明这些域，并根据「App 跟踪透明度」框架请求跟踪权限。有关更多信息，请参阅[用户隐私与数据使用](https://developer.apple.com/app-store/user-privacy-and-data-use/)。当用户尚未授予跟踪权限时，操作系统会阻止对已声明跟踪域的网络请求。

如果你不希望 App 进行跟踪，请考虑移除相关代码，或联系代码会访问该域的第三方 SDK 开发者。如果第三方 SDK 有 privacy manifest，该清单也可能提供有关该 SDK 是否参与跟踪的详细信息。有关更多信息，请参阅[在 privacy manifest 中描述数据使用](../bundleresources/describing-data-use-in-privacy-manifests.md)。

## 另请参阅

### 调试策略

- [诊断运行中 App 的外观问题](diagnosing-issues-in-the-appearance-of-your-running-app.md) — 检查正在运行的 App，以调查其显示内容的外观和位置问题。
- [尽早诊断内存、线程与崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md) — 在测试期间使用 Xcode 的 sanitizer 工具识别 App 中的运行时崩溃和未定义行为。
- [使用 Instruments 分析 HTTP 流量](../foundation/analyzing-http-traffic-with-instruments.md) — 测量 App 基于 HTTP 的网络性能和使用情况。
