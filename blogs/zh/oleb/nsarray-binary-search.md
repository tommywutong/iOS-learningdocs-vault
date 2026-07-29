---
title: NSArray 二分查找
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2013/07/nsarray-binary-search/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:890103f0b8555f48'
translated: true
---

> 原文：[NSArray Binary Search](https://oleb.net/blog/2013/07/nsarray-binary-search/)　·　Ole Begemann

# NSArray 二分查找

前几天我了解到，[`NSArray`](https://developer.apple.com/library/ios/#documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html) 提供了一个名为 [`indexOfObject:inSortedRange:options:usingComparator:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-SW31) 的二分查找（binary search）方法。使用该方法可以极大地加快搜索速度，但要求数组必须已排序。

# containsObject: 和 indexOfObject:

你可能熟悉搜索 NSArray 最常用的方法：[`containsObject:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-BABCEJDI) 会告诉你其参数是否存在于数组中，而 [`indexOfObject:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-BABDHGFB) 则返回该对象所在位置的索引。这两种方法都会从索引 0 开始，遍历数组中的所有元素，直到找到匹配项。在最坏的情况下（没有匹配项），它们必须遍历整个数组。用[大 O 表示法](https://en.wikipedia.org/wiki/Big_O_notation)来说，这些方法的性能特征是 O(n)。

对于只有几十个元素的小数组来说，这通常不是问题。但如果你的代码经常需要在包含数千个元素的数组中查找对象，你可能需要寻找一种更快的搜索算法。

**2013 年 7 月 11 日更新：** [Bavarious](https://objectivistc.tumblr.com) 提醒我，尽管名字如此，`NSArray` [并不一定是以数组特性实现的](https://twitter.com/bavarious/status/355252119542042624)。事实上，[`CFArray` 的头文件](http://www.opensource.apple.com/source/CF/CF-744/CFArray.h)（`NSArray` 基于它实现）在计算复杂度方面有如下说明：

> 对于任何当前和未来的实现，数组中某个值的访问时间在最坏情况下保证不超过 O(lg N)，但通常会是 O(1)（常数时间）。线性搜索（linear search）操作在最坏情况下的复杂度同样为 O(N*lg N)，不过通常边界会更紧一些，以此类推。

换句话说：由于随机访问（random access）不能保证具有常数时间的性能特征，线性搜索在实际中可能比 O(n) 还要慢。由于二分查找也基于随机元素访问（见下文），与纯数组相比，它的最坏情况性能退化与线性搜索类似。但将这两种算法相互比较，二分查找仍然遥遥领先。

如果你想了解更多关于 `CFArray`/`NSArray` 的令人惊讶的性能特征，我推荐[这篇 2005 年的文章](http://ridiculousfish.com/blog/posts/array.html)。

# 二分查找

如果数组是按搜索键排序的，[二分查找](https://en.wikipedia.org/wiki/Binary_search_algorithm)可以为你带来巨大的性能提升。通过将数组的中间元素与搜索项进行比较，该算法在每次迭代中有效地将需要搜索的元素数量减半。二分查找具有 O(log n) 的性能。这在实际中意味着什么？使用二分查找搜索一个包含 100,000 个元素的已排序数组最多需要 17 次比较，而朴素的线性搜索平均需要进行 50,000 次比较。

以下是执行二分查找所需的全部步骤：

```
NSArray *sortedArray = ... // must be sorted
id searchObject = ...
NSRange searchRange = NSMakeRange(0, [sortedArray count]);
NSUInteger findIndex = [sortedArray indexOfObject:searchObject
                                    inSortedRange:searchRange
                                          options:NSBinarySearchingFirstEqual
                                  usingComparator:^(id obj1, id obj2)
                                  {
                                      return [obj1 compare:obj2];
                                  }];
```

请注意，[排序数组](https://en.wikipedia.org/wiki/Sort_algorithms#Comparison_of_algorithms)至少是一个 O(n) 操作，更可能是 O(n log n) 的量级。因此，如果你只需要进行一次搜索，先对数组排序（使用 [`sortedArrayUsingComparator:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSArray_Class/NSArray.html#//apple_ref/doc/uid/20000137-SW28) 或类似方法）是没有意义的。

# 在插入新对象时保持数组已排序

你还可以使用 `indexOfObject:inSortedRange:options:usingComparator:` 方法，在插入新对象时保持已排序数组的排序状态。当你使用 `NSBinarySearchingInsertionIndex` 选项调用该方法时，它会返回一个索引，你应该在该索引处插入新对象以保持数组已排序。
