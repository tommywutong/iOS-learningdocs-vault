---
title: 有效使用文件系统
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/using-the-file-system-effectively
source_url: 'https://developer.apple.com/documentation/foundation/using-the-file-system-effectively'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/using-the-file-system-effectively.json'
content_hash: 'sha256:7508aa3e61aea51f'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [文件系统](file-system.md)

# 有效使用文件系统

<sub>文章</sub>

通过使用系统提供的专用目录，获得自动备份或清除等优势。

## 概述

App 持久化数据时，通常会根据不同目的使用不同的文件。例如，当用户使用你的 App 创建文稿时，App 会永久存储该文稿，并使其可用于自动备份。你的 App 可能还会创建运行所必需的文件，但这些文件在用户使用 App 时不可见。还有一些其他类型的文件可能在某个时间段内有用，但最终可以被删除。Foundation 为不同类型的文件提供了特殊的目录，其中一些目录提供了独特的行为，可以帮助你的 App 更高效地存储文件。

通过审慎管理文件系统资源的使用，你可以避免浪费空间，从而带来以下好处：

- 你的 App 不会因为空间不足而阻止系统执行更新。
- 在系统更新期间，你的 App 被删除并重新下载的可能性降低。
- 你的 App 被用户删除以释放存储空间的可能性降低。
- 你的 App 受益于更小、更快的备份。

此外，将正确的文件放入正确的目录还能提供有用的功能，如自动备份或清除。

> [!tip] 提示
> 如果你需要持久化的数据非常小——几个字符串或名称-值对——你可能会发现使用 [UserDefaults](userdefaults.md) 比管理平面文件更方便。

### 访问常用目录

在 iOS、tvOS、watchOS 和 visionOS 上，App 在其 bundle 内执行所有文件访问。除了在更高层级的 API 代表 App 访问外部文件的情况下（例如使用 [Media Player](../mediaplayer.md) 播放设备音乐库中的歌曲），不能访问 bundle 外部的文件。沙盒化的 macOS App 也使用类似的设置。

在 bundle 内，系统提供了特定的目录，其中一些具有不同的行为，例如备份或定期清除文件。使用 [URL](url.md) 和 [FileManager](filemanager.md) 类型的方法和属性来访问这些目录：

- 在 Swift 中，[URL](url.md) 为常用目录定义了属性，例如 [documentsDirectory](url/documentsdirectory.md)、[cachesDirectory](url/cachesdirectory.md)、[temporaryDirectory](url/temporarydirectory.md) 等。每个属性都是一个单一的、非可选值（nonoptional）的 [URL](url.md) 实例，你可以与 [FileManager](filemanager.md) 一起使用。
- 在 Swift 或 Objective-C 中，你可以使用 [FileManager](filemanager.md) 方法 [- URLsForDirectory:inDomains:](<filemanager/urls(for_in_).md>) 来访问常用目录。`for` 参数接受 [SearchPathDirectory](filemanager/searchpathdirectory.md) 类型，该类型定义了用于搜索常用目录的常量，例如 [NSDocumentDirectory](filemanager/searchpathdirectory/documentdirectory.md) 和 [NSCachesDirectory](filemanager/searchpathdirectory/cachesdirectory.md)。

尽可能使用这些 API。不要硬编码看似是常用目录的路径，因为像访达这样的 App 可能会在用户界面中本地化目录名称并省略文件扩展名。

### 存储长期文件

在使用 [UIDocument](../uikit/uidocument.md) 和 [NSDocument](../appkit/nsdocument.md) 等 API 编写基于文稿的 App 时，将文件存储在 `Documents` 文件夹中。你可以使用 URL [documentsDirectory](url/documentsdirectory.md) 或搜索路径 [NSDocumentDirectory](filemanager/searchpathdirectory/documentdirectory.md) 访问此文件夹。

即使你不使用 [UIDocument](../uikit/uidocument.md) 或 [NSDocument](../appkit/nsdocument.md) API，也可以将此文件夹用于用户管理的其他文件。

当通过 USB 线缆将 iOS 设备连接到 macOS 电脑，或执行 iCloud 备份时，系统会备份 `Documents` 文件夹中的文件。系统还可以使 `Documents` 文件夹的内容可用于文件共享。只在此文件夹中存储你想要暴露给用户的文件。

此外，当你在 iOS App 的 `Documents` 文件夹中存储文件时，这些文件也会在系统的“文件”App 中可见。

