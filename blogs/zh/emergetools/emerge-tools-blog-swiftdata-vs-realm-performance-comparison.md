---
title: 'Emerge Tools 博客 | SwiftData 与 Realm：性能对比'
source: Emerge Tools Blog
source_key: emergetools
source_url: 'https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:3ef2b820cb6de664'
translated: true
---

> 原文：[Emerge Tools Blog | SwiftData vs Realm: Performance Comparison](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison)　·　Emerge Tools Blog

# SwiftData 与 Realm：性能对比

2024 年 6 月 19 日

作者：Jacob Bartlett

iOS 性能客座文章

![SwiftData vs Realm: Performance Comparison](https://www.emergetools.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcover.3aa53788.png&w=3840&q=100&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

今天我们为两个宿敌之间的激战当裁判。一边是粗犷、老派、无处不在的 Realm 数据库，另一边是光鲜亮丽的年轻新秀 SwiftData。我们将从三个关键指标比较这两个 iOS 持久化框架的性能：

- 速度
- 存储
- 内存

本着科学同行评审的精神，欢迎查看我的[开源仓库](https://github.com/jacobsapps/RealmVsSwiftData)以及[原始测试结果](https://docs.google.com/spreadsheets/d/1v_7Yc2UE1sqbseKn4QrOtqVApMQCvOvVUGw64SBZtWI/edit?usp=sharing)。

## [认识框架](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#meet-the-frameworks)

在深入科学实验之前，先简单介绍一下每个框架的工作原理：

### [Realm](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#realm)

Realm 于 2014 年发布 iOS 版本，一直以高性能作为其卖点。

标准的 SQL 包装器涉及[大量抽象层](https://academy.realm.io/posts/threading-deep-dive/)：将请求传递给框架、翻译成 SQL 语句、实例化数据库连接、执行磁盘 I/O、分配内存、反序列化二进制数据，再转换回语言兼容的对象。

Realm 数据库引擎从头开始用 C++ 编写，以最大限度地减少这些开销。Realm 通过其**零拷贝架构**跳过了许多步骤：它将数据以虚拟内存的形式存储在磁盘上。进行查询时，Realm 可以直接访问数据库文件中的偏移量，并将其直接读入内存。

Realm 实现了多版本并发控制（MVCC）方法，以避免在长时间的写入期间对数据库加锁。这本质上是写时复制，数据库连接在数据的快照上操作，写入通过两阶段提交进行验证。

### [SwiftData](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#swiftdata)

SwiftData 在 [WWDC 2023](https://developer.apple.com/videos/play/wwdc2023/10187/) 上亮相，备受瞩目。终于有了一个完全 Swift 原生的持久化解决方案，让工程师能够全面拥抱 Swift 来构建 App 的每个部分：Swift 语言、SwiftUI，现在终于还有了 SwiftData。

在实践中，SwiftData 是 Core Data 之上一个干净、符合 Swift 风格的包装器。Core Data 是一个**对象图管理**框架，旨在管理对象的生命周期并将其持久化到磁盘上。

Core Data 默认使用 SQLite 作为其底层存储机制（也可以使用 XML、二进制或内存存储）。因此，将 SwiftData 描述为包装器上的包装器上的包装器并不为过。但话说回来，你也可以说 SQLite 只是 B 树之上的包装器，而 B 树又是磁盘上磁化比特的包装器。[我们不要跑偏了](https://xkcd.com/378/)。

SwiftData（以及默认情况下的 Core Data）使用 WAL（预写日志）来管理并发，已提交的事务被追加到日志中，而读取操作可以同时在主数据库文件上执行。SQLite 会定期执行“检查点”操作，将数据合并到主数据库文件中。

## [实验](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#the-experiment)

我的目标是创建公平的测试条件，既能覆盖 App 中常见的持久化场景，也能在极端数据量下考验框架：

- [构建一个同时使用 Realm 和 SwiftData 的应用程序](https://github.com/jacobsapps/RealmVsSwiftData/)
- 创建 2 个模型：一个简单模型，一个带有关联关系的复杂模型
- 测试标准 CRUD 操作的性能
- 跨数量级测试，从 100 到 1000 万个对象
- 测量每个数据库文件使用的存储空间，以及 App 的二进制体积
- 测量每次测试的峰值内存使用量

实验通过[一些简单的脚本](https://github.com/jacobsapps/RealmVsSwiftData/tree/main/RealmVsSwiftData/PerformanceTesting)运行，记录各种数据库操作的执行时间，同时也在 Xcode 中进行手动分析。

实验在 iPhone 15 Pro 上实时运行，优化级别为 `-Os`，以模拟生产环境。

我不会在这里详述每一个底层结果，但如果你感兴趣，所有性能测试结果都记录在[这里](https://docs.google.com/spreadsheets/d/1v_7Yc2UE1sqbseKn4QrOtqVApMQCvOvVUGw64SBZtWI/edit?usp=sharing)。欢迎你将数据用于同行评审，并亲自运行实验。

### [数据模型](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#data-models)

我们设计了两个数据模型，以帮助模拟简单和复杂的查询。`User` 对象有 ID、名、姓和年龄几个字段。`Student` 对象更复杂，包含多个关联关系。基对象与用户类似，但还包括一个 `School`（包含名称和位置），以及零到多个 `Grades`（包含科目、字母等级和考试委员会）。

### [硬件限制](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#hardware-limitations)

虽然我希望测试最多 1000 万个对象，但我的硬件有其他想法。我开始遇到内存限制，因此相应调整了实验，以尽可能接近系统上限（存储 100–200 万个简单对象，或约 20 万个复杂对象）。

![系统在尝试一次性写入 10,000,000 个对象时终止了测试 App](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fout-of-memory.png&w=1200&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

系统在尝试一次性写入 10,000,000 个对象时终止了测试 App

## [速度](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#speed)

Realm，这个为高性能而构建的数据库，在**大多数**情况下更快，但也存在一些明显的例外。

### [对象实例化](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#object-instantiation)

在性能测试套件的开端，对象在内存中被创建。这不是一个完美的测试，因为 `init()` 方法执行了一些低效的随机生成，然而每种类型之间的差异——Realm 的 `Objects` 和 SwiftData 的 `@Models`——不言自明。

由于我们跨多个数量级进行测试，图表使用了双对数尺度。这些图表显示，SwiftData 对象的实例化时间大约长了 **10 倍**。

![使用简单的 User 对象和复杂的 Student 对象测量对象实例化性能](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Finit-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

使用简单的 User 对象和复杂的 Student 对象测量对象实例化性能

我们的 Realm User 和 Student 都是 `Object` 的子类，而 `Object` 本身又继承自 [RLMObjectBase](https://github.com/realm/realm-swift/blob/master/Realm/RLMObjectBase.mm)。这赋予了 Realm 对象标志性功能，例如实时同步（通过键值观察）。

SwiftData 的 `@Model` 宏添加了大量功能，你可以通过右键单击并选择“展开宏”来内联查看。以下是最终的 `firstName` 属性的样子：

```swift
@_PersistedProperty
var firstName: String
@Transient
private var _firstName: _SwiftDataNoType
  @storageRestrictions(accesses: _$backingData, initializes: _firstName)
      init(initialValue) {
                  _$backingData.setValue(forKey: .firstName, to: initialValue)
                  _firstName = _SwiftDataNoType()
      }

  get {
                  _$observationRegistrar.access(self, keyPath: .firstName)
                  return self.getValue(forKey: .firstName)
      }

  set {
                  _$observationRegistrar.withMutation(of: self, keyPath: .firstName) {
                          self.setValue(forKey: .firstName, to: newValue)
                  }
      }
```

SwiftData 的 `@Model` 宏创建了额外的属性，例如 ` _$backingData`、`schemaMetadata` 和 `_$observationRegistrar`，这些属性为跟踪和访问数据更改提供了存储。不幸的是，与 Realm 相反，我们无法查看 SwiftData 中 `BackingData` 类型的闭源代码。

所有这些额外的即时分配，远远超过了实例化 Realm 对象时所执行的工作量。

### [写入性能](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#write-performance)

既然我们已经创建了大量兼容持久化框架的对象，下一步自然是将其写入磁盘。

在生产环境中，当一次写入 100,000 个对象时，我们通常会考虑通过在后台上分批写入来避免大规模的 I/O 操作。在这种情况下，单一批次符合我们的目的——测试持久化框架实际保存数据的速度。

在大多数情况下，Realm 比 SwiftData 快得多，但在对象数量较少时（≤1000），SwiftData 获胜。在 Realm 的写入、更新或删除操作中未观察到这种基线延迟。似乎 Realm 在写入磁盘或设置其内存映射时会产生一些小的恒定开销。

![使用简单的 User 对象和复杂的 Student 对象测量写入性能](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fwrite-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

使用简单的 User 对象和复杂的 Student 对象测量写入性能

对于实例化和写入，我们观察到数据量与速度之间呈线性 `O(n)` 关系。

Realm 在达到内存不足异常并崩溃之前，最多写入 2,000,000 个简单的 `User` 对象。SwiftData 只能勉强处理区区 1,000,000 个对象。当写入量超过 1,000 个对象时，Realm 的速度大约快 **3–6 倍**。

### [读取性能](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#read-performance)

在评估读取查询性能时，似乎并非所有数据模型都是平等的：最佳框架取决于我们存储的数据结构——简单还是复杂。

对于极其简单的 `User` 对象（几个字段，无关联关系），我们查询所有名为“Jane”的用户。Realm 快得多，其零拷贝架构在将数据直接读入内存时大放异彩。对于简单的 SwiftData 对象，读取性能一开始还不错，但当数据库中有超过 10 万个对象时，性能急剧下降。

对于更复杂的 `Student` 模型，我们搜索所有获得最高分的物理学生。我们观察到了相反的效果：SwiftData 通常比 Realm 快 **10 倍以上**。

![使用简单的 User 对象和复杂的 Student 对象测量读取性能](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fread-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

使用简单的 User 对象和复杂的 Student 对象测量读取性能

两个查询都需要进行全数据库扫描，以查找匹配给定谓词的对象。这导致了我们在数据中观察到的线性 `O(n)` 时间复杂度，加上一些额外开销，使得对少于 10,000 个简单对象的查询耗时大致相同。

SwiftData 在处理这些复杂关联关系时表现如此出色，是因为其 Core Data 基础，后者在管理复杂对象图和跨关系过滤数据时游刃有余。

查找性能是底层存储数据结构的一个函数。对于 Realm（[使用其自定义引擎](https://academy.realm.io/posts/jp-simard-realm-core-database-engine/)）和 SwiftData（[构建在 SQLite 之上](https://fly.io/blog/sqlite-internals-btree/)）来说，**底层都是 B 树**。这意味着在数据库中查询特定对象将表现出 `O(log n)` 的时间复杂度。

### [更新性能](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#update-performance)

我们的更新查询包括几个步骤：查询以将一些数据读入内存，执行一些代码以修改这些数据，然后写回磁盘。

在 Realm 中，对 `Object` 的所有修改都必须在一个**写事务**内进行。在 SwiftData 中，我们可以直接修改 `@Model` 对象，并将其**更新插入**回数据库。

对于简单的 `User` 模型，我们获取了所有名为“Jane”的用户，并将其重命名为“Wendy”（一定是 Jane 做了些可怕的事情）。对于更复杂的 `Student` 模型，考试委员会发现某所特定学校的所有数学学生都在作弊，因此他们所有的数学考试成绩都被修改为 `F` 等级。

在两个框架之间，每种数据模型都观察到了相似的结果。SwiftData 在处理中小数据量时快得多，只有在一次修改 100,000 个对象时才被 Realm 超越。

![使用简单的 User 对象和复杂的 Student 对象测量更新性能](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fupdate-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

使用简单的 User 对象和复杂的 Student 对象测量更新性能

这种性能差异可以通过多步骤的更新过程来解释：我们查询整个数据库——包含 `n` 个项目——以找到 `m` 个匹配我们谓词的对象，然后修改并重新保存那些对象。

当 `n` 较小时，两个框架的读取都非常快（SwiftData 略有优势），并且需要写入的数据量非常少。

然而，随着数据总量的增加，`m` 也会增加，这代表匹配我们谓词的项目数量——因此所需的写入量也会增加。两个框架的写入速度都比读取慢得多，这种效应在 SwiftData 中，当写入量较大时更为明显。

### [删除性能](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#delete-performance)

我们的删除操作清空了数据库中的所有对象，因此没有查询开销。对于更复杂的 `Student` 对象，这包括一个级联删除，它也会清除 `Schools` 和 `Grades`。

这个操作相当有趣，因为很难精确界定每个框架的时间复杂度。

![使用简单的 User 对象和复杂的 Student 对象测量删除性能](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fdelete-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

使用简单的 User 对象和复杂的 Student 对象测量删除性能

SwiftData 似乎对两种模型都表现出线性 `O(n)` 时间复杂度，然而其对象图管理能力在级联删除复杂的 `Student` 模型时，给了它一点速度上的优势。

Realm 对复杂的 `Student` 模型表现出线性行为，但对简单的 `User` 对象却表现出**优于线性**的速度。删除同一类型的所有对象很快，因为内存映射的对象在存储中具有相同的布局，因此计算最终偏移量（直到删除为止）很简单。这使得非级联的 `User` 删除操作能够以 `O(log n)` 的时间运行。

## [存储](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#storage)

两个持久化框架的存储性能相当。

### [文件系统](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#file-system)

使用一个小工具函数记录文件 URL，测量每个框架数据占用的存储空间相当简单。

对于 Realm，我们可以使用 `Realm.Configuration.defaultConfiguration.fileURL`，对于 SwiftData，我们可以记录 `container.configurations.first?.url`。从这里，我们可以使用 `FileManager` API 来测量存储空间。

Realm 的底层数据文件存储在 App `default.realm` 文件夹中的 `/Documents`。它还包括一个 `default.realm.lock` 文件，以帮助管理其多版本并发控制。

SwiftData 文件位于 `/Library/Application Support`，并将 SQLite 数据存储在 `default.store` 文件中。SwiftData 的并发机制——预写日志——也在这里可见：`default.store-wal`。

![RealmVsSwiftData App 的文件系统，其中存储了 100,000 个 Student 对象](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fapp-db-files.png&w=1920&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

RealmVsSwiftData App 的文件系统，其中存储了 100,000 个 Student 对象

### [存储性能](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#storage-performance)

不出所料，我们观察到存储的对象数量与使用的空间之间存在线性关系——`O(n)` 空间复杂度。

SwiftData 似乎有一个 70 kB 的最小文件大小，这比理论上的 [SQLite 数据库最小文件大小 512 字节](https://www.sqlite.org/fileformat.html)高出数倍。Realm 的自定义引擎没有显示任何此类最小大小，仅用 20 kB 就存储了 100 个用户。

![使用简单的 User 对象和复杂的 Student 对象测量数据库文件大小](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fstorage-space.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

使用简单的 User 对象和复杂的 Student 对象测量数据库文件大小

奇怪的是，我测量到 SwiftData 在多达 10,000 个用户之前，基线数据为 0.07 MB——当我们测量数据库文件大小时，数据可能还在预写日志中，等待检查点操作并合并到主数据库中。

尽管 Realm 的零拷贝架构以内存映射格式存储其数据，但这似乎非常优化——两个框架使用了非常相似的存储空间。

总的来说，Realm 在数据量极小的情况下表现稍好，而 SwiftData 在存储大量对象时表现稍好。

### [二进制体积](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#binary-size)

查看我们示例 App 的[体积分析](https://www.emergetools.com/product/sizeanalysis)，我们可以看到大部分存储空间被 2.2 MB 的 Realm 库占用。

![Emerge Tools 对开源测试项目 RealmVsSwiftData 的体积分析 X 射线图](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fbinary-x-ray.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Emerge Tools 对开源测试项目 RealmVsSwiftData 的体积分析 X 射线图

SwiftData 是 iOS 的一部分，因此不会在你的 App bundle 中占用任何额外的存储空间——该框架由 [dyld](https://www.emergetools.com/glossary/dyld) 与其他系统框架一起动态链接。

## [内存](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#memory)

内存性能自然是测试数据量的一个函数——当我们在持久化中进出操作更多对象时，App 将使用更多内存。

在小数据量时，Realm 的内存使用量比 SwiftData 稍高，但在大数据量时，Realm 的性能远超 SwiftData——执行相同工作时，其内存占用空间仅为 SwiftData 的一小部分。

### [峰值内存使用量](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#peak-memory-usage)

我想在这里再创建一个工具函数，但 Mach 进程内存 API 返回的结果与我通过标准 Xcode 调试器观察到的结果相差甚远，因此在这些测试中，我采用了老式的人工观察法。

我在运行实验中使用的同一测试套件时，测量了 Xcode 内存使用情况图。

![Xcode 在将 1,000,000 个复杂对象保存到磁盘时开始吃力](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fmemory-graph.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

Xcode 在将 1,000,000 个复杂对象保存到磁盘时开始吃力

由于我们的测试设计方式，性能测试开始时的大规模写入操作是运行时间最长、内存最密集的操作。

在生产环境中，我们通常希望实现批处理和分页来避免这种资源消耗，但在此次测试中，我打算将两个框架推向内存不足的崩溃，看看它们能承受多少。

结果显示，两个框架在写入 10,000 个或更多对象之前都毫不费力。SwiftData 似乎有较低的内存基线，但在更高的数据量下，Realm 占用的内存大约是 SwiftData 的 **1/3**。

![使用简单的 User 对象和复杂的 Student 对象测量峰值内存使用量](https://www.emergetools.com/_next/image?url=%2Fimages%2Fblogs%2Fblog22%2Fmemory-performance.png&w=2048&q=75&dpl=dpl_9GUvYRYkSXVcp9398feaiSHuz7SE)

使用简单的 User 对象和复杂的 Student 对象测量峰值内存使用量

Realm 似乎会使用一些内存来“预热”框架，即使在写入极少量的数据时也是如此。另一方面，SwiftData 系统框架在数据量极低时对内存使用的影响可以忽略不计。

在高数据量下，有一点变得清晰：Realm 自定义构建的移动数据库引擎在内存利用方面大幅超越了高度抽象的 SwiftData。

## [其他考虑因素](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#other-considerations)

虽然我们已经进行了一个相当全面的性能测试，但移动 App 需要考虑的不仅仅是速度、存储和内存利用。

在受控实验之外，有许多因素会影响你对框架的选择：

- SwiftData 最低支持 iOS 17+，因此除非你的开发团队支持 `n-1` 版本，否则你短期内不会在生产环境中使用它。
- 在撰写本文时，SwiftData 的 Bug 相当多——我不得不将几个 `Grade` 枚举替换为原始字符串，才能使宏正常运行。
- Realm 是开源的，这意味着如果你发现 Bug，可以研究引擎代码库，提交详细的问题报告，甚至建议修复方法。SwiftData 是闭源的，你解决问题的唯一途径是提交 Radar 并等待下一个版本。
- 这两个数据库都不太可能消失——它们分别由 MongoDB 和 Apple 支持，都是大型上市公司。Realm 还有一个大型的开源社区，因此即使 Mongo 倒闭，它也不会轻易消亡。
- SwiftData 非常不成熟，我们可以预期它在未来几年内会发生重大变化。Realm 则持续添加新功能（例如用 `@Persisted` 属性包装器取代 `@objc dynamic`），但其核心引擎和实现一直保持稳定。
- SwiftData [还不支持索引](https://www.hackingwithswift.com/quick-start/swiftdata/how-to-index-swiftdata-properties-for-faster-searching)。如果你需要高效查询大型数据集，这是一个重要的考虑因素。
- 尽管有 Bug，但 SwiftData 入门要容易得多。

## [结论](https://www.emergetools.com/blog/posts/swiftdata-vs-realm-performance-comparison#conclusion)

当我开始这项工作时，我强烈地预期成熟、注重性能的老牌选手 Realm 会在各个方面击败 SwiftData。

在写入、简单读取查询和内存占用空间方面，这完全正确。Realm 的 `Objects` 创建轻量级，可以快速大量存储，其内存映射结构允许在不占用系统资源的情况下快速处理大量数据。Realm 在处理大量简单对象时尤其优于 SwiftData。

然而，SwiftData 在几个方面令人惊讶。其 Core Data 传统赋予的出色对象图管理能力意味着，对于跨关联关系的更复杂数据，其查询能力显著优于 Realm。在较小的数据量下（≤10,000 个项目，这涵盖了绝大多数移动用例），SwiftData 在更新现有数据时也快得多。

*那么，哪个框架更好？*

和往常一样，看情况而定。所有 App 都有不同的用例、不同的数据量和不同的资源约束。我希望这篇文章能帮助你决定哪种方法最适合你的 App。

🍺

这是一篇来自 **Jacob Bartlett** 的 Emerge Tools 客座文章。如果你想看到更多他的内容，可以[订阅 Jacob's Tech Tavern](https://jacobbartlett.substack.com)，每两周接收一次关于 iOS、Swift、技术和独立项目的深度文章；或者[在推特上关注他](https://twitter.com/jacobs_handle)。
