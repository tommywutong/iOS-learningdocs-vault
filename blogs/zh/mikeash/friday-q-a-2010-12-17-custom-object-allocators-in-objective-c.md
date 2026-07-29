---
title: 'Friday Q&A 2010-12-17：Objective-C 中的自定义对象分配器'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-12-17-custom-object-allocators-in-objective-c.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b8f6776f5a7a28f4'
translated: true
---

> 原文：[Friday Q&A 2010-12-17: Custom Object Allocators in Objective-C](https://www.mikeash.com/pyblog/friday-qa-2010-12-17-custom-object-allocators-in-objective-c.html)　·　mikeash.com Friday Q&A

发布于 2010-12-17 18:27 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2010-12-31：C 宏技巧与陷阱](https://www.mikeash.com/pyblog/friday-qa-2010-12-31-c-macro-tips-and-tricks.html)  
上一篇：[Friday Q&A 2010-12-03：访问器、内存管理与线程安全](https://www.mikeash.com/pyblog/friday-qa-2010-12-03-accessors-memory-management-and-thread-safety.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [memory](https://www.mikeash.com/pyblog/?tag=memory) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2010-12-17：Objective-C 中的自定义对象分配器

作者：[Mike Ash](https://www.mikeash.com/)

**它意味着什么**  
 任何使用 Objective-C 的人都知道，通过编写 `[MyClass alloc]` 来分配一个类的实例。创建自定义分配器，只需替换标准分配器，让 `[MyClass alloc]` 转而调用你自己的代码。

一个 Objective-C 对象[只是一块大小正确的内存，其第一个指针大小的块指向对象的类](https://www.mikeash.com/pyblog/friday-qa-2009-03-13-intro-to-the-objective-c-runtime.html)。因此，自定义分配器需要返回一个指向大小合适的内存块的指针，并正确填充 class 信息。

**它为什么有用**  
 编写自定义分配器的最大原因是为了性能。标准分配器所做的权衡可能不适合你的特定情况。它还必须能在所有类和各种情况下工作，而你的自定义分配器只需要与你编写的类及其使用场景配合。

另一个原因是开销。由于各种原因，标准分配器需要为每次分配预留一定的额外存储空间。这对于大量分配的极小对象来说尤其昂贵。自定义分配器可以通过针对所编写类的需求进行定制，大幅减少这种开销。

**关于垃圾收集的说明**  
 本文假设手动 `retain`/`release` 内存管理。自定义分配器在垃圾收集下基本无法使用，因为无法添加自定义的 `free` 回调。可以使用其中一些技术（如对象缓存），但大多数情况下，自定义分配器仅适用于手动内存管理的场景。

**一个基本的自定义分配器**  
 `+alloc` 方法实际上只是调用 `+allocWithZone:`。尽管内存区（memory zone）现在基本上只是历史遗留产物，但它仍然保留在 API 中。因此，要重写的方法是 `+allocWithZone:`：

```
    + (id)allocWithZone: (NSZone *)zone
    {
```

作为一个简单的分配器示例，我只需调用 `calloc`。与标准分配器相比，这几乎没有优势，但它展示了如何实现。（我使用 `calloc` 而不是 `malloc`，因为 Objective-C 代码假定实例变量是被清零的。）

为了调用 `calloc`，你需要知道要分配多少内存。幸运的是，Objective-C runtime 让这变得简单。`class_getInstanceSize` 函数会告诉你确切的大小：

```
        id obj = calloc(class_getInstanceSize(self), 1);
```

接下来，你需要设置这个新分配对象的 isa。isa 位于对象的开头，通过一点巧妙的类型转换（casting），你可以轻松地设置它：

```
        *(Class *)obj = self;
```

现在你可以返回新创建的对象：

```
        return obj;
    }
```

我们还没有完成。我们还需要重写 `-dealloc` 来调用 `free`：

```
    - (void)dealloc
    {
        free(self);
```

通常这就够了。然而，对于没有调用 `super` 的 `-dealloc` 方法，编译器会发出警告。为了消除这个警告，我在 `return` 语句后插入了一个不会执行的虚拟调用：

```
        return;
        [super dealloc]; // shut up compiler
    }
```

你的自定义分配器就准备好了。

**陷阱**  
 和这个层次的大多数事情一样，有几点需要注意。

首先，不要这样做，除非你直接从 `NSObject` 派生子类（subclass）。`-dealloc` 方法既涉及销毁对象本身，也涉及释放它持有的资源。`-[NSObject dealloc]` 只是（大部分）销毁对象，因此不调用它是安全的。但是，对于任何其他类来说，这样做是不安全的。例如，如果你尝试对一个 `NSView` 的子类这样做，最终会泄漏大量内部状态。

其次，上面提到的“（大部分）”意味着 `NSObject` 所做的某些事情你需要考虑。其中一个是移除关联对象（associated objects）。如果你的对象可能有关联对象，或者你认为即使有可能，那么你需要确保它们被移除。这可以通过调用 `objc_removeAssociatedObjects(self)` 来实现。另一个是调用实例变量中 C++ 对象的析构函数。你最好的选择是避免使用 C++ 对象作为实例变量。如果你必须使用它们，请研究调用或模仿私有 runtime 函数 `objc_destructInstance` 的可能性，该函数同时处理 C++ 析构函数和关联对象。

第三，像 ObjectAlloc 和 zombies 这样的内存调试工具无法在使用自定义分配器的对象上工作。因此，我建议你定义一个用于内存调试的预处理器宏，使你的对象使用标准分配器而不是自定义分配器，这样你就可以在需要时切换并启用这些工具。

**缓存对象**  
 作为一个实际的例子，我将编写一个分配器，它将已销毁的对象放入缓存，以便它们可以被快速重用。这对于那些分配和销毁如此频繁以至于标准分配器太慢的类非常有用。

为了达到最大速度，我将对这个类的工作和使用方式做一些假设：

- 它永远不会被派生子类（subclass），或者即使有子类，子类也从不添加实例变量。（这允许将所有实例放入同一个缓存。）
- 它的初始化方法可以处理一个“脏”对象；即实例变量不需要被清零。（这节省了从缓存中取出每个实例时清零的时间。）
- 它只从同一个线程进行分配和销毁。（这使得不需要创建线程安全的缓存。）

我现在先忽略缓存的具体工作方式，只假设它提供了一个简单的包含两个函数的接口：`AddObjectToCache` 和 `GetObjectFromCache`。然后 `+allocWithZone:` 的重写看起来像这样：

```
    + (id)allocWithZone: (NSZone *)zone
    {
        id obj = GetObjectFromCache();
        if(obj)
            *(Class *)obj = self;
        else
            obj = [super allocWithZone: zone];
        return obj;
    }
```

`-dealloc` 重写只是将对象返回给缓存：

```
    - (void)dealloc
    {
        // 在此处释放所有实例变量
        AddObjectToCache(self);
        
        // 让编译器闭嘴
        return;
        [super dealloc];
    }
```

缓存本身就是一个链表，利用每个对象的 `isa` 槽位来指向列表中的下一个条目。列表头是一个全局变量：

```
    static id gCacheListHead;
```

接下来，我需要一些辅助函数来访问每个列表项的 `next` 指针：

```
    static id GetNext(id cachedObj)
    {
        return *(id *)cachedObj;
    }
    
    static void SetNext(id cachedObj, id next)
    {
        *(id *)cachedObj = next;
    }
```

有了这些辅助函数，两个主要的缓存函数就很容易编写了：

```
    static id GetObjectFromCache(void)
    {
        id obj = gCacheListHead;
        if(obj)
            gCacheListHead = GetNext(obj);
        return obj;
    }
    
    static void AddObjectToCache(id obj)
    {
        SetNext(obj, gCacheListHead);
        gCacheListHead = obj;
    }
```

有了这个系统，对象最初是正常分配的，但当其被销毁时，会进入缓存。一旦缓存中有对象，新的对象就会从中取出，这比分配新内存要快得多。

**自定义块分配器**  
 缓存对象可以带来很大的速度提升，但初始分配并不会加速，而且你仍然有所有这些小分配的空间开销。通过分配一大块（block）内存并将其分割成小块，可以加速初始分配并大幅减少每个对象的开销。为此，我将使用上述相同的对象缓存方案，但对 `+allocWithZone:` 的实现稍作修改：

```
    + (id)allocWithZone: (NSZone *)zone
    {
        id obj = GetObjectFromCache();
        if(!obj)
        {
            AllocateNewBlockAndCache(self);
            obj = GetObjectFromCache();
        }
        *(Class *)obj = self;
        return obj;
    }
```

所有有趣的事情都将在 `AllocateNewBlockAndCache` 中发生。这个函数要做的第一件事是分配一大块内存。我选择 `4096` 作为块大小，因为它与 OS X 使用的页面大小匹配，并且是一个方便处理的大小：

```
    static void AllocateNewBlockAndCache(Class class)
    {
        static size_t kBlockSize = 4096;
        char *newBlock = malloc(kBlockSize);
```

一旦有了这块内存，它就需要将其分割成小块，并将每个小块添加到缓存中。为此，它将遍历这块内存，使用 `class_getInstanceSize` 来标记每个实例大小的区域，然后使用 `AddObjectToCache` 将每个区域放入缓存：

```
        int instanceSize = class_getInstanceSize(class);
        int instanceCount = kBlockSize / instanceSize;
        while(instanceCount-- > 0)
        {
            AddObjectToCache((id)newBlock);
            newBlock += instanceSize;
        }
    }
```

就是这样。对象缓存机制负责回收旧对象，以便它们可以被再次使用。

**结论**  
 在 Objective-C 中编写自定义对象分配器相对简单。困难的部分在于分配器本身，这在很大程度上取决于你。一旦你有了分配器，你可以通过以下步骤将其插入到你的 Objective-C 类中：

1. 重写 `+allocWithZone:` 以调用你的自定义分配器，将块的 `isa` 设置为 `self`，并可选地清零其余内存。
2. 重写 `-dealloc` 以调用你的自定义分配器，并且_不要_调用 `super`。
3. 如果可能包含关联对象，则在 `-dealloc` 中调用 `objc_removeAssociatedObjects`。
4. 只直接子类化（subclass）`NSObject`，不要子类化 `NSObject` 的任何其他子类。

除了完整的自定义分配器之外，像对象缓存这样的技术可以用更低的复杂度为你带来速度提升。

本期 Friday Q&A 就到这里。两周后回来观看下一期精彩内容。一如既往，欢迎并期待你提出希望涵盖的主题想法，如果你有想在这里看到的内容，请[发送过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在出售这些文章的完整合集！第二卷和第三卷现已出版！提供 ePub、PDF、印刷版、iBooks 和 Kindle 版本。[点击此处获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-12-17-custom-object-allocators-in-objective-c.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
