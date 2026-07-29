---
title: Power ISA 链接器笔记
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-02-26-linker-notes-on-power-isa'
original_language: en
published: 2023-02-26
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e08216729ef416de'
translated: true
---

> 原文：[Linker notes on Power ISA](https://maskray.me/blog/2023-02-26-linker-notes-on-power-isa)　·　MaskRay (宋方睿)

[2023-02-26](https://maskray.me/blog/2023-02-26-linker-notes-on-power-isa)

# Power ISA 链接器笔记

本文介绍了 ELF 链接器中关于 Power ISA 的目标架构细节。最初有 IBM POWER。1991 年 Apple–IBM–Motorola 联盟创建了 PowerPC。2006 年，该架构更名为 Power ISA。根据 ISA 手册，“2006 年，Freescale 和 IBM 合作创建了 Power ISA Version 2.03，这标志着架构的重新统一，将 Book E 内容与更通用的 PowerPC Version 2.02 合并。”

“PowerPC”和“powerpc”这些术语在众多地方仍然流行，包括官方目标三连名中的 `powerpc-*-*-*` 和 `powerpc64-*-*-*`。缩写“PPC”（“ppc”）也在很多地方使用。为简单起见，我将 32 位架构称为“PPC32”，将 64 位架构称为“PPC64”。

我们将看到，Power10 之前缺少 PC-relative 寻址如何导致 ABI 和链接器变得极其复杂。

## ABI 文档

- _Power Architecture™ 32-bit Application Binary Interface Supplement 1.0 - Linux® & Embedded_ 修订于 2011 年。
- _64-bit PowerPC ELF Application Binary Interface Supplement 1.9_。这通常被称为 ELFv1，现已废弃。一些 64 位目标仍然使用此 ABI。
- _64-Bit ELF V2 ABI Specification: Power Architecture_

32 位 ELF ABI 或多或少不受维护者关注，仅在一些爱好者中仍有相关性。2019 年，我花了一周时间研究 PPC32 ABI，并为 ld.lld 添加了 PPC32 移植。

对于一个 64 位目标文件，存在 `.opd` 节是 ELFv1 的一个良好指示器。`e_flags` 为 2 是 ELFv2 的良好指示器。`e_flags` 为 0 的可能是 ELFv1 目标文件，或者是未使用任何受差异影响特性的目标文件。

_A new ABI for little-endian PowerPC64 Design & Implementation_ (2014) 描述了引入 ELFv2 的动机。

## 全局偏移表（Global Offset Table）

### PPC32 GOT

在 PPC32 上，`_GLOBAL_OFFSET_TABLE_` 定义在 `.got` 节的开始位置。`.got` 有 3 个保留条目。`_GLOBAL_OFFSET_TABLE_[0]` 存储 `_DYNAMIC` 的链接时地址，由 glibc `sysdeps/powerpc/powerpc32/dl-machine.h` 使用。`_GLOBAL_OFFSET_TABLE_[1]` 和 `_GLOBAL_OFFSET_TABLE_[2]` 用于延迟绑定 PLT（glibc 中的 `_dl_runtime_resolve` 和 link map）。

`.plt` 类似于其他架构的 `.got.plt`。`.plt[n]` 保存 PLT 条目（位于 `.glink` 中的某处）的地址。

与 x86-32 一样，PPC32 缺少带有 PC-relative 寻址的内存加载。作为一个简陋的替代方案，PPC32 设置 r30 来保存 GOT 基址，用于与位置无关的代码（PIC）。GOT 基址对于 small PIC 和 large PIC 是不同的。

- 对于 `-fpic` 和 `-fpie`，r30 指向组件中的 `_GLOBAL_OFFSET_TABLE_`。
- 对于 `-fPIC` 和 `-fPIE`，r30 指向当前编译单元的 `.got2`。如下所述，这对生成 PLT 的重定位有影响。

```plaintext
.section        ".got2","aw"
.align 2
.LCTOC1 = .+32768
.LC0:
  .long var

  ...
  bcl 20,31,.L2
.L2:
  mflr 30                     # r30 = lr
  addis 30,30,.LCTOC1-.L2@ha
  addi 30,30,.LCTOC1-.L2@l    # finish setting up the GOT base
  lwz 9,.LC0-.LCTOC1(30)      # load the address of var relative to the GOT base
```

组件可能有多个编译单元，每个都有不同的 `.got2`。在输出文件中，一个文件中的 `.got2` 可能相对于输出 `.got2` 有任意偏移。

### PPC64 GOT

在 PPC64 上，`.got` 有 1 个保留条目：`.TOC.` 的链接时地址。`.TOC.` 定义在 `.got` 节起始位置加上 0x8000 处。

`.plt` 类似于其他架构的 `.got.plt`。`.plt` 的类型为 `SHT_NOBITS`，对齐为 4。

### PPC64 ELFv2 目录表（Table of Contents, TOC）

在 Power10 之前，PPC64 使用 `.toc` 而不是 `.got` 来保存全局变量和取地址函数的地址。这与大多数架构不同。

```c
extern int var0, var1;
__attribute__((noinline)) int foo() { return var0 + var1; }
int bar() { return foo(); }
```

上面的 C 程序编译为以下汇编代码：  
1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
23  
foo:  
.Lfunc_begin0:  
.Lfunc_gep0:  
 addis 2, 12, .TOC.-.Lfunc_gep0@ha  
 addi 2, 2, .TOC.-.Lfunc_gep0@l  
.Lfunc_lep0:  
 .localentry foo, .Lfunc_lep0-.Lfunc_gep0  
  
 addis 3, 2, .LC0@toc@ha  
 addis 4, 2, .LC1@toc@ha  
 ld 3, .LC0@toc@l(3)  
 ld 4, .LC1@toc@l(4)  
 lwz 3, 0(3)  
 lwz 4, 0(4)  
 add 3, 4, 3  
 extsw 3, 3  
 blr  
  
.section .toc,"aw",@progbits  
.LC0:  
 .tc var0[TC],var0  
.LC1:  
 .tc var1[TC],var1

`foo` 有一个全局入口 `foo`/`.Lfunc_gep0` 和一个本地入口 `.Lfunc_lep0`。在本地入口之后，r2 保存当前组件的 TOC 基址。

如果 `foo` 和 `foo` 的调用者（例如 `bar`）在同一个组件中，调用者可以直接跳转到本地入口，跳过从全局入口开始的几条指令（通常为 2 条）。否则，调用者需要跳转到全局入口，以便 `foo` 自己更新 r2。此更新要求 r12 指向函数入口地址。我们将在深入探讨调用桩的小节中看到，维护 r2 和 r12 会导致很多麻烦。

另一个区别是显式提及 `.toc`。这种方案让编译器在编译单元内拥有控制权。使用传统的 GOT 方案，输入文件不会提及 `.got`。编译器无法控制链接器如何布局 `.got`。嗯，我不同意 `.toc` 的假定优势：编译器不知道全局信息，编译单元本地的布局可能不理想。链接器更适合做此类链接时优化。

`.tc` 指令是生成类型为 `R_PPC64_ADDR64` 的重定位的一种花哨方式。如果链接器决定创建一个 TOC 条目，该条目将是一个链接时常量（`-no-pie`），或者与一个动态重定位关联（`-pie` 或 `-shared`）。

Alan Modra

> ld.bfd 的一个特性是，输入 .toc（和 .got）节（匹配一个链接器输入节语句）可以被排序，将小模型代码使用的条目放在靠近 TOC 基址的前面。这就是 powerpc64 上的脚本通常使用 `*(.got .toc)` 而不是 `*(.got) *(.toc)` 的原因，因为第一种形式允许更大的排序自由度。

#### 尾调用（Tail call）

在上面的例子中，`bar` 尾调用了 `foo`，其中 `foo` 是非本地函数并使用 TOC（`st_other>0`）。大多数其他架构只需要一条分支指令。然而，TOC ABI 需要在分支指令之前增加 2 条额外指令（用于设置 TOC 指针）。  
1  
2  
3  
4  
5  
6  
7  
8  
9  
bar:  
.Lfunc_begin1:  
.Lfunc_gep1:  
 addis 2, 12, .TOC.-.Lfunc_gep1@ha  
 addi 2, 2, .TOC.-.Lfunc_gep1@l  
.Lfunc_lep1:  
.localentry bar, .Lfunc_lep1-.Lfunc_gep1  
 b foo  
 nop

**情况 1：`foo` 不可抢占**

链接器会将 `b foo` 解析为 `foo` 的本地入口。`bar` 的额外指令确保了：即使 `bar` 在没有设置 TOC 指针的情况下被调用，`foo` 仍然能获得正确的 TOC 指针。

**情况 2：`foo` 可抢占**

将需要一个调用桩，并且 `call foo` 后面的 `nop` 指令将被链接器替换为 `ld 2,4(1)`。即使这是尾调用，我们仍然需要一个 `nop`。

如果想保留尾调用语义（例如[这个跨模块 musttail 问题](https://github.com/llvm/llvm-project/issues/63214)），我们需要避免链接器进行这种 `nop => ld 2,4(1)` 的重写。这是可行的：`bar` 的所有调用者都必须恢复 TOC，即使 `bar` 不可抢占。虽然这可以通过 `.localentry bar, 1` 来实现（它在 `st_other` 中设置第 5 位，指示 GEP 和 LEP 之间偏移为零，并且对于调用者来说 r2 是调用者保存的），但工具链实现起来比较困难。

### TOC-间接 到 TOC-相对 优化

参见 [All about Global Offset Table#GOT optimization](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#got-optimization)。

## 过程链接表（Procedure Linkage Table）

### PPC32 PLT

_Power Architecture® 32-bit Application Binary Interface Supplement 1.0 - Linux® & Embedded_ 指定了两种 PLT ABI：BSS-PLT 和 Secure-PLT。

BSS-PLT 是较旧的方法，现已废弃。其他架构上的 `.plt` 由链接器创建，而 BSS-PLT 让 ld.so 生成 PLT 条目。优点是该节可以设为 `SHT_NOBITS`，因此不占用文件大小。然而，缺点是可写可执行内存页面的安全问题。更糟糕的是，作为一个实现问题，GNU ld 将 `.plt` 放置在 text 段中，使得整个 text 段可写可执行。这使得 `-z relro -z now` 失效。

在较新的 Secure-PLT ABI 中，`.plt` 保存函数地址表。`.plt` 类似于其他架构的 `.got.plt`。

链接器合成 `.glink`，这类似于其他架构的 `.plt`。与大多数架构不同，`.glink` 有一个尾部而不是头部。每个 PLT 条目要么是 `b footer`，要么是一个 nop 并落入尾部。在 ld.lld 中，为简单起见，我们只使用 `b footer`。关于 ld.lld 中 `PPC32GlinkSection` 的详细信息，请参见 [https://reviews.llvm.org/D75394](https://reviews.llvm.org/D75394)。

```plaintext
000102b4 <.glink>:
  b 0x102c0 <.glink+0xc>
  b 0x102c0 <.glink+0xc>
  b 0x102c0 <.glink+0xc>
  addis 11, 11, 0          # start of the resolver
  mflr 0
  bcl 20, 31, 0x102cc <.glink+0x18>
  addi 11, 11, 24
  mflr 12
  mtlr 0
  sub     11, 11, 12
  addis 12, 12, 1
  lwz 0, 184(12)
  lwz 12, 188(12)
  mtctr 0
  add 0, 11, 11
  add 11, 0, 11
  bctr
  nop
  nop
```

对于非 PIC 代码，一个可能可抢占的分支使用重定位类型 `R_PPC_REL24`。  
1  
2  
bl foo # R_PPC_REL24  
bl foo # R_PPC_REL24

如果调用目标可抢占，链接器会创建一个非 PIC 调用桩，并将调用者的分支指令重定向到该调用桩。非 PIC 调用桩将使用绝对寻址加载 `.plt[n]` 到 r11（调用者破坏的寄存器，call-clobbered）并跳转到那里。这种行为与大多数其他架构不同，其他架构中调用者可以直接跳转到 PLT 条目。  
1  
2  
3  
4  
5  
6  
7  
8  
9  
 bl 00000000.plt_call32.f  
 bl 00000000.plt_call32.f  
 ...  
  
00000000.plt_call32.f:  
 lis 11, .plt[n]@ha  
 lwz 11, .plt[n]@l(11)  
 mtctr 11  
 bctr

对于 PIC 代码，跳转到可能可抢占的目标使用 `R_PPC_PLTREL24` 作为生成 PLT 的重定位类型。附加数编码了调用者设置的 r30。是的，这很不寻常。

- 对于 `-fpic` 和 `-fpie`，附加数为 0。
- 对于 `-fPIC` 和 `-fPIE`，附加数为 0x8000。在 `-r` 模式下链接此可重定位目标文件可能会增加附加数。

调用函数时，如果目标可抢占，链接器会创建一个 PIC 调用桩，并将调用者的分支指令重定向到该调用桩。GNU ld 将 small PIC 调用桩命名为 `*.plt_pic32.*`，将 large PIC 调用桩命名为 `*.got2.plt_pic32.*`。ld.lld 遵循此命名约定。

调用桩知道调用者设置的 r30 的值（GOT 基址）。`.plt[n]` 到 r30 的距离是一个常数。调用桩计算 `.plt[n]` 的地址，加载条目，并跳转到那里。  
1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
14  
15  
16  
17  
18  
19  
20  
21  
22  
00000000.plt_pic32.f:  
 ## 如果 GOT 偏移超过 64KiB  
 addis 11, 30, .plt[n]-_GLOBAL_OFFSET_TABLE_@ha(30)  
 lwz 11, .plt[n]-_GLOBAL_OFFSET_TABLE_@l(30)  
 mtctr 11  
 bctr  
  
 ## 如果 GOT 偏移在 64KiB 以内  
 # lwz 11, .plt[n]-_GLOBAL_OFFSET_TABLE_(30)  
 # mtctr 11  
 # bctr  
 # nop  
  
00000000.got2.plt_pic32.f:  
 ## .got2 指的是属于当前编译单元的副本。
 ## 不同的编译单元必须使用不同的桩。
 addis 11, 30, .plt[n]-(.got2+0x8000)(30)  
 lwz 11, .plt[n]-(.got2+0x8000)@l(30)  
 mtctr 11  
 bctr  
  
 ## GOT 偏移在 64KiB 以内的情况与 plt_pic32.f 类似。

虽然我们有一个可行的解决方案，但如果我们重新审视这个方案，会发现设置 r30 极其昂贵。一个简单的尾调用示例（`void foo() { bar(); }`）需要许多条指令：

```plaintext
<foo>:
  stwu 1, -16(1)      # allocate stack
  mflr 0
  bcl 20, 31, 0x1bc   # set lr to PC
  stw 30, 8(1)        # save r30 which is used as the GOT base
  mflr 30
  addis 30, 30, 2     # high 16 bits of the GOT base (.got2+0x8000)
  stw 0, 20(1)        # save lr (copied to r0)
  addi 30, 30, 32140  # low 16 bits of the GOT base (.got2+0x8000)
  bl 0x1f0
  lwz 0, 20(1)
  lwz 30, 8(1)
  addi 1, 1, 16
  mtlr 0
  blr
```

### PPC64 ELFv2 PLT

`.glink` 类似于其他架构的 `.plt`，有一个 60 字节的头部。每个 PLT 条目由一条指令 `b .plt` 组成。PLT 头部从 `r12` 中减去第一个 PLT 条目的地址，以计算 PLT 索引。

无条件分支指令 `b`/`bl` 可能生成 `R_PPC64_REL24` 或 `R_PPC64_REL24_NOTOC` 类型的重定位。`R_PPC64_REL24` 表示调用者使用 TOC。`R_PPC64_REL24_NOTOC` 表示调用者不使用 TOC 或不保留 r2（[`DT_PPC64_OPT`](https://reviews.llvm.org/D150631) 将被设置为 2）。

条件分支指令可能生成类型为 `R_PPC64_REL14` 的重定位。

`R_PPC64_REL14`、`R_PPC64_REL24` 和 `R_PPC64_REL24_NOTOC` 都是生成 PLT 的重定位类型。如果需要 PLT 条目，链接器将创建一个传统或 PC-relative 的 PLT 调用桩，并将调用者的分支指令重定向到该调用桩。这种行为与大多数其他架构不同，其他架构中调用者可以直接跳转到 PLT 条目。效率低下的原因在于为 TOC 维护 r2 和 r12。

没有 `R_PPC64_REL14_NOTIC`。条件分支使用的 `R_PPC64_REL14` 通常不用于函数调用。

下面我将详细描述用于 TOC/NOTOC 互操作和范围扩展的调用桩。

## 线程局部存储（Thread Local Storage）

PPC32 和 PPC64 都使用 TLS Variant I 的一个变体：静态 TLS 块位于线程指针之上。线程指针指向线程控制块的末尾。

链接器执行 TLS 优化。

参见 [All about thread-local storage](https://maskray.me/blog/2021-02-14-all-about-thread-local-storage)。

### 旧版 IBM XL 编译器的应对措施

对于通用动态（General Dynamic）/本地动态（Local Dynamic）代码序列，需要用 `R_PPC64_TLSGD` 或 `R_PPC64_TLSLD` 标记 `bl __tls_get_addr`。

```plaintext
addis r3, r2, x@got@tlsgd@ha # R_PPC64_GOT_TLSGD16_HA
addi r3, r3, x@got@tlsgd@l   # R_PPC64_GOT_TLSGD16_LO
bl __tls_get_addr(x@tlsgd)   # R_PPC64_TLSGD followed by R_PPC64_REL24
nop
```

然而，有两种偏离上述标准的情况：

1. 直接调用 `__tls_get_addr`。这对于在 glibc/musl/FreeBSD 中实现 rtld 至关重要。

```plaintext
bl __tls_get_addr
nop
```

这仅在 `-shared` 链接中使用，因此不受下面 GD/LD 到 IE/LE 松弛处理的影响。

1. 编译器生成的 TLS 引用缺少 `R_PPC64_TLSGD`/`R_PPC64_TLSGD`

根据 Stefan Pintille 的说法，“在用于大端 PowerPC Linux 发行版的 ELFv1 ABI 过渡到用于小端 PowerPC Linux 发行版的 ELFv2 ABI 的早期阶段，TLS 重定位的规范存在一些歧义。GNU 链接器已经实现了对缺少重定位的 `__tls_get_addr` 调用的正确处理。不幸的是，我们直到尝试将 XL 编译的库与 LLD 链接时，才注意到 IBM XL 编译器没有按照更新后的 ABI 处理 TLS。”

不幸的是，简而言之，ld.lld 需要应对旧版 IBM XL 编译器的问题。否则，如果目标文件以 `-no-pie` 或 `-pie` 模式链接，结果将不正确，因为 4 条指令被部分重写（后 2 条未更改）。

## PPC64 ELFv2 TOC 调用者

使用 TOC 的调用者使用重定位类型 `R_PPC64_REL24` 标记其函数调用。

调用者期望 r2 不会改变，而被调用者可能会改变 r2。为了解决这个问题，编译器和链接器协作来保留 r2。

对于一个可能解析到不同编译单元的调用目标（例如，非定义声明、hidden visibility 定义），编译器在分支指令后插入一个 NOP。保证解析到当前编译单元的调用目标（例如，内部链接）不需要 NOP，因为 r2 不会改变。  
1  
2  
3  
4  
5  
caller:  
 bl foo  
 nop # 可能变为 `ld 2, 24(1)`  
 bl nonpreemptible  
 blr

注意：外部链接 hidden visibility 的调用目标也需要 NOP，以防被调用者不维护 TOC 指针时破坏 r2。

### TOC 调用者和可抢占的被调用者

如果被调用者可抢占，调用者和被调用者可能位于不同的组件中。

- 如果被调用者使用 TOC，它可能会将 r2 更改为其组件的 TOC 基址。
- 如果被调用者使用 PC-relative 寻址，它可能会将 r2 视为调用者保存的寄存器并破坏 r2。

链接器创建一个 PLT 调用桩，将 r2 保存在调用者栈帧中，并将 `nop` 修补为 `ld 2, 24(1)` 以恢复 r2。

```plaintext
<caller>:
  bl __plt_foo
  ld 2, 24(1)        # restore r2
  bl nonpreemptible
  bl nonpreemptible

<__plt_foo>:
  std 2, 24(1)       # save r2
  addis 12, 2, ...
  ld 12, ...(12)     # load .plt[n]
  mtctr 12
  bctr               # jump to the PLT entry
```

### TOC 调用者和 `localentry=1` 的不可抢占被调用者

非 TOC 被调用者可能保留也可能不保留 r2。它的 `.localentry` 值可能是 0 或 1，其中 1 表示 r2 可能被破坏。

与可抢占的被调用者情况类似，链接器创建一个调用桩来保存 r2，并将 `nop` 修补为 `ld 2, 24(1)` 以恢复 r2。

```plaintext
<caller>:
  bl __toc_save_foo
  ld 2, 24(1)        # restore r2
  bl nonpreemptible
  blr

<__toc_save_foo>:
  std 2, 24(1)       # save r2
  b foo              # jump to the callee
```

如果调用桩无法通过一条 `b` 指令到达调用目标，链接器会尝试使用 `addis+addi` 计算目标地址。  
1  
2  
3  
4  
5  
6  
\<__toc_save_far\>:  
 std 2, 24(1) # 保存 r2  
 addis 12, 2, ...  
 addi 12, 12, ...  
 mtctr 12  
 bctr # 跳转到被调用者

如果 `addis+addi` 无法到达调用目标，链接器会将目标地址存储在 `.branch_lt` 条目中，并执行间接分支。  
1  
2  
3  
4  
5  
6  
\<__toc_save_farther\>:  
 std 2, 24(1) # 保存 r2  
 addis 12, 2, ...  
 ld 12, ...(12) # 加载 .branch_lt[n]  
 mtctr 12  
 bctr # 跳转到被调用者

## PPC64 ELFv2 非 TOC 调用者

不使用 TOC 的调用者使用重定位类型 `R_PPC64_REL24_NOTOC` 标记其函数调用。

```plaintext
caller:
  bl foo@notoc
  blr
```

以下是关于非 TOC 调用者和 TOC 被调用者的测试。在 `a0` 和 `a1` 中，被调用者 `foo` 是不可抢占的，而在 `a2` 中，`foo` 是可抢占的。

```sh
echo 'int x = 42; void foo(); int main() { foo(); }' > a.c
printf '#include <stdio.h>\nextern int x; void foo() { printf("%%d\\n", x); }' > b.c
sed 's/^        /\t/' > Makefile <<'eof'
.MAKE.MODE := meta curDirOk=true
CC := /tmp/Rel/bin/clang --target=powerpc64le-linux-gnu
LDFLAGS := -fuse-ld=lld -Wl,--dynamic-linker=/usr/powerpc64le-linux-gnu/lib64/ld64.so.2,-rpath=/usr/powerpc64le-linux-gnu/lib -Wl,--no-power10-stubs

run: a0 a1 a2
        qemu-ppc64le-static -cpu power10 ./a0
        qemu-ppc64le-static -cpu power10 ./a1
        qemu-ppc64le-static -cpu power10 ./a2

a0: a.o b.o
        ${LINK.c} $> -o $@

a1: a.o b.o
        ${LINK.c} -r $> -o $@.ro
        ${LINK.c} $@.ro -o $@

a2: a.o b.so
        ${LINK.c} a.o ./b.so -o $@

a.o: a.c
        ${CC} -mcpu=power10 -c $>

b.so: b.o
        ${LINK.c} -shared $> -o $@
eof
```

调用 `bmake` 来运行测试。

### 非 TOC 调用者和可抢占的被调用者

被调用者可能使用也可能不使用 TOC。如果被调用者使用 TOC 且其 `.localentry` 值大于 1，则其全局入口点要求调用者将 r12 设置为函数入口地址。

链接器创建一个 PC-relative 的 PLT 调用桩，以在被调用者需要时设置 r12。

```plaintext
<caller>:
  bl __plt_pcrel_foo
  blr

<__plt_pcrel_foo>:
  pld 12, .plt[n]@pcrel   # load .plt[n]
  mtctr 12
  bctr                    # jump to the PLT entry
```

如果我们不使用 Power10 的 `pld`（`--power10-stubs=no`），将需要更多指令：  
1  
2  
3  
4  
5  
6  
7  
8  
9  
\<__plt_pcrel_foo\>:  
 mflr 12 # 保存 lr  
 bcl 20, 31, .+4  
 mflr 11 # r11 = 当前位置  
 mtlr 12 # 恢复 lr  
 addis 12, 11, offset@ha  
 ld 12, offset@l(12) # 加载 .plt[n]  
 mtctr 12  
 bctr # 跳转到 PLT 条目

### 非 TOC 调用者和不可抢占的 TOC 被调用者

不可抢占的被调用者可能使用也可能不使用 TOC。

- 如果被调用者不使用 TOC，分支指令可以直接指向目标。
- 如果被调用者使用 TOC，则使用可抢占被调用者的情况。

```plaintext
<caller>:
  bl __gep_setup_foo
  blr

<__gep_setup_foo>:
  paddi 12, 0, foo@pcrel  # compute target address
  mtctr 12
  bctr                    # jump to target
```

如果我们不使用 Power10 的 `paddi`（`--power10-stubs=no`），将需要更多指令。  
1  
2  
3  
4  
5  
6  
7  
8  
9  
\<__gep_setup_foo\>:  
 mflr 12  
 bcl 20, 31, .+4  
 mflr 11  
 mtlr 12  
 addis 12, 11, offset@ha  
 addi 12, 12, offset@l  
 mtctr 12  
 bctr

### 不可抢占 IFUNC 的 IPLT 代码序列

在 PPC64 上，不可抢占的 IFUNC 放置在 `.glink` 中。如果存在非 GOT 非 PLT 的重定位，出于指针相等性的考虑，我们会将符号的类型从 `STT_IFUNC` 和 `STT_FUNC` 更改，并将其绑定到 `.glink` 条目。

在 PPC64 ELFv2 上，`.glink` 中的每条 `bl` 指令都与一个由 `R_PPC64_JUMP_SLOT` 重定位的 `.plt` 条目相关联。IPLT 没有关联的 `R_PPC64_JUMP_SLOT`，因此我们不能在 `.iplt` 中使用 `bl`。相反，我们创建一个常规的 TOC 调用桩。

不可抢占的 ifunc 实现可能不保存 TOC 指针，因此如果另一个 DSO 定义了一个解析为此实现的 ifunc 解析器，调用该 ifunc 将无法正确设置 TOC 指针。这是 [https://sourceware.org/glibc/wiki/GNU_IFUNC](https://sourceware.org/glibc/wiki/GNU_IFUNC) 中描述的限制（尽管在许多架构上在实践中是有效的）：

> 要求 (a)：解析器必须与实现在同一个编译单元中定义。

参见 [https://reviews.llvm.org/D71509](https://reviews.llvm.org/D71509)。

## 范围扩展桩（Range extension thunks）

在 PPC32 上，无条件分支指令 `b`/`bl` 的范围为 +-32MiB，可能使用 3 种重定位类型：`R_PPC_LOCAL24PC`、`R_PPC_REL24` 和 `R_PPC_PLTREL24`。如果目标无法从指令位置到达，将使用范围扩展桩。`R_PPC_LOCAL24PC` 是一个无用的重定位。所有出现都可以替换为 `R_PPC_REL24`。

在 PPC64 上，无条件分支指令 `b`/`bl` 的范围为 +-32MiB，可能使用 `R_PPC64_REL24` 或 `R_PPC64_REL24_NOTOC`。上述用于 TOC/NOTOC 互操作的调用桩已经处理了许多长分支。尚未处理的情况是：

- TOC 调用者和不可抢占的 TOC 被调用者
- 非 TOC 调用者和不可抢占的非 TOC 被调用者

ld.lld 仅对第一种情况有实现。链接后，调用者可能看起来像这样：

```plaintext
<caller>:
  bl __long_branch_nonpreemptible
  blr

<__long_branch_nonpreemptible>:
  addis 12, 2, offset@ha
  ld 12, offset@l(12)     # load .branch_lt[n]
  mtctr 12
  bctr                    # jump to the target
```

桩的分支目标可能是一个 PLT 条目。

## GPR 保存和恢复函数

GPR 保存和恢复函数（GPR Save and Restore Functions）定义了一些特殊函数，这些函数可能被 GCC 生成的汇编引用（LLVM 不引用它们）。

使用 GCC -Os，当调用保存的寄存器数量超过某个阈值时，GCC 会生成 `_savegpr[01]_{14..31}` 和 `_restgpr[01]_{14..31}` 调用，并期望链接器定义它们。参见 [https://sourceware.org/pipermail/binutils/2002-February/017444.html](https://sourceware.org/pipermail/binutils/2002-February/017444.html) 和 [https://sourceware.org/pipermail/binutils/2004-August/036765.html](https://sourceware.org/pipermail/binutils/2004-August/036765.html)。

这很奇怪，因为 `libgcc.a` 是更自然的位置。然而，链接器生成方法的好处是链接器可以生成多个副本以避免长分支桩。我不认为这个好处足够重要到让 ld.lld 的主干实现复杂化，所以我采用了一个简单的方法。

- 检查是否使用了 `_savegpr0_{14..31}`
- 如果是，定义所需的符号，并添加一个包含代码序列的 InputSection。

## `--emit-relocs`

在 GNU ld 中，与 aarch64 和 x86 不同，powerpc 端口会转换重定位类型。例如，TOC-间接到 TOC-相对的优化使用一对重定位 `R_PPC64_TOC16_HA(.toc)+R_PPC64_TOC16_LO_DS(.toc)`。优化后，它们将变为 `R_PPC64_TOC16_HA(sym)+R_PPC64_TOC16_LO(sym)`。即使第一条指令被转换为 NOP，`R_PPC64_TOC16_HA` 重定位仍然存在。

通用动态 TLS 模型代码序列可能使用重定位 `R_PPC64_GOT_TLSGD16_HA+R_PPC64_GOT_TLSGD16_LO+R_PPC64_TLSGD+R_PPC64_REL24`。优化后，它们将变为：

- `R_PPC64_NONE+R_PPC64_TPREL16_HA+R_PPC64_TPREL16_LO+R_PPC64_NONE`（通用动态到本地执行 TLS 优化后）。
- `R_PPC64_GOT_TPREL16_HA+R_PPC64_GOT_TPREL16_LO_DS+R_PPC64_NONE+R_PPC64_NONE`（通用动态到初始执行 TLS 优化后）。

```plaintext
addis 3,2,x@got@tlsgd@ha
addi 3,3,x@got@tlsgd@l
bl __tls_get_addr(x@tlsgd)
nop

=>

addis or nop                     # R_PPC64_GOT_TLSGD16_HA(x)
addi 3, 2, ...                   # R_PPC64_GOT_TLSGD16_LO(x)
bl thunk_for___tls_get_addr_opt  # R_PPC64_TLSGD(x), R_PPC64_REL24(__tls_get_addr_opt@GLIBC_2.22)
nop
```

GNU ld 甚至用重定位类型注解桩，例如  
1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
11  
12  
13  
0000000000002000 \<0000001b.plt_branch.1c:2\>:  
 2000: ff ff 82 3d addis 12, 2, -1  
 0000000000002000: R_PPC64_TOC16_HA *ABS*+0x20020d0  
 2004: d0 7e 8c e9 ld 12, 32464(12)  
 0000000000002004: R_PPC64_TOC16_LO_DS *ABS*+0x20020d0  
 2008: a6 03 89 7d mtctr 12  
 200c: 20 04 80 4e bctr  
 ...  
  
0000000000002030 \<0000001b.long_branch.1c:2+8\>:  
 2030: f8 ff ff 49 b 0x2002028 \<high_target+0x8\>  
 0000000000002030: R_PPC64_REL24 *ABS*+0x2002028  
 ...

## REL 和 RELA

`.plt` 和 `.branch_lt` 的类型为 `SHT_NOBITS`，可能需要具有非零附加数的动态重定位。这使得 REL 对这两个节不可行。因此，当需要 `.plt` 或 `.branch_lt` 时，不能使用 `-z rel`。

## PPC64 ELFv1 函数描述符

在 ELFv1 ABI 中，TOC 指针（r2）由调用者而不是被调用者设置。这意味着外部函数调用需要同时更新程序计数器和 TOC 指针。

为了实现这一点，每个外部可见函数都有一个专用的函数描述符，存储在 `.opd` 节中。该描述符包含三个双字：

- 函数入口点地址。
- TOC 基址。
- 环境指针：由 Pascal 和 PL/1 等语言使用，但对于 C/C++ 为零。

调用站点使用一条 BL 指令后跟一条 NOP 指令。当被调用者可抢占时，链接器会创建一个 PLT 调用桩，并将 NOP 修补为 `ld r2, 40(r1)` 以恢复 TOC 指针，类似于 ELFv2。PLT 桩将当前 TOC 指针保存到栈上，加载函数入口点和 TOC 指针，然后跳转到函数入口点。

```plaintext
  bl 0000001b.plt_call.foo
  ld r2,40(r1)               # restore TOC pointer
  bl 0000001b.plt_call.foo
  ld r2,40(r1)               # restore TOC pointer

0000001b.plt_call.foo:
  std     r2,40(r1)          # save r2
  ld      r12,val(r2)        # load the function entry point
  mtctr   r12
  ld      r2,val+8(r2)       # set TOC pointer
  bctr                       # jump
```

r2 是被调用者保存的（call-preserved，即被调用者必须保留），这要求在 PLT 调用桩中进行 TOC 加载/恢复，因此[抑制了可抢占的尾调用](https://maskray.me/blog/2021-09-19-all-about-procedure-linkage-table#got-setup-is-expensive-without-pc-relative-addressing)。这是一个设计缺陷。从技术上讲，不可抢占的尾调用是可行的，但 GCC 似乎没有实现它。

调用一个不可抢占的函数使用 `R_PPC64_REL24` 重定位，链接器应将其解析为函数入口点。

函数符号的值（`st_value`）实际上是 `.opd` 节中函数描述符的地址。对于大多数与函数调用无关的重定位类型，链接器可以以相同的方式处理函数和数据符号。然而，对于函数调用使用的 `R_PPC_REL24`，链接器需要解析重定位，使其引用不可抢占函数的函数入口点。

编译器为每个编译单元生成 `.opd` 节，由链接器合并。

```plaintext
.section        ".opd","aw"
.align 3
foo:
  .quad   .L.foo,.TOC.@tocbase,0
bar:
  .quad   .L.bar,.TOC.@tocbase,0
```

另一个设计缺陷是编译器生成 `.opd` 节，然后由链接器合并。默认的垃圾回收规则会在任何函数描述符活跃时保留整个 `.opd`。相反，我们应该将每个函数描述符视为一个子节，可以独立丢弃。此外，与每个函数描述符关联的两个重定位是浪费的。

如果我们放弃函数符号值指向函数描述符的优势，并修复几个设计错误：

- 使 r2 成为调用者破坏的（call-clobbered）寄存器。
- 移除未使用的环境指针。
- 引入一个重定位来标识函数描述符，并移除编译器生成的 `.opd`。

我们基本上会得到一个 [FDPIC ABI](https://maskray.me/blog/2024-02-20-mmu-less-systems-and-fdpic)！
