---
title: 消息参数格式化器
framework: os
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/os/message-argument-formatters
source_url: 'https://developer.apple.com/documentation/os/message-argument-formatters'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/message-argument-formatters.json'
content_hash: 'sha256:2d9fad35ffcd0750'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md) · [Logging](logging.md)

# 消息参数格式化器

<sub>API 集合</sub>

使用类型感知的格式化器管理消息插值内容的隐私性和呈现方式。

## 主题

### 隐私选项

- [OSLogPrivacy](oslogprivacy.md) — 决定何时在日志消息中隐去或显示值的隐私选项。

### 值格式化器

- [OSLogBoolFormat](oslogboolformat.md) — 布尔值的格式化选项。
- [OSLogIntegerFormatting](oslogintegerformatting.md) — 整数值的格式化选项。
- [OSLogInt32ExtendedFormat](oslogint32extendedformat.md) — 32 位整数值的格式化选项。
- [OSLogFloatFormatting](oslogfloatformatting.md) — double 和浮点数的格式化选项。
- [OSLogPointerFormat](oslogpointerformat.md) — 指针数据的格式化选项。

### 值插值

- [OSLogInterpolation](osloginterpolation.md) — 日志消息各元素的容器。
- [OSLogIntExtendedFormat](oslogintextendedformat.md) — 在日志记录期间展开以 int 存储的比特率信息的选项。

### 字符串对齐

- [OSLogStringAlignment](oslogstringalignment.md) — 插值字符串的对齐选项。

## 另请参阅

### 日志消息

- [Logger](logger.md) — 用于向统一日志系统写入插值字符串消息的对象。
- [OSLogType](oslogtype.md) — 统一日志系统提供的各种日志级别。
