---
title: 'Friday Q&A 2013-03-08：让我们构建 NSInvocation，第一部分'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2d9b330fce386d90'
translated: true
---

> 原文：[Last time on Friday Q&A](https://www.mikeash.com/pyblog/friday-qa-2013-03-08-lets-build-nsinvocation-part-i.html)　·　mikeash.com Friday Q&A

发表于 2013-03-08 14:33 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2013-03-22：让我们构建 NSInvocation，第二部分](https://www.mikeash.com/pyblog/friday-qa-2013-03-22-lets-build-nsinvocation-part-ii.html)  
上一篇：[Friday Q&A 2013-02-22：让我们构建 UITableView](https://www.mikeash.com/pyblog/friday-qa-2013-02-22-lets-build-uitableview.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [objectivec](https://www.mikeash.com/pyblog/?tag=objectivec)

Friday Q&A 2013-03-08：让我们构建 NSInvocation，第一部分

作者：[Mike Ash](https://www.mikeash.com/)

**代码**  
`MAInvocation` 的代码发布在 GitHub 上：

[https://github.com/mikeash/MAInvocation](https://github.com/mikeash/MAInvocation)

**总览**  
一个 `NSInvocation` 对象表示一次方法调用。一次方法调用有一个 target、一个选择器（selector）、一组参数和一个返回值。

只把这些值存起来未免太平淡了。随手写一个简单的模型类就能做到：给返回值一个变量，给参数一个数组，就完事了。（target 和选择器不过是第一、第二个参数。）`NSInvocation` 的有意思之处，在于它能够真正捕获并发送它所表示的调用。

`NSInvocation` 可以在某个特定对象上被_调用_（invoke）。这做的相当于 `[target message: argument]` 这样的代码，只不过 target、消息和参数全部在运行时才确定。构建 `NSInvocation` 时可以借助运行时内省，对方法本身一无所知也无妨。

更进一步，`NSInvocation` 还可以_由_一次失败的消息发送构造出来。如果你写了 `[target message: argument]`，而 `target` 其实没有实现 `message:`，那么它会收到一次 `forwardInvocation:` 调用，其中传入一个表示这次调用的 `NSInvocation *`。接下来它想拿这个 invocation 对象做什么都可以：把它调用到别的对象上、摆弄参数，或者设一个任意返回值传回给调用方。

所以 `NSInvocation` 包含两块互补的难事：

1. 一段代码，能拿一组参数去发起方法调用，并收集返回值。
2. 一段代码，能接住一次方法调用，收集参数，再向调用方返回一个任意返回值。

这两块都要求在实现中写入大量关于 CPU 架构调用约定（calling convention）的知识，还需要汇编语言胶水代码（assembly glue）。

**调用约定**  
既然需要如此多架构相关的代码，我决定只聚焦一个架构。对我们这些 Mac 用户来说，`x86-64` 是最方便的选择。为了进一步简化，我决定不支持浮点参数和浮点返回值，也放弃了 `struct` 参数，不过 `struct` 返回值的支持我还是实现了。下面的讨论会略过这些我没实现的部分。

要实现哪怕这个缩水版的 `MAInvocation`，也必须理解 `x86-64` 函数调用约定的相关部分；而要理解调用约定，你首先得对 `x86-64` 架构本身有点概念。

`x86-64` 架构是 Intel 32 位 `x86` 架构的 64 位扩展，后者随 386 CPU 问世。它又是 Intel 8086 的 16 位架构的扩展，而 8086 又深深植根于 Intel 8080 的 8 位架构——8080 通常被认为是第一颗值得围绕它造一台计算机的微处理器。它能寻址多达 64kB 的内存，也就刚够放下如今一个中等尺寸的 App 图标。

通用寄存器有十六个：`rax`、`rbx`、`rcx`、`rdx`、`rbp`、`rsp`、`rsi`、`rdi`、`r8`、`r9`、`r10`、`r11`、`r12`、`r13`、`r14` 和 `r15`。前一半继承自 Intel 的 32 位架构，后一半是 `x86-64` 新增的。每个寄存器 64 位。

在这些调用约定面前，指针和整数被一视同仁：都只是 64 位的量。更小的整数会被扩展到 64 位。

调用函数时，前六个参数按顺序填入这些寄存器：`rdi`、`rsi`、`rdx`、`rcx`、`r8` 和 `r9`。多余的参数（如果有）作为 64 位的量从栈上传递，因此后续参数可以在内存中的 `rsp`、`rsp + 8`、`rsp + 16` 等处找到。

如果函数有返回值，就把它放进 `rax` 返回。如果函数返回两个值——比如返回像 `NSRange` 这种包含两个值的 `struct`——第二个值用 `rdx`。如果函数返回更大的 `struct`，处理办法是让调用方分配足够的内存，然后一个指向那块内存的指针作为隐式的第一个参数传入 `rdi`，所有显式参数相应后移一位。

注意，对 Objective-C 方法而言，前两个参数是 `self` 和 `_cmd`，因此它们走 `rdi` 和 `rsi`（若方法返回更大的 `struct`，则走 `rsi` 和 `rdx`）。显式参数（如果有）排在这两个之后。

据我所知，用于传参的寄存器数量、以及用的是哪几个，并没有什么特别的根本原因。调用约定本质上是几者之间的权衡：给调用方添负担、给被调用方添负担、让参数传递更高效、让周边代码更高效。这套约定想必落在各种相互冲突的诉求之间某个合理的折衷点上。

要发起函数调用，`MAInvocation` 需要拿到函数的参数，把前六个放进相应寄存器，把其余的放上栈，然后真正跳转到函数地址。返回之后，它要把两个返回值寄存器里的值记录下来。

要接住一次函数调用，`MAInvocation` 需要记录六个传参寄存器的值以及栈指针的位置，并据此提取参数值。返回之前，它要把期望的返回值放进两个返回值寄存器。"哪个值进寄存器、哪个进栈"的逻辑可以用 Objective-C 写，但真正操作寄存器和栈的代码必须用汇编写。

**数据结构**  
为了让 Objective-C 代码与汇编代码干净地互通，我定义了一个 `struct`，装下所有相关内容。发起调用时，`MAInvocation` 按需填好这个 `struct`，然后调用汇编语言胶水代码。接住调用时，汇编胶水根据当前状态构造出这个 `struct`，再交给 Objective-C 代码。并非所有字段在两种情形下都有用，但所有情形共用同一个 `struct`，总比为每种情形做特化要容易。

这个 `struct` 的第一个成员是要调用的函数地址：

```
    struct RawArguments
    {
        void *fptr;
```

接着是六个 64 位传参寄存器的值：

```
        uint64_t rdi;
        uint64_t rsi;
        uint64_t rdx;
        uint64_t rcx;
        uint64_t r8;
        uint64_t r9;
```

然后是栈上传入的参数的地址，以及栈参数有多少个：

```
        uint64_t stackArgsCount;
        uint64_t *stackArgs;
```

再往后是两个返回值寄存器：

```
        uint64_t rax_ret;
        uint64_t rdx_ret;
```

`rdx` 在传参区已经存在，但为返回值单开一个条目，总比复用那个字段容易。

最后是一个标志位，记录这次调用是否使用 `struct` 返回约定，即 `rdi` 是否被用来存放为返回值分配的空间的指针。用 Objective-C 运行时的术语说，这类调用叫做 `stret`，是 "`struct` return" 的缩写：

```
        uint64_t isStretCall;
    };
```

"struct return" 这个说法其实有点名不副实，因为小的 `struct` 是走寄存器返回的，但事情就是这么叫的。看到 "struct return" 或 "stret" 时，请理解成"足够大的 `struct` 的返回"。

**函数调用胶水**  
函数调用胶水是一个 C 签名如下的函数：

```
    void MAInvocationCall(struct RawArguments *);
```

它用汇编实现，但有了上面这个原型，Objective-C 代码就能像调用 C 函数一样调用它。传入一个填好的 `struct RawArguments`，汇编胶水就会完成调用。

汇编代码先声明符号。它被标记为 global，这样程序的其他部分才能访问它。前导下划线源于一段与 Fortran 有关的古老历史——每个 C 符号都会隐式得到一个；一个希望被 C 代码访问的非 C 符号也需要带上它：

```
    .globl _MAInvocationCall
    _MAInvocationCall:
```

任何规矩的 `x86-64` 函数做的第一件事，都是保存旧的帧指针（存在 `rbp` 里），并把栈指针拷贝过去建立新的帧指针：

```
    pushq %rbp
    movq %rsp, %rbp
```

接下来的代码会用到 `r12` 到 `r15`。按照平台调用约定，这些寄存器属于 callee-saved，意味着我们不许随便摧毁它们的内容。所以先把它们的值压栈保存，供以后恢复：

```
    pushq %r12
    pushq %r13
    pushq %r14
    pushq %r15
```

`struct RawArguments *` 参数存放在 `rdi`。它是本函数的第一个参数，而调用约定规定第一个参数经 `rdi` 传入。但被调用函数的第一个参数也要用 `rdi`，所以我们把当前值存进 `r12`。`struct RawArguments` 参数的各个成员，之后都可以从 `r12` 加不同偏移来访问：

```
    mov %rdi, %r12
```

现在可以开始把参数拷贝到该去的地方了。因为这需要操纵栈指针，代码先把栈指针拷进 `r15`，方便以后恢复：

```
    mov %rsp, %r15
```

栈参数最先拷贝——没什么特别的理由，只是这样写起来稍微容易些：拷贝它们时可以拿传参寄存器当草稿寄存器用，反正里面没有要紧东西。第一步是加载栈参数的数量，它位于 `struct Rawarguments` 中偏移 `56` 处：

```
    movq 56(%r12), %r10
```

如果你好奇 `56` 哪来的：这个 `struct` 的每个成员占 `8` 字节，栈参数数量是第 8 个成员，也就是说它排在 `7` 个成员之后。`7 * 8 = 56`。这段代码里的所有偏移都是这么算出来的。

`r10` 现在装着待拷贝的栈参数数量。接着计算这些参数需要的栈空间大小，等于参数数量乘以 8（每个参数 64 位，即 8 字节）。做法是把参数数量拷进 `r11`，再左移三位，等价于乘以 8：

```
    movq %r10, %r11
    shlq $3, %r11
```

然后从 `struct RawArguments` 的偏移 `64` 处把栈参数指针加载进 `r13`：

```
    movq 64(%r12), %r13
```

借这个机会盘点一下此刻各临时寄存器里装着什么：

- `r10`：待拷贝的栈参数数量。
- `r11`：栈参数所需的字节数。
- `r13`：栈参数指针。

在汇编里我们没法给东西起方便的名字，所以任何时刻都务必仔细盯住"哪个寄存器装着什么"。

下一步是把栈指针下移，给参数腾出空间，做法是从栈指针里减去 `r11`：

```
    subq %r11, %rsp
```

调用函数之前栈还必须 16 字节对齐，做法就是和一个低四位清零的值做一次逻辑与：

```
    andq $-0x10, %rsp
```

万事俱备。此时只需执行一个简单的内存拷贝循环。等价的 C 代码是：

```
    for(int i = 0; i != r10; i++)
        rsp[i] = r13[i];
```

`r14` 充当循环计数器。第一步把它初始化为零：

```
    movq $0, %r14
```

循环顶部需要一个标号，让后面的代码能方便地跳回来：

```
    stackargs_loop:
```

接下来是 `r14 != r10` 的判断：

```
    cmpq %r14, %r10
    je done
```

`cmp` 指令比较两个寄存器，并相应地设置 `FLAGS` 寄存器的内容。若 `FLAGS` 表明两者相等，`je` 指令就跳到 `done` 标号。这种两段式结构有点怪，但 `x86-64` 就是这么工作的。

两者不相等就继续循环。下一步是拷贝当前参数，分两步走：先把参数从 `r13` 所指的内存拷进一个临时寄存器（这里是 `rdi`），再把它从 `rdi` 拷到 `rsp` 所指的内存：

```
    movq 0(%r13, %r14, 8), %rdi
    movq %rdi, 0(%rsp, %r14, 8)
```

括号表达式有点吓人。`x86-64` 允许内存引用由多个不同部分组成，这让这种"计算式数组解引用"好写很多。表达式的一般形式是：

```
    offset(%r1, %r2, elementSize)
```

它指的是这个地址：

```
    r1 + r2 * elementSize + offset
```

可以把它想成一次数组解引用：`r1` 是数组指针，`r2` 是索引，`elementSize` 是数组每个元素的大小，`offset` 只是对整个结果做的最后修正。简言之，`0(%r13, %r14, 8)` 等价于 `((uint64_t *)r13)[r14]`。

之后是 `i++`，汇编里有简单的等价物：

```
    inc %r14
```

最后，跳回 `stackargs_loop` 补完循环；它后面跟着 `done` 标号，循环退出后执行就从那里继续：

```
    jmp stackargs_loop

    done:
```

栈参数这就绪了。剩下的只是把寄存器参数拷进真正的寄存器，用一串 move 指令完成：

```
    movq 8(%r12), %rdi
    movq 16(%r12), %rsi
    movq 24(%r12), %rdx
    movq 32(%r12), %rcx
    movq 40(%r12), %r8
    movq 48(%r12), %r9
```

一切就绪，该调用目标函数了。函数指针恰好就放在 `r12` 所指的位置上，因为它是 `struct RawArguments` 的第一个成员。这条指令发起调用：

```
    callq *(%r12)
```

调用返回后，返回值（如果有）就在 `rax` 和 `rdx` 里。代码立刻把这两个寄存器的内容拷进 `struct RawArguments`：

```
    movq %rax, 72(%r12)
    movq %rdx, 80(%r12)
```

眼看就完了。除了返回，唯一还要做的，是把 `r12`-`r15` 里保存的值恢复成调用方原先的样子。第一步，把栈指针恢复到这几个寄存器刚压完栈时的状态：

```
    mov %r15, %rsp
```

然后按与压栈相反的顺序把它们弹出：

```
    popq %r15
    popq %r14
    popq %r13
    popq %r12
```

最后，用一组神奇搭配的指令把栈指针和帧指针重新调整好，再跳回调用方的地址，控制权交还调用方：

```
    leave
    ret
```

函数调用的胶水代码到此完工。Objective-C 代码现在可以按要发起的调用填好一个 `struct RawArguments`，然后调用 `MAInvocationCall` 并传入指向该 `struct` 的指针，调用就完成了。

**转发胶水**  
在 Objective-C 里，捕获一次方法调用叫做"转发"（forwarding）。运行时有一个特殊的转发处理器，每当某个选择器找不到实现时就会被调用。实际上转发处理器有两个：一个服务普通调用，一个服务 `stret` 调用。转发处理器需要知道去哪里找 `self` 和 `_cmd` 参数，而这两个参数的位置在 `stret` 调用中会变化，所以需要一点点特化。

这里的策略是设两个入口，各自先记下这是不是一次 `stret` 调用，然后都跳到同一个公共实现。公共实现据此填好一个新的 `struct RawArguments`，调用进一个 Objective-C 函数；该函数返回后，再把返回值拷回返回值寄存器，然后返回。

函数被调用时 `r10` 寄存器里没有什么特别内容，而且它也不要求保存。这使它成为临时存放 `stret` 标志的好地方。普通转发处理器跳到公共实现前把它设为 `0`，`stret` 处理器把它设为 `1`。普通处理器的完整代码是：

```
    .globl _MAInvocationForward
    _MAInvocationForward:
    movq $0, %r10
    jmp _MAInvocationForwardCommon
```

`stret` 处理器几乎一样：

```
    .globl _MAInvocationForwardStret
    _MAInvocationForwardStret:
    movq $1, %r10
    jmp _MAInvocationForwardCommon
```

有趣的部分全在公共处理器里：

```
    .globl _MAInvocationForwardCommon
    _MAInvocationForwardCommon:
```

它做的第一件事，是计算传入函数的栈参数的位置。从被调用方的视角看，栈参数从 `rsp + 8` 开始。调用方发出的 `call` 指令把返回地址压上了栈，所以从那一侧看栈参数正好从 `rsp` 开始，但在这里不是。`r11` 是另一个方便的寄存器——既没有有用内容、也不需要保存——代码就在这个寄存器里算出地址：

```
    movq %rsp, %r11
    addq $8, %r11
```

然后函数执行建立帧指针的标准序言：

```
    pushq %rbp
    movq %rsp, %rbp
```

现在终于到了构造 `struct RawArguments` 的时候。做法是把值逐一压栈。先快速盘点一下此刻各寄存器里有什么：

- `r10`：`isStretCall` 标志。
- `r11`：指向栈参数的指针。
- `rdi-r9`：寄存器参数。

处理器用 `pushq` 指令在栈上构建这个 `struct`。因为是往栈上压，所有内容必须逆序压入。`isStretCall` 是 `struct` 的最后一员，所以第一个压它：

```
    pushq %r10
```

返回值寄存器不需要装什么特定内容，所以压两次零给它们腾位：

```
    pushq $0
    pushq $0
```

接下来是 `stackArgs` 指针，它的值此刻在 `r11` 里：

```
    pushq %r11
```

再往后是栈参数的数量。这个数目前还不知道，所以处理器只压一个零占位。这个字段稍后由 Objective-C 代码填写：

```
    pushq $0
```

接下来是参数寄存器，逆序压入：

```
    pushq %r9
    pushq %r8
    pushq %rcx
    pushq %rdx
    pushq %rsi
    pushq %rdi
```

`struct` 的第一个成员是函数指针。这里用不到它，所以再压一个零占位：

```
    pushq $0
```

此时，`rsp` 已经指向新建好的 `struct RawArguments`。目标是调用一个原型如下的 C 函数：

```
    void MAInvocationForwardC(struct RawArguments *r);
```

指向 `struct` 的指针是它唯一的参数，所以要把这个地址移到 `rdi`——第一个参数从这里传：

```
    movq %rsp, %rdi
```

处理器之后还要查阅这个 `struct` 来提取返回值寄存器。由于 `rdi` 在函数调用前后不保存，`rsp` 又可能在对齐栈时被改动，处理器还把这个地址拷进 `r12`，供之后使用：

```
    movq %rdi, %r12
```

现在该对齐栈、调用进 Objective-C 了：

```
    andq $-0x10, %rsp
    callq _MAInvocationForwardC
```

Objective-C 代码接下来会构建一个 `MAInvocation` 实例，并调用对象的 `forwardInvocation:` 方法。

控制权返回后，返回值（如果有）就在这个 `struct` 里。为了让调用方看得见，把值从 `struct` 拷进相应的寄存器：

```
    movq 72(%r12), %rax
    movq 80(%r12), %rdx
```

完事！返回调用方：

```
    leave
    ret
```

Objective-C 运行时的转发处理器居然是可配置的。要把它们设成这段代码，你只需在合适的地方调用：

```
    objc_setForwardHandler(MAInvocationForward, MAInvocationForwardStret);
```

此后，运行时会对所有未实现的选择器使用这两个转发处理器。

**结语**  
汇编语言胶水代码与调用约定的基础知识到此收尾。剩下的工作还有很多，但这里的两个胶水函数打下了必要的地基，`MAInvocation` 的 Objective-C 部分将盖在其上。`MAInvocation` 需要管理一个 `struct RawArguments`，并在该 `struct` 的内容与 API 客户端提供、请求的参数和返回值之间做转换。发起方法调用时，它要把 `struct` 布置妥当，再调进上面的胶水代码；接住方法调用时，它要从 `struct` 的内容构建出一个新的 `MAInvocation`。

这些下次再讲。在那之前，请[把你的点子发给我](mailto:mike@mikeash.com)，供 Friday Q&A 选题。下一期的主题可能已经有主了，但你对将来主题的建议永远欢迎。

喜欢这篇文章吗？我还在销售整本整本的文章合集！第二卷和第三卷已经出版，提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解详情](https://www.mikeash.com/book.html)。

---

暂无评论。

发表你的想法，发一条评论：

垃圾内容和离题帖子将被无通知删除。发帖者可能会按我的个人判断被公开羞辱。

代码语法高亮由 [Pygments](http://pygments.org/) 提供。