对于 App 运行所需但你不想公开可见的支持文件，建议使用 `ApplicationSupport` 目录，方法是使用 URL 属性 [applicationSupportDirectory](url/applicationsupportdirectory.md) 或搜索路径 [NSApplicationSupportDirectory](filemanager/searchpathdirectory/applicationsupportdirectory.md)。此目录存储诸如配置文件、模板以及 bundle 中默认文件的修改版本等数据。系统也会将此文件夹的内容作为常规备份的一部分。

> [!important] 重要
> 如果你想将 `Documents` 或 `ApplicationSupport` 中的某个项目排除在备份之外，请在 Swift 中使用值 [isExcludedFromBackup](urlresourcevalues/isexcludedfrombackup.md) 调用 [setResourceValues(_:)](<url/setresourcevalues(__).md>)，或在 Objective-C 中使用键 [NSURLIsExcludedFromBackupKey](urlresourcekey/isexcludedfrombackupkey.md) 调用 [- setResourceValue:forKey:error:](<nsurl/setresourcevalue(__forkey_).md>)。将你的 App 可以重新创建或重新下载的任何文件（尤其是大型媒体文件）排除在备份之外。

### 存储短期文件

你的 App 也可能使用生命周期更短的文件，这些文件不需要备份或永久存储。Foundation 提供了几个用于存储这些类型文件的目录。

使用 URL 属性 [temporaryDirectory](url/temporarydirectory.md) 和文件管理器属性 [temporaryDirectory](filemanager/temporarydirectory.md) 访问临时目录。将此目录用于生命周期短的文件，例如计算操作的副作用，或一次性下载且使用后可丢弃的文件。

只将临时目录用于不需要在 App 启动之间持久化的文件，因为系统可能会在 App 未运行时清除此目录。然而，系统不保证何时或是否会清除该目录，因此一旦确认不再需要临时文件，就应立即删除。

对于持久化时间比临时文件长，但仍然可被清除的文件，请使用**缓存**目录。在缓存目录中，存储 App 运行所不需要、但能提高性能的文件，例如数据库缓存文件和临时可下载内容。

使用 URL 属性 [cachesDirectory](url/cachesdirectory.md) 或文件管理器搜索路径 [NSCachesDirectory](filemanager/searchpathdirectory/cachesdirectory.md) 访问缓存目录。与临时目录一样，系统可能会在 App 未运行时清除此目录。你的 App 需要能够在没有这些文件的情况下运行，或者根据需要重新生成它们。此外，尽可能使缓存文件失效（invalidate）并删除它们，不要在不必要的文件上浪费存储空间。

系统不会备份临时目录或缓存目录。

下面的决策树总结了选择存储目录时需要考虑的因素，以及这些目录对应的 [URL](url.md) 常量。

![](../../../attachments/83778edc2ff98e6e2f0b37fe988744a6/storage-usage-best-practices-decision-flow@2x.png)

<sub>一个从左到右阅读的决策树示意图。第一个决策点写着“你的文件是长期的吗？”。“是”的答案指向另一个决策点：“谁管理这个文件？”</sub>

### 在非沙盒化 macOS App 中访问文件系统其余部分

非沙盒化的 macOS App 可以访问其自身容器外部的文件。这个能力对于需要读取和写入文件系统其他位置的 App 很有用。

> [!tip] 提示
> 要使用沙盒化 macOS App 容器外部的文件，请参阅[从 macOS App 沙盒访问文件](../security/accessing-files-from-the-macos-app-sandbox.md)。

当 macOS App 未沙盒化时，[URL](url.md) 中的常用目录属性会提供不同的值。例如，在非沙盒化 macOS App 中，[applicationSupportDirectory](url/applicationsupportdirectory.md) 是“`~/Library/Application Support`”，[cachesDirectory](url/cachesdirectory.md) 是“`~/Library/Caches`”。当使用带有 [NSApplicationSupportDirectory](filemanager/searchpathdirectory/applicationsupportdirectory.md) 和 [NSCachesDirectory](filemanager/searchpathdirectory/cachesdirectory.md) 等搜索路径常量的 [- URLsForDirectory:inDomains:](<filemanager/urls(for_in_).md>) 时，这种值差异同样适用。

## 另请参阅

### 文件系统操作

- [提高访问文件系统时的性能和稳定性](improving-performance-and-stability-when-accessing-the-file-system.md) — 通过以协调、异步的方式与文件系统交互并避免不必要的磁盘 I/O，来防止数据丢失和 App 崩溃。
- [FileManager](filemanager.md) — 访问文件系统内容的便捷接口，也是与之交互的主要方式。
- [FileManagerDelegate](filemanagerdelegate.md) — 文件管理器的委托（delegate）用于在操作期间或发生错误时进行干预的接口。
- [关于 Apple 文件系统](about-apple-file-system.md) — 使用高级 API 来充分利用 Apple 文件系统。
