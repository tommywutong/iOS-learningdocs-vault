---
title: 到达不可达点
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reaching-of-unreachable-point
source_url: 'https://developer.apple.com/documentation/xcode/reaching-of-unreachable-point'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reaching-of-unreachable-point.json'
content_hash: 'sha256:55698ae575d2c8e5'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 到达不可达点

<sub>文章</sub>

检测程序到达不可达点的情况。

## 概述

使用此检查可检测控制流何时到达你使用 `__builtin_unreachable` 创建的程序中的不可达点，这可能导致程序突然终止。此检查在 Xcode 9 及更高版本中可用。

### 在 C 中执行不可达代码

如果 `switch` 语句未能处理函数返回的某个值，程序就会到达 `__builtin_unreachable()`。

```occ
switch (value_returning_function()) {
case ...:                  // 警告：如果 case 并不完备
default:                   // 可能到达 __builtin_unreachable
    __builtin_unreachable();
}
```

#### 解决方案

确保 `switch` 语句和其他控制流语句是完备的。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐的指针](misaligned-pointer.md) — 检测代码访问未对齐指针或创建未对齐引用的情况。
- [无效的布尔值](invalid-boolean.md) — 检测程序访问值并非 true 或 false 的布尔变量的情况。
- [越界数组访问](out-of-bounds-array-access.md) — 检测对数组的越界访问。
- [无效的枚举值](invalid-enumeration-value.md) — 检测枚举变量具有无效值的情况。
- [动态类型违规](dynamic-type-violation.md) — 检测对象具有错误动态类型的情况。
- [无效的浮点转换](invalid-float-cast.md) — 检测与浮点类型相互转换或在浮点类型之间转换时发生的越界转换。
- [除以零](division-by-zero.md) — 检测除数为零的除法。
- [非空参数违规](nonnull-argument-violation.md) — 检测参数错误接收空值的情况。
- [非空返回值违规](nonnull-return-value-violation.md) — 检测函数错误返回空值的情况。
- [非空变量赋值违规](nonnull-variable-assignment-violation.md) — 检测错误地将空值赋给变量的情况。
- [创建空引用和解引用空指针](null-reference-creation-and-null-pointer-dereference.md) — 检测创建空引用和解引用空指针的情况。
- [无效的对象大小](invalid-object-size.md) — 检测因类型大小不同而导致的无效指针转换。
- [无效的移位](invalid-shift.md) — 检测无效移位和溢出移位。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效的变长数组](invalid-variable-length-array.md) — 检测负数数组边界。
