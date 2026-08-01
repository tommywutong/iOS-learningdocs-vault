---
title: 可重定位链接
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2022-11-21-relocatable-linking'
original_language: en
published: 2022-11-21
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b7ef1e8e20aa2984'
translated: true
---

> 原文：[可重定位链接](https://maskray.me/blog/2022-11-21-relocatable-linking)　·　MaskRay (宋方睿)

[2022-11-21](https://maskray.me/blog/2022-11-21-relocatable-linking)

# 可重定位链接

更新于 2025-02。

在 GNU ld 中，`-r` 会生成可重定位目标文件。这称为可重定位链接或部分链接。该模式会抑制许多为可执行文件或共享对象输出执行的阶段（`-no-pie/-pie/-shared` 模式）。`-r`、`-no-pie`、`-pie` 和 `-shared` 指定四种不同模式，四个选项互斥。

可重定位输出可用于分析和二进制操作，之后还可用来链接最终的可执行文件或共享对象。

```sh
clang -pie a.o b.o

# ==>

clang -r a.o b.o -o r.o
clang -pie r.o
```

下面依次考察各个链接器阶段，看看可重定位链接会如何改变操作。

## 链接器阶段

### 查找并扫描输入文件

只允许将可重定位目标文件、归档文件和链接器脚本作为输入。为支持 LTO，也可能允许另一类文件。其他文件会导致错误。换句话说，`-r` 隐含 `-static`（`-Bstatic`）。

```plaintext
% ld -r a.o b.so
ld.lld: error: attempted static link of dynamic object b.so
```

会执行 COMDAT 解析，并且可能丢弃一些节，以及相对于这些节定义的符号。

启用 FatLTO 时，非 LTO 的可重定位链接应移除 `.llvm.lto` 节，因为默认拼接的 `.llvm.lto` 节无法反映链接语义。

### 符号解析

链接器不会对符号版本控制做特殊处理。符号名中的 `@` 和 `@@` 保持原样。

链接器不会定义保留符号（例如 `__ehdr_start, _GLOBAL_OFFSET_TABLE_`），也不会为名称是 C 标识符的节定义封装符号（`__start_$section, _stop_$section`）。

使用 LTO 时，LTO 假定所有非局部符号都可能被使用，避免消除它们。

### 创建合成节

链接器不会创建合成节（`.interp, .gnu.hash, .rela.dyn, .got, .plt, .comment` 等）。

### 将输入节和合成节映射到输出节

GNU ld 会抑制内部链接器脚本。因此不会有将 `.text.*` 映射到 `.text`、将 `.data.*` 映射到 `.data` 等默认映射。

可以编写链接器脚本来映射节。

在 GNU ld 中，`link_info.resolve_section_groups` 默认对可重定位链接关闭。这意味着：

- 带有 `SHF_GROUP` 标志的节会像匹配 `--unique=pattern` 选项的节一样处理。它们按孤立节处理，并忽略输入节描述。
- 节组（通常名为 `.group`）的内容会随节索引更新而更新。可使用 `/DISCARD/ : { *(.group) }` 丢弃节组。

`-r --force-group-allocation` 会改变这种行为：

- 节组会被丢弃。
- 带有 `SHF_GROUP` 标志的输入节会像普通节一样匹配。

在下例中，`a.o` 包含两个节组。

```sh
cat > a.cc <<eof
extern int x;
inline int inline0() { return x; }
inline int inline1() { return x+1; }
int use() { return inline0() + inline1(); }
eof
echo 'SECTIONS { .text1 : { *(.text .text.*) }}' > a.t
clang -c a.cc
ld.bfd -r -T a.t a.o -o bfd.ro
ld.bfd -r -T --force-group-allocation a.t a.o -o bfd.force.ro
ld.lld -r -T a.t a.o -o lld.ro
ld.lld -r -T --force-group-allocation a.t a.o -o lld.force.ro  # https://github.com/llvm/llvm-project/pull/94704 (milestone: lld 19)
```

`.text._Z7inline0v` 在 `bfd.ro` 中被视为孤立节。在 `lld.ro` 中同样被视为孤立节，而在另外三个输出文件中被视为普通节。

在 `lld.ro` 中，两个节组都包含 `.text1`，这违反 ELF 规范。`llvm-readelf -g lld.ro` 报告：

```plaintext
COMDAT group section [    3] `.group' [_Z7inline0v] contains 1 sections:
   [Index]    Name
   [    1]   .text1

COMDAT group section [    4] `.group' [_Z7inline1v] contains 1 sections:
   [Index]    Name
llvm-readelf: warning: 'lld.ro': section with index 1, included in the group section with index 3, was also found in the group section with index 4
   [    1]   .text1
```

同名且链接到不同输入节的 `SHF_LINK_ORDER` 节不能合并。([https://reviews.llvm.org/D68094](https://reviews.llvm.org/D68094))

### 扫描重定位

跳过这个阶段。链接器不会确定是否需要 GOT/PLT/TLSDESC/TLSGD 等。

### 布局并分配地址

输出节只会得到零地址。

### 写入头部

会照常创建 ELF 头和节头表，不会创建程序头。

### 符号表

符号通常会被拼接，不过需要合并 `STT_SECTION` 符号。

与可执行文件或共享对象链接不同，可重定位目标文件中具有 `STV_HIDDEN` 可见性的符号不会转换为 `STB_LOCAL` 绑定。

### 将节内容复制到输出并解析重定位

链接器会把相对于输入节的重定位转换为相对于输出节的重定位。这与 `--emit-relocs` 类似。附加数可能改变，隐式附加数可能导致节内容变化。

某些节可能被丢弃。对于非 `SHF_ALLOC` 节，ld.lld 会对引用相对于已丢弃节定义的符号的重定位应用墓碑值。

注意，只有有限类型的重定位能在可重定位文件中解析。具体来说，这适用于遵循 (S-P+A) 公式的重定位：S 是与 P 位于同一节的非 ifunc 局部符号。该行为与[汇编器修补解析](https://maskray.me/blog/2025-03-16-relocation-generation-in-assemblers)一致：

> 修补解析取决于修补类型：
>  
> - 描述符号本身的 PC 相对修补（重定位运算形如 S - P + A）中，若 sym_a 是在当前节中定义的非 ifunc 局部符号，则解析为常量。
> - `relocation_specifier(S + A)` 形式的修补在 S 指向绝对符号时解析。
> - 其他修补，包括 TLS 和 GOT 相关修补，仍不解析。

许多情形会阻止重定位解析：

- 跨节符号引用
- 带有 STB_WEAK 或 STB_GLOBAL 绑定的符号（因为共享库中的潜在符号插桩和链接器脚本符号赋值）
- TLS 或 GOT 相关重定位，以及可能需要 PLT 条目的重定位
- 可能需要范围扩展跳板或链接器松弛的重定位

链接器实现 `-r` 时通常只是保留全部重定位。

不会分配 COMMON 符号。

对于前面提及的主要阶段，可重定位链接似乎跳过了大多数阶段。不过，可重定位链接也与常规链接模式（`-no-pie, -pie, -shared`）共享大量次要特性：`--wrap, --compress-debug-sections, --build-id, -Map` 等。

链接器实现可以用单独文件描述可重定位链接的阶段，但很容易遗漏这些杂项特性。

## 垃圾回收

输出会合并节，相比使用所有输入文件会丧失粒度，因此最终链接的垃圾回收效果会更差。

可同时使用 `-r --gc-sections`。我在 [https://reviews.llvm.org/D84131](https://reviews.llvm.org/D84131) 中为 ld.lld 添加了支持。可重定位链接不会设置默认入口符号（通常是 `_start`）。使用 `-r --gc-sections` 时，应设置 GC 根（`--entry` 和 `-u`）。

## 可重定位链接步骤造成的输出差异

下面两种链接可能生成不同的输出。1  
2  
3  
4  
clang -pie a.o b.o -lz -ltinfo  
  
clang -r a.o b.o -o r.o  
clang -pie r.o -lz -ltinfo

假设两个可重定位目标文件都定义 `.rodata._ZL7indent8` 和 `.rodata._ZL7indent16`。（这些节名由 `-fdata-sections` 造成。）在第一种链接中，四个输入节按以下顺序合并：`a.o:.rodata._ZL7indent8, a.o:.rodata._ZL7indent16, b.o:.rodata._ZL7indent8, b.o:.rodata._ZL7indent16`。在第二种链接中，可重定位链接会合并 `a.o:.rodata._ZL7indent8` 和 `b.o:.rodata._ZL7indent8`（`.rodata._ZL7indent8` 也同理），因此最终顺序看起来被打乱。

这种分组效果可能因对齐填充而影响输出节大小。

## 应用

### 静态库的替代方案

节和符号的总数更少，使可重定位文件小于输入文件的总大小。代价是垃圾回收效果较差，因此可重定位链接可作为静态库的替代方案。

### glibc

glibc 提供许多 crt1 文件：`Scrt1.o, rcrt1.o, crt1.o, grcrt1.o, gcrt1.o`。这些文件共享大量通用代码，但各有定制。glibc 使用可重定位链接创建这些文件，例如：

- `Scrt1.o` 是 `csu/start.os`、`csu/abi-note.o` 和 `csu/init.o` 的可重定位链接输出。
- `crt1.o` 是 `csu/start.o`、`csu/abi-note.o` 和 `csu/init.o` 的可重定位链接输出。

`elf/Makefile` 会执行以下步骤来构建 `elf/ld.so`：

- 从 libc 的 `.os` 文件创建 `elf/libc_pic.a`
- 从 rtld `.os` 文件的可重定位链接创建 `elf/dl-allobjs.os`
- 从 `elf/dl-allobjs.os`、`elf/libc_pic.a` 和 `-lgcc` 的可重定位链接创建链接映射 `elf/librtld.map`
- 从 `elf/librtld.map` 获取已提取归档成员列表（`elf/librtld.mk`），并创建 `elf/rtld-libc.a`
- 从 `elf/dl-allobjs.os` 和 `elf/rtld-libc.a` 的可重定位链接创建 `elf/librtld.os`
- 通过 `elf/librtld.os` 的 `-shared` 链接及版本脚本 `ld.map` 创建 `elf/ld.so`

这里使用可重定位链接进行符号解析：确定哪些 libc 组件需要进入 `elf/ld.so`。版本脚本 `ld.map` 用于将 libc 符号本地化。

### grub

`grub-core/genmod.sh.in` 使用可重定位链接生成模块（例如 `grub-core/reboot.module`）。`grub-core/gensyminfo.sh.in` 将符号转储到 `grub-core/syminfo.lst`，之后用它生成模块依赖列表。

### Linux 内核

`tools/objtool/objtool-in.o` 是链接到 `tools/objtool/objtool` 的可重定位输出。我不知道为何需要这一步。

`vmlinux.o` 是用于分析的可重定位输出（参见 `scripts/Makefile.vmlinux_o`）。

- 供模块使用
- objtool 使用 `vmlinux.o` 执行“noinstr”（无插桩）验证。

```sh
ld.lld -m elf_x86_64 -z noexecstack -r -o vmlinux.o  --whole-archive vmlinux.a --no-whole-archive --start-group  --end-group
llvm-objcopy  -j .modinfo -O binary vmlinux.o modules.builtin.modinfo
tr '\0' '\n' < modules.builtin.modinfo | sed -n 's/^[[:alnum:]:_]*\.file=//p' | tr ' ' '\n' | uniq | sed -e 's:^:kernel/:' -e 's/$/.ko/' > modules.builti
```

内核模块（`.ko` 文件）由 `ld -r` 和 `modpost` 创建。

不出所料，ClangBuiltLinux 项目的贡献者发现了 ld.lld 一些有趣的边缘情况。我认为大多数问题在 2019 年由我报告并修复。

### Sanitizer 内部符号化器

Sanitizer 可以使用外部工具 `llvm-symbolizer` 或内部符号化器进行符号化。

内部符号化器使用脚本 [`compiler-rt/lib/sanitizer_common/symbolizer/scripts/build_symbolizer.sh`](https://github.com/llvm/llvm-project/blob/main/compiler-rt/lib/sanitizer_common/symbolizer/scripts/build_symbolizer.sh)。

- 使用 `-flto` 构建一部分 LLVM。
- 调用 `llvm-link` 链接 LLVM bitcode 文件。
- 使用 `opt -internalize -internalize-public-api-list=$list` 将大多数符号内部化。只有 `__sanitizer_symbolize_*` 保持全局符号。
- 将 bitcode 编译为 `symbolizer.o`。
- 将 `symbolizer.o` 注入 `libclang_rt*san*.a` 归档。

使用 `llvm-link` 编译 bitcode 是可重定位链接的一种替代方案。

构建出的运行时库将由用户程序使用。`clang -fsanitize=address` 以 `--whole-archive` 模式链接 `libclang_rt.asan.a`，因此输出会链接带有内部符号化器功能的 `symbolizer.o`。输出也可能使用 LLVM，而链接的 LLVM 版本可能不同。`symbolizer.o` 的内部化避免了符号冲突。

### 符号本地化

上一节提到过 `llvm-link` 技巧。使用可重定位链接也能达到相同效果。可重定位链接后，使用 `objcopy --keep-global-symbol` 保留少数入口符号，并将其余符号本地化。输出可作为单个 `.o` 文件或归档文件的一部分分发。

`llvm-link` 方法和可重定位链接方法都需要格外注意处理 COMDAT 组。参见[COMDAT 与节组#GRP_COMDAT](https://maskray.me/blog/2021-07-25-comdat-and-section-group#grp_comdat)，了解为何应让所有 COMDAT 组签名保持全局，以避免陷阱。

步骤如下：

- 默认以隐藏符号编译（对定义使用 `-fvisibility=hidden`，或对定义和引用都使用 `#pragma GCC visibility("hidden")`）。将必要符号标记为导出。
- 运行 `ld -r --force-group-allocation`。可选地指定 `--unique=*` 以保留节粒度。
- 使用可能带有其他选项的 `objcopy --localize-hidden` 处理输出。

### 查找更多使用可重定位链接的项目

许多项目的构建系统很复杂，很难知道是否使用 `-r`。我使用 ld 包装器 `/usr/local/bin/ld` 来获取链接器命令行：1  
2  
3  
4  
5  
6  
7  
8  
#!/bin/zsh  
for i in "$@"; do  
 if [[ $i == -r ]]; then  
 echo "$@" \>\> /tmp/link.log  
 break  
 fi  
done  
LD_PRELOAD=path/to/libmimalloc.so ~/Stable/bin/ld.lld --threads=8 "$@"

## Mach-O

Apple ld 也支持 `-r`，它会生成类型为 `MH_OBJECT` 的目标文件。该特性有时称为“单目标预链接”。

你可以指定 `-exported_symbol` 或 `-exported_symbols_list` 将符号设为私有。

```plaintext
printf 'void foo(){} void bar(){}' | clang -c -xc - -o a.o
ld -arch arm64 -r -exported_symbol bar a.o
ld -arch arm64 -r -exported_symbols_list a.txt a.o
```
