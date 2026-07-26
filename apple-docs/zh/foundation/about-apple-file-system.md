---
title: 关于 Apple File System
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/about-apple-file-system
source_url: 'https://developer.apple.com/documentation/foundation/about-apple-file-system'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/about-apple-file-system.json'
content_hash: 'sha256:c275ae0bbb2a19da'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [File System](file-system.md)

# 关于 Apple File System

<sub>文章</sub>

使用高级 API 充分发挥 Apple File System 的优势。

## 概述

在 iOS 10.3 及更高版本、以及 macOS High Sierra 及更高版本中，Apple File System 取代 HFS Plus 成为默认的文件系统。Apple File System 不仅改进了文件系统的基础能力，还提供了若干新特性，包括克隆、快照、空间共享、快速目录大小计算、原子安全保存和稀疏文件。

使用 Foundation 中的高级 API（例如 [FileManager](filemanager.md) 和 [FileHandle](filehandle.md)）与文件交互时，会自动利用 Apple File System 提供的这些新行为，而无需修改你的代码。

如果你需要在不使用任何框架或操作系统的情况下直接与文件系统交互，请阅读 [Apple File System Reference](https://developer.apple.com/go/?id=apfs-file-format-spec)。

### 克隆可降低复制成本

克隆是文件或目录的一个副本，它不会在磁盘上占用额外的空间。借助克隆，你可以在同一个卷上快速、节能地复制文件。[FileManager](filemanager.md) 的 [- copyItemAtURL:toURL:error:](<filemanager/copyitem(at_to_).md>) 和 [- copyItemAtPath:toPath:error:](<filemanager/copyitem(atpath_topath_).md>) 方法会针对 Apple File System 卷自动创建克隆，如下方代码所示。

```swift
let origin = URL(fileURLWithPath: "/path/to/origin")
let destination = URL(fileURLWithPath: "/path/to/destination")
do {
    // Creates a clone for Apple File System volumes, or makes
    // a copy immediately for other file systems.
    try FileManager.default.copyItem(at: origin, to: destination)
} catch {
    // ... Handle the error ...
}
```

对数据的修改会写入到其他位置，而两个文件会继续共享未被修改的数据块。举例来说，你可以利用这一行为来减少文稿修订版本和副本所需的存储空间。下图展示了一个名为“My file”的文件及其副本“My file copy”，它们有两个共同的数据块，以及一个两者不同的数据块。在 HFS Plus 之类的文件系统上，两者各自都需要三个磁盘数据块，但在 Apple File System 卷上，这两个共同的数据块是共享的。

![](../../../attachments/27b2bfeee815b6f57e42c609f653edfa/media-2991758@2x.png)

### 各个卷之间共享可用空间

许多文件系统（包括 HFS Plus）每个分区只支持一个卷。由于可用空间无法在各分区之间共享，因此每个卷的大小在对存储设备分区时就已确定，且每个卷只能在其可用空间内增长。相比之下，Apple File System 支持在单个分区内容纳多个卷，从而使这些卷都能共享可用空间。同一 Apple File System 分区内的所有卷都可以独立增长和缩小；某个卷缩小时释放出的空间，可以供另一个卷增长时使用。

![](../../../attachments/252b67dfdb6ad872f88aec6c8fa47ca2/media-3001372@2x.png)

容器中的每个卷都可以使用共享的可用空间，因此在报告可用空间时，它们都会把这部分空间计算在内。举例来说，当你调用 [FileManager](filemanager.md) 的 [- attributesOfFileSystemForPath:error:](<filemanager/attributesoffilesystem(forpath_).md>) 方法时，所报告的数值会包含全部共享的可用空间。

```swift
if let attributes = try? FileManager.default.attributesOfFileSystem(forPath: "/") {
    let availableFreeSpace = attributes[.systemFreeSize] 
}
```

计算各个卷可用空间的总和，并不是确定某个分区总可用空间的可靠方法。通常情况下，应检查执行某项特定操作所需的空间在该卷上是否可用，而不是尝试计算该分区的总可用空间。

### 稀疏文件不会为空白数据块分配空间

在支持稀疏文件的文件系统（包括 Apple File System）中，只有当磁盘数据块被实际写入时，才会为其分配空间。这一行为使得包含空白区段的文件（例如磁盘映像和数据库转储）能够更高效地保存在磁盘上。

当你使用 [FileHandle](filehandle.md) 类创建一个新的写入句柄时，系统会自动创建一个稀疏文件。举例来说，如果你写入一个数据块，然后调用 [- seekToFileOffset:](<filehandle/seek(tofileoffset_).md>) 跳过一个数据块，再写入另一个数据块，那么存储在磁盘上的数据组织方式如下：

![](../../../attachments/c665c832bc9bddb8d859d4c44b40eeaf/media-2991755@2x.png)

HFS Plus 以及其他不支持稀疏文件的格式会为该文件分配三个数据块——每个被写入的数据块各一个，中间还有一个空白数据块。而在支持稀疏文件的情况下，只会分配两个数据块，中间的空白数据块会被省略。

由于上述 Apple File System 示例中的稀疏文件在磁盘上并不包含空白的第二个数据块，后续再向第二个数据块写入时，就会导致数据块顺序错乱，如下图所示。像 [FileHandle](filehandle.md) 这样的高级 API 会替你处理这种碎片化，而碎片化造成的性能损失通常并不显著。

![](../../../attachments/1264e600bdc2cf31e25eecf92c104409/media-2991757@2x.png)

你无法使用 [FileHandle](filehandle.md)，从磁盘上已经存有空白数据的现有文件创建稀疏文件。

## 另请参阅

### File system operations

- [访问文件系统时提升性能和稳定性](improving-performance-and-stability-when-accessing-the-file-system.md) — 通过以协调、异步的方式与文件系统交互，并避免不必要的磁盘 I/O，防止数据丢失和 App 崩溃。
- [有效地使用文件系统](using-the-file-system-effectively.md) — 通过使用系统提供的专用目录，获得自动备份或清理等好处。
- [FileManager](filemanager.md) — 一个访问文件系统内容的便捷接口，也是与之交互的主要方式。
- [FileManagerDelegate](filemanagerdelegate.md) — 文件管理器的委托在操作期间或发生错误时用于介入的接口。
