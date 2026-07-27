---
title: 文件系统
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/file-system
source_url: 'https://developer.apple.com/documentation/foundation/file-system'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/file-system.json'
content_hash: 'sha256:98937dab9c82890c'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md)

# 文件系统

<sub>API 集合</sub>

在文件系统中创建、读取、写入和检查文件与文件夹。

## 主题

### 文件系统操作

- [访问文件系统时提升性能与稳定性](improving-performance-and-stability-when-accessing-the-file-system.md) — 以协调、异步的方式与文件系统交互，并避免不必要的磁盘 I/O，从而防止数据丢失和 App 崩溃。
- [有效使用文件系统](using-the-file-system-effectively.md) — 使用系统提供的专用目录，获得自动备份或清除等好处。
- [FileManager](filemanager.md) — 一个便捷的文件系统内容接口，也是与文件系统交互的主要方式。
- [FileManagerDelegate](filemanagerdelegate.md) — 文件管理器委托（delegate）用来在操作期间或发生错误时进行干预的接口。
- [关于 Apple File System](about-apple-file-system.md) — 使用高级 API 充分发挥 Apple File System 的作用。

### 协调式文件访问

- [NSFilePresenter](nsfilepresenter.md) — 文件协调器用于向呈现文件的对象告知系统中其他位置对该文件所做更改的接口。
- [NSFileAccessIntent](nsfileaccessintent.md) — 协调式读取或协调式写入操作的详细信息。
- [NSFileCoordinator](nsfilecoordinator.md) — 在多个文件呈现方之间协调文件和目录读写的对象。

### 托管式文件访问

- [FileHandle](filehandle.md) — 文件描述符的面向对象包装器。
- [NSFileSecurity](nsfilesecurity.md) — 封装文件安全信息的存根类。
- [NSFileVersion](nsfileversion.md) — 文件在特定时间点的快照。
- [FileWrapper](filewrapper.md) — 文件系统中节点（文件、目录或符号链接）的表示。

### 错误

- [文件系统错误码](file-system-error-codes.md) — 识别文件系统操作生成的常见错误码。

## 另请参阅

### 文件与数据持久化

- [归档与序列化](archives-and-serialization.md) — 在对象和值与属性列表、JSON 和其他扁平二进制表示之间进行转换。
- [设置](settings.md) — 使用持久存储在本地磁盘或 iCloud 中的数据配置你的 App。
- [聚焦](spotlight.md) — 搜索本地设备上的文件和其他项目，并为 App 内容创建索引以供搜索。
- [iCloud](icloud.md) — 管理在用户的 iCloud 设备之间自动同步的文件和键值数据。
- [为 iCloud 备份优化 App 数据](optimizing-your-app-s-data-for-icloud-backup.md) — 从备份中排除可清除和不可清除数据，尽量减少备份占用的空间和创建时间。
