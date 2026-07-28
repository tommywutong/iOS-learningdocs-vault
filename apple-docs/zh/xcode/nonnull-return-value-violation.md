---
title: 非空返回值违规
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/nonnull-return-value-violation
source_url: 'https://developer.apple.com/documentation/xcode/nonnull-return-value-violation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/nonnull-return-value-violation.json'
content_hash: 'sha256:70306053710af987'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 非空返回值违规

<sub>文章</sub>

检测函数错误地返回 null。

## 概述

使用此检查项可检测带有 `returns_nonnull` 特性（attribute）的函数，或返回类型带有 `_Nonnull` 标注的函数返回 null 的情况。此检查项适用于 Xcode 9 及更高版本。

> [!note] 注意
> 针对带有 `_Nonnull` 标注的返回类型的非空违规检查默认处于关闭状态。你可以通过启用 `-fsanitize=nullability-return` 编译器标志来打开它。

### C 语言中函数非空特性违规

在以下代码中，`nonnull_returning_function` 函数违反了 `returns_nonnull` 特性：

```occ
__attribute__((returns_nonnull)) int *nonnull_returning_function(int *p) {
    return p; // 警告：此处可能返回 NULL
}
nonnull_returning_function(NULL); // 错误：非空返回值特性违规
```

#### 解决方案

修正逻辑错误，为函数添加必要的空值防护，或移除 `returns_nonnull` 特性并相应地重写函数调用方的逻辑。

### C 语言中返回类型非空标注违规

以下代码违反了 `nonnull_returning_function` 函数返回类型的 `_Nonnull` 标注：

```occ
int *_Nonnull nonnull_returning_function(int *p) {
    return p; // 警告：此处可能返回 NULL
}
nonnull_returning_function(NULL); // 错误：非空返回值特性违规
```

#### 解决方案

修正逻辑错误，为函数添加必要的空值防护，或移除 `_Nonnull` 标注并相应地重写函数调用方的逻辑。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐指针](misaligned-pointer.md) — 检测代码访问未对齐指针或创建未对齐引用的情况。
- [无效布尔值](invalid-boolean.md) — 检测程序访问布尔变量且其值非 true 或 false 的情况。
- [数组越界访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [无效枚举值](invalid-enumeration-value.md) — 检测枚举变量的值无效的情况。
- [抵达不可达点](reaching-of-unreachable-point.md) — 检测程序到达不可达点的情况。
- [动态类型违规](dynamic-type-violation.md) — 检测对象动态类型错误的情况。
- [无效浮点数转换](invalid-float-cast.md) — 检测浮点数类型之间或向浮点数类型进行转换时超出范围的情况。
- [除零](division-by-zero.md) — 检测除数为零的除法。
- [非空参数违规](nonnull-argument-violation.md) — 检测参数错误地接收 null 值的情况。
- [非空变量赋值违规](nonnull-variable-assignment-violation.md) — 检测你错误地将 null 赋值给变量的情况。
- [空引用创建与空指针解引用](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建与空指针的解引用。
- [无效对象大小](invalid-object-size.md) — 检测因类型大小差异导致的无效指针转换。
- [无效移位](invalid-shift.md) — 检测无效及溢出的移位。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效变长数组](invalid-variable-length-array.md) — 检测数组长度为负数的情况。
