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
x += 1; // 错误：加法结果无法存入 x
```

> [!note] 注意
> 除有符号除法检查外，启用 `-fwrapv` 编译器标志会禁用 UBSan 的溢出检查。

#### 解决方案

解决有符号溢出的一种方法是使用更大的类型。

如果你不需要表示负数，另一个选择是使用无符号类型，它会在算术溢出时环绕。或者，向编译器传入 `-fwrapv` 标志，以在溢出时启用有符号环绕。但这可能会对性能产生不利影响。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐的指针](misaligned-pointer.md) — 检测代码何时访问了未对齐的指针或创建了未对齐的引用。
- [无效的布尔值](invalid-boolean.md) — 检测程序何时访问了一个布尔变量，且其值既不是 true 也不是 false。
- [数组的越界访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [无效的枚举值](invalid-enumeration-value.md) — 检测枚举变量何时具有无效值。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序何时到达了一个不可达点。
- [动态类型冲突](dynamic-type-violation.md) — 检测对象何时具有错误的动态类型。
- [无效的浮点转换](invalid-float-cast.md) — 检测转换到、转换自浮点类型以及浮点类型之间的越界转换。
- [除以零](division-by-zero.md) — 检测除数为零的除法运算。
- [Nonnull 参数冲突](nonnull-argument-violation.md) — 检测参数何时错误地接收到空值。
- [Nonnull 返回值冲突](nonnull-return-value-violation.md) — 检测函数何时错误地返回空值。
- [Nonnull 变量赋值冲突](nonnull-variable-assignment-violation.md) — 检测你何时错误地将空值赋给一个变量。
- [创建空引用与解引用空指针](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建以及空指针的解引用。
- [无效的对象大小](invalid-object-size.md) — 检测因类型大小不同而导致的无效指针转换。
- [无效的移位](invalid-shift.md) — 检测无效及溢出的移位操作。
- [无效的可变长度数组](invalid-variable-length-array.md) — 检测负数的数组边界。
