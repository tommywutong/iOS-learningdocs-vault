---
title: 空引用创建和空指针解引用
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/null-reference-creation-and-null-pointer-dereference
source_url: 'https://developer.apple.com/documentation/xcode/null-reference-creation-and-null-pointer-dereference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/null-reference-creation-and-null-pointer-dereference.json'
content_hash: 'sha256:59807c0ed5e0a1bd'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 空引用创建和空指针解引用

<sub>文章</sub>

检测空引用的创建和空指针解引用。

## 概述

在 Xcode 9 及更高版本中，你可以使用这项检查来检测空引用的创建和空指针解引用。解引用空指针总会引发未定义行为，并可能导致崩溃。如果编译器发现指针解引用，它会将该指针视为非空（nonnull）。因此，优化器可能会移除针对已解引用指针的空相等性检查。

### 在 C++ 中创建空引用

以下示例展示了如何创建空引用。C++ 中的引用必须是非空的：

```occ
int &x = *(int *)nullptr; // 错误：空引用
```

#### 解决方案

改用指针。

```occ
int *x = nullptr; // 正确
```

### 通过空指针访问 C++ 中的成员

以下代码对地址为空的对象进行了成员调用。编译器可能会移除 `this` 指针上的空检查，因为它要求该指针为 `nonnull`。

```occ
struct A {
    int x;
    int getX() {
        if (!this) { // 警告：冗余的空检查可能被移除
            return 0;
        }
        return x; // 警告：'this' 指针为空，但在这里被解引用
    }
};
A *a = nullptr;
int x = a->getX(); // 错误：通过空指针访问成员
```

> [!important] 重要
> 务必避免对 `this` 指针进行空检查。

#### 解决方案

避免对空对象调用方法。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐指针](misaligned-pointer.md) — 检测代码何时访问未对齐的指针或创建未对齐的引用。
- [无效布尔值](invalid-boolean.md) — 检测程序何时访问布尔变量且其值不是 true 或 false。
- [数组越界访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [无效枚举值](invalid-enumeration-value.md) — 检测枚举变量何时具有无效值。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序何时到达不可达点。
- [动态类型违规](dynamic-type-violation.md) — 检测对象何时具有错误的动态类型。
- [无效浮点转换](invalid-float-cast.md) — 检测转换为浮点类型、从浮点类型转换，以及浮点类型之间转换超出范围。
- [除零](division-by-zero.md) — 检测除数为零的除法。
- [非空参数违规](nonnull-argument-violation.md) — 检测参数何时错误地接收到空值。
- [非空返回值违规](nonnull-return-value-violation.md) — 检测函数何时错误地返回空值。
- [非空变量赋值违规](nonnull-variable-assignment-violation.md) — 检测你何时错误地将空值赋给变量。
- [无效对象大小](invalid-object-size.md) — 检测因类型大小差异导致的无效指针转换。
- [无效移位](invalid-shift.md) — 检测无效和溢出的移位。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效变长数组](invalid-variable-length-array.md) — 检测负数组边界。
