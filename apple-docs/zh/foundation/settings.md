---
title: 设置
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/settings
source_url: 'https://developer.apple.com/documentation/foundation/settings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/settings.json'
content_hash: 'sha256:08870eaad1511716'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 设置

<sub>API 集合</sub>

使用持久存储在本地磁盘或 iCloud 中的数据配置你的 App。

## 概述

设置是用于配置 App 界面和行为的小块数据。你的代码无需在每次想要更改配置时重新编译，而是使用设置动态调整 App 的配置。通常，你会使用这类数据来反映 App 使用者的个人偏好。例如，绘图 App 可以存储用户更偏好以英寸还是厘米为距离测量单位。不过，你也可以使用设置来管理内部行为，例如 App 在测试期间记录的数据量。

系统会将每个 App 的设置持久存储到磁盘，以便在多次启动之间继续使用。通常你会将字符串、数值和其他简单数据类型存储到磁盘，但也可以按需存储更复杂的类型。[UserDefaults](userdefaults.md) 类型管理当前设备上你的 App 设置，但不会将这些设置与用户的其他设备共享。若要在用户所有设备上运行的 App 实例之间共享设置，请使用 [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) 类型将设置放入 iCloud。

## 主题

### App 专属设置

- [从代码访问设置](accessing-settings-from-your-code.md) — 在 App 运行时获取或更改设置，并监视这些值的外部更改。
- [UserDefaults](userdefaults.md) — 用户默认值数据库的接口，该数据库存储系统范围和 App 专属设置。

### 设置界面

- [向 App 添加设置界面](adding-a-settings-interface-to-your-app.md) — 创建专用界面来显示和修改 App 设置。
- [为 App 构建 Settings bundle](building-a-settings-bundle-for-your-app.md) — 将 App 的自定义设置集成到 iOS、iPadOS、tvOS 和 visionOS 的“设置”App 中，并支持 Mac Catalyst 设置窗口。

### iCloud 键值存储

- [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) — 一个基于 iCloud 的键值对容器，可在用户设备上运行的 App 实例之间共享。

## 另请参阅

### 文件与数据持久化

- [文件系统](file-system.md) — 在文件系统中创建、读取、写入和检查文件及文件夹。
- [归档（archives）与序列化](archives-and-serialization.md) — 在对象和值与属性列表、JSON 及其他平面二进制表示之间进行转换。
- [聚焦](spotlight.md) — 搜索本地设备上的文件和其他项目，并为你的 App 内容建立索引以供搜索。
- [iCloud](icloud.md) — 管理会在用户的 iCloud 设备之间自动同步的文件和键值数据。
- [优化 App 数据以进行 iCloud 备份](optimizing-your-app-s-data-for-icloud-backup.md) — 通过从备份中排除可清除和不可清除的数据，尽量减少创建备份所需的空间和时间。
