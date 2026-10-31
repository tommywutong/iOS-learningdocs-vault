---
title: 'Friday Q&A 2009-04-10：ChemicalBurn 中的多线程优化'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2009-04-10-multithreaded-optimization-in-chemicalburn.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6d95bb4add8cf151'
translated: true
---

> 原文：[Friday Q&A 2009-04-10: Multithreaded Optimization in ChemicalBurn](https://www.mikeash.com/pyblog/friday-qa-2009-04-10-multithreaded-optimization-in-chemicalburn.html)　·　mikeash.com Friday Q&A

发布于 2009-04-10 17:22 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2009-04-17: Code Generation with LLVM, Part 1: Basics](https://www.mikeash.com/pyblog/friday-qa-2009-04-17-code-generation-with-llvm-part-1-basics.html)  
上一篇文章：[Friday Q&A 2009-04-03: On Hold](https://www.mikeash.com/pyblog/friday-qa-2009-04-03-on-hold.html)  
标签：[chemicalburn](https://www.mikeash.com/pyblog/?tag=chemicalburn) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [performance](https://www.mikeash.com/pyblog/?tag=performance) [threading](https://www.mikeash.com/pyblog/?tag=threading)

Friday Q&A 2009-04-10：ChemicalBurn 中的多线程优化

作者：[Mike Ash](https://www.mikeash.com/)

**背景**

如果你还不熟悉 [ChemicalBurn](http://www.mikeash.com/?page=software/chemicalburn/)，应该去看看。本质上，它展示一个网络，包裹在网络中被路由。窍门在于：网络的性能会随包裹移动而改变，从而形成一个有趣的动态系统。

若想跟着看，[源代码](http://www.mikeash.com/svn/ChemicalBurn/) 也可用。

ChemicalBurn 的核心是路由算法。在每个时间步，系统内会生成包裹。它们被赋予随机源和随机目的地。给定全部连接及其速度，系统会计算最优路径。由于连接随时可能变化，包裹每到达一个中间节点，就会重新做一次路由。图形只是简单的 OpenGL，别的也不多，路由算法很容易成为整个屏保的瓶颈。

**算法**  
路由方法位于 [ChemicalBurnView](http://www.mikeash.com/svn/ChemicalBurn/ChemicalBurnView.m)。因为高度优化而有点乱，但它只是标准寻路算法 [Dijkstra 算法](http://en.wikipedia.org/wiki/Dijkstra's_algorithm) 的实现。（后排那些跳着喊 [A*](http://en.wikipedia.org/wiki/A*_search_algorithm) 的同学请注意：ChemicalBurn 不太适合 A*，因为缺乏好的启发函数。）

完整说明请点链接，但算法基础其实很简单。图中每个节点有一个代价和一个前驱。维护一个节点队列，初始化时放入起点。在循环中，从队列弹出代价最小的节点。枚举它的所有连接。若到达该节点的代价加上连接代价，比另一节点当前记录的代价更小，就把另一节点的代价设为这个和，并把其前驱设为刚弹出的节点。一旦弹出目的节点，沿前驱链回溯，就得到到目的地的最便宜路径。

**优先队列**  
该算法的心脏是待处理节点的队列。我最初的实现只是把它们存进 NSMutableSet。要取最便宜的那个，就遍历集合找代价最低的。这个队列可能变得很大，而搜索发生在屏保主要热点内层循环的每一次，所以非常慢。

这里容易的答案是改用优先队列。如果你还不熟悉：这是一种专用数据结构，能高效支持添加任意元素，以及按某种任意比较取出「最小」元素。我选择给 C++ STL 的堆算法写了[一个包装](http://www.mikeash.com/svn/ChemicalBurn/ChemicalBurnOrderedQueue.mm)。另一个不错的选择是 CoreFoundation 里的 [CFBinaryHeap](http://developer.apple.com/documentation/CoreFOundation/Reference/CFBinaryHeapRef/index.html) 类。仅这一处改动就带来了可观加速。

**内联元数据**  
路由算法依赖每个节点的两块元数据。原先我用两个 CFMutableDictionary，以节点为键，代价和回指指针为值。但这些值在这个极热的循环里不断被取、被设，即便通常很快的字典查找也开始变慢。解决方案很容易，实际上也是实现 Dijkstra 算法的常见做法：把这两个值存在节点自身上。我把它们做成公开实例变量，慢的字典查找就变成了快的 ivar 查找。

**多线程**  
由于每个包裹的路由彼此独立，而在计算受限的情况下每帧需要为许多包裹做路由，给寻路代码加多线程是获得更多速度的明显办法。

我如何实现多线程本身并不特别有趣。我采用了明显且标准的做法：按机器处理器核心数派生同样多的工作线程，再把包裹推进一个由工作线程访问的队列。

不过有个麻烦。我说每个包裹的路由彼此独立，其实并不完全如此。在原先实现里是独立的，但**内联元数据**优化把这搞砸了。每个节点上的值在概念上私属于每一次单独的路由问题，但存进实例变量后它们全局可见，于是工作线程势必会争抢它们。

解决这个问题的技巧是：不只存一对值，而是存一个值数组。[ChemicalBurnNode](http://www.mikeash.com/svn/ChemicalBurn/ChemicalBurnNode.h) 类最终看起来像这样：

```
    @class ChemicalBurnNode;
    struct ChemicalBurnNodePerThread {
        unsigned             cost;
        ChemicalBurnNode*    prev;
    };
    
    @interface ChemicalBurnNode : NSObject {
        unsigned             mID;
        NSPoint              mPos;
        
        @public
        struct ChemicalBurnNodePerThread    mPerThread[0];
    }
```

那个 `[0]` 是实现变长数组的技巧。我不想把最大线程数写死，然后过几年来个巨大的多核怪兽却用不上。为给数组准备存储，我在[实现](http://www.mikeash.com/svn/ChemicalBurn/ChemicalBurnNode.m)里重写 `+allocWithZone:`，多分配一些空间：

```
+ allocWithZone: (NSZone *)zone
    {
        unsigned extraBytes = gProcessorCount * sizeof( struct ChemicalBurnNodePerThread );
        return NSAllocateObject( self, extraBytes, zone );
    }
```

这解决了存储问题，但还留下如何选择数组下标的问题。显然每个线程需要选不同的下标。显然每个线程需要选一个小数字。

我为此写了一对函数：

```
    // the key parameter allows multiple independent views to share IDs
    // IDs will count up from 0 based on the unique key passed in
    int NodeGetThreadID( void *key );
    void NodeThreadIDCleanup( void *key );
```

思路是：不同线程调用 `NodeGetThreadID` 时，返回值从 0 开始，每出现一个新线程就递增。做法是用 `pthread_getspecific` 按线程存储 ID，并用 [CFBag](http://developer.apple.com/DOCUMENTATION/CoreFoundation/Reference/CFBagRef/index.html) 跟踪给定 key 已有多少线程请求过 ID，好让每个新线程拿到合适的 ID。实现如下：

```
    int NodeGetThreadID( void *key )
    {
        // we store ID + 1 because NULL is used to indicate "does not exist"
        int threadID = (int)pthread_getspecific( gThreadIDKey );
        if( threadID == 0 )
        {
            pthread_mutex_lock( &gIDMutex );
            CFBagAddValue( gIDs, key );
            threadID = CFBagGetCountOfValue( gIDs, key );
            pthread_mutex_unlock( &gIDMutex );
            
            pthread_setspecific( gThreadIDKey, (void *)threadID );
            
            if( threadID > gProcessorCount )
                NSLog( @"Attempted to get ID for thread #%d, more than allowed!", threadID );
        }
        
        return threadID - 1;
    }
    
    static void MakeKey( void )
    {
        int err = pthread_key_create( &gThreadIDKey;, NULL );
        if( err )
            NSLog( @"%s: pthread_key_create returned %d", __func__, err );
    }
    
    void NodeThreadIDCleanup( void *key )
    {
        while( CFBagGetCountOfValue( gIDs, key ) )
            CFBagRemoveValue( gIDs, key );
    }
```

（`MakeKey` 函数只从该类的 `+initialize` 方法调用一次。）

就这些，就足以让这段代码与多个工作线程和谐相处，同时仍能快速访问两块关键的节点元数据。

**结论**  
我已经很久没动 ChemicalBurn 了，但印象中这些优化合在一起，在我的 4 核 Mac Pro 上从始至终大概带来了约 100 倍加速。

所有这些优化都相对明显、直接，但效果也极其显著。这里有一套不错的优化技术组合。用优先队列代替集合，对算法整体性能影响巨大，因为优先队列是 `O(log n)`，而集合是 `O(n)`。把节点元数据挪成节点对象的 ivar 是纯粹的微优化，但由于那份数据被访问得极为频繁，收益也很可观。然后给路由代码加多线程，是利用并行计算的明显办法。

本周的 Friday Q&A 就到这里。下周再来，但愿上周害我没法写稿的那些腊肠犬别再挡路，我就能再谈一个读者贡献的话题。记住，Friday Q&A 靠你们的想法驱动。若有问题或想讨论的话题，请在评论里发，或[发邮件给我](mailto:mike@mikeash.com)（若不想我用你的名字请说明）。

对本代码有问题或评论？想讲自己的优化战争故事？请在下面发表评论。

喜欢这篇文章吗？我在卖整本整本的书！第二卷和第三卷已经出了！有 ePub、PDF、纸质版，以及 iBooks 和 Kindle。[点此了解更多](https://www.mikeash.com/book.html)。

---

尚无评论。

写下你的想法，发表评论：

垃圾信息和跑题帖会不经通知删除。肇事者可能由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
