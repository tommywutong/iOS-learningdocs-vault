---
title: 无效移位
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/invalid-shift
source_url: 'https://developer.apple.com/documentation/xcode/invalid-shift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/invalid-shift.json'
content_hash: 'sha256:f1cd79908e9229e1'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 无效移位

<sub>文章</sub>

检测无效的移位数，以及可能溢出的移位操作。

## 概述

使用这项检查，可以发现移位数无效的位移位，以及可能溢出的移位。这类移位的计算结果属于未定义行为（undefined behavior），优化器可能将它们丢弃。适用于 Xcode 9 及后续版本。

### C 语言中的无效移位数

以下代码展示了一次移位数无效的移位操作，因为赋值目标类型无法表达它的运算结果：

```occ
int32_t x = 1;
x <<= 32; // 错误：(1 << 32) 无法用 int32_t 表达
```

如果优化器能证明某次移位的位数可能无效，就可能用一个不确定的值来替代运算结果。

#### 解决方式

换个更大的目标类型，例如 `int64_t`。

### C 语言中的移位溢出

在以下代码里，第二次移位会让 `x` 溢出，因为 `int32_t` 没办法表达 `((1U << 31) - 1) << 2` 这个结果：

```occ
int32_t x = (1U << 31) - 1;
x <<= 2; // 错误：移位的结果超出 x 的表示范围
```

#### 解决方式

换个更大的目标类型，例如 `int64_t`。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐的指针](misaligned-pointer.md)——检测代码访问未对齐指针，或者创建未对齐引用。
- [无效的布尔值](invalid-boolean.md)——检测程序访问某个布尔变量，而它的值既不是真也不是假。
- [数组越界访问](out-of-bounds-array-access.md)——检测对数组的越界访问。
- [无效的枚举值](invalid-enumeration-value.md)——检测枚举变量保存了无效的值。
- [抵达不可达代码点](reaching-of-unreachable-point.md)——检测程序抵达了标注为不可达的代码点。
- [动态类型违背](dynamic-type-violation.md)——检测某个对象携带了错误的动态类型。
- [无效的浮点转换](invalid-float-cast.md)——检测超出范围的、以浮点类型作为源或目标的类型转换，以及浮点类型之间的越界转换。
- [除以零](division-by-zero.md)——检测除数为零的除法操作。
- [nonnull 实参违背](nonnull-argument-violation.md)——检测某个参数错误地收到了空值。
- [nonnull 返回值违背](nonnull-return-value-violation.md)——检测某个函数错误地返回了空值。
- [nonnull 变量赋值违背](nonnull-variable-assignment-violation.md)——检测你把空值错误地赋给了某个变量。
- [创建空引用并解引用空指针](null-reference-creation-and-null-pointer-dereference.md)——检测创建空引用，以及解引用空指针。
- [无效的对象大小](invalid-object-size.md)——检测由于类型大小差异而出现的无效指针转换。
- [整数溢出](integer-overflow.md)——检测算术运算中的溢出。
- [无效的可变长度数组](invalid-variable-length-array.md)——检测数组边界为负数的情况。
