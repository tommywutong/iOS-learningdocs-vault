---
title: OSLog.Category
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslog/category
source_url: 'https://developer.apple.com/documentation/os/oslog/category'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/category.json'
content_hash: 'sha256:02c961390bc06b3e'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# OSLog.Category

<sub>结构体</sub>

标识你的 App 中已知部分的系统定义分类。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Category
```

## 关系

- **遵循**： [Sendable](../../swift/sendable.md)、[SendableMetatype](../../swift/sendablemetatype.md)

## 主题

### 记录 Signpost

- [pointsOfInterest](category/pointsofinterest.md) — 用于记录 signpost 的分类。
- [dynamicStackTracing](category/dynamicstacktracing.md) — 用于动态堆栈追踪的分类。
- [dynamicTracing](category/dynamictracing.md) — 用于动态追踪的分类。

### 检查日志分类

- [rawValue](category/rawvalue.md) — 唯一标识日志分类的字符串。

## 另请参阅

### 创建日志

- [init(subsystem:category:)](<init(subsystem_category_)-17gyy.md>) — 使用指定的子系统和分类创建日志。
- [init(subsystem:category:)](<init(subsystem_category_)-72ghw.md>) — 使用指定的子系统和系统定义的分类创建日志。
