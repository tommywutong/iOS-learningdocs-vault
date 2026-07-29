---
title: x86 链接器笔记
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-02-19-linker-notes-on-x86'
original_language: en
published: 2023-02-19
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:df025cc76cbaf50c'
translated: true
---

> 原文：[Linker notes on x86](https://maskray.me/blog/2023-02-19-linker-notes-on-x86)　·　MaskRay (宋方睿)

[2023-02-19](https://maskray.me/blog/2023-02-19-linker-notes-on-x86)

# x86 链接器笔记

更新于 2024-01。

本文描述 ELF 链接器中与 x86 架构相关的特定细节。我将使用 "x86" 同时指代 x86-32 和 x86-64。

## 全局偏移表（Global Offset Table）

全局偏移表由两个节（section）组成：

- `.got.plt` 保存 PLT 的代码地址。
- `.got` 保存其他地址和偏移量。

符号 `_GLOBAL_OFFSET_TABLE_` 定义在 `.got.plt` 节的开头。如果 `.got.plt` 不存在，GNU ld 会将 `_GLOBAL_OFFSET_TABLE_` 定义在 `.got` 节的开头。

`.got.plt` 有 3 个保留表项。

`.got.plt[0]` 出于历史原因保存 `_DYNAMIC` 的链接时地址。glibc 2.35 之前的版本需要 `_DYNAMIC`。参见 [All about Global Offset Table](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#global_offset_table_0)。

`.got.plt[1]` 和 `.got.plt[2]` 用于延迟绑定（lazy binding）PLT。链接器通过动态标签 `DT_PLTGOT` 将 `.got.plt` 的地址传递给 rtld。

### GOT 优化

参见 [All about Global Offset Table#GOT optimization](https://maskray.me/blog/2021-08-29-all-about-global-offset-table#got-optimization)。

## 过程链接表（Procedure Linkage Table）

### 间接分支跟踪（Indirect Branch Tracking）

间接分支跟踪的相关内容请见下面的 `.note.gnu.property`。详情参见 [All about Procedure Linkage Table#x86](https://maskray.me/blog/2021-09-19-all-about-procedure-linkage-table#x86)。

GNU ld 使用的方案不必要地引入了两个节：`.plt` 和 `.plt.sec`。ld.lld 也采用了同样的做法，以避免给 objdump（PLT 识别）等工具增加复杂性。mold 采用了一种替代方案（也就是间接分支跟踪一开始应该采用的方案）。不幸的是，这已是既成事实，增加替代方案并不会简化世界。我认为这只会给其他希望支持其方案的工具增加实现复杂性。

### Retpoline

Retpoline 用于缓解 Spectre v2。PLT 表项由链接器合成，因此也需要适配。在 ld.lld 中可以通过 `-z retpolineplt` 启用。

### mark-plt

关于 x86 PLT 重写，请参见 [All about Procedure Linkage Table](https://maskray.me/blog/2021-09-19-all-about-procedure-linkage-table#x86-plt-rewriting)。

## 线程本地存储（Thread Local Storage）

x86 使用 TLS Variant II：静态 TLS 块（block）位于线程指针的下方。

除了传统的通用动态（general dynamic）和本地动态（local dynamic）TLS 模型外，x86-32 和 x86-64 还有 TLSDESC ABI。

链接器会执行 TLS 优化。

参见 [All about thread-local storage](https://maskray.me/blog/2021-02-14-all-about-thread-local-storage)。

## 程序属性（Program Property）

`.note.gnu.property` 节包含程序属性 note，描述了链接器和动态加载器的特殊处理要求。

x86 psABI 定义了许多属性 note，但很多似乎并不是特别有用。

- `GNU_PROPERTY_X86_ISA_1_BASELINE`、`GNU_PROPERTY_X86_ISA_1_V2`、`GNU_PROPERTY_X86_ISA_1_V2`、`GNU_PROPERTY_X86_ISA_1_V3`：这些属性描述 x86 ISA 级别。
- `GNU_PROPERTY_X86_ISA_1_USED`、`GNU_PROPERTY_X86_ISA_1_NEEDED`：在引入 x86 ISA 级别时已废弃（deprecated）。
- `GNU_PROPERTY_X86_FEATURE_1_IBT`、`GNU_PROPERTY_X86_FEATURE_1_SHSTK`：由 Intel CET 使用（参见 [Control flow integrity](https://maskray.me/blog/2022-12-18-control-flow-integrity)）。见下文。

对于 x86，链接器解析输入的 `.note.gnu.property` 节，识别 `-z force-ibt` 和 `-z shstk`，以计算输出的 `.note.gnu.property`（类型为 `SHT_NOTE`）节。

以下代码（摘自 ld.lld）描述了其行为。基本上，在没有额外选项的情况下，如果所有输入的 `.note.gnu.property` 节都设置了 `GNU_PROPERTY_X86_FEATURE_1_IBT` 位（逻辑 AND），则输出也设置该位。`-z force-ibt` 会强制设置该位，并给出警告。

如果所有输入的 `.note.gnu.property` 节都设置了 `GNU_PROPERTY_X86_FEATURE_1_SHSK` 位（逻辑 AND），则输出也设置该位。`-z shstk` 会强制设置该位，且不给出警告。

```cpp
for (ELFFileBase *f : ctx.objectFiles) {
  uint32_t features = f->andFeatures;
  if (!(features & GNU_PROPERTY_X86_FEATURE_1_IBT)) {
    if (config->zCetReport == "error")
      error(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_IBT property");
    else if config->zCetReport == "warning")
      warn(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_IBT property");
  }
  if (!(features & GNU_PROPERTY_X86_FEATURE_1_SHSTK)) {
    if (config->zCetReport == "error")
      error(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_SHSTK property");
    else if config->zCetReport == "warning")
      warn(toString(f) + ": -z cet-report: file does not have GNU_PROPERTY_X86_FEATURE_1_SHSTK property");
  }

  if (config->zForceIbt && !(features & GNU_PROPERTY_X86_FEATURE_1_IBT)) {
    if (config->zCetReport == "none")
      warn(toString(f) + ": -z force-ibt: file does not have "
                         "GNU_PROPERTY_X86_FEATURE_1_IBT property");
    features |= GNU_PROPERTY_X86_FEATURE_1_IBT;
  }
  ret &= features;
}

// 强制启用 Shadow Stack。
if (config->zShstk)
  ret |= GNU_PROPERTY_X86_FEATURE_1_SHSTK;
```

## `.eh_frame`

`.eh_frame` 节的类型通常是 `SHT_PROGBITS`。对于一个专用用途的节没有专用类型，这被认为是一个设计失误。x86-64 psABI 指出应该使用 `SHT_X86_64_UNWIND`。对于未来的架构，最好不要将 0x70000001 保留给其他用途。

自 rL252300 起，Clang 会发出类型为 `SHT_X86_64_UNWIND` 的 `.eh_frame` 节，以符合 psABI。链接器需要允许混合使用 `SHT_PROGBITS` 和 `SHT_X86_64_UNWIND` 类型的 `.eh_frame` 节。

## `.gnu.linkonce.t.__x86.get_pc_thunk.bx`

在 COMDAT 被引入 ELF 之前，使用了魔数符号前缀 `.gnu.linkonce`。如今 `.gnu.linkonce` 早已过时，但不幸的是，`.gnu.linkonce.t.__x86.get_pc_thunk.bx` 在 glibc x86-32 中一直保持相关性，直到 glibc 2.32（2020-08）。

## 分割栈（Split stack）

gccgo 使用了一种称为 "split stack" 的分段栈方案。分割栈允许非连续的栈空间，该栈会根据需要自动增长。（gc Go 编译器现在使用栈拷贝而非栈分割。在 gccgo 中使用栈拷贝很困难，因为编译器需要为栈上的所有帧（frame）提供精确的栈映射，并且要了解所有的指针。）

该方案会调用 libgcc 中定义的运行时函数（`__morestack*`），并要求链接器重写某些代码序列。

每个使用分割栈的可重定位目标文件都有一个名为 `.note.GNU-split-stack` 的标记节。链接器使用此节来识别使用分割栈编译的可重定位目标文件。

对于从分割栈可重定位目标文件到非分割栈可重定位目标文件的函数调用，链接器会重写函数序言。序言可以是以下两种方案中的任意一种。

```plaintext
  cmp   rsp, qword ptr fs:[0x70]
  jae   1f
  call  __morestack
  ret
1:
  ...

=>

  stc
  nop   dword ptr [rax + rax]
  jae   1f
  call  __morestack_non_split
  ret
1:
  ...
```

```plaintext
  lea   r10, [rsp-0x100]     # The register is r10 or r11
  cmp   r10, qword ptr fs:[0x70]
  jae   1f
  call  __morestack
  ret
1:
  ...

=>

  lea   r10, [rsp-0x4100]    # The displacement is changed
  cmp   r10, qword ptr fs:[0x70]
  jae   1f
  call  __morestack_non_split
  ret
1:
  ...
```
