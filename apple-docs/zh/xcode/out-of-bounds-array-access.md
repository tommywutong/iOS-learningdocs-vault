---
title: 数组越界访问
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/out-of-bounds-array-access
source_url: 'https://developer.apple.com/documentation/xcode/out-of-bounds-array-access'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/out-of-bounds-array-access.json'
content_hash: 'sha256:7c3ff4fc7e10fc61'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [及早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 数组越界访问

<sub>文章</sub>

检测数组的越界访问。

## 概述

使用此检查来检测试图访问超出数组边界的索引。数组越界访问的行为是未定义的，可能导致崩溃或程序输出不正确。从 Xcode 9 及更高版本开始可用。

> [!note] 注意
> 此检查不检测堆分配数组的越界访问。

### C 语言中的数组越界访问

在以下示例中，循环的最后一次迭代发生了对 `array` 的越界访问：

```occ
int array[5];
for (int i = 0; i <= 5; ++i) {
    array[i] += 1; // 错误：最后一次迭代发生越界访问
}
```

#### 解决方案

确保被访问的索引不超过数组的边界。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐指针](misaligned-pointer.md) — 检测代码是否访问了未对齐的指针或创建了未对齐的引用。
- [无效布尔值](invalid-boolean.md) — 检测程序是否访问了值既非 true 也非 false 的布尔变量。
- [无效枚举值](invalid-enumeration-value.md) — 检测枚举变量是否具有无效值。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序是否到达了不可达点。
- [动态类型违规](dynamic-type-violation.md) — 检测对象是否具有错误的动态类型。
- [无效浮点转换](invalid-float-cast.md) — 检测向浮点类型、从浮点类型或在浮点类型之间的越界转换。
- [除以零](division-by-zero.md) — 检测除数为零的除法。
- [非空参数违规](nonnull-argument-violation.md) — 检测参数是否错误地接收了 null 值。
- [非空返回值违规](nonnull-return-value-violation.md) — 检测函数是否错误地返回了 null。
- [非空变量赋值违规](nonnull-variable-assignment-violation.md) — 检测你是否错误地将 null 赋值给变量。
- [创建空引用与空指针解引用](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建和空指针的解引用。
- [无效对象大小](invalid-object-size.md) — 检测由于类型大小差异导致的无效指针转换。
- [无效移位](invalid-shift.md) — 检测无效和溢出的移位操作。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效可变长度数组](invalid-variable-length-array.md) — 检测负的数组边界。
