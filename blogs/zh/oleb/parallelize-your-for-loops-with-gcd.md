---
title: 用 GCD 并行化你的 for 循环
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/07/parallelize-for-loops-gcd-dispatch_apply/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:07b4315bf3c50f1e'
translated: true
---

> 原文：[Parallelize Your for Loops With GCD](https://oleb.net/blog/2013/07/parallelize-for-loops-gcd-dispatch_apply/)　·　Ole Begemann

# 用 GCD 并行化你的 for 循环

# Cocoa 集合的并发迭代

Foundation 提供了一系列便捷方法来枚举集合（collection）中的条目，例如 [`enumerateObjectsUsingBlock:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-SW19)。通过向同一方法的更详细版本 [`enumerateObjectsWithOptions:usingBlock:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-SW18) 传入 [`NSEnumerationConcurrent`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Miscellaneous/Foundation_Constants/Reference/reference.html#//apple_ref/doc/uid/TP40003793-CH3g-SW193) 标志，你可以轻松地将集合中每个元素上执行的 block 并行化。

# Grand Central Dispatch 中的并发迭代

通过阅读优秀的 [objc.io 第二期](http://www.objc.io/issue-2/)，我最近了解到 [Grand Central Dispatch](http://developer.apple.com/library/ios/#documentation/Performance/Reference/GCD_libdispatch_Ref/) 在更低的层次上包含一个非常类似的模式，适用于你遍历的对象不是 Cocoa 集合的情况：[`dispatch_apply()`](http://developer.apple.com/library/ios/documentation/Performance/Reference/GCD_libdispatch_Ref/Reference/reference.html#//apple_ref/doc/uid/TP40008079-CH2-SW5) 函数。

`dispatch_apply()` 会在指定的调度队列（dispatch queue）上执行给定的 block _n_ 次，并将当前的迭代索引传递给该 block。然后该函数会等待所有迭代完成后再返回。如果你将一个并发队列传递给 `dispatch_apply()`，基本上可以把这个结构看作是一个并行（且高效，如文档所述）的 `for` 循环。

在合适的地方使用 `dispatch_apply()` 有可能带来巨大的性能提升。如果你的代码逐像素处理图像，或逐字节遍历其他内存区域，那么一定要关注这个功能。然而，正如 Daniel Eggert 在[他的文章](http://www.objc.io/issue-2/low-level-concurrency-apis.html#iterative_execution)中所强调的，你应该仔细衡量并行化带来的性能影响。它甚至可能产生负面影响：

> 这种方法的效果在很大程度上取决于你在循环内部具体做什么。
> 
> block 内完成的工作必须是非平凡的（non trivial），否则开销就太大了。除非代码受计算带宽限制，否则关键在于每个工作单元需要读取和写入的内存能够很好地适配到缓存大小。这会对性能产生巨大影响。受临界区（critical section）限制的代码可能根本无法很好地运行。
