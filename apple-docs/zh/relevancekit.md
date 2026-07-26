---
title: RelevanceKit
framework: RelevanceKit
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/relevancekit
source_url: 'https://developer.apple.com/documentation/relevancekit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/relevancekit.json'
content_hash: 'sha256:644ffa6721350e8d'
translated: true
---

> 导航：[Technologies](technologies.md)

# RelevanceKit

<sub>框架</sub>

通过设备端智能提供上下文线索，提高你的小组件在 Apple Watch 上的可见性。

## 概述

在 Apple Watch 上，小组件会以最适合个人当前情境的顺序出现在智能叠放中。为了给智能叠放里出现的小组件排序，watchOS 会尝试根据多种因素来判定小组件的相关性，其中就包括你的 App 向系统提供的上下文线索。

若想让你的小组件在 watchOS 智能叠放中获得更高的可见性，并确保它在用户需要时出现，可使用 RelevanceKit 来提供表明该小组件相关性的上下文线索。例如，你的小组件可能在特定地点或时间最有用，或者每次用户开始锻炼时最有用。

请注意，你需要将 RelevanceKit 与 [WidgetKit](widgetkit.md) 和 [App Intents](appintents.md) 结合使用，以便在智能叠放中提供可交互且与上下文相关的小组件，其中也包括出现在 Apple Watch 上的 iPhone 小组件。当你在代码中为 App Intents 添加 import 语句时，App Intents 会隐式添加对 RelevanceKit 的依赖。你不需要在代码中显式添加 `import RelevanceKit`。

更多信息请参阅 [Increasing the visibility of widgets in Smart Stacks](widgetkit/widget-suggestions-in-smart-stacks.md)。

> [!note] 注意
> 智能叠放在 iOS、iPadOS 和 watchOS 上均可使用。但 RelevanceKit 提供的功能仅在 watchOS 上可用。在其他平台上调用其 API 不会产生任何效果。

## 主题

### 提供相关性信息

- [Increasing the visibility of widgets in Smart Stacks](widgetkit/widget-suggestions-in-smart-stacks.md) — 向系统提供上下文信息并捐赠意图，确保你的小组件在智能叠放中显眼地出现。
- [RelevantContext](relevancekit/relevantcontext.md) — 系统用于在 watchOS 智能叠放中展示相关小组件的上下文线索。

### 健身线索

- [fitness(_:)](<relevancekit/relevantcontext/fitness(__).md>) — 根据用户的健身活动告知系统某个小组件是相关的。
- [FitnessCondition](relevancekit/relevantcontext/fitnesscondition.md) — 表示用户健身活动的值。

### 硬件线索

- [hardware(headphones:)](<relevancekit/relevantcontext/hardware(headphones_).md>) — 在用户的耳机已连接时告知系统某个小组件是相关的。
- [HeadphonesCondition](relevancekit/relevantcontext/headphonescondition.md) — 表示用户耳机是否已连接的结构体。

### 位置线索

- [location(_:)](<relevancekit/relevantcontext/location(__).md>) — 在特定位置告知系统某个小组件是相关的。
- [location(inferred:)](<relevancekit/relevantcontext/location(inferred_).md>) — 在用户的推断位置告知系统某个小组件是相关的。
- [InferredLocation](relevancekit/relevantcontext/inferredlocation.md) — 包含用户推断的住所、工作地点、学校和通勤地点值的结构体。

### 睡眠线索

- [sleep(_:)](<relevancekit/relevantcontext/sleep(__).md>) — 根据用户的睡眠时间表告知系统某个小组件是相关的。
- [SleepCondition](relevancekit/relevantcontext/sleepcondition.md) — 表示用户通常就寝或起床时间的值。

### 时间线索

- [date(_:)](<relevancekit/relevantcontext/date(__).md>) — 在特定日期告知系统某个小组件是相关的。
- [date(_:kind:)](<relevancekit/relevantcontext/date(__kind_).md>) — 在特定日期告知系统某个小组件是相关的，并提供额外的上下文提示。
- [date(interval:kind:)](<relevancekit/relevantcontext/date(interval_kind_).md>) — 在某个时间间隔内告知系统某个小组件是相关的，并提供额外的上下文提示。
- [date(range:kind:)](<relevancekit/relevantcontext/date(range_kind_).md>) — 在已知日期范围内告知系统某个小组件是相关的，并提供额外的上下文提示。
- [DateKind](relevancekit/relevantcontext/datekind.md) — 系统用作基于时间的相关性线索附加上下文的值。
- [date(from:to:)](<relevancekit/relevantcontext/date(from_to_).md>) — 在两个日期之间告知系统某个小组件是相关的。_(已废弃)_
