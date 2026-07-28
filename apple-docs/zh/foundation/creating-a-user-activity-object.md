---
title: 创建用户活动对象
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/creating-a-user-activity-object
source_url: 'https://developer.apple.com/documentation/foundation/creating-a-user-activity-object'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/creating-a-user-activity-object.json'
content_hash: 'sha256:7d7c40ebfdbf77a0'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [任务管理](task-management.md)

# 创建用户活动对象

<sub>文章</sub>

识别关键的用户交互，并包含用于日后恢复这些交互的信息。

## 概述

在人们可能想要日后继续、或在另一台设备上继续的关键时刻创建 [NSUserActivity](nsuseractivity.md) 对象，并将其注册到系统。例如，你可以在人们打开网页、播放歌曲或在你的 App 中执行重要任务时创建用户活动对象。你还可以使用这些对象提供更好的「聚焦」搜索结果。不过，用户活动对象并不用于跟踪 App 中的每项任务，也不适用于细小的编辑或次要更改。

创建 [NSUserActivity](nsuseractivity.md) 对象时，你需要指定一个用于标识活动类型的字符串。活动类型字符串通常采用反向 DNS 格式。例如，当用户打开网页时，你可以指定 `com.myCompany.myApp.OpenWebPage` 这样的活动字符串。通过在 App 的[信息属性列表](../bundleresources/information-property-list.md)文件中包含 [NSUserActivityTypes](../bundleresources/information-property-list/nsuseractivitytypes.md) 键，声明 App 支持的活动类型。系统使用该键中的信息来确定你的 App 能否处理给定的用户活动对象。

### 定义活动

定义用户活动对象时，请执行以下操作：

1. 使用适当的活动类型创建并初始化用户活动对象。（支持哪些活动类型由你定义。）
2. 设置用户活动对象的 [title](nsuseractivity/title.md)。
3. 启用以下一个或多个属性，以配置该对象适用的任务：[eligibleForHandoff](nsuseractivity/iseligibleforhandoff.md)、[eligibleForSearch](nsuseractivity/iseligibleforsearch.md) 和 [eligibleForPublicIndexing](nsuseractivity/iseligibleforpublicindexing.md)。
4. 配置此对象中与用户当前活动有关的属性。
5. 对于配置为可供搜索或公开建立索引的用户活动对象，请配置 [contentAttributeSet](nsuseractivity/contentattributeset.md)、[keywords](nsuseractivity/keywords.md) 或 [webpageURL](nsuseractivity/webpageurl.md) 属性，以便「聚焦」可以为该对象建立索引。
6. 调用 [- becomeCurrent](<nsuseractivity/becomecurrent().md>) 方法，将用户活动对象注册到系统。

### 将活动标识符与你的 App 关联

系统使用你的开发者 Team ID 来关联来自你 App 的用户活动对象。继续某项活动时，系统会查找支持给定活动类型、且与活动来源 App 具有相同开发者 Team ID 的 App。将活动对象与你的开发者 Team ID 绑定，可确保竞争对手的 App 无法截获你创建的活动。若要将 Team ID 与你的 App 关联，请通过 App Store 分发 App，或使用你的开发者 ID 为 App 签名。

## 另请参阅

### 活动共享

- [在你的 App 中实现 Handoff](implementing-handoff-in-your-app.md) — 直接创建、发送和接收用户活动。
- [使用 Handoff 继续用户活动](continuing-user-activities-with-handoff.md) — 定义并管理你 App 中哪些活动可以在设备之间继续。
- [通过基于用户活动的建议提高 App 使用率](increasing-app-usage-with-suggestions-based-on-user-activities.md) — 从 App 中捕获信息并将其作为主动建议展示在整个系统中，从而提供连续的用户体验。
- [支持创建快速备忘录](supporting-the-creation-of-quick-notes.md) — 支持创建包含你 App 内容的备忘录。
- [NSUserActivity](nsuseractivity.md) — 你的 App 在某一时刻状态的表示形式。
- [NSUserActivityDelegate](nsuseractivitydelegate.md) — 用户活动实例通过其向委托（delegate）通知更新的接口。
