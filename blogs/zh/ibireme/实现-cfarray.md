---
title: 实现 CFArray
source: ibireme (郭曜源)
source_key: ibireme
source_url: 'https://blog.ibireme.com/2014/02/17/cfarray/'
original_language: zh
published: 2014-02-17
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:5b5ef458ba3e5a42'
translated: n/a
---

> 原文：[实现 CFArray](https://blog.ibireme.com/2014/02/17/cfarray/)　·　ibireme (郭曜源)

平时都在用 NSArray，但最近搞一个纯C的库，不想有太多依赖，所以想把 NSArray 的功能提取出来。NSArray 和 CFArray 是 Toll-Free bridged的，而且 CFArray 是开源的。所以这里研究了一下 CFArray 的实现，并且给出一个纯C的、无其他依赖的替代实现。

### 苹果的实现

在翻CF的源码前，我在网上找到一篇很有意思的老文章：[http://ridiculousfish.com/blog/posts/array.html](http://ridiculousfish.com/blog/posts/array.html) (2005年)。这篇文章里面，对 CFArray 和 STL Vector 做了一次性能对比，结果如下：  
 [![vector_results](https://blog.ibireme.com/wp-content/uploads/2014/02/vector_results.jpg)](https://blog.ibireme.com/wp-content/uploads/2014/02/vector_results.jpg)[![cfarray_results](https://blog.ibireme.com/wp-content/uploads/2014/02/cfarray_results.jpg)](https://blog.ibireme.com/wp-content/uploads/2014/02/cfarray_results.jpg)

这篇文章写于2005年，那时的 CFArray 实现的非常有意思：在 CFArray 容量超过300000左右时，消耗的时间完全变了。我很好奇的测试了一下现在系统的实现，已经跟那时的结果完全不一样了。于是我翻了一下CF的历史源码，看到了 CFArray 这些年的变化。

1.最开始，CFArray 底层是用 [deque](http://en.wikipedia.org/wiki/Double-ended_queue)([双端队列](http://zh.wikipedia.org/wiki/%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97))实现的，在头部尾部进行插入删除性能很高，但是在 deque 中间插入删除时，就需要 memmove 来挪动内存了，性能就会降下来。苹果的方法是，当 CFArray 长度超过某个数值(具体来说是262040)时，将底层的 deque 换成 [balanced tree](http://en.wikipedia.org/wiki/Balanced_tree)。

具体来说，苹果写了一个名为 [CFStorage](http://www.opensource.apple.com/source/CF/CF-855.11/CFStorage.h) 的类，用 balanced tree 实现了大数量的数值的存储和编辑，并且在插入和删除时有很好的性能。CFArray 在长度达到阈值(262040)时，就会在底层替换为CFStorage来完成操作。

2. 但是在2011年，CF-635.15中，苹果把这个特性去掉了。具体的对比可以看下面两个文件。  
 [http://opensource.apple.com/source/CF/CF-550/CFArray.c](http://opensource.apple.com/source/CF/CF-550/CFArray.c)  
 [http://opensource.apple.com/source/CF/CF-635.15/CFArray.c](http://opensource.apple.com/source/CF/CF-635.15/CFArray.c) 在这之后， CFArray 就只是用简单的deque实现了，长度越大，位于中间的插入删除耗时就越长。至于为什么这么改？我也不知道。。也许是怕切换数据结构造成的时间抖动？也许是这个 feature 根本没有多少人用到？

3.最新的 CFArray 中，代码应该又调整了。性能比单纯的[双端队列](http://zh.wikipedia.org/wiki/%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97)高，我猜测应该换成了一个[环形缓冲区](http://zh.wikipedia.org/wiki/%E5%9C%86%E5%BD%A2%E7%BC%93%E5%86%B2%E5%8C%BA)。但是苹果还没有开源最新的代码。

### 我的测试和实现

在我的系统(10.9.1)里面，我参考最新的 CFArray 源码实现了一个纯 C 的 deque。随后与系统CFArray做性能对比，发现在随机插入的时候，系统的CFArray仍然有更高的性能。当我把deque换成circular后再进行对比，性能就完全一致了。所以，我猜测现在系统的 CFArray 底层又换成了 [circular](http://en.wikipedia.org/wiki/Circular_buffer)，只是最新的代码还没有开源出来。

我的实现代码放到了 [https://github.com/ibireme/yy_music_base/blob/master/yy_music_base/ym_array.c](https://github.com/ibireme/yy_music_base/blob/master/yy_music_base/ym_array.c)，里面有个纯C的、简单的引用计数对象的实现，有个 CFMutableArray 和 CFMutableDictionary 的模仿实现。所有 API 都和 CoreFoundation 类似。 还没有没仔细 test，但应该没什么大问题。

下面是我自己的实现和CFArray的一个性能对比：除去随机数的影响，插入性能应该是一致的。  
 [![yy_array_time_cost](https://blog.ibireme.com/wp-content/uploads/2014/02/yy_array_time_cost.png)](https://blog.ibireme.com/wp-content/uploads/2014/02/yy_array_time_cost.png)

### 结论

好了，现在可以回头看看苹果给出的时间复杂度的描述了：

```
Computational Complexity
The access time for a value in the array is guaranteed to be at
worst O(lg N) for any implementation, current and future, but will
often be O(1) (constant time). Linear search operations similarly
have a worst case complexity of O(N*lg N), though typically the
bounds will be tighter, and so on. Insertion or deletion operations
will typically be linear in the number of values in the array, but
may be O(N*lg N) clearly in the worst case in some implementations.
There are no favored positions within the array for performance;
that is, it is not necessarily faster to access values with low
indices, or to insert or delete values with high indices, or
whatever.
```

用开头那篇博客的话来说：Don’t second guess Apple, because Apple has already second guessed YOU.

PS: [NSMutableArray arrayWithCapacity:xxx]中的capacity没有任何作用。。仅仅是一个hint而已。。
