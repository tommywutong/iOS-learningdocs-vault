---
title: 'Friday Q&A 2012-05-18：PLWeakCompatibility 导览：第一部分'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-05-18-a-tour-of-plweakcompatibility-part-i.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3d1464909cd47821'
translated: true
---

> 原文：[Last time](https://www.mikeash.com/pyblog/friday-qa-2012-05-18-a-tour-of-plweakcompatibility-part-i.html)　·　mikeash.com Friday Q&A

发表于 2012-05-18 16:53 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2012-06-01：PLWeakCompatibility 导览：第二部分](https://www.mikeash.com/pyblog/friday-qa-2012-06-01-a-tour-of-plweakcompatibility-part-ii.html)  
上一篇：[解决模拟器引导错误](https://www.mikeash.com/pyblog/solving-simulator-bootstrap-errors.html)  
标签：[arc](https://www.mikeash.com/pyblog/?tag=arc) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [hack](https://www.mikeash.com/pyblog/?tag=hack) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-05-18：PLWeakCompatibility 导览：第一部分

作者：[Mike Ash](https://www.mikeash.com/)

**动机**  
ARC 确实是很好用的技术。它比不上真正的垃圾回收器那么好，但比手动内存管理好用得多。然而，用 ARC 却没有 `__weak` 关键字实在恼人。替代品是 `__unsafe_unretained`，它给你一个不保留的引用，但在目标对象被释放时_不会_置零。如果你在目标被销毁之后访问这样的变量，就会崩溃。相比之下，`__weak` 变量会在对象被释放时自动变成 `nil`，让访问悬空指针变得不可能（或者至少难得多）。

在 [Plausible Labs](http://plausible.coop/)，我们想把一个大项目迁到 ARC，但又需要保持对 iOS 4 的兼容。一个办法是使用 [`MAZeroingWeakRef`](https://github.com/mikeash/MAZeroingWeakRef) 这样的显式代理对象来管理零值弱引用（zeroing weak reference）。另一个办法是用 `__unsafe_unretained`，它与手动内存管理时代的老式不保留引用相比，其实安全不到哪去。

只要能避免，我们真不想要任何折衷方案。最终我们决定试试：能不能骗过编译器，让它接受旧系统上的 `__weak`，并提供必要的运行时代码让它真正工作。一番调查之后发现，这不仅可行，而且相当直接——`PLWeakCompatibility` 就此诞生。

**编译器侧**  
从编译器的角度看，`__weak` 其实相当简单。所有有意思的部分都委托给运行时，编译器只需在恰当时机发出正确的运行时调用。这些运行时函数列在 [clang ARC 文档](http://clang.llvm.org/docs/AutomaticReferenceCounting.html)里，它们是：

```
    void objc_copyWeak(id *dest, id *src);
```

这个函数把一个弱指针从一处拷到另一处，用于目标位置尚未持有弱指针的情形。对应的代码如：

```
    __weak id weakPtr1 = ...;
    __weak id weakPtr2 = weakPtr1;
```

下一个函数是：

```
    void objc_destroyWeak(id *object);
```

它注销一个 `__weak` 指针。用于局部 `__weak` 变量离开作用域之时，或带有 `__weak` 实例变量的类的 `dealloc` 实现之中。

```
    id objc_initWeak(id *object, id value);
```

这个函数初始化一个 `__weak` 变量。用于这样的代码：

```
    id strongPtr = ...;
    __weak id weakPtr = strongPtr;
```

再往下：

```
    id objc_loadWeak(id *object);
```

它从弱指针里取出值并返回，取值前会先保留并放入自动释放池，确保值活得够久、调用方来得及使用。凡是在表达式里用到 `__weak` 变量的地方都会用到它。

```
    id objc_loadWeakRetained(id *object);
```

它与上一个函数一样，只是省去了 autorelease。这能让编译器发出更高效的代码。

```
    void objc_moveWeak(id *dest, id *src);
```

它把弱指针从一处拷到另一处，与 `objc_copyWeak` 很像，区别是它可以选择清空源位置。最后是：

```
    id objc_storeWeak(id *object, id value);
```

这个函数向 `__weak` 变量存入新值。凡 `__weak` 变量作为赋值目标的地方都会用到它。

细心的读者会注意到，这里的函数远比需要的多。实际上，严格必需的只有两个：`objc_loadWeakRetained` 和 `objc_storeWeak`。其余全部可以基于这两个实现。例如，`objc_destroyWeak` 可以简单地实现为 `objc_storeWeak(location, nil);`。`objc_initWeak` 就是 `*location = nil; objc_storeWeak(location, value);`。而事实上 Objective-C 运行时也正是这样实现它们的。那要这么多额外函数干什么？

看样子只是为了给优化留后门。虽然这些函数_都_能基于两个原语实现，但取决于运行时的实现方式，某些场景（比如初始化一个确定从未用过的 `__weak` 变量）可能存在更快的路径。虽然运行时目前没有利用这一点，但让编译器生成更专门的调用，就为将来留出了可能。

由于 `PLWeakCompatibility` 并不关心旧平台上的速度，在新平台上又只是直接转发到 Apple 的实现，我们干脆把其余调用全部基于那两个原语来实现。

**骗过编译器**  
运行时函数的发出方式与其他任何函数调用一样。也就是说，只要你的 App 里有一个名为 `objc_storeWeak` 的函数，编译器就会乐呵呵地生成调用它的代码——它并没有与 Objective-C 运行时库硬绑定。然而默认情况下，当部署目标是不官方支持 `__weak` 的操作系统时，`clang` 会拒绝编译任何含 `__weak` 的代码。好在可以通过一对编译器标志告诉 `clang`：当前目标真的支持 `__weak`：

```
    -Xclang -fobjc-runtime-has-weak
```

第二个标志告诉 `clang`：运行时确实支持 `__weak`，即便部署目标显示相反。第一个标志是个小 hack，用来把第二个标志偷偷塞过顶层编译器驱动——那个驱动不认识这个标志，会直接忽略它。

有了这两个标志，`clang` 就接受 `__weak` 并发出相应的函数调用。剩下的就是提供我们自己对那些函数的实现。

**绕开 ARC**  
运行时函数的官方原型全都用 `id`。但这给 `PLWeakCompatibility` 出了个难题：我们的目标是产出一个单独的文件，丢进 ARC 项目就能启用 `__weak`，无需多少设置。这意味着这些函数会用 ARC 编译，而在其中使用 `id` 会让 ARC 发出一大堆多余的 retain 和 release 调用。

我最终决定改用 `void *` 代替 `id`，藏在一个方便的 typedef 后面：

```
    typedef void *PLObjectPtr;
```

如此一来，运行时函数的原型变成这样：

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location);
    PLObjectPtr objc_initWeak(PLObjectPtr *addr, PLObjectPtr val);
    void objc_destroyWeak(PLObjectPtr *addr);
    void objc_copyWeak(PLObjectPtr *to, PLObjectPtr *from);
    void objc_moveWeak(PLObjectPtr *to, PLObjectPtr *from);
    PLObjectPtr objc_loadWeak(PLObjectPtr *location);
    PLObjectPtr objc_storeWeak(PLObjectPtr *location, PLObjectPtr obj);
```

虽然这些原型不再与官方一致，它们仍是二进制兼容的——这才是要紧的。编译器发出运行时调用时并不会看这些原型，而 `id` 当作 `void *` 对待毫无问题。

**直通**  
当原生 `__weak` 支持可用时，我们不想越俎代庖。这意味着我们所有函数要做的第一件事，都是检查原生支持是否可用，可用就改为直通（fallthrough）调用原生实现。例如 `objc_loadWeak` 的实现大致长这样：

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location) {
        PLObjectPtr (*fptr)(PLObjectPtr *) = dlsym(RTLD_NEXT, "objc_loadWeakRetained");
        if(fptr != NULL)
            return fptr(location);

        return PLLoadWeakRetained(location);
    }
```

给不熟悉的朋友：`dlsym` 是一个能在运行时查找符号的函数，`RTLD_NEXT` 是一个特殊参数，告诉它去查找某个符号的"下一个"实现。换句话说：如果调用方不存在于 App 里，那时能找到哪个符号？这实质上是让它去找这个函数的原始运行时实现（如果存在）。

我们不想在这个函数的每次调用上都跑一遍 `dlsym`，那相当慢。用 `dispatch_once` 把检查限制为一次就能很好地提速。此外，声明函数指针时还得把函数类型再写一遍，有点烦——用 `__typeof__` 轻松解决。改造后的代码如下：

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location) {
        static dispatch_once_t fptrOnce
        static __typeof__(&objc_loadWeakRetained) fptr;
        dispatch_once(&fptrOnce, ^{ fptr = dlsym(RTLD_NEXT, "objc_loadWeakRetained"); });
        if(fptr != NULL)
            return fptr(location);

        return PLLoadWeakRetained(location);
    }
```

这已经足够通用，可以塞进宏里避免重复。这个宏接受函数名和参数，只要原始实现可用就自动直通调用：

```
    #define NEXT(name, ...) do { \
            static dispatch_once_t fptrOnce; \
            static __typeof__(&name) fptr; \
            dispatch_once(&fptrOnce, ^{ fptr = dlsym(RTLD_NEXT, #name); });\
            if (fallthroughEnabled && fptr != NULL) \
                return fptr(__VA_ARGS__); \
        } while(0)
```

注意额外的 `fallthroughEnabled` 标志，它纯粹为测试而设：关掉直通后，单元测试就能把两种情况都练一遍。

有了这个宏，就可以快速写出所有非原语函数的实现：

```
    PLObjectPtr objc_initWeak(PLObjectPtr *addr, PLObjectPtr val) {
        NEXT(objc_initWeak, addr, val);
        *addr = NULL;
        return objc_storeWeak(addr, val);
    }

    void objc_destroyWeak(PLObjectPtr *addr) {
        NEXT(objc_destroyWeak, addr);
        objc_storeWeak(addr, NULL);
    }

    void objc_copyWeak(PLObjectPtr *to, PLObjectPtr *from) {
        NEXT(objc_copyWeak, to, from);
        objc_initWeak(to, objc_loadWeak(from));
    }

    void objc_moveWeak(PLObjectPtr *to, PLObjectPtr *from) {
        NEXT(objc_moveWeak, to, from);
        objc_copyWeak(to, from);
        objc_destroyWeak(from);
    }

    PLObjectPtr objc_loadWeak(PLObjectPtr *location) {
        NEXT(objc_loadWeak, location);
        return objc_autorelease(objc_loadWeakRetained(location));
    }
```

原语函数 `objc_loadWeakRetained` 只需转发到另一个内部函数——那个函数的存在只是为了在代码里把事情分得更清楚：

```
    PLObjectPtr objc_loadWeakRetained(PLObjectPtr *location) {
        NEXT(objc_loadWeakRetained, location);

        return PLLoadWeakRetained(location);
    }
```

`objc_storeWeak` 的实现稍微复杂些。它先像其他函数一样直通调用运行时实现（如果有）：

```
    PLObjectPtr objc_storeWeak(PLObjectPtr *location, PLObjectPtr obj) {
        NEXT(objc_storeWeak, location, obj);
```

之后调用一个内部函数，注销当前位于 `location` 的弱引用：

```
        PLUnregisterWeak(location, obj);
```

接着把新值存入 `location`，若新值不是 `nil`，就登记这个位置：

```
        if (obj != nil)
            PLRegisterWeak(location, obj);
```

最后直接返回被存入的对象：

```
        return obj;
    }
```

至此，这套功能被分解成三个内部原语函数。`PLLoadWeakRetained` 加载弱引用并返回指向它的已保留指针。`PLRegisterWeak` 为特定对象登记一个新的弱引用位置，并确保对象销毁时该位置被置零。`PLUnregisterWeak` 把位置从对象的弱引用列表中移除，使对象销毁时不再碰它。这三个函数实现完毕，`PLWeakCompatibility` 就大功告成了。

**计划**  
在 Cocoa 里做一个零值弱引用系统，有两大挑战。其一是准确弄清对象何时被销毁，并在那一刻把指向它的所有引用置零。

其二是在加载弱引用时避免竞态条件（race condition）。在 Cocoa 中，从最后一条 `release` 消息发给一个将死对象，到该对象的 `dealloc` 方法被调用，中间存在一段间隙。在这个间隙里加载指向该对象的弱引用_必须_返回 `nil`，因为对象的销毁在那一刻已不可避免，此时保留它也救不活它。

这两个挑战都已由 [`MAZeroingWeakRef`](https://github.com/mikeash/MAZeroingWeakRef) 解决，它用动态派生子类与 isa 调配（isa-swizzling）来搞定。`PLWeakCompatibility` 在 `MAZeroingWeakRef` 存在时会直接转发给它。不过我们还想要一个更简单的实现，能与其余代码放在一起，做到完全独立使用。因此 `PLWeakCompatibility` 也需要自己的解法。

`PLWeakCompatibility` 的解法是调配目标对象的 `release` 与 `dealloc` 方法。调配 `dealloc` 解决了"何时知道对象被销毁"的难题。被调配的 `release` 方法会把对象加进一个"正在释放"的对象列表。任何解析指向列表中对象之弱引用的尝试都会阻塞，直到这次 `release` 完成——那时对象要么还活着、可以取得弱引用，要么已死、弱引用为零。不过这一切的细节得等到第二部分再讲！

**结语**  
`PLWeakCompatibility` 是在旧系统上使用 ARC 的一大助力。只需向编译器传几个标志，就能骗它发出那些启用 `__weak` 的运行时函数调用，哪怕运行时并不支持。然后，再提供我们自己的、语义相同的函数实现，就能在不原生支持 `__weak` 的系统上实现完整的 `__weak` 兼容。

最后，我们把多个运行时函数分解成三个原语函数：一个负责加载弱引用，一个负责登记，一个负责注销。下次我会详细讲解这三个函数的实现与工作原理。

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论的 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-05-18-a-tour-of-plweakcompatibility-part-i.html)

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
