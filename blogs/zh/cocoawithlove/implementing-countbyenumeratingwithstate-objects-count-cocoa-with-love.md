---
title: '实现 countByEnumeratingWithState:objects:count: | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/05/implementing-countbyenumeratingwithstat.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:09990ef4b0c1ecb0'
translated: true
---

> 原文：[Implementing countByEnumeratingWithState:objects:count: | Cocoa with Love](https://www.cocoawithlove.com/2008/05/implementing-countbyenumeratingwithstat.html)　·　Cocoa with Love (Matt Gallagher)

如果你想在自己的类上使用快速枚举（fast enumeration），就必须实现 countByEnumeratingWithState:objects:count:。遗憾的是，这是个容易让人迷惑的方法。这里给出两个示例实现，展示在大多数情况下实现该方法所需的步骤。

## 几个 NSFastEnumeration 示例实现

如果你想让自定义类用上 Objective-C 2.0 的 “for...in” 快速枚举语言特性，就需要实现 NSFastEnumeration。

它唯一的方法（countByEnumeratingWithState:objects:count:）的文档相当晦涩、令人生畏——这主要是因为该方法必须保持灵活，而 Apple 又不想告诉你该怎么写代码。我没有这种顾虑，而且目前网上也没有多少示例，所以我想给你展示几种在自己的程序中实现它的简单方法。

枚举有两种不同的方式。第一种是你的类已经拥有（或愿意创建）一个由指向被枚举对象的 Objective-C id 值组成的 C 数组；第二种是你没有这种存储，想使用传递给你的存储。

> **警告：** 这些示例没有使用 mutationsPtr，因此只适用于 _不可变_（immutable）集合。如果被枚举的集合是 _可变_（mutable）的，你就需要把 mutationsPtr 指向一个合适的变更防护值（mutation guard value）（通常是变更计数值）。

## 第一种情况：已经拥有用于存储的 C 数组

我们的类如下所示：

```objc
@interface SimpleStringArray : NSObject &lt;NSFastEnumeration&gt;
{
    NSString *stringArray[ARRAY_LENGTH];
}
```

在这种情况下，countByEnumeratingWithState:objects:count: 的实现会是这个样子：

```objc
- (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState *)state objects:(id *)stackbuf count:(NSUInteger)len
{
    if (state->state >= ARRAY_LENGTH)
    {
        return 0;
    }

    state->itemsPtr = stringArray;
    state->state = ARRAY_LENGTH;
    state->mutationsPtr = (unsigned long *)self;
    
    return ARRAY_LENGTH;
}
```

快速说明：

- 我们忽略了 stackbuf 和 count（因为我们已经有存储）。
- 按要求，我们把 state-\>state 设置成了一个非零值（当前这批对象迭代完成后的迭代索引）。
- 按要求，我们把 state-\>mutationsPtr 设置成了一个非零值（即 self 指针，因为我们没有可以指向的“数组已变更”标志）。
- 我们返回了数组的完整长度，因此所有对象会在一遍之内迭代完（第二遍时，state-\>state 将等于 ARRAY_LENGTH，我们会返回 “0”，从而结束循环）。

## 第二种情况：需要存储

如果我们类的数据是存储在一个由线性相连（linearly connected）的 C 结构体组成的列表中的一组 NSString 对象，那么我们可能就没有 C 数组值可以返回。

假定我们的列表声明如下：

```objc
typedef struct
{
    NSString * stringPtr;
    struct MyList * nextNode;
} MyList;
```

而我们的类声明如下：

```objc
@interface StringList : NSObject &lt;NSFastEnumeration&gt;
{
    MyList * _startOfListNode;
    MyList * _endOfListPlusOneNode;
}
```

这个例子更复杂一些，因为我们需要真正地从列表中收集数据，并在各次迭代之间保存遍历状态。它可能看起来像这样：

```objc
- (NSUInteger)countByEnumeratingWithState:(NSFastEnumerationState *)state objects:(id *)stackbuf count:(NSUInteger)len
{
    MyList *currentNode;
    if (state->state == 0)
    {
        // 设置起点。假定 _startOfListNode 是本对象指向列表起点的
        // 那个实例变量。
        currentNode = _startOfListNode;
    }
    else
    {
        // 后续迭代时，从 state->state 中取出当前进度
        currentNode = (struct MyList *)state->state;
    }
    
    // 从列表中累积节点，直到到达本对象的
    // _endOfListPlusOneNode
    NSUInteger batchCount = 0;
    while (currentNode != _endOfListPlusOneNode && batchCount < len)
    {
        stackbuf[batchCount] = currentNode->stringPtr;
        currentNode = currentNode->nextNode;
        batchCount++;
    }

    state->state = (unsigned long)currentNode;
    state->itemsPtr = stackbuf;
    state->mutationsPtr = (unsigned long *)self;

    return batchCount;
}
```

对这个例子的说明：

- 现在我们用 stackbuf 来存放从列表中累积的数据，并通过 state-\>itemsPtr 返回它。
- 现在用到了 len，因为它是我们每次能在 stackbuf 中累积的对象数上限。
- 第一次执行时（当 state-\>state == 0 时），我们把 currentNode 设为对象私有的 _startOfListNode——我们假定已经把它正确设置为列表的起点。
- 之后的每次执行，state-\>state 都会保存着上一次迭代留存下来的 currentNode。
- 快速枚举会反复调用这个方法，直到我们到达列表末尾的 currentNode == _endOfListPlusOneNode——记住，state-\>state 不允许是 nil，这正是我们使用这个非 nil 结束标记节点的原因。如果你使用的列表以 nil 结尾，那么你应当检测到这种情况，并把 state-\>state 设置成一个特殊的非 nil“结束”标志，以免陷入无限循环。
