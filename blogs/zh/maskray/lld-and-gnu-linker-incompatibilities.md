---
title: LLD 与 GNU 链接器兼容性差异
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2020-12-19-lld-and-gnu-linker-incompatibilities'
original_language: en
published: 2020-12-19
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:35236d176dba5e62'
translated: true
---

> 原文：[LLD 与 GNU 链接器的兼容性差异](https://maskray.me/blog/2020-12-19-lld-and-gnu-linker-incompatibilities)　·　MaskRay（宋方睿）

[2020-12-19](https://maskray.me/blog/2020-12-19-lld-and-gnu-linker-incompatibilities)

# LLD 与 GNU 链接器兼容性差异

更新于 2024 年 6 月。

副标题：ld.lld 能直接替代 GNU ld 吗？

本文源于有人质疑 LLD 网站上“直接替代”的说法（讨论针对类 Linux 的 ELF 工具链）：

> LLD 是 LLVM 项目的链接器，可以直接替代系统链接器，运行速度也远快于后者。它还提供了对工具链开发者有用的功能。

99.9% 的软件无需修改就能使用 ld.lld。某些使用链接器脚本的程序可能需要适配，而这通常源于脆弱的假设：它们过度依赖 GNU ld 本就应当修正的行为。因此，我为这一说法进行了辩护。

Piotr Kubaj 表示，这更像营销术语而非技术术语，目的是让现有用户觉得“它和你熟悉的一样，只是更好！”。我认为这在某些方面不无道理：对许多应用而言，ld.lld 的速度远快于 GNU ld，内存占用也低得多。更重要的是，ld.lld 为这一领域增加了第三种选择，给双方带来竞争压力，激励改进，也促使未来的功能与扩展更加标准化。我订阅 binutils 邮件列表的原因之一，就是希望参与它的设计过程（我很自豪自己能在多项新功能的早期发现问题）。

总之，我认为记录 ld.lld 与 GNU ld 的 ELF 移植之间的兼容性问题很有价值，不仅方便他人，也方便未来的自己，因此写下本文。我也会尽量介绍 GNU gold 的行为。

下面是一份很长的列表。请记住，许多兼容性问题其实无关紧要，用户可能永远也碰不到；其中不少内容只用于教学和个人备忘。确实有一些用户可感知的差异，但 GNU ld 与 ld.lld 双方也都把相当多的问题标为 WONTFIX。ld.lld 是较新的链接器，历史兼容负担更少，有时可以选择更好的默认行为，也能拒绝不必要的功能。GNU ld 的不同移植中则存在大量重复功能，同一功能在移植 A 和移植 B 中表现不同也很常见。

- GNU 在 `gc-sections requires either an entry or an undefined symbol``-r --gc-section` 链接时报告 ld.lld`gc-sections requires either an entry or an undefined symbol`。ld.lld[https://reviews.llvm.org/D84131#2162411](https://reviews.llvm.org/D84131#2162411) 不会报错。我不确定这种诊断是否有用（这是一种不常见的用例，其中 GC 根多于显式的链接器选项）。
- `-no-pie` 链接的默认映像基址不同。例如在 x86-64 上，GNU ld 默认为 0x400000，ld.lld 默认为 0x200000。
- GNU ld 在复制非 `STT_SECTION``STB_LOCAL` 符号时会合成一个 `STT_FILE` 符号，ld.lld 不会。

    - `STT_FILE` 符号名就是输入文件名。对于编译器驱动指定的 `crti.o`、`crtn.o` 等启动文件，其绝对路径会进入链接映像。对部分用户而言，这会泄露工具链路径，破坏本地构建的确定性。
    - 我提交了 [LLVM #47367](https://github.com/llvm/llvm-project/issues/47367) 和 [binutils #26822](https://sourceware.org/bugzilla/show_bug.cgi?id=26822)。binutils 2.36 起改用基本文件名。
- 默认库路径。

    - GNU ld 有默认库路径。
    - ld.lld 没有。这是有意为之，因此无法接受用于 NetBSD 的 [D70048](https://reviews.llvm.org/D70048)。
- GNU ld 支持组合短选项。拼错选项或使用尚未实现的选项时，这有时会产生意外行为：例如 `-no-pie` 会被解释为 `-n -o -pie`，因为 GNU ld 2.35 尚未实现 `-no-pie`。Nick Clifton 提交了 `Update the BFD linker so that it deprecates grouped short options.`，开始弃用这一 GNU ld 功能。ld.lld 从不支持组合短选项。
- 在一个输出节中混用 SHF_LINK_ORDER 与非 SHF_LINK_ORDER 输入节。

    - ld.lld 在输入节描述内部排序，并允许任意混合。
    - GNU ld 不允许混合这两类节（[问题 26256](https://sourceware.org/bugzilla/show_bug.cgi?id=26256)，H.J. Lu 提供了补丁）。
- ld.lld 默认启用 `-z relro`。这可能不是理想的默认值，但现在很难更改；我在 [LLVM #48549](https://bugs.llvm.org/show_bug.cgi?id=48549) 中留有评论。对非 Linux/FreeBSD 的 BFD 仿真（例如 `-m aarch64elf`），GNU ld 会对 `-z relro` 和 `-z norelro` 发出警告。
- 不同的归档成员提取语义。详见 [http://lld.llvm.org/ELF/warn_backrefs.html](http://lld.llvm.org/ELF/warn_backrefs.html)。
- 如果 `def.a` 无法满足此前的未解析符号，ld.lld 的 `--warn-backrefs` 会对 `def.a ref.o def.so` 发出警告。ld.lld 把定义解析到 `def.a`，GNU 链接器则解析到 `def.so`。
- GNU 的 `-static` 传统上是 `-Bstatic` 的同义词。最近在 x86 上已修改为行为与 `gold -static` 类似，即不允许链接共享对象。ld.lld -staticld.lld `-static` 仍然是 -Bstatic 的同义词。`-Bstatic`.
- GNU 链接器有默认的 `--dynamic-linker`. ld.lld 没有。
- GNU ld 会更激进地丢弃空段。ld.lld 不会丢弃包含空输入段的输出段。
- GNU ld 有 architecture-specific 针对引用未定义弱符号的重定位的体系结构相关规则。我不认为 GNU ld 的行为可以简单概括（即使是维护者也做不到！）ld.lld 的则是一致的。
- 创建 `.interp` 的条件不同。我认为 GNU ld 的规则很难描述。
- `--no-allow-shlib-undefined` 和 `--rpath-link`

    - GNU ld 跟踪所有共享对象（传递的 `DT_NEEDED` 依赖），并模拟动态加载器的行为，从而对更多情况发出警告。
    - gold 和 ld.lld 实现了简化版本：当共享对象的所有 `DT_NEEDED` 依赖都作为输入文件出现时发出警告。
    - ld.lld 接受但忽略 `--rpath-link`
- `--fatal-warnings`

    - GNU ld 仍会报告 `warning: ...`。
    - ld.lld 改为报告 `error: ...`。
- `--no-relax`

    - GNU ld：禁用 `R_X86_64_[REX_]GOTPCRELX`
    - ld.lld：14.0.0 之前不执行任何操作（[D113615](https://reviews.llvm.org/D113615)）
- GNU ld 的内部链接器脚本会将 `.ctors` 放入 `.init_array`。gold 默认启用 `--ctors-in-init-array`，效果相同。ld.lld 未实现该功能。
- ld.lld 将 `.rodata`（以及其他 `SHF_ALLOC` 且非 `SHF_WRITE`-non-`SHF_EXECINSTR` 段）放在 `.text`（以及其他 `SHF_ALLOC` 且 `SHF_EXECINSTR` 段）之前。
- `.symtab`/`.shstrtab`/`.strtab` 在链接器脚本中。

    - GNU ld 会忽略，因此 `--orphan-handling=` 不会警告或报错。
    - ld.lld 会遵守该设置
- GNU ld 会把 `.text`、`.tbss` 等节视为特殊节（`bfd_elf_special_section`）。当 `.text` 作为输出节存在时，即使向其中加入带 `SHF_WRITE` 标志的输入节，它也不会获得 `SHF_WRITE` 标志。
- 链接器脚本中的 `ADDR(.foo)` 能否保留一个空的输出段。

    - GNU ld：不会。相对于这种空节的符号赋值可能得到异常的 `st_shndx`。
    - ld.lld：会。
- GNU ld 不会在 `.rela.eh_frame` 或 `-r` 模式下产生 `--emit-relocs`。gold 和 ld.lld 会生成 `.rela.eh_frame`.
- GNU ld 会对 `.dynstr` 和 `.strtab` 进行尾部合并，但 ld.lld 不会。
- GNU ld 默认会对其他 `SHF_MERGE|SHF_STRINGS` 段进行尾部合并。ld.lld 仅在使用了 `-O2`.
-  选项时才执行尾部合并。`R_X86_64_JUMP_SLOT` 如果一个未定义符号同时被 `R_X86_64_GLOB_DAT` (non-lazy)

    - GNU ld 生成带 `R_X86_64_GLOB_DAT` 重定位的 `.plt.got`，从而可以省略 `R_X86_64_JUMP_SLOT`，减少动态重定位数量。
    - ld.lld 没有实现这一优化，因为它自然需要多遍扫描重定位，而 ld.lld 目前不这样做。[LLVM #32938](https://bugs.llvm.org/show_bug.cgi?id=32938)
- GNU ld 会松弛某些形式的 `R_X86_64_GOTPCREL` 重定位（例如 `movq foo@GOTPCREL(%rip), %reg -> leaq foo(%rip), %reg`），ld.lld 从不松弛 `R_X86_64_GOTPCREL` 重定位。
- GNU 链接器赋予 `.gnu.linkonce*` 段以 COMDAT 段语义。ld.lld 直接忽略这些段。[https://bugs.llvm.org/show_bug.cgi?id=31586](https://bugs.llvm.org/show_bug.cgi?id=31586) 记录了何时可以移除这个权宜之计。
- GNU ld 会同时添加 `PT_PHDR` 和 `PT_INTERP`。共享对象通常没有这两个程序头；在 ld.lld 中，只要地址分配仍允许放置程序头，就一定会添加 `PT_PHDR`。
-  条件是创建动态符号表 `.dynsym`.

    - ld.lld：存在输入共享对象，或指定了 `-pie`/`-shared`、`--export-dynamic`。
    - GNU ld 的规则相当复杂，不过 `--export-dynamic` 并不特殊。
- `--export-dynamic-symbol`

    - gold 的选项会隐含启用 `-u`。
    - GNU ld（2.35 起）和 ld.lld 都不会隐含启用 `-u`。
-  中，一个已定义的 GNU ld 中，一个已定义的 `foo@v` 可以抑制对定义了 `foo@@v1`. ld.lld 的归档成员的提取。[ 关于符号版本控制的所有内容](https://maskray.me/blog/2020-11-26-all-about-symbol-versioning) 了解详情。
-  默认的程序头。

    - 使用传统的 `-z noseparate-code` 时，GNU ld 默认采用 `RX/R/RW` 程序头布局；使用 `-z separate-code`（binutils 2.31 起为 Linux/x86 默认值）时，默认采用 `R/RX/R/RW` 布局。
    - ld.lld 默认为 `R/RX/RW(RELRO)/RW(non-RELRO)`；使用 `--rosegment` 时改为 `RX/RW(RELRO)/RW(non-RELRO)`。
    - 把所有 R 段放在 RX 之前更好，因为可以节省一个程序头并降低对齐成本。
    - ld.lld 拆分 RW 段可节省一次 maxpagesize 对齐，使链接映像更小。
    - 这会打破一些所谓“文本段”位于所谓“数据段”之前的假设。
    - 例如，某些程序假定 `.text` 是文本段的第一个节，并指定 `-Ttext=0`，把 `PF_R|PF_X` 程序头放在 p_vaddr=0。这个假设很脆弱，应当避免。需要 `PT_PHDR` 时可改用 `--image-base=0`；不需要 `PT_PHDR` 时可改用 `.text 0 : { *(.text .text.*) }`。
    - 如果 `-Ttext=` 或 `--section-start` 指定的输出节地址低于该基址，结果通常并非本意。ld.lld 21 起会报错。[LLVM #140187](https://github.com/llvm/llvm-project/pull/140187/)
- ld.lld 将 `.iplt` 放入同名输出节，GNU ld 和 gold 则直接使用 `.plt`。ld.lld 的做法能凸显这一棘手特性，也让符号化工具无需处理混合的 PLT 条目。
- GNU ld 和 gold 在 `__rela_iplt_start` 模式下定义 `-no-pie` 模式，但在 `-pie` 模式下则不会。glibc 的 `csu/libc-start.c` 在静态链接时需要它，但在静态 pie 模式下则不需要。ld.lld 不区分 `-no-pie`, `-pie` 和 `-shared`. [https://bugs.llvm.org/show_bug.cgi?id=48674](https://bugs.llvm.org/show_bug.cgi?id=48674)
- ld.lld 默认使用 `--no-apply-dynamic-relocs`。GNU 会用链接时 GOT 值填充 link-timeGNU，`--no-apply-dynamic-relocs` 仅支持 aarch64 的 [https://sourceware.org/bugzilla/show_bug.cgi?id=25891](https://sourceware.org/bugzilla/show_bug.cgi?id=25891).
- 在对 `R_X86_64_REX_GOTPCRELX`, GNU 时，如果放松会导致重定位溢出，GNU ld 会抑制该放松。ld.lld 不执行此检查。
- GNU 和 gold 允许用 `--exclude-libs=b` 来隐藏 `b.a`. ld.lld 要求使用 `--exclude=libs=b.a`.
- ld.lld 无法回收不属于组、且不带 SHF_LINK_ORDER 的 `.gcc_except_table*` 节；GNU ld 可以。对于 Clang\>=13，`clang -fbinutils-version=2.36` 可以在 `.gcc_except_table*` 上设置 `SHF_LINK_ORDER`，从而允许回收。
- 在 GNU ld 中，未被需要的（`--as-needed`）共享对象所引用的定义不会导出到 `.dynsym`[PR26551](https://sourceware.org/bugzilla/show_bug.cgi?id=26551)。gold 和 ld.lld 会导出这类定义。
- ppc64：GNU ld 将 `.TOC.` 定义为 `.got` 输出节加 0x8000，ld.lld 则选择输入节 `.got` 加 0x8000。据我所知，所有架构都相对于输入节 `.got` 定义 GOT 重定位。
- 当采用复制重定位的符号带有别名时（例如 `environ`、`_environ`、`__environ`），ld.lld 会复制所有别名，GNU ld 只复制一部分。
- 在 GNU ld 中，不在 `--retain-symbols-file` 中的符号会被排除出 `.symtab`，但 `.dynsym` 不受影响；而 ld.lld 会同时从 `.symtab` 和 `.dynsym`. [https://github.com/llvm/llvm-project/issues/91055](https://github.com/llvm/llvm-project/issues/91055)

### `--as-needed`

在 GNU ld 和 gold 中，一个共享对象会在以下情况下获得 `DT_NEEDED` 条目：

- 在以 --no-as-needed 模式被链接至少一次时（i.e. `--as-needed a.so --no-as-needed a.so` =\> 即需要）
- 或者它有一个定义，解析了某个非 non-weak 弱引用

在 GNU ld 中，一个 as-needed 的共享对象类似于归档文件。它应该出现在引用之后。

在 ld.lld,

- 它以 `--no-as-needed` 模式被链接至少一次时（i.e. `--as-needed a.so --no-as-needed a.so` =\> 即需要）
- 或者它有一个定义，解析了某个非 non-weak 弱引用，且该引用来自一个活跃段（未被 `--gc-sections`)

```plaintext
# RUN: split-file %s %t
# RUN: cc -c %t/a.s -o %t/a.o
# RUN: cc -shared -Wl,--soname=b.so %t/b.s -o %t/b.so
## DT_NEEDED entry.
# RUN: ld.bfd --gc-sections %t/a.o --as-needed %t/b.so -o %t.out
## No DT_NEEDED entry.
# RUN: ld.lld --gc-sections %t/a.o --as-needed %t/b.so -o %t.out

#--- a.s
.globl _start
_start:

.section .text.a,"ax"
call foo

#--- b.s
.weak foo
foo:
 ret
```

### —wrap 的语义 --wrap

GNU ld 和 ld.lld 的 `--wrap` 语义略有不同。我用“略有”一词，是因为在大多数用例中，用户不会察觉到差异。

在 GNU ld 中，`--wrap` 只作用于未定义符号；在 ld.lld 中，`--wrap` 发生在所有其他符号解析步骤之后。实现方式是改写每个目标文件的符号表（`foo -> __wrap_foo; __real_foo -> foo`），从而重定向所有指向 `foo` 或 `__real_foo` 的重定位。

ld.lld 语义的优点是非 LTO、LTO 与可重定位链接的行为一致。我为 GNU ld 提交了[问题 26358](https://sourceware.org/bugzilla/show_bug.cgi?id=26358)。

```plaintext
# GNU ld: call bar
# ld.lld: call __wrap_bar
  call bar
.globl bar
bar:
```

如果存在 `__real_foo` 引用但 `foo` 不存在，GNU 链接器可以将 `__real_foo` 引用重定向到 `foo`. ld.lld。ld.lld 不做任何处理。这个差异在实践中无关紧要。

```plaintext
# REQUIRES: x86
# RUN: rm -rf %t && split-file %s %t
# RUN: llvm-mc -filetype=obj -triple=x86_64 %t/a.s -o %t/a.o
# RUN: llvm-mc -filetype=obj -triple=x86_64 %t/b.s -o %t/b.o
# RUN: rm -f %tb.a && llvm-ar r %tb.a %t/b.o
# RUN: ld.lld %t/a.o %tb.a -o %t/lld --wrap pthread_create -z undefs
# RUN: ld.bfd %t/a.o %tb.a -o %t/bfd --wrap pthread_create -z undefs
# RUN: gold %t/a.o %tb.a -o %t/bfd --wrap pthread_create --unresolved-symbols=ignore-in-object-files

#--- a.s
.globl _start
_start:
.cfi_startproc
  call pthread_create
.cfi_endproc

#--- b.s
.global pthread_create
pthread_create:
.cfi_startproc
  ret
.cfi_endproc
```

### 引用相对于已丢弃输入节段的本地符号的重定位

- 如何解析引用与已丢弃的 `STT_SECTION` 符号关联的 `.debug_*` 输入节段的重定位

    - GNU ld 和 gold 会把重定位解析到胜出的节符号。
    - ld.lld 没有这套逻辑；ld.lld 11 定义了一些墓碑值。

> 具有 STB_LOCAL 绑定且相对于组中某个节段定义、包含在非该组的符号表节段中的符号表条目，在组成员被丢弃时必须一并丢弃。不允许从组外引用此符号表条目。

如果包含重定位的节带有 SHF_ALLOC 标志，ld.bfd/gold/lld 会报错。`.debug*` 节没有 SHF_ALLOC 标志，因此允许这类重定位。

lld 把这类重定位解析为 0。ld.bfd 和 gold 则通过一些 CB_PRETEND/PRETEND 逻辑，将其解析到胜出 comdat 组中的定义。这段代码很取巧，可能不适合 lld。

[https://bugs.llvm.org/show_bug.cgi?id=42030](https://bugs.llvm.org/show_bug.cgi?id=42030)

### ifunc 的规范 PLT 条目

如何处理引用 `STT_GNU_IFUNC`?

c.f. [GNU 间接函数](https://maskray.me/blog/2021-01-18-gnu-indirect-function).

### `__rela_iplt_start`

GNU、gold 在 `__rela_iplt_start` 模式下定义 `-no-pie`，但在 `-pie` 模式下不定义。ld.lld 无论使用 `__rela_iplt_start`、`-no-pie`, `-pie` 还是 `-shared`.

静态 pie 和静态 no-pie 重定位处理在 glibc 中差异很大。

- 使用特殊代码处理由 no-pie 分隔的魔术数组。`__rela_iplt_start/__rela_iplt_end`.
- 使用 self-relocation 来处理 `R_*_IRELATIVE`。以上魔术数组代码也会被执行。如果 `__rela_iplt_start`/`__rela_iplt_end` 被定义（如 ld.lld 所做的），在 `0 < __rela_iplt_start < __rela_iplt_end` 中我们会得到 `csu/libc-start.c`. `ARCH_SETUP_IREL`。当解析第一个已处理过的重定位时，

nsz 有一个 glibc 补丁，将 self-relocation 移到后面，以便为 ifunc 解析器做好所有设置。

## 文本重定位

- 在 GNU 中，`-z notext`/`-z text`/unspecified 是一个 tri-state.。对于 `-z notext`/unspecified，动态标签 `DT_TEXTREL` 和 `DF_TEXTREL` 按需添加。如果未指定且 GNU 配置了 `--enable-textrel-check=warning`，则会发出警告。
- ld.lld 有两个状态，并在指定了 `DT_TEXTREL` 和 `DF_TEXTREL`，如果 `-z notext` 被指定。
- GNU 支持更多重定位类型作为文本重定位。

LLD16.0.0 改变了与 `.eh_frame` 中绝对重定位相关的行为。参见[杂项](#misc).

```cpp
echo 'void bar(); int main() { try { bar(); } catch (...) {} }' > a.cc
echo 'void bar() {}' > b.cc
clang++ -m32 -fno-pic -no-pie -fuse-ld=lld -z notext a.cc b.cc
```

## Short-range 绝对重定位

```sh
cat > a.s <<e
.globl _start; _start:
.data; .short _start
e
llvm-mc -filetype=obj -triple=i686 a.s -o x86_32.o
llvm-mc -filetype=obj -triple=x86_64 a.s -o x86_64.o
```

对于短程绝对重定位（例如 `R_X86_64_16` 和 `R_X86_64_32`），GNU ld 的 x86_64 移植无论使用 `-z text` 还是 `-z notext` 都会拒绝。ld.lld 同样会拒绝：1  
2  
3  
4  
5  
6  
7  
% ld.bfd -pie x86_64.o && readelf -Wr a.out  
ld.bfd: x86_64.o: relocation R_X86_64_16 against symbol `_start' can not be used when making a PIE object; recompile with -fPIE  
ld.bfd: failed to set dynamic section sizes: bad value  
% ld.lld -pie x86_64.o  
ld.lld: error: relocation R_X86_64_16 cannot be used against symbol '_start'; recompile with -fPIC  
\>\>\>定义于 x86_64.o  
\>\>\>引用自 x86_64.o：(.data+0x0)

的 link-time 链接时地址可以用 `_start` 表示。然而，使用 `R_X86_64_16` 时，语义要求 `-pie` 的运行时地址可表示，但事实并非如此。因此链接器会报错。这一行为已在 run-time`_start` 的许多其他端口中实现。GNU

（要使 `R_X86_64_16` 重定位被接受，该重定位应引用一个绝对符号（`SHN_ABS`）才能被接受。）

GNU ld 的 i386 移植不知为何会在 PIC 链接中接受这类短程重定位，可能是某项未实现的检查后来被人依赖。x86-32 基本已被视为遗留架构，因此现在或许没有必要再修改链接器。1  
2  
3  
% ld.bfd -m elf_i386 -pie x86_32.o && readelf -Wr a.out  
  
此文件中没有重定位。

ld.lld 在默认 `-z text` 下的行为与其他移植一致，都会拒绝短程重定位。不过，为 x86-32 链接指定 `-z notext` 时，ld.lld 会把短程重定位转换为动态重定位，也就是文本重定位。我认为转换 `R_386_8` 和 `R_386_16` 并非有意为之；只有 `R_386_32`、`R_386_TLS_LE` 与 `R_386_TLS_LE_32` 应支持作为文本重定位。之所以出现这一行为，是因为 ld.lld 通常比 GNU ld 支持更少的文本重定位类型。x86-32 链接器历来有许多绕过旧代码问题的特殊处理，其中一些可能早已不再需要。1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
% ld.lld -pie x86_32.o  
ld.lld: error: relocation R_386_16 cannot be used against symbol '_start'; recompile with -fPIC  
\>\>\> 在 x86_32.o  
\>\>\> 被 x86_32.o 引用：(.rodata+0x0)
% ld.lld -pie x86_32.o -z notext && readelf -Wr a.out  
  
位于偏移量 0x170 的重定位节 '.rel.dyn' 包含 2 条目：
  偏移量 信息 类型 符号值 符号名称
00000180 00000014 R_386_16  
000031f4 00000014 R_386_16

## 链接器脚本

- 未指定 `-T`（`--script`）或 `-dT`（`--default-script`）时，GNU ld 使用内部链接器脚本；gold 和 ld.lld 没有内部链接器脚本。

    - 我关闭了 [LLVM #51309](https://bugs.llvm.org/show_bug.cgi?id=51309)，因为输出内部链接器脚本会显著增加复杂度，却没有足够收益。
    - 某些内置处理无法序列化为链接器脚本。
- 如果既未指定 `FILEHDR` 也未指定 `PHDRS`，并且 `SHF_ALLOC` 节的最小地址被设置为添加头部将需要额外添加一个页面，那么 ld.lld 不会将 ELF 头部和程序头部放入 `PT_LOAD` 程序头部中。`FILEHDR``PHDRS` 未指定，并且 `SHF_ALLOC` 节的最小地址被设置为添加头部将需要额外添加一个页面，那么 `SHF_ALLOC` 不会将 ld.lld 头部和程序头部放入一个 ELF 程序头部中。`PT_LOAD`
- 某些链接器脚本命令未在 ld.lld 中实现，例如作为 `ALIGN()` 兼容别名的 `BLOCK()`。GNU ld 把 `BLOCK` 记录为兼容别名，而且它并未广泛使用，因此没有理由在 ld.lld 中保留这种特殊处理。
- ld.lld 不识别某些语法。例如它识别 `*(EXCLUDE_FILE(a.o) .text)`，却不识别 `EXCLUDE_FILE(a.o) *(.text)`（[LLVM #45764](https://bugs.llvm.org/show_bug.cgi?id=45764)）。

    - 在我看来，无法识别这些语法容易误导用户。
    - 如果已经支持一种完成某件事的写法，即使它还有其他等价语法，我们也不一定只为求完整而支持所有写法。
- 当输出节没有输入节且只含符号赋值时（例如 `.foo { symbol = 42; }`，[参考](https://sourceware.org/binutils/docs/ld/Output-Section-Discarding.html)），GNU ld 会消除它。ld.lld 会保留这类节，除非所有符号赋值都是未被引用的 PROVIDED。
- [孤儿节放置不同](https://maskray.me/blog/2024-06-02-understanding-orphan-sections). GNU ld 具有非常复杂的规则，并且某些节名称具有特殊语义。ld.lld 采纳了其一些核心思想，但做了大量简化：ld.lld 采纳了其一些核心思想，但做了大量简化：

    - 为输出节分配等级
    - 输出节会放在符号赋值之后。我们应该找时间把它记录下来。[LLVM #42327](https://bugs.llvm.org/show_bug.cgi?id=42327)
- 对处理链接器脚本时发现的错误，ld.lld 可能重复报告多次（例如 `ASSERT` 失败）。GNU ld 也有这类问题，但可能少得多。
- `SORT` 命令

    - GNU ld：[文档](https://sourceware.org/binutils/docs/ld/Input-Section-Basics.html#Input-Section-Basics)提到了该功能，但行为奇怪且不直观。我发起了讨论 [输入节描述中的 SORT 与多个模式](https://sourceware.org/pipermail/binutils/2020-November/114083.html)。
    - ld.lld 在输入节描述内部执行排序。[D91127](https://reviews.llvm.org/D91127)
- 在 ld.lld 中，`AT(lma)` 会强制创建新的 `PT_LOAD` 程序头。若 LMA 地址连续，GNU ld 可以复用前一个 `PT_LOAD` 程序头。`lma-offset.s`
- 在 ld.lld 中，非 `SHF_ALLOC` 节的 `sh_addr` 始终为 0。GNU ld 允许非零 `sh_addr`，但引用这类节的 `STT_SECTION` 重定位其实没有意义。
- 输出节描述中的点号赋值（例如 `. = 4;`）。

    - GNU ld：点号相对于起始位置前进到 4。若考虑右侧的 `.` 与 `ABSOLUTE(.)`，我认为其行为并不一致。
    - ld.lld：把点号移动到地址 0x4，通常会触发 `unable to move location counter backward` 错误。[LLVM #41169](https://bugs.llvm.org/show_bug.cgi?id=41169)

### 输出节内的符号赋值

参见一个关于 GNU ld 和 lld 行为的示例。GNU ld 和 lld 行为的示例。
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
// a.s  
nop
  
// a.x  
SECTIONS {  
 . = 0x1204;  
 .text : {  
 *(.text)  
 /* dot is 0x1205 */  
 a1 = ALIGN(32); /* = ALIGN(ABSOLUTE(.), 32) */  
 a2 = 32;  
 a2_1 = a2;  
 a3 = ABSOLUTE(0x1225);  
 a3_1 = a3;  
 a4 = ABSOLUTE(0x1225) + 1;  
 a4_1 = a4;  
 a5 = ADDR(.text);  
 }  
 /DISCARD/ : { *(.dynsym) *(.gnu.hash) *(.hash) *(.dynstr) }
}

对于 `bar = 32;`）在输出段描述中，GNU ld 将 `bar` 定义在相对于输出段起始位置偏移 32 处。类似地，`. = 32` 将位置计数器前进到相对于输出段起始位置偏移 4 处。对于输出段外部的符号赋值，行为有所不同，而 `ABSOLUTE` 具有特殊但不清晰的语义。当考虑二元运算符时，行为更加令人困惑。

ld.lld 根本没有实现输出节内相对偏移那套特殊但含糊的语义。

```plaintext
% as a.s -o a.o

# I choose -pie because st_shndx can be different in GNU ld's -no-pie mode. I think both ld.lld -no-pie and ld.lld -pie should be consistent with ld.bfd -pie, instead of ld.bfd -no-pie.
% ld.bfd -pie a.o -T a.x
% readelf -W -s a.out
...
     2: 0000000000001220     0 NOTYPE  GLOBAL DEFAULT    1 a1
     3: 0000000000001225     0 NOTYPE  GLOBAL DEFAULT  ABS a3
     4: 0000000000002429     0 NOTYPE  GLOBAL DEFAULT    1 a3_1
     5: 000000000000242a     0 NOTYPE  GLOBAL DEFAULT    1 a4_1
     6: 0000000000001204     0 NOTYPE  GLOBAL DEFAULT    1 a5
     7: 0000000000001224     0 NOTYPE  GLOBAL DEFAULT    1 a2
     8: 0000000000001224     0 NOTYPE  GLOBAL DEFAULT    1 a2_1
     9: 0000000000001226     0 NOTYPE  GLOBAL DEFAULT  ABS a4

% ld.lld -pie a.o -T a.x  # lld makes many symbols absolute
% readelf -W -s a.out
...
     2: 0000000000000020     0 NOTYPE  GLOBAL DEFAULT  ABS a2
     3: 0000000000001225     0 NOTYPE  GLOBAL DEFAULT  ABS a3
     4: 0000000000001226     0 NOTYPE  GLOBAL DEFAULT  ABS a4
     5: 0000000000001220     0 NOTYPE  GLOBAL DEFAULT  ABS a1
     6: 0000000000000020     0 NOTYPE  GLOBAL DEFAULT  ABS a2_1
     7: 0000000000001225     0 NOTYPE  GLOBAL DEFAULT  ABS a3_1
     8: 0000000000001226     0 NOTYPE  GLOBAL DEFAULT  ABS a4_1
     9: 0000000000001204     0 NOTYPE  GLOBAL DEFAULT    1 a5
```

为了可移植性，我仅推荐：

- `sym = .;` 在当前地址定义一个符号
- `. += 4;` 前进位置计数器。这比 `. = . + 4;`

### 输出段填充

当[填充模式](https://sourceware.org/binutils/docs/ld/Output-Section-Fill.html)是十六进制字面量（例如 0x90）时，它会自动复制成 32 位模式 0x90909090（`ld/ldexp.c:exp_get_fill`）。该行为不适用于十进制字面量或表达式。

```plaintext
.text : { *(.text) } =0x90        # set the fill pattern to 0x90909090
.text : { *(.text) } =0x90909090  # set the fill pattern to 0x90909090
.text : { *(.text) } =144         # set the fill pattern to 0x00000090
.text : { *(.text) } =0x90+0      # set the fill pattern to 0x00000090
```

此行为让我感到困惑（[PR30865](https://sourceware.org/bugzilla/show_bug.cgi?id=30865)). ld.lld 将 `=0x90` 视为与 `=144`.

### `PROVIDE`

在 GNU ld 中，PROVIDE 赋值的右侧仅在符号被引用时处理（`ld/ldexp.c:exp_fold_tree_1`）。因此，如果一个符号仅被 PROVIDE 赋值的右侧引用，则该符号不被视为被引用，并且 `PROVIDE` 不会定义它。

为简化起见，[ld.lld 未实现此特殊规则](https://github.com/llvm/llvm-project/issues/74771). 1  
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
作为 /dev/null -o a.o  
cat \> a.t \<\<e  
SECTIONS {  
 PROVIDE(f3 = 0x1000);  
 PROVIDE(f2 = f3);  
 PROVIDE(f1 = f2);  
 PROVIDE(foo = f1);  
}  
e  
ld.bfd a.o -T a.t -o a.bfd  
ld.lld a.o -T a.t -o a.lld  
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
% readelf -s a.bfd  
  
Symbol table '.symtab' contains 1 entry:  
 Num: Value Size Type Bind Vis Ndx Name  
 0: 0000000000000000 0 NOTYPE LOCAL DEFAULT UND  
% readelf -s a.lld  
  
Symbol table '.symtab' contains 4 entries:  
 Num: Value Size Type Bind Vis Ndx Name  
 0: 0000000000000000 0 NOTYPE LOCAL DEFAULT UND  
 1: 0000000000001000 0 NOTYPE GLOBAL DEFAULT ABS f3  
 2: 0000000000001000 0 NOTYPE GLOBAL DEFAULT ABS f2  
 3: 0000000000001000 0 NOTYPE GLOBAL DEFAULT ABS f1

GNU ld 会执行多次迭代，但某些移植（例如 x86）不允许迭代太多次。1  
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
% cat chain.t  
PROVIDE(f7 = 0x1000);  
PROVIDE(f6 = f7);  
PROVIDE(f5 = f6);  
PROVIDE(f4 = f5);  
PROVIDE(f3 = f4);  
PROVIDE(f2 = f3);  
PROVIDE(f1 = f2);  
PROVIDE(newsym = f1);  
% ld.bfd a.o -T chain.t  
ld.bfd:chain.t:2: undefined symbol `f7' referenced in expression

## `.note.GNU-stack`

链接器创建 `PT_GNU_STACK` 程序头以指示程序栈是否应可执行。

默认情况下，GNU ld 和 gold 会在一个可重定位目标文件不包含 `PF_X` 位的 `PT_GNU_STACK` 程序头中设置 `.note.GNU-stack`。此行为可通过配置选项 `--enable-default-execstack=no`.

ld.lld 忽略 `.note.GNU-stack`，并默认使用 `-z noexecstack`。

- Arch Linux 功能请求：[[binutils] 设置 --enable-default-execstack=no 配置选项](https://bugs.archlinux.org/task/75601)

## `.gnu.warning`

如果名为 `.gnu.warning` 的输入段包含在输出中，GNU 链接器将发出警告，警告消息从该段的内容中提取。1  
2  
3  
echo '.globl _start; _start: .section .gnu.warning; .asciz "hello"' \> a.s  
gcc -c a.s  
ld.bfd a.o # a.o: warning: hello

如果可重定位目标文件或共享目标文件中的段名为 `.gnu.warning.$symbol`, GNU 链接器将记录该符号名。如果该符号被某个可重定位目标文件引用，它们将发出警告。1  
2  
3  
4  
echo '.globl _start; _start: .section .gnu.warning._start; .asciz "hello"' \> a.s  
echo 'call _start; call _start' \> b.s  
gcc -c a.s b.s  
gcc -shared a.o -o a.so  
 1  
2  
3  
4  
5  
% ld.bfd a.o b.o  
ld.bfd: warning: hello  
% gold a.o b.o  
b.o(.text+0x1): warning: hello  
b.o(.text+0x6): warning: hello

GNU ld 可能会扫描符号表，并为每个设置了警告位的被引用符号报告一个警告。gold 将检查移至重定位扫描，并为每个引用报告一个警告。然而，这种方法引入了每个重定位的开销。per-relocation 的

ld.lld 没有实现该功能，目前也不清楚它是否有用。[LLVM #41353](https://github.com/llvm/llvm-project/issues/41353)

对于 GCC 和 Clang，我认为 `__attribute__((deprecated(...)))` (`-Wdeprecated-declarations`）是一个相当不错的替代方案。

对于非可重定位链接，ld.lld 会在 `.comment` 节中记录链接器版本信息。

GNU ld 自 2023 年 3 月起使用链接器脚本指令 `LINKER_VERSION` 记录此信息。外部链接器脚本用户可指定 `--enable-linker-version`.

## 杂项

我还会提及一些 ld.lld 的发布说明，这些说明可以展示早期版本中某些 GNU 不兼容性。（例如，如果某项功能在版本 N 中得到支持，则意味着在早期版本中不支持。当然，也有可能该功能在旧版本中有效，但在某个版本出现回退。不过，我并不知道此类情况的存在。）

LLD 16.0.0

- 早期版本在指定 `.eh_frame` 时可能会在 `-z notext` 中生成动态重定位。[https://reviews.llvm.org/D143136](https://reviews.llvm.org/D143136) 切换为规范的 PLT 条目。

LLD 12.0.0

- `-r --gc-sections` 已得到支持。
-  符号的归档成员提取语义默认（COMMON）与 `--fortran-common` ld 兼容。你可能想阅读 GNU 以了解详情。[存档中公共定义的语义](https://sourceware.org/pipermail/binutils/2020-August/112878.html)。这令人遗憾。
- `.rel[a].plt` 和 `.rel[a].dyn` 获取 `SHF_INFO_LINK` 标志。[https://reviews.llvm.org/D89828](https://reviews.llvm.org/D89828)

LLD 11.0.0

- ld.lld`--discard-all`/`--discard-locals` 在指定 `-r` 或 `--emit-relocs` 时，可以丢弃未使用的符号。[https://reviews.llvm.org/D77807](https://reviews.llvm.org/D77807)
- `--emit-relocs --strip-debug` 可以配合使用。[https://reviews.llvm.org/D74375](https://reviews.llvm.org/D74375)
- `SHT_GNU_verneed` 共享对象中的 non-default 版本符号原本可能导致 `--no-allow-shlib-undefined` 报错。[https://reviews.llvm.org/D80059](https://reviews.llvm.org/D80059)
- `DF_1_PIE` 会在 position-independent 可执行文件中设置。[https://reviews.llvm.org/D80872](https://reviews.llvm.org/D80872)
- 改善了输出段对齐和 LMA 区域相关的兼容性。[D75286](https://reviews.llvm.org/D75286)[D74297](https://reviews.llvm.org/D74297)[D75724](https://reviews.llvm.org/D75725)[D81986](https://reviews.llvm.org/D81986)
- `-r` 允许将 `SHT_X86_64_UNWIND` 合并为 `SHT_PROGBITS`。这使得 clang/GCC 生成的目标文件可以混合使用。[https://reviews.llvm.org/D85785](https://reviews.llvm.org/D85785)
- 在输入段描述中，文件名可以用双引号指定。`archive:file` 语法也已添加。[https://reviews.llvm.org/D72517](https://reviews.llvm.org/D72517)[https://reviews.llvm.org/D75100](https://reviews.llvm.org/D75100)
- 链接器脚本指定的空 `(.init|.preinit|.fini)_array` 现在允许与 RELRO. [https://reviews.llvm.org/D76915](https://reviews.llvm.org/D76915)

LLD 10.0.0

- ld.lld 支持`\`（将下一个字符视为 non-meta 字符）以及 `[!...]`（取反）在 glob 模式中使用。[https://reviews.llvm.org/D66613](https://reviews.llvm.org/D66613)

LLD 9.0.0

- 在使用 `DF_STATIC_TLS` 标志会在 i386 和 x86-64 上设置，当使用 initial-exec TLS 模型时。
- Linux 内核 arm32_7、arm64、powerpc64le 和 x86_64 移植的许多配置都可以用 ld.lld 链接。

LLD 8.0.0

- `SHT_NOTE` 段获得很高的排序等级（它们通常排在其他段之前）。[https://reviews.llvm.org/D55800](https://reviews.llvm.org/D55800)

在 LLD 7.0.0 时代，[D44264](https://reviews.llvm.org/D44264) 是我为 ld.lld 提交的第一个有意义但很简单的补丁。之后我参与了 `--warn-backrefs`，又开始修复版本化符号的复制重定位、重复 `--wrap`、节等级等棘手问题，并从代码审查中学到很多。在 8.0.0、9.0.0 和 10.0.0 时代，我修复了多项复杂问题，也改进了十余处其他功能。可以自信地说，除 MIPS ;-) 和某些 ISA 特有内容外，我熟悉代码库的每个角落。仍有一些挑战，例如集成 RISC-V 风格的链接器松弛与链接后优化，以及改进链接器脚本的某些方面；除此之外，ld.lld 已是工具链中稳定而完整的一部分。

一些零散的说明：

- 符号解析可能占用 10%~20% 的时间。理论上并行化可以改进这个过程，但很难夸大其中的挑战（如果再考虑确定性问题的话）。
- 要警惕功能蔓延。我从 ELF 设计讨论（尤其是在 generic-abi 上的讨论）以及 Solaris 的“链接器异类”中学到了很多。很抱歉这样说，但 ld.lld 上的一些开发确实属于此类。有时很难在不受支持的遗留特性和我们必须支持的遗留特性之间划清界限。
- ld.lld 的采用规模现在已经很大，以至于有时一个决策（比如某个选项的默认值）无法让所有人都满意。
