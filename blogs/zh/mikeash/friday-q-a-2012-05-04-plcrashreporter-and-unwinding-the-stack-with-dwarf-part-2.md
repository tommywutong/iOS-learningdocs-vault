---
title: 'Friday Q&A 2012-05-04：PLCrashReporter 与使用 DWARF 展开栈，第二部分'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-05-04-plcrashreporter-and-unwinding-the-stack-with-dwarf-part-2.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:55194055ae60a5c4'
translated: true
---

> 原文：[Friday Q&A 2012-05-04: PLCrashReporter and Unwinding the Stack With DWARF, Part 2](https://www.mikeash.com/pyblog/friday-qa-2012-05-04-plcrashreporter-and-unwinding-the-stack-with-dwarf-part-2.html)　·　mikeash.com Friday Q&A

发表于 2012-05-04 18:44 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Solving Simulator Bootstrap Errors](https://www.mikeash.com/pyblog/solving-simulator-bootstrap-errors.html)  
上一篇文章：[Friday Q&A 2012-04-27: PLCrashReporter and Unwinding the Stack With DWARF](https://www.mikeash.com/pyblog/friday-qa-2012-04-27-plcrashreporter-and-unwinding-the-stack-with-dwarf.html)  
标签：[dangerous](https://www.mikeash.com/pyblog/?tag=dangerous) [debugging](https://www.mikeash.com/pyblog/?tag=debugging) [dwarf](https://www.mikeash.com/pyblog/?tag=dwarf) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [semi-evil](https://www.mikeash.com/pyblog/?tag=semi-evil)

Friday Q&A 2012-05-04：PLCrashReporter 与使用 DWARF 展开栈，第二部分

作者：[Gwynne Raskind](http://blog.darkrainfall.org/)

---

**为什么不直接用现成的那些东西？**  
我接手这个项目后做的第一件事就是寻找一个简单的解决方案。这些方案在很多情况下确实存在，却因为没有多少人知道去哪里找而最终未被使用。

我想到的第一个方案是 Apple 自己的 `libunwind` 实现。它内置于系统、始终可用，并且完全满足需求：利用所有可用信息提供栈上函数的地址。可惜。Apple 的库：

- 没有提供任何公开 API 来访问当前线程以外的任何线程的栈。
- 会调用 `dyld`（不是 async-signal safe）。
- 会调用 `dladdr`（不是 async-signal safe）。
- 会分配内存（不是 async-signal safe）。
- 在紧凑展开（compact unwinding）、DWARF 和帧指针（frame pointer）遍历全部失败时没有后备方案。
- 不执行符号化（symbolication）。
- 在 Lion 之前不能保证可用。
- 使用 APSL 许可，因此分支（fork）该库不是一个可选项。

所以，它基本对我们的目的完全没用。接下来想到的是原始的 `libunwind`，[可在此处获得](http://www.nongnu.org/libunwind)。再次可惜：

- 没有 Darwin 支持。
- 没有 Mach-O 支持。
- 没有紧凑展开编码（compact unwind encoding）支持。
- 没有后备的栈扫描器（stack scanner）。
- 源码复杂，且没有关于移植或扩展的文档。

同样基本上对我们的目的没用。

剩下的选项是创建自己的 DWARF 解析器、紧凑展开编码解析器和栈扫描器实现。我本可以把它直接集成到 PLCrashReporter 里，但考虑到开源社区中缺少栈展开库这一现状，我觉得把它写成完全独立的代码更好。于是我打开 Xcode 并创建了一个新 target，起名为 `libtinyunwind`。

**一点 API 设计**  
`libtinyunwind` 背后的理念正如其名：一个精巧的小型展开库，只做崩溃后收集回溯（backtrace）所必需的事情。（它也可以用于异常展开，但前提是我要实现相应的 C++ ABI。Apple 的 `libunwind` 已经做到了这一点。）由于我只打算解决 x86_64 上的问题，当时也没有过分担心跨平台，尽管我确实会把这件事放在心上。

在设计 API 时，我从 `PLCrashReporter` 和原始的 `libunwind` 中汲取了相当多的灵感。首先是库的公共接口。一个栈展开器必须提供：

- 跟踪加载到（以及从）活动进程中加载/卸载的二进制映像（binary image）。
- 从任意现有线程派生状态上下文（state context）。
- 对上下文中的栈帧（stack frame）逐个按顺序迭代。
- 访问每个帧中可用的任意寄存器数据。
- 最好还能符号化返回的任意函数地址。

基于 `PLCrashReporter` 的高层实现，我创建了下面这组函数。在讨论中，为简洁和可读起见，我使用简短的函数名和数据类型名，但真实的函数名和数据类型都带有 `tinyunw_` 前缀。

```
    int set_image_tracking(bool tracking_flag);
    int getcontext(context_t *context);
    int getthreadcontext(context_t *context, thread_t thread);
    int init_cursor(context_t *context, cursor_t *cursor);
    int step(cursor_t *cursor, flags_t flags);
    int get_register(cursor_t *cursor, register_t regnum, word_t *value);
    const char *register_name(register_t regnum);
    int get_symbol_info(word_t ip, word_t *start_addr, const char **name);
```

`context_t` 是 `x86_thread_state64_t` 的 `typedef`，而 `cursor_t` 是一个不透明结构体类型。`register_t` 是 x86_64 上可用寄存器的枚举，`word_t` 是 `uint64_t` 的 `typedef`。把它们做成不透明类型可以简化日后的跨平台支持。

由于使用 context 和 cursor 的代码必须是 async-signal safe 的，我不能简单地写成 `typedef cursor_struct *cursor_t;`。客户端代码必须能在自己的栈上分配 context 和 cursor，如果编译器不知道结构体的大小就无法做到这一点。解决办法是这个有点丑陋的技巧：

```
    typedef struct cursor_t {
        uint64_t opaque[120];
    } cursor_t;
```

实际上，在内部头文件中定义的真正 cursor 结构体只有 352 字节，而不是 960 字节，但额外的空间允许：1）将来扩展而不破坏二进制兼容性；2）为实际实现留出余地。在该库的预期用例中，任何时候你都只会持有一个 cursor，因此在 64 位地址空间中损失 608 字节并不是什么特别让人担心的事。这有点过头，但根据需要调整起来也不难。

公开头文件还定义了一组 UNIX 风格的错误码，供函数返回（再次强调，真实的错误码带有前缀）：

```
    enum {
        ESUCCESS            = 0,            /* no error */
        ENOFRAME            = 1,            /* no more frames to unwind */
        EUNSPEC             = -6540,        /* unknown error */
        ENOMEM              = -6541,        /* out of memory */
        EBADREG             = -6542,        /* bad register number */
        EINVALIDIP          = -6545,        /* invalid IP */
        EBADFRAME           = -6546,        /* bad frame */
        EINVAL              = -6547,        /* unsupported operation or bad value */
        ENOINFO             = -6549,        /* no unwind info available */
    };
```

这些错误码大多与 Apple 的 `libunwind.h` 头文件中的值对应，以便与熟悉该库的人更好地互操作（interoperability）。

`step()` 函数还有一组标志：

```
    enum {
        FLAG_NO_DWARF = (1 << 0),
        FLAG_NO_COMPACT = (1 << 1),
        FLAG_NO_STACKSCAN = (1 << 2),
        FLAG_TRY_FRAME_POINTER = (1 << 3),
    };
    typedef int flags_t;
```

这允许库的客户端精确控制在尝试逐帧遍历栈时使用哪些信息。这在几种情况下很有用：

- 如果某个实现中发现了 bug，可以在不移除整个库的情况下关掉那个实现。
- 如果客户端代码事先知道哪些信息可用、哪些不可用，或者只是想用准确性换取更快的执行速度（DWARF 比其他方法慢得多），它可以避免去二进制文件的调试信息里进行可能代价高昂的搜索。
- 如果客户端更关心准确性而不是尽可能多的信息，关掉栈扫描器可以消除大部分产生垃圾数据的可能性。
- 库的客户端可以为用户（很可能是一名开发者）提供只使用部分可用数据的选项，以便他们查看某个程序是否包含（或排除了）所需的信息。

下面是一个非常基本的 API 使用示例：

```
    int     main(int argc, char **argv)
    {
        /* ... */
        set_image_tracking(true);
        /* ... */
    }

    void    walk_thread_stack(thread_t thread)
    {
        context_t context;
        cursor_t cursor;
        int res = ESUCCESS, n = 0;
        word_t reg = 0, addr = 0;
        const char *name = NULL;

        getthreadcontext(&context, thread);
        init_cursor(&context, &cursor);
        while (true)
        {
            res = step(&cursor, 0);
            if (res == ESUCCESS)
            {
                if (get_register(&cursor, X86_64_RIP, &reg) != ESUCCESS)
                    break;
                if (get_symbol_info(reg, &addr, &name) != ESUCCESS)
                    break;
                printf("Frame %d has IP %p, which is in function %s, starting at address %p\n", n, reg, addr, name);
                continue;
            }
            else if (res == ENOFRAME || res == ENOINFO)
                printf("End of stack.\n");
            else
                printf("Error %d\n", res);
            break;
        }
    }
```

开头的 `set_image_tracking()` 调用至关重要；没有它，只有栈扫描器能工作，而且地址也无法被符号化。

**为什么我必须跟踪二进制映像？**  
你可能会好奇，为什么库不直接扫描进程的地址空间来找到所需信息。不幸的是，那根本不现实。库在运行时被加载到可执行文件的方式涉及大量陷阱，多到在 async-signal 时间内几乎不可能把这一切弄清楚。这意味着库必须在二进制映像被加载到进程以及从进程中卸载时在内部跟踪它们。

幸运的是，`dyld` 提供了一种简单方便（更重要的是，有文档且稳定）的方法来做到这一点：`_dyld_register_func_for_add_image` 和 `_dyld_register_func_for_remove_image`。

当一个映像（请记住，在这个上下文中，“映像”指运行时加载到进程中的任意一段可执行代码，包括可执行文件本身）被加载时，`libtinyunwind` 会立即将其解析为 Mach-O，并将其存储在一个 async-safe 的读写锁链表中（实现得益于 Landon 写的 `PLCrashReporter`，一段非常漂亮的代码！）。

你可能会问，为什么？因为这就是它找到以下信息的方式：

- 映像可执行代码的地址，也称为其 TEXT 段。所有方法都会用到。
- 映像的 `__eh_frame` 和 `__debug_frame` 段的地址。DWARF 解析器使用。
- 映像的 `__unwind_info` 段的地址。紧凑展开解析器使用。
- 映像的 `__LINKEDIT` 段和符号表。符号化使用。

所有这些信息本可以在 async-signal 时间内解析出来，但没有理由不在映像加载到进程后立即解析，而在可以安全调用普通 API 的时候做这件事有一个好处：它还可以（并且确实）调用 `dladdr()` 来获取映像在磁盘上的名称。知道有人调用了一个名为 `foo` 的函数当然很好，但它是主应用程序里的 `foo`、某个第三方库里的 `foo`，还是 CoreFoundation 里的 `foo`？（不，并不是真的有一个叫 `foo` 的函数。:)

具备了所有这些数据，`libtinyunwind` 就可以开始真正展开栈的工作了。

**让我们把它放到上下文中**  
展开栈的第一步是获取线程状态，也称为上下文（context）。简而言之，它就是你想检查的那个线程的所有 CPU 寄存器的一份快照（snapshot）。可以通过 Mach API `thread_get_state` 获取（`getthreadcontext()` 就是这么做的），或者如果你正好在所关注的线程上执行，也可以用汇编语言直接获取。纯属好玩，下面是 `getcontext()` 的实现：

```
    movq    %rax,   (%rdi)
    movq    %rbx,  8(%rdi)
    movq    %rcx, 16(%rdi)
    movq    %rdx, 24(%rdi)
    movq    %rdi, 32(%rdi)
    movq    %rsi, 40(%rdi)
    movq    %rbp, 48(%rdi)
    movq    %rsp, 56(%rdi)
    addq    $8,   56(%rdi)
    movq    %r8,  64(%rdi)
    movq    %r9,  72(%rdi)
    movq    %r10, 80(%rdi)
    movq    %r11, 88(%rdi)
    movq    %r12, 96(%rdi)
    movq    %r13,104(%rdi)
    movq    %r14,112(%rdi)
    movq    %r15,120(%rdi)
    movq    (%rsp),%rsi
    movq    %rsi,128(%rdi) # store return address as rip
    # 跳过 rflags —— 在栈状态未知时 pushq 不安全，lahf 可能不被支持
    # 跳过 cs
    # 跳过 fs
    # 跳过 gs
    xorl    %eax, %eax # return TINYUNW_ESUCCESS
    ret
```

该函数没有 prologue 或 epilogue，因为那会破坏基址寄存器和栈指针。存放信息的上下文由 `rdi`（第一个整数参数寄存器）指向。寄存器值大多直接加载到上下文中。栈指针增加 8（一个 64 位字），是为了抵消本函数 `call` 指令压入的保存返回地址。返回地址作为 `rip` 存储在上下文结构体中，是根据 `call` 的语义解引用栈指针得到的。本质上，这个函数假装自己不在栈上。标志寄存器被跳过是因为在 async-signal safe 时间没有安全的加载方式，段寄存器被跳过是因为它们在 64 位代码中没有意义。

除非你关心尽可能少地调用系统 API，否则用这个代替直接调用 `thread_get_state()` 并没有太多意义。不过在非 Mach 平台上它也很有用，因为在那里获取上下文状态可能要困难得多。

**躺下，然后展开**  
现在，你有了一个上下文，以及一个用来迭代它的 cursor。那这个迭代实际是如何工作的？

`step()` 函数使用以下逻辑：

1. cursor 的 `rip` 值是否为 `NULL`，或者落在了 `start` 或 `thread_start` 符号的预定范围内？如果是，立即返回 `ENOFRAME`；已经到达栈的顶部。

   扫描器在 `start` 和 `thread_start` 处显式停止，是因为栈扫描器尤其容易跑过线程栈的底部，而且 DWARF 和紧凑展开编码并不总能编码一种万无一失的方法来检测栈底，以便避免尝试栈扫描器。这两个符号之一保证总会出现在任意栈的底部，因此它们是安全的停止点。
2. 如果客户端没有要求跳过紧凑展开编码，尝试用它寻找栈帧。成功或出现任何错误就返回；如果不存在紧凑展开信息，继续。
3. 如果客户端没有要求不要使用 DWARF，尝试用这种方式寻找栈帧。成功或出现任何错误就返回；如果不存在 DWARF 信息，继续。
4. 如果客户端要求了帧指针扫描，尝试使用 `rbp` 作为指向下一栈帧的指针。成功就返回……嗯，你懂的。
5. 最后，如果以上全部失败，尝试从最后一个有效帧开始执行栈扫描。

我们按顺序逐一审视每种方法。

**哇，真紧凑；你能展开讲讲吗？**  
紧凑展开编码解析器先检查加载到进程中的任意映像是否包含 cursor 当前上下文中的 `rip` 值。如果不包含，它立即返回“无信息”，因为连去哪里找都不知道。搜索进程中每个映像的展开表没有意义；对误报来说这并不比栈扫描器好。如果找到的映像没有紧凑展开信息，它也返回“无信息”。

下一步是对 `rip` 值执行两级表查找，如第一部分所述。由于两级表都是升序排列的，查找代码会对函数地址执行二分搜索。展开表中的地址存储为相对于映像 Mach-O 头地址的偏移量，因此 `rip` 值首先要减去该偏移量。假设找到匹配条目，二级表就包含了该函数展开信息的编码。

紧凑展开编码有五种实际信息编码类型：

- 兼容编码。这种编码看起来是历史遗留，在 OS X 上从未使用过。Apple 的 `libunwind` 和 `libtinyunwind` 都将其解释为“无可用展开信息”。
- DWARF 编码。这表示该函数的展开信息过于复杂，无法用紧凑编码表示，应转而搜索 DWARF 数据。`libtinyunwind` 的处理方式是直接返回“无信息”，让 DWARF 解析器接下来去搜索。
- RBP 帧编码。该展开信息适用于带有帧指针的函数。从编码中读取已保存的寄存器编号，并根据线程的栈更新寄存器值。解引用当前 `rbp` 以找到新的 `rbp`，将 `rsp` 设为旧 `rbp` 加两个字（帧指针和返回地址），并将 `rip` 设为栈上的返回地址（`rbp` + 8）。
- 栈立即编码和栈间接编码。这两种编码适用于没有帧指针的函数。两种编码的寄存器处理方式相同（与 RBP 帧编码相同，但保存寄存器的编号编码不同）。在立即编码中，栈大小按一个数字计算。在间接编码中，函数必须以 `subl %rsp, $some_number_here` 指令开头，该指令会被解析以获取栈大小。`rsp` 设为旧 `rsp`，加上栈大小，减去已保存的寄存器数量，再加 8（返回地址）。`rip` 设为栈上的返回地址。

仅此而已！随着 `rsp` 和 `rip`（以及可能时还有 `rbp`）更新，继续进入下一栈帧所需的一切都已就绪。此时返回成功。

**我感觉自己被（虚拟机）搞得 DWARF 了**  
要是 DWARF 解析也这么简单就好了！可惜并不是。

DWARF 解析器开头与紧凑展开解析器的步骤相同：查找包含 `rip` 的映像。没有映像？没有 DWARF 信息？此时当场放弃。

啊，糟糕，我们找到了点什么。现在我们必须搜索调试信息段，找到与函数地址匹配的函数数据条目（Function Data Entry，FDE）（如[上周讨论的](https://www.mikeash.com/pyblog/friday-qa-2012-04-27-plcrashreporter-and-unwinding-the-stack-with-dwarf.html)）。这意味着要解析整段内容。我们从段开头开始，一次解析一个条目。算法如下：

1. 下一个条目是 FDE 还是 CIE？如果是 CIE，跳过。我们会在解析 FDE 时一并解析它们。不幸的是，这意味着每解析一个 FDE，我们就会把每个 CIE 都解析一次。这是因为我们运行在 async-signal 时间内，没有地方可以缓存找到的 CIE。
2. 是 FDE？把它以及对应的 CIE 解析出来。如果它包含我们正在寻找的函数地址，返回它；否则继续处理。

我要在这里打断一下自己，讨论一下 DWARF 数据是怎么解析的。DWARF 是一种非常有趣的数据格式；它包含多种针对不同信息的不同编码，任意时刻都可能用到其中任何一种。

比如，一个 CIE 以简单的 32 位、64 位和 8 位数字开头。然后是一个 C 字符串，描述使用它的所有 FDE 的“增补（augmentation）”。然后有几个“ULEB128”和“SLEB128”数字。“LEB128”代表“小端 Base-128（Little Endian Base-128）”，DWARF 标准称其为“一种利用大多数整数绝对值较小的假设来紧凑编码整数的方案。”尽管名字里有，但它实际上并不是小端序。

就我个人意见而言，LEB128 的存在主要是为了把事情搞得更麻烦；在处理虚拟机操作码的编码中试图在整数字节上省几个零，我觉得这不止一点点蠢。我只能假设背后有我不理解的某些想法。

无论如何，CIE 中的增补字符串必须逐字符解析，以了解相关 FDE 中数据的某些关键信息。特别地，它给出了增补数据的大小（正确解析 FDE 所必需）和 FDE 中指针值的编码（甚至仅仅为了判断某个函数偏移量到底是否包含在条目内，这部分也是必需的）。CIE 中的其他信息给出了代码和数据的对齐因子，指出虚拟 CFA 表中哪一列代表函数返回地址，并给出 DWARF 数据的实际版本。版本 1（由 GCC 或 Clang 生成的 .eh_frame 段）和版本 3（DWARF 2 标准）是相同的，也是 `libtinyunwind` 试图理解的唯二版本。

指针编码也有点意思；FDE 中的指针可以用不少于 36 种不同的方式编码（9 种数值表示形式，范围从有符号和无符号 8 位到有符号和无符号 64 位，并包括 uleb128 和 sleb128，几种用于指针“基值”的编码（其中只支持两种），以及一个用于值间接引用的标志）。

当这一切都完成之后，我们（希望）得到了一个对应于正在展开的函数的 FDE（包含 CIE）。现在必须运行 CFA 程序。这意味着设置一个虚拟机状态，先运行 CIE 中的所有指令，再运行 FDE 中的所有指令，一旦虚拟 CFA PC 超过该函数当前的 `rip` 值就立即停止。运行超过这一点的任何指令都会导致不正确的寄存器状态，因为实际执行的代码从没走到那一步！

DWARF 有压入和弹出状态指令。由于我们不能分配内存，对虚拟栈的深度施加了一个硬性大小限制。虚拟状态相当大，因此限制为 8。幸运的是，我还没见过哪怕用了一次的 DWARF 编码，所以我认为这个限制是安全的。

实际的操作码（opcode）大多是直截了当的。虚拟机会维护一个 CFA 寄存器编号、一个 CFA 寄存器偏移量、一个 CFA PC，以及一组通过数字编码的寄存器值和位置。这些数字对应的机器寄存器是架构特定的；`libtinyunwind` 通过明显的 switch-case 语句将它们映射到 x86_64 寄存器集。DWARF 有以下操作码：

- 什么都不做（nop）
- 修改 CFA PC（设为 n，增加 1/2/4/n）
- 修改寄存器的值（设为 n，设为 CFA +/- n，设为其他寄存器，设为未定义，设为表达式的结果）
- 保存和恢复 DWARF 状态（压入/弹出虚拟栈）
- 设置 CFA 寄存器（设为 n，设为 n +/- m，设为当前值 +/- m，设为表达式的结果）
- 各种 GNU 扩展和用户操作码，`libtinyunwind` 将所有此类操作码视为错误，因为它们不在 Darwin 或现代代码中使用（有一个例外：args_size 操作码会被解析但不使用）。

一旦 CFA 程序运行完毕，它会产生一个虚拟机状态，也就是在给定 `rip` 处的 DWARF CFA 表快照。现在必须把该状态应用到当前寄存器状态上。

首先，确定 CFA 寄存器的值。CFA 寄存器可以是某个特定机器寄存器的值（在应用任何更改之前）加上或减去一个偏移量，也可以是 DWARF 表达式的结果。`libtinyunwind` 目前不解析 DWARF 表达式，因为它们在现实中非常罕见，且丢失的数据会回退到栈扫描器；将来某个时候会实现。

接下来，对虚拟状态中的每个寄存器，将虚拟寄存器的值和位置应用到真实寄存器上。寄存器的位置可以是“未使用（unused）”（不改变真实寄存器）、“CFA 值 +/- 偏移量”（将真实寄存器设为 CFA 寄存器的值）、“寄存器”（将真实寄存器设为另一虚拟寄存器的当前值），或“表达式”（如上所述，尚未实现）。

最后，用 CIE 中列为返回地址寄存器的虚拟寄存器的值更新 `rip`，并将 `rsp` 更新为 CFA 寄存器的值（CFA 寄存器被定义为始终是栈指针的最终值）。

到这里，我们 *终于* 完成了。如果这 *任意一步* 期间发生错误，会立即返回，DWARF 解析器完全退出。从这一切里的任何差错中恢复根本不值得费那个劲。

**函数对 CPU 说：我被诬陷了！**  
用帧指针遍历栈是所有方法中最简单的。它只需要解引用当前 `rbp` 的值，做一个简单检查确保它指向进程栈中大致合理的位置。当然，没办法完全确定它没把你带到一个彻底错误的地方。如果你信任它，把 `rsp` 更新为旧 `rbp` 加 16，解引用旧 `rbp` + 8 来更新 `rip`，搞定。

`libtinyunwind` 的帧指针函数目前还不存在。将来要做的另一件事，就跟 DWARF 表达式求值器一样。这主要是因为对有栈帧的函数而言，帧指针尝试并不比栈扫描器好多少，而对没有栈帧的函数，它甚至更糟。

**你在这个栈里看到返回地址了吗？慢慢看。**  
栈扫描器的工作方式确实有点像警察列队辨认；它每次以指针大小的一个字为单位遍历栈，直到找到看起来像返回地址的东西，然后就用它。

关于 `libtinyunwind` 中栈扫描器的实现，没有太多可说的。它只是把上次在栈上找到看起来像返回地址的位置保存下来，下次被调用时就把那个位置用作起点。如果它在某个固定字数（代码里的值是 50）内没找到地址，就放弃。`rip` 用找到的地址更新，`rbp` 用栈上它前面的下一个字（最佳猜测）更新，就这样。

**你连函数名都没拿到就走了？**  
一旦在栈上找到了一个函数，知道它究竟是哪个函数，甚至可能知道当时进程在函数内的位置，确实很有帮助。`libtinyunwind` 通过前面提到的 `get_symbol_info` 函数提供了符号化功能。`get_symbol_info` 是目前 `libtinyunwind` 中唯一适用于 32 位进程的函数。

`get_symbol_info` 首先检查映像跟踪是否已开启，因为没有它就没有东西可以做符号化。接下来，它做所有展开方法都做的事：查找包含正被搜索的 `rip` 值的映像。如果找不到映像，或者该映像看起来没有符号表，就放弃。

接着，它搜索该映像的全局符号表和局部符号表以寻找匹配符号。符号表存储为起始地址列表。这意味着如果映像有五个符号，起始地址分别为 0x001、0x005、0x009、0x015 和 0x020，而你查询包含地址 0x014 的函数，就必须搜索表直到同时找到 0x009 和 0x015，这样才能确定下界和上界。先搜索全局表，再搜索局部表。两者都会完整搜索一遍；符号表不保证有序，确保给定结果正确的唯一方法就是确保每一个边界都检查过。

当找到匹配的符号表条目时，从条目中读取其起始地址，从映像的字符串表中读取名称。会返回一个指向名称的直接只读指针，使该函数成为 async-signal safe。

**内存安全（memory safety）**  
`libtinyunwind` 的一个特别之处在于，一个 async-signal safe 的崩溃处理器（crash handler），在已经出了足够严重的问题导致首次崩溃之后运行，可能会处理大量无效的内存地址。在这种情况下，你读出的任何内存都可能导致崩溃，而在崩溃处理器里崩溃要么让进程死锁（因为 UNIX 信号仍然被阻塞，哪怕信号处理器无法继续执行），要么直接导致进程终止。无论哪种方式，你都丢失了那么感兴趣想要收集的崩溃数据。

幸运的是，你可以用一种方式读取进程内存，在访问无效地址时只是返回错误，而不是触发又一次 `EXC_BAD_ACCESS`。这一点我也要归功于 Landon，这也是我从 `PLCrashReporter` 本身复制的又一段代码。关键是 [`vm_read_overwrite()`](http://web.mit.edu/darwin/src/modules/xnu/osfmk/man/vm_read.html) 函数。我不完全清楚它是如何工作的，当然也不理解为什么叫这个名字，但它在无效访问时读取进程内存而不导致进程崩溃，这才是重要的部分。`libtinyunwind` 到处使用它，以便在内存损坏太严重而无法处理时能够优雅地失败。

**结论**  
这差不多总结了我对栈展开的讨论。正如你在我解说过程中看到的，`libtinyunwind` 还缺失一些部分，最重要的是多架构支持，但它们不会永远缺失。我在这个项目上获得了极大的乐趣，非常感激能有机会做这件事；我打算继续下去。代码采用与 `PLCrashReporter` 本身相同的许可条款；我希望很快会有一次发布。在 Mike 接下来的文章之后，我会再带来另一篇 Friday Q&A。在此之前，祝你编程愉快！

喜欢这篇文章吗？我正在出售整本的文集！第二卷和第三卷现已上市！提供 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-05-04-plcrashreporter-and-unwinding-the-stack-with-dwarf-part-2.html)

添加你的想法，发表评论：

垃圾评论和离题内容将被删除，恕不另行通知。违规者可能由我自行公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
