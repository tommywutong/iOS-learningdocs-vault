---
title: 如何制作 Core Data SQLite 数据库的副本
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/03/core-data-sqlite-backup/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:96329bf7cd4c38d8'
translated: true
---

> 原文：[How to make a copy of a Core Data SQLite database](https://oleb.net/blog/2018/03/core-data-sqlite-backup/)　·　Ole Begemann

# 如何制作 Core Data SQLite 数据库的副本

在 [Core Data](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CoreData/) 正在使用 SQLite 数据库文件时，为其制作副本（例如用于备份）并不简单：

1. 需要处理[多个文件](https://sqlite.org/tempfiles.html)：主数据库文件、预写日志（write‑ahead log，以 `-wal` 结尾）和共享内存文件（shared memory file，以 `-shm` 结尾）。
2. 在事务进行中制作数据库文件的副本可能会导致[副本损坏](https://www.sqlite.org/howtocorrupt.html#_backup_or_restore_while_a_transaction_is_active)。

你应该使用官方的 Core Data API 来制作数据库的副本。我不知道 Apple 是否为此任务提供了官方示例代码，但 [`NSPersistent​Store​Coordinator.​migrate​Persistent​Store​(_:to:​options:​withType:)`](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468927-migratepersistentstore) 看起来是正确的方法。不过，我发现使用它并不十分容易，主要是因为文档中的这条注释：

> 调用此方法后，指定的存储会从协调器中移除，因此 `store` 不再是一个有用的引用。

由于目标是不影响源存储（活跃的 Core Data 叠放（stack）应保持可用），我们必须创建一个临时的 [`NSPersistentStore`](https://developer.apple.com/documentation/coredata/nspersistentstore) 实例，其唯一目的是作为复制操作的源存储。我遵循了 [Tom Harrington 在 Stack Overflow 回答中提出的策略](https://stackoverflow.com/questions/22670273/copy-backup-persistent-store/22672386#22672386)：

1. 创建一个新的仅用于迁移的 [`NSPersistent​Store​Coordinator`](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator#) 并添加原始存储文件。这将创建一个全新的 `NSPersistentStore` 实例。（据我所知，让两个持久化存储（persistent store）同时操作同一个数据库文件没有问题。）
2. 使用这个新的持久化存储协调器迁移到目标 URL。
3. 放弃所有对仅迁移协调器的引用。

# 用法

按以下步骤创建备份：

```
let storeCoordinator: NSPersistentStoreCoordinator = ...
do {
    let backupFile = try storeCoordinator.backupPersistentStore(atIndex: 0)
    defer {
        // Delete temporary directory when done
        try! backupFile.deleteDirectory()
    }
    print("The backup is at \"\(backupFile.fileURL.path)\"")
    // Do something with backupFile.fileURL
    // Move it to a permanent location, send it to the cloud, etc.
    // ...
} catch {
    print("Error backing up Core Data store: \(error)")
}
```

# 代码

以下是 `backupPersistentStore(atIndex:)` 方法的代码（Swift 4.0）：

```
import CoreData
import Foundation

/// Safely copies the specified `NSPersistentStore` to a temporary file.
/// Useful for backups.
///
/// - Parameter index: The index of the persistent store in the coordinator's
///   `persistentStores` array. Passing an index that doesn't exist will trap.
///
/// - Returns: The URL of the backup file, wrapped in a TemporaryFile instance
///   for easy deletion.
extension NSPersistentStoreCoordinator {
    func backupPersistentStore(atIndex index: Int) throws -> TemporaryFile {
        // Inspiration: https://stackoverflow.com/a/22672386
        // Documentation for NSPersistentStoreCoordinate.migratePersistentStore:
        // "After invocation of this method, the specified [source] store is
        // removed from the coordinator and thus no longer a useful reference."
        // => Strategy:
        // 1. Create a new "intermediate" NSPersistentStoreCoordinator and add
        //    the original store file.
        // 2. Use this new PSC to migrate to a new file URL.
        // 3. Drop all reference to the intermediate PSC.
        precondition(persistentStores.indices.contains(index), "Index \(index) doesn't exist in persistentStores array")
        let sourceStore = persistentStores[index]
        let backupCoordinator = NSPersistentStoreCoordinator(managedObjectModel: managedObjectModel)

        let intermediateStoreOptions = (sourceStore.options ?? [:])
            .merging([NSReadOnlyPersistentStoreOption: true],
                     uniquingKeysWith: { $1 })
        let intermediateStore = try backupCoordinator.addPersistentStore(
            ofType: sourceStore.type,
            configurationName: sourceStore.configurationName,
            at: sourceStore.url,
            options: intermediateStoreOptions
        )

        let backupStoreOptions: [AnyHashable: Any] = [
            NSReadOnlyPersistentStoreOption: true,
            // Disable write-ahead logging. Benefit: the entire store will be
            // contained in a single file. No need to handle -wal/-shm files.
            // https://developer.apple.com/library/content/qa/qa1809/_index.html
            NSSQLitePragmasOption: ["journal_mode": "DELETE"],
            // Minimize file size
            NSSQLiteManualVacuumOption: true,
            ]

        // Filename format: basename-date.sqlite
        // E.g. "MyStore-20180221T200731.sqlite" (time is in UTC)
        func makeFilename() -> String {
            let basename = sourceStore.url?.deletingPathExtension().lastPathComponent ?? "store-backup"
            let dateFormatter = ISO8601DateFormatter()
            dateFormatter.formatOptions = [.withYear, .withMonth, .withDay, .withTime]
            let dateString = dateFormatter.string(from: Date())
            return "\(basename)-\(dateString).sqlite"
        }

        let backupFilename = makeFilename()
        let backupFile = try TemporaryFile(creatingTempDirectoryForFilename: backupFilename)
        try backupCoordinator.migratePersistentStore(intermediateStore, to: backupFile.fileURL, options: backupStoreOptions, withType: NSSQLiteStoreType)
        return backupFile
    }
}
```

代码使用了[我昨天介绍的 `TemporaryFile` 辅助类型](https://oleb.net/blog/2018/03/temp-file-helper/)。你可以从 GitHub [一起下载所有内容](https://gist.github.com/ole/e113a716158e26c1089a1d74b468deed)。

关于这段代码，我特别喜欢以下几点：

- 目标存储配置为[禁用预写日志](https://developer.apple.com/library/content/qa/qa1809/_index.html)。这意味着整个存储将包含在单个 `.sqlite` 文件中。你不必再处理 `-wal` 和 `-shm` 文件。
- 目标存储启用了 [`NSSQLite​Manual​Vacuum​Option`](https://developer.apple.com/documentation/coredata/nssqlitemanualvacuumoption#)，以最小化其文件大小。
- 源存储和目标存储都配置为只读。

# 兼容外部 BLOB 存储

**更新于 2018 年 3 月 24 日：** [Thomas Krajacic 询问](https://twitter.com/thomaskrajacic/status/977569511162499072)该方法是否能处理 Core Data 管理的外部二进制数据（即你在模型编辑器中勾选了“允许外部存储”选项的特性）。可以——临时目录会在复制的数据库文件旁边包含一个[名为 `.<store-name>_SUPPORT` 的隐藏文件夹](https://twitter.com/olebegemann/status/977637553905037312)。

但是，该函数不会向调用方报告还有其他文件需要考虑这一事实，因此你必须记得自行处理它们。

# 我并不百分百确定这是安全的

免责声明：这种方法在我的（有限）测试中是有效的，但我不能肯定它在所有情况下都百分百安全。如果你知道更好的方法，我很乐意听取你的意见。

**更新于 2018 年 3 月 26 日：** [Drew McCormack 来信说](https://twitter.com/drewmccormack/status/978169575069057024)：

> 那个 Core Data 迁移方法曾经有一个问题，就是它会把整个存储加载到内存中。……不确定现在是否还是这样。

我也不知道，但如果你在处理非常大的数据库，请将其作为潜在问题牢记在心。
