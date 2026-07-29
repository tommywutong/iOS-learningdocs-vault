---
title: 'dyld：OS X 上的动态链接'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-11-09-dyld-dynamic-linking-on-os-x.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d9d749e975dabfe6'
translated: true
---

> 原文：[dyld: Dynamic Linking On OS X](https://www.mikeash.com/pyblog/friday-qa-2012-11-09-dyld-dynamic-linking-on-os-x.html)　·　mikeash.com Friday Q&A

发布于 2012-11-09 15:51 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py) ([全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇：[Friday Q&A 2012-11-16: Let's Build objc_msgSend](https://www.mikeash.com/pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html)  
上一篇：[Friday Q&A 2012-11-02: Building the FFT](https://www.mikeash.com/pyblog/friday-qa-2012-11-02-building-the-fft.html)  
标签：[assembly](https://www.mikeash.com/pyblog/?tag=assembly) [dyld](https://www.mikeash.com/pyblog/?tag=dyld) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [link](https://www.mikeash.com/pyblog/?tag=link) [linking](https://www.mikeash.com/pyblog/?tag=linking) [macho](https://www.mikeash.com/pyblog/?tag=macho)

Friday Q&A 2012-11-09: dyld：OS X 上的动态链接

作者：[Gwynne Raskind](http://blog.darkrainfall.org/)

---

****警告****  
_由于 `dyld` 工作方式的具体细节相当复杂且频繁变更，同时我自己也尚未完全了解所有细节，本文对其的大多数考察都经过了简化，有些地方甚至只是概念性的。如果你对具体实现细节感兴趣，我强烈推荐 `dyld` 的源代码，它公开在 [http://opensource.apple.com](http://opensource.apple.com)。_

**静态链接**  
那么，我们从静态链接说起吧，它通常简称为“链接”。这一步通常发生在编译之后，编译器从你的源代码生成的目标文件中的机器语言被“链接”在一起，形成一个单一的二进制文件。

为什么静态链接对动态链接很重要？因为静态链接器 `ld`（以及 `ld64`）负责将源代码中的符号引用转换为间接符号查找，供 `dyld` 稍后使用。这是一个非常简单的例子：

```
    // 这是 OS X 上 main() 的实际完整声明。"apple"
    //  参数是可执行文件的路径，即 _NSGetProgname()。
    int main(int argc, char **argv, char **envp, char **apple)
    {
        puts("Hello, world!\n");
        return 0;
    }
```

由 `clang -S test.c -o test.s -Os` 生成，并剥离了部分调试信息的（优化后的）汇编代码如下：

```
            .section        __TEXT,__text,regular,pure_instructions
            .globl  _main
    _main:                                  ## @main
            pushq   %rbp
            movq    %rsp, %rbp
            leaq    L_str(%rip), %rdi
            callq   _puts
            xorl    %eax, %eax
            popq    %rbp
            ret
            .section        __TEXT,__cstring,cstring_literals
    L_str:                                  ## @str
            .asciz  "Hello, world!"
```

看起来相当直接。让我们将其编译为目标文件并导出完全编译后的版本（`clang -c test.c -o test.o -Os`, `otool -tv test.o`）：

```
    _main:
    0000000000000000        pushq   %rbp
    0000000000000001        movq    %rsp,%rbp
    0000000000000004        leaq    0x00000000(%rip),%rdi
    000000000000000b        callq   0x00000010
    0000000000000010        xorl    %eax,%eax
    0000000000000012        popq    %rbp
    0000000000000013        ret
```

哎呀，我们的符号名不见了！编译器用一组零字节替换了它们。对于 `leaq` 指令，结果是从 `rip` 的当前值加载。`callq` 指令是一个“有符号偏移量”跳转，这意味着偏移量为 0 会调用紧接在代码中的下一条指令（本例中地址为 `0x10`）。别担心，编译器已经生成了重定位条目，告诉链接器在哪里更新所有这些零（`otool -r test.o`）：

```
    Relocation information (__TEXT,__text) 2 entries
    address  pcrel length extern type    scattered symbolnum/value
    0000000c 1     2      1      2       0         4
    00000007 1     2      1      1       0         0
```

第一个条目说：“在 `__TEXT,__text` 段偏移量 `0xc` 处，有一个未分散的、外部的、PC 相对的 `X86_64_RELOC_BRANCH` 引用，长度为 '长字'，指向符号表中索引为 4 的符号。”查看一下符号表（`nm -ap`）得到：

```
    0000000000000014 s L_str
    0000000000000048 s EH_frame0
    0000000000000000 T _main
    0000000000000060 S _main.eh
                     U _puts
```

索引为 4（第五个条目）的符号是 `_puts`。类似地，索引为 0 的符号是 `L_str`，它将在目标文件中偏移量 `0x7` 处被重定位（`leaq` 指令的三个字节处）。最后，让我们看看将此目标文件链接成可执行文件的结果（`clang test.c -o test -Os`, `otool -tv test`）：

```
    _main:
    0000000100000f36        pushq   %rbp
    0000000100000f37        movq    %rsp,%rbp
    0000000100000f3a        leaq    0x00000029(%rip),%rdi
    0000000100000f41        callq   0x100000f4a
    0000000100000f46        xorl    %eax,%eax
    0000000100000f48        popq    %rbp
    0000000100000f49        ret
```

`ld` 已经：

1. 将 `__TEXT` 段定位于 `x86_64` 的标准可执行加载地址 `0x0000000100000000`，并将 `__TEXT,__text` 段定位于其后的 `0xf36` 处。`__TEXT` 的前 `0xf35`（实际上是 `0xa0f`，因为更大的偏移量未计入文件的 Mach-O 头部）个字节被清零。这使 `__TEXT` 段与 `__DATA` 段紧密对齐。我不完全知道为什么这样做，但我推测这与缓存效率有关。
2. 将 `0` 替换为从 `leaq` 指令到 `L_str` 符号的实际偏移量，本例中为 `0x29`。得到的地址是 `0x100000f61`，查看加载命令（`otool -l test`）告诉我们这正好是 `__TEXT,__cstring` 段的起始位置。
3. 将 `0` 替换为 `puts()` 的符号桩（symbol stub）的地址，它紧跟在 `main` 之后。再次查看加载命令，将其定位在 `__TEXT,__stubs` 段，我们稍后将详细讨论这个段。

因此，静态链接合并目标文件，解析对外部库的符号引用，应用这些符号的重定位，并构建一个完整的可执行文件。显然，这是一个巨大的简化，并且仅适用于可执行文件。动态库的链接过程类似但不完全相同，为简洁起见，此处不再赘述。

**`dyld` 究竟是做什么的？**  
总的来说，`dyld` 实际上负责相当多的工作。它（大致按此顺序）：

1. 基于内核为进程设置的非常简单的原始栈进行自举。
2. 递归且缓存式地，将所有可执行文件所依赖的动态库加载到进程的内存空间中，包括根据需要检索环境中的搜索路径以及可执行文件的“runpath”。
3. 通过立即绑定非延迟符号并为延迟绑定设置必要的表，将这些库链接到可执行文件中。
4. 运行可执行文件的静态初始化器。
5. 设置可执行文件 `main` 函数的参数并调用它。
6. 在进程执行期间，处理对延迟绑定的符号桩的调用（通过绑定符号），提供运行时动态加载服务（通过 `dl*()` API），并为 `gdb` 和其他调试器提供挂钩以获取关键信息。
7. 在 `main` 返回后运行静态终止器例程。
8. 在某些场景下，在 `main` 返回后，调用 `libSystem` 的 `_exit` 例程。

我将大致按顺序检查每个步骤。

**自举**  
`dyld` 是新进程中运行的第一个代码。具体来说，调用了一个名为 `__dyld_start`（名字相当形象）的符号。这是由于内核中的一些魔法，它注意到主可执行文件中的 `LC_LOAD_DYLINKER` 加载命令，并将给定的动态链接器的入口符号用作进程的初始指令指针。`__dyld_start` 执行以下伪代码（实际实现是一段紧凑的汇编代码）：

```
    noreturn __dyld_start(stack mach_header *exec_mh, stack int argc, stack char **argv, stack char **envp, stack char **apple, stack char **STRINGS)
    {
        stack push 0 // debugger end of frames marker
        stack align 16 // SSE align stack
        uint64_t slide = __dyld_start - __dyld_start_static;
        void *glue = NULL;
        void *entry = dyldbootstrap::start(exec_mh, argc, argv, slide, ___dso_handle, &glue);
        if (glue)
            push glue // pretend the return address is a glue routine in dyld
        else
            stack restore // undo stack stuff we did before
        goto *entry(argc, argv, envp, apple); // never returns
    }
```

回过头来看，我不确定这个伪代码是否比汇编更容易理解，但让我们快速过一遍：

1. 将 0 压入栈，并将栈对齐到 SSE 要求。
2. 通过将地址始终相同的符号的地址从 `__dyld_start` 的当前地址中减去，来计算 dyld 自身的滑动量（slide）。
3. 运行 `dyld` 的实际自举例程，该例程为 `dyld` 自身设置一些最小状态（例如，在不实际链接的情况下从 `libSystem` 引入某些函数，并设置 Mach 消息传递），然后运行 `dyld` 的真正 `main` 例程，该例程执行加载、链接和初始化器。
4. 如果 `dyld` 检测到主可执行文件使用 `LC_MAIN` 加载命令来设置其入口点，则返回一个胶水例程的地址，该例程负责在进程结束时调用 `_exit`。该地址被压入栈，欺骗入口点使其认为这是例程的返回地址；该函数末尾的 `ret` 指令将跳转到该胶水代码。
5. 另一方面，如果 `dyld` 检测到可执行文件使用较旧的 `LC_UNIXTHREAD` 加载命令，它只需将栈恢复到其原始状态并跳转到该入口点，入口点将是来自 crt1.o（C 运行时）的 `start` 例程。C 运行时基本上重做了 `__dyld_start` 刚刚完成的所有工作，减去实际的 `dyld` 启动部分，这就是它被 `LC_MAIN` 命令取代的原因之一。
6. 跳转到入口点。

**加载**  
每次 `dyld` 必须加载一个动态库时，无论是在应用程序启动时还是由于运行时的请求，它都必须找到磁盘上正确的二进制文件，将文件映射到内存，解析 Mach-O 头部，并记录它为链接（在此上下文中意味着符号绑定）而生成的所有数据。（天哪，“链接”这个词有多少不同的用途啊，不是吗？）

在磁盘上找到正确的二进制文件_通常_相当简单。`LC_LOAD_DYLIB` 命令会提供一个绝对路径，二进制文件就从该路径加载。当然，有时该路径包含一个特殊标记，告诉 `dyld` 到别处查找：

- `@executable_path` - 直到 OS X 10.3，这是 `dyld` 支持的唯一标记，其效用相当有限。`dyld` 会用主可执行文件的完整路径替换此标记。
- `@loader_path` - 在 10.4 中添加，此标记被替换为加载当前正在被加载的二进制文件的二进制文件的完整路径。这并不总是主可执行文件，它主要使框架能够在不求助于“伞状框架”（umbrella framework）机制的情况下嵌入自身框架，Apple 从未完全公开该机制并积极劝阻使用。
- `@rpath` - 当这个标记在 10.5 中添加时，引起了极大的欢呼。此标记依次替换为嵌入在加载二进制文件（递归）中的每个“运行路径”，使得框架和动态库最终可以只构建一次，并用于系统范围的安装和嵌入，而无需更改其安装名称，并允许应用程序为给定的库提供替代位置，甚至覆盖为深度嵌入的库指定的位置。

还有一些默认搜索路径，并且在某些情况下，可以在环境和加载命令中指定更多路径。

**链接**  
一旦动态库被加载到进程中（暂且忽略与地址空间随机化相关的一些操作，也不考虑代码签名问题），其非延迟符号就必须被绑定。

此时，我应该花点时间解释延迟符号和非延迟符号之间的区别。这并不复杂；延迟符号的绑定被推迟到符号被可执行文件第一次调用时，而非延迟符号在其所属的库被加载时立即绑定。实际的绑定过程是相同的；唯一的区别在于该过程是如何触发的。

从概念上讲，绑定一个符号很简单。在实践中，它相当有趣：

1. 在可执行文件的 `__LINKEDIT` 段的绑定信息中，查找该符号的符号桩的地址。以我们上面的例子为例，`_puts` 的桩位于 `0xf4a`（加上一些偏移，为简单起见我缩短了！）。如果我们反汇编该地址处的机器代码，会得到：

  ```
      Contents of (__TEXT,__stubs) section
      0000000100000f4a        jmp     *0x000000c0(%rip)
      Contents of (__TEXT,__stub_helper) section
      0000000100000f50        leaq    0x000000b1(%rip),%r11
      0000000100000f57        pushq   %r11
      0000000100000f59        jmp     *0x000000a1(%rip)
      0000000100000f5f        nop
      0000000100000f60        pushq   $0x00000000
      0000000100000f65        jmp     0x100000f50
  ```

  哇，一个漂亮的简单跳转指令！不幸的是，它并不是_那么_简单，只需将跳转的目标替换为符号的地址，因为跳转只能使用有符号的 32 位偏移量，而符号可能（而且应该！）位于 64 位地址空间的任何位置。所以，下一步是...
2. 同样，在绑定信息中，查找 `__DATA,__nl_symbol_ptr` 段中 `puts` 的符号指针的地址。如果是延迟符号，则在 `__DATA,__la_symbol_ptr` 段中查找。在我们的示例可执行文件中，这些段看起来像这样（使用 `otool` 输出的混合形式）：

  ```
      Contents of (__DATA,__nl_symbol_ptr) section
      0000000100001000        dq      0x0000000000000000
      0000000100001008        dq      0x0000000000000000
      Contents of (__DATA,__la_symbol_ptr) section
      0000000100001010        dq      0x0000000100000f60
  ```

  简而言之，非延迟符号指针只是零字节，而延迟符号指针直接指向桩辅助段！
3. 将相应 `__DATA` 段中符号指针的地址更新为已加载库中符号的真实地址。完毕！

你可能会问，所有这些疯狂的间接引用和所有这些额外的段到底是干什么用的？

嗯，对于非延迟符号，间接引用是必要的，原因有两个。首先，你不能将可变数据放在 `__TEXT` 段中，该段是可执行代码。这意味着你不能在运行时直接更新跳转指令，即使你有一条接受绝对 64 位地址的跳转指令。其次，你不能将可执行代码放在 `__DATA` 段中，该段是可写数据！所以你也无法在那里直接放置一条 64 位跳转指令。因此，跳转指令被编码为采用额外的间接引用级别，就像在 C 语言中解引用指针一样。

所有这些对于延迟绑定的符号也同样适用，但有一些注意事项。`dyld` 并_不_立即绑定这样的符号，而是保持原样。由静态链接器保存在延迟符号指针中的地址不是简单的 0，而是指向“桩辅助”（stub helper）。桩辅助是嵌入在 `__TEXT,__stub_helper` 段中的一点代码（真的吗？谁能想到呢？），它将延迟符号指针表中的偏移量压入栈，并跳转到 `dyld` 内部符号绑定器的（不是延迟绑定的！）符号。在这个非常简单的例子中看不到，但桩辅助会为每个延迟符号增加两条指令，以便将正确的偏移量传递给 `dyld`。当延迟绑定完成后，符号指针照常更新，并且该符号的桩辅助永远不会再被调用。

**静态初始化器、静态终止器和运行时服务**  
此时，大多数有趣的事情已经发生了。`dyld` 会运行可执行文件中的任何静态初始化器（最常见的是全局 C++ 对象的构造函数和 Objective-C 类的 `+load` 方法，尽管也有用于纯 C 的 `__attribute__((constructor))` 函数）。初始化器列表存储在二进制文件中一个单独的 `__DATA,__mod_init_func` 段中，它只是指向 `__TEXT,__text` 段的一组地址，`dyld` 按出现顺序调用它们。初始化函数接收与 `main` 相同的参数。

当进程退出时，`dyld` 也会运行静态终止器，这主要指 C++ 对象的静态析构函数和 `__attribute__((destructor))` 函数。它们的处理方式与静态初始化器类似，只是它们存储在 `__DATA,__mod_term_func` 中并且不带参数。静态终止器在与 `atexit()` 函数相同的上下文中运行。

最后，`dyld` 为其已加载的二进制文件提供运行时服务。`dl*()` API 是访问 `dyld` 服务的首选接口（并且自 10.5 起，是唯一获认可的接口；旧函数已被废弃）：

- `dlopen` - 执行加载动态库的加载阶段，可以选择部分或完全执行绑定阶段。
- `dlsym` - 在动态库（或整个进程）中查找符号。最简单地说，这无非是一个“名称到地址”的查找。
- `dladdr` - `dlsym` 的反向操作，将地址转换为一组符号信息。
- `dlclose` - 如果动态库没有其他句柄在使用，则从进程中卸载它。卸载会使该动态库提供的所有符号失效，这可能是一个相当敏感的操作，尤其是在 Objective-C 环境中。

**缺失的内容**  
虽然我已经讲了很多，但我在本文中也遗漏了_大量_信息：

- 两级命名空间（Two-level namespaces），防止动态库中出现简单的符号冲突
- `dyld` 共享缓存（shared cache），维护系统范围内已加载动态库的映射，以实现快速绑定
- 重定基址（Rebasing）
- 代码签名（Code signing）
- 动态库链接
- `dyld` 庞大的环境变量集
- “受限”二进制文件（特别是 `setuid` 二进制文件）
- 内核与 `dyld` 的大部分交互
- Mach-O 二进制文件中的压缩和加密
- `dyld` 自身是如何构建的
- 符号插入（Symbol interposing）
- `dyld` 在 i386 和 ARM 上的操作，概念上相同，但两种架构在细节上有显著差异
- Mach-O 二进制格式的细节
- “胖”二进制文件（Fat binaries）是如何处理的

我遗漏了这些，原因有二：一是我写这篇文章时有点落后进度，实在没时间全部包含进去；二是真的没有篇幅在一篇文章中涵盖所有内容。然而，所有这些概念至少都有 Apple 的某些文档，并且内核和 `dyld` 都是开源的。以下是我希望有用的一些链接（警告，其中一些已经相当过时，因为 Apple 似乎对更新文档不太感兴趣）：

[Apple 的 Mach-O 文档](https://developer.apple.com/library/mac/#documentation/developertools/conceptual/MachOTopics/0-Introduction/introduction.html)  
 [Apple 的 Mach-O 参考](https://developer.apple.com/library/mac/#documentation/developertools/conceptual/MachORuntime/Reference/reference.html)  
 [Mach-O “加载器”头部，一个非常好的参考（也看看 `mach-o/` 目录中的其他文件）](file:///usr/include/mach-o/loader.h) [Apple 的 dyld 参考](https://developer.apple.com/library/mac/#documentation/developertools/Reference/MachOReference/Reference/reference.html)  
 [dlopen(3) 手册页](http://developer.apple.com/library/Mac/#documentation/Darwin/Reference/ManPages/man3/dlopen.3.html)  
 [dyld 的发行说明](http://developer.apple.com/library/mac/#releasenotes/DeveloperTools/RN-dyld/_index.html)  
 [dyld 截至 10.8.2 的源代码](http://opensource.apple.com/source/dyld/dyld-210.2.3/)  
 [内核截至 10.8.2 的源代码（特别是 `bsd/kern/kern_exec.c` 和 `bsd/kern/mach_loader.c`）](http://opensource.apple.com/source/xnu/xnu-2050.18.24/)

**结论**  
`dyld` 是 OS X 最基本的部分之一；没有它，除了内核之外什么都不会运行。伴随这种责任而来的是显著的复杂性，而 `dyld` 充满了这种复杂性。其中一些复杂性来自 `dyld` 巨大的向后兼容性要求，还有一些仅仅来自它必须处理的任务的广泛范围。大多数开发者无需如此详细地理解链接，但也许下次你在 Xcode 中从链接器收到一条奇怪的错误信息时，你会对在哪里寻找问题有更好的主意。不过，也可能不会；`ld` 有时会相当令人困惑。

这就是本周我为你准备的全部内容。下周回来，Mike 会带来一个特别的惊喜；他的下一篇文章特别棒！

你喜欢这篇文章吗？我整本书都在卖！第二卷和第三卷已经出版了！它们有 ePub、PDF、印刷版，以及 iBooks 和 Kindle 版本。[点击这里了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-11-09-dyld-dynamic-linking-on-os-x.html)

添加你的想法，发表评论：

垃圾帖和离题帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
