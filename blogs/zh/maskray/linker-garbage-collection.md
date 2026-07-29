---
title: 链接器垃圾回收
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2021-02-28-linker-garbage-collection'
original_language: en
published: 2021-02-28
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:311e6ff83b4a5b73'
translated: true
---

> 原文：[Linker garbage collection](https://maskray.me/blog/2021-02-28-linker-garbage-collection)　·　MaskRay (宋方睿)

[2021-02-28](https://maskray.me/blog/2021-02-28-linker-garbage-collection)

# 链接器垃圾回收

一个程序中可能包含大量未使用的代码和数据。原因可能有很多：

- 在所有代码路径中确实存在未使用的代码和数据。
- 某些代码和数据在某些代码路径中未被使用，但在其他路径中却被使用。这在库中很常见，因为并非所有用法都能执行所有代码路径。
- 编译器生成了重复的定义，并期望链接器（linker）去重，例如内联函数、隐式模板实例化、虚函数表（vtable）、`type_info` 对象。只需要一份副本，其他的可以（或必须）被丢弃。

对于第一点，编译器可以检测到一些未使用的代码和数据（例如 `-Wunused`）。然而，由于只能看到一个翻译单元（translation unit）的限制，许多情况（例如未使用的非 internal 链接定义）无法被检测到。拥有全局可见性、能看到所有翻译单元的链接器是进行此项工作的最佳场所。许多链接器提供了丢弃未使用代码和数据的功能：

- 归档成员选择（Archive member selection）。如果一个归档成员无法满足一个未定义引用（undefined reference），它可能不会被拉入链接过程。这避免了该成员的所有段贡献（section contribution）。
- COMDAT 段去重（COMDAT section deduplication）
- 基于段的垃圾回收（Section based garbage collection）

本文聚焦于最后一点。在 GNU 链接器中，该特性被称为“垃圾回收”（`ld --gc-sections`）。在 macOS 上，ld64 称之为“死代码剥离”（`ld -dead_strip`）。在 Windows 上，文档称之为“消除从未被引用的函数和数据”（`link.exe /OPT:REF`）。

段（Section）是该功能的合适粒度。在许多目标文件格式中，“段”是一个不可分割的单位。垃圾回收特性从一个应被保留的段列表（GC 根，GC roots）开始。对于每个保留的段，链接器通过重定位（relocations）和关联段（关联段：ELF 段分组和 PE `IMAGE_COMDAT_SELECT_ASSOCIATIVE`）标记被引用的段。最后，未标记的段被丢弃。如果一个符号定义在被丢弃的段内，该符号也会被丢弃。

以下伪代码描述了该过程：

```cpp
set visited;
stack work_list;
for each section
  if section is a GC root {
    work_list.push_back(section);
    visited.insert(section);
  }
while (work_list.size()) {
  section sec = work_list.back();
  work_list.pop_back();
  for each section referenced by sec
    if (visited.insert(section))
      work_list.push_back(section);
}
```

一个段可能通过几种方式引用其他段。最常见的方式是通过重定位。段 `A` 包含重定位，一个重定位可能引用定义在另一个段 `B` 中的符号。我们说 `A` 引用了 `B`。段 `A` 可能有从属段（dependent sections）。这些从属段可能需要随着 `A` 作为一个整体被丢弃。

## ELF

使用 `-ffunction-sections` 和 `-fdata-sections` 编译源文件，以利用基于段的 GC。

没有这些选项时，编译器倾向于生成整体式的文本段和数据段。这些大段使得 GC 粒度变粗，它们很可能作为一个整体被保留。`ld --gc-sections` 仍然可以丢弃一些段，但效果可能非常差。

下面是一个汇编文件，其中穿插了描述 GC 根和通过重定位引用段的注释。

```text
# _start 是一个 GC 根。
.text
.globl _start
_start:
  # 这个重定位会导致 .text.foo 被标记。
  call foo

.section .text.foo,"ax",@progbits
.globl foo
foo:
  # 这个重定位会导致 .text.bar 被标记。
  call bar

.section .text.bar,"ax",@progbits
.globl bar
bar:
  ret
```

### `-fno-unique-section-names`

`-ffunction-sections` 会导致段名如 `.text.name`。`-fdata-sections` 会导致段名如 `.data.name`、`.rodata.name`、`.data.rel.local.name`。虽然这些名称便于调试，但有几个问题：

- 链接器脚本（linker script）中的输入段描述需要处理可选后缀：`*(.data .data.*)`。
- 唯一的段名会增大字符串表（string table）的大小。
- 为优化目的而设的段，其名称不幸地具有歧义：`.text.exit.*`、`.text.hot.*`、`.text.unlikely.*` 等。它们可能与某些函数名冲突。

对于第一点，PE/COFF 中的 `$` 是一个很好的替代方案。

对于第二点，Clang 提供了 `-fno-unique-section-names` 来节省字符串表空间：使用诸如 `.text`、`.data`、`.rodata` 的词干名称。`-fno-unique-section-names` 需要创建多个同名段。这需要一种新的汇编器语法：`.section .text,"a",@progbits,unique,1`。LLVM 首先实现了该语法。随后 H.J. Lu 为 binutils 2.35 实现了该语法。

### GNU ld

以下段是 GC 根。

- 定义了由 `-u`、`--entry`、`--init` 或 `--fini` 指定的符号的段
- 定义了导出到 `.dynsym` 的符号的段

    - 符号的可见性（visibility）为 `STV_DEFAULT` 或 `STV_PROTECTED` 且未被本地化
    - 指定了 `-shared`、`--export-dynamic` 或 `--gc-keep-exported` 其中之一
    - （其他我未知的条件）
- 具有 `SHF_GNU_RETAIN` 标志的段
- `SHT_PREINIT_ARRAY/SHT_INIT_ARRAY/SHT_FINI_ARRAY`
- 非 `SHF_ALLOC` 非 `SHF_LINK_ORDER` 的 `SHT_NOTE`
- 链接器创建的段 (`SEC_LINKER_CREATED`)
- 被包含 `KEEP` 关键字的输入段描述匹配的段
- （其他我未知的条件）

GNU ld 实现了一个有趣的启发式规则：如果一个可重定位目标文件中至少有一个保留的非 `SHT_NOTE` 的 `SHF_ALLOC` 段，GNU ld 会标记更多段。否则，大多数段（例如 `.debug_*`）将被丢弃。（参见 `bfd/elflink.c:_bfd_elf_gc_mark_extra_sections`）当没有非 `SHT_NOTE` 的 `SHF_ALLOC` 段被保留时，这个启发式规则可以丢弃相当多的调试段。

以下段也会被丢弃：

- 不在段分组（section group）中的非 `SHF_ALLOC` 非 `SHF_LINK_ORDER` 段

    - 除了与已丢弃的文本段关联的 `.debug_line.*`
- 仅包含非 `SHF_ALLOC` 段的分组段

GNU ld 不支持对 `SHF_MERGE` 段进行 GC（[PR26622](https://sourceware.org/bugzilla/show_bug.cgi?id=26622)）。如果对一个 `as-needed` 共享目标（shared object）的唯一引用来自被丢弃的段，那么 `DT_NEEDED` 条目本可以被省略。GNU ld 没有实现此功能（[PR24836](https://sourceware.org/bugzilla/show_bug.cgi?id=24836)）。

GNU ld 不会使符号赋值（symbol assignment）的 RHS 保留一个段（[PR31158](https://sourceware.org/bugzilla/show_bug.cgi?id=31158)）。

你可以使用 `--print-gc-sections` 或 `--print-gc-sections=<file>`（LLD 22）打印被丢弃的段。

### ld.lld

以下段是 GC 根。

- 定义了由 `-u`、`--entry`、`--init` 或 `--fini` 指定的符号的段
- 定义了导出到 `.dynsym` 的符号的段
- 定义了由链接器脚本引用的符号的段
- 具有 `SHF_GNU_RETAIN` 标志的段
- `SHT_PREINIT_ARRAY/SHT_INIT_ARRAY/SHT_FINI_ARRAY`
- 不在段分组内的 `SHT_NOTE`（此规则用于 Fedora watermark）
- `.ctors/.dtors/.init/.fini/.jcr`
- `.eh_frame` 引用的特性例程（personality routines）或语言特定数据区（language-specific data area）。ld.lld 在 `.eh_frame` 去重之前处理 `--gc-sections`，因此这可能会保留比所需更多的段。
- 被包含 `KEEP` 关键字的输入段描述匹配的段

非 `SHF_ALLOC`、非 `SHF_LINK_ORDER`、非 `SHF_REL[A]`、非 `SHF_GROUP` 的段会被保留，尽管它们不是 GC 根。

如果一个活跃段（live section）包含一个重定位，该重定位引用了一个在共享目标中定义的非弱符号，则该共享目标被认为是必需的（这将产生一个 `DT_NEEDED` 标签）。

当 `-z nostart-stop-gc` 生效时，如果一个活跃段包含一个重定位，引用了符号 `__start_$secname` 或 `__stop_$secname`，并且 `$secname` 具有 C 标识符名称，则将保留所有名为 `$secname` 的输入段。详情请参见[元数据段、COMDAT 和 SHF_LINK_ORDER](https://maskray.me/blog/2021-01-31-metadata-sections-comdat-and-shf-link-order)。

### 调试段

链接器不会丢弃调试段。这遵循“智能格式，呆板链接器（smart format, dumb linker）”的理念。DWARF 段很大。优化它们将花费大量的链接时间。

然而，在某些情况下，被丢弃的文本段会导致 DWARF 中出现一些占位值（有时称为墓碑值（tombstone values））。

- `.debug_ranges` 和 `.debug_loc`：1（ld.lld<11：0+addend；GNU ld 对 .debug_ranges 使用 1）
- `.debug_*`：0（ld.lld<11：0+addend；GNU ld 使用 0；未来的 ld.lld：0xffffffff 或 0xffffffffffffffff）

### `SHF_GNU_RETAIN`

在 binutils 2.36 中，GNU as 引入了标志 `R` 来表示 FreeBSD 和 Linux 模拟环境上的 `SHF_GNU_RETAIN`。这是一种架构无关的方式，用于将段标记为 GC 根。我已经为 LLVM 集成汇编器和 ld.lld 添加了支持，并允许在所有 ELF 平台上使用此语法。1  
.section meta,"aR",@progbits

使用 GCC>=11 或 Clang>=13 ([https://reviews.llvm.org/D97447](https://reviews.llvm.org/D97447))，你可以这样写：1  
2  
__attribute__((retain,used,section("meta")))  
static const char dummy[0];

`used` 属性（attribute）附加到函数或变量定义时，表示可能存在源文件中不明显的对该实体的引用。在 COFF 和 Mach-O 目标（Windows 和 Apple 平台）上，`used` 属性防止符号被链接器段 GC 移除。在 ELF 目标上，如果定义未被其他方式引用，GNU ld/gold/ld.lld 可能会移除该定义。

`retain` 属性在 GCC 11 中被引入，用于在 ELF 目标上设置 `SHF_GNU_RETAIN` 标志。

在 `SHF_GNU_RETAIN` 出现之前的典型解决方案是：1  
2  
3  
asm(".pushsection .init_array,\\"aw\\",%init_array\\n" \\  
 ".reloc ., BFD_RELOC_NONE, meta\\n" \\  
 ".popsection\\n")

(`BFD_RELOC_NONE` 需要 binutils>=2.26。)

其思想是 `SHT_INIT_ARRAY` 段是 GC 根。一个空的 `SHT_INIT_ARRAY` 不会改变输出。`.reloc` 指令产生一个重定位。`BFD_RELOC_NONE` 是一个特殊标记，它被转换成架构相关的 `R_*_NONE` 重定位类型。该重定位作为一个人工引用：它不修改位置，但可以保持定义 `meta` 的段活跃。

我在 LLVM 9.0.0 中添加了对 `R_ARM_NONE/R_AARCH64_NONE/R_386_NONE/R_X86_64_NONE/R_PPC_NONE/R_PPC64_NONE` 的 `.reloc` 支持，并在 LLVM 13.0.0 中添加了 `BFD_RELOC_NONE` 支持。如果你的目标 Clang 版本较旧，可以这样写：

```c
asm(".pushsection .init_array,\"aw\",%init_array\n" \
    ".reloc ., R_AARCH64_NONE, meta\n"              \
    ".popsection\n")
```

元数据段的用法请参见[元数据段、COMDAT 和 SHF_LINK_ORDER](https://maskray.me/blog/2021-01-31-metadata-sections-comdat-and-shf-link-order)。

### `SHF_MERGE` 段

此段标志适用于一些包含常量内容（整数常量、字符串常量等）的数据段。如果该段包含统一大小的数据元素，并且地址无关紧要，则重复元素可以被一个代表性元素替换。来自其他段的引用可以绑定到该代表性元素。

ld.lld 支持对未使用片段进行垃圾回收。GNU ld 尚未实现此功能（[PR26622](https://sourceware.org/bugzilla/show_bug.cgi?id=26622)）。

### 被抑制的未定义符号错误

ELF 链接器不会扫描已丢弃输入段中的重定位。当启用 `--gc-sections` 时，某些未定义符号错误会被抑制。1  
2  
3  
4  
5  
6  
7  
8  
9  
% cat a.c  
void bar();  
void foo() { bar(); }  
int main() { }  
% clang -ffunction-sections -Wl,--gc-sections a.c # 无错误  
% clang -ffunction-sections a.c  
ld.lld: error: undefined symbol: bar  
\>\>\> referenced by a.c  
\>\>\> /tmp/a-cda298.o:(foo)

## PE/COFF

PE 有一个“分组段（Grouped Sections）”的概念：如果段名包含 `$`，链接器会丢弃 `$` 及其后的字符。因此，一个名为 `.text$name` 的对象段实际上会贡献到映像（image）中的 `.text` 段。

`.CRT$XCU` 是全局初始化器段（类似于 ELF 的 `SHT_INIT_ARRAY`）。一个 `.CRT$XCU` 位于 `IMAGE_COMDAT_SELECT_ASSOCIATIVE` 段中，如果它引用一个 `IMAGE_SCN_LNK_COMDAT` 文本段，则可以被垃圾回收。

### lld-link

- 定义了由 `/include:` 指定的符号的段
- 定义了由 `llvm.used` 指定的符号的段（在比特码（bitcode）中，`/include:` 解决方法已经太晚）
- 定义了由 `/export:` 指定的符号的段
- 如果指定了 `/delayload`，则定义了延迟加载辅助函数的段

### 其他

不幸的是，额外的 GC 根需要链接器选项。对于局部符号（local symbol），没有好的方法来保留其定义，因为无法使用 `/include:`。使用一个唯一名称的 COMDAT，其名称被 `/include:` 指令引用，是一种可能的解决方法。

`__attribute__((used))` 防止符号被链接器段 GC 移除。由于上述限制，在 LLVM 中，此属性对局部符号无效。

## Mach-O

现代 Mach-O 派生自 a.out 的一个变体，并保留了一些严重的限制。有一些技术可以解除这些限制，但你会在结果中看到不优雅之处。例如，你不能有超过 255 个段。值得庆幸的是，有一个有趣的特性 `.subsections_via_symbols`。当其他目标文件格式引入更多段并为每个段定义一个单独的符号时，`.subsections_via_symbols` 使用一个单一的段，并让符号将该段分割成逻辑上独立的片（pieces）。这是一个非常棒的发明，绕过了这个限制。

```plaintext
.section __TEXT,__text,regular,pure_instructions
.globl _a
_a:
  ...

.globl _b
_b:
  ...
```

因为 `.subsections_via_symbols` 始终启用，`-ffunction-sections` 和 `-fdata-sections` 是空操作（no-op）。

当在声明上指定 GNU 属性 `__attribute__((used))` 时，关联的符号会获得一个 `.no_dead_strip` 指令以保持其活跃。在目标文件中，该位是 `N_NO_DEAD_STRIP`。

可以在段上指定段属性 `no_dead_strip` 以保持其活跃。在目标文件中，该位是 `S_NO_DEAD_STRIP`。

可以在段上指定段属性 `live_support`。如果该段引用的任何段是活跃的，则该段本身也是活跃的。在目标文件中，该位是 `S_ATTR_LIVE_SUPPORT`。此属性被 `__TEXT,__eh_frame` 使用，可以被视为泛化的 `SHF_LINK_ORDER`。

## LLVM IR

全局变量 `llvm.used` 是一个 appending linkage 数组，包含一个 `GlobalValue`（大部分是 `GlobalObject`）列表。如果一个符号出现在列表中，编译器、汇编器和链接器都不能丢弃它。

全局变量 `llvm.compiler.used` 是一个 appending linkage 数组，包含一个 `GlobalValue`（大部分是 `GlobalObject`）列表。这与 `llvm.used` 类似，不同之处在于链接器可以丢弃该符号。

GNU 属性 `__attribute__((used))` 在 ELF 上降级为 `llvm.compiler.used`，在 COFF/Mach-O/wasm 上降级为 `llvm.compiler.used`。

## 链接时优化（Link-time optimization）

代码生成选项可以分为 IR 生成选项（例如 `-g`）和目标文件生成选项（例如 `-ffunction-sections -fdata-sections`）。没有 LTO（链接时优化）时，你通常不会看到两者之间的界线，因为两者都在生成目标文件时起作用。有了 LTO，区别就更清晰了：IR 生成选项影响 `.c` -> `.ll`/`.bc`（`.o` 也常用于比特码文件），目标文件生成选项影响 `.ll`/`.bc` -> `.o`。在 LLVM 中，`-ffunction-sections` 和 `-fdata-sections` 是目标文件生成选项，不影响 IR 生成。ld.lld 和 `LLVMgold.so` 会自动启用函数段和数据段。

在 LLVM LTO 中，有一个默认启用的死代码剥离功能（`-mllvm -compute-dead=true`）。它计算死符号列表（`computeDeadSymbolsWithConstProp`），即无法从一个保留符号到达的符号。对于 ThinLTO，这可以减少编译时间（因为更少的函数导入），并改善内部化（因为更少的导入/导出）。在 `thinBackend` 中，这些死符号会被丢弃。

一个自然的问题是，既然有了 LTO，为什么 `--gc-sections` 仍然有用？

对于常规 LTO，由编译器生成的极少段会被 `--gc-sections` 丢弃。它们不被丢弃的原因如下：

- LLVM IR 中的一些常量引用可以通过目标特定的优化丢弃（例如 `memcpy(..., &constant, sizeof(constant));`）。
- 由于阶段排序（phase ordering）问题，一些定义不会被优化器丢弃。

对于 ThinLTO，有更多段会被 `--gc-sections` 丢弃：

- ThinLTO 可能导致定义被导入到其他模块。原始定义可能在导入后变得不必要。
- 定义可能在模块内优化后仍然存在。在导入之后，`computeDeadSymbolsWithConstProp` 之后的一轮（模块间）IR 优化可能使得该定义变得不必要。
- 符号解析（Symbol resolution）是保守的。

关于符号解析，符号解析发生在 LTO 之前，LTO 发生在 `--gc-sections` 之前。符号解析过程可能是保守的：它可能告知 LTO 某些符号被常规目标文件引用，而在 GC 阶段，由于具有更精确 GC 根的段被丢弃，这些引用实际上并不存在。

## Linux 内核

自 v4.10 起，提供了 `CONFIG_LD_DEAD_CODE_DATA_ELIMINATION` 配置选项，以利用 `ld --gc-sections`。

## Mach-O

- 定义了由 `-u`、`-e` 或 `-exported_symbol` 指定的符号的段
- 定义了具有 `N_NO_DEAD_STRIP` 属性或 `ReferencedDynamically` 属性的符号的段
- 具有 `S_ATTR_NO_DEAD_STRIP` 标志的段

## Windows `link.exe /OPT:REF`

在 `link.exe` 中，垃圾回收仅对 COMDAT 段有效。这在实践中不是主要问题，因为使用函数段时，每个文本段都在一个 COMDAT 中（无论是 `IMAGE_COMDAT_SELECT_NODUPLICATES` 还是 `IMAGE_COMDAT_SELECT_ANY`）。

未解析的外部符号（Unresolved external symbols）在垃圾回收之前诊断，这可以通过 `/force:unresolved` 或 `/force` 抑制。[https://developercommunity.visualstudio.com/t/unresolved-external-symbol-referenced-in-function/1016851](https://developercommunity.visualstudio.com/t/unresolved-external-symbol-referenced-in-function/1016851)
