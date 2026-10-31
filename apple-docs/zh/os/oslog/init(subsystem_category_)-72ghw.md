---
title: 'init(subsystem:category:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslog/init(subsystem:category:)-72ghw'
source_url: 'https://developer.apple.com/documentation/os/oslog/init(subsystem:category:)-72ghw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslog/init%28subsystem%3Acategory%3A%29-72ghw.json'
content_hash: 'sha256:cde7a60cab768fbb'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLog](../oslog.md)

# init(subsystem:category:)

<sub>初始化方法</sub>

使用指定的子系统和系统定义的分类创建日志。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(subsystem: String, category: OSLog.Category)
```

## 参数

- `subsystem` — 采用反向 DNS 表示法的标识符字符串，表示正在执行日志记录的子系统，例如 `com.your_company.your_subsystem_name`。日志系统使用此信息对相关日志消息进行分类和过滤。

- `category` — 指定子系统内的一个系统定义分类。系统使用此值对相关日志消息进行分类和过滤。分类的日志记录设置会覆盖其所属子系统的设置。

## 返回值

一个自定义日志对象，你可以把它传给其他日志记录函数以执行日志记录，并判断特定级别的日志记录是否处于启用状态。

## 另请参阅

### 创建日志

- [init(subsystem:category:)](<init(subsystem_category_)-17gyy.md>) — 使用指定的子系统和分类创建日志。
- [Category](category.md) — 标识你的 App 中已知部分的系统定义分类。
