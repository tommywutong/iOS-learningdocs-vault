---
title: 'Friday Q&A 2012-11-30：让我们构建一个 Mach-O 可执行文件'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f5e089a6803c6ed6'
translated: true
---

> 原文：[Friday Q&A 2012-11-30: Let's Build A Mach-O Executable](https://www.mikeash.com/pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html)　·　mikeash.com Friday Q&A

发布于 2012-11-30 17:59 | [RSS 源](https://www.mikeash.com/pyblog/rss.py) ([全文源](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2012-12-14: Objective-C Pitfalls](https://www.mikeash.com/pyblog/friday-qa-2012-12-14-objective-c-pitfalls.html)  
前一篇文章：[Friday Q&A 2012-11-16: Let's Build objc_msgSend](https://www.mikeash.com/pyblog/friday-qa-2012-11-16-lets-build-objc_msgsend.html)  
标签：[assembly](https://www.mikeash.com/pyblog/?tag=assembly) [dwarf](https://www.mikeash.com/pyblog/?tag=dwarf) [evil](https://www.mikeash.com/pyblog/?tag=evil) [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [guest](https://www.mikeash.com/pyblog/?tag=guest) [letsbuild](https://www.mikeash.com/pyblog/?tag=letsbuild) [macho](https://www.mikeash.com/pyblog/?tag=macho)

Friday Q&A 2012-11-30：让我们构建一个 Mach-O 可执行文件

作者：[Gwynne Raskind](http://www.darkrainfall.org/)

**合适的工具做合适的事**  
在 OS X 上，从汇编语言输入生成二进制文件的最佳工具当然是汇编器 `as`。不过，如果你试图直接用其来构建一个原始二进制文件，你会发现 `as` 本身也充当了静态链接器（static linker）。这并非我们想要的。

这方面的更灵活的工具是 `nasm`，即 [Netwide Assembler](http://nasm.us/)。Xcode 命令行工具也安装了 `nasm`，但不幸的是，Apple 提供的版本极其老旧，为 0.98.40——就 bug 修复来说，只能追溯到 2007 年，就功能而言则停在 1999 年。在撰写本文时，最新版本是 2.10.05，可以通过 `port install nasm`、`brew install nasm` 或任何你喜欢的包管理器来安装。如果你不使用包管理器，也可以自行下载并编译源代码。

`nasm` 2.x 包含许多有用的功能，例如 64 位支持和 Mach-O 输出。我们不会使用 `nasm` 的 Mach-O 支持，因为这一切的要点在于手动完成，但能用 64 位指令构建一个 64 位二进制文件总归不错，而不必拼凑 32 位字！

**回看最初的程序**  
以下是我们要为其构建 Mach-O 二进制文件的 C 源代码。为了让生成的二进制文件保持相对简单，我编写时避免了导入超出最低限度的信息：

```
    #define NULL ((void *)0L)
    extern int printf(const char * restrict format, ...);
    typedef long time_t;
    extern time_t time(time_t *sloc);

    int main(void)
    {
        printf("Hello, world #%ld!\n", time(NULL));
        return 0;
    }
```

需要注意的几点：

- 我没有使用 `#include <stdio.h>` 和 `#include <time.h>`，而是手动声明了 `printf()` 和 `time()`，定义了 `time_t` 类型，并用宏定义了 `NULL`。这样避免了为标准头文件中各种各样定义的内容发出额外的调试信息。
- 我将 `main()` 定义为不接受参数。这通常是非常糟糕的做法，但由于 C 的调用约定，它仍能正确工作。
- 我使用了一个实际进行格式替换的格式字符串，这样我用来生成测试文件的编译器就不会过于高效地将其替换为 `puts()` 调用。

对应的汇编如下（使用 Clang 3.3svn 在 `-Os` 下构建）：

```
            .section        __TEXT,__text,regular,pure_instructions
            .globl  _main
    _main:                                  ## @main
            .cfi_startproc
    ## BB#0:                                ## %entry
            pushq   %rbp
    Ltmp2:
            .cfi_def_cfa_offset 16
    Ltmp3:
            .cfi_offset %rbp, -16
            movq    %rsp, %rbp
    Ltmp4:
            .cfi_def_cfa_register %rbp
            xorl    %edi, %edi
            callq   _time
            leaq    L_.str(%rip), %rdi
            movq    %rax, %rsi
            xorb    %al, %al
            callq   _printf
            xorl    %eax, %eax
            popq    %rbp
            ret
            .cfi_endproc

            .section        __TEXT,__cstring,cstring_literals
    L_.str:                                 ## @.str
            .asciz   "Hello, world #%ld!\n"

    .subsections_via_symbols
```

代码本身非常直白：在 `__TEXT,__text` 段（section）内，建立栈帧（stack frame），调用 `time()`，加载 `L_.str` 字符串，将 `al` 置零，调用 `printf`，将 `eax` 清零，拆除栈帧，然后返回。接着在 `__TEXT,__cstring` 段中，将 `L_.str` 标签定义为指向一个以零结尾的 ASCII 字符串。最后，声明此文件中没有符号位于基本块（basic block）内部——这是链接器（linker）进行死代码剥离（dead code stripping）时需要的。

其余指令与调用帧信息（Call Frame Information）有关，用于展开数据（`.unwind_info` 与 `.eh_frame`，提供异常处理支持）和调试信息（`.debug_frame`）。我们将手动构建前两者。

为清晰起见，我将省略完整的 DWARF 调试信息。即便对这个非常简单的程序来说，这也会让已经过长的文章再增加不少篇幅。

**Mach-O 可执行文件的开头**  
我们的 `nasm` 输入文件将用来生成一个 Mach-O 文件，所以我们需要以 Mach-O 头部开头。我们将使用 64 位小端 Mach-O 格式，其头部结构如下：

```
    struct mach_header_64 {
        uint32_t    magic;      /* mach magic number identifier */
        cpu_type_t  cputype;    /* cpu specifier */
        cpu_subtype_t   cpusubtype; /* machine specifier */
        uint32_t    filetype;   /* type of file */
        uint32_t    ncmds;      /* number of load commands */
        uint32_t    sizeofcmds; /* the size of all the load commands */
        uint32_t    flags;      /* flags */
        uint32_t    reserved;   /* reserved */
    };

    /* Constant for the magic field of the mach_header_64 (64-bit architectures) */
    #define MH_MAGIC_64 0xfeedfacf /* the 64-bit mach magic number */
    #define MH_CIGAM_64 0xcffaedfe /* NXSwapInt(MH_MAGIC_64) */
```

对应 Mach-O 头部的 `nasm` 输入如下：

```
    bits 64
    cpu x64

    __mh_execute_header:
        dd 0xfeedfacf   ; MH_MAGIC_64
        dd 16777223     ; CPU_TYPE_X86 | CPU_ARCH_ABI64
        dd 0x80000003   ; CPU_SUBTYPE_I386_ALL | CPU_SUBTYPE_LIB64
        dd 2            ; MH_EXECUTE
        dd 16           ; number of load commands
        dd ___loadcmdsend - ___loadcmdsstart    ; size of load commands
        dd 0x00200085   ; MH_NOUNDEFS | MH_DYLDLINK | MH_TWOLEVEL | MH_PIE
        dd 0            ; reserved
    ___loadcmdsstart:
```

`bits` 和 `cpu` 指令只是告诉 `nasm` 以 64 位模式运行。

Mach-O 头部之后紧接着的就是加载命令（load commands）。对一个可执行文件来说，有一整套命令是必需的，此外还有一大堆**可能**出现的命令。Clang 为本可执行文件生成了 16 条加载命令。一条加载命令的结构如下：

```
    struct load_command {
        uint32_t cmd;       /* type of load command */
        uint32_t cmdsize;   /* total size of command in bytes */
    };
```

每条加载命令实际上都比这个大；`cmd` 字段告诉加载器（loader）如何解释后续数据。对 64 位 Mach-O 文件而言，加载命令**必须**对齐到 8 字节边界。

**段（Segment）与节（Section）**  
段是 `dyld` 在运行时实际映射到内存中的数据块和代码块。节是段内部的进一步划分。段和节都有名称，其中不少是标准预定义的。

这是我们的第一条段命令：

```
    ___pagezerostart:
        dd 0x19         ; LC_SEGMENT_64
        dd ___pagezeroend - ___pagezerostart    ; command size
        db '__PAGEZERO',0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0            ; VM address
        dq 0x100000000  ; VM size
        dq 0            ; file offset
        dq 0            ; file size
        dd 0x0          ; VM_PROT_NONE (maximum protection)
        dd 0x0          ; VM_PROT_NONE (inital protection)
        dd 0            ; number of sections
        dd 0x0          ; flags
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___pagezeroend:
```

这是 `__PAGEZERO` 段，它将 64 位虚拟内存空间的整个低 4GB 预置为不可访问。由于该段被标记为不可读、不可写、不可执行，解引用 `NULL` 指针会立刻导致段错误（segmentation fault）。

下一条段命令更复杂：

```
    ___TEXTstart:
        dd 0x19         ; LC_SEGMENT_64
        dd ___TEXTend - ___TEXTstart    ; command size
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000  ; VM address
        dq 0x1000       ; VM size
        dq 0            ; file offset
        dq 0x1000       ; file size
        dd 0x7          ; VM_PROT_READ | VM_PROT_WRITE | VM_PROT_EXECUTE
        dd 0x5          ; VM_PROT_READ | VM_PROT_EXECUTE
        dd 6            ; number of sections
        dd 0x0          ; flags
    ___TEXTtextstart:
        db '__text',0,0,0,0,0,0,0,0,0,0 ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___codestart - ___TEXTload ; address
        dq ___codeend - ___codestart    ; size
        dd ___codestart ; offset
        dd 0            ; alignment as power of 2 (1)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x80000400   ; S_REGULAR | S_ATTR_PURE_INSTRUCTIONS | S_ATTR_SOME_INSTRUCTIONS
        dd 0            ; reserved1
        dd 0            ; reserved2
        dd 0            ; reserved3
    ___TEXTstubsstart:
        db '__stubs',0,0,0,0,0,0,0,0,0  ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___stubstart - ___TEXTload ; address
        dq ___stubend - ___stubstart    ; size
        dd ___stubstart ; offset
        dd 1            ; alignment as power of 2 (2)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x80000408   ; S_SYMBOL_STUBS | S_ATTR_PURE_INSTRUCTIONS | S_ATTR_SOME_INSTRUCTIONS
        dd 0            ; reserved1 (index into indirect symbol table)
        dd 6            ; reserved2 (size per stub)
        dd 0            ; reserved3
    ___TEXTstubhelperstart:
        db '__stub_helper',0,0,0    ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___stubhelpstart - ___TEXTload ; address
        dq ___stubhelpend - ___stubhelpstart    ; size
        dd ___stubhelpstart ; offset
        dd 2            ; alignment as power of 2 (4)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x80000400   ; S_REGULAR | S_ATTR_PURE_INSTRUCTIONS | S_ATTR_SOME_INSTRUCTIONS
        dd 0            ; reserved1
        dd 0            ; reserved2
        dd 0            ; reserved3
    ___TEXTcstringstart:
        db '__cstring',0,0,0,0,0,0,0    ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___strsstart - ___TEXTload ; address
        dq ___strsend - ___strsstart    ; size
        dd ___strsstart ; offset
        dd 0            ; alignment as power of 2 (1)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000002   ; S_CSTRING_LITERALS
        dd 0            ; reserved1
        dd 6            ; reserved2
        dd 0            ; reserved3
    ___TEXTunwindinfostart:
        db '__unwind_info',0,0,0    ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___uwstart - ___TEXTload   ; address
        dq ___uwend - ___uwstart    ; size
        dd ___uwstart   ; offset
        dd 0            ; alignment as power of 2 (1)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000000   ; no flags
        dd 0            ; reserved1
        dd 0            ; reserved2
        dd 0            ; reserved3
    ___TEXTehframestart:
        db '__eh_frame',0,0,0,0,0,0 ; section name (pad to 16 bytes)
        db '__TEXT',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100000000 + ___ehstart - ___TEXTload   ; address
        dq ___ehend - ___ehstart    ; size
        dd ___ehstart   ; offset
        dd 3            ; alignment as power of 2 (8)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000000   ; no flags
        dd 0            ; reserved1
        dd 0            ; reserved2
        dd 0            ; reserved3
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___TEXTend:
```

这就是 `__TEXT` 段，它涵盖了所有可执行代码和大量其他数据。它包含六个节。每个节根据各自的节信息进行对齐，并且所有节紧贴着放在段的末尾，因此 `__TEXT` 开头不少字节是零。不过，由于链接器映射段的方式，`__TEXT` 实际上囊括了所有 Mach-O 头部。我们稍后会看到，符号表中甚至还为 `__mh_execute_header` 保留了一条记录。这六个节分别是：

1. `__text`——可执行文件的**实际**代码，所有函数都在这里。在本例中，只有一个函数——`main()`。它被标记为 `S_REGULAR`，意为“就是一个普通节”，并被标记为同时包含“一些指令”（至少含有一部分可执行代码）和“纯指令”（**只**包含可执行代码）。
2. `__stubs`——跳转到非延迟（non-lazy）和延迟（lazy）符号节的跳转表。关于本节内容的解释，请参阅我之前的文章。它被标记为 `S_SYMBOL_STUBS`，含义相当不言而喻。
3. `__stub_helper`——供延迟动态绑定（lazy dynamically bound）符号使用的辅助函数。
4. `__cstring`——存放代码中只读 C 字符串字面量的节。
5. `__unwind_info`——可执行文件代码的紧凑展开（compact unwind）信息，为 OS X 上的异常处理而生成。
6. `__eh_frame`——可执行文件代码的 DWARF2 展开信息，为异常处理与调试而生成。

接下来是 `__DATA` 段：

```
    ___DATAstart:
        dd 0x19         ; LC_SEGMENT_64
        dd ___DATAend - ___DATAstart    ; command size
        db '__DATA',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100001000  ; VM address
        dq 0x1000       ; VM size
        dq 0x1000       ; file offset
        dq 0x1000       ; file size
        dd 0x7          ; VM_PROT_READ | VM_PROT_WRITE | VM_PROT_EXECUTE
        dd 0x3          ; VM_PROT_READ | VM_PROT_WRITE
        dd 2            ; number of sections
        dd 0x0          ; flags
    ___DATAnlsymptrstart:
        db '__nl_symbol_ptr',0  ; section name (pad to 16 bytes)
        db '__DATA',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100001000 + ___nlsymptrstart - ___DATAload ; address
        dq ___nlsymptrend - ___nlsymptrstart    ; size
        dd ___nlsymptrstart ; offset
        dd 3            ; alignment as power of 2 (8)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000006   ; S_NON_LAZY_SYMBOL_POINTERS
        dd 2            ; reserved1 (index into indirect symbol table)
        dd 0            ; reserved2
        dd 0            ; reserved3
    ___DATAlasymptrstart:
        db '__la_symbol_ptr',0  ; section name (pad to 16 bytes)
        db '__DATA',0,0,0,0,0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100001000 + ___lasymptrstart - ___DATAload ; address
        dq ___lasymptrend - ___lasymptrstart    ; size
        dd ___lasymptrstart ; offset
        dd 3            ; alignment as power of 2 (8)
        dd 0            ; relocations data offset
        dd 0            ; number of relocations
        dd 0x00000007   ; S_LAZY_SYMBOL_POINTERS
        dd 4            ; reserved1 (index into indirect symbol table)
        dd 0            ; reserved2
        dd 0            ; reserved3
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___DATAend:
```

这里只有两个节，因为该程序没有任何全局或静态数据：非延迟和延迟符号桩（stub）。

然后是最后一个段，`__LINKEDIT`：

```
    ___LINKEDITstart:
        dd 0x19         ; LC_SEGMENT_64
        dd ___LINKEDITend - ___LINKEDITstart    ; command size
        db '__LINKEDIT',0,0,0,0,0,0 ; segment name (pad to 16 bytes)
        dq 0x100002000  ; VM address
        dq 0x1000       ; VM size
        dq 0x2000       ; file offset
        dq ___LINKEDITdataend - ___LINKEDITdatastart    ; file size
        dd 0x7          ; VM_PROT_READ | VM_PROT_WRITE | VM_PROT_EXECUTE
        dd 0x1          ; VM_PROT_READ
        dd 0            ; number of sections
        dd 0x0          ; flags
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___LINKEDITend:
```

`__LINKEDIT` 段包含 `dyld` 所使用的各种数据，如符号表、间接符号表、rebase 操作码、binding 操作码、导出表、函数起始（function starts）信息、代码内数据（data-in-code）表，以及部分代码签名（code signing）数据。

**大量链接器（Linker）数据**  
接下来的几条加载命令处理静态与动态链接信息：

```
    ___dyldinfostart:
        dd 0x80000022   ; LC_DYLD_INFO | LC_REQ_DYLD
        dd ___dyldinfoend - ___dyldinfostart    ; command size
        dd ___rebasestart   ; rebase info offset
        dd ___rebaseend - ___rebasestart    ; rebase info size
        dd ___bindstart ; binding info offset
        dd ___bindend - ___bindstart    ; binding info size
        dd 0            ; weak binding info offset
        dd 0            ; weak binding info size
        dd ___lazystart ; lazy binding info offset
        dd ___lazyend - ___lazystart    ; lazy binding info size
        dd ___exportstart   ; export info offset
        dd ___exportend - ___exportstart    ; export info size
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___dyldinfoend:
    ___symtabinfostart:
        dd 0x2          ; LC_SYMTAB
        dd ___symtabinfoend - ___symtabinfostart    ; command size
        dd ___symtabstart   ; symbol table offset
        dd (___symtabend - ___symtabstart) >> 4 ; number of symbols
        dd ___strtabstart   ; string table offset
        dd ___strtabend - ___strtabstart    ; string table size
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___symtabinfoend:
    ___dysymtabinfostart:
        dd 0xb          ; LC_DYSYMTAB
        dd ___dysymtabinfoend - ___dysymtabinfostart    ; command size
        dd 0            ; local symbols index
        dd 8            ; number of local symbols
        dd 8            ; external symbols index
        dd 2            ; number of external symbols
        dd 10           ; undefined symbols index
        dd 3            ; number of undefined symbols
        dd 0            ; table of contents offset
        dd 0            ; table of contents entries
        dd 0            ; module table offset
        dd 0            ; module table entries
        dd 0            ; external references table offset
        dd 0            ; external references table entries
        dd ___indirsymstart ; indirect symbol table offset
        dd (___indirsymend - ___indirsymstart) >> 2 ; indirect symbol table entries
        dd 0            ; local relocation table offset
        dd 0            ; local relocation table entries
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___dysymtabinfoend:
    ___loaddylinkerstart:
        dd 0xe          ; LC_LOAD_DYLINKER
        dd ___loaddylinkerend - ___loaddylinkerstart    ; command size
        dd ___loaddylinkername - ___loaddylinkerstart   ; offset to name
    ___loaddylinkername:
        db '/usr/lib/dyld',0    ; name
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___loaddylinkerend:
    ___maincmdstart:
        dd 0x80000028   ; LC_MAIN | LC_REQ_DYLD
        dd ___maincmdend - ___maincmdstart  ; command size
        dq _main        ; offset of main from start of __TEXT
        dq 0            ; stack size
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___maincmdend:
    ___loadlibsystemstart:
        dd 0xc          ; LC_LOAD_DYLIB
        dd ___loadlibsystemend - ___loadlibsystemstart  ; command size
        dd ___loadlibsystemname - ___loadlibsystemstart ; offset to path
        dd 2            ; UNIX time stamp Wed Dec 31 19:00:02 1960
        dd 0x00a90300   ; current version (0.169.3.0)
        dd 0x00010000   ; compatibility version (0.1.0.0)
    ___loadlibsystemname:
        db '/usr/lib/libSystem.B.dylib' ; path
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___loadlibsystemend:
    ___fstartscmdstart:
        dd 0x26         ; LC_FUNCTION_STARTS
        dd ___fstartscmdend - ___fstartscmdstart    ; command size
        dd ___functionstartsstart   ; offset to function starts data (fun label name, isn't it?)
        dd ___functionstartsend - ___functionstartsstart    ; size of function starts data (even more fun name!)
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___fstartscmdend:
    ___datacodecmdstart:
        dd 0x29         ; LC_DATA_IN_CODE
        dd ___datacodecmdend - ___datacodecmdstart  ; command size
        dd ___datacodestart ; offset to data-in-code information
        dd ___datacodeend - ___datacodestart ; size of data-in-code information
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___datacodecmdend:
    ___dycodesigncmdstart:
        dd 0x2b         ; LC_DYLIB_CODE_SIGN_DRS
        dd ___dycodesigncmdend - ___dycodesigncmdstart  ; command size
        dd ___dylibcodesignaturesstart  ; offset to code signatures from dylibs
        dd ___dylibcodesignaturesend - ___dylibcodesignaturesstart  ; you get the idea, right?
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___dycodesigncmdend:
```

概括一下，这一长串数据包含：

1. 一份二进制文件的动态链接信息清单。此命令以及部分其他命令被标记为 `LC_REQ_DYLD`，这意味着如果加载此二进制文件的 `dyld` 版本不理解该命令，必须直接终止，而不能在缺少这些信息的情况下继续运行。
2. 符号表与字符串表的所在位置。这些位置以距文件开头的偏移量给出，但实际数据约定位于 `__LINKEDIT` 段内。运行时，`dyld` 会计算 `symtable_base_address = linkedit_base_address + (symtab_offset - linkedit_offset)` 来得到符号表在内存中的实际地址。字符串表同理，对 `LC_DYLD_INFO` 和 `LC_DYSYMTAB` 命令中给出的偏移量同样如此处理。
3. 二进制文件的一组动态符号数据，给出了符号表内不同类型符号的偏移量与数量。
4. `LC_LOAD_DYLINKER` 命令给出用于加载该可执行文件的动态链接器（dynamic linker）的硬编码路径。这由内核（kernel）使用，而非动态链接器：内核启动进程时会运行此处指定的程序。但别以为能用它来劫持加载过程；内核不会让你随便指定动态链接器的。
5. `LC_MAIN`，取代了较旧的 `LC_UNIXTHREAD` 命令。过去，可执行文件会通过内嵌在线程状态中的信息来初始化，但最近有人意识到，由于 `dyld` 很早就开始运行，而且几乎所有可执行文件的线程状态都一模一样，这纯粹是浪费时间和空间。于是改成用 `LC_MAIN` 给出入口点（`main()`）的地址，`dyld` 直接跳转过去，同时也取代了原先负责设置 `main()` 调用环境的 `crt1.o` 对象文件。
6. `LC_LOAD_DYLIB` 就是“我为解决某些未定义符号而链接到以下动态库”的命令。此二进制文件仅链接到 `libSystem.B.dylib`，即 OS X 上等价于 `libc` 的库。
7. `LC_FUNCTION_STARTS` 是 `__LINKEDIT` 段中的一张表，给出了可执行文件中每个函数入口点的地址。除其他用途外，它允许存在未在符号表中出现的函数。
8. `LC_DATA_IN_CODE` 类似地是一张表，标出嵌在可执行代码内部的数据字节的位置。这有非常多的用途，准确反汇编只是其中一端。
9. 最后，`LC_DYLIB_CODE_SIGN_DRS` 给出了与可执行文件链接的每条动态库的指定要求（designated requirements）列表。这让代码签名机制能够在不必加载每条所链接动态库的前提下，判断可执行文件的适用性。

**还有几条！**  
你刚以为结束了，我们还有三条加载命令没介绍：

```
    ___uuidstart:
        dd 0x1b         ; LC_UUID
        dd ___uuidend - ___uuidstart    ; command size
        db 0xd3,0xec,0x58,0x28,0x02,0x26,0x36,0x29,0xab,0xc3,0x7d,0x6d,0xc9,0xf9,0x2d,0xda  ; D3EC5828-0226-3629-ABC3-7D6DC9F92DDA
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___uuidend:
    ___osverstart:
        dd 0x24         ; LC_VERSION_MIN_MACOSX
        dd ___osverend - ___osverstart  ; command size
        dd 0x000a0800   ; OS min version: 10.8
        dd 0x000a0800   ; Build SDK version: 10.8
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___osverend:
    ___sourceverstart:
        dd 0x2a         ; LC_SOURCE_VERSION
        dd ___sourceverend - ___sourceverstart  ; command size
        dq 0            ; Source version: 0.0.0.0.0
        align 8, db 0   ; pad with zero to 8-byte boundary
    ___sourceverend:
    ___loadcmdsend:
```

这些分别是二进制的 UUID、其目标 OS X 版本、其所链接的 SDK 版本，以及“源代码版本（source version）”。我完全没有找到“源代码版本”到底是什么的线索，而且在我看过的二进制文件里它只是一串零，所以你的猜测应该跟我差不多。

**终于来点不一样的了！**  
现在要做的第一件事，是把文件填充到 `main()` 的开始位置：

```
    ___TEXTload:
        times (0xf14-($-$$)) db 0   ; pad the __TEXT segment
```

你可能会问为什么不写 `_main-($-$$)` 而是硬编码起始地址。这看起来确实脆弱。没错。问题在于 `nasm` 没有提供简单的办法把数据对齐到段的“末尾”，毕竟我们没有使用它内置的节支持。在填上这部分填充前，它根本不知道 `_main` 在哪儿！于是这里我直接硬编码了 `main()` 开始的偏移量（即 `__TEXT,__text` 节的 `addr` 字段的精确值），把它当作一个 hack 保留下来，而不是去琢磨一个优雅却复杂的办法。

现在我们按顺序处理数据；其实未必要按某种特定顺序，因为我们在加载命令里使用的标签会根据它们在文件中的实际位置把一切重新定位，但按顺序来也没坏处。首先是 `__TEXT,__text`，也就是可执行代码。注意，我们必须把原始汇编代码改写为 `nasm` 的语法——`nasm` 用的是 Intel 语法，而非 GNU 语法。主要区别是所有操作数的方向是反的，并且寄存器名称上没有前缀。所有各种指令也被去掉了，因为我们现在手工完成它们原本的工作。

```
    ___codestart:
    _main:
        push    rbp
        mov     rbp, rsp
        xor     edi, edi
        call    _time
        lea     rdi, [rel L_str]
        mov     rsi, rax
        xor     al, al
        call    _printf
        xor     eax, eax
        pop     rbp
        ret
    ___codeend:
```

指令上也没有加任何大小后缀，因为 `nasm` 能从操作数自行推断。字符串加载的 `rel` 限定符就是让 `nasm` 生成 `rip` 相对寻址而非绝对位置，这是必要的，因为我们把这个可执行文件标记为位置无关（position-independent）代码。

接下来是 `time()` 与 `printf()` 的符号桩，以及桩辅助函数：

```
    ___stubstart:
    _printf:
        jmp     [rel _lazy_printf]
    _time:
        jmp     [rel _lazy_time]
    ___stubend:

    ___stubhelpstart:
    _stub_helper:
        lea     r11, [rel _nonlazy_dyld_stub_binder]
        push    r11
        jmp     [rel _nonlazy_dyld_stub_binder]
        nop
        push    strict qword (_lazy_printf - ___lasymptrstart)
        jmp     _stub_helper
        push    strict qword (_lazy_time - ___lasymptrstart)
        jmp     _stub_helper
    ___stubhelpend:
```

桩本身跳转到 `__DATA` 段中的延迟符号绑定（lazy symbol bindings）地址。这些地址最初会直接跳回 `_stub_helper` 底部，后者将符号在延迟符号节中的偏移量加载出来，并通过一个非延迟符号（它将在可执行文件加载时被 `dyld` 绑定）调用到 `dyld` 内部。接着 `dyld` 会绑定该符号并改写延迟符号节，使得此后对该桩的调用直接跳转到目标函数。请注意，这些全都是直接的非条件跳转，而不是子程序调用。另请注意使用了 `strict qword` 指令，强制 `nasm` 为栈压入操作发出完整的 64 位值。

然后是 C 字符串节，因为我们只有一个字符串，所以非常简短：

```
    ___strsstart:
    L_str:
        db      "Hello, world #%ld!\n",0
    ___strsend:
```

现在轮到展开表。这里是使用 Apple 定义的“紧凑展开编码（compact unwind encoding）”进行编码的（据我所知）。

```
    ___uwstart:
        dd 1            ; unwind info version
        dd _commonEncodings - ___uwstart    ; common encodings array offset
        dd 0            ; count of common encodings
        dd _personalities - ___uwstart  ; personality array offset
        dd 0            ; count of personalities
        dd _index - ___uwstart  ; first-level index offset
        dd 2            ; count of entries in first-level index
    _commonEncodings:
    _personalities:
    _index:
    __entry1_0:
        dd _main        ; function offset
        dd __entry2_0 - ___uwstart  ; offset to second-level entry
        dd _lsda - ___uwstart   ; offset to language-specific data array entry
    __entry1_1:
        dd ___codeend+1 ; function offset (end of table)
        dd 0            ; offset to second-level entry - zero means end of table
        dd _lsda - ___uwstart   ; offset to LSDA
    _lsda:
    _pages:
    __entry2_0:
        dd 3            ; UNWIND_SECOND_LEVEL_COMPRESSED
        dw ___entrypage0 - __entry2_0   ; offset to entry page
        dw 1            ; number of entries in entry page
        dw ___enc0 - __entry2_0 ; offset to encoding page
        dw 1            ; number of entries in encoding page
    ___entrypage0:
    ____entrypage0_0:
        dd (0 << 24) | (0)  ; encoding index and function offset relative to first-level index offset
    ___enc0:
    ____enc0_0:
        dd 0x01000000   ; UNWIND_X86_64_MODE_RBP_FRAME | UNWIND_X86_64_REG_NONE
    ___uwend:
```

然后是同一信息的 DWARF 编码版本。为了节省大家的时间，我就不带注释写出这部分了，因为它很复杂，而且仅是以更加冗长的方式重复了上面的展开信息。

```
    ___ehstart:
        db 0x14,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x01,0x7a,0x52,0x00,0x01,0x78,0x10,0x01
        db 0x10,0x0c,0x07,0x08,0x90,0x01,0x00,0x00,0x24,0x00,0x00,0x00,0x1c,0x00,0x00,0x00
        db 0x34,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x20,0x00,0x00,0x00,0x00,0x00,0x00,0x00
        db 0x00,0x41,0x0e,0x10,0x86,0x02,0x43,0x0d,0x06,0x00,0x00,0x00,0x00,0x00,0x00,0x00
    ___ehend:
```

**数据，数据，数据……呃，算是吧**  
`__TEXT` 段到此结束。接下来是 `__DATA` 段，它包含延迟与非延迟符号指针：

```
    ___DATAload:

    ___nlsymptrstart:
    _nonlazy_dyld_stub_binder:
        dq 0x0000000000000000
    _nonlazy_table_start:
        dq 0x0000000000000000
    ___nlsymptrend:

    ___lasymptrstart:
    _lazy_printf:
        dq 0x100000000 + _stub_helper_printf
    _lazy_time:
        dq 0x100000000 + _stub_helper_time
    ___lasymptrend:
```

在真实的可执行文件中，`__DATA` 通常还会包含静态数据、全局变量的空间等内容。

**链接编辑器（Link Editor）**  
`__LINKEDIT` 是个真正的麻烦所在，因为它的结构是任意的，里面的数据也未必总有充分的文档。我尽可能以易于理解的方式表示其中的内容，但我不能保证已经做到。

我们从 rebasing 操作码开始，`dyld` 在应用 ASLR 时会用到它们：

```
    ___rebasestart:
        db 0x10 | 0x01  ; REBASE_OPCODE_SET_TYPE_IMM | REBASE_TYPE_POINTER
        db 0x20 | 0x02  ; REBASE_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB | indexOfSegment(__DATA) (2)
        db 0x10         ; uleb128_encode(_lazy_printf - ___DATAload)
        db 0x50 | 0x02  ; REBASE_OPCODE_DO_REBASE_IMM_TIMES | 2
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___rebaseend:
```

这段的意思是：“在 __DATA 段中，从偏移 0x10 开始，使用指针类型，依据该段的加载地址 rebase 两个指针。”

接下来是 binding 操作码和延迟 binding 操作码：

```
    ___bindstart:
        db 0x11         ; BIND_OPCODE_SET_DYLIB_ORDINAL_IMM | 1
        db 0x40         ; BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMM | 0
        db 'dyld_stub_binder',0 ; immediate operand
        db 0x51         ; BIND_OPCODE_SET_TYPE_IMM | BIND_TYPE_POINTER
        db 0x72         ; BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB | indexOfSegment(__DATA) (2)
        db 0x00         ; uleb128_encode(0)
        db 0x90         ; BIND_OPCODE_DO_BIND
        db 0x00         ; BIND_OPCODE_DONE
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___bindend:
    ___lazystart:
        db 0x72,0x10    ; BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB | indexOfSegment(__DATA) (2), uleb128_encode(0x10)
        db 0x11         ; BIND_OPCODE_SET_DYLIB_ORDINAL_IMM | 1
        db 0x40,'_printf',0 ; BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMM | 0, '_printf'
        db 0x90,0x00    ; BIND_OPCODE_DO_BIND, BIND_OPCODE_DONE
        db 0x72,0x18    ; BIND_OPCODE_SET_SEGMENT_AND_OFFSET_ULEB | indexOfSegment(__DATA) (2), uleb128_encode(0x18)
        db 0x11         ; BIND_OPCODE_SET_DYLIB_ORDINAL_IMM | 1
        db 0x40,'_time',0   ; BIND_OPCODE_SET_SYMBOL_TRAILING_FLAGS_IMM | 0, '_time'
        db 0x90,0x00    ; BIND_OPCODE_DO_BIND, BIND_OPCODE_DONE
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___lazyend:
```

这些操作码将一个名为 `dyld_stub_binder` 的非延迟符号作为指针绑定到 `__DATA` 段偏移 0 的位置。对延迟符号，它们把 `_printf` 绑定到 `__DATA` 段偏移 `0x10`，把 `_time` 绑定到偏移 `0x18`。

下面是导出 trie：

```
    ___exportstart:
    _exnode0:
        db 0x00         ; terminal size
        db 0x01         ; child count
        db '_',0        ; name
        db _exnode1 - ___exportstart    ; child node offset
    _exnode1:
        db 0x00         ; terminal size
        db 0x02         ; child count
        db '_mh_execute_header',0   ; name
        db _exnode3 - ___exportstart    ; child node offset
    _exnode2:
        db 'main',0     ; name
        db _exnode4 - ___exportstart    ; child node offset
    _exnode3:
        db 0x02         ; terminal size
        db 0x00         ; flags
        db 0x00         ; address - uleb128_encode(0)
        db 0x00         ; child count
    _exnode4:
        db 0x03         ; terminal size
        db 0x00         ; flags
        db 0x94,0x1e    ; address - uleb128_encode(0xf14)
        db 0x00         ; child count
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___exportend:
```

它们构成了该可执行文件导出的两个符号 `__mh_execute_header` 和 `_main` 的 trie（前缀树）。

下面是压缩函数起始表，表示为一组需要叠加到基代码地址上的增量：

```
    ___functionstartsstart:
        db 0x94         ; delta = 0x14, address  = ___codestart
        db 0x1e         ; delta = 0x1e, end 
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___functionstartsend:
```

然后是代码内数据表。哎呀，这个可执行文件里压根没有这类数据，但加载命令照样被加上了：

```
    ___datacodestart:
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___datacodeend:
```

来点针对 dylib 的指定要求如何？我不太确定这是用什么格式表示的，我只是尽可能去解读：

```
    ___dylibcodesignaturesstart:
        dd 1            ; count of code signatures (maybe?)
        dd 0            ; unknown
        dd 0x14         ; unknown
        db 0xfa,0xde,0x0c,0x00,0x00,0x00,0x00,0x28
        db 0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x06
        db 0x00,0x00,0x00,0x02,0x00,0x00,0x00,0x0b
        db 0x6c,0x69,0x62,0x53,0x79,0x73,0x74,0x65
        db 0x6d,0x2e,0x42,0x00,0x00,0x00,0x00,0x03  ; code signature for libSystem.B.dylib
        dd 0            ; unknown
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___dylibcodesignaturesend:
```

**符号表**  
符号表是余下大部分有趣内容所在：

```
    ___symtabstart:
        dd L_srcdir - ___strtabstart    ; string table offset
        db 0x64         ; N_SO
        db 0x00         ; section 0
        dw 0x00         ; no desc
        dq 0            ; address 0
        dd L_srcfile - ___strtabstart   ; string table offset
        db 0x64         ; N_SO
        db 0x00         ; section 0
        dw 0x00         ; no desc
        dq 0            ; address 0
        dd L_objfile - ___strtabstart   ; string table offset
        db 0x66         ; N_OSO
        db 0x03         ; section 3
        dw 0x01         ; desc(?)
        dq 0x50b8c91f   ; st_mtime
        dd L_empty - ___strtabstart ; no string
        db 0x2e         ; N_BNSYM
        db 0x01         ; section 1
        dw 0x00         ; desc
        dq 0x100000000 + _main      ; start address
        dd L_main1 - ___strtabstart ; string table offset
        db 0x24         ; N_FUN
        db 0x01         ; section 1
        dw 0x00         ; desc
        dq 0x100000f14  ; start address
        dd L_empty - ___strtabstart ; no string
        db 0x24         ; N_FUN
        db 0x00         ; section 0
        dw 0x00         ; desc
        dq 0x20         ; address
        dd L_empty - ___strtabstart ; no string
        db 0x4e         ; N_ENSYM
        db 0x01         ; section 1
        dw 0x00         ; desc
        dw 0x20         ; address
    _sym_mh_execute_header:
        dd L_mhexechead - ___strtabstart    ; string table offset
        db 0x0f         ; N_SECT | N_EXT
        db 0x01         ; section 1
        dw 0x0010       ; REFERENCED_DYNAMICALLY
        dq 0x100000000 + __mh_execute_header    ; start address
    _sym_main:
        dd L_main2 - ___strtabstart ; string table offset
        db 0x0f         ; N_SECT | N_EXT
        dw 0x0000       ; no extra flags
        dq 0x100000000 + _main  ; start address
    _sym_printf:
        dd L_printf - ___strtabstart    ; string table offset
        db 0x01         ; N_UNDF | N_EXT
        dw 0x0100       ; dynamic library 1
        dq 0            ; address
    _sym_time:
        dd L_time - ___strtabstart  ; string table offset
        db 0x01         ; N_UNDF | N_EXT
        dw 0x0100       ; dynamic library 1
        dq 0            ; address
    _sym_dyld_stub_binder:
        dd L_binder - ___strtabstart    ; string table offset
        db 0x01         ; N_UNDF | N_EXT
        dw 0x0100       ; dynamic library 1
        dq 0            ; address
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___symtabend:

    ___indirsymstart:
        dd (_sym_printf - ___symtabstart) >> 4  ; index into symbol table
        dd (_sym_time - ___symtabstart) >> 4    ; index into symbol table
        dd (_sym_dyld_stub_binder - ___symtabstart) >> 4    ; index into symbol table
        dd 0x40000000   ; INDIRECT_SYMBOL_ABS
        dd (_sym_printf - ___symtabstart) >> 4  ; index into symbol table
        dd (_sym_time - ___symtabstart) >> 4    ; index into symbol table
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___indirsymend:

    ___strtabstart:
    L_spc:
        db ' '
    L_empty:
        db 0
    L_srcdir:
        db '/Users/gwynne/',0
    L_srcfile:
        db 'test.c',0
    L_objfile:
        db '/var/folders/b8/qgjb841d71d55cf8jh1myb540000gn/T/test-KyuIba.o',0
    L_main1:
        db '_main',0
    L_mhexechead:
        db '__mh_execute_header',0
    L_main2:
        db '_main',0
    L_printf:
        db '_printf',0
    L_time:
        db '_time',0
    L_binder:
        db 'dyld_stub_binder',0
        align 8, db 0   ; pad with 0 to 8-byte boundary
    ___strtabend:

    ___LINKEDITdataend:
```

这里有符号表（包括 STABS 条目）、间接符号表（只是一组指向符号表的索引，告诉 `dyld` 在 binding 操作码不够用时如何使用这些符号桩——基本上可视为遗留数据），以及字符串表，其中存放着符号表所需的所有人类可读字符串。

**结论**  
这确实是一长串主要由原始十六进制字节组成的混乱堆。而笑点在于：即便按此处写出的内容，它也**仍然**无法生成一个能用的 Mach-O 二进制文件！

为什么？因为我没有正确考虑对齐要求，而到文章该发布时我已经来不及修好这个问题。不过，这里所有的表和结构都是正确的，所以希望它仍然能提供认知价值，让你体会到哪怕最简单的二进制文件背后也涉及那么多东西，更让你庆幸 `ld` 和 `dyld` 替你干了这么多活！

一如既往，感谢阅读。希望你喜欢这篇文章！

喜欢这篇文章吗？我准备出售一整本此类文章的合集！第二卷和第三卷现已出版！它们以 ePub、PDF、印刷版以及 iBooks 和 Kindle 格式提供。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[本页评论 RSS 源](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2012-11-30-lets-build-a-mach-o-executable.html)

添加你的想法，发表评论：

垃圾留言和离题帖子将被直接删除，恕不另行通知。违规者可能被我全权酌情公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
