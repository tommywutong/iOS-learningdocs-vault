---
title: 为 Apple 平台编写 64 位 Intel 代码
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/writing-64-bit-intel-code-for-apple-platforms
source_url: 'https://developer.apple.com/documentation/xcode/writing-64-bit-intel-code-for-apple-platforms'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/writing-64-bit-intel-code-for-apple-platforms.json'
content_hash: 'sha256:6c26fe19ab4a67d7'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [应用程序二进制接口](application-binary-interfaces.md)

# 为 Apple 平台编写 64 位 Intel 代码

<sub>文章</sub>

创建符合 Apple 平台所支持应用程序二进制接口（ABI）的 64 位 Intel 汇编语言指令。

## 概述

在 Apple 芯片推出之前，Mac 使用 Intel 64 位架构，这种架构通常称为 x86-64、x86_64、AMD64 或 x64。macOS 平台针对该架构的应用程序二进制接口（ABI）定义了函数调用、栈管理以及执行其他操作的规则。如果代码包含汇编指令，你必须遵守这些规则，代码才能与 Xcode 中编译器生成的代码正确交互。同样，如果你编写编译器，所生成的机器指令也必须遵守这些规则。若不遵守，代码可能出现意外行为甚至崩溃；在某个操作系统版本上看似正常工作的代码，也可能在下一版本中停止工作。

> [!note] 注意
> 自 macOS Catalina 起，Apple 不再支持任何基于 32 位 Intel 的平台。

