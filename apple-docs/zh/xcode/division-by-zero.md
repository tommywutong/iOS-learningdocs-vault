---
title: 除以零
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/division-by-zero
source_url: 'https://developer.apple.com/documentation/xcode/division-by-zero'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/division-by-zero.json'
content_hash: 'sha256:7c810dcadc2cc921'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程与崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 除以零

<sub>文章</sub>

检测除数为零的除法运算。

## 概述

使用此检查来检测除数为零的整数和浮点数除法。除以零属于未定义行为，可能导致崩溃或不正确的程序输出。此检查可用于 Xcode 9 及更高版本。

### C 中的整数除以零

在以下代码中，`for` 循环会在第一次迭代时执行除以零的运算：

```occ
int sum = 10;
for (int i = 0; i < 64; ++i) {
    sum /= i; // 错误：第一次迭代时除以零
}
```

> [!note] 注意
> 如果优化器确定循环的任何一次迭代都可能触发未定义行为，它可能会移除循环的一部分。

#### 解决方案

修改逻辑，以检查除数是否可能等于零，并在这种情况下避免执行除法。

## 另请参阅

### 未定义行为 Sanitizer

- [未对齐的指针](misaligned-pointer.md) — 检测代码何时访问未对齐的指针或创建未对齐的引用。
- [无效的布尔值](invalid-boolean.md) — 检测程序何时访问布尔变量且其值既不是 true 也不是 false。
- [越界数组访问](out-of-bounds-array-access.md) — 检测对数组的越界访问。
- [无效的枚举值](invalid-enumeration-value.md) — 检测枚举变量何时具有无效值。
- [到达不可达位置](reaching-of-unreachable-point.md) — 检测程序何时到达不可达位置。
- [动态类型违规](dynamic-type-violation.md) — 检测对象何时具有错误的动态类型。
- [无效的浮点数转换](invalid-float-cast.md) — 检测转换为浮点类型、从浮点类型转换或在浮点类型之间转换时发生的越界转换。
- [Nonnull 实参违规](nonnull-argument-violation.md) — 检测实参何时错误地接收了空值。
- [Nonnull 返回值违规](nonnull-return-value-violation.md) — 检测函数何时错误地返回 null。
- [Nonnull 变量赋值违规](nonnull-variable-assignment-violation.md) — 检测何时错误地将 null 赋给变量。
- [创建空引用和解引用空指针](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建和空指针解引用。
- [无效的对象大小](invalid-object-size.md) — 检测因类型大小不同而产生的无效指针转换。
- [无效的移位](invalid-shift.md) — 检测无效和溢出的移位。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效的变长数组](invalid-variable-length-array.md) — 检测为负数的数组边界。
