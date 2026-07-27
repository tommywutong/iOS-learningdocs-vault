---
title: 整数溢出
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/integer-overflow
source_url: 'https://developer.apple.com/documentation/xcode/integer-overflow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/integer-overflow.json'
content_hash: 'sha256:ebe8be07a4a7e4b3'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)

# 整数溢出

<sub>文章</sub>

检测运算中的溢出。

## 概述

溢出会导致未定义行为。使用此检查可检测加法、减法、乘法和除法中的溢出。适用于 Xcode 9 及以上版本。

### C 语言中的有符号加法溢出

在以下代码中，`x` 变量在加法运算前已达到 `int32_t` 的最大值，加法运算的结果导致 `x` 溢出，而优化器可能不会以可预测的方式处理这种情况：

```occ
int32_t x = (1U << 31) - 1;
x += 1; // Error: the add result can't fit in x
```

> [!note] 注意
> 除有符号除法检查外，启用 `-fwrapv` 编译器标志会禁用 UBSan 的溢出检查。

#### 解决方案

解决有符号溢出的一种方法是使用更大的类型。

如果你不需要表示负数，另一个选择是使用无符号类型，它会在算术溢出时环绕。或者，向编译器传入 `-fwrapv` 标志，以在溢出时启用有符号环绕。但这可能会对性能产生不利影响。

## 另请参阅

### Undefined Behavior Sanitizer

- [Misaligned pointer](misaligned-pointer.md) — 检测代码何时访问了未对齐的指针或创建了未对齐的引用。
- [Invalid Boolean value](invalid-boolean.md) — 检测程序何时访问了一个布尔变量，且其值既不是 true 也不是 false。
- [Out-of-bounds array access](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [Invalid enumeration value](invalid-enumeration-value.md) — 检测枚举变量何时具有无效值。
- [Reaching of unreachable point](reaching-of-unreachable-point.md) — 检测程序何时到达了一个不可达点。
- [Dynamic type violation](dynamic-type-violation.md) — 检测对象何时具有错误的动态类型。
- [Invalid float cast](invalid-float-cast.md) — 检测浮点类型之间、或与浮点类型互相转换时的越界转换。
- [Division by zero](division-by-zero.md) — 检测除数为零的除法运算。
- [Nonnull argument violation](nonnull-argument-violation.md) — 检测参数何时错误地接收到空值。
- [Nonnull return value violation](nonnull-return-value-violation.md) — 检测函数何时错误地返回空值。
- [Nonnull variable assignment violation](nonnull-variable-assignment-violation.md) — 检测你何时错误地将空值赋给一个变量。
- [Null reference creation and null pointer dereference](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建以及空指针的解引用。
- [Invalid object size](invalid-object-size.md) — 检测因类型大小不同而导致的无效指针转换。
- [Invalid shift](invalid-shift.md) — 检测无效及溢出的移位操作。
- [Invalid variable-length array](invalid-variable-length-array.md) — 检测负数的数组边界。
</content>
