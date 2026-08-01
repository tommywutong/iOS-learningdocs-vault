---
title: 探索链接器输出中的 section 布局
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-12-17-exploring-the-section-layout-in-linker-output'
original_language: en
published: 2023-12-17
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bb8d2db224324266'
translated: true
---

> 原文：[探索链接器输出中的 section 布局](https://maskray.me/blog/2023-12-17-exploring-the-section-layout-in-linker-output)　·　MaskRay (宋方睿)

[2023-12-17](https://maskray.me/blog/2023-12-17-exploring-the-section-layout-in-linker-output)

# 探索链接器输出中的 section 布局

2026 年 3 月更新。

本文介绍节布局，以及它与动态加载器和大页面之间的交互。

先来看一个 Linux x86-64 示例，其中的全局变量具有各种不同属性，例如只读与可写、零初始化与非零初始化等。

```c
#include <stdio.h>
const int ro = 1;
int w0, w1 = 1;
int *const pw0 = &w0;
int main() {
  printf("%d %d %d %p\n", ro, w0, w1, pw0);
}
```

```plaintext
% clang -c -fpie a.c
% clang -pie -fuse-ld=lld -Wl,-z,separate-loadable-segments a.o -o a
% objdump -wt a | grep -P 'main|w[01]|ro$'
00000000000010f0 g     F .text  000000000000002e              main
0000000000003044 g     O .bss   0000000000000004              w0
0000000000003010 g     O .data  0000000000000004              w1
000000000000058c g     O .rodata        0000000000000004              ro
0000000000002010 g     O .data.rel.ro   0000000000000008              pw0
% readelf -Wl a
...
Program Headers:
  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align
  PHDR           0x000040 0x0000000000000040 0x0000000000000040 0x000268 0x000268 R   0x8
  INTERP         0x0002a8 0x00000000000002a8 0x00000000000002a8 0x00001c 0x00001c R   0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x000000 0x0000000000000000 0x0000000000000000 0x000628 0x000628 R   0x1000
  LOAD           0x001000 0x0000000000001000 0x0000000000001000 0x000180 0x000180 R E 0x1000
  LOAD           0x002000 0x0000000000002000 0x0000000000002000 0x0001e0 0x001000 RW  0x1000
  LOAD           0x003000 0x0000000000003000 0x0000000000003000 0x000040 0x000048 RW  0x1000
  DYNAMIC        0x002018 0x0000000000002018 0x0000000000002018 0x0001a0 0x0001a0 RW  0x8
  GNU_RELRO      0x002000 0x0000000000002000 0x0000000000002000 0x0001e0 0x001000 R   0x1
  GNU_EH_FRAME   0x0005a0 0x00000000000005a0 0x00000000000005a0 0x00001c 0x00001c R   0x4
  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0
  NOTE           0x0002c4 0x00000000000002c4 0x00000000000002c4 0x000020 0x000020 R   0x4
...
```

（稍后会讨论 [`-Wl,-z,separate-loadable-segments`](#z-separate-loadable-segments)。）

可以看到，这些函数和全局变量被放置在不同的节中。

- `.rodata`：不含动态重定位的只读数据，在链接单元中保持不变
- `.text`：函数
- `.data.rel.ro`：与动态重定位关联的只读数据，在重定位解析后保持不变，属于 `PT_GNU_RELRO` 段
- `.data`：可写数据
- `.bss`：已知为零的可写数据

## 节与段的布局

TODO：以后可能会进一步介绍链接器如何布局节和段。

总之，链接器会将 `.data` 和 `.bss` 放在同一个 `PT_LOAD` 程序头（段）中，其余内容则放在不同的 `PT_LOAD` 段中。（这里有一些细微差别：如果使用 `-z noseparate-code`、lld 的 [`--no-rosegment`](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options#no-rosegment) 或 GNU ld 的 `--rosegment`，`.rodata` 和 `.text` 会被放在同一个 `PT_LOAD` 段中。）

各个 `PT_LOAD` 段具有不同的标志（`p_flags`）：`PF_R`、`PF_R|PF_X`、`PF_R|PF_W`。随后，动态加载器（也称为动态链接器）会调用 `mmap` 将文件映射到内存。各个内存区域（VMA）的内存权限与对应的段标志一致。

对于一个 `PT_LOAD` 段，其关联的内存区域起始于 `alignDown(p_vaddr, pagesize)`，结束于 `alignUp(p_vaddr+p_memsz, pagesize)`。

```plaintext
    Start Addr           End Addr       Size     Offset  Perms  objfile
0x555555554000     0x555555555000     0x1000        0x0  r--p   /tmp/c/a
0x555555555000     0x555555556000     0x1000     0x1000  r-xp   /tmp/c/a
0x555555556000     0x555555557000     0x1000     0x2000  r--p   /tmp/c/a
0x555555557000     0x555555558000     0x1000     0x3000  rw-p   /tmp/c/a
```

假设页面大小为 4096 字节。下面计算 `alignDown(p_vaddr, pagesize)`，并将结果与“起始地址”并列显示：1  
2  
3  
4  
5  
起始地址 alignDown(p_vaddr, pagesize)  
0x555555554000 0x0000000000000000
0x555555555000 0x0000000000001000
0x555555556000 0x0000000000002000
0x555555557000 0x0000000000003000

可以看到，起始地址等于基地址加上 `alignDown(p_vaddr, pagesize)`。

当存在 `SHT_NOTE` section 时，它们会被放在开头，以便更有可能被包含在核心文件中。在 Linux 内核中，2007 年的提交 [添加 MMF_DUMP_ELF_HEADERS](https://git.kernel.org/linus/82df39738ba9e02c057fa99b7461a56117d36119) 与此相关。

## [`--no-rosegment`](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options#no-rosegment)

此选项要求 lld 合并只读段和 RX 段，从而减少输出文件在运行时占用的地址空间。

```plaintext
    Start Addr           End Addr       Size     Offset  Perms  objfile
0x555555554000     0x555555555000     0x1000        0x0  r-xp   /tmp/c/a
0x555555555000     0x555555556000     0x1000        0x0  r--p   /tmp/c/a
0x555555556000     0x555555557000     0x1000     0x1000  rw-p   /tmp/c/a
```

GNU ld 也实现了 `--rosegment`/`--no-rosegment`（两者默认均关闭），但由于节的排列顺序不同，其语义与 lld 不同。

lld 将 `.rodata` 放在 `.text` **之前**，因此 `--no-rosegment` 会自然地将前面的 R 段合并到 R+X 段中。GNU ld 将 `.rodata` 放在 `.text` **之后**（位于单独的 R 段中），因此 `--rosegment` 会把 `.rodata` 移到 `.text` 之前，再将二者合并成 R+X 段。实际上，lld 的 `--no-rosegment` 与 GNU ld 的 `--rosegment` 结果相同（段更少），只是二者的默认布局相反。

注意，GNU ld 的 `--no-rosegment` 与 `-z separate-code` 结合使用时没有明显效果：输出仍有 4 个段（R、R+X、R、RW），因为 `.rodata` 位于 `.text` 之后，无法向前合并。

## MAXPAGESIZE

页面是内存展示不同权限的粒度单位，在一个页面内，我们不能有不同权限。使用之前的例子，其中 `p_align` 为 4096，如果页面大小更大，例如 65536 字节，程序可能会崩溃。

通常，动态加载器会在内核分配的特定地址为第一个 `PT_LOAD` segment（`PF_R`）分配内存。后续的 `PT_LOAD` segment 随后会覆盖之前的内存区域。因此，某些代码页或重要的全局变量可能会被垃圾数据替换，导致崩溃。

那么，如何创建一个能适应不同页面大小的链接单元？只需确定最大页面大小（例如 2097152），然后将 `-z max-page-size=2097152` 传给链接器。链接器会把各个 `PT_LOAD` 段的 `p_align` 设为 MAXPAGESIZE。

```plaintext
Program Headers:
  Type           Offset   VirtAddr           PhysAddr           FileSiz  MemSiz   Flg Align
  PHDR           0x000040 0x0000000000000040 0x0000000000000040 0x000268 0x000268 R   0x8
  INTERP         0x0002a8 0x00000000000002a8 0x00000000000002a8 0x00001c 0x00001c R   0x1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
  LOAD           0x000000 0x0000000000000000 0x0000000000000000 0x000640 0x000640 R   0x200000
  LOAD           0x200000 0x0000000000200000 0x0000000000200000 0x000180 0x000180 R E 0x200000
  LOAD           0x400000 0x0000000000400000 0x0000000000400000 0x0001e0 0x001000 RW  0x200000
  LOAD           0x600000 0x0000000000600000 0x0000000000600000 0x000040 0x000048 RW  0x200000
  DYNAMIC        0x400018 0x0000000000400018 0x0000000000400018 0x0001a0 0x0001a0 RW  0x8
  GNU_RELRO      0x400000 0x0000000000400000 0x0000000000400000 0x0001e0 0x001000 R   0x1
  GNU_EH_FRAME   0x0005b8 0x00000000000005b8 0x00000000000005b8 0x00001c 0x00001c R   0x4
  GNU_STACK      0x000000 0x0000000000000000 0x0000000000000000 0x000000 0x000000 RW  0
  NOTE           0x0002c4 0x00000000000002c4 0x00000000000002c4 0x000038 0x000038 R   0x4
```

在链接器脚本中，可以通过 `CONSTANT(MAXPAGESIZE)` 获取 `max-page-size`。

补充一点：如果需要在页面更大的系统上运行预构建的可执行文件，可以合并 `PT_LOAD` 段及其权限来修改该文件。这样很可能产生一个相当大的 RWX `PT_LOAD` 段，令人联想到 OMAGIC。

## 过度对齐的段

可以使用 `aligned` 属性增大单个 `PT_LOAD` 段的 `p_align` 值。当该值超过页面大小时，问题随之而来：应由内核加载器还是动态加载器确定合适的基地址，以满足这一对齐要求？

2020 年，Linux 内核加载器决定[按照最大的 `p_align` 对齐基地址](https://git.kernel.org/linus/ce81bb256a224259ab686742a6284930cbe4f1fa)。这有助于对映射文件使用[透明大页面](#transparent-huge-pages-for-mapped-files)，代价则是地址随机化程度降低。

```plaintext
% cat align.c
#include <stdio.h>
__attribute__((aligned(A))) int aligned;
int main() { printf("%p\n", &aligned); }
% cc -DA=4096 align.c -o align && ./align
0x55e994c13000
% cc -DA=2097152 align.c -o align && ./align
0x55639a400000
```

用户态动态加载器是否也应该这样做？如果是，对齐要求大于页面大小的变量确实会获得相应的对齐。截至 glibc 2.35，它已经[采用了同样的做法](https://sourceware.org/PR28676)。

另一方面，传统的解释规定，对齐要求大于页面大小的变量是无效的。大多数其他动态加载器没有实现这个特定逻辑，这会有一些开销。

## `-z separate-loadable-segments`

在前面使用 `-z separate-loadable-segments` 的示例中，各个 `PT_LOAD` 段的 `p_vaddr` 都是 MAXPAGESIZE 的倍数。通用 ABI 规定：“可加载进程段的 p_vaddr 与 p_offset 必须以页面大小为模同余。”

> p_offset - 此成员给出段第一个字节在文件中的偏移量。
>  
> p_vaddr - 此成员给出段第一个字节在内存中的虚拟地址。

这一对齐要求与 `mmap` 文档一致。例如，Linux man-pages 规定：“offset 必须是 `sysconf(_SC_PAGE_SIZE)` 返回的页面大小的倍数。”

`p_offset` 值也都是 MAXPAGESIZE 的倍数。布局完一个 `PT_LOAD` 段后，链接器必须在末尾补零，使下一个 `PT_LOAD` 段从 MAXPAGESIZE 的整数倍位置开始。

不过，对齐填充会浪费空间。我们可以使用不同的 MAXPAGESIZE 和对齐设置来链接 `a.o`：`-z noseparate-code`、`-z separate-code`、`-z separate-loadable-segments`。

```sh
clang -pie -fuse-ld=lld -Wl,-z,noseparate-code a.o -o a0.4096
clang -pie -fuse-ld=lld -Wl,-z,noseparate-code,-z,max-page-size=65536 a.o -o a0.65536
clang -pie -fuse-ld=lld -Wl,-z,noseparate-code,-z,max-page-size=2097152 a.o -o a0.2097152

clang -pie -fuse-ld=lld -Wl,-z,separate-code a.o -o a1.4096
clang -pie -fuse-ld=lld -Wl,-z,separate-code,-z,max-page-size=65536 a.o -o a1.65536
clang -pie -fuse-ld=lld -Wl,-z,separate-code,-z,max-page-size=2097152 a.o -o a1.2097152

clang -pie -fuse-ld=lld -Wl,-z,separate-loadable-segments a.o -o a2.4096
clang -pie -fuse-ld=lld -Wl,-z,separate-loadable-segments,-z,max-page-size=65536 a.o -o a2.65536
clang -pie -fuse-ld=lld -Wl,-z,separate-loadable-segments,-z,max-page-size=2097152 a.o -o a2.2097152
```

```plaintext
% stat -c %s a0.4096 a0.65536 a0.2097152
6168
6168
6168
% stat -c %s a1.4096 a1.65536 a1.2097152
12392
135272
4198504
% stat -c %s a2.4096 a2.65536 a2.2097152
16120
200440
6295288
```

我们可以推导出两个性质：

- 在同一个 MAXPAGESIZE 下，我们有 `size(noseparate-code) < size(separate-code) < size(separate-loadable-segments)`.
- 对于 `-z noseparate-code`，增加 MAXPAGESIZE 不会改变输出大小。

AArch64 和 PowerPC64 的默认 MAXPAGESIZE 为 65536。保持 `-z noseparate-code` 的默认设置可以确保它们不会经历不必要的体积增大。

## `-z noseparate-code`

`-z noseparate-code` 是如何工作的？我们用一个例子来说明。

只读 `PT_LOAD` 段末尾的地址是 0x628。下一个段不从 `alignUp(0x628, MAXPAGESIZE) = 0x1000` 开始，而从 `alignUp(0x628, MAXPAGESIZE) + 0x628 % MAXPAGESIZE = 0x1628` 开始。由于 `.text` 节的对齐值（`sh_addralign`）为 16，实际从 0x1630 开始。地址虽然前移得超出必要范围，但文件偏移（以 MAXPAGESIZE 为模与地址同余）可以缩减为 0x630，仅比前一节的末尾多 8 字节（来自对齐填充）。

接着，可执行 `PT_LOAD` 段末尾的地址是 0x17b0。下一个段不从 `alignUp(0x17b0, MAXPAGESIZE) = 0x2000` 开始，而从 `alignUp(0x17b0, MAXPAGESIZE) + 0x17c0 % MAXPAGESIZE = 0x27b0` 开始。地址同样前移得超出必要范围，但文件偏移可以缩减为 0x7b0，恰好位于前一节的末尾。

```plaintext
% readelf -WSl a0.4096
...
  [Nr] Name              Type            Address          Off    Size   ES Flg Lk Inf Al
  [ 0]                   NULL            0000000000000000 000000 000000 00      0   0  0
  [ 1] .interp           PROGBITS        00000000000002a8 0002a8 00001c 00   A  0   0  1
  ...
  [12] .eh_frame         PROGBITS        00000000000005c0 0005c0 000068 00   A  0   0  8
  [13] .text             PROGBITS        0000000000001630 000630 00011e 00  AX  0   0 16
  ...
  [16] .plt              PROGBITS        0000000000001780 000780 000030 00  AX  0   0 16
  [17] .fini_array       FINI_ARRAY      00000000000027b0 0007b0 000008 08  WA  0   0  8
  ...
  [20] .dynamic          DYNAMIC         00000000000027c8 0007c8 0001a0 10  WA  7   0  8
  [21] .got              PROGBITS        0000000000002968 000968 000028 00  WA  0   0  8
  [22] .relro_padding    NOBITS          0000000000002990 000990 000670 00  WA  0   0  1
  [23] .data             PROGBITS        0000000000003990 000990 000014 00  WA  0   0  8
  ...
  [26] .bss              NOBITS          00000000000039d0 0009d0 000008 00  WA  0   0  4
...
  LOAD           0x000000 0x0000000000000000 0x0000000000000000 0x000628 0x000628 R   0x1000
  LOAD           0x000630 0x0000000000001630 0x0000000000001630 0x000180 0x000180 R E 0x1000
  LOAD           0x0007b0 0x00000000000027b0 0x00000000000027b0 0x0001e0 0x000850 RW  0x1000
  LOAD           0x000990 0x0000000000003990 0x0000000000003990 0x000040 0x000048 RW  0x1000
  DYNAMIC        0x0007c8 0x00000000000027c8 0x00000000000027c8 0x0001a0 0x0001a0 RW  0x8
  GNU_RELRO      0x0007b0 0x00000000000027b0 0x00000000000027b0 0x0001e0 0x000850 R   0x1
```

从第一个 RW `PT_LOAD` 段过渡到第二个时，`-z separate-code` 会使用这一技巧，而 `-z separate-loadable-segments` 不会。

## 当 MAXPAGESIZE 大于实际页面大小时

让我们考虑两个相邻的 `PT_LOAD` segment。与第一个 segment 关联的内存区域结束于 `alignUp(load[i].p_vaddr+load[i].p_memsz, pagesize)`，而与第二个 segment 关联的内存区域起始于 `alignDown(load[i+1].p_vaddr, pagesize)`。当实际页面大小等于 MAXPAGESIZE 时，这两个地址是相同的。然而，如果实际页面大小更小，这些地址之间就会出现一个间隙。

一个典型的链接单元通常呈现三个间隙。这些间隙可能未被映射，也可能已被映射。当被映射时，它们需要 Linux 内核中的 `struct vm_area_struct` 对象。截至 Linux 6.3.13，`struct vm_area_struct` 的大小为 152 字节。例如，10000 个已映射的目标文件将需要 `10000 * 3 * sizeof(struct vm_area_struct) = 4,560,000 bytes`，这意味着相当大的内存占用空间。你可以参考 [Extra struct vm_area_struct with ---p created when PAGE_SIZE \< max-page-size](https://sourceware.org/bugzilla/show_bug.cgi?id=31076).

动态加载器通常使用 `mmap` 调用 `PROT_READ`，覆盖整个文件，然后使用 `mmap` 和相应标志进行多次 `MAP_FIXED` 调用。当动态加载器（如 musl）不处理间隙时，这些间隙会保留 `r--p` 权限。然而，在 glibc 的 `elf/dl-map-segments.h` 中，`has_holes` 代码会使用 `mprotect` 将权限从 `r--p` 转换为 `---p`.

虽然 `---p` 可能被视为一项安全增强，但就个人而言，我认为它不会显著影响可利用性。虽然 `r-xp` 区域中可能存在大量 gadgets，但减少 `r--p` 区域中的 gadgets 似乎影响不大。([https://isopenbsdsecu.re/mitigations/rop_removal/](https://isopenbsdsecu.re/mitigations/rop_removal/))

### 取消映射间隙

在 Linux 内核加载可执行文件及其解释器（如果存在）的过程中（`fs/binfmt_elf.c`），间隙会被取消映射，从而释放一个 `struct vm_area_struct` 对象。在动态加载器中实现类似的方法可以带来相同的节省。

然而，取消映射间隙会带来风险，即未来不相关的 `mmap` 可能会占用该间隙：

```plaintext
564d8e90f000-564d8e910000 r--p 00000000 08:05 2519504        /sample/build/main
   ================ an unrelated mmap may be placed in the gap
564d8e91f000-564d8e920000 r-xp 00010000 08:05 2519504        /sample/build/main
```

目前尚不清楚可能出现不相关的 mmap 是否被视为安全方面的退化。就个人而言，我认为这不会构成重大问题，因为程序不会访问这些间隙。当输入重定位到链接器使用具有 in-bounds 加数的符号（例 e.g 如，当 x 被定义为相对于某个输入段时，我们知道 `R_X86_64_PC32(x)` 必须 in-bounds).

然而，某些程序可能期望文件的映射区域是连续的（例如，当 glibc 的 `link_map::l_contiguous` 设置为 1 时）。如果攻击者能够确保一个映射位于间隙内而不是文件外部，这种选择是否会使程序变得可利用？在我看来，他们可以通过文件外部的映射实现同样的目的。

话虽如此，在与单个文件描述符关联的映射之间出现一个无关的映射仍然很奇怪，因此最好尽可能避免这种情况。

### 扩展内存区域以覆盖间隙

这似乎是最佳的解决方案。

在创建内存区域时，我们不将结束地址设置为 `alignUp(load[i].p_vaddr+load[i].p_memsz, pagesize)`，而是将结束地址扩展到 `min(alignDown(min(load[i+1].p_vaddr), pagesize), alignUp(file_end_addr, pagesize))`.

```plaintext
564d8e90f000-**564d8e91f000** r--p 00000000 08:05 2519504        /sample/build/main  (the end is extended)
564d8e91f000-564d8e920000 r-xp 00010000 08:05 2519504        /sample/build/main
```

对于最后一个 `PT_LOAD` 段，我们也可以直接使用 `alignDown(min(load[i+1].p_vaddr), pagesize)` 并忽略 `alignUp(file_end_addr, pagesize))`。访问超出文件支撑范围之外的字节将触发一个 `SIGBUS` 信号。

### 一个新的链接器选项？

我个人更倾向于区域结束地址扩展的方法。我也曾思考过这是否属于链接器的职责范围。这样的更改看起来有些侵入性且不美观。如果链接器扩展 p_memsz 的结束地址以覆盖间隙，是否也应该扩展 p_filesz？

- 如果不扩展，我们就创建一个 pPT_LOADfilesz/p_memsz 不是用于 _ 的 BSS，这很奇怪。
- 如果扩展，我们就会得到一个包含重叠文件偏移范围的输出文件，这也同样奇怪。

此外，一个结束地址不由任何段支撑的 PT_LOAD 也很不寻常。我担心许多二进制操作工具可能无法正确处理这种情况。使用链接器脚本可以有意创建不连续的地址范围。我担心链接器可能无法通过关于 p_filesz/p_memsz 的智能逻辑来区分这些情况。

这个功能请求似乎属于加载器的范畴，并且像页面大小这样的特定信息只有加载器才能访问。我相信加载器更适合处理这个任务。

## 映射文件的透明巨页

某些程序通过使用透明巨页来优化其对有限的转译查找缓冲区的使用。当 Linux 内核加载可执行文件时，它会考虑 TLB 字段来创建一个内存区域。如果 `p_align` 是 4096，内存区域将从一个 4096 的倍数开始，但不一定是巨页的倍数。`p_align` 是 4096，内存区域将从一个 4096 的倍数开始，但不一定是巨页的倍数。

映射文件的透明巨页有几个要求，包括：

- 内存区域的起始地址和起始文件偏移量与巨页对齐（`include/linux/huge_mm.h:transhuge_vma_suitable`).
- `CONFIG_READ_ONLY_THP_FOR_FS` 已启用（`scripts/config -e TRANSPARENT_HUGEPAGE -e TRANSPARENT_HUGEPAGE_MADVISE -e READ_ONLY_THP_FOR_FS`)
- ~~没有 VMA 标志 `VM_EXEC` 标志~~（我已[移除了 v6.8 的这个条件](https://git.kernel.org/linus/7fbb5e188248c50f737720825da1864ce42536d1))
- 该文件未出于写入目的而打开

当调用 `madvise(addr, len, MADV_HUGEPAGE)` 时，内核代码路径为 `do_madvise -> madvise_vma_behavior -> hugepage_madvise -> khugepaged_enter_vma -> thp_vma_allowable_order+__khugepaged_enter`.

为确保 `addr-fileoff` 是巨页的倍数，我们应该使用 `-z max-page-size=` 并将值设为巨页大小来链接可执行文件。

在具有 `VM_EXEC` 要求的内核（v6.8 之前）中，如果我们想从 ELF 头部将文件重新映射为巨页，我们必须向 `--no-rosegment` 指定 ld.lld.

使用 `c++ -fuse-ld=lld -Wl,-z,max-page-size=2097152` 构建以下程序并运行它。我们暂时不定义 `COLLAPSE`。
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
24  
25  
26  
27  
28  
29  
30  
31  
32  
33  
34  
35  
36  
37  
38  
39  
40  
41  
42  
43  
44  
45  
46  
47  
48  
49  
50  
51  
52  
53  
54  
55  
56  
57  
58  
59  
60  
61  
62  
63  
64  
65  
66  
67  
68  
69  
70  
71  
72  
73  
74  
75  
76  
77  
78  
79  
80  
81  
82  
83  
84  
85  
86  
87  
88  
89  
90  
91  
92  
93  
94  
95  
96  
97  
98  
99  
#include \<err.h\>  
#include \<errno.h\>  
#include \<fcntl.h\>  
#include \<linux/kernel-page-flags.h\>  
#include \<stddef.h\>  
#include \<stdint.h\>  
#include \<stdio.h\>  
#include \<stdlib.h\>  
#include \<string.h\>  
#include \<sys/mman.h\>  
#include \<unistd.h\>  
  
// 改编自 https://mazzo.li/posts/check-huge-page.html  
// 普通页面，4KiB
#define PAGE_SIZE (1 \<\< 12)  
// 巨页，2MiB
#define HPAGE_SIZE (1 \<\< 21)  
  
// 参见 \<https://www.kernel.org/doc/Documentation/vm/pagemap.txt\> 了解
// 这些位掩码所指的格式
#define PAGEMAP_PRESENT(ent) (((ent) & (1ull \<\< 63)) != 0)  
#define PAGEMAP_PFN(ent) ((ent) & ((1ull \<\< 55) - 1))  
  
extern char __ehdr_start[];
__attribute__((used)) const char pad[HPAGE_SIZE] = {};  
  
// 检查 `ptr` 指向的页面是否为巨页。假设 `ptr` 已经
// 被分配。
static void check_huge_page(void *ptr) {  
 if (getuid())  
 return warnx("not root; skip KPF_THP check");  
 int pagemap_fd = open("/proc/self/pagemap", O_RDONLY);  
 if (pagemap_fd \< 0)  
 errx(1, "could not open /proc/self/pagemap: %s", strerror(errno));  
 int kpageflags_fd = open("/proc/kpageflags", O_RDONLY);  
 if (kpageflags_fd \< 0)  
 errx(1, "could not open /proc/kpageflags: %s", strerror(errno));  
  
 // 每个条目为 8 字节长
 uint64_t ent;
 if (pread(pagemap_fd, &ent, sizeof(ent), ((uintptr_t)ptr) / PAGE_SIZE * 8) != sizeof(ent))  
 errx(1, "could not read from pagemap\\n");  
  
 if (!PAGEMAP_PRESENT(ent))
 errx(1, "page not present in /proc/self/pagemap, did you allocate it?\\n");  
 if (!PAGEMAP_PFN(ent))
 errx(1, "page frame number not present, run this program as root\\n");  
  
 uint64_t flags;
 if (pread(kpageflags_fd, &flags, sizeof(flags), PAGEMAP_PFN(ent) \<\< 3) != sizeof(flags))  
 errx(1, "could not read from kpageflags\\n");  
 if (!(flags & (1ull \<\< KPF_THP)))  
 errx(1, "could not allocate huge page\\n");  
 if (close(pagemap_fd) \< 0)  
 errx(1, "could not close /proc/self/pagemap: %s", strerror(errno));  
 if (close(kpageflags_fd) \< 0)  
 errx(1, "could not close /proc/kpageflags: %s", strerror(errno));  
}  
  
int main() {  
 printf("__ehdr_start: %p\\n", __ehdr_start);  
 int ret, tries = 2;  
#ifdef COLLAPSE // 使用 Linux 6.1 MADV_COLLAPSE  
 do {
 ret = madvise(__ehdr_start, HPAGE_SIZE, MADV_COLLAPSE);  
 } while (ret && errno == EAGAIN && --tries);  
 printf("madvise(MADV_COLLAPSE): %d\\n", ret);  
 if (ret) {  
 ret = madvise(__ehdr_start, HPAGE_SIZE, MADV_HUGEPAGE);  
 if (ret)
 err(1, "madvise");  
 }  
#else
 ret = madvise(__ehdr_start, HPAGE_SIZE, MADV_HUGEPAGE);  
 if (ret)
 err(1, "madvise");  
#endif
  
 size_t size = HPAGE_SIZE;  
 char *buf = (char *)aligned_alloc(HPAGE_SIZE, size);  
 madvise(buf, 2 \<\< 20, MADV_HUGEPAGE);  
 *((volatile char *)buf);  
 check_huge_page(buf);  
  
 int fd = open("/proc/self/maps", O_RDONLY);  
 read(fd, buf, HPAGE_SIZE);  
 write(STDOUT_FILENO, buf, strstr(buf, "[stack]\\n") - buf + 8);  
 close(fd);  
  
#ifndef COLLAPSE  
 fd = open("/sys/kernel/mm/transparent_hugepage/khugepaged/scan_sleep_millisecs", O_RDONLY);  
 read(fd, buf, 32);  
 close(fd);  
 usleep(atoi(buf) * 1000);  
#endif
  
 memcpy(buf, __ehdr_start, HPAGE_SIZE);  
 check_huge_page(__ehdr_start);  
}

输出看起来像这样：
2  
3  
4  
5  
6  
7  
8  
% g++ test.cc -o ~/tmp/test -O2 -fuse-ld=lld -Wl,-z,max-page-size=2097152 && sudo ~/tmp/test  
__ehdr_start: 0x55f3b1c00000  
55f3b1c00000-55f3b1e00000 r--p 00000000 103:03 555277119 /home/ray/tmp/test  
55f3b1e00000-55f3b1e01000 r--p 00200000 103:03 555277119 /home/ray/tmp/test  
55f3b2000000-55f3b2002000 r-xp 00200000 103:03 555277119 /home/ray/tmp/test  
55f3b2201000-55f3b2202000 r--p 00201000 103:03 555277119 /home/ray/tmp/test  
55f3b2401000-55f3b2402000 rw-p 00201000 103:03 555277119 /home/ray/tmp/test  
55f3b3a9a000-55f3b3abb000 rw-p 00000000 00:00 0 [heap]

感谢周洲仪帮助我理解 khugepaged 的行为。

`usleep` 给 khugepaged 一个机会来折叠页面（`hpage_collapse_scan_file => collapse_file => retract_page_tables => pmdp_collapse_flush`）。在幸运的情况下，当此次折叠发生时，并且下一个页面错误被触发（`memcpy(buf, __ehdr_start, HPAGE_SIZE)`），内核将用巨页填充 `pmd`（`handle_page_fault ...=> handle_pte_fault ...=> do_fault_around => filemap_map_pages ...=> do_set_pmd => set_pmd_at`).

然而，在不走运的情况下，`check_huge_page(__ehdr_start)` 将失败并显示 `could not allocate huge page`. `scan_sleep_millisecs` 默认值为 10000（10 秒）。减小该值会增加幸运情况发生的可能性。

Linux 6.1 引入了 `MADV_COLLAPSE` 以尝试将内存范围映射的原生页面同步合并为透明大页面（THP）。虽然成功无法保证，但成功合并后无需等待 khugepaged 守护进程（`madvise_collapse => hpage_collapse_scan_file => collapse_file => retract_page_tables => pmdp_collapse_flush`）。在反复 `MADV_COLLAPSE` 失败的情况下，可以使用 `MADV_HUGEPAGE` 的 fallback 机制。1  
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
% g++ -static -DCOLLAPSE test.cc -o test -O2 -fuse-ld=lld -Wl,-z,max-page-size=2097152  
% sudo ./test  
__ehdr_start: 0x200000  
madvise(MADV_COLLAPSE): -1  
...  
test: could not allocate huge page  
% sudo ./test  
__ehdr_start: 0x55f3b1c00000  
madvise(MADV_COLLAPSE): 0  
00200000-00429000 r--p 00000000 fd:03 260 /root/test  
00628000-0069f000 r-xp 00228000 fd:03 260 /root/test  
0089e000-008a3000 r--p 0029e000 fd:03 260 /root/test  
00aa2000-00aa5000 rw-p 002a2000 fd:03 260 /root/test  
00aa5000-00aab000 rw-p 00000000 00:00 0  
01800000-01822000 rw-p 00000000 00:00 0 [heap]  
7fd141600000-7fd141800000 rw-p 00000000 00:00 0  
7fd141800000-7fd141a00000 rw-p 00000000 00:00 0  
7fd141a00000-7fd141a01000 rw-p 00000000 00:00 0  
7ffe69edf000-7ffe69f00000 rw-p 00000000 00:00 0 [stack]

在使用 `--rosegment` 的 `-z noseparate-code` 布局中（这是 lld 的默认设置，会保持 R 与 R+X 分离），R+X 段的起始偏移没有按大页面大小对齐。Linux 内核的 THP 实现不支持这种未对齐的段。使用 `--no-rosegment`（lld）将 R 与 R+X 合并成一个从偏移 0 开始的段，即可避免此问题。

在 `-z noseparate-code` 布局中，如果目标是只把代码而非 rodata 放入大页面，代码会位于页面中部，rodata 可能浪费半个大页面。改用 `-z separate-code` 可以重新利用这半个大页面，却会增大文件。两者很难兼顾。一种可能的方案是使用 `fallocate(FALLOC_FL_PUNCH_HOLE)`，但这会增加链接器的复杂度，而且更像是绕过内核限制。更理想的做法是让文件支持的大页面不再要求文件偏移按大页面边界对齐。

### RELRO 的成本

为了容纳 `PT_GNU_RELRO`，运行时链接器映射程序后，`RW` 区域将具有两个权限。虽然 GNU ld 提供了一个由动态加载器拆分的 RW 段，但 lld 使用了两个显式的 RW `PT_LOAD` 段。重定位解析后，lld 和 GNU ld 的效果类似。

感兴趣的话，可以阅读我关于 GNU ld [因 RELRO 导致文件增大](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options#z-relro)的笔记。

由于 RELRO 的存在，覆盖两个 RW `PT_LOAD` 段至少需要 2 个（大）页面；相比之下，没有 RELRO 时至少只需 1 个。这意味着最多可能浪费 MAXPAGESIZE-1 字节，而这些空间原本可以覆盖更多数据。

如今，RELRO 被视为安全基线，移除它可能会让注重安全的人感到不安。
