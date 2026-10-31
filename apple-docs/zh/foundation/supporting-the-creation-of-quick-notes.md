---
title: 支持创建快速备忘录
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/supporting-the-creation-of-quick-notes
source_url: 'https://developer.apple.com/documentation/foundation/supporting-the-creation-of-quick-notes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/supporting-the-creation-of-quick-notes.json'
content_hash: 'sha256:5a4f27b4c798ced0'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [Task Management](task-management.md)

# 支持创建快速备忘录

<sub>文章</sub>

支持创建包含你 App 内容的备忘录。

## 概述

人们在 macOS 和 iOS 上使用快速备忘录，将 App 专属内容快速添加到「备忘录」App。当有人从你的 App 激活快速备忘录时，系统会显示一个用于创建备忘录内容的界面。如果你的 App 有一个配置得当的活动，系统还会在备忘录中包含指向该活动的链接。稍后查看备忘录的人可以使用该链接打开你的 App 并执行该活动。例如，某人在查看照片时激活快速备忘录，之后可以使用该链接再次查看那张照片。

### 用你的内容配置用户活动对象

App 可以使用 [NSUserActivity](nsuseractivity.md) 对象为快速备忘录提供初始内容。当你的 App 拥有当前活动对象时，快速备忘录系统会在新备忘录中添加指向该活动的链接。不过，只有当你的活动对象在其 [webpageURL](nsuseractivity/webpageurl.md)、[persistentIdentifier](nsuseractivity/persistentidentifier.md) 或 [targetContentIdentifier](nsuseractivity/targetcontentidentifier.md) 属性中提供了值时，系统才会创建此链接。系统依赖这些属性，因为它们通常包含能够长期留存的信息：

- [webpageURL](nsuseractivity/webpageurl.md) 属性包含一个采用 `https:` 方案的 URL。
- [persistentIdentifier](nsuseractivity/persistentidentifier.md) 属性包含活动对象的唯一标识符。
- [targetContentIdentifier](nsuseractivity/targetcontentidentifier.md) 属性包含你 App 内容某一部分的唯一标识符。

你提供的 URL 或标识符需要保持稳定和一致，以便你可以在不同设备上再次执行该活动。人们可以在他们的任何设备上查看备忘录，也可以与他人分享备忘录。如果你使用 URL，请考虑使用通用链接，为 App 中的项目提供一致的位置。如果你使用活动或内容标识符，请确保该标识符在你的 App 内唯一，但在用户的所有设备上都相同。如果内容的位置因任何原因发生变化，请妥善处理这一变化，自动导览到新位置。如果内容不再可用，请在 App 的界面中显示一条消息，告知用户内容已不可用。

除了为你的内容提供稳定的标识符外，还要在活动对象的 [title](nsuseractivity/title.md) 属性中提供一个描述性的名词短语。在显示备忘录时，「备忘录」App 会将该属性中的文本用作指向你项目的链接的一部分。请提供能够传达关于内容的有用信息的名词短语。例如，照片 App 可能会把查看照片活动的标题设置为类似「2025 年 12 月 28 日拍摄的照片」。

### 让你的活动对象保持最新

要让你的内容可用于快速备忘录，请调用活动对象的 [- becomeCurrent](<nsuseractivity/becomecurrent().md>) 方法。快速备忘录系统只从你 App 的当前活动对象中提取内容。你可以随时更改此对象，以反映 App 界面中的变化。例如，如果有人正在浏览条目目录，就在他们聚焦到不同条目时更改活动对象。如果你的 App 没有反映任何适合纳入备忘录的内容，可以通过调用当前活动对象的 [- resignCurrent](<nsuseractivity/resigncurrent().md>) 方法来清除它。

## 另请参阅

### 活动共享

- [Creating a user activity object](creating-a-user-activity-object.md) — 确定关键的用户交互，并包含用于在之后恢复它们的信息。
- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md) — 直接创建、发送和接收用户活动。
- [Continuing User Activities with Handoff](continuing-user-activities-with-handoff.md) — 定义并管理你 App 的哪些活动可以在设备之间继续。
- [Increasing App Usage with Suggestions Based on User Activities](increasing-app-usage-with-suggestions-based-on-user-activities.md) — 从 App 中捕获信息并将其作为主动建议展示在整个系统中，从而提供连续的用户体验。
- [NSUserActivity](nsuseractivity.md) — 你的 App 在某一时刻状态的表示形式。
- [NSUserActivityDelegate](nsuseractivitydelegate.md) — 用户活动实例通过其向委托通知更新的接口。
