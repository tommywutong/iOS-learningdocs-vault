---
title: 通过访问文件系统提升性能与稳定性
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/improving-performance-and-stability-when-accessing-the-file-system
source_url: 'https://developer.apple.com/documentation/foundation/improving-performance-and-stability-when-accessing-the-file-system'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/improving-performance-and-stability-when-accessing-the-file-system.json'
content_hash: 'sha256:ac9e814f627958ff'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [File System](file-system.md)

# 通过访问文件系统提升性能与稳定性

<sub>文章</sub>

以协调、异步的方式与文件系统交互，并避免不必要的磁盘 I/O，从而防止数据丢失和 App 崩溃。

## 概述

设备的文件系统是所有正在运行的进程共享的资源。如果多个进程（或同一进程内的多个线程）同时尝试操作同一个文件，就可能发生数据损坏或丢失，你的 App 甚至可能崩溃。

要实现安全高效的文件访问，应避免在 App 的主线程上执行即时的文件 I/O。使用 [NSFileCoordinator](nsfilecoordinator.md) 来编排文件访问，优先选择文件相关 API 中免 I/O 的变体，并实现 [UICollectionView](../uikit/uicollectionview.md) 与 [UITableView](../uikit/uitableview.md) 的预取机制，以高效地为显示准备文件相关数据。

### 协调文件访问以减少挂起

_阻塞调用_ 是一种可能暂时挂起调用线程执行的任务，例如检查某个文件或目录是否存在。当阻塞调用源自 App 的主线程时，被挂起的执行会表现为用户界面挂起以及较高的滚动卡顿率，从而对用户体验造成负面影响。如果相关文件位于设备外部（例如存放在 iCloud Drive 或其他文件提供程序中，或是挂载的 USB 驱动器或 SMB 服务器上的文件），这种特定阻塞调用的持续时间往往是不确定的。

采用 [NSFileCoordinator](nsfilecoordinator.md) 与 [NSFilePresenter](nsfilepresenter.md) 来协调跨线程、跨进程的安全文件访问。当某个文件即将发生变化时，_文件协调器_ 会通知所有关注该文件的文件呈现方。每个呈现方随后都有机会执行任何必要的操作以保护自身的完整性。文件协调器会等待所有文件呈现方都做出响应后，才会在文件上执行所请求的操作。通过指定一个后台操作队列，协调器可以异步工作，因此可以安全地从主线程调用。更多信息请参阅 [- coordinateAccessWithIntents:queue:byAccessor:](<nsfilecoordinator/coordinate(with_queue_byaccessor_).md>)。

### 预取可显示的文件数据以维持较低的滚动卡顿率

如果你的 App 显示任意规模的基于列表或集合的布局，请采用 [UITableView](../uikit/uitableview.md) 或 [UICollectionView](../uikit/uicollectionview.md) ——以及相应的数据源与预取协议——以提供流畅的滚动体验。实现数据源协议的对象为视图提供要显示的项目，而实现预取协议的对象则负责准备并缓存这些项目的数据。

系统只提供几毫秒的时间来为单元格准备内容，超出这个时间可能导致滚动卡顿率升高或掉帧。掉帧尤其表明系统正在数据源协议方法（例如系统在主线程上调用的 [collectionView(_:cellForItemAt:)](<../uikit/uicollectionviewdatasource/collectionview(__cellforitemat_).md>)）中执行文件 I/O。要避免此类问题，请将所有文件 I/O 委托给 [NSFileCoordinator](nsfilecoordinator.md)，并在视图预取协议定义的一个或多个方法中调用所需的读取（和写入）操作。

更多信息请参阅 [UICollectionViewDataSourcePrefetching](../uikit/uicollectionviewdatasourceprefetching.md)、[UITableViewDataSourcePrefetching](../uikit/uitableviewdatasourceprefetching.md)，以及示例代码 [Prefetching collection view data](../uikit/prefetching-collection-view-data.md)。

### 并行请求访问多个文件以提升效率

在对一系列文件执行某项操作时，App 可能会遍历该列表并依次处理每个文件，例如在 `for` 或 `while` 循环中处理。然而，访问设备外部的文件（例如存放在 iCloud Drive 中的文件）可能导致代价高昂的阻塞式网络请求，因为系统必须先下载这些文件才能让你的 App 使用它们。

