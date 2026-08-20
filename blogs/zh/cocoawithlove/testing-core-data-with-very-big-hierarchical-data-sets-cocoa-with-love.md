---
title: '在大规模分层数据集上测试 Core Data | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/03/testing-core-data-with-very-big.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2603c1f0ae981e2a'
translated: true
---

> 原文：[Testing Core Data with very big hierarchical data sets | Cocoa with Love](https://www.cocoawithlove.com/2008/03/testing-core-data-with-very-big.html)　·　Cocoa with Love (Matt Gallagher)

我用一个包含一百万个对象的数据集（存储在一个基本的三层层级结构中）测试了 Core Data 的性能。我考察了构建、加载、获取以及遍历时的性能表现。

## 测试数据

我的测试数据将是一个三层层级结构。这种安排反映了一种数据集合包含在另一集合中很重要的情形。它也创造了一种场景，在此场景下，图的遍历、搜索和包含性测试可以以多种方式执行，且没有哪种方式明显更优——这就引发了性能测试的需求。

![](https://www.cocoawithlove.com/assets/objc-era/coredatasetentities.png)

以下所有测试都将使用相同的数据：

- 一个顶层对象
- 一千个中间层对象，每个都与顶层对象相连
- 一百万个底层对象，每个中间层对象连接一千个底层对象

每个底层对象都会有一个名称，格式如下："Object x, y, z"，其中"x"、"y"和"z"分别是它所连接的顶层、中间层和底层对象的索引。这样能确保每个名称都是唯一的，并且方便调试，我可以验证我拿到的是否是我期望的那个对象。

## 构建测试文稿

以下是创建上述数据并将其保存到磁盘所花的时间。表中每一项改进都已包含其之前改进的效果。

| 创建方法 | 耗时 | 峰值内存 |
|---|---|---|
| 一次性创建所有对象并保存 | 368.236 秒 | 798 MB |
| 同上，但在操作前先对上下文（Context）调用 setUndoManager:nil | 342.618 秒 | 778 MB |
| 在外层循环内容外包裹 NSAutoreleasePool 的 init/release 以及 NSManagedObjectContext 的 save | 262.511 秒 | 254 MB |
| 每次保存后调用 NSManagedObjectContext 的 reset | 258.904 秒 | 20.1 MB |

我进行速度测试的不同保存方案，就是 Apple 在其 [《Core Data 编程指南：高效导入数据》](http://developer.apple.com/documentation/Cocoa/Conceptual/CoreData/Articles/cdImporting.html) 页面上给出的那些。

此前我从未在 Core Data 中创建过拥有一百万个对象的文稿，所以没预料到创建文稿会花这么长时间。花 4 到 6 分钟来保存一个 77.1 MB 的文件，这看起来确实不太对劲。Apple 宣称 Core Data 能够应对 TB（Terabyte）级别的数据库；光是想到要创建这样的数据库，我就觉得很恐怖。

为了确定 Core Data 相比直接通过 SQLite 创建数据究竟有多慢，我写了一个命令行工具直接与 sqlite3 对话，向 ZBOTTOMLEVEL 表中写入一百万行数据。这花了 124 秒，因此 Core Data 大约是让耗时翻了一倍。这或许还算合理，尽管**感觉**上仍然太久了。

尽管我对这么长的耗时很沮丧，但保存过程看起来确实是高度线性的。这张表展示了一个一百万行的数据库保存花了 250 秒。对于 10,000 个对象，我记录的时间是 2.5 秒；对于 100,000 个对象，是 25 秒；而一千万行则大约花了 40 分钟（大约 2,500 秒）。

出于好奇，我试着把这个有一百万行的文稿保存为 XML 文件。这花了 941 秒，其中大部分时间都花在了我的电脑（配有 2.25 GB RAM，并且不乐意承受这种努力）上超过 3 GB 的内存颠簸交换（thrashing）上。我不清楚这么多的内存都在干什么，因为 XML 文件大小是 227.8 MB，而保存前的对象只占用了大约 100 MB 的 RAM。

最后一个选项（`-[NSManagedObjectContext reset]`）在一个 App 中用起来尤其不便（因为你必须从该上下文中重新获取每一个 NSManagedObject），但由于它对内存使用量的影响（所用内存比其他任何技术少 12 倍），如果你想以这种方式创建并保存一个两千万行的数据库，它就是唯一能保持可用的选项了。

## 加载所有底层对象名称的集合

我的第一个测试将是构建一个集合，其中包含所有属于顶层对象之下底层对象子级的名称。如果你在测试层级结构内的名称唯一性，或者只是想要一份该层级结构所使用的所有名称的列表，就可能进行这类操作。

我会通过两种方法来测试。第一种是使用如下 NSPredicate 的 NSFetchRequest：

```objc
[NSPredicate predicateWithFormat:@"midLevel.topLevel == %@", topLevelObject];
```

然后，从返回数组中各对象的“name”键构建一个 NSSet。

第二种是键路径（keyPath）抓取（fetch）：

```objc
bottomLevelNames = [topLevelObject valueForKeyPath:
    @"midLevel.@distinctUnionOfSets.bottomLevel.name"];
```

| 抓取（Fetch）方法 | 耗时（首次迭代） | 耗时（后续 4 次迭代的平均值） |
|---|---|---|
| NSFetchRequest | 27.4 秒 | 15.3 秒 |
| 键路径（keyPath）访问 | 217.1 秒 | 6.4 秒 |
| 预抓取（prefetching）后的键路径访问（预抓取耗时 13.9 秒） | 18.5 秒 | 6.4 秒 |

预抓取的做法是使用一个 NSFetchRequest 来返回数据库中的所有 BottomLevel 对象，同时使用 setRelationshipKeyPathsForPrefetching: 并传入一个包含“midLevel”的数组，以进一步抓取 MidLevel 对象。

从这些数据得出的结论：

- 对于冷启动，NSFetchRequest 是最快的方式
- 在未预抓取的数据上使用键路径极其慢
- 键路径一旦被缓存就非常快

我确实也测试了使用“for (child in parentChildSet)”方式遍历所有对象的方法。这本质上就是“键路径”方法的一种手动形式，不出所料地返回了几乎相同的耗时。

## 查找具有特定名称的底层对象

本测试将在层级结构中搜索具有特定“name”值的 BottomLevel 对象。

我将以 4 种不同的方式执行本测试：

- 和之前一样，一种搜索方法将使用 NSFetchPredicate 完成工作，数据库字段不建索引。
- 第二种搜索同样使用 NSFetchPredicate，但这次对 BottomLevel 上的“name”字段建立索引。
- 第三种方法将与最朴素的方法比较：手动遍历整个对象图来寻找具有给定“name”的 BottomLevel 对象。
- 最后，我将尝试通过生成从“name”值到层级结构中具有该值的 BottomLevel 对象的映射来缓存查找，并将这种缓存查找与其他方法进行比较。

两个 NSFetchRequest 测试都将使用如下 NSPredicate：

```objc
[NSPredicate predicateWithFormat:
    "midLevel.topLevel == %@ AND name == 'Object 5, 5, 0'", topLevelObject];
```

手动遍历会遍历所有对象，并测试其名称是否等于 @"Object 5, 5, 0"。由于手动遍历可以在找到匹配项时立即退出，我将以恰好经过 500,000 次比较后找到匹配项为基准进行计时（这应能提供一个合适的平均值）。

从“name”值到 BottomLevel 对象的缓存映射将是一个 NSDictionary，构建方式如下：

```objc
NSSet *bottomLevelSet = [topLevelObject
    valueForKeyPath:@"midLevel.@distinctUnionOfSets.bottomLevel"];
NSArray *bottomLevelArray = [bottomLevelSet allObjects];
NSArray *bottomLevelNames = [bottomLevelArray valueForKey:@"name"];
NSDictionary *bottomLevelKeyedByName =
    [NSDictionary
        dictionaryWithObjects:bottomLevelArray
        forKeys:bottomLevelNames];
```

| 抓取（Fetch）方法 | 耗时 |
|---|---|
| NSFetchRequest（'name' 未建索引） | 670,000 微秒 |
| NSFetchRequest（'name' 已建索引） | 2,174 微秒 |
| 键路径遍历（预抓取后的平均值） | 940,000 微秒 |
| NSDictionary（在花费 12.6 秒初始化设置后） | 24 微秒 |

键路径遍历只需遍历到找到它想要的值为止。我故意搜索了一个不存在的值（强迫完成全遍历），然后将时间减半来获得该平均值。

在我运行完这些测试之后，我试了一种不带层级约束的 NSFetchRequest（使用谓词格式字符串：@"name == 'Object 5, 5, 0'"）。这大约将耗时减半，但表明一个 JOIN 操作并不像忘记为搜索字段建索引那样灾难性。

从这些数据得出的结论：

- 在此类查找上，NSFetchRequest 的速度快得可以预料。
- 为字段建立索引（使用 XCode 数据模型编辑器中的复选框）极其重要。若没有这个，SQLite 会手动搜索每个元素，那几乎和全遍历一样慢。
- 对一百万个字符串比较进行迭代比我预想的要快得多，但依然不如一次索引查找那么快。
- 没有什么能与 NSDictionary（一旦建立好之后）相比。它比 SQL 索引查找快 100 倍。这并不意外，因为它是专门为这类查找设计的数据结构。

## 最终结论

Core Data 并不是应对所有数据管理问题的万灵药。它并不会让一切魔法般地变快。显然，仍然有些方面它会很慢（有时非常慢），而且有些数据访问方式必须避免采用。

NSFetchRequest 做了它该做的事情，并且做得很迅速。前提是你为搜索字段建立了索引。

NSSQLStore 似乎能够再保存得快一点。花上 4 到 6 分钟保存一个 77.1 MB 的文稿，看起来不太正常。不过，它并没有比裸 SQLite 慢一个数量级，而且对于任何大于极小规模的数据而言，它仍然比 NSXMLStore 或者 NSBinaryStore 要快。

考虑到背后的工作量之大，对已缓存的 Core Data 对象进行基本迭代，其效果好得惊人。数百万次的键路径访问和数百万次的字符串比较在一秒内就能完成——与不带索引搜索时 SQLite 的优化版本相比，并没有明显慢多少。
