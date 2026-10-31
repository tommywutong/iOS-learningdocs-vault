---
title: 验证数学计算
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/verifying-mathematical-calculations
source_url: 'https://developer.apple.com/documentation/uikit/verifying-mathematical-calculations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/verifying-mathematical-calculations.json'
content_hash: 'sha256:dd12d32a94294e4b'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Updating your app from 32-bit to 64-bit architecture](updating-your-app-from-32-bit-to-64-bit-architecture.md)

# 验证数学计算

<sub>文章</sub>

确保你的数学运算在 64 位架构下的准确性。

## 概述

数学运算会受到 64 位运行时中的数值影响。请检查你的 App 执行的任何计算结果的准确性。检查有符号值的结果，确保它们对其运算和操作数来说是正确的。验证你的位掩码代码没有对类型大小做假设。

### 验证有符号数学运算的准确性

C 及类似语言使用一组 _符号扩展规则_ 来决定当值被赋给更宽的变量时，是否把整数的最高位当作符号位。符号扩展规则如下：

1. 无符号值在提升为更大型别时会被零扩展（而非符号扩展）。
2. 有符号值在提升为更大型别时总是会被符号扩展，即使结果类型是无符号类型。
3. 常量（除非被后缀修改，如 `0x8L`）被当作能容纳该值的最小尺寸。十六进制数可能被编译器当作 `int`、`long` 和 `long long` 类型，并且可能是 `signed` 或 `unsigned` 类型。十进制数总是被当作 `signed` 类型。
4. 同样大小的有符号值与无符号值之和是无符号值。

```objc
int a = -2;
unsigned int b = 1;
long c = a + b;
long long d = c; // To get a consistent size for printing.

printf("%lld\n", d);
```

这段代码在 32 位运行时执行时，结果是 -1（`0xffffffff`）。在 64 位运行时运行相同代码时，结果是 4294967295（`0x00000000ffffffff`），这是不正确的。

要理解为什么会发生这种情况，考虑这些数相加时，有符号值加无符号值的结果是无符号值（规则 4）。该结果被提升为更大型别，但这种提升不会导致符号扩展。

要修复此问题，把 `b` 转换为 `long` 整数。这个转换在加法运算之前把 `b` 强制提升为 64 位类型且不进行符号扩展，从而强制有符号整数（以有符号方式）提升以匹配。做出这一改动后，结果就是预期的 -1。

```objc
unsigned short a = 1;
unsigned long b = (a << 31);
unsigned long long c = b;

printf("%llx\n", c);
```

在上面的代码中，位移用于把 `a` 的值移动到 `b` 中的不同位置，然后复制到 `c`。`printf` 的预期结果（以及 32 位可执行文件的结果）是 `0x80000000`。然而 64 位可执行文件生成的结果是 `0xffffffff80000000`。

这个结果有两个原因。第一，调用左移运算符 `<<` 时，变量 `a` 被提升为 `int` 类型的变量。因为 `short` 整数的所有值都可以装入有符号 `int` 类型，这次提升的结果是有符号的。第二，左移完成后，结果被存储在一个 `long` 整数中。因此，`(a << 31)` 所表示的 32 位有符号值在提升为 64 位值时会被符号扩展（规则 2），即使结果类型是无符号的。

解决方案是在移位之前把初始值转换为 `long` 整数。`short` 整数只提升一次——这次是提升为 64 位类型（在编译为 64 位可执行文件时）。

### 检查代码对类型大小的假设

在使用 64 位值的位掩码时，遵循以下提示以避免无意得到 32 位值。

**不要假设数据类型具有特定长度。** 如果你正在移位存储在 `long` 整数类型变量中的位，请使用 `LONG_BIT` 值来确定位数。超过变量长度的移位结果取决于架构。

**必要时使用反向位掩码。** 使用长整数的位掩码时要小心，因为其宽度在 32 位与 64 位运行时之间不同。根据你希望它被零扩展还是被一扩展，有两种创建位掩码的方式：

- 如果你希望位掩码值在 64 位运行时的高 32 位包含零，通常的固定宽度位掩码按预期工作，因为它以无符号方式扩展为 64 位数量。
- 如果你希望位掩码值的高位包含一，请把位掩码写成其反码的按位取反。

```objc
long function_name(long value)
{
    // Use the complement (~) operator to get ones instead of zeros.
    // Mask will be 0xfffffffc in the 32-bit runtime,
    //   or 0xfffffffffffffffc in the 64-bit runtime.
    long mask = ~0x3;
    return (value & mask);
}
```

注意，在 64 位运行时，位掩码中的高位全部为一。

## 另请参阅

### 性能与准确性

- [Optimizing memory performance](optimizing-memory-performance.md) — 测量 64 位运行时对你的 App 内存使用的影响。
