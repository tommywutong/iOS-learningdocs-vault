---
title: 'Friday Q&A 2012-03-02: 正确实现键值观察：第二轮'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-03-02-key-value-observing-done-right-take-2.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6928ebc07b61e6b8'
translated: true
---

> 原文：[Friday Q&A 2012-03-02: Key-Value Observing Done Right: Take 2](https://www.mikeash.com/pyblog/friday-qa-2012-03-02-key-value-observing-done-right-take-2.html)　·　mikeash.com Friday Q&A

发布于 2012-03-02 14:09 | [RSS 供稿](https://www.mikeash.com/pyblog/rss.py) ([全文供稿](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2012-03-09: 让我们构建 NSMutableArray](https://www.mikeash.com/pyblog/friday-qa-2012-03-09-lets-build-nsmutablearray.html)  
上一篇文章：[Friday Q&A 2012-02-17: 环形缓冲区与镜像内存：第二部分](https://www.mikeash.com/pyblog/friday-qa-2012-02-17-ring-buffers-and-mirrored-memory-part-ii.html)  
标签：[cocoa](https://www.mikeash.com/pyblog/?tag=cocoa) [后续](https://www.mikeash.com/pyblog/?tag=followup) [客座](https://www.mikeash.com/pyblog/?tag=guest) [kvo](https://www.mikeash.com/pyblog/?tag=kvo) [半邪恶](https://www.mikeash.com/pyblog/?tag=semi-evil)

Friday Q&A 2012-03-02: 正确实现键值观察：第二轮

作者：[Gwynne Raskind](http://blog.darkrainfall.org/)

---

**对 Apple 所做努力的思考**  
键值观察（Key-Value Observing，KVO）自 Panther（10.3）起就已存在，此后经历了三次公开可见的更新：

1. 在 Tiger 中，添加了针对无序集合（set）的变更类型（mutation types）。
2. 在 Leopard 中，添加了“初始（initial）”和“先前（prior）”观察，以及大幅改进的注册依赖键（dependent keys）的方法。
3. 在 Lion（及 iOS 5）中，添加了基于传入的 context 来移除已注册观察的方法。

在 Mike Ash 于 2008 年（大约 Leopard 时期）的文章中，他描述了三个主要问题。其中，只有一个问题此后得到了解决（即观察移除缺少 context 参数）。其余两个问题——缺少自定义选择器（selector）以及 context 指针（context pointer）无用——仍未解决，并且还出现了更多问题：

- 有了 Snow Leopard，我们获得了 block，但 KVO 完全忽略了它们。
- KVO 无法处理观察从未被反注册的对象，这个问题甚至从未被提出过。
- `NSNotificationCenter` 获得了 block 以及有目标的观察移除（从 add 调用中返回一个对象，该对象随后可用于移除同一个观察）。KVO 也错过了后者。
- KVO 从未有过“移除这个对象上的所有观察者”或“移除这个对象注册的所有观察”的语义，使得派生子类（subclass）和扩展（extension）更加痛苦。
- KVO 没有一次性注册多个键路径（key path）进行观察的语法。也没有一次性观察多个对象的语法。
- Mike 的解决方案（`MAKVONotificationCenter`）对观察者（observer）和被观察对象都施加了额外的保留（retain），导致容易产生保留循环（retain cycle），并且无法在 `dealloc` 方法中移除观察。

所有这些都是 Apple 应该处理的事情，而针对这些局限性提交的错误报告在两个主要操作系统版本中只带来了一项变化。

我个人认为，KVO 之所以受到如此少的关注，是因为它最初只是作为 Cocoa 绑定（bindings）背后的一个拼图而实现的。在许多人（包括我自己）看来，Cocoa 绑定在使 UI 轻松连接到代码这一预期目标上，是一场惨痛的失败。它仍然适用于 Apple 用它来做的事情，这对他么来说已经够好了。

但对我来说，这还不够好。

**设计更好的 KVO**  
很长一段时间里，我使用了 `MAKVONotificationCenter`，并加上了一些由灵感迸发的 Jerry Krinock 和我自己所做的额外调整（请参见 [Mike 的原始文章](https://www.mikeash.com/pyblog/key-value-observing-done-right.html#comment-c725ea36f22415152e31afb4c45e3d46) 的评论），这些调整增加了基本的 block 支持，以及更不具体和更具体的观察者反注册。但那个实现有点不优雅，并且仍然受制于保留循环问题。我最终决定坐下来，拼凑出一些更正式的东西。

在我看来，“全新改进”的 KVO 需要具备以下特性：

- 它必须解决 Mike 列出的所有三个问题，因此至少必须在某种程度上基于他的原始实现。
- 它需要支持将 block 作为观察者回调（callback）。
- 它需要支持“自动反注册（automatic deregistration）”，即在一个对象被释放（deallocation）时，移除它注册的任何观察，或注册在它身上的任何观察。
- 它需要**大大**简化注册多个键路径以及多个对象上的键路径的过程。
- 它需要**不**保留观察者或被观察对象。

**实现全新改进的 KVO**  
第一步是为这个新版本的 KVO 构建接口。从 `MAKVONotificationCenter` 开始，我添加了：

- 一个关闭自动反注册行为的标志。由于这肯定会涉及一点点运行时技巧，我认为最好能够按需关闭它。
- 一个用于“观察（observation）”的协议（protocol）。这将是一个由观察注册方法返回的通用对象，可用于移除该特定注册。它可被查询以了解该注册是否仍然有效。
- 一个用于“键路径集（key path set）”的协议。任何对象都可以实现一个返回快速可枚举（fast-enumerable）对象的方法，从而被用作“键路径”。`NSString`、`NSSet`、`NSArray` 和 `NSOrderedSet` 免费获得了此支持。
- 一个表示单个 KVO 通知信息的对象，即 `MAKVONotification`。该对象将传递给观察 block，并提供对通常隐藏在 change 字典（change dictionary）中所有内容的便捷访问。
- 在 `NSObject` 上的分类（category），提供基于选择器和 block 的注册方法，以及配套的反注册方法。我还加入了“反向语义”方法，因为我不喜欢 KVO 做事的顺序。

  KVO 的原始方法是“`[target addObserver:observer …]`”。对我来说，告诉观察目标去添加一个观察者是反的。所以我添加了“`[observer observeTarget:target …]`”方法，这些方法承担了将参数以相反顺序发送给 `MAKVONoticationCenter` 方法这一艰巨而困难的任务。
- 在同一个分类中，用于基于观察者、目标、键路径、选择器的任意组合（包括无组合）来反注册观察的方法。

从 Mike 的实现开始，添加 block 支持是相当简单的：

```
    #if NS_BLOCKS_AVAILABLE
            if (_selector)
    #endif
                ((void (*)(id, SEL, NSString *, id, NSDictionary *, id))objc_msgSend)(_observer, _selector, keyPath, object, change, _userInfo);
    #if NS_BLOCKS_AVAILABLE
            else
            {
                MAKVONotification       *notification = nil;

                // 传递 object 而非 _target 作为通知对象，
                //  以便数组观察能按预期工作。
                notification = [[MAKVONotification alloc] initWithObserver:_observer object:object keyPath:keyPath change:change];
                ((void (^)(MAKVONotification *))_userInfo)(notification);
            }
    #endif
```

适当的“注册观察”例程只是将 `NULL` 选择器和 block 作为用户信息（user info）传递给辅助对象。`MAKVONotification` 的实现非常简单，只是传递适当的数据并添加一些访问器从字典中抓取数据。

处理“键路径集”的代码也非常简单：

```
    NSMutableSet                *keyPaths = [NSMutableSet set];

    for (NSString *path in [keyPath ma_keyPathsAsSetOfStrings])
        [keyPaths addObject:path];

    _MAKVONotificationHelper    *helper = [[_MAKVONotificationHelper alloc] initWithObserver:observer object:target keyPaths:keyPaths selector:selector userInfo:userInfo options:options];
```

键路径被复制到一个集合（set）中，以避免要求原始键路径对象（或其返回的对象）具有持久且不可变的生命周期。例如，我为 `NSArray` 和 `NSSet` 提供的默认实现会返回 `self` 作为“字符串集”，而它们很可能是不变的（immutable），这会在以后当辅助对象需要反注册其观察时带来麻烦。

通过检测数组目标来实现一次观察多个对象是可能的：

```
    for (NSString *keyPath in _keyPaths)
    {
        if ([target isKindOfClass:[NSArray class]])
        {
            [target addObserver:self toObjectsAtIndexes:[NSIndexSet indexSetWithIndexesInRange:NSMakeRange(0, [target count])]
                     forKeyPath:keyPath options:options context:&MAKVONotificationHelperMagicContext];
        }
        else
            [target addObserver:self forKeyPath:keyPath options:options context:&MAKVONotificationHelperMagicContext];
    }
```

我没有使用一个中央的辅助对象字典来追踪观察（这需要昂贵的字符串构建，并且对于 block 来说无论如何都不可靠），而是将每个辅助对象作为关联对象（associated object）同时添加到观察者和目标上：

```
    NSMutableSet                *observerHelpers = nil;

    if (_observer) {
        @synchronized (_observer)
        {
            if (!(observerHelpers = objc_getAssociatedObject(_observer, &MAKVONotificationCenter_HelpersKey)))
                objc_setAssociatedObject(_observer, &MAKVONotificationCenter_HelpersKey, observerHelpers = [NSMutableSet set], OBJC_ASSOCIATION_RETAIN_NONATOMIC);
        }
        @synchronized (observerHelpers) { [observerHelpers addObject:self]; }
    }
```

有些人可能会反对我在这里使用的赋值表达式浓缩语法，但它是有效的。`@synchronized` 块使操作成为线程安全的（thread-safe）。现在，根据目标、观察者、键路径和选择器的某种组合来移除特定观察变得相对简单：

```
    - (void)removeObserver:(id)observer object:(id)target keyPath:(id<MAKVOKeyPathSet>)keyPath selector:(SEL)selector
    {
        NSParameterAssert(observer || target);  // at least one of observer or target must be non-nil

        @autoreleasepool
        {
            NSMutableSet                *observerHelpers = objc_getAssociatedObject(observer, &MAKVONotificationCenter_HelpersKey) ?: [NSMutableSet set],
                                        *targetHelpers = objc_getAssociatedObject(target, &MAKVONotificationCenter_HelpersKey) ?: [NSMutableSet set],
                                        *allHelpers = [NSMutableSet set],
                                        *keyPaths = [NSMutableSet set];

            for (NSString *path in [keyPath ma_keyPathsAsSetOfStrings])
                [keyPaths addObject:path];
            @synchronized (observerHelpers) { [allHelpers unionSet:observerHelpers]; }
            @synchronized (targetHelpers) { [allHelpers unionSet:targetHelpers]; }

            for (_MAKVONotificationHelper *helper in allHelpers)
            {
                if ((!observer || helper->_observer == observer) &&
                    (!target || helper->_target == target) &&
                    (!keyPath || [helper->_keyPaths isEqualToSet:keyPaths]) &&
                    (!selector || helper->_selector == selector))
                {
                    [helper deregister];
                }
            }
        }
    }
```

首先，获取目标和观察者上的辅助对象列表。我充分利用了向 `nil` 发送消息是安全的且总是返回 `nil` 这一事实，以避免额外的检查，代价是有一两个小小的内存分配。然后将键路径列表构建成一个集合，并以线程安全的方式将目标和观察者的辅助对象列表合并成一个单独的集合。由于集合是不重复的集合，这个合并后的列表中不会有重复的辅助对象。

现在，循环遍历该列表中的所有辅助对象，检查每个辅助对象是否符合指定的条件——它是否具有正确的观察者、正确的目标、正确的键路径集以及正确的选择器？（注意：代码检查的是键路径集的精确相等性，而不是检查被检查的辅助对象是否观察了传递路径中的“任一”而非“全部”路径。我觉得不值得花费额外精力去添加额外的检查。）如果是，则反注册该辅助对象，它将自行处理其线程安全性。

**在对象释放时自动移除 KVO 通知**  
这个改进版 KVO 最复杂的新特性是，不再需要寻找调用 `[self removeAllObservations]` 的地方，即使这个位置是 `-dealloc`。这在精神上与 ARC 无需调用 `[super dealloc]` 相似；我几乎从不需要在观察者或目标被释放之前移除观察，而跟踪何时这样做可能变得相当艰巨。

在 `dealloc` 时始终反注册观察的最明显方法是从 `-dealloc` 方法中执行此操作。这意味着要么动态派生子类（dynamic subclassing），要么方法混写（swizzling）。由于 KVO 已经做了动态派生子类，那是我不准备深入探究的一层复杂性。我选择了方法混写。

我的 `MAKVONotificationCenter` 在观察者和目标对象上都调用了 `-_swizzleObjectClassIfNeeded:`。它看起来像这样：

```
    - (void)_swizzleObjectClassIfNeeded:(id)object
    {
        if (!object)
            return;
        @synchronized (MAKVONotificationCenter_swizzledClasses)
        {
            Class           class = [object class];//object_getClass(object);

            if ([MAKVONotificationCenter_swizzledClasses containsObject:class])
                return;

            SEL             deallocSel = NSSelectorFromString(@"dealloc");/*@selector(dealloc)*/
            Method          dealloc = class_getInstanceMethod(class, deallocSel);
            IMP             origImpl = method_getImplementation(dealloc),
                            newImpl = imp_implementationWithBlock(/* ... snip ... */        
            class_replaceMethod(class, deallocSel, newImpl, method_getTypeEncoding(dealloc));

            [MAKVONotificationCenter_swizzledClasses addObject:class];
        }
    }
```

首先要做的是检查这个特定的类之前是否已被混写。我们想要的是对象自认为的类，而不是它实际的类——使用 KVO 时，这两者是不同的，并且混写 KVO 的动态子类被证明会导致非常奇怪的行为。如果它已经被混写了，就什么也不做。我不会检查给定类的超类（superclass）或子类是否已经被混写过，因为在层级结构中执行多次是无害的，最坏情况下也只会导致一些额外的无用工作。

接下来，获取 `-dealloc` 的 `SEL`；在 ARC 模式下无法使用 `@selector(dealloc)`，所以我不得不使用 `NSSelectorFromString()` 来欺骗编译器。我获取了 `dealloc` 的实例方法及其原始实现。然后，我使用 Lion 出色的 `imp_implementationWithBlock()` API 从一个 block 创建了一个新的实现——我将在下面描述这个实现本身。最后，我用新的实现替换了类上原始的 `dealloc`，并将该类添加到已混写类的列表中。

以下是新的 `dealloc` 实现本身：

```
    (__bridge void *)^ (void *obj)
    {
        @autoreleasepool
        {
            for (_MAKVONotificationHelper *observation in [objc_getAssociatedObject((__bridge id)obj, &MAKVONotificationCenter_HelpersKey) copy])
            {
                // 这里需要检查选项，因为某个特定观察
                //  可能希望手动反注册，而同一类
                // （甚至同一对象）上的其他观察
                //  可能不希望。
                if (!(observation->_options & MAKeyValueObservingOptionUnregisterManually))
                    [observation deregister];
            }
        }
        ((void (*)(void *, SEL))origImpl)(obj, deallocSel);
    };
```

这里有很多值得注意的地方。首先，请注意我将 block 本身转换为 `(__bridge void *)`——这是为了让 ARC 对将 block（它是一个对象）转换为其指针形式保持安静，这是 C API 所要求的。

接下来，block 将其参数作为 `void` 指针，而不是 `id`。这似乎是反直觉的；毕竟，传递给实现 block 的对象是 `self`！再次，ARC 给出了答案。在 ARC 下，函数（block 也是函数）的所有参数在进入函数时都会自动发送 `retain` 消息。但由于这是 `dealloc` 方法的实现，结果将是尝试复活对象，这会破坏内存。随之而来的是各种混乱。将对象强制为普通指针可以将其对 ARC 隐藏。这比将其标记为 `__unsafe_unretained` 更好，因为语义更清晰。

方法的整个主体被包裹在一个自动释放池（autorelease pool）中，因为这里可能会发生相当多的工作，并且不希望所有这些工作一直悬而未决直到下一个事件循环。

接下来，循环遍历为此对象注册的辅助对象集合。请记住，这个集合将包括以该对象为观察者的辅助对象，以及以该对象为目标的辅助对象，因为一个辅助对象总是同时添加到它的观察者和目标上。我们检查手动反注册选项，如果未设置，则反注册该辅助对象。这里不需要线程安全性；正在被释放的对象不能从多个线程使用，否则无论我们做什么，程序都注定要崩溃。

最后，我们调用原始的 `dealloc` 实现，该实现已被 block 从其周围上下文中捕获。这就是使用 block 实现的美妙之处；完全不需要将原始的 `dealloc` 保存在任何地方；block 会为我们处理。这也是为什么混写子类是安全的原因。如果某个类不知何故被混写了两次（例如，一个具有 `dealloc` 的类，以及它的一个没有 `dealloc` 的子类），那么只会发生两个混写的 block 被调用，接着是正确原始的 `dealloc`。

**辅助对象使用 `__unsafe_unretained` 引用！为什么不用 `__weak` 引用？你想在这里搞什么名堂！？**  
如果你在读这篇文章时一直在看代码，你可能已经注意到执行大部分魔法的 `_MAKVONotificationHelper` 对象对其观察者和目标持有 `__unsafe_unretained` 引用。使用 ARC 如此乐于提供的更安全的清零弱引用（zeroing weak references，ZWR）不是更有意义吗？

嗯，不。原因如下：

- `__weak` 在 OS X 10.6 / iOS 4.x 上不可用。虽然已经使用了其他 API（特别是 `imp_implementationWithBlock()`）破坏了向后兼容性，但如果你愿意，它们并不难绕开，并且还有不使用 ZWR 的其他原因。
- 在 OS X 上，你不能对包括 `NSWindow` 在内的整个类列表使用 ZWR。这意味着你不能将此类对象用作观察者或使其成为观察的目标。
- 在存在混写的 `-dealloc` 方法的情况下，`__unsafe_unretained` **并不危险**！观察者或目标总是会在辅助对象消失之前移除它，此时它也从另一个对象上消失了。如果调用者恰好传递了“我要手动反注册”标志，那么原始的 KVO 语义就回归了：释放一个拥有已注册观察者的对象已经是非法/导致崩溃的错误。将这些改为适当的 `__weak` 引用只会暂时掩盖问题，而不是解决问题。

**到底谁需要一个观察者？**  
在所有这些变更的开发过程中，Mike Ash 和 Tony Xiao 一直在密切关注。特别是 Tony 想出了一个在 `NSObject` 分类中特别巧妙的方法：

```
    - (id<MAKVOObservation>)addObservationKeyPath:(id<MAKVOKeyPathSet>)keyPath options:(NSKeyValueObservingOptions)options block:(void (^)(MAKVONotification *notification))block;
```

这个方法质疑了 KVO 工作需要有一个“观察者”对象这一基本假设！使用基于 block 的回调，唯一重要的对象是被观察的对象。观察者是谁根本不重要，而 KVO 自身的内部需求由辅助对象作为观察者来满足。虽然在实践中观察者仍然很重要，因为 block 几乎肯定会引用它，但从概念上讲，没有明确的理由让它存在。

Tony 还负责了导致将 `__weak` 观察者和目标引用替换为 `__unsafe_unretained` 引用的讨论。他帮了大忙，我在此向他大声说：“谢谢，Tony！”

**结论**  
文件中其余的代码基本上是样板文件，相当直接，所以这就结束我的讨论了，除了要提一下，我编写的单元测试对于确保代码正常工作具有不可估量的价值。单元测试是个好东西，各位！

这周就到这里，三周后我会回来，在 Mike 关于从头重建 Cocoa 集合类（collection classes）的两部分文章之后。一如既往，感谢阅读！

你喜欢这篇文章吗？我正在出售装满它们的整本书！第二卷和第三卷现已出版！它们以 ePub、PDF、印刷版以及 iBooks 和 Kindle 格式提供。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 供稿](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-03-02-key-value-observing-done-right-take-2.html)

添加你的想法，发表评论：

垃圾邮件和离题的文章将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
