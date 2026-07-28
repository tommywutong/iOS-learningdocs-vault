---
title: 无效的变长数组
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/invalid-variable-length-array
source_url: 'https://developer.apple.com/documentation/xcode/invalid-variable-length-array'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/invalid-variable-length-array.json'
content_hash: 'sha256:94d2169d3c43a635'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 无效的变长数组

<sub>文章</sub>

检测数组的负边界。

## 概述

使用此检查可检测数组的负边界。长度小于零的变长数组（variable-length array）的行为是未定义的，可能导致栈损坏。在 Xcode 9 及更高版本中可用。

### C 语言中的负长度变长数组

在以下代码中，对 `invalid_index_returning_function` 函数的调用返回了一个负数，从而导致无效数组：

```occ
int invalid_index_returning_function() {
    return -1;
}
int idx = invalid_index_returning_function();
int array[idx]; // 错误：无效的数组长度
```

#### 解决方案

在构造数组前检查数组边界，即可修复此问题。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐指针](misaligned-pointer.md)——检测代码访问未对齐指针或创建未对齐引用的行为。
- [无效布尔值](invalid-boolean.md)——检测程序访问布尔变量时其值非真非假的情况。
- [数组越界访问](out-of-bounds-array-access.md)——检测数组的越界访问。
- [无效枚举值](invalid-enumeration-value.md)——检测枚举变量取无效值的情况。
- [到达不可达代码点](reaching-of-unreachable-point.md)——检测程序到达不可达代码点的行为。
- [动态类型违规](dynamic-type-violation.md)——检测对象动态类型错误的情况。
- [无效浮点转换](invalid-float-cast.md)——检测浮点类型转换时超出范围的转换行为。
- [除零](division-by-zero.md)——检测除数为零的除法。
- [非空参数违规](nonnull-argument-violation.md)——检测参数被错误地赋为空值的情况。
- [非空返回值违规](nonnull-return-value-violation.md)——检测函数错误返回空值的情况。
- [非空变量赋值违规](nonnull-variable-assignment-violation.md)——检测你错误地将空值赋给变量的行为。
- [空引用创建与空指针解引用](null-reference-creation-and-null-pointer-dereference.md)——检测空引用的创建与空指针的解引用行为。
- [无效对象大小](invalid-object-size.md)——检测因类型大小差异导致的无效指针转换。
- [无效移位](invalid-shift.md)——检测无效和溢出的移位操作。
- [整数溢出](integer-overflow.md)——检测算术运算中的溢出。
