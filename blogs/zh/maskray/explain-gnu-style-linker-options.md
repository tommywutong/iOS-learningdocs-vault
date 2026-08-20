---
title: 解释 GNU 风格的链接器选项
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2020-11-15-explain-gnu-linker-options'
original_language: en
published: 2020-11-15
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:17820542dd551eee'
translated: true
---

> [解释 GNU 风格的链接器选项](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options)　·　MaskRay (宋方睿)

[2020-11-15](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options)

# 解释 GNU 风格的链接器选项

[中文版](https://maskray.me/blog/zh/2020-11-15-explain-gnu-linker-options)

更新于 2025 年 2 月

(首先庆祝一下 LLVM 2000 commits 达成！)

## 编译器驱动选项

在描述链接器选项之前，我们先介绍驱动选项的概念。user-facing 和 `gcc` 的 `clang` 对外选项称为驱动选项。某些驱动选项会影响传递给链接器的选项。其中许多选项与链接器的选项同名，并且除了传递给链接器同名选项的功能之外，通常还具有额外功能，例如：

- `-shared`：不设置 `-dynamic-linker`；不链接 `crt1.o`
- `-static`：不设置 `-dynamic-linker`；使用 `crtbegint.o` 而不是 `crtbegin.o`，使用 `--start-group` 链接 `-lgcc -lgcc_eh -lc`（它们存在（不良的）循环依赖）

`-Wl,--foo,value,--bar=value` 会将这三个选项 `--foo`, `value`、`--bar=value` 和 `response.txt` 传递给链接器。如果有大量链接选项，你可以将每一行写入文本文件 `-wl,@response.txt`.

注意，`-O2` 不会将 `-O2` 传递给链接器，但 `-Wl,-O2` 会。

- `-fno-pic,-fno-PIC` 是同义词，生成 position-dependent 位置相关代码。
- `-fpie,-fPIE` 分别称为小 PIE 和大 PIE。它们在 PIC 的基础上引入了一项优化：编译后的 .o 只能用于可执行文件。请参阅下面的 `-Bsymbolic`。
- `-fpic,-fPIC` 分别称为小 PIC 和大 PIC。它们生成 position-independent 位置无关代码。在 32 位 powerpc 和 sparc（即将淘汰的架构）上，这两种模式在代码生成上存在差异。在大多数架构上没有差异。

## 输入文件

链接器接受多种类型的输入。对于符号，每个输入文件的符号表会影响符号解析。对于段，只有常规目标文件中的段（称为输入段）会贡献给输出文件的段（称为输出段）。

- .o（常规目标文件）
- .so（共享对象）：仅影响符号解析
- .a（归档文件）

有关符号解析的详细信息，请参阅 [符号处理](https://maskray.me/blog/2021-06-20-symbol-processing)。

## 模式

链接器处于以下四种模式之一。该模式控制输出类型（可执行文件/共享对象/可重定位对象）。

- `-no-pie`（默认）：生成 position-dependent 位置相关可执行文件（`ET_EXEC`）。此模式的要求最为宽松：源文件可以使用 `-fno-pic, -fpie/-fPIE, -fpic/-fPIC`.
- `-pie`：生成 position-independent 位置无关可执行文件（`ET_DYN`）。源文件需要使用 `-fpie/-fPIE, -fpic/-fPIC`
- `-shared`：生成 position-independent 位置无关共享对象（`ET_DYN`）。限制最严格的模式：源文件需要使用 `-fpic/-fPIC`.
- `-r`：生成可重定位文件。这称为可重定位链接，比较特殊。它抑制了链接器合成的各种段并保留了重定位。请参阅 [可重定位链接](https://maskray.me/blog/2022-11-21-relocatable-linking).

令人困惑的是，编译器驱动提供了几个同名的选项：`-no-pie, -pie, -shared, -r`. GCC 6 引入了 configure-time 配置时选项 `--enable-default-pie`：此类构建默认启用 `-fPIE` 和 `-pie`。现在，许多 Linux 发行版已将此选项作为基本的安全强化措施启用。

### 可执行文件链接（`-no-pie` 和 `-pie`)

已定义符号是 non-preemptible. 不可抢占的。对于使用 PLT-generating 生成 PLT 的重定位的分支指令，分支可以直接绑定到该定义，从而避免 PLT。对于涉及 GOT-generating 生成 GOT 的重定位的代码序列，该代码序列可以被优化为使用直接访问。有关详细信息，请参阅 [关于全局偏移表的一切](https://maskray.me/blog/2021-08-29-all-about-global-offset-table)。

非局部的 non-local `STV_DEFAULT/STV_PROTECTED` 定义符号默认不会导出到动态符号表。

#### `-no-pie`

`-no-pie` 表示链接时地址等于运行时地址。链接器可以利用这一性质，解析所有引用不可抢占符号的重定位，包括生成 GOT 的绝对重定位（例如 `R_AARCH64_LD64_GOT_LO12_NC`）、生成 GOT 的 PC 相对重定位（例如 `R_X86_64_REX_GOTPCRELX`）等。即使没有 GOT 优化，不可抢占符号的 GOT 表项也是常量，因此无需动态重定位。映像基址默认是由架构决定的非零值。

- 某些架构有不同的 PLT 代码序列（i386、ppc32 .glink）。
- `R_X86_64_GOTPCRELX` 和 `R_X86_64_REX_GOTPCRELX` 可以进一步优化
- ppc64 `.branch_lt`（长分支地址）可以优化

#### `-pie`

`-pie` 与 `-shared -Bsymbolic` 非常相似，但它生成的是可执行文件。以下行为接近 `-no-pie`，但与 `-shared`:

- 允许拷贝重定位和规范 PLT。
- 允许将通用动态/局部动态 TLS 模型和 TLS 描述符放宽为初始执行/局部执行。
-  不会生成动态重定位。ld.lld 是否生成动态重定位的规则非常复杂，且依赖于架构。GNUgnu ld 是否生成动态重定位有非常复杂的规则，且依赖于架构。

 定义默认是可抢占的（可插桩），即该定义可能会在运行时被可执行文件或其他共享对象中的定义替换。编译器和链接器通过使用 non-local `STV_DEFAULT` 和 GOT 条目来引用此类符号。PLTplt 条目来引用此类符号。

 符号会导出到动态符号表。non-local `STV_DEFAULT/STV_PROTECTED`E.g 例如，在以下程序中，`foo` 在使用 `-shared` 链接时会导出到动态符号表，但使用 `-no-pie` 或 `-pie`. 1  
void foo() {}

 符号重定位（绝对重定位且宽度与字长匹配）会转换为相对重定位。non-preemptible non-TLS 有关详细信息，请参阅

 请参阅[相对重定位与 RELR](https://maskray.me/blog/2021-10-31-relative-relocations-and-relr) 了解详情。

### `-Bsymbolic`

 系列选项使共享对象中的 `-Bsymbolic` 定义变为 non-local `STV_DEFAULT`。它们对于可执行文件输出是 non-preemptible.。关于“可抢占”的说明，请参见上方的“模式”部分。no-op 此外，需要注意：

- `-Bsymbolic` 使所有定义（除非匹配 `--dynamic-list/--export-dynamic-symbol-list/--export-dynamic-symbol` non-preemptible
- `-Bsymbolic-functions` 类似 `-Bsymbolic`，但仅适用于 `STT_FUNC` 定义
- `-Bsymbolic-non-weak-functions` 类似 `-Bsymbolic`，但仅适用于非 `STB_WEAK``STT_FUNC` 定义

请参阅[ELF 插桩与 -Bsymbolic](https://maskray.me/blog/2021-05-09-elf-interposition-and-bsymbolic) 了解详情。

### `--defsym`

定义一个符号。

类似 ld64 的 `-alias`.

### `--exclude-libs`

 如果匹配的归档文件（无论是常规归档，还是被 `--whole-archive`/`--no-whole-archive` 包围的归档）定义了 non-local 符号，则不导出该符号。

例如，`clang++ -static-libstdc++ -Wl,--export-dynamic,--exclude-libs=libstdc++.a a.cc` 不会导出 libstdc++ 定义的符号。

### `--export-dynamic`

 该选项将 non-local `STV_DEFAULT/STV_PROTECTED` 定义符号放入可执行文件输出的动态符号表中。该选项在以下情况下是 no-op

- `-shared` 指定时，因为共享对象默认这样做。
- `-no-pie` 指定时且没有任何输入的共享对象，因为动态符号表不存在。

以下是符号被导出到动态符号表的规则（逻辑 AND）：

- non-local `STV_DEFAULT/STV_PROTECTED`（这意味着它可以被 `--exclude-libs`)
- 以及以下条件的逻辑或：

    - undefined symbol
    - (`--export-dynamic` || `-shared`) && `! (unnamed_addr linkonce_odr GlobalValue || local_unnamed_addr linkonce_odr (constant GlobalVariable || Function))`（在 LTO 中，某些 `linkonce_odr` 符号可以隐藏）
    - matched by `--dynamic-list/--export-dynamic-symbol-list/--export-dynamic-symbol`
    - 由共享对象以 `STV_DEFAULT` 形式定义或引用
    - 指定 `--ignore-{data,function}-address-equality}` 时，共享对象中的 `STV_PROTECTED` 定义被复制重定位或规范 PLT 抢占
    - `-z ifunc-noplt` && has at least one relocation

如果可执行文件定义了一个符号，而该符号被 link-time 共享对象引用，则链接器会导出该符号，以便共享对象中未定义的符号在运行时可以绑定到可执行文件中的定义。如果可执行文件定义了一个符号，而该符号同样被 link-time 共享对象定义，则链接器会导出该符号，以在运行时实现符号插桩。

在 LLVM 中，某些未命名的_地址 `GlobalValue` 不受可执行文件链接时的 `--export-dynamic` 影响。请参阅 `lld/test/ELF/lto/internalize-exportdyn.ll` 和 `lld/test/ELF/lto/unnamed-addr-comdat.ll`.

### `--export-dynamic-symbol=glob`, `--export-dynamic-symbol-list`, 以及 `--dynamic-list`

这些选项对于可执行文件和共享对象具有不同的语义。

- 可执行文件：将匹配的 non-local 已定义符号放入动态符号表（`--export-dynamic` 适用于所有 non-local 已定义符号。）
- 共享对象：对匹配的 non-local `STV_DEFAULT` 符号的引用不应绑定到共享对象内的定义，即使它们由于 `-Bsymbolic`, `-Bsymbolic-functions` 或 `--dynamic-list`

`--dynamic-list` 此外还隐含 `-Bsymbolic`.

对于共享对象的情况，我通常称此操作为“使符号可抢占”。

可以使用 `--export-dynamic-symbol=foo*` 来匹配所有 non-local `STV_DEFAULT` 符号 `foo*`. ld.lld。ld.lld 11 之前使用精确匹配而非通配符。

`--export-dynamic-symbol-list` 自 [GNU ld 2.35](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=37a141bfed4dd3c33d77c15dfde00e4b4f5b24c7) 和 [ld.lld 14](https://reviews.llvm.org/D107317).

在以下示例中，我们将看到 `GLOB_DAT` 动态重定位，当且仅当 `var` 是可抢占的。1  
2  
3  
// a.c  
int var;  
int inc() { return ++var; }

```plaintext
# Preemptible by default in a shared object.
% clang -O2 -fpic -shared a.cc && readelf -Wr a.out | grep var
0000000000003fc8  0000000500000006 R_X86_64_GLOB_DAT      000000000000400c var + 0

# -Bsymbolic makes a definition non-preemptible.
% clang -O2 -fpic -shared -Bsymbolic a.cc && readelf -Wr a.out | grep var

# --export-dynamic-symbol makes a definition preemptible despite -Bsymbolic
% clang -O2 -fpic -shared -Wl,-Bsymbolic,--export-dynamic-symbol=var a.cc && readelf -Wr a.out | grep var
0000000000003fc8  0000000500000006 R_X86_64_GLOB_DAT      000000000000400c var + 0

# Without a symbolic intention option, --export-dynamic-symbol is a no-op for -shared.
% clang -O2 -fpic -shared -Wl,--export-dynamic-symbol=foo a.cc && readelf -Wr a.out | grep var
0000000000003fc8  0000000500000006 R_X86_64_GLOB_DAT      000000000000400c var + 0

# --dynamic-list implies -Bsymbolic.
% clang -O2 -fpic -shared -Wl,--dynamic-list=<(printf '{a;};') a.cc && readelf -Wr a.out | grep var

# A matched symbol is still preemptible.
% clang -O2 -fpic -shared -Wl,--dynamic-list=<(printf '{var;};') a.cc && readelf -Wr a.out | grep var
0000000000003fc8  0000000500000006 R_X86_64_GLOB_DAT      000000000000400c var + 0
```

如果版本脚本中 `local:` 匹配的符号也被动态列表指定，则版本脚本优先，该符号将被设为局部符号。

### `--discard-none`, `--discard-locals` 和 `--discard-all`

如果生成了 `.symtab`，则当满足以下条件时，保留在活跃段中定义的局部符号：

```cpp
if ((--emit-relocs or -r) && referenced) || --discard-none
  return true
if --discard-all
  return false
if --discard-locals
  return is not .L
# No --discard-* is specified.
return not (.L in a SHF_MERGE section)
```

这些 `.L` 符号（MC 中的临时标签）可以在 `clang -Wa,-L` 构建中生成。然后，如果未指定 `ld --discard-locals`，链接器会将这些符号写入可执行文件。

此外，RISC-V 链接器松弛可能会生成 `.L0`（末尾带空格）符号（[llvm-project#89693](https://github.com/llvm/llvm-project/pull/89693)）。对于 RISC-V，较新的 GCC 和 Clang 会向链接器传递 `-X` (`--discard-locals`）。

### `--no-undefined-version`

如果版本脚本指定了精确模式但未匹配到任何已定义符号，则报告错误。

假设我们有以下版本脚本，如果 `foo` 不是一个已定义符号，链接器将报告错误。对于未匹配到任何符号的通配符模式（e.g. `bar*`），则不会报错。这是一种折衷。1  
2  
3  
4  
v1 {  
 foo;  
 bar*;  *;  
};

GNU ld 自 `--no-undefined-version` 起就支持 [2002-08](https://sourceware.org/git/?p=binutils-gdb.git;a=commit;h=3194163592008a9e575d577921647ab91b09c77b)，但 `--undefined-version` 是 2022 年 10 月（里程碑：binutils 2.40）才新增的。

### `--strip-all`

不要创建 `.strtab` 或 `.symtab`.

### `-u symbol`

如果归档文件定义了 `-u` 指定的符号，则拉取相关的成员（从归档文件转换为目标文件，然后该文件将像普通的 .o 一样处理）。

例如：`ld -u foo ... a.a`。如果 `a.a` 没有定义先前目标文件引用的符号，则不会拉取 `a.a`。如果指定了 `-u foo`，那么将拉取 `foo` 中定义了 `a.a` 的归档成员。

的另一个用途是指定 GC 根。`-u` 的另一个用途是指定 GC 根。

### `--version-script=script`

版本脚本有三个用途：

- 定义版本
- 指定一些模式，使匹配到的已定义且未版本化的符号具有指定的版本
- local 版本：`local:` 可以将匹配的已定义符号设为 `STB_LOCAL`

未版本化符号的绑定为 `STB_LOCAL`，并且不会导出到动态符号表

如果版本脚本中 `local:` 匹配的符号也被动态列表指定，则版本脚本优先，该符号将被设为局部符号。

[关于符号版本控制的所有内容](https://maskray.me/blog/2020-11-26-all-about-symbol-versioning) 详细描述了符号版本控制。

### `-y symbol`

通常用于调试。输出指定符号被引用和定义的位置。

### `-z muldefs`

别名：`--allow-multiple-definition`

允许在一个符号在多个文件中被定义。默认情况下，链接器不允许两个同名的 non-local 常规定义（non-weak, non-common）存在。

### `-z unique-symbol`

重命名局部符号以确保没有重复。

一些 Intel 员工正在致力于实现函数粒度的内核地址空间布局随机化，并希望有这样的特性（[https://sourceware.org/bugzilla/show_bug.cgi?id=26391](https://sourceware.org/bugzilla/show_bug.cgi?id=26391)). GNU 自 2.36 版起，GNU ld 就已支持该选项。我关闭了 ld.lld [特性请求](https://bugs.llvm.org/show_bug.cgi?id=50745).

我认为这不是一个好的设计。

首先是稳定性问题。假设旧内核中有 `foo.1 foo.2`。如果有新的局部 `foo` 符号，新内核将会有 `foo.1 foo.2 foo.3`。然而，新符号并不一定对应旧内核中同名局部符号。这种干扰在使用 LTO 或 PGO 时可能更常见。对于 ClangLTO，内核 Makefile 当前指定了 `-mllvm -import-instr-limit=5`。如果某个接近边界的函数恰好跨越了该边界，并且在被内联到其他编译单元时，稳定性问题可能会影响到许多编译单元。

该实现必须对所有局部符号执行一次迭代，这可能会影响链接速度。

此外，`.[0-9]+` 方案已被 C++ 名称修饰所使用。Itanium C++ABI 指出：“包含句点的 vendor-specific 表示由第一个句点之前的命名的实体的一个特定于供应商的版本或部分。对句点后的后缀中可能出现的字符没有限制。”在 GNU 中，这用于表示函数克隆。

```text
% c++filt <<< $'_ZL3foov\n_ZL3foov.1'
foo()
foo() [clone .1]
```

作为替代方案，我建议 FGASLR 开发者使用 `STT_FILE` 符号：1
2  
3  
4  
STT_FILE a.c  
STT_NOTYPE foo
STT_FILE b.c  
STT_NOTYPE foo

ELF 规范指出：

> 按惯例，符号名称给出与目标文件关联的源文件名。文件符号具有 STB_LOCAL 绑定，其节索引为 SHN_ABS，并且如果存在，它位于该文件的其他 STB_LOCAL 符号之前。

我在对 `[PATCH v9 02/15] livepatch: use `-z unique-symbol` if available to nuke pos-based search`](https://lore.kernel.org/all/20211223002209.1092165-3-alexandr.lobakin@intel.com/).

### `--as-needed` 和 `--no-as-needed`

通常每个 link-time 共享对象都有一个 `DT_NEEDED` 标签。这样的共享对象将由动态加载器加载。

`--as-needed` 可以避免不必要的 `DT_NEEDED` 标签。`--as-needed` 和 `--no-as-needed` 是 position-dependent 选项（非正式称呼，但没有更合适的形容词）。在 ld.lld 中，一个共享对象被视为必需的，如果满足以下任一条件：

- 它至少在 `--no-as-needed` 模式下被链接一次（i.e. `--as-needed a.so --no-as-needed a.so` =\> → 必需）
- 或者它提供了一个定义，解析了来自活跃节的 non-weak 引用（未被 `--gc-sections`)

在 gold 中，规则可能是：

- 它至少在 `--no-as-needed` 模式下被链接一次（i.e. `--as-needed a.so --no-as-needed a.so` =\> → 必需）
- 或者它提供了一个定义，解析了 non-weak 引用

在 GNUld 中，规则相当复杂。基本规则如下所示：

- 它至少在 `--no-as-needed` 模式下被链接一次（i.e. `--as-needed a.so --no-as-needed a.so` =\> → 必需）
- 或者它提供了一个定义，解析了来自前一个输入文件的 non-weak 引用（其工作方式类似于归档选择）

在 `ld.bfd ... a.so --as-needed b.so --no-as-needed`, [如果 `a.so` 引用了由 `b.so` 定义的一个符号，但 `a.so` 本身不需要 `b.so`，最终输出将需要 `b.so`](https://discourse.llvm.org/t/as-needed-breaks-our-build-with-undefined-symbols/75505/6)。这可能被用作一种解决低链接问题的工作区。当共享对象缺失的依赖项（`b.so`）被看到时，输出会添加 `DT_NEEDED` 条目以满足 `b.so` 的需求，即使自身并不需要该依赖项。

### `-Bdynamic` 和 `-Bstatic`

这两个选项是 position-dependent 选项，会影响稍后在命令行上出现的 `-lname`。

- `-Bdynamic`（默认）：在由 `libfoo.so` 指定的目录列表中搜索 `libfoo.a` 和 `-l`
- `-Bstatic`：在由 `libfoo.a` 指定的目录列表中搜索 `-l`

历史上，`-Bstatic` 和 `-static` 在 GNU ld 中同义。编译器驱动选项 `-static` 是一个不同的选项。除了向 ld 传递 `-static` 外，它还会移除默认的 `--dynamic-linker`，这会影响 libgcc、libc 等的链接。

### `--no-dependent-libraries`

这是 ld.lld 特有的选项，用于忽略目标文件中类型为 `SHT_LLVM_DEPENDENT_LIBRARIES` 的节（依惯例命名为 `.deplibs`）。

此部分包含一个文件名列表。这些文件名将由 ld.lld 作为额外的输入文件添加。

### `-soname=name`

在生成的共享对象的动态表中设置 `DT_SONAME` 动态标签。

链接器会在链接时记录共享对象，并在生成的可执行文件/共享对象的动态表中使用 `DT_NEEDED` 记录来描述每个链接时的共享对象。

- 如果共享对象包含 `DT_SONAME`，其值就是 `DT_NEEDED` 的值
- 否则，如果通过 `-l` 链接，其值为文件基本名称
- 再否则，其值为路径名（绝对路径与相对路径的处理存在差异）

例如，执行 `ld -shared -soname=a.so.1 a.o -o a.so; ld b.o ./a.so` 后，`a.out` 的 `DT_NEEDED` 标签为 `a.so.1`。如果第一条命令不含 `-soname`，`a.out` 的 `DT_NEEDED` 标签则为 `./a.so`。

### `--start-group` 和 `--end-group`

如果 `a.a` 和 `b.a` 之间存在相互引用，并且你不确定哪个会先被拉入链接，则必须使用这对选项。示例如下：

对于存档链接顺序：`main.o a.a b.a`，假设 `main.o` 引用了 `b.a`，而 `a.a` 不满足之前的某个未定义符号，那么该链接顺序会导致错误。能否将链接顺序替换为 `main.o b.a a.a`？如果 `main.o` 在更改后引用了 `a.a`，并且 `b.a` 不满足之前的某个未定义符号，那么该链接顺序也会导致错误。

一种解决方案是 `main.o a.a b.a a.a`。在很多情况下，重复 `a.a` 一次就足够了，但如果链接第一个 `a.a(a.o)` 时只加载了 a.a，链接 `b.a(b.o)` 时只加载了 b.a，而链接第二个 `a.a(c.o)` 时只加载了 `a.a(c.o)`，并且 `b.a` 需要  

 的另一个成员，这个链接顺序仍然会导致未定义符号错误。`b.a`，即 `main.o a.a b.a a.a b.a`，但更好的解决方案是 `main.o --start-group a.a b.a --end-group`，或 `main.o -( a.a b.a -)`.

### `--start-lib` 和 `--end-lib`

参见 [Archives and --start-lib](https://maskray.me/blog/2022-01-16-archives-and-start-lib)。如果 `a.a` 包含 `b.o c.o`, `ld ... --start-lib b.o c.o --end-lib` 的功能类似于 `ld ... a.a`.

### `--sysroot`

这与 `--sysroot` 驱动选项不同。在 GCC/Clang 中，驱动选项 `--sysroot` 做两件事：

- 决定 include/library 搜索路径（e.g. `$sysroot/usr/include`, `$sysroot/lib64`)
- 传递给 ld。`--sysroot` 传递给 ld。

在 ld 中，

- `-l =foo` 和 `-l=foo` 在 sysroot 目录下查找 `libfoo.so` 或 `libfoo.a`。
- `foo` 在 `INPUT` 或 `GROUP` 中在 sysroot 目录下查找 `foo`。
- 如果链接脚本在 sysroot 目录中，当它打开一个绝对路径文件（`INPUT` 或 `GROUP`）时，在绝对路径前添加 sysroot。

### `-t` `--trace`

输出可重定位的目标文件、共享对象以及提取的存档成员。

### `--whole-archive` 和 `--no-whole-archive`

.a 位于 `--whole-archive` 选项之后将被视为不带延迟语义的 .o。如果 `a.a` 包含 `b.o c.o`，那么 `ld --whole-archive a.a --no-whole-archive` 的效果等同于 `ld b.o c.o`.

### `--push-state` 和 `--pop-state`

GNU ld 在 binutils 2.25 中实现了这些选项。

`-Bstatic, --whole-archive, --as-needed` 等都是 position-dependent 选项，代表布尔状态。`--push-state` 可以保存这些选项的布尔状态，`--pop-state` 则会恢复它。

在链接命令行中插入一个新选项来改变状态时，你通常想要恢复它。这时，你可以使用 `--push-state` 和 `--pop-state`。例如，为了确保链接 `libc++.a` 和 `libc++abi.a`，你可以使用 `-wl,--push-state,-Bstatic -lc++ -lc++abi -wl,--pop-state`.

参见[依赖相关的链接器选项](https://maskray.me/blog/2021-06-13-dependency-related-linker-options)了解详情。

### `-z defs` 和 `-z undefs`

是否报告常规对象中未解析的未定义符号的错误。“未解析”表示该符号未由常规对象文件或 link-time 共享对象定义。可执行文件链接默认为 `-z defs/--no-undefined`（不允许）且 `-shared` 链接默认为 `-z undefs`（允许）。

许多构建系统启用 `-z defs`，要求共享对象在链接时指定所有依赖项（链接你使用的）。

### `--allow-shlib-undefined` 和 `--no-allow-shlib-undefined`

是否报告共享对象中未解析的 `STB_GLOBAL` 未定义符号的错误。可执行文件链接默认为 `--no-allow-shlib-undefined`（报告错误）且 `-shared` 链接默认为 `--allow-shlib-undefined`（不报告错误）。

对于以下代码，链接可执行文件时会报告错误： 1  
2  
3  
4  
5  
6  
7  
// a.so  
void f();  
void g() {f();}  
  
// exe  
void g()  
int main() {g();}

如果你在链接可执行文件时指定 `--allow-shlib-undefined`，链接会成功，但 ld.so 会在运行时报告错误。在 glibc 中，错误是 `symbol lookup error: ... undefined symbol:`.

GNU ld 有一个复杂的算法来查找传递闭包。只有当传递闭包的共享对象无法解析未定义符号时，才会报告错误。gold 和 lld 使用简化的规则：如果共享对象的所有 `DT_NEEDED` 依赖项都直接链接，则启用错误；如果某些依赖项未链接，那么 gold/lld 无法准确确定间接共享对象是否能提供定义，因此它们会保守处理，不报告错误。

 和 `-z defs/-z undefs/--no-undefined` 可以通过选项 `--[no-]allow-shlib-undefined` 来控制。`--unresolved-symbols`.

### `--warn-backrefs`

参见[依赖相关的链接器选项#--warn-backrefs](https://maskray.me/blog/2021-06-13-dependency-related-linker-options#warn-backrefs).

### `--no-rosegment`

默认情况下，ld.lld 将 read-only 数据段（e.g. `.rodata`）和代码段（e.g. `.text`）放入两个 `PT_LOAD` 段中。

- R `PT_LOAD`
- RX `PT_LOAD`
- RW `PT_LOAD`（与 `PT_GNU_RELRO`)
- RW `PT_LOAD`

指定此选项以合并 R`PT_LOAD` 和 RX`PT_LOAD`。RX`PT_LOAD` 段传统上称为文本段，是第一个段。

ld.lld 将 rodata 和 data 放在 text 两侧。这种布局的优点是 text 与 data 之间的距离更短，可以降低重定位溢出的压力。

gold 是第一个实现 `--rosegment`.

### `--xosegment`

此选项支持[execute-only 内存](https://isopenbsdsecu.re/mitigations/execute_only/).

- AArch32 使用 `SHF_ARM_PURECODE` 段标志来标记仅包含纯程序指令且不含数据的段。
- AArch64 使用 `SHF_AARCH64_PURECODE` 段标志。

默认情况下，LLD 将具有 `SHF_ALLOC|SHF_EXECINSTR|SHF_AARCH64_PURECODE` 标志的段视为与具有 `SHF_ALLOC|SHF_EXECINSTR` 标志的段兼容，将它们合并到一个 `PT_LOAD segment` 段中。当指定 `--xosegment` 时，LLD 将这些段分离到不同的 `PT_LOAD` 段中：一个用于具有 `SHF_ALLOC|SHF_EXECINSTR|SHF_AARCH64_PURECODE` 标志的段，另一个用于具有 `SHF_ALLOC|SHF_EXECINSTR`.

### `-z noseparate-code`

这是 GNU ld 的经典布局，允许某些文件内容被映射为多个 `PT_LOAD` 段，其中一段为可执行段，另一段为 non-executable.。在此布局中，两个相邻的 `PT_LOAD` 程序头在文件偏移上可以重叠。这种技巧避免了下一个程序头开始前的填充。

在没有链接脚本片段的情况下，通常只有两个 `PT_LOAD` 段：

- RX `PT_LOAD`：包含只读节（read-only）和可执行节（`SHF_ALLOC`）。`SHF_ALLOC|SHF_EXECINSTR`).
- RW `PT_LOAD`

    - 前半部分为 `PT_GNU_RELRO`，rtld 处理完动态重定位后会通过 mprotect 将其设为只读。
    - 非 `PT_GNU_RELRO` 部分，在运行时始终可写。

第一个 `PT_LOAD` 通常称为文本段。这个术语不太准确，因为该段也包含只读数据。read-only

自 ld.lld 10 起，这种布局因其尺寸优势而被默认使用。

注意：当一个 `SHT_NOBITS` 节后面跟着另一个节时，该 `SHT_NOBITS` 节的行为就像它占据文件偏移范围一样。这是因为 ld.lld 没有实现文件大小优化。几乎所有的链接映像都不会使用此优化，因为很少会在 `SHF_ALLOC` 节之后添加 `SHT_NOBITS SHF_ALLOC` 节。

### `-z separate-code`

该选项在 binutils 2.31 中引入，并在 Linux/x86 上默认启用。GNU ld 具有如下布局：

- R `PT_LOAD`
- RX `PT_LOAD`
- R `PT_LOAD`
- RW `PT_LOAD`

    - `PT_GNU_RELRO` part
    - Non-`PT_GNU_RELRO` part

在这种布局中，相邻的 `PT_LOAD` 程序头不能在文件偏移上重叠。也就是说，文件中映射到可执行节（RX `PT_LOAD`）的字节不会同时映射到 R `PT_LOAD`。其思路是，只读内存不可执行，其中的 ROP gadget 也就无法使用。不过这更像是安全表演，因为可执行内存本来就含有大量 ROP gadget。

受实现复杂度影响，最终采用的布局并不理想：`RX` `PT_LOAD` 之后还有一个只读 `PT_LOAD`。更好的布局是把这个 R 段与第一个 R 段合并（[PR23704](https://sourceware.org/bugzilla/show_bug.cgi?id=23704)）。另一个问题是，当不存在 RW `PT_LOAD` 时，开头几个非 `non-`SHF_ALLOC 节的内容可能会映射到 RX 内存。

我在 ld.lld 10 中引入了此选项。其语义类似于 GNU ld，但布局不同：两个 RW `PT_LOAD` 允许重叠，这意味着第二个 `PT_LOAD` 的地址无需对齐，最多可浪费 max-page-size*2 个字节。

GNU ld 的 `-z separate-code` 在 lld 中实际上拆成了两个选项：`-z separate-code` 和 `--rosegment`。

### `-z separate-loadable-segments`

这是 ld.lld 的传统布局：所有 `PT_LOAD` 段均不重叠（同一字节不会同时载入两个内存映射）。我在 [2019 年](https://reviews.llvm.org/D67481)加入了该选项。

其实现方式是把每个新 `PT_LOAD` 的地址按 max-page-size 对齐。lld 预设 4 个 `PT_LOAD`（r、rx、rw(relro)、rw(non-relro)），输出文件中的三次对齐会浪费一些空间。在 aarch64 和 powerpc 上，ABI 指定的 max-page-size 较大（65536），最多可能浪费 65536*3 字节。

### `-z relro`

将 RELRO 节放置在 `PT_GNU_RELRO` 程序头中。

GNU ld 使用一个开头带填充的 RW `PT_LOAD` 程序头。该 `PT_LOAD` 的前半部分与 `PT_GNU_RELRO` 重叠；加入填充是为了让 `PT_GNU_RELRO` 的末尾按 [max-page-size](https://sourceware.org/bugzilla/show_bug.cgi?id=28824) 对齐（参见 `ld.bfd --verbose` 输出）。GNU ld 2.39 之前使用 common-page-size 对齐。单个 RW `PT_LOAD` 的布局会使对齐直接增大文件，而 max-page-size 在许多系统上可达 65536，因而造成[空间浪费](https://sourceware.org/bugzilla/show_bug.cgi?id=30612)。

lld 利用两个 RW 的 `PT_LOAD` 程序头：一个用于 RELRO 段，另一个用于 non-RELRO 段。虽然这最初看起来可能不寻常，但它消除了 GNU ld 布局中所需的对齐填充。关键变化：

- [https://reviews.llvm.org/D58892](https://reviews.llvm.org/D58892) 从 `PT_LOAD(PT_GNU_RELRO(.data.rel.ro .bss.rel.ro) .data .bss)` 切换为 `PT_LOAD(PT_GNU_RELRO(.data.rel.ro .bss.rel.ro)) PT_LOAD(.data. .bss)`.
-  段和关联的 RW 的结尾 `PT_GNU_RELRO` 段 `PT_LOAD` 被[填充到 common-page-size 边界](https://github.com/llvm/llvm-project/pull/66042)。填充段 `.relro_padding` 类似于 mold。在 LLD 18 之前，存在一个问题，即运行时_页面_大小\< common-page-size 无效。

mold 使用的布局与 lld 的类似。在 mold 的情况下，`PT_GNU_RELRO` 的结尾通过追加一个 max-page-size 段填充到 `SHT_NOBITS` `.relro_padding`。这种方法确保 `PT_GNU_RELRO` 的最后一页受到保护，无论系统页大小如何。但是，当系统页大小小于 max-page-size 时，第一个 RW 的映射 `RW` `PT_LOAD` 会大于所需。

在我看来，当运行时页大小大于 common-page-size 时，失去对最后一页的保护并不是真正的问题。为保护而双重映射最多为 max-common-page 的页面可能会导致不必要的 VM 浪费。保护 `.got.plt` 是 `-z now` 的主要目的。保护 `.data.rel.ro` 的一小部分并不会真正使程序更安全，因为 `.data` 和 `.bss` 是如此巨大且充满攻击目标。如果用户真的担心，他们可以将 common-page-size 设置为其系统页大小。

GNU ld 的内部链接器脚本将 RELRO 段放置在 RELRO 和 `DATA_SEGMENT_ALIGN`（内置 `DATA_SEGMENT_RELRO_END` (built-in 函数）之间。`DATA_SEGMENT_ALIGN` 是添加填充的位置，以便 `DATA_SEGMENT_RELRO_END` 对齐到 max-page-size 边界。1  
2  
3  
. = DATA_SEGMENT_ALIGN(CONSTANT(MAXPAGESIZE), CONSTANT(COMMONPAGESIZE));  
. = DATA_SEGMENT_RELRO_END(0, .);  
. = DATA_SEGMENT_END(.);

ld.lld 模拟了这些内置函数：

- `DATA_SEGMENT_ALIGN`：将当前位置设置为 `alignTo(script->getDot(), + align)`
- `DATA_RELRO_END`：将当前位置设置为 `alignTo(script->getDot(), MAXPAGESIZE)`。`.relro_padding``alignTo(script->getDot(), MAXPAGESIZE)`. `.relro_padding` 紧接在 `DATA_RELRO_END`.

### `-z lrodata-after-bss`

参见 [Relocation overflow and code models#x86-64 链接器要求](https://maskray.me/blog/2023-05-14-relocation-overflow-and-code-models#x86-64-linker-requirement).

### `--execute-only`

这是 ld.lld 用于 AArch64 的特定选项。该选项要求 `--rosegment`，并使 RX 段 `RX` `PT_LOAD` 变为可执行独占 (`PF_X`)。executable-only (`PF_X`).

### `--apply-dynamic-relocs`

一些 psABI 使用 RELA 格式（AArch64、PowerPC、RISC-V, x86-64 等）：重定位包含 addend 字段。在这些目标上，`--apply-dynamic-relocs` 要求链接器将被重定位位置的初始值设置为 addend 而不是 0。如果可执行文件/共享对象使用压缩，`--no-apply-dynamic-relocs` 可以改善压缩效果。

`--apply-dynamic-relocs` 在所有端口中均受 ld.lld 支持。截至 2023 年 8 月，[仅 aarch64 端口](https://sourceware.org/PR25891) 的 GNU ld 支持 `--apply-dynamic-relocs`.

### `--emit-relocs`

此选项使 `-no-pie/-pie/-shared` 链接保留输入重定位，方式类似于 `-r`。可用于链接后的二进制分析。我所知的唯一两种用途是 `config_relocatable` 和 Linux 内核 x86 的 bolt。

输出段的顺序可能不同于 `--emit-relocs`. `.rela.eh_frame` 的情况。`,` 段[https://reviews.llvm.org/D44679](https://reviews.llvm.org/D44679) 被保留。参见 `.rela.eh_frame` 输入段 `.eh_frame` 被放置在只读 read-only 输出段之前。

GNU ld 的 powerpc 使用[转换后的重定位类型](https://maskray.me/blog/2023-02-26-linker-notes-on-power-isa#emit-relocs).

### `--pack-dyn-relocs=value`

`relr` 可以启用 `DT_RELR`，这是一种更紧凑的相对重定位（`R_*_RELATIVE`）编码格式。相对重定位在位置无关的可执行文件中很常见。

### `-z rel` 和 `-z rela`

每种架构都有其主流的重定位格式。ld.lld 实现了 `-z rel` 来在即使主流格式为 REL 的架构上也使用 RELA 进行动态重定位。该选项可以节省一些空间。

- COPY, GLOB_DAT 和 J[U]MP_SLOT 的加数始终为 0。运行时链接器（rtld）的实现无需读取隐式加数。REL 严格更优。
- 一个 RELATIVE 具有一个 non-zero 的加数。它也可以使用隐式加数。另外，此类重定位可以通过 RELR 重定位条目格式进行紧凑打包。
- 对于其他动态重定位类型（e.g. 符号重定位 R_X86_64_64），ld.so 的实现需要读取隐式加数。REL 可能有轻微的性能影响，因为隐式加数会强制进行随机访问读取，而无法在遍历重定位数组时一次性发出大量写入操作。

### `-z report-relative-reloc`

转储有关 `R_*_RELATIVE` 和 `R_*_IRELATIVE` 重定位的信息。

### `-z text` 和 `-z notext`

`-z text` 不允许文本重定位。`-z notext` 允许文本重定位。

从 binutils 2.35 开始，GNU ld 在 linux/x86 上默认启用了 configure-time 选项 `--enable-textrel-warning=warning`，如果存在文本重定位，则会发出警告。

“文本重定位”这一概念的措辞并不精确。其实际含义是作用于没有 `SHF_WRITE` 标志的 section 的动态重定位的总称。如果 .o 文件中重定位的值在链接时无法确定，则需要将其转换为动态重定位，并由 ld.so 在运行时计算（类型与 .o 中的相同）。如果目标 section 没有 `SHF_WRITE` 标志，ld.so 将不得不临时执行 `mprotect` 来更改内存映射的权限、进行修改，然后恢复之前的 read-only 权限，这会妨碍页面共享。

共享对象比可执行文件更容易产生文本重定位。可执行文件具有规范的 PLT 和复制重定位，以避免某些文本重定位。

不同的链接器在不同的架构上允许不同的文本重定位类型。GNU ld 可能允许 glibc ld.so 支持的相当多的重定位类型。x86-64 上，链接器将允许 `R_X86_64_64` 和 `R_X86_64_PC64`。然而，大多数加载器不支持 `R_X86_64_PC64`.

 在以下汇编代码中，`defined_in_so` 是在共享对象中定义的符号。每种文本重定位的场景在注释中给出。

```plaintext
.globl global
global:
local:
  .quad local              # (-pie or -shared) R_X86_64_RELATIVE
  .quad global             # (-pie) R_X86_64_RELATIVE or (-shared) R_X86_64_64
  .quad defined_in_so      # (-shared) R_X86_64_64
  .quad defined_in_so - .  # (-shared) R_X86_64_PC64
```

在 `-no-pie` 或 `-pie` 模式下，链接器会根据 `defined_in_so`:

- `STT_FUNC`：生成规范的 PLT
- `STT_OBJECT`：生成复制重定位
- `STT_NOTYPE`：GNU ld 会生成复制重定位。lld 会生成文本重定位

### `--gc-sections`

在编译时指定 `-ffunction-sections` 或 `-fdata-sections` 以使其生效。链接器会进行活跃度分析，从输出中移除未使用的 section。

参见 [链接器垃圾收集](https://maskray.me/blog/2021-02-28-linker-garbage-collection) 了解详情。

### `-z start-stop-gc` 和 `-z nostart-stop-gc`

`-z start-stop-gc` 表示来自活跃 section 的 `__start_foo` 或 `__stop_foo` 引用不会保留所有 `foo` 输入 section。

`-z nostart-stop-gc` 表示来自活跃 section 的 `__start_foo` 或 `__stop_foo` 引用会保留所有 `foo` 输入 section。

参见 [Metadata sections、COMDAT 和 SHF_LINK_ORDER](https://maskray.me/blog/2021-01-31-metadata-sections-comdat-and-shf-link-order) 了解详情。

### `--icf=all` 和 `--icf=safe`

启用相同代码折叠。这个名称源于 MSVC 链接器的 `/OPT:ICF`，其中 "ICF" 代表 "Identical COMDAT Folding"。gold 将其命名为 "identical code folding"。

这个名称略有误导性：

- 该功能作用于 section 而非函数。
- 该功能也适用于只读数据。

我们将相同的 section 定义为其内容相同，并且它们的传出重定位集无法区分：它们需要具有相同数量的重定位，具有相同的相对位置，且引用的符号无法区分。这是一个递归定义：如果 `.text.a` 和 `.text.b` 在相同位置引用了不同的符号，但只要这些被引用的符号满足相同代码/只读数据的要求，它们仍然可以无法区分。

在一组相同的节中，链接器可能会保守地对其中一些节抑制折叠。`--keep-unique=<symbol>` 会使定义 `<symbol>` 的节成为唯一。在 ld.lld 中，只读节默认是可折叠的（gold 不会折叠只读数据）。但是，定义 `.dynsym` 符号的只读节则不可折叠。

对于其余节，在一组相同的节中，链接器会选取一个代表节并丢弃其余节，然后将引用重定向到该代表节。

gold 实现了基于重定位的 `--icf=safe`。

`ld.lld --icf=safe` 使用一个特殊的节 `.llvm_addrsig` (LLVM 地址重要性表，类型为 `SHT_LLVM_ADDRSIG`），该表由 Clang 的 `-faddrsig` 生成。截至 2023 年 1 月，`-faddrsig` 在大多数 Linux 目标上是默认启用的，但在 Android、Gentoo 和使用了 `-fintegrated-as` 的情况下会被禁用。如果该节缺失，ld.lld 会采取保守策略，假设表中定义了符号的每个节都是地址重要的。

`SHT_LLVM_ADDRSIG` 将符号索引编码为 ULEB128. `objcopy`, `ld -r`。`objcopy` 和 `ld -r` 等二进制操作工具可能会修改符号表。一个有趣的特性是，`sh_link=0` 和 `SHT_LLVM_ADDRSIG`. ld.lld 会将已知节类型 `sh_link!=0` 的 `sh_link==0`.

 设为 0。ld 的 lld 版本使用 `-faddrsig` 来检查其有效性，并在遇到 `-fno-addrsig` 时报告警告。`R_*_NONE`：某种重定位类型（在 ELF 中用于标记无操作的重定位）。REL：一种重定位格式，将重定位信息存储在节中。RELA：另一种重定位格式，在节中包含附加的加数。`-fno-addrsig`。那么这可能意味着我们应该默认禁用  

 并让用户选择启用此特性。Mach-O 的 [端口](https://discourse.llvm.org/t/problems-with-mach-o-address-significance-table-generation/63392) 选择了使用 relocation-based 基于重定位的表示形式来表示 `__DATA,__llvm_addrsig`.

`ld.lld --icf=all`。`.llvm_addrsig`.

 会忽略 `-shared`。
2  
int foo() { return 1; }  
int bar() { return 1; }

`foo` 和 `bar` 都位于 `.dynsym` 中。`ld.lld --icf=safe` 假定 `.dynsym` 中的符号具有地址意义，两个符号不能共享同一地址，因此 ld.lld 会保守地禁止合并 `.text.foo` 和 `.text.bar`。

`gold --icf=safe` 会合并 `.text.foo` 和 `.text.bar`。如果程序使用映射，并期望 `map[dlsym(h, "foo")]` 与 `map[dlsym(h, "bar")]` 解析到不同对象，这种做法就不安全。

在 LLVMCodeGen 中，带有 `{,local_}unnamed_addr` 属性的全局值不会进入 `.llvm_addrsig`。

`--icf=all` 放弃了 C++ 语言对指针相等性的保证。有人认为这可以接受，因为部分保证本来就会被破坏（例如使用 `-fvisibility-inlines-hidden` 时）。参见 [ELF 插位与 -Bsymbolic](https://maskray.me/blog/2021-05-09-elf-interposition-and-bsymbolic)。

在 [D141310](https://reviews.llvm.org/D141310) 中，有人提出可选的 Clang 诊断 `-Wcompare-function-pointers`，用于捕获一些会导致 `--icf=all` 失效的问题。

ICF 会增加调试难度，因为调试器可能无法区分被折叠的不同实例。

- 与被折叠函数关联的调试信息实际上会被重定向。
- 在一个函数上设置断点也会影响与它折叠在一起的函数。

ICF 还会改变栈回溯中的函数名，并使性能分析结果不准确。

 会改变堆栈跟踪中的函数名，并使性能分析不准确。`DW_AT_LLVM_stmt_sequence`，并使用调用者来区分折叠函数中的地址。

https://github.com/llvm/llvm-project/pull/139493#issuecomment-2896493771

当我们有

- 节 A1，包含一个指向符号 S1 的重定位，其中 S1 位于节 B1 的偏移量 K 处。
- 节 A2，包含一个指向符号 S2 的重定位，其中 S2 位于节 B2 的偏移量 K 处。

当重定位类型为 `R_AARCH64_ADR_GOT_PAGE`，并且节 B1 和 B2 被合并（保持符号 S1 和 S2 分离）时，节 A1 和 A2 目前可以被合并，这会导致正确性问题。

### `--symbol-ordering-file=<file>`

指定一个文本文件，每行包含一个已定义符号。在输入节描述（e.g. `*(.text .text.*)`）内，对匹配的输入节进行排序：如果符号 A 在排序文件中位于符号 B 之前，则将定义 A 的节放在定义 B 的节之前。

如果符号未定义或其所在的节被丢弃，链接器将输出一条警告，除非指定了 `--no-warn-symbol-ordering`。然而，默认的 `--no-warn-symbol-ordering` 似乎经常会妨碍工作。

`--symbol-ordering-file=` 主要用于两个目标：性能或压缩。

如果一个函数频繁调用另一个函数，并且这两个函数所在的输入节在链接后的镜像中彼此接近，那么它们落在同一页上的概率就会增加。通过考虑函数间的引用并将相关的函数放在一起，可以减少页面工作集，并降低 TLB 的抖动。参见 Karl Pettis 和 Robert C. Hansen 的 _配置文件引导的代码放置_。

移动应用通常优先考虑压缩后的代码体积。对于冷函数，压缩后的大小远比其性能更重要。为了改善压缩率，可以将相似函数分组放在一起，以提高压缩算法（如 Lempel-Ziv 系列）的效果。

此选项是 ld.lld 独有的。`--section-ordering-file` 具有按节名称排序的 `clang -fno-unique-section-names` ([GCC 特性请求](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=95095)可以创建名称相同的节，这会使 `--section-ordering-file`.

```sh
cat > a.s <<e
.section .rodata.0,"a",@progbits; .byte 0x0
.section .rodata.1,"a",@progbits; .byte 0x1
.section .rodata.2,"a",@progbits; .byte 0x2
.section .rodata.3,"a",@progbits; .byte 0x3
.section .rodata.4,"a",@progbits; .byte 0x4
e
cat > a.txt <<e
.rodata.3
.rodata.[2]
.rodata.1
e
as a.s -o a.o
gold --section-ordering-file=a.txt a.o -o a
```

```plaintext
% readelf -x .rodata a

Hex dump of section '.rodata':
  0x004000b0 00040302 01                         .....
```

GNU 引入了 `--section-ordering-file`，其语义有所不同。节排序脚本必须指定链接器脚本中已定义的输出节。指定的额外映射将被前置到输出节。  
2  
3  
4  
cat \> b.txt \<\<e  
.rodata : { *(.rodata.3) *(.rodata.[2]) *(.rodata.1) }  
e  
ld.bfd --section-ordering-file=b.txt a.o -o a

### `--call-graph-profile-sort`

当 `--call-graph-profile-sort`（默认启用）生效时，ld.lld 会检查输入可重定位目标文件中的 `SHT_LLVM_CALL_GRAPH_PROFILE` 节（调用图剖析）。一个 `SHT_LLVM_CALL_GRAPH_PROFILE` 节由（from_symbol, to_symbol, weight）元组组成。LLD 利用这些信息计算调用图，其中输入节是节点，（from_section, to_section, weight）是边，然后在输入节描述内部对节排序。排序算法基于《_面向大规模数据中心应用的函数布局优化_》。

LLD 按密度递减的顺序对输入节进行排序，其中密度的计算方式为权重除以大小。最初，每个输入节单独放置在一个簇中。处理每个输入节时，其簇会被追加到调用图中包含其最可能前驱节点的簇之后。如果满足以下任一条件，则合并会被阻止：

- 该边可能性很低（考虑到输入边的权重之和，该边的权重过小）。
- 两个簇的总大小超过一个阈值。
- 合并后的密度会使前驱簇的密度大幅降低。

最后，所有簇按密度递减排序。

如果指定了 `--symbol-ordering-file=`，则 `--symbol-ordering-file=` 指定的节会被放在最前面。调用图谱分析仍会用于其他节（lld \>= 20).

优先级高于 `--call-graph-profile-sort`.

当同时指定 `--call-graph-profile-sort` 和 `--print-symbol-order=` 时，ld.lld 会将符号顺序转储到指定的文件中。该文件可以配合 `--symbol-ordering-file=`.

### `--bp-compression-sort=` 和 `--bp-startup-sort=`

这两个选项都指示链接器按照以下目标优化节的布局：

- `--bp-compression-sort=[data|function|both]`：通过将相似节分组在一起，改善 Lempel-Ziv 压缩，从而得到更小的压缩 App 体积。
- `--bp-startup-sort=function --irpgo-profile=<file>`：利用时序分析文件减少程序启动期间的页错误。

链接器通过考虑以下三组来决定节顺序：

- 函数节：按照时序剖析（`--irpgo-profile=`）排序，优先放置较早访问和频繁访问的函数。
- 函数节：包含相似函数的节被放置在一起，以最大化压缩效率。
- 数据节：相似的数据节被放置在一起。

在每个组内，使用平衡分区算法对节进行排序。

链接器构建一个二分图，包含两组顶点：节和效用顶点。

- 对于剖析引导的函数节：

    - 效用顶点的数量由剖析文件中的符号顺序决定。
    - 如果指定 `--bp-compression-sort-startup-functions`，则会分配额外的效用顶点，优先考虑相邻函数的相似性。
- 对于为压缩而排序的节：效用顶点通过分析节内容和重定位中的 k-mers 来确定。

在此优化期间，调用图谱分析被禁用。

当指定了 `--symbol-ordering-file=` 时，该文件中描述的节会被放在更靠前的位置。

### `-z nosectionheader`

GNU ld 2.41 引入了省略节头表的选项。

### `--unique`

默认情况下，链接器将所有同名输入节合并到一个输出节中。例如，来自不同目标文件的所有 `.text` 节会被合并为一个 `.text` 输出节。

GNU 的 `--unique` 选项会为每个孤立节创建独立的输出节。请注意，使用 `-r`（可重定位输出）时，内部链接器脚本仍会导致某些节（如 `.text` 和 `.debug_info`）被合并。

如需更精细的控制，使用 `--unique=glob` 匹配特定模式——例如，`--unique=*` 匹配所有节。

ld.lld 只实现了适用于所有节的 `--unique` 形式。没有链接器脚本时，它会把所有输入节都视为孤立节。

### `--cref`

输出交叉引用表。对于每个 non-local 符号，输出其定义所在文件以及所有引用该符号的文件列表。

### `-m` 和 `-map=<file>`

输出链接映射，你可以查看输出节的地址、文件偏移以及包含的输入节。

### `--fatal-warnings`

将警告视为错误。警告和错误的区别在于，除了是否包含 `warning` 或 `error` 字符串之外，更重要的区别是错误会阻止链接结果的输出。

### `--noinhibit-exec`

将某些错误降级为警告。注意不要指定 `--fatal-warnings` 将降级后的警告再次提升为错误:)

### `--no-warnings`

压制警告。因 `--fatal-warnings` 而转为错误的警告不会被压制。

### `--shuffle-sections=<seed>`

打乱输入节的顺序，以揭露那些依赖于特定节顺序的缺陷。

### `--randomize-section-padding=<seed>`

使用给定的种子，在输入节之间以及每个段的开头随机插入填充字节。

想象一种变更，它意外地降低了频繁执行函数的内存对齐。虽然原始程序可能没有保证该函数的对齐，但该变更可能会加剧这个问题。使用 `--randomize-section-padding` 可以通过在内存布局中引入可变性来帮助发现此类细微的性能衰退。

## 其他

### `--build-id=value`

生成 `.note.gnu.build-id` 以便为输出提供一个标识符。该标识符通过对整个输出进行哈希运算来生成。

SHA-1 是最常见的选择。链接器会用零填充 `.note.gnu.build-id` 的内容，逐字节进行哈希，然后将结果写回 `.note.gnu.build-id`。某些链接器使用 tree-style 风格的哈希以实现并行。

### `--compress-debug-sections=[zlib|zstd]`

使用 zlib 或 zstd 压缩输出文件的 `.debug_*` 节，并标记 `SHF_COMPRESSED`。参见[压缩调试节](https://maskray.me/blog/2022-01-23-compressed-debug-sections).

### `--format=binary`, `-b binary`

每个输入文件都会被当作一个 ELF 文件处理，其 `.data` 节包含该文件的原始二进制内容。符号 `_binary_<filename>_{start,end,size}` 被定义用于访问嵌入的数据。

```plaintext
echo hello > a.txt
ld.bfd -r -b binary -m elf_x86_64 a.txt
objdump -s a.out
```

输出：1  
2  
3  
4  
a.out：文件格式 elf64-x86-64  
  
节 .data 的内容：  
 0000 68656c6c 6f0a hello.

输入文件的转换方式类似于以下 objcopy 操作：

```plaintext
# compatible with llvm-objcopy
objcopy -I binary -O elf64-x86-64 a.txt a.o

# GNU objcopy only
objcopy -I binary -O default a.txt a.o
```

### `--hash-style=style`

ELF 规范要求一个哈希表 `DT_HASH` 用于动态符号查找。`--hash-style=sysv` 用于生成该表。

`DT_GNU_HASH` 在空间消耗和性能方面都比 `DT_HASH` 好。mips 使用另一种 `DT_MIPS_XHASH`（这是 mips abi 自食其果的一个好例子）。我个人认为 `DT_MIPS_XHASH` 是在解决一个错误的问题。事实上，有一种方法可以使用 `DT_GNU_HASH`，但 mips 社区的人可能不想再为它费心了。

参见[glibc 与 DT_GNU_HASH](https://maskray.me/blog/2022-08-21-glibc-and-dt-gnu-hash)以了解关于“简易反作弊”的故事。Anti-Cheat".

### `--no-ld-generated-unwind-info`

参见[PR12570.plt 没有关联的 .eh_frame/.debug_frame](https://sourceware.org/bugzilla/show_bug.cgi?id=12570).

当 pc 位于 plt 条目中时，如果链接器没有合成 `.eh_frame` 信息，从当前 PC 展开将无法获取帧。在 i386 和 x86-64 上，在延迟绑定状态下，对 plt 条目的第一次调用会执行 push 指令。在 esp/rsp 改变后，如果 plt 条目没有由 `.eh_frame` 提供的展开信息，展开器可能无法正确展开，这会影响性能分析工具的准确性。

```plaintext
jmp *got(%rip)
pushq $0x0
jmpq .plt
```

然而，由于 `-Wl,-z,relro,-z,now` (BIND_NOW). PLT（BIND_NOW）的普遍使用，此特性如今已基本过时。PLT 条目的行为类似于没有序言的函数。性能分析工具可以通过默认规则轻松获取返回地址：如果某个代码区域没有被元数据覆盖，则假定返回地址在 `*rsp` (x86-64).

处。PLT 名称，性能分析工具需要执行以下操作：

- 解析 `.plt` 节以识别 PLT 条目的区域
- 解析 `.rel[a].plt` 以获取 `R_*_JUMP_SLOT` 动态重定位及其引用的符号名称。
- 如果当前 PC 位于 PLT 区域内，则解析附近的指令并找到 GOT 加载位置。关联的 `R_*_JUMP_SLOT` 标识了符号名称。
- 拼接符号名称和 `@plt` 以形成 `foo@plt`

注意：`foo@plt` 是 objdump 等工具使用的约定，但目标文件中并不包含这样的符号。

gdb 有启发式方法来识别这种情况。

此问题不会影响 C++ 异常。PLT 条目是一个尾调用，由 `_Unwind_RaiseException` 调用的 `__cxa_throw` 会穿透 ld.so 解析器和 PLT 条目的尾调用。PC 会被恢复为 PLT 条目调用者的下一条指令。

```cpp
// b.cc - b.so
void ext() { throw 3; }

// a.cc - exe
#include <stdio.h>

void ext();
void foo() {
  try {
    ext(); // PLT entry
  } catch (int x) {
    printf("%d\n", x);
  }
}

int main() {
  foo();
}
```

### `-O`

启用大小优化。此优化级别不同于编译器驱动选项 `-O`. `-O`。`--lto-O` 不意味着 LTO：它对 LTO 代码生成没有影响。

在 ld.lld 中，ld.lld, `-O1` 是默认值。

`-O0` 禁用对 `SHF_MERGE`.

`-O2` 的常量合并。

- 启用 `SHF_MERGE|SHF_STRINGS` 的字符串后缀合并。该操作非常慢，且无法并行执行。
- `--compress-debug-sections=zlib` 使用压缩率更高的 zlib 压缩。
- 从 14.0.0 版本开始，在 `.strtab` 中去除重复的局部符号名称。一旦 ld.lld 支持并行写入 `.symtab`，我可能会完全移除这一功能。

在 GNU ld 中，非零的 `-O` 可以让 `.hash` 和 `.gnu.hash` 更小。

对于引用 `SHF_MERGE` 节的符号赋值，它被认为是指向常量数据元素。在去重之后，符号值会被调整，以指向输出节中的数据元素。

### `-plugin file`

GNU ld 和 gold 支持用此选项加载 GCC LTO 插件（`liblto_plugin.so`）或 LLVM LTO 插件（`LLVMgold.so`）。除非指定 `-fuse-ld=lld`，否则 `clang -flto={full,thin}` 会传递 `-plugin path/to/LLVMgold.so`。

`binutils-gdb/include/plugin-api.h` 定义了插件 API.

尽管 `LLVMgold.so` 的名称中含有 gold，该文件仍可由 GNU binutils（ld、gold、nm、ar）和 mold 使用。

### `--verbose`

GNU ld 使用此选项转储链接脚本（内置或外部）。gold、ld.lld 和 mold 并非由链接脚本驱动，因此没有链接脚本输出。

### `-Ttext-segment`

文本段传统上是第一个段。指定了 `-Ttext-segment` 的用户可能实际上是想指定映像基址。当同时使用 `-z separate-code` 时，此选项具有奇怪的语义（可能是一个 bug）：[https://sourceware.org/bugzilla/show_bug.cgi?id=25207](https://sourceware.org/bugzilla/show_bug.cgi?id=25207).

ld.lld 提供 `--image-base` 来设置映像基址。

GNU ld 的 PE/COFF 移植很早就支持 `--image-base`，并在 binutils 2.44 中为 ELF 实现了该选项。

该选项似乎主要用于配合 `mmap` 的 `MAP_FIXED`，以避免与 ASLR 冲突。更好的选择是不要设置固定地址。qemu 的 `linux-user/elfload.c:probe_guest_base` 或许能提供一些思路。

## Target-specific

### `--cmse-implib`, `--out-implib=out.lib`

请参阅[AArch32 的链接器笔记](https://maskray.me/blog/2023-04-23-linker-notes-on-aarch32)