Apple 平台通常采用标准 [AMD64 System V psABI](https://gitlab.com/x86-psABIs/x86-64-ABI) 中的数据表示和过程调用规则，并使用 LP64 编程模型。不过，如果这些规则与 Apple LLVM 编译器（Clang）在 Apple 平台上的长期行为冲突，ABI 通常会偏离标准的处理器特定应用程序二进制接口（psABI），转而遵循既有行为。下文列出了若干此类差异。如果发现本文未说明的差异，请[向 Apple 报告](https://developer.apple.com/bug-reporting/)。

### 遵守 CPU 功能的可用性

Intel 64 位架构经过多次扩展，为指令集架构（ISA）添加了新的寄存器和指令。你可以利用 ISA 扩展提高代码的运行效率。根据 Mac 所使用的处理器，不同 Mac 可用的 ISA 扩展也有所不同。一般来说，如果代码在不支持某项 ISA 扩展的处理器上使用该扩展，处理器会崩溃。

强烈建议你编写的 App 不要设置比指定最低操作系统版本更复杂的安装要求，其中也包括要求特定的一组处理器扩展才能运行 App。某些 macOS 版本只支持提供特定 ISA 扩展的 Mac，因此能够保证这些扩展存在。如果你希望使用某项 ISA 扩展，但 App 的最低 macOS 部署 target 并不保证其存在，请使用 CPUID 指令动态检测该扩展，并在其不可用时准备回退到另一种实现。

下表汇总了不同 macOS 版本所保证的 ISA 扩展：

| macOS 版本 | 支持的最旧处理器 | 可用的 CPU 功能 |
|---|---|---|
| 所有版本 | [Merom](<https://en.wikipedia.org/wiki/Merom_(microprocessor)>) | x86-64 基线，以及 CMPXCHG16B、LAHF-SAHF、SSE3、SSSE3 |
| Sierra（10.12） | [Penryn](<https://en.wikipedia.org/wiki/Penryn_(microprocessor)>) | 上述功能，以及 SSE4.1 |

较新的 64 位 Intel Mac 还包含大量其他 ISA 扩展，但任何 macOS 版本都不保证这些扩展存在，因此你需要对其进行动态检测。

Rosetta 对 64 位 Intel 处理器的支持包括上述全部 ISA 扩展，以及 POPCNT 和 SSE4.2 ISA 扩展。

### 按照 CPU 寄存器的预定用途使用寄存器

普通函数的寄存器用法遵循标准 psABI。

调用 C++ `thread_local` 变量的初始化函数（通常以 `_ZTH` 和 `_ZTW` 开头）时，除了标准 psABI 指定的寄存器外，还会将 `rcx`、`rdx`、`rsi`、`r8`、`r9`、`r10` 和 `r11` 视为被调用者保存寄存器。

根据 Swift 函数的签名以及它是同步函数还是异步函数，Swift 调用约定会使用若干在标准 psABI 中没有特殊含义的寄存器。

同步函数分为三种情况：

- **间接返回值** — 第一个间接返回地址通过 `rax` 传递。其他间接返回地址作为位于所有其他参数之前的普通参数传递；例如，第二个地址位于 `rdi`，第三个位于 `rsi`，依此类推。
- **可装入单个整数寄存器的上下文参数** — 闭包和类方法即属此类。函数通过 `r13` 接收此上下文。此类调用会保留 `r13`；调用结束后，`r13` 必须保存调用者传入的相同值。
- **抛出 `Error`** — 这些函数为此使用 `r12`。调用者必须在调用前将 `r12` 设为零；如果返回后 `r12` 非零，则函数正在抛出错误，而 `r12` 中的值就是该错误。对于此类调用，`r12` 不再是被调用者保存寄存器。

异步 Swift 函数通过 `r14` 接收其异步帧的地址。对于此类调用，`r14` 不再是被调用者保存寄存器。

### 正确处理数据类型和数据对齐

数据类型表示方式大体遵循标准 psABI。不过，Apple LLVM 编译器支持若干 psABI 未涵盖的类型；这些类型的规则说明如下。

- Apple LLVM 编译器允许向量具有任意数量的元素。向量类型的存储大小（以字节为单位）始终向上舍入到最接近的 2 的幂。其对齐值等于存储大小，但上限为当前 target CPU 功能决定的最大原生向量大小：启用 AVX-512 时为 64 字节，否则启用 AVX 时为 32 字节，否则为 16 字节。请注意，这意味着大型向量类型的 ABI 取决于 target CPU 功能，使用不同 CPU 功能编译的文件之间可能无法互操作；这一行为继承自标准 psABI。
- Objective-C ARC 中带 `__strong` 和 `__weak` 限定符的指针类型，与非 ARC Objective-C 中的底层引用类型（reference type）具有相同布局。不过，包含 `__strong` 和 `__weak` 限定字段的结构体具有非平凡所有权；当调用者将它们作为参数传递时，被调用者负责销毁这些字段。此外，与不可平凡复制的 C++ 类类型一样，你必须间接传递和返回包含 `__weak` 限定字段的结构体。

### 正确地向函数传递参数

向函数传递参数和从函数返回结果时，Apple 平台在以下方面与标准 psABI 不同：

- 小于 `int` 的整数参数必须由调用者提升为 `int`，被调用者可以假定调用者已完成此操作。（这包括底层类型小于 `int` 的枚举。）例如，如果调用者通过寄存器传递 `signed short` 参数，则调用时寄存器的低 32 位必须表示 -32,768 到 32,767（含）之间的值。同样，如果调用者通过寄存器传递 `unsigned char` 参数，则调用时寄存器的低 32 位必须表示 0 到 255（含）之间的值。此规则也适用于返回值和通过栈传递的参数。
- 分类算法将小于 8 字节的向量视为 `INTEGER` 类。由 `double` 组成的 8 字节向量归类为 `MEMORY`。元素类型为 64 位整数的 8 字节向量归类为 `INTEGER`。其他 8 字节向量归类为 `SSE`。
- 对于大于 8 字节的向量，分类算法使用标准 psABI 中的规则，包括将大于最大原生向量大小的向量归类为 `MEMORY` 的规则。与数据布局一样，这意味着大于 16 字节的向量类型所采用的调用约定取决于当前 target CPU 功能，使用不同 CPU 功能编译的文件之间可能无法互操作。
- 分类算法不执行合并后清理的步骤 (b)。而是在其他分类全部完成后（而非递归分类过程中），当 `X87UP` 不跟在 `X87` 之后时，将其转换为 `SSE`。例如：

  ```
  typedef union { long double d; void *p; } odd_union;
  void f(odd_union u);
  ```

  调用者通过 `rdi` 传递 `u` 的前 8 个字节，并通过 `xmm0` 的低位传递后 8 个字节（即 `u.d` 的指数位）。

psABI 规则仅适用于 C、C++ 和 Objective-C 调用。除上述寄存器用法差异外，Swift 调用约定在许多方面都与 psABI 有显著差异，其说明超出了本文范围。

## 另请参阅

### 64 位接口

- [为 Apple 平台编写 ARM64 代码](writing-arm64-code-for-apple-platforms.md) — 创建符合 Apple 平台所支持应用程序二进制接口（ABI）的 64 位 ARM 汇编语言指令。
