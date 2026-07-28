---
title: 优化 App 数据以进行 iCloud 备份
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/optimizing-your-app-s-data-for-icloud-backup
source_url: 'https://developer.apple.com/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/optimizing-your-app-s-data-for-icloud-backup.json'
content_hash: 'sha256:de1a43b52f6c2c49'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 优化 App 数据以进行 iCloud 备份

<sub>文章</sub>

通过从备份中排除可清除数据（purgeable data）和不可清除数据（nonpurgeable data），尽量减少创建备份所需的空间和时间。

## 概述

启用 iCloud 云备份后，它会定期创建用户设备的备份，其中包括你的 App 数据。通过将可清除数据存储在特定目录中，并向系统指示备份可以排除某些不可清除数据，你可以缩短创建备份所需的时间，并帮助减少备份占用的空间。

### 排除可清除数据

_可清除数据_ 是系统可以删除而不影响 App 运行、并且 App 可以在需要时重新创建的数据。例如，你的 App 可能会为较大的图像生成缩略图，以便在集合视图（collection view）中显示。如果 App 将缩略图保存到磁盘，应将其视为可清除数据，因为系统删除这些文件后，App 可以根据源文件重新创建它们。

App 容器提供两个用于存储可清除数据的目录：

- `/tmp`
- `/Library/Caches`

系统会定期清除这些目录，因此 iCloud 云备份默认会排除它们。如果你的 App 创建可清除数据，请将其存储在其中一个目录中；否则，iCloud 云备份可能会纳入这些数据，无谓地增加备份的物理大小，而不会给用户带来任何好处。不要使用这些目录来从 iCloud 云备份中排除不可清除数据。

要获取这些系统提供的目录的位置，请使用 [FileManager](filemanager.md) 类，如下例所示。

```swift
let manager = FileManager.default

// 获取 App 容器中 'tmp' 目录的 URL。
let tmpDirectoryURL = manager.temporaryDirectory

// 获取 App 容器中 'Caches' 目录的 URL。
let cachesDirectoryURL = try manager.url(for: .cachesDirectory,
                                         in: .userDomainMask,
                                         appropriateFor: nil,
                                         create: false)
```

考虑在 App 使用完可清除数据后立即将其删除，以免这些数据继续占用用户设备上的空间。

### 将不可清除数据标记为可排除

_不可清除数据_ 是用户创建的数据，或 App 按用户预期运行所必需的数据。某些不可清除数据并不适合备份。

例如，如果你的 App 下载高清影片供离线观看，应排除这些文件，因为它们通常很大，而且用户可以在恢复后的设备上按需重新下载。相反，如果你的 App 允许用户导入 PDF、电子书和数字漫画等任意文件，则不要排除这些文件，因为用户可能很难甚至无法在恢复后的设备上重新创建它们。

如果你的 App 创建了不适合备份的不可清除数据，可以将相应文件和目录的 [isExcludedFromBackup](urlresourcevalues/isexcludedfrombackup.md) 资源值设为 [true](../swift/true.md)，指示系统可以排除哪些内容，如下例所示。

```swift
func excludeItem(at url: URL) throws {
    // 为指定 URL 创建资源值。
    var values = URLResourceValues()
    values.isExcludedFromBackup = true

    // 将这些值应用到 URL。
    var url = url
    try url.setResourceValues(values)
}
```

> [!note] 注意
> 由于某些文件操作可能会重置资源值，请确保每次保存已排除的文件时都设置其资源值。

[isExcludedFromBackup](urlresourcevalues/isexcludedfrombackup.md) 资源值只用于向系统提供可以排除哪些文件和目录的指导；它无法保证这些项目永远不会出现在备份中或恢复后的设备上。

要指示系统可以从 iCloud 云备份中排除一组相关文件，请将这些文件移入一个目录，并更新该目录的 [isExcludedFromBackup](urlresourcevalues/isexcludedfrombackup.md) 资源值。如果你在 App 容器的 `Library` 目录中创建可排除的目录，可考虑使用 App 的套装标识符为该目录命名，以免与系统将来可能在此创建的目录发生冲突。

```swift
let manager = FileManager.default

// 获取 App 的套装标识符。
if let bundleIdentifier = Bundle.main.bundleIdentifier {
    
    // 获取 App 容器中 'Library' 目录的 URL。
    var url = try manager.url(for: .libraryDirectory,
                              in: .userDomainMask,
                              appropriateFor: nil,
                              create: false)
    
    // 将套装标识符附加到获取的 URL。
    url.appendPathComponent(bundleIdentifier, isDirectory: true)
    
    // 使用该 URL 创建新目录。
    try manager.createDirectory(at: url,
                                withIntermediateDirectories: true,
                                attributes: nil)
}
```

## 另请参阅

### 文件与数据持久化

- [文件系统](file-system.md) — 在文件系统中创建、读取、写入和检查文件及文件夹。
- [归档（archives）与序列化](archives-and-serialization.md) — 在对象和值与属性列表、JSON 及其他平面二进制表示之间进行转换。
- [设置](settings.md) — 使用持久存储在本地磁盘或 iCloud 中的数据配置你的 App。
- [聚焦](spotlight.md) — 搜索本地设备上的文件和其他项目，并为你的 App 内容建立索引以供搜索。
- [iCloud](icloud.md) — 管理会在用户的 iCloud 设备之间自动同步的文件和键值数据。
