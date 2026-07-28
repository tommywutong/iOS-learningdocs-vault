---
title: 非空参数违规
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/nonnull-argument-violation
source_url: 'https://developer.apple.com/documentation/xcode/nonnull-argument-violation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/nonnull-argument-violation.json'
content_hash: 'sha256:6af32d0312515f55'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [及早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 非空参数违规

<sub>文章</sub>

检测参数何时错误地接收了空值。

## 概述

使用此检查来检测，当函数的某个参数带有 `nonnull` 特性或 `_Nonnull` 标注时，该参数却接收到空值的情况。此检查在 Xcode 9 及更高版本中可用。

> [!note] 注意
> 针对带有 `_Nonnull` 标注的参数的“非空违规”检查默认处于关闭状态。你可以通过启用 `-fsanitize=nullability-arg` 编译器标志来开启它。

### C 语言中违反 nonnull 参数特性

在以下示例中，对 `has_nonnull_argument` 函数的调用违反了参数 `p` 的 `nonnull` 特性：

```occ
void has_nonnull_argument(__attribute__((nonnull)) int *p) { 
     // ... 
}
has_nonnull_argument(NULL); // 错误：非空参数特性违规
```

#### 解决方案

纠正逻辑错误，或者移除 `nonnull` 特性并相应重写所调用函数的逻辑。

### C 语言中违反参数的非空标注

在以下示例中，对 `has_nonnull_argument` 函数的调用违反了参数 `p` 的 `_Nonnull` 标注：

```occ
void has_nonnull_argument(int * _Nonnull p) { 
     // ... 
}
has_nonnull_argument(NULL); // 错误：_Nonnull 标注违规
```

#### 解决方案

纠正逻辑错误，或者移除 `_Nonnull` 特性并相应重写所调用函数的逻辑。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐指针](misaligned-pointer.md) — 检测代码何时访问未对齐指针或创建未对齐引用。
- [无效布尔值](invalid-boolean.md) — 检测程序何时访问布尔变量且其值不是 true 或 false。
- [数组越界访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [无效枚举值](invalid-enumeration-value.md) — 检测枚举变量何时包含无效值。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序何时到达不可达点。
- [动态类型违规](dynamic-type-violation.md) — 检测对象何时具有错误的动态类型。
- [无效浮点数转型](invalid-float-cast.md) — 检测至浮点类型、自浮点类型或浮点类型之间的越界转型。
- [除零错误](division-by-zero.md) — 检测除数为零的除法。
- [非空返回值违规](nonnull-return-value-violation.md) — 检测函数何时错误地返回空值。
- [非空变量赋值违规](nonnull-variable-assignment-violation.md) — 检测你何时错误地将空值赋值给变量。
- [创建空引用与空指针解引用](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建和空指针的解引用。
- [无效对象大小](invalid-object-size.md) — 检测由于类型大小差异导致的无效指针转型。
- [无效移位](invalid-shift.md) — 检测无效和溢出的移位操作。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效变长数组](invalid-variable-length-array.md) — 检测负数数组边界。
