---
title: Foundation
framework: Foundation
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation
source_url: 'https://developer.apple.com/documentation/foundation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation.json'
content_hash: 'sha256:c8fe9df838099279'
translated: true
---

> 导航：[技术](technologies.md)

# Foundation

<sub>框架</sub>

访问基本数据类型、集合和操作系统服务，为你的 App 定义基础功能层。

## 概述

Foundation 框架为 App 和框架提供基础功能层，包括数据存储与持久化、文本处理、日期与时间计算、排序与筛选以及网络。macOS、iOS、watchOS 和 tvOS SDK 全程使用 Foundation 定义的类、协议和数据类型。

## 主题

### 基本原理

- [Numbers, Data, and Basic Values](foundation/numbers-data-and-basic-values.md) — 使用 Cocoa 中普遍采用的原始值和其他基础类型。
- [Strings and Text](foundation/strings-and-text.md) — 创建和处理 Unicode 字符串，使用正则表达式查找模式，并对文本执行自然语言分析。
- [Collections](foundation/collections.md) — 使用数组、字典、集合和专用集合来存储和迭代对象组或值组。
- [Dates and Times](foundation/dates-and-times.md) — 比较日期与时间，并执行日历和时区计算。
- [Units and Measurement](foundation/units-and-measurement.md) — 为数值标注物理维度，以便进行区域设置感知的格式化和相关单位间转换。
- [Data Formatting](foundation/data-formatting.md) — 在数值、日期、测量结果及其他值与适应区域设置的字符串表示形式之间进行转换。
- [Filters and Sorting](foundation/filters-and-sorting.md) — 使用谓词、表达式和排序描述符检查集合及其他服务中的元素。

### App 支持

- [Task Management](foundation/task-management.md) — 管理 App 的工作及其与 Handoff 和“快捷指令”等系统服务的交互方式。
- [Resources](foundation/resources.md) — 访问与你的 App 捆绑在一起的资源及其他数据。
- [Notifications](foundation/notifications.md) — 用于广播信息和订阅广播的设计模式。
- [App Extension Support](foundation/app-extension-support.md) — 管理 App 扩展与托管它的 App 之间的交互。
- [Errors and Exceptions](foundation/errors-and-exceptions.md) — 响应与 API 交互时出现的问题，并微调 App 以改善调试体验。
- [Scripting Support](foundation/scripting-support.md) — 允许用户使用 AppleScript 和其他自动化技术控制你的 App，或从 App 内运行脚本。

### 文件与数据持久化

- [File System](foundation/file-system.md) — 在文件系统中创建、读取、写入和检查文件及文件夹。
- [Archives and Serialization](foundation/archives-and-serialization.md) — 在对象和值与属性列表、JSON 及其他平面二进制表示之间进行转换。
- [Settings](foundation/settings.md) — 使用持久存储在本地磁盘或 iCloud 中的数据配置你的 App。
- [Spotlight](foundation/spotlight.md) — 搜索本地设备上的文件和其他项目，并为你的 App 内容建立索引以供搜索。
- [iCloud](foundation/icloud.md) — 管理会在用户的 iCloud 设备之间自动同步的文件和键值数据。
- [Optimizing Your App’s Data for iCloud Backup](foundation/optimizing-your-app-s-data-for-icloud-backup.md) — 通过从备份中排除可清除和不可清除的数据，尽量减少创建备份所需的空间和时间。

### 网络

- [URL Loading System](foundation/url-loading-system.md) — 使用标准互联网协议与 URL 交互并和服务器通信。
- [Bonjour](foundation/bonjour.md) — 在本地网络上公布服务以便于发现，或发现他人公布的服务。

### 低层实用工具

- [XPC](foundation/xpc.md) — 管理安全的进程间通信。
- [Object Runtime](foundation/object-runtime.md) — 获取对 Objective-C 基本功能、Cocoa 设计模式和 Swift 集成的底层支持。
- [Processes and Threads](foundation/processes-and-threads.md) — 管理 App 与宿主操作系统及其他进程的交互，并实现底层并发功能。
- [Streams, Sockets, and Ports](foundation/streams-sockets-and-ports.md) — 使用底层 Unix 功能管理文件、进程和网络之间的输入与输出。

### 参考

- [Foundation Enumerations](foundation/foundation-enumerations.md)
- [Foundation Data Types](foundation/foundation-data-types.md) — 本文档描述 Foundation 框架中的数据类型和常量。

### 类

- [ProgressManager](foundation/progressmanager.md) — 一个向用户传达指定任务正在进行中的进度的对象。_(beta)_
- [ProgressReporter](foundation/progressreporter.md) — ProgressReporter 是 ProgressManager 的包装器，携带关于 ProgressManager 的信息。_(beta)_

### 协议

- [NSPredicateValidating](foundation/nspredicatevalidating.md)

### 结构体

- [Subprogress](foundation/subprogress.md) — Subprogress 用于在两个 `ProgressManager` 实例之间建立父子关系。_(beta)_
