---
title: 将 block 转换为函数指针
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-02-12-trampolining-blocks-with-mutable-code.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:87f53fcc883c7c36'
translated: true
---

> 原文：[converting blocks into function pointers](https://www.mikeash.com/pyblog/friday-qa-2010-02-12-trampolining-blocks-with-mutable-code.html)　·　mikeash.com Friday Q&A

发布于 2010-02-12 18:20 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文文本订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2010-02-19: 字符编码](https://www.mikeash.com/pyblog/friday-qa-2010-02-19-character-encodings.html)  
上一篇文章：[Friday Q&A 2010-02-05: 使用 Continuation Passing 风格的错误返回](https://www.mikeash.com/pyblog/friday-qa-2010-02-05-error-returns-with-continuation-passing-style.html)  
标签：[汇编](https://www.mikeash.com/pyblog/?tag=assembly) [blocks](https://www.mikeash.com/pyblog/?tag=blocks) [邪恶](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [蹦床](https://www.mikeash.com/pyblog/?tag=trampoline)

Friday Q&A 2010-02-12: 使用可变代码实现 Block 的蹦床（Trampoline）

作者：[Mike Ash](https://www.mikeash.com/)

**背景**  
Block 真的很棒，但 Mac 上并非所有 API 都已经支持它们。很多 API 仍然使用接受函数指针的旧式回调。虽然你可以构建小的适配函数来让那些 API 使用 block，但每次你想用的时候都得这么做，这很烦人，尤其因为每个这样的 API 工作方式都略有不同。

我构建的这个玩具项目允许将一个 block 转换为一个函数指针，当该函数指针被调用时，它会调用这个 block。然后可以将这个函数指针传递给任何接受函数指针回调的 API，它会调用你的 block，而 API 对此毫不知情。

**警告**  
我即将讨论的代码是一个*极端的 hack*。它依赖于底层平台调用约定的细节，以至于我甚至懒得让它能在 `x86_64` 以外的任何架构上工作。即使在 `x86_64` 上，它也有重要的限制。本文的目的*不是*提供一个实用的库，而是探索一些有趣但不实用的底层 hack。在任何情况下都*不要*使用此代码。

**代码**  
既然说清楚了这一点，让我们来谈谈代码！如果你想跟随完整的代码库，可以在通常的位置找到它：

```
    svn co http://mikeash.com/svn/BlockFptr/
```

**概念**  
在我深入细节之前，让我们快速讨论一下整个机制应该如何工作。这样我就不用后面重复一千遍了，让我先声明，我讨论的每个平台特定细节都是关于 `x86_64` 的，不一定适用于其他平台，甚至不一定适用于 OS X 运行的其他平台。

如果你还习惯于 32 位的世界，请记住这意味着指针是*八*个字节长。

首先，快速回顾一下函数指针是什么：它只是一个指向函数开头的普通旧指针。为了调用它，编译器会生成代码来设置栈和寄存器以传递参数并保存临时值，然后简单地跳转到内存中的那个位置。执行从那里继续。

Block 的工作方式类似，但更复杂一些。block 是一个 *Objective-C 对象*，这意味着它是一片内存区域，其前八个字节包含一个 `isa` 指针。block 的其余部分包含各种其他对 block 有用的数据，比如捕获的局部变量。其中一部分数据是一个指向 block 实际实现的函数指针。为了调用一个 block，编译器生成的代码会简单地获取这个函数指针，然后像其他任何函数指针一样调用它。

在运行时，函数指针和 block 之间的主要区别是*上下文*。函数指针是纯代码，没有关联的数据。每当你遇到一个函数指针回调 API 时，你几乎总会看到一个与之配套的*上下文指针*。通常这只是一个指向任意数据的 `void *`。这是调用者通过 API 将*上下文*传递给函数指针的一种方式，这样函数指针就可以知道发生了什么。一个没有上下文的纯函数指针实际上只能访问传递给它的参数和全局变量。使用上下文指针，它可以回溯到设置回调的对象、当前正在处理的特定调用的数据等。

Block 自动携带上下文。指向其实现的函数指针将指向 block 对象本身的指针作为一个隐藏的第一个参数。通过这种方式，block 能够访问捕获的局部变量，从而让它们能够访问所需的所有上下文，且无需程序员做额外工作。

我的代码的目标是弥合这个上下文差距。我决定解决它的方法是构建一个*蹦床（trampoline）*。这是一小段代码，其中嵌入了 block 的地址。当蹦床执行时，它加载 block 的地址和 block 的函数指针，然后跳转到该函数指针，并将 block 作为第一个参数传递。通过将 block 地址直接嵌入代码中，这解决了*上下文*的问题，因为现在一个指针就能让你同时获得代码和数据。

为了将特定 block 的地址嵌入代码中，该代码需要被复制和修改，这是所有这些中最*有趣*的部分。

**蹦床工厂**  
是的，你可以复制、修改然后执行代码。这甚至不算太难！你确实需要确保相关代码能够容忍被修改（不包含任何在移动后失效的 PC 相对引用），但如果你用汇编编写，这很容易，而为了进行蹦床所需的参数混排和尾部调用（tail-calling），我无论如何都需要使用汇编。

可以通过从其指针开始进行内存拷贝来访问代码。一个小汇编技巧可以让你找出代码的结束位置。一旦将其复制到堆上，你就可以随意修改其内容。完成后，准备好运行它时，你可以调用 `mprotect()` 使该数据可执行，然后就可以调用它了。

然而，这个过程开销很大。`mprotect()` 的调用是一个系统调用。此外，它只对完整的页（4096 字节）起作用，但蹦床本身只有几十个字节，所以有很多浪费的空间。为了降低开销，我想要一种批量构建蹦床的方法，并且在初始构建后*无需*修改其代码即可重用它们。

因此，我的架构增加了一层额外的间接寻址。代码包含一个指向另一块内存区域的指针。那部分内存又包含一个指向 block 的指针。想要将蹦床重新指向一个新的 block？很简单，只需修改那额外的内存块即可。这样，我可以用蹦床的副本填满整个 4096 字节的页面，然后再填写它们的 block 指针。

如果这让你感到困惑（怎么可能不困惑呢？），这里有一个示意图：

```
    Trampoline      Intermediary        Block
    ----------      ------------        -----
    ...code...
    ...code...
    ...code...                         +------+
      pointer ------> pointer -------->|block |
    ...code...                         |object|
    ...code...                         +------+
    ...code...
```

**汇编**  
闲聊够多了，让我们来看一些代码。

蹦床需要做四件事。首先，将中介指针加载到一个寄存器中。涉及的特定寄存器是 `%r11`，一个指定的暂存寄存器，其值不会跨越函数调用保留：

```
    movabsq $0xdeadbeefcafebabe, %r11
```

第二，将 block 指针从中介加载到 `%rdi`，即保存函数第一个参数的寄存器：

```
    mov (%r11), %rdi
```

第三，将 block 中的函数指针提取到暂存寄存器 `%r11`：

```
    mov BLOCK_FUNCTION_POINTER_OFFSET(%rdi), %r11
```

（`BLOCK_FUNCTION_POINTER_OFFSET` 只是一个 `#define` 为 `16` 的宏。）

第四，跳转到 `%r11` 中包含的地址：

```
    jmp *%r11
```

第一条指令中使用的指针值 `0xdeadbeefcafebabe` 是代码中的字面量。我使用一个可识别的模式，以便稍后修改此代码的代码可以搜索到它，这样我就不必硬编码指针值的偏移量。

**查找地址**  
搜索 `0xdeadbeefcafebabe` 的代码很简单。首先，我们从一个外部定义开始，让编译器能够找到汇编代码：

```
    extern char Trampoline;
    extern char TrampolineEnd;
```

这些对应于汇编中使用的标签。第一个是蹦床函数本身，第二个是紧跟在它后面的标签，以便于识别其结束位置。

注意，这些不是指针。当程序被链接时，`Trampoline` 最终会指向蹦床函数的第一个字节。为了获得一个指向蹦床的指针，我们写 `&Trampoline`，同样地，写 `&TrampolineEnd` 来获得结束位置。`char` 类型是相当随意的，但它使得对结果指针进行指针算术运算变得容易，因为根据定义，`char` 是一个字节长。

鉴于此，查找魔术值的代码非常简单：只需循环遍历，尝试每个内存位置，直到找到它或者超出范围。当然，我忍不住要加入一点 [Grand Central Dispatch](http://www.mikeash.com/pyblog/friday-qa-2009-08-28-intro-to-grand-central-dispatch-part-i-basics-and-dispatch-queues.html) 来使这个值被延迟计算：

```
    static int TrampolineAddrOffset(void)
    {
        static int addrOffset;
        static dispatch_once_t pred;
        dispatch_once(&pred, ^{
            uint64_t magic = 0xdeadbeefcafebabeULL;
            for(addrOffset = 0; addrOffset <= &TrampolineEnd - &Trampoline - sizeof(uint64_t); addrOffset++)
                if(*((uint64_t *)(&Trampoline + addrOffset)) == magic)
                    break;
        });
        
        return addrOffset;
    }
```

大概在这个时候，你可能会想，如果代码*恰好*在魔术指针值本身之前的某个位置包含了 `0xdeadbeefcafebabe` 的位模式，并且这会得到错误的偏移量，该怎么办？

好吧，这极不可能（如果你看看这可能代表什么指令序列，很可能是完全不可能的），但即使真的发生了，最终也没关系。用汇编编写蹦床的美妙之处在于，每次构建它都会产生完全相同的输出。这不像写 C 代码，编译器可能会根据优化级别、其他代码、编译器版本、月相等等生成不同的代码。因此，如果这段代码一次返回了正确的值，它每次都会这样做。同样地，如果它失败了，它也会立即失败。唯一的风险是在修改蹦床之后，所以你只需要快速测试一下，确保这一部分仍然正常工作。

**中介**  
中介相当简单，但对于蹦床的需求来说稍微复杂了一点。原因是我希望重用这些值，这意味着在用完之后要将它们保存在缓存中。为了最大程度的线程安全和速度，缓存采用了 [OSQueue](http://developer.apple.com/Mac/library/documentation/Darwin/Reference/ManPages/man3/OSAtomicDequeue.3.html) 的形式。这反过来要求中介有两个字段（一个用于队列内部的 `next` 指针，另一个用于反向引用与其关联的蹦床以便我们获取它），尽管蹦床只需要一个。这是中介的定义：

```
    struct Intermediary
    {
        // 在队列中时，第一个字段是必需的 'next' 指针
        // 在使用中时，第一个字段是 block 指针
        void *nextPtrOrBlock;
        
        // 在队列中时，第二个字段指向关联的蹦床
        // 在使用中时，第二个字段未使用
        void *trampoline;
    };
```

**创建蹦床**  
现在我们准备好实际将蹦床复制到堆上并将其指向它的中介了。给定一个堆中的位置、一个长度（从 `Trampoline` 和 `TrampolineEnd` 计算得出）、一个偏移量（来自 `TrampolineAddrOffset`）和一个中介指针，执行复制和修改的代码很容易。首先，复制代码：

```
    static void CreateTrampoline(void *destination, int length, int addrOffset, struct Intermediary *intermediary)
    {
        memcpy(destination, &Trampoline, length);
```

填写中介：

```
        intermediary->nextPtrOrBlock = NULL;
        intermediary->trampoline = destination;
```

（这里还没有分配中介的 block 指针，因为我们稍后会在真正有 block 时再做。这里为了安全起见，我将其设置为 `NULL`。）

最后，将新创建的蹦床指向中介：

```
        *((void **)(destination + addrOffset)) = &intermediary->nextPtrOrBlock;
    }
```

**创建蹦床工厂**  
这就是如何创建单个蹦床，但我们的计划是批量构建它们，以分摊 `mprotect()` 调用的成本。为此，我构建了一个函数，它创建一个充满蹦床的页面，然后将它们全部入队到 `OSQueue` 上，以便稍后可以取出。

首先要做的是计算蹦床的长度、中介地址的偏移量、系统的页面大小，以及多少蹦床能放进该页面：

```
    void CreateNewFptrsAndEnqueue(void)
    {
        int trampolineLength = &TrampolineEnd - &Trampoline;
        int addrOffset = TrampolineAddrOffset();
        
        int pageSize = getpagesize();
        int howmany = pageSize / trampolineLength;
```

接下来，为蹦床分配一个页面（使用 `valloc`，以确保结果地址实际上是页面对齐的），并为中介分配一块内存：

```
        void *page = valloc(pageSize);
        
        struct Intermediary *intermediaries = malloc(howmany * sizeof(*intermediaries));
```

接下来，循环创建所有蹦床：

```
        for(int i = 0; i < howmany; i++)
        {
            void *destination = page + i * trampolineLength;
            CreateTrampoline(destination, trampolineLength, addrOffset, &intermediaries[i]);
        }
```

然后将页面标记为可执行：

```
        int err = mprotect(page, pageSize, PROT_READ | PROT_EXEC);
        if(err)
            perror("mprotect");
```

最后，将它们全部推入蹦床缓存：

```
        for(int i = 0; i < howmany; i++)
        {
            void *trampoline = page + i * trampolineLength;
            EnqueueCachedFptr(trampoline);
        }
    }
```

接下来，我们需要一小段代码，它将从那个全局缓存中取出一个蹦床，并将中介设置为指向一个 block：

```
    static void *DequeueCachedFptr(id block)
    {
        struct Intermediary *intermediary = OSAtomicDequeue(&gFptrCache, 0);
        if(!intermediary)
            return NULL;
        
        intermediary->nextPtrOrBlock = [block copy];
        return intermediary->trampoline;
    }
```

最后，我们可以把它们放在一起，用一个面向公众的函数返回一个蹦床。它首先尝试缓存。如果缓存为空，它创建一个完整的蹦床页面，然后再次尝试缓存。在不太可能的情况下缓存*仍然*为空（其他线程在它拿到任何蹦床之前用光了所有蹦床），那么它创建另一个页面并重试，并一直这样做直到它拿到一个：

```
    void *CreateBlockFptr(id block)
    {
        void *fptr;
        while(!(fptr = DequeueCachedFptr(block)))
            CreateNewFptrsAndEnqueue();
        return fptr;
    }
```

最后，返回的参数可以像函数指针一样用于实际调用 block：

```
    void (*fptr)(void) = CreateBlockFptr(^{ printf("hello, world!\n"); });
    fptr();
```

这将打印出 `hello, world!`

**参数移位**  
如果你运行这段代码，你会发现它对不接受参数的 block 工作正常，但对接受参数的 block 效果不佳。问题在于函数签名不匹配：由于 block 实现将 block 指针作为隐式的第一个参数，所有其他参数都被移位了。因为蹦床在它被调用时不接触已经就位的参数，结果是第一个参数被 block 指针覆盖，其余所有参数最终都被移位了。

这里有一些坏消息：在一般情况下，如果不预先知道完整的函数签名（这个蹦床旨在与任意函数指针一起工作），*不可能*在 `x86_64` ABI 下可靠地将参数向下移位一个位置。

更具体地说：在 `x86_64` ABI 下，前六个 `INTEGER` 类型的参数（基本上是整数和指针，以及一些由多个整数/指针类型组成的小结构体）被存储在六个通用寄存器中，它们依次是：`%rdi`、`%rsi`、`%rdx`、`%rcx`、`%r8` 和 `%r9`。超过六个，它们被溢出到栈上。问题是很多其他参数也可能被溢出到栈上，而这种情况发生的顺序取决于函数所接受的所有参数的确切性质和顺序。

蹦床需要将所有那些寄存器向下移位一个位置（将 `%rdi` 移到 `%rsi`，`%rsi` 移到 `%rdx`，等等）*并且*将 `%r9` 的内容溢出到栈上。然而，不可能知道要溢出到哪里，甚至是否需要这样做。

仅仅因为我们不能在一般情况下解决这个问题，并不意味着我们不能解决足够多的问题使其变得有用。如果我们跳过将 `%r9` 溢出到栈上的步骤，结果将会对接受超过五个 `INTEGER` 类型的函数失败，但大多数回调不会受此影响。只需将寄存器向下移位一个就足够了。这可以通过在开头放置一系列 `mov` 指令来将所有参数下移，然后像之前演示的那样继续执行蹦床的其余部分来完成。最终结果如下：

```
    .globl _Trampoline
    _Trampoline:
        // 将整数参数寄存器向下移位一个位置
        // 为隐式的 block ptr 参数腾出空间
        mov %r8, %r9
        mov %rcx, %r8
        mov %rdx, %rcx
        mov %rsi, %rdx
        mov %rdi, %rsi
        
        // 将 block 指针的指针移到 r11，运行时替换为虚拟值
        movabsq $0xdeadbeefcafebabe, %r11
        // 解引用 block 指针的指针，将 block 指针移到 %rdi
        mov (%r11), %rdi
        // 将 block 实现函数指针提取到 %r11
        mov BLOCK_FUNCTION_POINTER_OFFSET(%rdi), %r11
        // 跳转到 block 实现
        jmp *%r11
    .globl _TrampolineEnd
    _TrampolineEnd:
        .long 0
        .long 0
```

由于蹦床复制/修改代码已经全面通用化，并且只是搜索魔术指针值，因此无需做任何更改即可适应新的蹦床。如果你尝试这个，你会发现它能够和参数一起工作……只要你不超过五个 `INTEGER` 类型的参数。

**示例**  
构建过程很有趣，但是*使用*它呢？

这些示例使用了一个 `AutoBlockFptr` 函数，它基本上包装了 `CreateBlockFptr` 来创建一个“自动释放”的 block 蹦床，当外层的 `NSAutoreleasePool` 被弹出时，它会自动销毁。我不会深入探讨它是如何工作的细节（我甚至根本没有涉及蹦床如何被回收），但如果你想看的话，可以[在代码中](http://mikeash.com/svn/BlockFptr/)查看。

`pthread` API 是一个处理函数指针的经典 API。你用 `pthread_create` 创建一个新线程，但它接受一个函数指针和一个上下文指针，这总是很麻烦。当然，既然我们有了 Grand Central Dispatch，`pthread` 可能就没那么有用了，但在很多地方它仍然派得上用场。让我们使用这个新代码来适配一个 block，而不是处理函数指针：

```
    pthread_t thread;
    pthread_create(&thread, NULL, AutoBlockFptr(^(void *ignore) {
        printf("hello, world from a pthread!\n");
    }), NULL);
    pthread_join(thread, NULL);
```

这正如你所期望的那样工作。`pthread` API 从未如此简单！

一些 Objective-C 运行时 hack 怎么样？

```
    int captured = 99;
    class_addMethod([NSObject class], @selector(printInt:), CreateBlockFptr(^(id self, SEL _cmd, int x) {
        printf("in object %p, the captured integer is %d, the passed integer is %d\n", self, captured, x);
    }), "v@:i");
    NSObject *obj = [[NSObject alloc] init];
    [obj printInt: 42];
    [obj printInt: -11];
    [obj release];
```

再次，完美工作：

```
    in object 0x1002003d0, the captured integer is 99, the passed integer is 42
    in object 0x1002003d0, the captured integer is 99, the passed integer is -11
```

CoreFoundation 是函数指针常见的地方。创建一个带有自定义回调的 `CFArray` 怎么样，所有回调都内联编写？

```
    CFArrayCallBacks callbacks = {
        0,
        AutoBlockFptr(^(CFAllocatorRef allocator, const void *value) {
            NSLog(@"retain %@", value);
            return value;
        }),
        AutoBlockFptr(^(CFAllocatorRef allocator, const void *value) {
            NSLog(@"release %@", value);
        }),
        AutoBlockFptr(^(CFAllocatorRef allocator, const void *value) {
            NSLog(@"description of %@", value);
            return [(id)value description];
        }),
        AutoBlockFptr(^(CFAllocatorRef allocator, const void *value1, const void *value2) {
            NSLog(@"equality %@ %@", value1, value2);
            return (Boolean)[(id)value1 isEqual: (id)value2];
        })
    };
    
    CFMutableArrayRef array = CFArrayCreateMutable(NULL, 0, &callbacks);
    CFArrayAppendValue(array, @"first object");
    CFArrayAppendValue(array, @"second object");
    CFArrayRemoveAllValues(array);
```

运行时，产生如下输出：

```
    2010-02-11 00:21:51.238 BlockFptr[9201:a0f] retain first object
    2010-02-11 00:21:51.241 BlockFptr[9201:a0f] retain second object
    2010-02-11 00:21:51.242 BlockFptr[9201:a0f] release first object
    2010-02-11 00:21:51.243 BlockFptr[9201:a0f] release second object
```

就是这样！

**注意事项**  
我已经提到过这段代码是危险的，你永远不应该使用它，但我想再次重申这个警告。有*很多*限制：

1. 不能与超过五个 `INTEGER` 参数一起工作。
2. 完全不能与 `struct` 返回值一起工作，如果该 `struct` 大到足以触发特殊的 `struct` 返回调用约定。大的结构体本质上是通过引用返回的，方法是传递一个指针作为函数的隐式第一个参数。蹦床会将 block 指针放在那里，导致混乱。这可以通过为 `struct` 返回添加第二个蹦床来解决。
3. 管理蹦床的生命周期可能很困难。对于一次性使用，比如与 `pthread_create` 一起使用，你可以在你的 block 开始运行后立即销毁蹦床。对于进程生命周期内持续存在的使用，比如向 Objective-C 对象添加一个永久方法，你可以直接创建它然后放着不管。当它可能被多次调用，但你最终想要清理它时，事情就变得棘手了，因为普通代码只是假设任何函数指针都会永远存在。`CFArray` 的例子就是一个很好的例子：没有简单的方法将蹦床的生命周期与 `CFArray` 的生命周期关联起来。（最好的方法可能是使用 Objective-C 的关联对象 API，但这相当难看。）
4. 最重要的是：即使你符合所有这些限制，蹦床也只在 `x86_64` 上存在。虽然可以移植到其他架构，但这些其他架构上的参数和返回类型限制可能会不同，从而破坏以前能正常工作的代码。（在 iPhone OS 上，Apple 根本不允许这种运行时代码生成。）

尽管有这些问题，这仍然是一个很好的学习体验和一个有趣的玩具。

**结论**  
这种底层的汇编 hack 可能很棘手，而且正如你所看到的，结果并不总是完全实用。然而，它非常有趣，也是了解系统底层如何组合在一起的绝佳方式。

本周就到这里。一如既往（除了本周！），Friday Q&A 由用户建议驱动，所以如果你有一个希望在这里看到的话题，[请发送给我](mailto:mike@mikeash.com)！否则，我们下周见。

喜欢这篇文章吗？我正在销售包含所有这些文章的完整书籍！第二卷和第三卷现已出版！它们有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里获取更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2010-02-12-trampolining-blocks-with-mutable-code.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会在我全权决定下被公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
