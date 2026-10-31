---
title: OSLog
framework: os
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslog
source_url: 'https://developer.apple.com/documentation/os/oslog'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog.json'
content_hash: 'sha256:b3a1685a1ad34cdd'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSLog

<sub>类</sub>

相关日志消息的容器。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class OSLog
```

## 概述

日志会对你写入的消息进行分类，便于排序和过滤。每个日志都包含你定义的子系统和分类。子系统标识你的 App 的某个较大功能区域，使用反向 DNS 表示法指定，例如 `com.your_company.your_subsystem_name`。分类用于在子系统内区分具体领域。

## 关系

- **继承自**： [NSObject](../objectivec/nsobject-swift.class.md)

- **遵循**： [CVarArg](../swift/cvararg.md)、[Equatable](../swift/equatable.md)、[Hashable](../swift/hashable.md)、[NSObjectProtocol](../objectivec/nsobjectprotocol.md)、[Sendable](../swift/sendable.md)、[SendableMetatype](../swift/sendablemetatype.md)

## 主题

### 创建日志

- [init(subsystem:category:)](<oslog/init(subsystem_category_)-17gyy.md>) — 使用指定的子系统和分类创建日志。
- [init(subsystem:category:)](<oslog/init(subsystem_category_)-72ghw.md>) — 使用指定的子系统和系统定义的分类创建日志。
- [Category](oslog/category.md) — 标识你的 App 中已知部分的系统定义分类。

### 获取共享日志

- [default](oslog/default.md) — 共享的默认日志。
- [disabled](oslog/disabled.md) — 共享的已禁用日志。

### 获取日志配置

- [os_log_type_enabled](<oslog/isenabled(type_).md>) — 返回一个布尔值，指示该日志是否可以写入指定日志类型的消息。
- [signpostsEnabled](oslog/signpostsenabled.md) — 一个布尔值，指示日志是否能够使用 signpost 日志记录。

## 另请参阅

### 创建 Logger

- [init()](<logger/init().md>) — 创建一个写入默认子系统的 logger。
- [init(subsystem:category:)](<logger/init(subsystem_category_).md>) — 使用指定的子系统和分类创建一个 logger。
- [init(_:)](<logger/init(__).md>) — 创建一个写入指定日志的 logger。
