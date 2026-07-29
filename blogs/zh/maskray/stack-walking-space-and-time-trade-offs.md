---
title: '栈遍历：空间与时间的权衡'
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2025-10-26-stack-walking-space-and-time-trade-offs'
original_language: en
published: 2025-10-26
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:614c73e313699e6b'
translated: true
---

> 原文：[Stack walking: space and time trade-offs](https://maskray.me/blog/2025-10-26-stack-walking-space-and-time-trade-offs)　·　MaskRay (宋方睿)

[2025-10-26](https://maskray.me/blog/2025-10-26-stack-walking-space-and-time-trade-offs)

# 栈遍历：空间与时间的权衡

在大多数 Linux 平台（AArch32 除外，它使用 `.ARM.exidx`）上，[C++ 异常处理](https://maskray.me/blog/2020-12-12-c++-exception-handling-abi) 和 [栈展开（stack unwinding）](https://maskray.me/blog/2020-11-08-stack-unwinding) 需要 DWARF `.eh_frame` 来恢复被调用者保存的寄存器。虽然 `.eh_frame` 可以用于调用栈记录，但它常因运行时开销而受到批评。作为一种替代方案，开发者可以启用帧指针（frame pointer），或者采用 SFrame——一种专为性能分析（profiling）设计的新格式。本文研究了在构建几个 LLVM 可执行文件时，启用非 DWARF 栈遍历机制所带来的空间开销。

运行时性能分析将在未来的更新中补充。

## 栈遍历机制

以下是 x86-64 可用机制的概览：

- **帧指针**：快速且简单，但会占用一个寄存器。
- **DWARF `.eh_frame`**：功能全面但较慢，支持 C++ 异常处理等额外功能。
- **SFrame**：这是一种新的实验性格式，仅支持性能分析（profiling）。调试和 C++ 异常处理仍需 `.eh_frame`。详情请查看 [关于 SFrame 的评论](https://maskray.me/blog/2025-09-28-remarks-on-sframe)。
- **LLVM 的紧凑展开格式（Compact Unwinding Format）**：一种空间效率极高的格式，[由 Apple 为 Mach-O 二进制文件实现](https://faultlore.com/blah/compact-unwinding/)。在 llvm、lld/MachO 和 libunwind 中有实现。支持 x86-64 和 AArch64。这种格式基本上可以替代 DWARF CFI，但部分条目仍需 DWARF 转义（escape）（`__eh_frame` 段（section）会很小）。OpenVMS 为他们的 x86-64 移植版修改了此格式。
- **x86 最后分支记录（Last Branch Record, LBR）**：一种硬件特性，可以捕获有限数量的最近分支历史（Skylake+ 上最多 32 条）。当配置为跟踪分支以用于 SamplePGO 时，其有限的深度意味着它无法可靠地捕获深层栈回溯。传统上只存在于 Intel 平台，但 AMD Zen 4 已实现了 [最后分支记录扩展版本 2（LbrExtV2）](https://lkml.kernel.org/lkml/b6bb0abaa8a54c0b6d716344700ee11a1793d709.1660211399.git.sandipan.das@amd.com/T/)。
- **控制流强制技术（Control-flow Enforcement Technology, CET）影子栈（Shadow Stack）**：这种硬件安全加固特性可用于获取栈回溯。虽然会引入一些开销，但它提供了按进程启用的灵活性。

## 空间开销分析

### 帧指针的大小影响

对于大多数架构，GCC 在 `-O` 编译时默认使用 `-fomit-frame-pointer`，以释放一个寄存器供通用使用。要启用帧指针，需指定 `-fno-omit-frame-pointer`，这会保留帧指针寄存器（例如 x86-64 上的 `rbp`），并在函数序言（prologue）和尾声（epilogue）中生成 `push`/`pop` 指令。

对于叶函数（leaf function）（不调用其他函数的函数），虽然为了保持一致性仍应保留帧指针寄存器，但 `push`/`pop` 操作通常是不必要的。编译器提供了 `-momit-leaf-frame-pointer`（具有目标相关的默认值）来减少代码大小。

此优化的可行性取决于目标架构：

- 在 AArch64 上，返回地址可在链接寄存器（Link Register, X30）中获得。直接调用者可以通过检查 X30 获取，因此 `-momit-leaf-frame-pointer` 不会影响展开。
- 在 x86-64 上，执行序言指令后，返回地址存储在 RSP 加上一个偏移量处。展开器（unwinder）需要知道栈帧大小才能检索返回地址，或者它必须利用 DWARF 信息获取叶帧，然后切换到帧指针链来处理父帧。

除了这个架构上的考虑，在 x86-64 上使用 `-momit-leaf-frame-pointer` 还有其他实际原因：

- 许多手写的汇编实现（包括大量 glibc 函数）没有建立帧指针，无论怎样都会在帧指针链中造成缺口。
- 在序言指令序列 `push rbp; mov rbp, rsp` 中，第一条指令执行后，RBP 尚未引用当前的栈帧。当启用收缩包装（shrink-wrapping）优化时，RBP 仍持有旧值的指令区间会变大，从而增加了帧指针不可靠的时间窗口。

考虑到这些权衡，出现了三种常见的配置：

- 省略 FP：`-fomit-frame-pointer -momit-leaf-frame-pointer`（开销最小）
- 保留 FP，但移除叶函数的 FP push/pop：`-fno-omit-frame-pointer -momit-leaf-frame-pointer`（帧指针链省略叶帧）
- 保留 FP：`-fno-omit-frame-pointer -mno-omit-leaf-frame-pointer`（完整的帧指针链，开销最大）

大小影响因程序而异。以下是一个[用于比较段大小的 Ruby 脚本 `section_size.rb`](https://github.com/MaskRay/object-file-size-analyzer/blob/master/section_size.rb)：

```plaintext
% ~/Dev/object-file-size-analyzer/section_size.rb /tmp/out/custom-{none,nonleaf,all}/bin/{llvm-mc,opt}
Filename                            |       .text size |        EH size |  VM size | VM increase
------------------------------------+------------------+----------------+----------+------------
/tmp/out/custom-none/bin/llvm-mc    |  2114687 (23.7%) |  367992 (4.1%) |  8914057 |           -
/tmp/out/custom-nonleaf/bin/llvm-mc |  2124143 (24.0%) |  301688 (3.4%) |  8856713 |       -0.6%
/tmp/out/custom-all/bin/llvm-mc     |  2149535 (24.0%) |  362408 (4.1%) |  8942729 |       +0.3%
/tmp/out/custom-none/bin/opt        | 39018511 (70.2%) | 4561112 (8.2%) | 55583965 |           -
/tmp/out/custom-nonleaf/bin/opt     | 38879897 (71.4%) | 3542288 (6.5%) | 54424789 |       -2.1%
/tmp/out/custom-all/bin/opt         | 38980905 (71.0%) | 3888624 (7.1%) | 54871285 |       -1.3%
```

例如，`llvm-mc` 主要由只读数据（read-only data）主导，使得 `.text` 的相对百分比非常小，因此帧指针对 VM 大小的影响微乎其微。（"VM size" 是 bloaty 使用的一个指标，表示 `PT_LOAD` 段的总 `p_memsz` 大小，不含 [对齐填充](https://maskray.me/blog/2023-12-17-exploring-the-section-layout-in-linker-output)。）正如所料，随着更多函数建立帧指针链，`llvm-mc` 变得更大。然而，`opt` 在启用 `-fno-omit-frame-pointer` 时反而**变得更小**——这是一个反直觉的结果，需要解释。

在没有帧指针的情况下，编译器使用 RSP 相对寻址（RSP-relative addressing）来访问栈对象。当使用寄存器间接 + disp8/disp32 寻址模式时，RSP 需要一个额外的 SIB 字节，而 RBP 则不需要。对于访问许多局部变量的大型函数，较短的 RBP 相对编码所节省的空间，可能超过序言/尾声中额外的 `push rbp; mov rbp, rsp; pop rbp` 指令。

```plaintext
% echo 'mov rax, [rsp+8]; mov rax, [rbp-8]' | /tmp/Rel/bin/llvm-mc -x86-asm-syntax=intel -output-asm-variant=1 -show-encoding
        mov     rax, qword ptr [rsp + 8]        # encoding: [0x48,0x8b,0x44,0x24,0x08]
        mov     rax, qword ptr [rbp - 8]        # encoding: [0x48,0x8b,0x45,0xf8]

# ModR/M 字节 0x44：Mod=01（寄存器间接寻址 + disp8），Reg=0（目标寄存器 RAX），R/M=100（后面跟着 SIB 字节）
# ModR/M 字节 0x45：Mod=01（寄存器间接寻址 + disp8），Reg=0（目标寄存器 RAX），R/M=101（RBP）
```

### SFrame 与 .eh_frame 对比

Oracle 正在倡导在 Linux 发行版中采用 SFrame。SFrame 的实现由汇编器（assembler）和链接器（linker）处理，而非编译器。让我们构建最新的 binutils-gdb 来测试它。

**构建测试程序**

我们将使用来自 [https://github.com/llvm/llvm-project/tree/release/21.x](https://github.com/llvm/llvm-project/tree/release/21.x) 的 clang 编译器作为测试程序。

仍然存在与垃圾回收（garbage collection）相关的问题（[目标文件格式设计问题](https://maskray.me/blog/2025-09-28-remarks-on-sframe#:~:text=garbage)），因此我将禁用 `-Wl,--gc-sections`。

```patch
--- i/llvm/cmake/modules/AddLLVM.cmake
+++ w/llvm/cmake/modules/AddLLVM.cmake
@@ -331,4 +331,4 @@ function(add_link_opts target_name)
         # TODO Revisit this later on z/OS.
-        set_property(TARGET ${target_name} APPEND_STRING PROPERTY
-                     LINK_FLAGS " -Wl,--gc-sections")
+        #set_property(TARGET ${target_name} APPEND_STRING PROPERTY
+        #             LINK_FLAGS " -Wl,--gc-sections")
       endif()
```

```sh
configure-llvm custom-sframe -DLLVM_TARGETS_TO_BUILD=host -DLLVM_ENABLE_PROJECTS='clang' -DLLVM_ENABLE_UNWIND_TABLES=on -DLLVM_ENABLE_LLD=off -DCMAKE_{EXE,SHARED}_LINKER_FLAGS=-fuse-ld=bfd -DCMAKE_C_COMPILER=$HOME/opt/gcc-15/bin/gcc -DCMAKE_CXX_COMPILER=$HOME/opt/gcc-15/bin/g++ -DCMAKE_C_FLAGS="-B$HOME/opt/binutils/bin -Wa,--gsframe" -DCMAKE_CXX_FLAGS="-B$HOME/opt/binutils/bin -Wa,--gsframe"
ninja -C /tmp/out/custom-sframe clang
```

```plaintext
% ~/Dev/bloaty/out/release/bloaty /tmp/out/custom-sframe/bin/clang
    FILE SIZE        VM SIZE
 --------------  --------------
  63.9%  88.0Mi  73.9%  88.0Mi    .text
  11.1%  15.2Mi   0.0%       0    .strtab
   7.2%  9.96Mi   8.4%  9.96Mi    .rodata
   6.4%  8.87Mi   7.5%  8.87Mi    .sframe
   5.1%  7.07Mi   5.9%  7.07Mi    .eh_frame
   2.9%  3.96Mi   0.0%       0    .symtab
   1.4%  1.98Mi   1.7%  1.98Mi    .data.rel.ro
   0.9%  1.23Mi   1.0%  1.23Mi    [LOAD #4 [R]]
   0.7%   999Ki   0.8%   999Ki    .eh_frame_hdr
   0.0%       0   0.5%   614Ki    .bss
   0.2%   294Ki   0.2%   294Ki    .data
   0.0%  23.1Ki   0.0%  23.1Ki    .rela.dyn
   0.0%  8.99Ki   0.0%  8.99Ki    .dynstr
   0.0%  8.77Ki   0.0%  8.77Ki    .dynsym
   0.0%  7.24Ki   0.0%  7.24Ki    .rela.plt
   0.0%  6.73Ki   0.0%       0    [Unmapped]
   0.0%  6.29Ki   0.0%  3.84Ki    [21 Others]
   0.0%  4.84Ki   0.0%  4.84Ki    .plt
   0.0%  3.36Ki   0.0%  3.30Ki    .init_array
   0.0%  2.50Ki   0.0%  2.50Ki    .hash
   0.0%  2.44Ki   0.0%  2.44Ki    .got.plt
 100.0%   137Mi 100.0%   119Mi    TOTAL
% ~/Dev/object-file-size-analyzer/eh_size.rb /tmp/out/custom-sframe/bin/clang
clang: sframe=9303875 eh_frame=7408976 eh_frame_hdr=1023004 eh=8431980 sframe/eh_frame=1.2558 sframe/eh=1.1034
```

结果显示，`.sframe`（8.87 MiB）比 `.eh_frame` 和 `.eh_frame_hdr` 的总大小（7.07 + 0.99 = 8.06 MiB）大约大 10%。虽然 SFrame 在设计上旨在提高栈遍历的效率，但与传统的 DWARF 展开信息相比，它带来了不可忽视的空间开销。

### SFrame 与帧指针（FP）对比

在研究了 SFrame 相对于 `.eh_frame` 的开销之后，现在让我们比较两种主要的非硬件辅助的栈遍历方法。

- **帧指针方法**：保留 FP，但省略叶函数的 push/pop：`g++ -fno-omit-frame-pointer -momit-leaf-frame-pointer`
- **SFrame 方法**：省略 FP，使用 SFrame 元数据：`g++ -fomit-frame-pointer -momit-leaf-frame-pointer -Wa,--gsframe`

为了进行公平的比较，我们使用 Clang 和 GCC 两种编译器，通过两种方法构建 LLVM 可执行文件。以下脚本使用每种组合配置并构建测试二进制文件：

```sh
#!/bin/zsh
conf() {
  configure-llvm $1 -DCMAKE_EXE_LINKER_FLAGS='-fuse-ld=bfd -pie -Wl,-z,pack-relative-relocs' \
    -DCMAKE_SHARED_LINKER_FLAGS=-fuse-ld=bfd -DLLVM_ENABLE_UNWIND_TABLES=on -DLLVM_ENABLE_LLD=off ${@:2}
}

clang=(-DCMAKE_CXX_COMPILER=/tmp/Rel/bin/clang++ -DCMAKE_C_COMPILER=/tmp/Rel/bin/clang)
gcc=("-DCMAKE_C_COMPILER=$HOME/opt/gcc-15/bin/gcc" "-DCMAKE_CXX_COMPILER=$HOME/opt/gcc-15/bin/g++")

compact="-fomit-frame-pointer -momit-leaf-frame-pointer -B$HOME/opt/binutils/bin -mllvm -elf-compact-unwind -mllvm -x86-epilog-cfi=0"
fp="-fno-omit-frame-pointer -momit-leaf-frame-pointer -B$HOME/opt/binutils/bin -Wa,--gsframe=no"
sframe="-fomit-frame-pointer -momit-leaf-frame-pointer -B$HOME/opt/binutils/bin -Wa,--gsframe"

conf custom-compact -DCMAKE_{C,CXX}_FLAGS="$compact" ${clang[@]} \
  -DCMAKE_EXE_LINKER_FLAGS='-fuse-ld=lld -pie -Wl,-z,pack-relative-relocs' \
  -DCMAKE_SHARED_LINKER_FLAGS=-fuse-ld=lld

conf custom-fp -DCMAKE_{C,CXX}_FLAGS="-fno-integrated-as $fp" ${clang[@]}
conf custom-sframe -DCMAKE_{C,CXX}_FLAGS="-fno-integrated-as $sframe" ${clang[@]}

conf custom-fp-gcc -DCMAKE_{C,CXX}_FLAGS="$fp" ${gcc[@]}
conf custom-sframe-gcc -DCMAKE_{C,CXX}_FLAGS="$sframe" ${gcc[@]}

for i in compact fp sframe  fp-gcc sframe-gcc; do ninja -C /tmp/out/custom-$i llvm-mc opt; done
```

结果揭示了编译器实现之间的有趣差异：

```plaintext
% ~/Dev/object-file-size-analyzer/section_size.rb /tmp/out/custom-{fp,sframe,compact,fp-gcc,sframe-gcc}/bin/{llvm-mc,opt}
Filename                               |       .text size |        EH size |   .sframe size |  VM size | VM increase
---------------------------------------+------------------+----------------+----------------+----------+------------
/tmp/out/custom-fp/bin/llvm-mc         |  2120895 (23.5%) |  301528 (3.3%) |       0 (0.0%) |  9043221 |           -
/tmp/out/custom-sframe/bin/llvm-mc     |  2109231 (22.3%) |  367424 (3.9%) |  348041 (3.7%) |  9474085 |       +4.8%
/tmp/out/custom-compact/bin/llvm-mc    |  2109519 (24.4%) |  106288 (1.2%) |       0 (0.0%) |  8639637 |       -4.5%
/tmp/out/custom-fp-gcc/bin/llvm-mc     |  2744214 (29.2%) |  301836 (3.2%) |       0 (0.0%) |  9389677 |       +3.8%
/tmp/out/custom-sframe-gcc/bin/llvm-mc |  2705860 (27.7%) |  354292 (3.6%) |  356073 (3.6%) |  9780985 |       +8.2%
/tmp/out/custom-fp/bin/opt             | 38769545 (69.9%) | 3547688 (6.4%) |       0 (0.0%) | 55425217 |           -
/tmp/out/custom-sframe/bin/opt         | 38891295 (62.4%) | 4559644 (7.3%) | 4448874 (7.1%) | 62292133 |      +12.4%
/tmp/out/custom-compact/bin/opt        | 38898415 (74.8%) | 1200764 (2.3%) |       0 (0.0%) | 52020449 |       -6.1%
/tmp/out/custom-fp-gcc/bin/opt         | 54654215 (78.1%) | 3631196 (5.2%) |       0 (0.0%) | 70001373 |      +26.3%
/tmp/out/custom-sframe-gcc/bin/opt     | 53644895 (70.4%) | 4857364 (6.4%) | 5263676 (6.9%) | 76206149 |      +37.5%

% ruby ~/Dev/object-file-size-analyzer/eh_size.rb  /tmp/out/custom-compact/bin/opt
opt: sframe=0 eh_frame=267008 eh_frame_hdr=933756 eh=1200764 sframe/eh_frame=0.0 sframe/eh=0.0
% ruby ~/Dev/object-file-size-analyzer/eh_size.rb  /tmp/out/custom-sframe/bin/opt
opt: sframe=4448874 eh_frame=3938448 eh_frame_hdr=621196 eh=4559644 sframe/eh_frame=1.1296 sframe/eh=0.9757

% ~/Dev/object-file-size-analyzer/section_size.rb /tmp/out/custom-{fp-sync,sframe-sync,compact-sync}/bin/{llvm-mc,opt}
Filename                                 |       .text size |        EH size |   .sframe size |  VM size | VM increase
-----------------------------------------+------------------+----------------+----------------+----------+------------
/tmp/out/custom-fp-sync/bin/llvm-mc      |  2120895 (24.1%) |  263396 (3.0%) |       0 (0.0%) |  8802093 |           -
/tmp/out/custom-sframe-sync/bin/llvm-mc  |  2109231 (23.2%) |  291084 (3.2%) |  248654 (2.7%) |  9090325 |       +3.3%
/tmp/out/custom-compact-sync/bin/llvm-mc |  2109519 (24.4%) |  106288 (1.2%) |       0 (0.0%) |  8639637 |       -1.8%
/tmp/out/custom-fp-sync/bin/opt          | 38769545 (72.2%) | 2997572 (5.6%) |       0 (0.0%) | 53706041 |           -
/tmp/out/custom-sframe-sync/bin/opt      | 38891295 (66.9%) | 3425116 (5.9%) | 2951292 (5.1%) | 58091421 |       +8.2%
/tmp/out/custom-compact-sync/bin/opt     | 38898415 (74.8%) | 1200764 (2.3%) |       0 (0.0%) | 52020449 |       -3.1%
```

- SFrame 引入了显著的 VM 大小增长。
- GCC 构建的二进制文件明显大于 Clang 构建的，这可能是由于更激进的内联（inlining）或向量化（vectorization）策略。
- `/tmp/out/custom-compact` 的 EH 大小显著更小。详见下文。

在使用 Clang 构建的二进制文件中，帧指针配置产生的 `opt` 可执行文件（55.6 MiB）比 SFrame 配置（62.5 MiB）更小。这加强了我们之前的观察：对于需要频繁访问局部变量的大型函数，RBP 寻址可能比 RSP 相对寻址更紧凑。

汇编对比显示，使用 RBP 和 RSP 寻址的函数生成的代码非常相似。

相比之下，GCC 构建的二进制文件呈现相反的趋势：帧指针版本的 `opt`（70.0 MiB）比 SFrame 版本（76.2 MiB）更小。

省略 FP 和不省略 FP 构建之间生成的汇编代码差异很大，我比较了两个 GCC 构建之间的符号大小。

```nvim -d =(/tmp/Rel/bin/llvm-nm -U --size-sort /tmp/out/custom-fp-gcc/bin/llvm-mc) =(/tmp/Rel/bin/llvm-nm -U --size-sort /tmp/out/custom-sframe-gcc/bin/llvm-mc)```

许多函数，例如 `_ZN4llvm15ELFObjectWriter24executePostLayoutBindingEv`，在保留 FP 的构建中有显著更多的指令。这表明 GCC 的帧指针代码生成可能不如其默认的省略 FP 路径优化得那么好。

`/tmp/out/custom-compact` 构建使用了我自己的 llvm-project 分支（[http://github.com/MaskRay/llvm-project/tree/demo-unwind](http://github.com/MaskRay/llvm-project/tree/demo-unwind)），该分支将 Mach-O 的紧凑展开移植到了 ELF，使得大多数 `.eh_frame` FDE 可以用展开描述符（unwind descriptor）替换 CFI 指令。链接器行为：

- 将 FDE 分成两组：基于描述符的（augmentation 'C'）和基于指令的。
- 当存在紧凑 FDE 时，生成带有 12 字节表项的 `.eh_frame_hdr` 版本 2：`(pc_ptr, unwind_descriptor_or_fde_ptr)`。由 `.eh_frame_hdr` 内联描述的紧凑 FDE 会从输出的 `.eh_frame` 段中移除。

注意：`.ARM.exidx` 和 [MIPS 紧凑异常表](https://maskray.me/blog/2020-11-08-stack-unwinding#:~:text=MIPS) 也直接在二分查找索引表中描述展开描述符。

无法由紧凑展开表示的 FDE（例如，收缩包装优化后的情况）则使用传统的 CFI 指令（在 Mach-O 紧凑展开信息中称为 DWARF 转义）。

此实现涉及几个组件：

- `-mllvm -elf-compact-unwind`：生成带有 augmentation 字符 'C' 的 `.eh_frame` CIE 以及使用展开描述符的 FDE。
- `-mllvm -x86-epilog-cfi=0`：为 x86 禁用尾声 CFI（主要由 [D42848](https://reviews.llvm.org/D42848) 在 2018 年实现，值得注意的是在 Darwin 和 Windows 上已禁用）。如果没有这个选项，大多数帧将无法使用展开描述符，因为当前的 Mach-O 紧凑展开实现不支持 `popq %rbp; .cfi_def_cfa %rsp, 8; ret`。我认为这仍然是公平的，因为我们期望使用一个 8 字节的描述符，足以描述尾声 CFI。
- lld/ELF 的改动：FDE 被分为基于描述符的（augmentation 'C'）和基于 CFI 指令的两组。当存在紧凑 FDE 时，生成带有 12 字节表项（包含 `(pc_ptr, unwind_descriptor_or_fde_ptr)`）的 `.eh_frame_hdr` 版本 2。PC 指针保持 4 字节，而 8 字节的表项表示展开描述符（奇数）或 FDE 指针（偶数）。

使用当前的实现，在 77648 个 FDE 中，有 4937 个（6.36%）需要 DWARF 转义，其余的 FDE 可以用展开描述符替换。

如果我们实现 Mach-O `__unwind_info` 中的两级页表结构，`.eh_frame_hdr` 将变得更小。

## 运行时性能分析

待办

EH 情况下的 `perf record` 开销

FP 情况下的 `perf record` 开销

这里有一个来自 [llvm-compile-time-tracker.com 的基准测试运行](https://llvm-compile-time-tracker.com/compare.php?from=5d0f1591f8b91ac7919910c4e3e9614a8804c02a&to=76cdaf78a7d4b06130031818397da11b8985ab08&stat=instructions:u)。

`stable2-O3` 基准测试是相关的。当为非叶函数启用 FP 时，`instructions:u` 指标增加了 +2.44%，而 `wall-time`（一个较嘈杂的指标）仅增加了 0.56%。

## 总结

本文研究了在构建 LLVM 可执行文件时，不同栈遍历机制的空间开销。

**帧指针配置：** 启用帧指针（`-fno-omit-frame-pointer`）可能会产生悖论，即在大量访问栈对象时减少 x86-64 二进制文件的大小。这是因为 RBP 相对寻址产生的编码比 RSP 相对寻址更紧凑，后者需要一个额外的 SIB 字节。较短指令所节省的空间可以抵消序言/尾声的开销。

**SFrame 与 .eh_frame 对比：** 对于 x86-64 `clang` 可执行文件，SFrame 元数据比 `.eh_frame` 和 `.eh_frame_hdr` 的总大小大约大 10%。考虑到显著的 VM 大小开销以及相较于已建立的替代方案缺乏明显优势，我对 SFrame 作为用户空间程序栈遍历的未来可行性持怀疑态度。虽然 SFrame 将在未来几个月内进行重大的 V3 修订，但它需要在与现有的紧凑展开方案相当的大小缩减方面取得实质性进展，才能证明其相对于帧指针的采用是合理的。我希望有兴趣的人能够实现类似于 macOS 的紧凑展开描述符（支持 x86-64）和 OpenVMS 的类似方案。

**ELF 紧凑展开（ELF Compact Unwind）：** 我将 Mach-O 紧凑展开移植到 ELF 的原型展示了显著的潜力。与帧指针相比，这种方法将 VM 大小减少了 4.5-6.1%，在我的基准测试中实现了最小的二进制文件。通过用 8 字节的展开描述符（对于像收缩包装函数这样的复杂情况，则使用 DWARF 转义）替换冗长的 CFI 指令，`.eh_frame` 大幅缩减——只有 6.36% 的 FDE 需要传统的 CFI 格式。这种方法一旦完成，将提供一个引人注目的 SFrame 替代方案：更好的压缩性，与现有 `.eh_frame` 基础设施的兼容性，以及清晰的实现路径。

**[LLVM 社区：我需要你们的支持](https://discourse.llvm.org/t/rfc-adding-sframe-support-to-llvm/86900/34?u=maskray)**。作为维护者，我曾对 SFrame RFC 提出过技术上的反对意见。一些工程师驳回了这些意见。现在他们正升级到项目委员会（Project Council）以推翻技术评审。这看起来是 OKR（目标与关键成果）驱动的，而非基于技术价值。

GCC 的帧指针代码生成似乎不如其默认的省略帧指针路径优化得好，生成的汇编代码中存在的巨大差异证明了这一点。

运行时性能分析仍有待进行，以完成权衡评估。

## 附录：`configure-llvm`

此脚本指定了配置 llvm-project 时的常见选项：[https://github.com/MaskRay/Config/blob/master/home/bin/configure-llvm](https://github.com/MaskRay/Config/blob/master/home/bin/configure-llvm)

- `-DCMAKE_CXX_ARCHIVE_CREATE="$HOME/Stable/bin/llvm-ar qc --thin <TARGET> <OBJECTS>" -DCMAKE_CXX_ARCHIVE_FINISH=:`：使用瘦归档（thin archive）以减少磁盘占用。
- `-DLLVM_TARGETS_TO_BUILD=host`：仅构建单个目标。
- `-DCLANG_ENABLE_OBJC_REWRITER=off -DCLANG_ENABLE_STATIC_ANALYZER=off`：禁用不太流行的组件。
- `-DLLVM_ENABLE_PLUGINS=off -DCLANG_PLUGIN_SUPPORT=off`：禁用 `-Wl,--export-dynamic`，防止产生大型的 `.dynsym` 和 `.dynstr` 段。

## 附录：我的 SFrame 构建

```sh
mkdir -p out/release && cd out/release
../../configure --prefix=$HOME/opt/binutils --disable-multilib
make -j $(nproc) all-ld all-binutils all-gas
make -j $(nproc) install-ld install-binutils install-gas
```

`gcc -B$HOME/opt/binutils/bin` 和 `clang -B$HOME/opt/binutils/bin -fno-integrated-as` 将会使用安装目录中的 `as` 和 `ld`。

## 附录：脚本

本文使用的 Ruby 脚本可在 [https://github.com/MaskRay/object-file-size-analyzer/](https://github.com/MaskRay/object-file-size-analyzer/) 获取。
