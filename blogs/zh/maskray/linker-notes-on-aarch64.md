---
title: AArch64 上的链接器笔记
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-03-05-linker-notes-on-aarch64'
original_language: en
published: 2023-03-05
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:98e1815e22a4e1be'
translated: true
---

> 原文：[Linker notes on AArch64](https://maskray.me/blog/2023-03-05-linker-notes-on-aarch64)　·　MaskRay (宋方睿)

[2023-03-05](https://maskray.me/blog/2023-03-05-linker-notes-on-aarch64)

# AArch64 上的链接器笔记

本文描述了 ELF 链接器中与 AArch64 相关的目标特定细节。AArch64 是 Arm 架构的 64 位执行状态。AArch64 执行状态运行 A64 指令集。AArch32 和 AArch64 执行状态使用截然不同的指令集，因此许多软件为 Arm 架构的这两种执行状态分别提供了两个移植版本。

曾存在“ARM 架构”和“ARM 指令集”，导致许多软件项目使用“ARM”或“arm”作为其移植版本的名称。2011 年，ARMv8 引入了两种执行状态：AArch32 和 AArch64。先前的指令集“ARM”和“Thumb”分别更名为“A32”和“T32”。2017 年，该架构更名为“Arm 架构”，以反映公司名称的品牌重塑。因此，“ARMv8-A”架构规范现在命名为“Armv8-A”。

对于 AArch64 执行状态，尽管许多项目使用“AArch64”作为移植名称，但由于历史原因，macOS、Windows、Linux 内核以及一些 BSD 操作系统不幸地使用了“arm64”。（对 AArch64 的支持是在 Linux 内核 3.7 版本中添加的。最初补丁集命名为“aarch64”，但后来根据内核开发者的[要求](https://lkml.org/lkml/2012/7/6/624)进行了更改。）

## ABI 文档

- [ELF for the Arm® 64-bit Architecture (AArch64)](https://github.com/ARM-software/abi-aa/blob/main/aaelf64/aaelf64.rst)
- [System V ABI for the Arm® 64-bit Architecture (AArch64)](https://github.com/ARM-software/abi-aa/blob/main/sysvabi64/sysvabi64.rst)

## 全局偏移表（Global Offset Table）

全局偏移表由两个 section 组成：

- `.got.plt` 保存 PLT 所需的代码地址。
- `.got` 保存其他地址和偏移量。

符号 `_GLOBAL_OFFSET_TABLE_` 定义在 `.got` section 的开头。GNU ld 为 `.got` 保留了一个条目，并且 `.got[0]` 保存了 `_DYNAMIC` 的链接时地址，这是出于历史原因。2.35 版本之前的 glibc 版本需要 `_DYNAMIC`。请参阅 [All about Global Offset Table](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#global_offset_table_0)。

`.got.plt[1]` 和 `.got.plt[2]` 用于延迟绑定（lazy binding）PLT。链接器通过动态标签 `DT_PLTGOT` 将 `.got.plt` 的地址传递给运行时动态链接器（rtld）。

## 过程链接表（Procedure Linkage Table）

寄存器 `x16` (IP0) 和 `x17` (IP1) 是第一个和第二个过程内调用临时寄存器。它们可能被 PLT 条目和 veneer 使用。

PLT 头部如下所示： 1  
2  
3  
4  
5  
6  
bti c // 如果启用了 BTI  
stp x16, x30, [sp,#-16]!  
adrp x16, &.got.plt[2]  
ldr x17, [x16, :lo12: &.got.plt[2]]  
add x16, x16, :lo12: &.got.plt[2]  
br x17

第 N 个 PLT 条目如下所示： 1  
2  
3  
4  
5  
6  
bti c // 如果启用了 BTI  
adrp x16, &.got.plt[N + 3]  
ldr x17, [x16, :lo12: &.got.plt[N + 3]]  
add x16, x16, :lo12: &.got.plt[N + 3]  
autia1716 // 如果启用了 PAC-PLT  
br x17

当输出文件启用了 BTI 时，代码序列以 `bti c` 开头。当启用了 PAC-PLT 时，代码序列在 `br x17` 之前包含 `autia1716`。

`x16` 由延迟 PLT 解析器使用。对于 `ld -z now`，设置 `x16` 是不必要的。[https://github.com/ARM-software/abi-aa/issues/202](https://github.com/ARM-software/abi-aa/issues/202) 讨论了使 `x16` 设置变为可选的可能性。

## 重定位优化

关于 GOT 优化，请参阅 [All about Global Offset Table#GOT optimization](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#got-optimization)。

除了 GOT 优化之外，还有一些其他优化方案，例如：

```plaintext
add  x2, x2, 0  // R_<CLS>_ADD_ABS_LO12_NC

=>

nop
```

```plaintext
adrp x0, symbol
add  x0, x0, :lo12: symbol

=>

nop
adr  x0, symbol
```

`--no-relax` 可禁用该优化。

请参阅 [ELF for the Arm® 64-bit Architecture (AArch64)#Relocation optimization](https://github.com/ARM-software/abi-aa/blob/main/aaelf64/aaelf64.rst#relocation-optimization)。

## 线程本地存储（Thread Local Storage）

AArch64 使用 TLS Variant I 的一种变体：静态 TLS 块放置在线程指针之上。线程指针指向线程控制块的末尾。

链接器执行 TLS 优化。

传统的通用动态和本地动态 TLS 模型已被废弃，ld.lld 不支持这些模型。

请参阅 [All about thread-local storage](https://maskray.me/blog/2021-02-14-all-about-thread-local-storage)。

## 程序属性（Program Property）

`.note.gnu.property` section 包含程序属性 notes，这些 notes 描述了链接器和动态加载器的特殊处理要求。

链接器解析输入的 `.note.gnu.property` section，并识别命令行选项 `-z force-bti` 和 `-z pac-plt`，以计算输出的 `.note.gnu.property`（类型为 `SHT_NOTE`）section。如果没有这些选项，链接器仅在所有输入的可重定位目标文件都设置了相应功能位时，才在输出文件中设置该功能位。

```cpp
for (ELFFileBase *f : ctx.objectFiles) {
  uint32_t features = f->andFeatures;
  if (!(features & GNU_PROPERTY_AARCH64_FEATURE_1_BTI)) {
    if (config->zBtiReport == "error")
      error(toString(f) + ": -z bti-report: file does not have GNU_PROPERTY_AARCH64_FEATURE_1_BTI property");
    else if (config->zBtiReport == "warning")
      warn(toString(f) + ": -z bti-report: file does not have GNU_PROPERTY_AARCH64_FEATURE_1_BTI property");
  }

  if (config->zForceBti && !(features & GNU_PROPERTY_AARCH64_FEATURE_1_BTI)) {
    if (config->zBtiReport == "none")
      warn(toString(f) + ": -z force-bti: file does not have "
                         "GNU_PROPERTY_AARCH64_FEATURE_1_BTI property");
    features |= GNU_PROPERTY_AARCH64_FEATURE_1_BTI;
  }
  if (config->zPacPlt && !(features & GNU_PROPERTY_AARCH64_FEATURE_1_PAC)) {
    warn(toString(f) + ": -z pac-plt: file does not have "
                       "GNU_PROPERTY_AARCH64_FEATURE_1_PAC property");
    features |= GNU_PROPERTY_AARCH64_FEATURE_1_PAC;
  }
  ret &= features;
}
```

## 范围扩展 thunk

函数调用通常使用 `B` 和 `BL` 指令。这两条指令的范围为 +/-128MiB，并可能使用两种重定位类型：`R_AARCH64_CALL26` 和 `R_AARCH64_JUMP26`。这个范围比许多其他指令集的分支范围要大。如果目标无法通过单个 `B`/`BL` 指令到达，链接器可能会插入一个 veneer（范围扩展 thunk）。

`-no-pie` 链接可能会使用一个采用绝对寻址的 thunk，目标为 64 位地址空间中的任何位置。 1  
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
\<caller\>:  
 bl __AArch64AbsLongThunk_nonpreemptible  
 b __AArch64AbsLongThunk_nonpreemptible  
  
\<__AArch64AbsLongThunk_nonpreemptible\>:  
 ldr x16, .+8  
 br x16  
  
\<$d\>:  
 .word 0x00000000  
 .word 0x00000010  
  
\<.plt\>:

`-pie` 和 `-shared` 链接需要使用一个采用 PC 相对寻址的 thunk，目标范围为 +/-4GiB。 1  
2  
3  
4  
5  
6  
7  
8  
\<caller\>:  
 bl __AArch64ADRPThunk_nonpreemptible  
 b __AArch64ADRPThunk_nonpreemptible  
  
\<__AArch64ADRPThunk_nonpreemptible\>:  
 adrp x16, nonpreemptible  
 add x16, x16, :lo12: nonpreemptible  
 br x16

thunk 的分支目标可能是一个 PLT 条目： 1  
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
\<caller\>:  
 bl __AArch64ADRPThunk_preemptible  
  
\<__AArch64ADRPThunk_preemptible\>:  
 adrp x16, preemptible@plt  
 add x16, x16, :lo12: preemptible@plt  
 br x16  
  
...  
  
\<preemptible@plt\>:  
 adrp x16, &.got.plt[N + 3]  
 ldr x17, [x16, :lo12: &.got.plt[N + 3]]  
 add x16, x16, :lo12: &.got.plt[N + 3]  
 br x17

在许多情况下，我们不需要长代码序列（`ldr/br` 或 `adrp/add/br`）。相反，thunk（[短范围 thunk](https://reviews.llvm.org/D148701)）可以使用单个 `b/bl` 指令到达目标。

### BTI thunk

长范围 thunk 使用间接分支（`br x16`）。当启用了 BTI 时，间接分支必须着陆在一个与 BTI 兼容的指令（`bti c`、`bti j`、`bti jc`、`paciasp` 或 `pacibsp`）上。GCC 可能会在函数入口省略 BTI 指令，前提是它能证明没有来自编译单元外部的间接分支。当目标没有 BTI 时，静态链接器负责生成一个着陆垫（landing pad）。

当输出设置了 `GNU_PROPERTY_AARCH64_FEATURE_1_BTI`，并且长范围 thunk 的目标是一个没有与 BTI 兼容指令的函数时，ld.lld（[自 2024-10 起](https://github.com/llvm/llvm-project/commit/c4d9cd8b747cb399a61dd987eb95ad518eb15448)）会在目标附近生成一个着陆垫 thunk（`AArch64BTILandingPadThunk`）： 1  
2  
3  
4  
5  
\<__AArch64BTIThunk_fn\>:  
 bti c  
 b fn // 如果着陆垫紧邻 fn 之前，则可以省略  
\<fn\>:  
 ...

当着陆垫可以放置在使得控制流直接落入目标的位置时，`b` 指令可以被省略，这在 `-ffunction-sections` 下很常见。

短范围 thunk 使用直接分支（`b`/`bl`），不需要着陆垫。一个目标最多需要一个着陆垫，并在所有调用者之间共享。PLT 条目已经以 `bti c` 开头，因此它们也不需要着陆垫。

## `--fix-cortex-a53-843419`

此选项为 Arm Cortex-A53 勘误表 843419 启用了链接器解决方法。完整细节可在 ARM-EPM-048406 文档中找到。链接器扫描 4KiB 页中最后两条指令中的 `adrp`，后跟一条加载或存储指令以及另外两条指令。一旦检测到勘误条件，链接器会尝试将其重写为替代代码序列。有关详细信息，请参阅实现中的注释。

在 ld.lld 中，这实现为一种 thunk，类似于范围扩展 thunk。当重定位 `R_AARCH64_JUMP26` 时，ld.lld 还额外设置了一个[解决方法](https://github.com/llvm/llvm-project/commit/20489ec5639e01c3c05ca5a39e6e43cac66c202f)。

## `--android-memtag-{mode,stack,heap}`

这些选项指示 ld.lld 创建 `DT_AARCH64_MEMTAG_*` 动态标签。请参阅 [Memtag ABI Extension to ELF for the Arm® 64-bit Architecture (AArch64)](https://github.com/ARM-software/abi-aa/blob/main/memtagabielf64/memtagabielf64.rst)。

## PAuth ABI

`-z pac-plt` 启用 PAC PLT 并设置 `DT_AARCH64_PAC_PLT` 动态标签。