为将影响降到最低，不要在循环中执行任何文件 I/O。而是在循环的每次迭代中创建一个 [NSFileCoordinator](nsfilecoordinator.md) 实例，并指定一个后台队列供系统在调用该协调器的 `accessor` 闭包时使用。采用这种方式后，你就能让系统以并发、非阻塞的方式下载任何远程文件，如下例所示：

```swift
// Create a background queue for the system to use
// when invoking each file coordinator's accessor 
// closure.
let queue = OperationQueue()
queue.underlyingQueue = .global(qos: .utility)

// Iterate over the file URLs.
for url in fileURLs {
    // Create a file coordinator and specify the appropriate
    // file access intent and queue.
    let intent = NSFileAccessIntent.readingIntent(with: url)
    let coordinator = NSFileCoordinator()
    coordinator.coordinate(with: [intent],
                           queue: queue) { error in
        if let error {
            // If there's an error, handle it here.
        } else {
            // Otherwise, process the file.
        }
    }
}
```

### 为文件 URL 提供目录提示以避免浪费的 I/O

许多便捷方法都可以创建表示文件系统中文件和目录（无论是本地还是其他位置）的 URL。如果你知道这样一个 URL 的目标是一个目录，请使用要求提供 `isDirectory` 参数的方法变体，并将其值指定为 [true](../swift/true.md)。如果你使用省略该参数的更简洁方法，系统就会对文件系统执行一次可能阻塞的调用，以判断该 URL 的目标是文件还是目录。

如果你使用 Swift，且你的 App 面向 iOS 16 及更高版本（或 macOS 13 及更高版本），请使用 [init(filePath:directoryHint:relativeTo:)](<url/init(filepath_directoryhint_relativeto_).md>) 来创建文件 URL——并使用 [appending(path:directoryHint:)](<url/appending(path_directoryhint_).md>) 来修改现有 URL——同时为 `directoryHint` 参数指定一个不同于 `inferFromPath` 的值。对于更早的版本，请选择下表中方法的非阻塞变体。

下表列出了阻塞和非阻塞的方法变体。

| 阻塞 | 非阻塞 |
|---|---|
| [+ fileURLWithPath:](<nsurl/fileurl(withpath_).md>) | [+ fileURLWithPath:isDirectory:](<nsurl/fileurl(withpath_isdirectory_).md>) |
| [- initFileURLWithPath:](<nsurl/init(fileurlwithpath_).md>) | [- initFileURLWithPath:isDirectory:](<nsurl/init(fileurlwithpath_isdirectory_).md>) |
| [+ fileURLWithPath:relativeToURL:](<nsurl/fileurl(withpath_relativeto_).md>) | [+ fileURLWithPath:isDirectory:relativeToURL:](<nsurl/fileurl(withpath_isdirectory_relativeto_).md>) |
| [- initFileURLWithPath:relativeToURL:](<nsurl/init(fileurlwithpath_relativeto_).md>) | [- initFileURLWithPath:isDirectory:relativeToURL:](<nsurl/init(fileurlwithpath_isdirectory_relativeto_).md>) |
| [- URLByAppendingPathComponent:](<nsurl/appendingpathcomponent(__).md>) | [- URLByAppendingPathComponent:isDirectory:](<nsurl/appendingpathcomponent(__isdirectory_).md>) |

此外，遍历目录层级结构的 API 也可能发生阻塞，阻塞的持续时间完全取决于所遍历层级结构的深度。因此，只能从后台线程调用这些 API。

## 另请参阅

### 文件系统操作

- [Using the file system effectively](using-the-file-system-effectively.md) — 通过使用系统提供的专用目录，获得自动备份或清除等好处。
- [FileManager](filemanager.md) — 一个便捷的文件系统内容接口，也是与文件系统交互的主要方式。
- [FileManagerDelegate](filemanagerdelegate.md) — 文件管理器的委托用来在操作期间或发生错误时进行干预的接口。
- [About Apple File System](about-apple-file-system.md) — 使用高级 API 充分发挥 Apple File System 的作用。
