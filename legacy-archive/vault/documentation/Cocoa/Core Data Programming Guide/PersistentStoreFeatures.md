---
title: Core Data 编程指南
apple_id: TP40001075
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/PersistentStoreFeatures.html
archived_at: '2026-07-15T07:14:27.632303Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Data 编程指南](index.md)



## 持久化存储的类型与行为

Core Data 提供一种内存中的持久化存储，以及三种基于磁盘的持久化存储，如表 16-1 所述。二进制存储（[NSBinaryStoreType](https://developer.apple.com/documentation/coredata/nsbinarystoretype)）和 XML 存储（[NSXMLStoreType](https://developer.apple.com/documentation/coredata/nsxmlstoretype)）一样，都是原子存储（atomic store）。你也可以创建自定义存储类型，既可以是原子的，也可以是增量的。参见 _[Atomic Store Programming Topics](../Atomic%20Store%20Programming%20Topics/Introduction%20to%20Atomic%20Store%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmrr)_ 和 _[Incremental Store Programming Guide](../../Data%20Management/Incremental%20Store%20Programming%20Guide/About%20Incremental%20Stores.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydombw)_。

> [!NOTE]
> 

__表 16-1__ 内置的持久化存储类型

| 存储类型 | 速度 | 对象图是否常驻内存 | 其他因素 |
| --- | --- | --- | --- |
| XML（原子） | 慢 | 整体常驻 | 可被外部解析 |
| 二进制（原子） | 快 | 整体常驻 | 无 |
| SQLite | 快 | 部分常驻 | 无 |
| 内存中 | 快 | 整体常驻 | 无需磁盘存储 |

> [!IMPORTANT]
> 

得益于 Core Data 提供的抽象层，通常没有必要在整个开发过程中都使用同一种存储。例如，在项目生命周期的早期阶段常常使用 XML 存储，因为它相对易读，你可以通过检查文件来确定其中是否包含预期的数据。而在使用大数据集的已部署应用中，通常会使用 SQLite 存储，因为它性能更高，且不要求整个对象图都常驻内存。如果希望存储写入是原子性的，则可以使用二进制存储。

### 持久化存储安全性的局限

Core Data 不对来自不受信任来源的持久化存储（相对于内部生成的存储而言）的安全性做任何保证，也无法检测文件是否被恶意修改过。SQLite 存储的安全性略高于 XML 和二进制存储，但不应被视为天生安全。另请注意，元数据（metadata）中归档的数据有可能被独立于存储数据本身进行篡改。要确保数据安全，应使用诸如加密磁盘映像之类的技术。

### 获取谓词与排序描述符

获取（fetching）操作会因存储类型不同而略有差异。在 XML、二进制和内存中存储中，谓词（predicate）和排序描述符的求值是在 Objective-C 中进行的，可访问所有 Cocoa 功能，包括 [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) 上的比较方法。

而 SQLite 存储则会将谓词和排序描述符编译为 SQL，并在数据库内部对结果求值。这样做主要是出于性能考虑，但也意味着求值发生在非 Cocoa 环境中，因此依赖 Cocoa 的排序描述符（或谓词）无法生效。SQLite 支持的排序选择器有 [compare:](https://developer.apple.com/documentation/healthkit/hkquantity/1615160-compare)、[caseInsensitiveCompare:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/caseInsensitiveCompare:)、[localizedCompare:](https://developer.apple.com/documentation/foundation/nsstring/1416999-localizedcompare)、[localizedCaseInsensitiveCompare:](https://developer.apple.com/documentation/foundation/nsstring/1417333-localizedcaseinsensitivecompare) 以及 [localizedStandardCompare:](https://developer.apple.com/documentation/foundation/nsstring/1409742-localizedstandardcompare)。最后一种是类似 Finder 的排序方式，也是大多数情况下大多数人应该使用的方式。此外，使用 SQLite 存储时无法对瞬态（transient）属性进行排序。

对于可用于 SQLite 存储的谓词，还存在一些额外限制：

- 并非所有任意的 SQL 查询都能转换为谓词。
- 谓词中的键路径（key path）里最多只能包含一个一对多（to-many）元素。

  例如，不允许出现 `toOne.toMany.toMany` 或 `toMany.toOne.toMany` 这类构造（它们会求值为“集合的集合”）。因此，在发送给 SQL 存储的任何谓词中，`ALL`、`ANY` 和 `IN` 这三种运算符中最多只能出现其中一种（且只能出现一次）。

Core Data 支持 `noindex:`，可用于在传递给 SQLite 的查询中丢弃索引。这样做主要是出于性能原因：SQLite 在每次查询中所使用的索引数量有限，`noindex:` 允许用户优先指定不应使用哪些索引。关于函数表达式的更多内容，请参阅 [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate) 文档。

### SQLite 支持的文件系统

SQLite 存储支持从驻留在任何类型文件系统上的文件中读取数据。但是，SQLite 存储通常不支持直接写入不支持字节范围锁定（byte-range locking）的文件系统。对于 DOS 文件系统以及某些不能正确支持字节范围锁定的 NFS 文件系统实现，SQLite 使用 `<dbfile>.lock` 锁定方式；对于 SMB 文件系统，则使用 flock 风格（文件级）锁定。

总的来说，支持字节范围锁定的文件系统具有最佳的并发读写支持，其中包括 HFS+、AFP 和 NFS。支持简单文件锁定的文件系统也可以使用，但不支持多进程之间那么高的并发读写访问，简单文件锁定系统包括 SMB 和 DOS。SQLite 存储**不**支持写入 WebDAV 文件系统。

### SQLite 文件大小与记录删除

仅仅从 SQLite 存储中删除一条记录，并不一定会使文件的体积减小。如果删除的项足够多，能在数据库文件中腾出一整个页（page），SQLite 的自动数据库清理（vacuuming）机制会在重新整理数据、移除该页的同时缩小文件体积。同样，如果你删除的是一个本身占用多个页的项（例如缩略图图像），文件体积也会随之减小。

SQLite 文件被组织为一系列页的集合。这些页内的数据是通过 B 树（B-tree）管理的，而不是以简单的定长记录形式存储。这种格式在搜索和整体存储方面效率更高，因为它使 SQLite 能够在单个文件中同时优化数据和索引的存储方式。这种格式也是 SQLite 数据完整性机制（事务与日志记录）的基础。然而，这种设计的代价是：某些删除操作可能会在文件中留下“空洞”，从而影响读写性能。如果你删除了一些数据又添加了新数据，被删除数据留下的空洞可能会被新增数据填补，也可能会对文件进行清理压缩，具体取决于 SQLite 根据当前操作认为哪种方式更合适。

### 为 SQLite 存储配置保存行为

Core Data 保存 SQLite 存储时，SQLite 只会更新存储文件的一部分。如果这部分更新丢失将是灾难性的，因此必须确保在应用程序继续运行之前文件已被正确写入。遗憾的是，这种局部文件更新方式意味着，在某些情况下，即使只保存一小组更改到 SQLite 存储，所花费的时间也可能远远长于保存到（比如）XML 存储。举例来说，保存到 XML 文件可能只需不到百分之一秒，而保存到 SQLite 存储则可能耗时接近半秒。对于 XML 或二进制存储而言，则不存在这种数据丢失风险：由于对这些存储的写入通常是原子性的，数据丢失涉及文件损坏的可能性更低，并且旧文件在新文件成功写入之前不会被删除。

> [!NOTE]
> 

### 更改存储的类型与位置

你可以使用 [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator) 的 [migratePersistentStore:toURL:options:withType:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468927-migratepersistentstore) 方法，将存储从一种类型或位置迁移到另一种（例如用于“另存为”操作）。调用该方法后，原始存储会从协调器中移除，因此该持久化存储的引用不再有用。下面的代码片段演示了该方法的用法，展示了如何将存储从一个位置迁移到另一个位置。如果旧存储的类型是 XML，示例还会将存储转换为 SQLite。

Objective-C

1. `NSPersistentStoreCoordinator *psc = [[self managedObjectContext] persistentStoreCoordinator];`
2. `NSURL *oldURL = <#URL identifying the location of the current store#>;`
3. `NSURL *newURL = <#URL identifying the location of the new store#>;`
4. `NSError *error = nil;`
5. `NSPersistentStore *xmlStore = [psc persistentStoreForURL:oldURL];`
6. `NSPersistentStore *sqLiteStore = [psc migratePersistentStore:xmlStore`
7. `toURL:newURL`
8. `options:nil`
9. `withType:NSSQLiteStoreType`
10. `error:&error];`

Swift

1. `let psc = self.persistentContainer.persistentStoreCoordinator`
2. `let oldURL = URL(fileURLWithPath: "<#oldURL#>")`
3. `let newURL = URL(fileURLWithPath: "<#newURL#>")`
4. `guard let oldStore = psc.persistentStore(for: oldURL) else {`
5. `fatalError("Failed to reference old store")`
6. `}`
7. `do {`
8. `try psc.migratePersistentStore(oldStore, to: newURL, options:nil, withType:NSSQLiteStoreType)`
9. `} catch {`
10. `fatalError("Failed to migrate store: \(error)")`
11. `}`
12. `}`

要迁移一个存储，Core Data 会：

1. 创建一个临时的持久化栈。
2. 挂载新旧两个存储。
3. 从旧存储中加载所有对象。
4. 将这些对象迁移到新存储。

   这些对象会先被赋予临时 ID，然后分配到新存储。新存储随后会保存这些新分配的对象（将其提交到外部仓库）。
5. 通知其他持久化栈对象 ID 已发生变化（从旧存储变为新存储），以便迁移完成后各个栈仍能继续正常工作。
6. 卸载旧存储。
7. 返回新存储。

在以下情况下可能会产生错误：

- 你为该方法提供了无效的参数
- Core Data 无法添加新存储
- Core Data 无法移除旧存储

对于后两种情况，你得到的错误与直接调用 `addPersistentStore:` 或 `removePersistentStore:` 时得到的错误相同。如果在添加或移除存储时发生错误，应将其当作异常处理，因为此时持久化栈很可能已处于不一致的状态。

如果迁移过程本身发生失败，你得到的将不是错误而是异常。在这些情况下，Core Data 会干净地回退，通常不需要额外的修复工作。你可以检查异常的描述信息来确定具体出了什么问题——可能的错误种类很多，从“磁盘已满”“权限问题”到“SQLite 存储已损坏”“Core Data 不支持跨存储关系”都有可能。

### 为存储关联元数据

存储的 _元数据（metadata）_ 提供了与该存储相关的附加信息，这些信息并不直接关联到存储中的任何实体。

元数据以字典形式表示。Core Data 会自动设置一些键值对，用以表明存储类型及其 UUID。你可以为应用程序创建额外的自定义键，或者提供一组标准键（例如 `kMDItemKeywords`）以支持 Spotlight 索引（前提是你也编写了相应的导入器）。

对于要放入元数据中的信息要格外谨慎。Spotlight 对元数据的大小有限制，将整份文档复制到元数据中通常没有意义。不过，如果你创建了用于标识存储中某个特定对象的 URL（使用 [URIRepresentation](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/1391689-urirepresentation)），将该 URL 包含在元数据中可能会很有用。

### 获取元数据

获取存储元数据有两种方式：

- 给定一个持久化存储的实例，使用 [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator) 的实例方法 [metadataForPersistentStore:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468911-metadata) 获取其元数据。
- 使用 [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator) 的类方法 [metadataForPersistentStoreOfType:URL:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468804-metadataforpersistentstore)，无需创建持久化栈即可获取存储的元数据。

这两种方式之间存在一个重要区别。实例方法 `metadataForPersistentStore:` 返回的是元数据在你程序中的当前状态，包括自上次保存存储以来所做的任何更改。而类方法 `metadataForPersistentStoreOfType:URL:error:` 返回的是元数据在存储本身中当前的表示形式。如果存储存在尚未保存的更改，返回值可能因此与程序中的状态不同步。

### 设置元数据

设置存储的元数据也有两种方式：

- 给定一个持久化存储的实例，使用 [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator) 的实例方法 [setMetadata:forPersistentStore:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468899-setmetadata) 设置其元数据。
- 使用 [NSPersistentStoreCoordinator](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator) 的类方法 [setMetadata:forPersistentStoreOfType:URL:error:](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468897-setmetadata)，无需创建持久化栈即可设置元数据。

这两种方式之间同样存在一个重要区别。如果使用 `setMetadata:forPersistentStore:`，必须先（通过托管对象上下文）保存存储，新的元数据才会被保存。而如果使用 `setMetadata:forPersistentStoreOfType:URL:error:`，元数据会立即被更新，同时文件的最后修改日期也会随之改变。

如果你在 macOS 中使用 [NSPersistentDocument](https://developer.apple.com/documentation/appkit/nspersistentdocument)，这一差异会带来特别的影响。如果你在持久化存储正被积极使用期间（也就是存在尚未保存的更改时）使用 `setMetadata:forPersistentStoreOfType:URL:error:` 更新元数据，那么在保存文档时会看到警告：“This document's file has been changed by another application since you opened or saved it.”（该文档的文件自打开或保存以来已被其他应用程序更改。）为避免这种情况，请改用 `setMetadata:forPersistentStore:`。要找到文档的持久化存储，通常可以向持久化存储协调器请求其持久化存储列表（[persistentStores](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/1468790-persistentstores)），并使用返回数组中的第一项来设置元数据。当你使用 `setMetadata:forPersistentStoreOfType:URL:error:` 时，该操作会被视为发生在你的 Core Data 栈之外的外部更改。

由于 Core Data 在同一份元数据中管理着 [NSStoreTypeKey](https://developer.apple.com/documentation/coredata/nsstoretypekey) 和 [NSStoreUUIDKey](https://developer.apple.com/documentation/coredata/nsstoreuuidkey) 的值，因此在设置自己的键和值之前，应先对现有元数据做一份可变拷贝，如以下代码片段所示：

Objective-C

1. `NSURL *url = [NSURL fileURLWithPath:@"url to store"];`
2. `NSPersistentStore *store = [self.managedObjectContext.persistentStoreCoordinator persistentStoreForURL:url];`
3. `NSMutableDictionary *metadata = [[store metadata] mutableCopy];`
4. `metadata[@"MyKeyWord"] = @"MyStoredValue";`
5. `[store setMetadata:metadata];`

Swift

1. `let url = NSURL(fileURLWithPath: "url to store")`
2. `let psc = self.persistentContainer.persistentStoreCoordinator`
3. `guard let store = psc.persistentStore(for: url) else {`
4. `fatalError("Failed to retrieve store from \(url)")`
5. `}`
6. `var metadata = store.metadata`
7. `metadata["MyKeyWord"] = "MyStoredValue"`
8. `store.metadata = metadata`

[Change Management](ChangeManagement.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrsfvjvomi)

[Concurrency](Concurrency.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzvfvbuqmrufvjvomi)
