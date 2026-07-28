---
title: 'Friday Q&A 2012-11-16：让我们构建 objc_msgSend'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4830a06afb70dcc9'
translated: true
---

> 原文：[Friday Q&A 2012-11-16: Let's Build objc_msgSend](https://www.mikeash.com/pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html)　·　mikeash.com Friday Q&A

发布于 2012-11-16 14:27 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([全文 feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)
下一篇文章: [Friday Q&A 2012-11-30：让我们构建一个 Mach-O 可执行文件](https://www.mikeash.com/pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html)
上一篇文章: [Friday Q&A 2012-11-09：dyld：OS X 上的动态链接](https://www.mikeash.com/pyblog/friday-qa-2012-11-09-dyld-dynamic-linking-on-os-x.html)
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2012-11-16：让我们构建 objc_msgSend

作者：[Mike Ash](https://www.mikeash.com/)

**Tramapoline！Trampopoline！**
每当你编写一条 Objective-C 消息发送：

```
    [obj message]
```

编译器会生成对 `objc_msgSend` 的调用：

```
    objc_msgSend(obj, @selector(message));
```

然后 `objc_msgSend` 负责分发这条消息。

它是怎么做到的？它查找合适的函数指针（即 `IMP`）来调用，然后跳转过去。任何传递给 `objc_msgSend` 的参数在跳转后都会成为该 `IMP` 的参数。`IMP` 的返回值最终会成为调用方看到的返回值。

因为 `objc_msgSend` 只是接管控制权足够长的时间，以获取正确的函数指针并直接跳转过去，所以它有时被称为_跳板（trampoline）_。通常，任何用于将代码重定向到其他地方的小段代码都可以称为跳板。

正是这种跳板行为让 `objc_msgSend` 显得特别。因为它只是查找正确的代码，然后直接跳转过去，所以它相当通用。它适用于传递给它的_任何_参数组合，因为它只是保持这些参数原样不动，供方法 `IMP` 读取。返回值稍微复杂一些，但实际上，所有可能的返回类型都可以通过 `objc_msgSend` 的少数几个变体来处理。

不幸的是，这种跳板行为无法用纯 C 语言编写。没有办法编写一个 C 函数，能将通用参数透传给另一个函数。你可以通过使用可变参数（variable arguments）来接近这个目标，但可变参数的传递方式与普通参数不同且速度更慢，因此它与常规 C 参数不兼容。

如果你_可以_用 C 语言编写 `objc_msgSend`，基本思路看起来会像这样：

```
    id objc_msgSend(id self, SEL _cmd, ...)
    {
        Class c = object_getClass(self);
        IMP imp = class_getMethodImplementation(c, _cmd);
        return imp(self, _cmd, ...);
    }
```

这实际上有点过于简化了。还有一个方法缓存（method cache）来加速整个查找过程，所以更像是这样：

```
    id objc_msgSend(id self, SEL _cmd, ...)
    {
        Class c = object_getClass(self);
        IMP imp = cache_lookup(c, _cmd);
        if(!imp)
            imp = class_getMethodImplementation(c, _cmd);
        return imp(self, _cmd, ...);
    }
```

区别在于，为了速度，`cache_lookup` 是内联实现的。

**汇编语言**
在 Apple 的运行时中，整个函数都是用汇编语言实现的，以获得最高速度。每一条 Objective-C 消息发送都会经过 `objc_msgSend`，而 App 中最简单的操作也可能导致成千上万条消息。

为了简化一些，我自己的实现将用汇编语言完成最少的工作，而所有逻辑都在一个单独的 C 函数中。汇编代码本身将完成相当于以下 C 代码的工作：

```
    id objc_msgSend(id self, SEL _cmd, ...)
    {
        IMP imp = GetImplementation(self, _cmd);
        imp(self, _cmd, ...);
    }
```

然后 `GetImplementation` 可以以更易理解的方式完成所有工作。

汇编代码需要：

1.  将所有可能的参数保存到安全的地方，这样 `GetImplementation` 就不会覆盖它们。
2.  调用 `GetImplementation`。
3.  将返回值保存到某处。
4.  恢复所有参数值。
5.  跳转到 `GetImplementation` 返回的 `IMP`。

那么让我们开始吧！

我将在这里使用 x86-64 汇编语言，因为这是在 Mac 上最便于使用的架构。同样的原则也适用于 i386 或 ARM。

这个函数放在它自己的文件中，我将其命名为 `msgsend-asm.s`。这个文件可以作为另一个源文件传给编译器，它会被汇编并链接到程序的其余部分。

首先要做的是实际声明全局符号。出于无聊的历史原因，C 函数的全局符号名称前面会多一个下划线：

```
    .globl _objc_msgSend
    _objc_msgSend:
```

编译器会愉快地链接到最近可用的 `objc_msgSend`。简单地将这个文件链接到测试 App 中，就足以让 `[obj message]` 表达式使用我们自己的代码而不是 Apple 的运行时，这在测试这段代码以确保它实际工作时非常方便。

整数和指针参数通过寄存器 `%rsi`、`%rdi`、`%rdx`、`%rcx`、`%r8` 和 `%r9` 传递。任何超出这些寄存器容纳范围的额外参数会通过栈传递。这个函数首先将这六个寄存器也保存到栈上，以便稍后可以恢复它们：

```
    pushq %rsi
    pushq %rdi
    pushq %rdx
    pushq %rcx
    pushq %r8
    pushq %r9
```

除了这些寄存器外，`%rax` 寄存器某种程度上充当了一个隐藏参数。它用于可变参数调用，在这种情况下它存储传入的向量寄存器的数量，被调用函数会用这个信息来正确准备可变参数列表。以防目标方法是一个可变参数方法，我也保存了这个寄存器：

```
    pushq %rax
```

为了完整性，用于传递浮点参数的 `%xmm` 寄存器实际上也应该被保存。但是，如果我可以安全地假设 `GetImplementation` 不使用任何浮点数，那么我就可以忽略它们，我只是为了让代码更短才这样做。

接下来，我对齐栈。Mac OS X 要求在调用函数时栈对齐到 16 字节边界。上面的代码无论如何都会给我们留下一个对齐的栈，但最好有显式处理它的代码，这样你就不必担心一切是否对齐，或者想知道为什么你的 App 在 `dyld` 函数中崩溃。为了对齐栈，我在将 `%r12` 的原始值保存到栈上之后，再将当前的栈指针保存到 `%r12` 中。选择 `%r12` 有点随意，任何调用方保存的寄存器都可以。重要的是，这个值保证在调用 `GetImplementation` 期间保持不变。然后我对栈指针执行 `and` 操作，与 `-0x10`，这仅仅清除了低四位：

```
    pushq %r12
    mov %rsp, %r12
    andq $-0x10, %rsp
```

现在栈指针对齐了。它也安全地避开了上面所有已保存的寄存器，因为栈向下增长，而这个对齐操作只会让它进一步向下移动。

终于到了调用 `GetImplementation` 的时候了。它接受两个参数，`self` 和 `_cmd`。调用约定要求这两个参数分别放入 `%rsi` 和 `%rdi`。但是，它们是以这种方式传入 `objc_msgSend` 的，并且没有被移动过，所以不需要做任何事情来将它们放到正确的位置。唯一需要做的就是实际调用 `GetImplementation`，它的名称前面也会加一个下划线：

```
    callq _GetImplementation
```

整数和指针返回值通过 `%rax` 返回，所以返回的 `IMP` 就在那里。由于必须恢复 `%rax` 的原始状态，返回的 `IMP` 需要移到别处。我随意选择将它存储到 `%r11`：

```
    mov %rax, %r11
```

现在是时候开始把所有东西恢复原状了。第一件事是恢复栈指针，它被保存在 `%r12` 中，并恢复 `%r12` 的旧值：

```
    mov %r12, %rsp
    popq %r12
```

然后按照与压栈相反的顺序从栈中弹出所有参数寄存器：

```
    popq %rax
    popq %r9
    popq %r8
    popq %rcx
    popq %rdx
    popq %rdi
    popq %rsi
```

现在一切都准备好了。参数寄存器已经恢复到之前的状态。所有为目标方法准备的参数都在目标方法期望找到它们的位置。`IMP` 本身在 `%r11` 中，所以唯一要做的就是跳转到那里：

```
    jmp *%r11
```

就是这样！汇编代码中不需要再做任何事情。跳转将控制权传递给方法实现。从那段代码的角度来看，看起来_完全_就像消息发送方直接调用了该方法一样。上面的所有间接操作都消失了。当方法返回时，它将直接返回到 `objc_msgSend` 的调用方，无需任何进一步干预。方法的任何返回值都会在正确的位置找到。

当涉及到不常见的返回值时，会有一些微妙之处。大的 `struct`（任何大到无法在寄存器中返回的 `struct`）是最常见的例子。在 x86-64 上，大的 `struct` 通过使用一个隐藏的第一个参数来返回。当你像这样调用时：

```
    NSRect r = SomeFunc(a, b, c);
```

该调用会被翻译成更像这样：

```
    NSRect r;
    SomeFunc(&r, a, b, c);
```

用于返回值的內存地址通过 `%rdi` 传递。由于 `objc_msgSend` 期望 `%rdi` 和 `%rsi` 包含 `self` 和 `_cmd`，因此对于返回大的 `struct` 的消息来说，这行不通。这个基本问题在许多不同平台上都存在。运行时通过提供一个单独的 `objc_msgSend_stret` 函数来解决这个问题，该函数用于 `struct` 返回值，其工作方式类似于 `objc_msgSend`，但知道在 `%rsi` 中找到 `self`，在 `%rdx` 中找到 `_cmd`。

在某些平台上，对于返回浮点值的消息也会出现类似的问题。在这些平台上，运行时提供了 `objc_msgSend_fpret`（在 x86-64 上，对于极其特殊的情况，还有 `objc_msgSend_fpret2`）。

**方法查找**
让我们继续实现 `GetImplementation`。上面的汇编跳板意味着这段代码可以用 C 语言编写。请记住，在真实的运行时中，这段代码全部是直接汇编的，以获得可能的最佳速度。这不仅允许对代码进行精细控制，而且还消除了像上面代码那样保存和恢复所有寄存器的需要。

`GetImplementation` 可以简单地调用 `class_getMethodImplementation` 就完事了，把所有工作都推给 Objective-C 运行时。不过，这有点无聊。真正的 `objc_msgSend` 会首先在类的方法缓存（method cache）中查找，以获得最高速度。由于 `GetImplementation` 旨在模仿 `objc_msgSend`，它也会这样做。只有当缓存中没有给定选择器（selector）的条目时，它才会回退到查询运行时。

我们首先需要一些 `struct` 定义。方法缓存是一组通过类结构体访问的私有结构，所以要访问它，我们需要自己的定义。请注意，虽然是私有的，但这些定义都可以作为 Apple 开源发布的 Objective-C 运行时的一部分获得。

首先是单个缓存条目的定义：

```
    typedef struct {
        SEL name;
        void *unused;
        IMP imp;
    } cache_entry;
```

非常简单。别问我关于 `unused` 字段的事，我不知道它为什么在那里。下面是整个缓存的定义：

```
    struct objc_cache {
        uintptr_t mask;
        uintptr_t occupied;
        cache_entry *buckets[1];
    };
```

缓存是作为哈希表（hash table）实现的。这个表是为速度和简单性而构建的，胜过一切，所以它有点不寻常。表的大小总是 2 的幂。表通过选择器（selector）来索引，桶索引的计算方式是取选择器的值，可能进行移位以去除无关的低位，然后与适当的掩码（mask）进行逻辑_与_操作。顺便说一下，下面是用于计算特定选择器和掩码的桶索引的宏（macro）：

```
    #ifndef __LP64__
    # define CACHE_HASH(sel, mask) (((uintptr_t)(sel)>>2) & (mask))
    #else
    # define CACHE_HASH(sel, mask) (((unsigned int)((uintptr_t)(sel)>>0)) & (mask))
    #endif
```

最后是类本身的结构体。这就是一个 `Class` 实际指向的内容：

```
    struct class_t {
        struct class_t *isa;
        struct class_t *superclass;
        struct objc_cache *cache;
        IMP *vtable;
    };
```

既然必要的结构体都有了，让我们开始实现 `GetImplementation`：

```
    IMP GetImplementation(id self, SEL _cmd)
    {
```

它做的第一件事是获取对象的类。真正的 `objc_msgSend` 使用等同于 `self->isa` 的方式来做这件事，但我会温和一点，在这部分使用官方 API：

```
        Class c = object_getClass(self);
```

因为我想访问内部结构，我会立即将其转换为指向 `class_t` 结构体的指针：

```
        struct class_t *classInternals = (struct class_t *)c;
```

现在该查找 `IMP` 了。我们把它初始化为 `NULL`。如果在缓存中找到一个条目，我们会设置它。如果在检查缓存后它仍然是 `NULL`，我们就回退到慢速路径：

```
        IMP imp = NULL;
```

接下来，获取一个指向缓存的指针：

```
        struct objc_cache *cache = classInternals->cache;
```

计算桶索引，并获取一个指向桶数组的指针：

```
        uintptr_t index = CACHE_HASH(_cmd, cache->mask);
        cache_entry **buckets = cache->buckets;
```

接下来，我们搜索具有相应选择器（selector）的缓存条目。运行时使用线性链接，所以只需要搜索后续的桶，直到找到匹配项或找到 `NULL` 条目：

```
        for(; buckets[index] != NULL; index = (index + 1) & cache->mask)
        {
            if(buckets[index]->name == _cmd)
            {
                imp = buckets[index]->imp;
                break;
            }
        }
```

如果没有找到条目，我们就回退到慢速路径并调用运行时。在真正的 `objc_msgSend` 中，上面的所有代码都是用汇编编写的，此时它会脱离汇编并调用运行时本身。一旦尝试了缓存但没有找到条目，任何快速消息发送的希望都破灭了。此时，快速运行的需求变得非常不重要，部分原因是因为它注定要变慢，部分原因是因为这条路径应该极其罕见。因此，脱离汇编代码并调用更易于维护的 C 语言是可以接受的：

```
        if(imp == NULL)
            imp = class_getMethodImplementation(c, _cmd);
```

现在已经通过这种方式或那种方式获得了 `IMP`。如果它在缓存中，就从那里检索出来，否则它就由运行时填充。`class_getMethodImplementation` 调用也会填充缓存，所以后续调用会更快。剩下唯一要做的就是返回这个 `IMP`：

```
        return imp;
    }
```

**测试**
为了确保这些东西实际有效，我编写了一个快速测试程序：

```
    @interface Test : NSObject
    - (void)none;
    - (void)param: (int)x;
    - (void)params: (int)a : (int)b : (int)c : (int)d : (int)e : (int)f : (int)g;
    - (int)retval;
    @end

    @implementation Test

    - (id)init
    {
        fprintf(stderr, "in init method, self is %p\n", self);
        return self;
    }

    - (void)none
    {
        fprintf(stderr, "in none method\n");
    }

    - (void)param: (int)x
    {
        fprintf(stderr, "got parameter %d\n", x);
    }

    - (void)params: (int)a : (int)b : (int)c : (int)d : (int)e : (int)f : (int)g
    {
        fprintf(stderr, "got params %d %d %d %d %d %d %d\n", a, b, c, d, e, f, g);
    }

    - (int)retval
    {
        fprintf(stderr, "in retval method\n");
        return 42;
    }

    @end

    int main(int argc, char **argv)
    {
        for(int i = 0; i < 20; i++)
        {
            Test *t = [[Test alloc] init];
            [t none];
            [t param: 9999];
            [t params: 1 : 2 : 3 : 4 : 5 : 6 : 7];
            fprintf(stderr, "retval gave us %d\n", [t retval]);

            NSMutableArray *a = [[NSMutableArray alloc] init];
            [a addObject: @1];
            [a addObject: @{ @"foo" : @"bar" }];
            [a addObject: @("blah")];
            a[0] = @2;
            NSLog(@"%@", a);
        }
    }
```

我还在 `GetImplementation` 中添加了一些调试日志，以确保它确实被调用了，以防我搞砸了构建并错误地调用了运行时的实现。一切正常，即使是字面量和下标语法也调用了替换后的实现。

**结论**
`objc_msgSend` 的核心相对简单。然而，它的使用方式需要使用汇编代码，这使得它比实际需要的更难理解。此外，极端的性能要求和必要的优化意味着它相当密集且棘手。但是，通过构建一个简单的汇编跳板，然后用 C 语言重新实现逻辑，我们可以看到它是如何工作的，而且它真的没有多少内容。

这应该是显而易见的，但永远不要在你的 App 中发布你自己的 `objc_msgSend`。你会搞坏东西然后后悔的。请仅将其用于教育目的。

这就是今天这篇令人神游的、充满汇编的文章的全部内容。下次再来享受更多乐趣、游戏和破解。正如我现在已经说了大约一千次，但又忍不住要提醒你的，Friday Q&A 是由读者建议驱动的。如果你有一个想让我写的主题，请[发给我](mailto:mike@mikeash.com)！

你喜欢这篇文章吗？我在卖整本整本的书！第二卷和第三卷已经出版了！它们有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html)

添加你的想法，发表评论：

垃圾邮件和偏离主题的帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
