---
title: How to make a copy of a Core Data SQLite database
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/03/core-data-sqlite-backup/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:96329bf7cd4c38d8'
translated: false
---

> 原文：[How to make a copy of a Core Data SQLite database](https://oleb.net/blog/2018/03/core-data-sqlite-backup/)　·　Ole Begemann

# How to make a copy of a Core Data SQLite database

Making a copy (e.g. for a backup) of a SQLite database file while it’s being used by [Core Data](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/CoreData/) is not trivial:

1. There are [multiple files to contend with](https://sqlite.org/tempfiles.html): the main database file, the write-ahead log (ending in `-wal`), and the shared memory file (ending in `-shm`).
2. Making a copy of the database file while a transaction is in progress can [result in a corrupt copy](https://www.sqlite.org/howtocorrupt.html#_backup_or_restore_while_a_transaction_is_active).

You should use official Core Data APIs to make copies of your database. I don’t know if Apple has official sample code for this task, but [`NSPersistent​Store​Coordinator.​migrate​Persistent​Store​(_:to:​options:​withType:)`](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468927-migratepersistentstore) seems to be the right method. I found using it not very easy, though, mainly because of this note in the documentation:

> After invocation of this method, the specified store is removed from the coordinator thus `store` is no longer a useful reference.

Since the goal is to not affect the source store (the active Core Data stack should remain usable), we’ll have to create a throwaway [`NSPersistentStore`](https://developer.apple.com/documentation/coredata/nspersistentstore) instance whose only purpose is to act as the source store for the copy operation. I followed the strategy [laid out by Tom Harrington in a Stack Overflow answer](https://stackoverflow.com/questions/22670273/copy-backup-persistent-store/22672386#22672386):

1. Create a new migrate-only [`NSPersistent​Store​Coordinator`](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator#) and add the original store file. This will create a fresh `NSPersistentStore` instance. (As far as I can tell, having two persistent stores that work on the same database file is not a problem.)
2. Use this new persistent store coordinator to migrate to the target URL.
3. Drop all reference to the migrate-only coordinator.

# Usage

Do this to create a backup:

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

# The code

Here’s the code for the `backupPersistentStore(atIndex:)` method (Swift 4.0):

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

The code uses the [`TemporaryFile` helper type I wrote about yesterday](https://oleb.net/blog/2018/03/temp-file-helper/). You can [download everything together](https://gist.github.com/ole/e113a716158e26c1089a1d74b468deed) from GitHub.

Some things I particularly like about the code:

- The target store is configured with [write-ahead logging disabled](https://developer.apple.com/library/content/qa/qa1809/_index.html). This means the entire store will be contained in a single `.sqlite` file. You don’t have to deal with the `-wal` and `-shm` files.
- The target store has the [`NSSQLite​Manual​Vacuum​Option`](https://developer.apple.com/documentation/coredata/nssqlitemanualvacuumoption#) enabled, minimizing its file size.
- Both the source and the target store are configured read-only.

# Works with external BLOB storage

**Update March 24, 2018:** [Thomas Krajacic asked](https://twitter.com/thomaskrajacic/status/977569511162499072) if the method can handle Core-Data-managed external binary data (i.e. attributes for which you have checked the “Allows External Storage” option in the model editor). It can — the temporary directory [will contain a hidden folder](https://twitter.com/olebegemann/status/977637553905037312) named `.<store-name>_SUPPORT` next to the copied database file.

However, the function doesn’t report the fact that there are additional files to consider to the caller, so you’ll have to remember to take care of them yourself.

# I’m not 100 % sure this is safe

Disclaimer: this approach worked in my (limited) testing, but I can’t say for sure that it’s 100 % safe in all situations. If you know better, I’d love to hear from you.

**Update March 26, 2018:** [Drew McCormack wrote in](https://twitter.com/drewmccormack/status/978169575069057024):

> One issue with that Core Data migration method used to be that it would pull the whole store into memory. … Not sure if that is still an issue.

Me neither, but keep it in mind as a potential problem if you’re dealing with very large databases.
