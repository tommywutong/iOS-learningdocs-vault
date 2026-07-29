---
title: 链接器笔记：PE/COFF
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2023-12-03-linker-notes-on-pe-coff'
original_language: en
published: 2023-12-03
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:027071583e044a64'
translated: true
---

> 原文：[Linker notes on PE/COFF](https://maskray.me/blog/2023-12-03-linker-notes-on-pe-coff)　·　MaskRay (宋方睿)

[2023-12-03](https://maskray.me/blog/2023-12-03-linker-notes-on-pe-coff)

# 链接器笔记：PE/COFF

更新于 2025-05。

本文介绍了关于 Windows 和 UEFI 环境中使用的可移植可执行（Portable Executable，PE）和通用对象文件格式（Common Object File Format，COFF）的链接器笔记。

在 ELF 中，目标文件（object file）可以是可重定位文件（relocatable file）、可执行文件（executable file）或共享对象文件（shared object file）。在 Windows 上，术语“目标文件”通常指类似 ELF 中的可重定位文件。此类文件使用通用对象文件格式（COFF），而映像文件（image file，例如可执行文件和 DLL）使用可移植可执行（PE）格式。

## 链接器一览

MSVC 链接器是 Windows 上的参考链接器。

得益于 MinGW 的努力，GNU ld 支持 Windows。以下是一些用于 PE 目标的常见 BFD 仿真：

- `i386pe`：适用于 32 位 Intel x86 架构。
- `i386pep`：适用于 64 位 Intel x86-64 架构。
- `arm64pe`：适用于 64 位 ARM（AArch64）架构。

例如，你可以使用类似 `ld.bfd -m i386pep a.o b.o` 的命令将两个目标文件链接成一个 PE 可执行文件。许多 Linux 上的选项在面向 PE/COFF 时也可以使用。

LLVM 链接器提供两种与 PE/COFF 相关的操作模式：

- `lld-link`：在此模式下，lld 模拟 MSVC 链接器，成为一个快速可行的替代方案。
- `ld.lld`：当使用 PE 仿真（如 `-m i386pep`）调用时，lld 模拟 GNU ld。`lld/MinGW` 中的代码将 GNU ld 选项转换为 link.exe 选项。

GNU ld 实现了其他链接器不具备的[可重定位链接](https://maskray.me/blog/2022-11-21-relocatable-linking)。

## 输入文件

链接器的输入文件可以是目标文件、归档文件（archive file）和导入库（import library）。GNU ld 和 lld-link 允许在无需导入库的情况下链接 DLL 文件。

### 目标文件

### 导入文件

导入文件（import file，`.lib`）是一种特殊的归档文件（archive file）。每个成员代表一个待导入的符号。符号 `__imp_$sym` 会被插入到全局符号表中。

导入头部有一个 `Type` 字段，表示 `IMPORT_OBJECT_CODE/IMPORT_OBJECT_DATA/IMPORT_OBJECT_CONST`。

对于 `IMPORT_OBJECT_DATA` 类型的导入，符号 `$sym` 被定义为 `__imp_$sym` 的别名。

对于 `IMPORT_OBJECT_CODE` 类型的导入，符号 `$sym` 被定义为一个导入 thunk，它类似于 ELF 中的 PLT 条目。

GNU ld 和 lld-link 允许在无需导入库的情况下链接 DLL 文件。其行为类似于链接器从 DLL 文件合成一个导入库。

## 符号

目标文件提供已定义符号和未定义符号。导入文件提供 DLL 中定义的符号，这些符号可以通过 `__imp_$sym` 引用。

已定义的符号可以是以下几种类型之一：

- 特殊符号（在全局符号表中被忽略）
- 公共符号（节编号为 `IMAGE_SYM_UNDEFINED` 且值不为 0）
- 绝对符号（节编号为 -1）
- 常规符号（节编号为正数）

未定义符号的存储类为 `IMAGE_SYM_CLASS_EXTERNAL`，节编号为 `IMAGE_SYM_UNDEFINED`（零），值为零。

存储类为 `IMAGE_SYM_CLASS_WEAK_EXTERNAL` 的未定义符号是一个弱外部符号。它后面跟着一个辅助记录：

- 当 `Characteristics` 为 `IMAGE_WEAK_EXTERN_SEARCH_ALIAS` 时，弱外部符号的行为类似于 ELF 中的弱定义。
- （ARM64EC 特有）当 `Characteristics` 为 `IMAGE_WEAK_EXTERN_SEARCH_ANTI_DEPENDENCY` 时，弱外部符号是一个反依赖别名。

PE 要求对 DLL 文件中的导出符号和导入符号进行显式注解。代码符号和函数符号之间存在差异。

### COMDAT

请参考 [COMDAT and section group](https://maskray.me/blog/2021-07-25-comdat-and-section-group)。

### 导出符号

链接器构建 `.edata`。规范说明：

> 导出数据节，名为 `.edata`，包含其他映像可以通过动态链接访问的符号信息。导出符号通常出现在 DLL 中，但 DLL 也可以导入符号。

### 导入的代码符号

```c
// b.dll
__declspec(dllexport) void f() {}

// a.exe
void local(void) {}
void __declspec(dllimport) f(void);
int main(void) {
  local();
  f();
}
```

链接 `b.dll` 会生成 `b.lib`（参见上文的“导入文件”）。  1  
2  
3  
4  
5  
6  
# b.dll  
.globl f  
f:  
  
.section .drectve,"yni"  
.ascii " -export:f"

`a.obj` 有两个函数调用。对 `f` 的调用引用了带前缀的符号 `__imp_f`。  1  
2  
3  
# a.obj  
 callq local  
 callq *__imp_f(%rip)

`call *__imp_f(%rip)` 类似于 ELF 中 `-fno-plt` 的代码生成。在这种情况下，当我们知道 `f` 是在其他地方定义时，生成的代码效率更高。

链接 `a.exe` 时，我们需要将导入文件 `b.lib` 作为输入文件。链接器解析导入文件，并为 `__imp_f` 创建一个指向导入地址表条目的定义。

TODO 导入表

实际上，当 `__imp_f` 已被定义时，不带前缀的符号 `f` 也会被定义。通常，不带前缀的 `f` 不会被使用，将被丢弃。然而，如果用户代码调用不带前缀的符号（例如 `call f`；类似于 ELF `-fplt`），`f` 的定义将保留在链接器输出中，并指向一个 thunk：  1  
2  
3  
4  
 call f # 生成的代码未使用 dllimport  
  
f: # x86-64 thunk  
 jmpq *__imp_f(%rip)

不同架构有不同的 thunk 实现。  1  
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
// x86-32 and x86-64  
jmp *0x0 // 引用导入地址表中的条目  
  
// AArch32  
mov.w ip, #0  
mov.t ip, #0  
ldr.w pc, [ip]  
  
// AArch64  
adrp x16, #0  
ldr x16, [x16]  
br x16

TODO link.exe 会发出警告。

MSVC 支持一个未公开（截至 2025 年 5 月）的选项 `/d2ImportCallOptimization`，该选项将间接调用偏移量记录到 `.impcall` 节中（[https://github.com/llvm/llvm-project/pull/121516](https://github.com/llvm/llvm-project/pull/121516)）。Windows 内核加载器会将间接调用重写为直接调用。

### 导入的数据符号

```c
// b.dll
__declspec(dllexport) int var;

// a.exe
int local_var;
__declspec(dllimport) extern int var;
int main() { return local_var + var;  }
```

```plaintext
# b.dll
.bss
.globl var
var:

.section        .drectve,"yni"
.ascii  " -export:var,data"
```

链接器解析导入文件，并为 `__imp_var` 创建一个指向导入地址表条目的定义。与代码符号不同，链接器不会为 `var`（不带 `__imp_` 前缀）创建定义。

使用 `dllimport` 时：  1  
2  
movq __imp_var(%rip), %rax  
movl (%rax), %eax

如果未指定 `dllimport`，我们会得到一个指向不带前缀符号的引用：  1  
movq var(%rip), %rax

link.exe 会报告一个错误。

MinGW 实现了运行时伪重定位来修补代码节，以便指向该符号的绝对指针和相对偏移量将被重写以绑定到实际定义。  1  
movq var(%rip), %rax # 运行时将重写此指令以指向 b.dll 中的定义

如果变量定义在当前位置的 +-2GiB 范围之外，则运行时伪重定位无法解决问题。请参阅 [crt: Check pseudo relocations for overflows and error out clearly](https://github.com/mingw-w64/mingw-w64/commit/ca35236d9799af8a3d2f9baa35b60e6c11abeb24)。

对于非定义声明，GCC 会保守地认为该变量可能在 DLL 中定义，并生成间接访问。这类似于 ELF 中的 GOT 代码序列。  1  
2  
extern int extern_var;  
int main() { return extern_var; }

```plaintext
// MSVC
  movl    extern_var(%rip), %eax

// GCC
  movq    .refptr.extern_var(%rip), %rax
  movl    (%rax), %eax

  .section        .rdata$.refptr.extern_var,"dr",discard,.refptr.extern_var
  .p2align        3, 0x0
  .globl  .refptr.extern_var
.refptr.extern_var:
  .quad   extern_var
```

## 非 dllexport 定义与 dllimport

目标文件引用的 `dllimport` 符号通常由导入文件满足。link.exe 允许另一个目标文件提供该定义。在这种情况下，link.exe 会发出警告（[链接器工具警告 LNK4217](https://learn.microsoft.com/en-us/cpp/error-messages/tool-errors/linker-tools-warning-lnk4217)）。lld-link 已实现此功能以保持兼容性。

```sh
echo '__declspec(dllimport) int foo(); int main() { return foo(); }' > a.cc
echo 'int foo() { return 42; }' > b.cc
clang-cl -c a.cc b.cc
lld-link -nodefaultlib -entry:main a.obj b.obj
```

```plaintext
lld-link: warning: a.obj: locally defined symbol imported: int __cdecl foo(void) (defined in b.obj) [LNK4217]
```

## MinGW

MinGW 提供了自动导出和自动导入特性，使 PE DLL 文件能够像 ELF 共享对象一样工作。生成 DLL 文件时，如果没有选择任何符号进行导出，默认会导出几乎所有符号（`--export-all-symbols`）。

如果未定义的符号 `$sym` 无法解析，而 `__imp_$sym` 已定义，则 `$sym` 将被别名为 `__imp_$sym`。TODO：示例

如果存在符号 `.refptr.$sym`，它也将被别名为 `__imp_$sym`。mingw-w64 默认使用 `-mcmodel=medium` 并生成 `.refptr.$sym`。TODO：示例

https://github.com/ziglang/zig/issues/9845

## 手动定义 `__imp_`

用户可以定义 `__imp_`，而不是让链接器来做。

https://github.com/llvm/llvm-project/issues/57982  1  
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
$ cat lto-dllimp1.c  
void __declspec(dllimport) importedFunc(void);  
void other(void);  
  
void entry(void) {  
 importedFunc();  
 other();  
}  
$ cat lto-dllimp2.c  
static void importedFuncReplacement(void) {  
}  
void (*__imp_importedFunc)(void) = importedFuncReplacement;  
  
void other(void) {  
}

## 范围扩展 thunk

TODO

共享库的设计在 1988 年左右取得了重大进展。1988 年之前，a.out 和 COFF 目标文件格式中已有共享库的实现，但它们存在严重的局限性，例如固定地址以及需要导入文件等额外文件。

这些局限性在《1986 年夏季 USENIX 技术会议与展览论文集》中 AT&T 的《UNIX System V 上的共享库》一文中得到了证实。它的共享库（推测使用了 COFF 目标文件格式）必须有一个固定的虚拟地址，这在《链接器与加载器》的术语中称为“静态共享库”。

1988 年，SunOS 4.0 发布，它采用了一种扩展的 a.out 二进制格式，支持动态共享库。与之前的静态共享库方案不同，a.out 共享库是位置无关的，可以加载到不同的地址。动态链接器的源代码在某个地方可用，我发现其 GOT 和 PLT 方案与当今 ELF 的方案完全相同。

AT&T 和 Sun 合作创建了第一个 System V Release 4 ABI（使用 ELF）。AT&T 贡献了 ELF 目标格式。Sun 贡献了来自 SunOS 4.x 的所有动态链接实现。1992 年，SunOS 5.0（Solaris 2.0）切换到了 ELF。

对于 ELF，设计者试图使共享库类似于静态库。使用共享库无需注解导出和导入符号。

我找不到更多关于 System V Release 3 共享库支持的信息，但 Windows DLL 无疑受到了它的启发，因为 PE 目标文件格式基于 COFF，并且 PE 规范在许多地方都引用了 COFF。

那么，ELF 中的共享库设计是否更先进？是的。然而，有两个方面值得深入思考。

- 手动导出和导入注解有其优势。
- 为使 ELF 共享库灵活而做出的选择有重大缺点。

    - 由于编译器端的符号干预导致的性能下降。请参阅 [_-fno-semantic-interposition_](https://maskray.me/blog/2021-05-09-fno-semantic-interposition)
    - 由于链接器和加载器端的符号干预导致的性能下降。请参阅 [ELF interposition and -Bsymbolic](https://maskray.me/blog/2021-05-16-elf-interposition-and-bsymbolic)
    - 链接器默认 `-z undefs` 加剧了欠链接问题。请参阅 [Dependency related linker options](https://maskray.me/static/2021-06-13-dependency-related-linker-options)。

## 限制

符号数量不能超过 65535。几个开源项目曾面临 DLL 文件无法导出超过 65535 个符号的问题。（GNU ld 有诊断信息 `error: export ordinal too large:`）。

节头部只有 8 个字节用于名称字段。link.exe 会将长节名截断为 8 个字节。对于具有长名称和 `IMAGE_SCN_MEM_DISCARDABLE` 标志的节，lld 会使用非标准字符串表并发出警告。

COMDAT 限制：MSVC link.exe 会对定义在 `IMAGE_COMDAT_SELECT_ASSOCIATIVE` 节中的外部符号报告[重复符号错误](https://maskray.me/blog/2021-07-25-comdat-and-section-group)（错误 LNK2005），即使该符号在处理前导符号后会被丢弃。
