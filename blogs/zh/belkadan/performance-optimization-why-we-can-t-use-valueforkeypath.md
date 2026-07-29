---
title: '性能优化：为什么我们不能使用 valueForKeyPath:'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2007/10/Performance-Optimization-Why-We-Cannot-Use-valueForKeyPath/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:eb05736a08bf8335'
translated: true
---

> 原文：[Performance Optimization: Why We Can't Use valueForKeyPath:](https://belkadan.com/blog/2007/10/Performance-Optimization-Why-We-Cannot-Use-valueForKeyPath/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Xcode 小技巧：插件](https://belkadan.com/blog/2007/09/Short-Xcode-Tip-on-Plugins/)

[GenericToolbar 与 IB3](https://belkadan.com/blog/2007/12/GenericToolbar-and-IB3/) »

[NSNumber、CFNumber 和 CFBoolean](https://belkadan.com/blog/2008/01/NSNumber-CFNumber-and-CFBoolean/?tag=cocoa) »

## [性能优化：为什么我们不能使用 valueForKeyPath:](#)

最近我在写代码时，发现自己需要在一个字典里往下取三级深度的数据。看到下面这段代码我立刻皱起了眉头：

```
[[[info objectForKey:@"tile-data"] objectForKey:@"file-data"] objectForKey:@"_CFURLStringType"];
```

为什么？因为它太丑了。我是说，从字典里取一个对象的代码完全掩盖了我在取哪个对象。如果能直接这样写就漂亮多了：

```
[info valueForKeyPath:@"tile-data.file-data._CFURLStringType"]
```

但我还是谨慎地跑了一下速度测试，使用了 Mike Ash 在他自己的[性能测试](http://mikeash.com/blog/pivot/entry.php?id=29)中用的测试框架。结果如下：

| 名称 | 迭代次数 | 总时间（秒） | 每次耗时（纳秒） |
|---|---|---|---|
| objectForKey x3 | 10000000 | 5.0 | 497.1 |
| valueForKey x3 | 10000000 | 5.6 | 561.9 |
| valueForKeyPath | 10000000 | 71.9 | 7186.2 |

看起来 `valueForKeyPath:` 比重复调用 `objectForKey:` **慢了十倍以上**。即使你需要跑一千万次才能看到这个差异，这样的性能差距也相当显著了。（好奇的话，`objectForKey:` 和 `valueForKey:` 的耗时大致与创建和释放一个 `NSAutoreleasePool` 相当；`valueForKeyPath:` 则比创建一个 `NSButtonCell` 稍慢一些。所以无论哪种方式其实都没那么慢。）

这是相当有力的证据。看来在养成习惯之前，我还是要牺牲掉更漂亮的语法了。

_注：本测试中我没有特意排除所有其他因素，例如各个键的长度、键路径中包含的键数，甚至当时计算机上还运行着什么其他程序。（最后一点我知道影响很大，尽管我确实避免在测试时进行其他操作。）我只是用上面给出的键路径测试了同一个字典（每个测试加载一次，不计入计时）。如果性能结果更接近，我可能会做更精确的测试，但结果差距实在太大，所以就不必了。_

本文发布于 [2007 年 10 月](https://belkadan.com/blog/2007/10) [27 日](https://belkadan.com/blog/2007)，归类于[技术](https://belkadan.com/blog/technical)。标签：[Cocoa](https://belkadan.com/blog/tags/cocoa)
