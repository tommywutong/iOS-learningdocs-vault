---
title: iCloud
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/icloud
source_url: 'https://developer.apple.com/documentation/foundation/icloud'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/icloud.json'
content_hash: 'sha256:2c0724457c1f3ec4'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md)

# iCloud

<sub>API 集合</sub>

管理在用户的 iCloud 设备之间自动同步的文件和键值数据。

## 主题

### iCloud 存储

- [FileManager](filemanager.md) — 访问文件系统内容的便捷接口，也是与文件系统交互的主要方式。
- [FileManagerDelegate](filemanagerdelegate.md) — 文件管理器的委托用来在操作期间介入或在发生错误时使用的接口。

### App 偏好设置

- [Synchronizing App Preferences with iCloud](synchronizing-app-preferences-with-icloud.md) — 将 App 偏好设置存储在 iCloud 中，并在用户已连接设备上运行的 App 实例之间共享它们。
- [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) — 一个基于 iCloud 的键值对容器，你可以在用户设备上运行的 App 实例之间共享它。

### 文件搜索

- [NSMetadataQuery](nsmetadataquery.md) — 一个针对 Spotlight 元数据执行的查询。
- [NSMetadataQueryDelegate](nsmetadataquerydelegate.md) — 使元数据查询的委托能够提供替代结果或属性的接口。
- [NSMetadataItem](nsmetadataitem.md) — 与文件关联的元数据。

### Entitlement

- [com.apple.developer.icloud-container-development-container-identifiers](../bundleresources/entitlements/com.apple.developer.icloud-container-development-container-identifiers.md) — iCloud 开发环境的容器标识符。
- [com.apple.developer.icloud-container-environment](../bundleresources/entitlements/com.apple.developer.icloud-container-environment.md) — iCloud 容器要使用的开发环境或生产环境。
- [iCloud Container Identifiers Entitlement](../bundleresources/entitlements/com.apple.developer.icloud-container-identifiers.md) — iCloud 生产环境的容器标识符。
- [iCloud Services Entitlement](../bundleresources/entitlements/com.apple.developer.icloud-services.md) — App 使用的 iCloud 服务。
- [iCloud Key-Value Store Entitlement](../bundleresources/entitlements/com.apple.developer.ubiquity-kvstore-identifier.md) — 用于 iCloud 键值存储的容器标识符。

### 错误

- [iCloud Error Codes](icloud-error-codes.md) — 发生 iCloud 相关错误时会出现的错误代码。

## 另请参阅

### 文件与数据持久化

- [File System](file-system.md) — 在文件系统中创建、读取、写入和检查文件与文件夹。
- [Archives and Serialization](archives-and-serialization.md) — 将对象和值与属性列表、JSON 以及其他扁平二进制表示形式相互转换。
- [Settings](settings.md) — 使用你存储在本地磁盘或 iCloud 中的持久化数据来配置你的 App。
- [Spotlight](spotlight.md) — 在本地设备上搜索文件和其他项目，并为你的 App 内容建立索引以供搜索。
- [Optimizing Your App’s Data for iCloud Backup](optimizing-your-app-s-data-for-icloud-backup.md) — 通过将可清除和不可清除的数据排除在备份之外，最大限度地减少创建备份所占用的空间和时间。
</content>
