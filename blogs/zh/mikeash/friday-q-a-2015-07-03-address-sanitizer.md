---
title: 'Friday Q&A 2015-07-03：Address Sanitizer'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2015-07-03-address-sanitizer.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:434172c49135fee8'
translated: true
---

> 原文：[Friday Q&A 2015-07-03: Address Sanitizer](https://www.mikeash.com/pyblog/friday-qa-2015-07-03-address-sanitizer.html)　·　mikeash.com Friday Q&A

发表于 2015-07-03 13:52 | [RSS 订阅](https://www.mikeash.com/pyblog/rss.py)（[全文订阅](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)） | [博客索引](https://www.mikeash.com/pyblog/)
下一篇：[Friday Q&A 2015-07-17：何时使用 Swift 结构体和类](https://www.mikeash.com/pyblog/friday-qa-2015-07-17-when-to-use-swift-structs-and-classes.html)
上一篇：[Friday Q&A 2015-06-19：Swift 新特性中最好的部分](https://www.mikeash.com/pyblog/friday-qa-2015-06-19-the-best-of-whats-new-in-swift.html)
标签：[c](https://www.mikeash.com/pyblog/?tag=c) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [valgrind](https://www.mikeash.com/pyblog/?tag=valgrind)

Friday Q&A 2015-07-03：Address Sanitizer

作者 [Mike Ash](https://www.mikeash.com/)

**一个极其危险的处境**
C 在很多方面都是一门伟大的编程语言。它历经四十多年依然蓬勃发展，便是明证。这不是我学习的第一门（或第二门）编程语言，但它是最初让我真正理解这些神秘计算机内部运行原理的语言，也是我学习并至今仍在使用的第一门语言。

C 同时也是一门危险得可怕的编程语言，它给世界带来了许多麻烦，让人们轻易创造出漏洞百出的 bug，而大多数其他语言甚至无法表达这类 bug。

主要问题在于内存安全（memory safety）。C 在这方面毫无保障。像下面这样的代码不仅可以通过编译，而且很可能会正常运行：

```
    char *ptr = malloc(5);
    ptr[12] = 0;
```

这段代码分配了一个 5 字节的数组，然后往该数组的第 13 个字节写入数据，静默地破坏了内存中那个位置上的任何内容。也许是无关紧要的内容（在 Apple 平台上，即使你要求的内存少于 16 字节，`malloc` 也总是至少分配 16 字节，所以这段代码在这里总是能正常工作。但请勿编写依赖这一事实的代码）。也许是一些无关紧要的内容，也许是重要的内容。

更为理智的编程语言会跟踪数组大小，并在允许操作之前验证索引。例如，等效的 Java 代码会可靠地抛出异常。当你能够依赖这一点时，调试神秘问题会变得容易得多。例如，如果一个变量本应包含值 4，但实际上包含值 5，你就知道是修改该变量的某段代码在作怪（至少在你到达开始仔细检查编译器的那个调试阶段之前是这样）。在 C 中，你不能做这种假设。它可能是某段故意修改该变量的代码，也可能是某段通过错误指针或越界索引意外修改该变量的代码。

解决这个问题已经催生了一个完整的产业。例如，Clang 的静态分析器可以检测源代码中的某些类型的内存安全问题。像 Valgrind 这样的程序可以在运行时检测不安全的内存访问。

Address Sanitizer 是另一种这样的解决方案。它采用一种新方法，既有优点也有缺点，但它可以成为发现代码问题的宝贵工具。

**内存访问验证**
许多这类工具的工作原理是在运行时验证内存访问。理论是，如果你能在访问发生时，通过将访问与程序实际分配的内存进行比较来验证它们，就可以在 bug 发生时发现它们，而不是很久之后通过它们的副作用才发现。

理想情况下，每个指针都会包含关于其所属整个内存区域大小和位置的数据，并且每次访问都可以根据这些数据进行验证。没有特别的理由认为不能构建一个这样做的 C 编译器，但附加到每个指针上的额外元数据会使其程序无法与正常 C 编译器编译的代码兼容。这意味着无法轻易使用系统库，这将严重限制可以用这样的系统进行测试的代码。

Valgrind 通过在模拟器中运行整个程序来解决这个问题。这使其能够与正常 C 编译器生成的二进制文件一起工作，无需任何修改。然后，它在程序运行时进行分析，跟踪程序操作时每块内存的状态。这使其能够与任何未修改的程序以及系统库一起工作。但这也带来了巨大的速度损失，可能使其无法在性能敏感的代码上使用。这种方法还需要深入理解平台上每个系统调用的语义，以便适当跟踪其对内存的更改，这需要与宿主操作系统紧密集成。因此，多年以来 Valgrind 对 Mac 的支持时好时坏，截至本文撰写时，它不支持 10.10。

Guard Malloc 利用了 CPU 内置的内存检查机制。它替换了标准的 `malloc` 函数，使新函数将每次分配之后的内存标记为不可读且不可写。当程序尝试访问末尾之后的内存时，程序会可靠地发生陷阱。

问题在于硬件内存保护相对粗糙。内存只能以页面粒度标记为可读或不可读，而任何现代系统上的内存页大小至少是 4kB。这意味着每次分配至少使用 8kB 内存：一页用于分配本身，另一页用于末尾的禁止访问页，即使分配只有几个字节。这也意味着较小的越界可能不会被检测到。内存需要在 16 字节边界上分配，以保留标准 `malloc` 的保证，因此任何不是 16 字节倍数的分配，在末尾都会有几个字节没有被标记为禁止访问。

Address Sanitizer 试图让这种禁止访问内存的概念更加精细。它本质上是一种比 Guard Malloc 更慢但更实用的方法。

**跟踪禁止访问的内存**
如果不能使用硬件内存保护，那么就必须在软件中进行跟踪。由于不能随指针传递额外数据，必须在某种全局表中进行跟踪。该表需要读取速度快且修改速度快。

Address Sanitizer 采用了一种简单而巧妙的方法。它在进程地址空间中保留一个固定区域，称为影子内存（shadow memory）。在 Address Sanitizer 的术语中，被标记为禁止访问的字节称为“已毒化”（poisoned），影子内存跟踪哪些字节已被毒化。一个简单的公式将进程地址空间内的每个地址转换为影子内存中的一个位置。每八字节的常规内存块映射到影子内存的一个字节，该字节跟踪这八个字节的毒化状态。

由于八字节的内存映射到影子内存的八位，自然会认为每个字节的毒化状态由影子内存中的一位来跟踪。然而，Address Sanitizer 实际上在影子内存字节中保留了一个单独的整数。它假设一个八字节块内所有已毒化的内存都是连续的并且位于末尾，因此影子字节描述该块内未毒化字节的数量。值 `1` 到 `7` 表示区域开头相应数量的字节未被毒化。值 `0` 表示整个区域未被毒化。负值表示整个区域已被毒化。这种略微奇怪的方案使得在根据影子内存检查访问时计算更简单。分配开始时不会那么紧密地靠在一起，因此已毒化字节连续且位于末尾的假设不会造成任何问题。

有了这个表结构，Address Sanitizer 会在程序中生成额外的代码，以检查每次通过指针进行的读写操作，如果相关内存已被毒化，则抛出错误。这就是集成到编译器中而不仅仅是作为外部库或运行时环境存在的优势：可以可靠地识别每次指针访问，并将适当的检查添加到机器代码中。

编译器集成还允许一些巧妙的技巧，例如能够毒化并保护局部和全局变量，而不仅仅是堆分配。局部变量和全局变量在它们之间会分配一些额外的填充，并且填充被毒化以捕获任何溢出。这是 Guard Malloc 做不到的事情，也是 Valgrind 难以做到的。

编译器集成也有缺点。特别地，Address Sanitizer 无法捕获系统库中的错误内存访问。它与系统库是兼容的，你可以开启 Address Sanitizer，构建一个链接了 Cocoa 的程序并使其正常工作，但它不会捕获 Cocoa 执行的错误内存访问，也不会捕获你的代码在 Cocoa 分配的内存上执行的错误内存访问。

Address Sanitizer 还有助于捕获释放后使用（use-after-free）错误。当内存被释放时，它全部被标记为已毒化，因此随后的访问将被捕获。当内存首先被重用于新的分配时，释放后使用错误尤其令人讨厌，因为你会破坏不相关的数据位。Address Sanitizer 通过将新释放的内存放入一个回收队列来防御这一点，该队列会在一段时间内保持其未分配状态，之后才能被重用。

当然，对每次指针访问都添加检查会带来相当大的开销。这在很大程度上取决于你的代码在做什么，因为不同类型的代码访问指针内容的频率可能相差很大。平均而言，预计会有大约 2-5 倍的减速。这很显著，但通常不足以使程序无法使用。

**如何使用**
在 Xcode 7 中，使用 Address Sanitizer 很简单。在命令行编译时，在 `clang` 调用中添加 `-fsanitize=address`。下面是一个演示它的程序：

```
    #include <stdlib.h>

    void Write(char *ptr, size_t index, char value) {
        ptr[index] = value;
    }

    int main(int argc, char **argv) {
        char *ptr = malloc(12);
        Write(ptr, 12, 42);
    }
```

使用 Address Sanitizer 编译并运行：

```
    $ clang -fsanitize=address test.c
    $ ./a.out
```

它会迅速崩溃并产生大量输出：

```
    ==18186==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000df9c at pc 0x000101025efc bp 0x7fff5ebda8a0 sp 0x7fff5ebda898
    WRITE of size 1 at 0x60200000df9c thread T0
        #0 0x101025efb in Write (/Users/mikeash/Dropbox/shell/asan/./a.out+0x100000efb)
        #1 0x101025f46 in main (/Users/mikeash/Dropbox/shell/asan/./a.out+0x100000f46)
        #2 0x7fff940025c8 in start (/usr/lib/system/libdyld.dylib+0x35c8)
        #3 0x0  (<unknown module>)

    0x60200000df9c is located 0 bytes to the right of 12-byte region [0x60200000df90,0x60200000df9c)
    allocated by thread T0 here:
        #0 0x101070960 in wrap_malloc (/Applications/Xcode-beta.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/lib/clang/7.0.0/lib/darwin/libclang_rt.asan_osx_dynamic.dylib+0x42960)
        #1 0x101025f2d in main (/Users/mikeash/Dropbox/shell/asan/./a.out+0x100000f2d)
        #2 0x7fff940025c8 in start (/usr/lib/system/libdyld.dylib+0x35c8)
        #3 0x0  (<unknown module>)

    SUMMARY: AddressSanitizer: heap-buffer-overflow ??:0 Write
    0x1c0400001ba0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    0x1c0400001bb0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    0x1c0400001bc0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    0x1c0400001bd0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    0x1c0400001be0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
    =>0x1c0400001bf0: fa fa 00[04]fa fa 00 06 fa fa 00 00 fa fa 00 04
    0x1c0400001c00: fa fa 00 06 fa fa 00 07 fa fa 00 fa fa fa 00 00
    0x1c0400001c10: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
    0x1c0400001c20: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
    0x1c0400001c30: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
    0x1c0400001c40: fa fa 00 00 fa fa 00 00 fa fa 00 00 fa fa 00 00
    Shadow byte legend (one shadow byte represents 8 application bytes):
    Addressable:           00
    Partially addressable: 01 02 03 04 05 06 07 
    Heap left redzone:       fa
    Heap right redzone:      fb
    Freed heap region:       fd
    Stack left redzone:      f1
    Stack mid redzone:       f2
    Stack right redzone:     f3
    Stack partial redzone:   f4
    Stack after return:      f5
    Stack use after scope:   f8
    Global redzone:          f9
    Global init order:       f6
    Poisoned by user:        f7
    Container overflow:      fc
    Array cookie:            ac
    Intra object redzone:    bb
    ASan internal:           fe
    Left alloca redzone:     ca
    Right alloca redzone:    cb
    ==18186==ABORTING
    Abort trap: 6
```

这是非常丰富的信息，在实际场景中对于定位问题极具帮助。它不仅显示错误写入的位置，还显示内存最初分配的位置，以及大量额外数据。

在 Xcode 内部使用 Address Sanitizer 同样简单：编辑你的 scheme，点击“诊断（Diagnostics）”标签，然后勾选“启用 Address Sanitizer（Enable Address Sanitizer）”复选框。然后像往常一样构建并运行，观察诊断信息的输出。

**额外功能：Undefined Behavior Sanitizer**
错误的内存访问只是 C 语言提供的众多有趣的未定义行为之一。Clang 提供了另一个 sanitizer，可以捕获许多未定义行为的实例。下面是一个示例程序：

```
    #include <stdio.h>
    #include <stdlib.h>

    int main(int argc, char **argv) {
        int value = 1;
        for(int x = 0; x < atoi(argv[1]); x++) {
            value *= 10;
            printf("%d\n", value);
        }
    }
```

来运行一下：

```
    $ clang undefined.c 
    $ ./a.out 15
    10
    100
    1000
    10000
    100000
    1000000
    10000000
    100000000
    1000000000
    1215752192
    -727379968
    1316134912
    276447232
    -1530494976
```

结果在最后变得有点奇怪。这并不意外：有符号整数溢出在 C 中是未定义行为。能够捕获这个问题而不是仅仅产生错误数据会很好。Undefined Behavior Sanitizer 来救场了！通过传递 `-fsanitize=undefined-trap -fsanitize-undefined-trap-on-error` 来启用它：

```
    $ clang -fsanitize=undefined-trap -fsanitize-undefined-trap-on-error undefined.c
    $ ./a.out 15
    10
    100
    1000
    10000
    100000
    1000000
    10000000
    100000000
    1000000000
    Illegal instruction: 4
```

这不像 Address Sanitizer 那样提供任何额外信息，但它确实会在未定义行为发生的那个点立即停止执行，并且可以轻松地在调试器中检查问题。

目前，undefined behavior sanitizer 尚未集成到 Xcode 中。你可以通过在项目的构建设置中直接添加上述编译器标志来为你的应用启用它。

**结论**
Address Sanitizer 是一项伟大的技术，可以捕获 C 代码中的许多有问题错误。它并不完美，无法找到所有错误，但即便如此，它也提供了极其有用的诊断信息。我强烈建议你在代码库上尝试它，看看它能发现什么。结果可能会让你大吃一惊。

今天就到这里。下次再见，带来更多精彩内容。一如既往，Friday Q&A 由读者的建议驱动，所以如果你有希望我在这里讨论的话题，请[发送给我](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我出售包含它们的整本书籍！第二卷和第三卷现已上市！它们提供 ePub、PDF、印刷版以及 iBooks 和 Kindle 版。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS 订阅](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2015-07-03-address-sanitizer.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会被我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
