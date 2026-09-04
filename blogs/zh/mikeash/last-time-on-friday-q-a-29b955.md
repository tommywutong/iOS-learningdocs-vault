---
title: 'Friday Q&A 2012-03-09：让我们构建 NSMutableArray'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-03-09-lets-build-nsmutablearray.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:ca6d931b5607ab36'
translated: true
---

> 原文：[Last time on Friday Q&A](https://www.mikeash.com/pyblog/friday-qa-2012-03-09-lets-build-nsmutablearray.html)　·　mikeash.com Friday Q&A

发表于 2012-03-09 13:44 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2012-03-16：让我们构建 NSMutableDictionary](https://www.mikeash.com/pyblog/friday-qa-2012-03-16-lets-build-nsmutabledictionary.html)  
上一篇：[Friday Q&A 2012-03-02：正确实现键值观察：第二轮](https://www.mikeash.com/pyblog/friday-qa-2012-03-02-key-value-observing-done-right-take-2.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-03-09：让我们构建 NSMutableArray

作者：[Mike Ash](https://www.mikeash.com/)

**概念**  
`NSMutableArray` 是一个类簇（class cluster），所以重新实现它相当容易。只要派生它的子类，然后实现那些原语方法（primitive method），你就得到了一个功能完备的 `NSMutableArray`，支持任何 `NSMutableArray` 的全部功能。下面就是这些原语方法：

```
    - (NSUInteger)count;
    - (id)objectAtIndex:(NSUInteger)index;
    - (void)addObject:(id)anObject;
    - (void)insertObject:(id)anObject atIndex:(NSUInteger)index;
    - (void)removeLastObject;
    - (void)removeObjectAtIndex:(NSUInteger)index;
    - (void)replaceObjectAtIndex:(NSUInteger)index withObject:(id)anObject;
```

这些原语方法提供的功能足以支撑其余所有 `NSMutableArray` 方法在其上构建，这一点应当相当清楚。实际上，这组原语方法已经略显多余。例如，`addObject:` 可以基于 `insertObject:atIndex:` 实现，`removeLastObject` 可以基于 `removeObjectAtIndex:` 实现。我也说不清这些额外的原语方法究竟为什么存在，但无论如何，把这一整套实现出来，我们就得到了一个功能完备的 `NSMutableArray` 子类。

那么问题是，我们该_如何_实现这些方法？思路是用一个 C 数组作为后备存储（backing storage）。从根本上说，C 数组只支持取值和设值，而 `NSMutableArray` 还允许增删值，增删会自动挪动其后的值。我们的应对办法是按需拷贝数组条目。`NSMutableArray` 还允许数组动态扩容，我们的应对是在必要时分配新的 C 数组，把旧内容拷进去。

**代码**  
老规矩，今天这些冒险的代码放在 GitHub 上，想一口气看全的可以去：

[https://github.com/mikeash/MACollections](https://github.com/mikeash/MACollections)

**实现**  
这个类的接口极其简单：

```
    @interface MAMutableArray : NSMutableArray
    @end
```

这个子类没有给接口新增任何东西，所以它就是一个直接的 `NSMutableArray` 子类。

下面是这个类会用到的实例变量：

```
    @implementation MAMutableArray {
        NSUInteger _count;
        NSUInteger _capacity;
        id *_objs;
    }
```

C 数组是 `_objs`，`_capacity` 存的是为数组分配的元素数量，实际用到的元素数量存在 `_count` 里。容量与计数分开存，这样每次增删对象都不必重新分配数组——那样做的效率会低到离谱。

接下来是初始化方法。`NSMutableArray` 要求实现 `initWithCapacity:`，这个类才能与 `+array` 这类内建便利方法配合工作。据我所知，这一点没有任何文档记载。对这个类来说，所有实例变量保持为零就行，所以这个初始化方法除了调用 `super` 什么都不用做：

```
    - (id)initWithCapacity: (NSUInteger)capacity
    {
        return [super init];
    }
```

注意 `capacity` 参数纯属建议性质，像这样无视它是安全的。

接下来是 `dealloc` 的实现。数组销毁时，需要释放它包含的所有对象。虽然有更快的实现方式，我在这里选择简单地移除全部对象。除此之外，C 数组本身需要释放，就完事了：

```
    - (void)dealloc
    {
        [self removeAllObjects];
        free(_objs);
        [super dealloc];
    }
```

现在可以进入各个原语方法的实现了。第一个是 `count`，非常简单，直接返回 `_count` 实例变量即可：

```
    - (NSUInteger)count
    {
        return _count;
    }
```

下一个是 `objectAtIndex:`，几乎同样简单。它只是从 C 数组里取出元素并返回：

```
    - (id)objectAtIndex: (NSUInteger)index
    {
        return _objs[index];
    }
```

为简短起见，这段代码省去了错误检查。这个方法的严谨实现应当先用 `_count` 检查 `index`，越界就抛异常。而照现在这个写法，`index` 的坏值会让方法返回垃圾数据或直接崩溃。

**插入**  
前面说过，`addObject:` 方法可以基于 `insertObject:atIndex:` 实现，我就这么做：

```
    - (void)addObject:(id)anObject
    {
        [self insertObject: anObject atIndex: [self count]];
    }
```

到了 `insertObject:atIndex:`，我们终于迎来一点有意思的代码。该方法要做的第一件事，是在现有后备 C 数组已满时为其扩容，给新对象腾出空间：

```
    - (void)insertObject: (id)anObject atIndex: (NSUInteger)index
    {
        if(_count >= _capacity)
        {
```

代码必须算出一个新的分配容量。我使用最少 `16` 个元素——用于第一次分配——之后每次重新分配都把容量乘以 `2`。每次重分配都把容量乘以一个固定倍数，会带来一些有益的性能后果，稍后会谈到。下面就是计算新容量、并按新容量分配新数组的代码：

```
            NSUInteger newCapacity = MAX(_capacity * 2, 16);
            id *newObjs = malloc(newCapacity * sizeof(*newObjs));
```

接下来要把旧数组的内容拷贝过去。这就是一次简单的 `memcpy`：

```
            memcpy(newObjs, _objs, _count * sizeof(*_objs));
```

最后，释放旧存储，把实例变量重新指向新存储：

```
            free(_objs);
            _objs = newObjs;
            _capacity = newCapacity;
        }
```

到这里，可以保证数组有足够的空间容纳新对象。如果数组之前是满的，现在已扩容；如果原本没满，那必然还有空间。条件满足后，下一个要求是挪动对象，把 `index` 处的槽位腾出来给新对象。数组中 `index` 之后的所有对象都要后移一位。这通过调用 `memmove` 完成：

```
        memmove(_objs + index + 1, _objs + index, ([self count] - index) * sizeof(*_objs));
```

给不熟悉的朋友解释一下：`memmove` 是 `memcpy` 的一个可能更慢的变体，它允许参数所指的内存区间重叠。`memcpy` 则被允许假定其参数互不重叠，若不成立行为可能出错。这段代码的参数几乎总是重叠的，而 `memmove` 允许这种情况。

简单拆解一下这些参数。`_objs + index` 是这次 `memmove` 的源地址，即需要挪动的那些对象的起点。需要后移的对象数量是 `[self count] - index`，乘以 `sizeof(*_objs)` 就得到这些指针以字节计的总大小。最后，它们要后移一个槽位，所以目标指针是 `_objs + index + 1`。

给新对象腾出空间后，剩下的就是把它放进 C 数组，并把 `_count` 加一：

```
        _objs[index] = [anObject retain];

        _count++;
    }
```

**移除与替换**  
`removeLastObject` 原语方法的实现，就是调用 `removeObjectAtIndex:` 并传入数组的最后一个索引：

```
    - (void)removeLastObject
    {
        [self removeObjectAtIndex: [self count] - 1];
    }
```

`removeObjectAtIndex:` 的实现也相对简单。第一件事是释放被移除的对象：

```
    - (void)removeObjectAtIndex: (NSUInteger)index
    {
        [_objs[index] release];
```

接着用 `memmove` 把所有对象前移。这本质上与 `insertObject:atIndex:` 里的挪动相同，只是方向相反：

```
        memmove(_objs + index, _objs + index + 1, ([self count] - index - 1) * sizeof(*_objs));
```

剩下的就是把对象计数减一：

```
        _count--;
    }
```

在真正的实现里，这个方法同样应该做些错误检查以确保 `index` 有效，但本例中我们照旧略过。

真正的实现还可能在计数（`_count`）跌破某个阈值时收缩 C 数组。如果你往数组里加了一百万个对象再全部移除，你不会希望数组还占着容纳一百万个对象的内存。不过这并非严格必需，而只是一种内存用量优化，我就省略了。代码会长得很像 `insertObject:atIndex:` 里重新分配的那段。

`replaceObjectAtIndex:withObject:` 的实现同样非常简单。它所做的只是保留新对象、释放旧对象，然后把新对象放进数组中的那个索引处：

```
    - (void)replaceObjectAtIndex: (NSUInteger)index withObject: (id)anObject
    {
        [anObject retain];
        [_objs[index] release];
        _objs[index] = anObject;
    }
```

到此为止！我们现在有了一个从零构建、功能完备的 `NSMutableArray`。

**重新分配的代价**  
重新分配数组时，代码每次都把容量翻倍。与「每次只把容量增加固定数量」这类做法相比，这可能不那么直观。我们来审视一下这两种做法的性能后果，看看为什么按固定倍数放大容量通常更好。

先看单次数组重分配的代价。可以假定分配本身（连同释放旧数组）耗时与数组大小关系不大。唯一的可变代价是把对象从旧数组拷到新数组。既然拷贝不做任何特别的事，只是把字节逐个搬动，我们可以假定：若数组中有 \\(\\mathrm{n}\\) 个对象，拷贝耗时大致与 \\(\\mathrm{n}\\) 成正比；用算法复杂度的话说，这个操作是 \\(\\mathrm{O(n)}\\)。知道了每次分配的代价与数组当前大小呈 \\(\\mathrm{O(n)}\\) 关系，我们就能推导出不同重分配策略的复杂度。

考虑每次把数组增加固定数量的情形。为便于分析，假设每次容量增加 \\(\\mathrm{1}\\)。这是个病态情形，但容易分析，结论也能推广到更合理的情形。据此，看看往数组里添加 \\(\\mathrm{1000}\\) 个元素的总代价。

每加一个新元素都要重分配一次，产生与数组当前元素数量成正比的代价。第一个元素耗时约 \\(\\mathrm{1}\\)，第二个约 \\(\\mathrm{2}\\)，依此类推。总代价就是 \\(\\mathrm{1 + 2 + 3 + \\cdots + 999 + 1000}\\)，即 \\(\\mathrm{500500}\\)。

更一般地，添加 \\(\\mathrm{m}\\) 个元素的代价是 \\(\\mathrm{1 + 2 + 3 + \\cdots + m}\\)，也就是：$$\\frac{m * (m + 1)}{2}$$ 用算法复杂度表示，可简写作 \\(\\mathrm{O(m^2)}\\)。换言之，添加 `m` 个元素的总代价与 `m` 的平方成正比。元素翻倍，添加耗时约变为四倍。添加一百万个元素的耗时约是添加一个元素的一万亿次，这个数字可不怎么令人愉快。

来看一个更现实的情形，比如每次重分配把容量增加 \\(\\mathrm{1024}\\)。此时添加 \\(\\mathrm{m}\\) 个元素的代价是 \\(\\mathrm{1024 + 2048 + 3076 + 4096 + \\cdots + m}\\)。全部算下来，结果仍是 `O(m`^`2``)`，尽管比之前快得多。代价仍与元素数量的平方成正比，只是常量因子小得多。这是实现数组增长的一种现实得多做法，但渐进表现依旧糟糕。

最后看本文实现的这种每次重分配把容量翻倍的策略。此时 `m` 个元素的总代价约为 \\(\\mathrm{1 + 2 + 4 + 8 + 16 + \\cdots + m}\\)，也就是 \\(\\mathrm{2m - 1}\\)，即 \\(\\mathrm{O(m)}\\)。简言之，添加元素的代价与添加的元素总数成正比。元素加一倍，耗时也大约只多一倍。

有意思的是，这个结论对其他倍数同样成立。比如说每次把容量增加 10%。这稍微难算一点，因为容量只能是整数。但先把这个搁置一旁、假定我们能处理分数，那么添加 \\(\\mathrm{m}\\) 个元素的代价是 \\(\\mathrm{1 + 1.1 + 1.21 + \\cdots + m}\\)，算出来约为 \\(\\mathrm{11m}\\)，仍是 \\(\\mathrm{O(m)}\\)，只是常量因子更大。一般地，_任何_大于 \\(\\mathrm{\>1}\\) 的倍数，插入 \\(\\mathrm{m}\\) 个元素的净代价都是 \\(\\mathrm{O(m)}\\)。不过倍数越大，前面的常量乘数越小，分配执行得就越快。

于是我们得到一个有趣的权衡。倍数越大，数组表现越好，但浪费的空间也越多。翻倍分配时，如果数组持有 \\(\\mathrm{m}\\) 个元素，可能有高达 \\(\\mathrm{m - 2}\\) 个额外元素的已分配空间未被使用。数组若继续增长，这些空间终会被用上；但如果增长就此打住，那片空间就永远浪费了。按 10% 增幅分配时，浪费的空间至多约 \\(\\mathrm{\\frac{m}{10}}\\)，但花在拷贝和重分配上的时间会显著变多。

**结语**  
`NSMutableArray` 的真实实现[比这里展示的要复杂得多](http://ridiculousfish.com/blog/posts/array.html)，但基本原理不变。看过这个简单的实现之后，希望整个概念对你更清晰了。

下次我会更进一步，展示一个基于哈希表的 `NSMutableDictionary` 实现。在那之前，未来文章的点子随时欢迎，[发给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-03-09-lets-build-nsmutablearray.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
