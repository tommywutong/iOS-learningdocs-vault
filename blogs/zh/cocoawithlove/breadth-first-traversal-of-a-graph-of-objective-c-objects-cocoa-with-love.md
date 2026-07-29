---
title: 'Objective-C 对象的图广度优先遍历 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/02/breadth-first-traversal-of-graph-of.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:a165476c8924bc7e'
translated: true
---

> 原文：[Breadth-first traversal of a graph of Objective-C objects | Cocoa with Love](https://www.cocoawithlove.com/2009/02/breadth-first-traversal-of-graph-of.html)　·　Cocoa with Love (Matt Gallagher)

如果你在 Objective-C 中有一组互相关联的对象，从最近到最远的顺序遍历它们的最佳方式是什么？`NSMutableSet` 的方法是否适合跟踪已经访问过的节点？相对于深度优先搜索（不需要 FIFO 队列），`NSMutableArray` FIFO 队列会带来多少额外开销？当对象被推入队列前端或后端时，`NSMutableArray` 的性能是否有所不同？在这篇文章中，我将回答这些问题以及更多内容。

## 图论

在编程中，图（graph）是任何一组连接的数据对象。

如果这对你来说是新的信息，那么我建议你阅读一下 Wikipedia 页面：[Graph (computer science)](http://en.wikipedia.org/wiki/Graph_(computer_science))，然后阅读它所链接的所有页面，再针对每个链接页面阅读它们所链接的所有页面。当讽刺意味显现出来后，再回到这一页。

处理图中节点的两种常见方式是深度优先遍历和广度优先遍历。广度优先图遍历通常比深度优先遍历稍微难写一些，因为我们还需要维护一个 FIFO 队列来处理待处理的节点。

当图中的所有节点都是 Objective-C 对象，并且使用 `NSMutableArray` 来维护 FIFO 队列时，最快的遍历方式是什么？我测试了几种不同的方法来看看哪个效果最好。

## 用于测试的图

我所有的测试都在这样的图中进行：图中的每个节点连接到另外两个节点，直到图的中间层，然后节点对随后连接到一个节点，直到图最终汇聚回一个节点。

这种图结构的一个示例（水平显示以便各层按列对齐），包含两个递增层和两个递减层：

![](https://www.cocoawithlove.com/assets/objc-era/graph.png)

由于有两个递增层和两个递减层，我将其称为「半深度（half-depth）」为 2。我将通过它们的「半深度」来指代所有后续图的大小。

所有节点都是以下类的对象：

```objc
@interface Node : NSObject
{
    NSSet *linkedNodes;
}
@property (nonatomic, retain) NSSet *linkedNodes;
@end
```

这些类不存储任何有用信息，但这并不是这些测试的重点：我只测试遍历性能。

## 初始方法

基本算法是：

1. 创建一个集合（set）来跟踪已经访问过的节点
2. 创建一个数组（array）来队列待处理的节点
3. 对于待处理数组中的每个节点（按顺序）：

    1. 获取连接到当前节点的集合
    2. 从连接集合中排除我们已经访问过的节点
    3. 将未排除的连接节点添加到待处理数组

我编写的第一段实现此算法的代码是：

```objc
NSMutableSet *visitedNodes = [NSMutableSet setWithObject:startingNode];
NSMutableArray *queue = [NSMutableArray arrayWithObject:startingNode];

while ([queue count] > 0)
{
    NSMutableSet *newNodes =
        [[((Node *)[queue lastObject]).linkedNodes mutableCopy] autorelease];
    [newNodes minusSet:visitedNodes];
    
    [visitedNodes unionSet:newNodes];
    [queue
        replaceObjectsInRange:NSMakeRange(0, 0)
        withObjectsFromArray:[newNodes allObjects]];
    
    [queue removeLastObject];
}
```

这段代码使用 `NSMutableSet` 自身的集合操作符来排除已访问节点。它还将新对象推入 `queue` 的前端，并从末尾弹出每个节点进行处理。

那么，这种方法的性能如何？一句话：糟糕至极——而这要归咎于 `-[NSMutableSet minusSet:]`。

> **教训 1：**  
> 只有当 `setOne` 大于 `setTwo` 时，才应使用 `[setOne minusSet:setTwo]`。此方法的运行时间为 O(_n_)，其中 _n_ 是 `setTwo` 的大小。在上面代码中，`visitedNodes` 可能比 `newNodes` 大几个数量级，因此我们自己遍历 `newNodes` 并排除在 `visitedNodes` 中找到的节点会快得多。这样我们的运行时间为 O(_m_)，其中 _m_ 是 `newNodes` 的大小（对于这个测试用例来说，实际上很小且恒定）。

方法 `minusSet:` 确实应该遍历接收者和参数中较小的那个集合。然而，由于它不会这样做，我们必须避免使用它。

## 从前端到后端还是从后端到前端

接下来要解决的问题：将对象推入 `NSMutableArray` 的前端并从末尾弹出更快，还是推入末尾并从前端弹出更快？

以下是将对象推入前端：

```objc
while ([queue count] > 0)
{
    NSSet *newNodes = ((Node *)[queue lastObject]).linkedNodes;
    for (Node *newNode in newNodes)
    {
        if (![visitedNodes containsObject:newNode])
        {
            [visitedNodes addObject:newNode];
            [queue insertObject:newNode atIndex:0];
        }
    }

    [queue removeLastObject];
}
```

这是将对象推入后端：

```objc
while ([queue count] > 0)
{
    NSSet *newNodes = ((Node *)[queue objectAtIndex:0]).linkedNodes;
    for (Node *newNode in newNodes)
    {
        if (![visitedNodes containsObject:newNode])
        {
            [visitedNodes addObject:newNode];
            [queue addObject:newNode];
        }
    }

    [queue removeObjectAtIndex:0];
}
```

测试结果，在图的半深度为 8、12、16 和 20（从 766 到 3145726 个节点）的情况下，推入后端（第二种方法）始终快 5%。

> **教训 2：**  
> 向 `NSMutableArray` 的末尾添加元素是唯一快速的操作——大多数其他操作都慢得多。如果操作次数相等，请优先选择向数组末尾添加元素的算法。

## 其他测试的问题

### 局部的 `NSAutoreleasePool` 对这样的小循环有帮助吗？

将上述循环的主体包裹在 `NSAutoreleasePool` 中以局部释放存储，导致耗时增加了 25%。

这些循环内部没有自动释放任何内存（`NSMutableArray` 和 `NSMutableSet` 手动维护自己的内存），因此自动释放池（autorelease pool）是徒劳的。

### 用 `NSOperationQueue` 作为 FIFO 队列更快吗？

将循环的内容移入一个 `NSOperation` 对象中，并将每个操作推入 `NSOperationQueue` 来遍历图，使得整体遍历速度慢了大约 100 倍。

创建每个操作对象所涉及的额外工作，以及 `NSOperationQueue` 在不同 CPU（我有一台 2 × PPC G5 CPU 的机器）之间分配任务、等待每个线程启动和结束的开销都很大。

此外，虽然 `NSOperationQueue` 是一个 FIFO 队列，但只有在我们将 `maxConcurrentOperationCount` 设置为 1 时，任务才会按顺序执行，因此使用 `NSOperationQueue` 并没有真正获得任何好处。

`NSOperationQueue` 旨在用于规模不小的独立（可线程化）操作。这个循环内部的情况不符合这一期望。

### FIFO 队列会带来多少额外开销？

检查这一点的唯一方法是使用递归算法进行深度优先搜索。

```objc
void RecursivelyTraverse(Node *node)
{
    NSSet *newNodes = node.linkedNodes;
    for (Node *newNode in newNodes)
    {
        if (![recursiveSet containsObject:newNode])
        {
            [recursiveSet addObject:newNode];
            RecursivelyTraverse(newNode);
        }
    }
}
```

测试结果，在半深度为 8、12、16 和 20 的情况下，递归算法始终快一倍。

> **教训 3：**  
> 使用 `NSMutableArray` 作为 FIFO 队列会为每个节点增加一个恒定的额外时间。在这个简单的测试中，额外时间占节点计算量的一半，但如果你对每个节点有显著额外的计算要执行，那么 FIFO 队列的开销相对于算法其余部分可能微不足道。

## 结论

> 你可以下载我使用的测试代码：[FIFOQueues.zip](https://www.cocoawithlove.com/assets/objc-era/FIFOQueues.zip)（46kB）

即使是在如此简单的算法中，也有一些教训值得学习。对我来说最大的惊喜是，我不能信任 `minusSet:` 会以最有效的方式工作。我想我需要就此向 Apple 提交一个 bug。

`NSMutableArray` 并非前后对称，尽管差异足够小，以至于可能并不总是重要。

像 `NSOperationQueue` 这样的工具在一定程度上有助于多线程，但在这类小段代码上效果不佳。像这样的小循环更适合向量化（SSE 或 Altivec）而非并行化——但你无法对包含 Objective-C 方法调用的循环进行向量化，所以这仍然不可行。
