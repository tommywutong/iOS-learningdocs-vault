---
title: 'NSArray 与 NSSet、NSDictionary 与 NSMapTable | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/08/nsarray-or-nsset-nsdictionary-or.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:56561f873993626f'
translated: true
---

> 原文：[NSArray 与 NSSet、NSDictionary 与 NSMapTable | Cocoa with Love](https://www.cocoawithlove.com/2008/08/nsarray-or-nsset-nsdictionary-or.html)　·　Cocoa with Love (Matt Gallagher)

有些数据类型可以用不止一种集合（collection）来存储。已经保证唯一的无序对象，既可以存入 NSArray，也可以存入 NSSet。凡是 NSDictionary 能存储的内容，NSMapTable 也都能存储。在这篇文章中，我测量了创建和使用这些不同选项的性能，以帮助你选择哪种方案最适合你。

## 消歧

几周前，我写过一篇关于 [NSMapTable 和 NSDictionary](https://www.cocoawithlove.com/2008/07/nsmaptable-more-than-nsdictionary-for.html) 可以用不同方式存储不同类型数据的文章。有人立刻问：“在存储_相同_数据时，哪个更快？”我虽然能猜到，但并不真正了解。

然后我开始思考其他可能存在歧义的集合选择。我意识到，我写的代码中存储着一组已经保证唯一、无序的对象——只是为了能遍历它们。我为此使用了 NSSet（因为该类定义是“唯一且无序”），但在创建集合之前，这些对象已经保证是唯一的，于是我想：如果改用 NSArray，我的代码能高效多少？

因此，有以下两种情况需要测试性能：

- NSArray 与 NSSet
- NSDictionary 与 NSMapTable

请记住，这些测试仅适用于两种集合在技术上都能容纳相同数据的情况。

## 方法

你可以[下载我用于测试的代码](https://www.cocoawithlove.com/assets/objc-era/MapTablePerformanceTest.m.zip)。

简而言之，我创建了两个数据数组：

- “键”数组——一个 NSString 数组，其中每个字符串是一个 10 位数字字符串，内容是它索引的字符串表示形式。
- “对象”数组——一个 NSNumbers 数组，其中每个数字是一个整数，设置为其索引。

我用这些数组中的各一百万个对象进行了测试（n = 1,000,000）。

这些数组依次用于提供我将要测试的集合的数据。单列集合（NSArray 和 NSSet）仅从“对象”源数组中取对象来创建和测试。双列集合（NSMapTable 和 NSDictionary）从“键”和“对象”源数组中取对象来创建和测试。

我的测试机器是一台 PPC G5 2x2Ghz。垂死的平台万岁！

## 结果

### NSArray 与 NSSet

| 测试 | NSArray 用时 | NSSet 用时 |
|---|---|---|
| 增量创建（未设置 capacity） | 0.582256 秒 | 2.67101 秒 |
| 增量创建（正确设置 capacity） | 0.572139 秒 | 0.930725 秒 |
| 遍历内容 | 0.004713 秒 | 0.025864 秒 |

顺便提一下，使用 `setWithArray:` 构建 NSSet 所需时间与“未设置 capacity”相同，因此如果你知道数组中的对象是唯一的，最好自行设置 capacity 并复制数据。

### NSArray 与 NSSet 的查找

_注_：这些结果是在 n = 10,000 时生成的

| 测试 | NSArray 用时 | NSSet 用时 |
|---|---|---|
| 查找所有对象 | 29.2667 秒（indexOfObject:） 0.185051 秒（indexOfObjectIdenticalTo:） | 0.00833601 秒 |

这些结果应该不会令人意外。此测试是为了完整性而包含的，因为两种集合都能进行包含性检查。

在数组中查找对象适用于 n < 100 的情况。如你所见，当 n = 10,000 时，NSArray 测试的 O(n^2) 特性（一次 O(n) 的查找乘以 n 次查找）使其相比 NSSet 测试的 O(n) 特性（常数时间查找乘以 n 次查找）成为一个糟糕的选择。我不打算等待 n = 1,000,000 时的此测试，但我向你保证，两种 NSArray 方法都会花费数分钟甚至数小时的时间。

### NSDictionary 与 NSMapTable

| 测试 | NSDictionary 用时 | NSMapTable 用时 |
|---|---|---|
| 构造 | 3.45922 秒 | 2.32607 秒 |
| 遍历键并查询每个对象 | 0.60859 秒 | 0.770289 秒 |

## 结论

没错，对于单纯的存储和遍历，NSArray 比 NSSet 更快。构造时至少快 50%，遍历时最多快 500%。教训：如果你只需要遍历内容，不要使用 NSSet。

当然，如果你需要测试包含性，就要尽量避免使用 NSArray。即使你既需要遍历_又_需要测试包含性，你可能仍然应该选择 NSSet。如果你需要保持集合有序，同时还要测试包含性，那么你应该考虑维护两个集合（一个 NSArray 和一个 NSSet），每个集合包含相同的对象。

NSDictionary 的构造比 NSMapTable 慢——因为它需要拷贝键数据。但它通过更快的查找弥补了这一点。当然，这两者具有不同的能力，因此大多数情况下，这种抉择应该基于其他因素做出。
