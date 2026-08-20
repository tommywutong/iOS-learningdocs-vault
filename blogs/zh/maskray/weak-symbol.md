---
title: 弱符号
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2021-04-25-weak-symbol'
original_language: en
published: 2021-04-25
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:75e0cc45a2ca26c5'
translated: true
---

> [弱符号](https://maskray.me/blog/2021-04-25-weak-symbol)　·　MaskRay (宋方睿)

[2021-04-25](https://maskray.me/blog/2021-04-25-weak-symbol)

# 弱符号

更新于 2026 年 3 月。

## C/C++

GCC 和 Clang 支持用 `__attribute__((weak))` 将符号标记为弱符号。预处理指令 `#pragma weak symbol` 可以达到相同效果。

## 对象文件格式

在 ELF 中有三种主要的符号绑定。ELF 规范说明如下：

- `STB_LOCAL`：局部符号在其所在对象文件之外不可见。多个文件中可以存在同名的局部符号而互不干扰。
- `STB_GLOBAL`：全局符号对所有参与链接的对象文件均可见。一个文件对全局符号的定义可以满足另一个文件对同一全局符号的未定义引用。
- `STB_WEAK`：弱符号与全局符号相似，但它们的定义优先级较低。

在 GNU ABI 中，还有一种绑定 `STB_GNU_UNIQUE`，它类似于 `STB_GLOBAL`，但具有额外的语义（即使使用 `RTLD_LOCAL` 也是唯一的，且带有 nodelete）。

在 GNU as 风格的汇编中，可以通过 `.weak sym` 设置符号的绑定。

一个符号只有一种绑定，因此不能同时为全局符号和弱符号。不过，自 [1996 年](https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=5ca547dc2399a0a5d9f20626d4bf5547c3ccfddd)起，GNU as 中的 `.weak` 会覆盖 `.globl`；LLVM 集成汇编器则以后出现的指令为准。自 LLVM 12（[D90108](https://reviews.llvm.org/D90108)）起，集成汇编器会对绑定变化报错或警告。对于 `.globl sym; .weak sym`，它只发出警告而不是错误，因为该行为确实与 GNU as 一致，但依赖指令覆盖很容易出错。

```plaintext
# error: local changed binding to STB_GLOBAL
local:
.local local
.globl local

## `.globl x; .weak x` matches the GNU as behavior. llvm-mc issues a warning.
# warning: global changed binding to STB_WEAK
global:
.global global
.weak global

# error: weak changed binding to STB_LOCAL
weak:
.weak weak
.local weak
```

弱符号既可以是定义，也可以是引用（即未定义符号），二者通过节索引区分：

- `st_shndx==SHN_UNDEF`：弱引用
- `st_shndx!=SHN_UNDEF`：弱定义

## ELF 规范要求的语义

规范对弱符号的描述非常有限。

> 当链接编辑器组合多个可重定位对象文件时，它不允许存在多个同名的 STB_GLOBAL 符号定义。另一方面，如果存在一个已定义的全局符号，那么出现同名弱符号不会导致错误。链接编辑器会采用全局定义并忽略弱定义。类似地，如果存在一个 common 符号（即其 _shndx 字段值为 SHN_COMMON 的符号），那么出现同名弱符号也不会导致错误。链接编辑器会采用 common 定义并忽略弱定义。
>  
> 当链接编辑器搜索归档库时（参见第 7 章中的“归档文件”），它会提取包含未定义全局符号之定义的归档成员。该成员中的定义可以是全局符号，也可以是弱符号。链接编辑器不会为解析未定义弱符号而提取归档成员。未解析弱符号的值为零。

弱定义允许多个定义。全局定义可以覆盖弱定义，但当存在两个同名的弱定义而没有全局定义时，链接器应该如何处理则未作说明。在 GNU ld/gold/ld.lld 中，链接器选择第一个弱定义并将所有引用解析到该定义。

未定义的弱符号不会触发归档成员提取。（ld.lld 使用一个弱 `LazyObject` 来表示这样的符号。）

另有一条备注：

> 弱符号在本文档未指定区域的行为由实现定义。弱符号主要供系统软件使用。使用弱符号的应用程序不可靠，因为运行时环境的变化可能导致执行失败。

## 弱定义

在 C++ 中，内联函数、模板实例化以及其他一些实体可以在多个对象文件中定义，但需要在链接时进行去重。

在 `.gnu.linkonce.*`/`GRP_COMDAT` 出现之前，实现会使用弱定义来避免链接器的多重定义错误。`GRP_COMDAT` 出现后，这一惯例仍被保留，可用于兼容不理解早期 `.gnu.linkonce.*` 或 COMDAT 的链接器。为 COMDAT 定义使用 `STB_GLOBAL` 可以检测 COMDAT 定义与非 COMDAT 定义共同造成的 ODR 违规，但这会是一次重大的行为变更。gold 提供 `--detect-odr-violations` 选项，用于检查两个弱定义的“文件:行号”调试信息是否不同。

可替换的定义可以声明为 weak。来自另一个翻译单元的 `STB_GLOBAL` 定义可以覆盖它。这是提供库中默认/后备定义并允许应用重新定义的绝佳方式。

```cpp
// lib.cc
__attribute__((weak)) void fun() {
  ...
}

void feature() {
  fun();
}

// app.cc - override the default implementation
void fun() {
  ...
}
```

弱别名是弱定义的一种特殊形式：它复用现有定义来定义弱符号。一种实用技巧是创建一个指向局部定义的弱符号别名。1  
2  
static void impl() {}  
__attribute__((weak,alias("impl"))) void fun();

（下面是一个在 GCC 4.8.2 中引入、在 4.9.2/5.0 中修复的跨过程优化错误示例。1  
2  
3  
4  
5  
// https://gcc.gnu.org/bugzilla/show_bug.cgi?id=61144  
// foo 是一个不精确的定义，但 ipa 错误地将 bar() 优化为总是返回 0。
static int dummy = 0;  
extern int foo __attribute__((__weak__, __alias__("dummy")));  
int bar() { if (foo) return 1; return 0; }  
 )

## 弱引用

ELF 规范指出：“未解析的弱符号值为零。”可以利用这一属性检查是否提供了某个定义，常见用法是实现可选钩子。

```cpp
__attribute__((weak)) void undef_weak_fun();

  if (&undef_weak_fun)
    undef_weak_fun();
```

编译器不知道符号最终是已定义还是未定义。它通常采取保守做法，生成从 GOT 表项加载地址的代码序列。

```plaintext
# AArch64
adrp    x0, :got:undef_weak_fun
ldr     x0, [x0, :got_lo12:undef_weak_fun]

# x86-64
movq    undef_weak_fun@GOTPCREL(%rip), %rax

# riscv64
.Lpcrel_hi0:
auipc   a0, %got_pcrel_hi(undef_weak_fun)
ld      a0, %pcrel_lo(.Lpcrel_hi0)(a0)
```

该代码序列包含一个或多个产生 GOT-generating 的重定位项。

如果该符号最终未定义，则生成的 GOT 表项初始值为零且没有对应的动态重定位。在 run-time 时，代码将获取一个零地址。

如果该符号最终已定义，则在 run-time 时，代码将获取该符号的地址。请参阅[全局偏移表详解](https://maskray.me/blog/2021-08-29-all-about-global-offset-table).

历史上，工具链，尤其是针对 lesser-used 架构的工具链，在弱引用方面往往有更多缺陷，因此 musl 避免使用弱引用。上述模式可以用弱别名替代。

```cpp
static void noop() {}
__attribute__((weak,alias("noop"))) void undef_weak_fun();

  undef_weak_fun();
```

在大多数情况下，弱引用会解析为该符号的一个 GOT 表项。

对于 ELF `-fno-pic`，存在一个优化：发出的代码可以使用绝对重定位来检查地址是否为零。但是，如果该符号最终在共享对象中定义，并且链接后的映像需要动态节，则将产生一个[规范 PLT 表项](https://maskray.me/blog/2021-01-09-copy-relocations-canonical-plt-entries-and-protected).

PE-COFF 可以使用一个 `IMAGE_SYM_CLASS_WEAK_EXTERNAL` `IMAGE_SYM_UNDEFINED` 辅助符号 `IMAGE_SYM_CLASS_EXTERNAL` `IMAGE_SYM_ABSOLUTE` 来模拟此特性 `.weak.<weaksymbol>.<relatedstrongsymbol>` 中的命名方式）。GNU).

如果弱引用最终未定义，MinGW 的 `.refptr.` 机制可以确保该值为 0。

### `.weakref` 指令

GNU 汇编器的[`.weakref alias, target`](https://sourceware.org/pipermail/binutils/2005-October/044471.html)会创建一个弱别名，而不直接修改目标符号的绑定。所有使用 `alias` 的重定位都会被重定向到 `target`.

- 如果 `target` 已定义或被直接引用，则 `target` 的绑定不受影响（如果使用了 `target`，`.weak target` 仍然可以为弱绑定）。保留 `STB_GLOBAL` 支持[归档成员提取](https://maskray.me/blog/2021-06-20-symbol-processing#archive-processing).
- 如果 `target` 仅通过该别名被引用，则 `target` 会成为未定义的弱符号。

```plaintext
.weakref foo, bar
call foo       # relocation references bar; bar becomes WEAK UNDEF

.weakref foo2, bar2
call foo2      # relocation references bar2; bar2 remains GLOBAL UNDEF
call bar2
```

LLVM 集成汇编器的 `.weakref` 处理存在若干问题（未引用的 `.weakref` 创建未定义的目标、崩溃），这些我已于[2025 年 5 月重构](https://github.com/llvm/llvm-project/commit/95756e67c230c231c616a9aeabc2eea1e2831829).

GCC 的特性，如运行时库头文件 `[[gnu::weakref]]` 中所用，即利用了此功能。`libgcc/gthr-posix.h`

```c
// Equivalent to: .weakref __gthrw_pthread_create, pthread_create
// If pthread_create is not otherwise referenced, it becomes a weak reference,
// avoiding pulling in pthread archive members unnecessarily.
static __typeof(pthread_create) __gthrw_pthread_create
  __attribute__((__weakref__("pthread_create"), __copy__(pthread_create)));
```

弱引用可以由共享对象定义来满足。此时弱引用与常规引用没有区别。

### 弱引用与归档文件

这是一条 lesser-known 规则。当 ELF 链接器看到一个弱引用时，它不会为了满足该弱引用而提取归档成员。请确保归档成员因其他符号而被提取。

有一个相关的[libstdc++ 中长期存在的问题](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=58909)：由于对 `pthread_*` 的引用是弱引用，`-lpthread` 中的相关成员在静态链接时可能不会被提取：

```text
% cat a.cc
#include <condition_variable>
int main() { std::condition_variable a; }
% g++ -static -pthread a.cc
% ./a.out
Segmentation fault
```

你可以使用 `-Wl,-y` 来理解发生此情况的原因。GNUld 会在不需要提取时丢弃归档文件，因此我必须使用 ld.lld 来展示 `lazy definition`. 1  
2  
3  
% g++ -fuse-ld=lld -static a.cc -lpthread -Wl,-y,pthread_cond_destroy  
/usr/lib/gcc/x86_64-linux-gnu/10/../../../x86_64-linux-gnu/libpthread.a: lazy definition of pthread_cond_destroy  
/usr/lib/gcc/x86_64-linux-gnu/10/libstdc++.a(condition_variable.o): reference to pthread_cond_destroy

### 链接映像中未定义符号的绑定

如果一个目标文件有一个未被其他目标文件定义的未定义符号（对于归档文件，我们认为提取出的归档成员与目标文件相同），则该符号在链接映像中是未定义的。该符号可能由共享对象定义，但链接映像中仍然有一个未定义符号。如果对该符号的所有重定位都被 `--gc-sections` 丢弃，则该未定义符号将从链接映像中移除。如果该未定义符号被保留，我们就说它是未解析的。

如果符号是 `STB_GLOBAL`. (`-z undefs`，链接器通常会报告一个未定义符号错误（`--no-allow-shlib-undefined` 和[是链接可执行文件时的默认设置；详情请参阅 GNU 风格链接器选项解析](https://maskray.me/blog/2020-11-15-explain-gnu-linker-options)。如果符号是未版本化的弱符号，链接器将抑制此诊断信息。（如果符号是版本化的弱符号，链接器仍会报告错误。请参阅[符号版本控制详解](https://maskray.me/blog/2020-11-26-all-about-symbol-versioning))

未定义符号不允许为 `STB_LOCAL`，因此绑定可以是 `STB_GLOBAL` 或 `STB_WEAK`。如果目标文件中所有的未定义符号都是 `STB_WEAK`，则绑定为 `STB_WEAK`，否则绑定为 `STB_GLOBAL`。注意：共享对象中的符号不影响绑定。

### 重定位类型

#### `-fno-pic`

GCC 和 Clang 的 `-fno-pic` 对于大多数目标会发出绝对重定位。ppc64 使用 TOC-generating 重定位。aarch64 使用 `.rodata.cst8`，其类似于 GOT.

`clang -fno-pic -fno-direct-access-external-data` 会发出 GOT-generating 重定位，即使对于隐藏的未定义弱符号也是如此。

#### `-fpie` 和 `-fpic`

编译器不会发出 PC-relative 重定位。

GCC 和 Clang `-fpie` 和 `-fpic` 会发出 GOT-generating 重定位，即使是针对隐藏的未定义弱符号也是如此。ppc64 `-fno-pic` 会发出 TOC-generating 重定位。

在初始化静态存储数据时获取地址可能会发出绝对重定位。

### 未解析的弱引用和 `R_*_GLOB_DAT`

#### 绝对重定位

在 `-no-pie` 模式下，GNU ld、gold 和 ld.lld 都会将绝对重定位静态解析为 0。

`-pie` 和 `-shared` 的情况则比较复杂。在 GNU ld 中，不同端口的行为不同。x86 端口试图变得智能（观察，应该接近成文规则）：如果至少有一个 GOT-generating 或 PLT-generating 重定位，并且 `-z dynamic-undefined-weak`（默认启用）生效，则会生成动态重定位。这可能会导致 `R_X86_64_64` 文本重定位，而 `-z text`.

相关问题：

在 [2017 年 11 月](https://sourceware.org/bugzilla/show_bug.cgi?id=22269#c30)之前，GNU ld aarch64 可能为静态 PIE 生成 `R_AARCH64_ABS64` 动态重定位。在 [2020 年 11 月](https://sourceware.org/bugzilla/show_bug.cgi?id=22269#c40)之前，GNU ld arm 可能为静态 PIE 生成 `R_ARM_RELATIVE` 动态重定位。自 [2021 年 5 月](https://sourceware.org/git/gitweb.cgi?p=binutils-gdb.git;h=4916030821bb0b052091bd1e29f1851e1512a056)起，如果不需要文本重定位，GNU ld ppc 默认会生成动态重定位。

ppc 自 2021-05 起支持 `-z {,no}dynamic-undefined-weak`。

ld.lld just emits dynamic relocations unconditionally for `-pie` and `-shared`, since 13.0.0 ([D105164](https://reviews.llvm.org/D105164)). Previous versions may suppress the relocation for `-pie`.

#### PC-relative 重定位

现代编译器不会发出 non-branch PC-relative 重定位。

GCC\<5（至少 x86_64 和 arm）可能会为隐藏的未定义弱符号发出 PC-relative 重定位。GCC\<5 i386 可能会将 `if (&foo) foo();` 优化为无条件调用 `foo();`.

#### 分支重定位

解析为当前指令、下一条指令或相对零地址，具体取决于架构，有时还取决于重定位类型。

对于 `-no-pie`，没有动态重定位。行为如下：

- aarch64：GNU ld：将指令重写为 NOP; ld.lld：跳转到下一条指令
- mips：GNU ld：跳转到文本段起始位置（？）
- ppc32：GNU ld：将指令重写为 NOP; ld.lld：跳转到当前指令
- ppc64：GNU ld：将指令重写为 NOP; ld.lld：跳转到当前指令
- riscv：GNU ld：跳转到绝对零地址；ld.lld：跳转到当前指令（[D103001](https://reviews.llvm.org/D103001))
- i386/x86_64: GNU ld/ld.lld：跳转到 link-time 零地址

aarch64 ABI 规定

> 在不支持符号动态 pre-emption 的平台上，由 `R_<CLS>_CALL26` 重定位的未解析弱引用应被视为跳转到下一条指令（该调用成为 no-op）。在此条件下，`R_<CLS>_JUMP26` 和 `R_<CLS>_PLT32` 的行为不受本标准的约束。

据我所知，在其他 ABI 上，这些行为大多未作规定。

#### GOT-generating 重定位

链接器可能会或可能不会为该 `R_*_GLOB_DAT` 条目生成动态重定位 GOT。如果没有 `R_*_GLOB_DAT` 条目在运行时始终为零。如果有 GOT，则该 `R_*_GLOB_DAT` 条目可能为 GOT 非零 non-zero，如果某个立即加载的共享对象在运行时定义了该符号。

GNU ld 的 x86 移植版试图表现得智能一些：如果至少有一个 GOT-generating 或 PLT-generating 重定位，并且 `-z dynamic-undefined-weak`（默认启用）生效，则生成一个 `R_*_GLOB_DAT`。对于 `-fpie` 和 `-fpic` 代码，链接器输出中通常有 `R_*_GLOB_DAT`；对于 `-fno-pic` 代码，则没有。

ppc 自 2021-05 起支持 `-z {,no}dynamic-undefined-weak`。

对于静态 PIE（由选项 `--no-dynamic-linker` 指示），他们认为不应有动态重定位。实际上 glibc 的 `--enable-static-pie` 支持依赖于这个（我认为很脆弱的）属性，e.g。例如 `__pthread_mutex_lock` 中的 `_dl_add_to_namespace_list` 引用，以及 `__pthread_initialize_minimal` 中的 `csu/libc-start.c`.

ld.lld generates `R_*_GLOB_DAT` in `-pie` and `-shared` modes.

#### 备注

不同目标对是否应该生成动态重定位有不同看法。GNU ld x86 可以用 `-z dynamic-undefined-weak` 禁用该重定位（[相关问题](https://sourceware.org/bugzilla/show_bug.cgi?id=19636)）。GNU ld 所采用的“至少存在一个生成 GOT 或 PLT 的重定位”条件带来了不必要的复杂性。

ld.lld [implemented `-z [no]dynamic-undefined-weak`](https://github.com/llvm/llvm-project/pull/143831) with the following effects:

- 静态 `-no-pie`: no-op
- 动态 `-no-pie`: `nodynamic-undefined-weak` 会抑制 `GLOB_DAT`/`JUMP_SLOT`
- 静态 `-pie`: `dynamic-undefined-weak` 会生成 `ABS`/`GLOB_DAT`/`JUMP_SLOT`
- 动态 `-pie`: `nodynamic-undefined-weak` 会抑制 `ABS`/`GLOB_DAT`/`JUMP_SLOT`

ld.lld 对动态 `-pie` 的处理通常与 GNU ld 不同。可移植代码不应依赖 `R_*_GLOB_DAT` 是否存在。ld.lld 目前对绝对重定位与生成 GOT 的重定位处理不一致：在下面的示例中，它会生成 `R_*_GLOB_DAT`，却抑制绝对重定位。

```c
// https://bugs.llvm.org/show_bug.cgi?id=50759
extern __attribute__((weak)) int weak_reference;
__attribute__((visibility("hidden"))) int* address_of_weak_reference = &weak_reference;

void _start() {
  if (&weak_reference)
    weak_reference = 1;
  if (address_of_weak_reference)
    *address_of_weak_reference = 1;
}
```

## ld.so

动态符号表中的 `STB_GLOBAL` 定义和 `STB_WEAK` 定义在 glibcld.so 和 muslld.so 中是等价的。如果符号查找找到了一个 `STB_WEAK` 定义，它会停止并返回该符号，而不是继续搜索共享对象。glibc 2.2 之前提供了一种不同的行为：`STB_WEAK` 定义可以被后续的 `STB_GLOBAL` 定义覆盖。

FreeBSD 的 ld.so 仍然使用旧版的 glibc 行为。[https://reviews.freebsd.org/D26352](https://reviews.freebsd.org/D26352)在环境变量 `LD_DYNAMIC_WEAK=1`.

动态符号表中的弱引用不会因为在任何位置都找不到定义而导致符号查找错误。

## PDP-11 对象文件格式

_PDP-11MACRO-11 语言参考手册_提到了 `.WEAK` 指令。

> 当 .WEAK 指令指定了一个外部定义的符号时，它被视为全局符号。如果链接器在另一个模块中找到了该符号的定义，它会使用该定义。如果链接器没有找到外部定义，则该符号的值为 0。链接器不会为了这个全局符号而去搜索库，但如果因其他原因从库中引入的某个模块包含了该符号的定义，链接器会使用该定义。
>  
> 如果当前模块中定义的符号由 .WEAK 指令指定，则该符号被视为全局定义。但是，如果当前模块被插入到对象库中，则该符号不会插入到库的符号表中。因此，在链接时搜索库以解析该符号时，不会找到该模块。

请注意，其用于外部定义符号的弱指令与 ELF 弱引用的语义非常接近。它可能是弱符号的起源。

不过，我不理解其弱定义的语义。

## BSD a.out

1994 年，Paul Kranenburg (pk) 为 NetBSD 风格的 a.out 二进制格式添加了弱符号支持。请参见[https://github.com/NetBSD/src/commit/8e0a22a5fb5d6662c8c3aae3e09ea86cf621f82f](https://github.com/NetBSD/src/commit/8e0a22a5fb5d6662c8c3aae3e09ea86cf621f82f)。它被认为比间接符号（`N_INDR`).

之前未使用的字段 `n_other` 的使用方式类似于 ELF `st_other`: `N_AUX` 取其最低有效 4 位，而 `N_BIND` 取剩余 4 位。

## Mach-O

与 ELF 不同，弱引用可以提取归档成员来满足该弱引用。

弱动态库符号也可以提取存档成员。

`.weak_definition` 设置 `N_WEAK_DEF`，用于弱定义（common/linkonce/linkonce_any/weak/weak_any）。在 ld64 中，绝对符号（`N_ABS`）会忽略 `N_WEAK_DEF`。

当多个弱定义合并时，如果所有输入都是 private extern，则输出也将只是 private extern 且不会被导出。如果任何符号带有 `N_NO_DEAD_STRIP` 位，则输出不会进行死代码剥离。

`.weak_def_can_be_hidden`（Mac OS X 10.6）会设置 `N_WEAK_DEF` 和 `N_WEAK_REF`。LLVMAsmPrinter 会为具有 `local_unnamed_addr`（非常量 `GlobalVariable` 除外）或 `unname_addr` 的 `linkonce_odr` 定义设置该属性。在链接器中，这类似于 `N_PEXT`（PrivateExtern）。如果所有实例都是 PrivateExtern 或 `.weak_def_can_be_hidden`，符号就不会被导出，也不会出现在弱绑定表中。在 ld64 中，一个 `weak_def_can_be_hidden` 定义可以覆盖一个 `N_PEXT` 定义。

弱绑定发生在平面命名空间中。

可执行文件中的弱定义优先于动态库中的强定义，但这只影响绑定时的符号解析；动态库内部的调用仍使用该动态库自身的定义。

```c
// shared.c
#include <stdio.h>
void f(void) { puts(__FILE_NAME__); }
void g(void) { f(); }

// main.c
#include <stdio.h>
[[gnu::weak]] void f(void) { puts(__FILE_NAME__); }
void g(void);
int main(void) {
  f(); // prints "main.c"
  g(); // prints "shared.c"
  return 0;
}
```

动态库中的弱定义可能输给后一个动态库中的强定义。

## PE/COFF

PE/COFF 没有直接的对应项，但可以通过一个带已定义 `IMAGE_SYM_CLASS_WEAK_EXTERNAL` `IMAGE_SYM_UNDEFINED` 辅助符号的 `IMAGE_SYM_CLASS_EXTERNAL` 符号来模拟弱定义（在 `.weak.<weaksymbol>.<relatedstrongsymbol>` 中命名为 GNU）。如果该符号在其他目标文件中没有常规定义，链接器将选择辅助定义。

辅助符号是已定义的。需要注意减少导致重复定义错误的可能性。（[link.exe。MinGW 和](https://reviews.llvm.org/D75989)要求辅助符号为外部 LLVM 为这样的弱定义推导出一个唯一名称 `.weak.$name.default.$something`。同一目标文件中已定义的外部符号是 `$something`. LLVM 的理想候选。LLVMnon-comdat 更倾向于一个[https://reviews.llvm.org/D75989](https://reviews.llvm.org/D75989)).

主要有三个链接器：MSVC `link.exe`、GNU ld（PE/COFF 移植）和 lld。当名称类似“lld-link”时，lld 的行为类似 `link.exe`；名称类似 `ld.lld` 时，lld 的行为类似 GNU ld 的 PE/COFF 移植，并使用某种 PE 仿真（例如 `i386pe, i386pep, thumb2pe, arm64pe`）。

`link.exe` 对于两个弱定义会报告重复定义错误。GNUld 和 `lld-link -lld-allow-duplicate-weak`（或 `-lldmingw`）都允许此行为，遵循 ELF 的处理方式。

```sh
printf '__attribute__((weak)) int def() { return 0; } int main() { def(); }' > a.c
printf '__attribute__((weak)) int def() { return 1; } void unused() {}' > b.c
x86_64-w64-mingw32-gcc -c a.c b.c
x86_64-w64-mingw32-gcc a.o b.o     # ok, no "multiple definition" error
wine a.exe                         # exit code is 0
```

link.exe 支持 `/alternatename:`，可以达到类似效果。该选项为符号指定了一个回退定义。如果该符号原本未定义，链接器将使用回退定义。

link.exe 不支持使用 GNU `.weak.*` 命名方案来链接两个弱定义：`fatal error LNK1227: conflicting weak extern definition for '?weak@@YAXXZ'.  New default '.weak.?weak@@YAXXZ.default.?foo@@YAXXZ' conflicts with old default '.weak.?wea....`

link.exe 不支持在有 `.pdata` 存在时用强定义覆盖弱定义：`fatal error LNK1223: invalid or corrupt file: file contains invalid .pdata contributions`

```sh
printf '__attribute__((weak)) void undef_weak_fun(); int main() { if (&undef_weak_fun) undef_weak_fun(); }' > a.c
llvm-objdump -t a.o          # .weak.undef_weak_fun.main
x86_64-w64-mingw32-gcc a.c   # ok, no "undefined reference" error
wine a.exe
```

lld-link 允许将未定义的引用解析为弱定义。GNUld 因[https://sourceware.org/PR9687](https://sourceware.org/PR9687). 1  
2  
3  
printf 'void f(); int main() { f(); }' \> a.c  
printf '__attribute__((weak)) void f() {} void unused() {}' \> b.c  
x86_64-w64-mingw32-gcc -c a.c b.c  
 1  
2  
3  
% x86_64-w64-mingw32-gcc a.o b.o  
/usr/bin/x86_64-w64-mingw32-ld: /tmp/ccyRH2ap.o:a.c:(.text+0xe): undefined reference to `f'  
collect2: error: ld returned 1 exit status

如果我们将`f`中的 `a.c` 改为弱引用（添加 `__attribute__((weak))`), GNUld 会像 lld-link.

## XCOFF

XCOFF 通过弱外部符号（`C_WEAKEXT`）支持弱定义。不支持弱引用。

`-qnoweakexp` 要求 AIXld 不导出弱外部符号。这可以达到类似 `-fvisibility-inlines-hidden`.
