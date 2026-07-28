---
title: 无效的枚举值
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/invalid-enumeration-value
source_url: 'https://developer.apple.com/documentation/xcode/invalid-enumeration-value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/invalid-enumeration-value.json'
content_hash: 'sha256:60b5a85a3a07599c'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 无效的枚举值

<sub>文章</sub>

检测枚举变量的值无效的情况。

## 概述

在 Xcode 9 及后续版本中，你可以使用此检查来检测对枚举变量的访问，而该变量的值并不在其类型的有效范围内。这种情况可能发生在枚举值未初始化时，或者在没有进行适当类型转换的情况下将整数用作枚举值时。使用超出范围的枚举值属于未定义行为，可能表明程序中存在逻辑错误。

### C++ 中的无效枚举变量访问

在下面的示例中，转换为 `E` 类型是无效的，因为 `2` 不在该枚举的范围内：

```occ
enum E {
    a = 1
};
int value = 2;
enum E *e = (enum E *)&value;
return *e; // 错误：2 超出了 E 的有效范围
```

#### 解决方法

确保枚举变量只使用其定义范围内的值。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐的指针](misaligned-pointer.md) — 检测代码访问未对齐的指针或创建未对齐的引用的情况。
- [无效的布尔值](invalid-boolean.md) — 检测程序访问布尔变量时，其值既不是 true 也不是 false 的情况。
- [数组的越界访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序到达不可达点的情况。
- [动态类型冲突](dynamic-type-violation.md) — 检测对象的动态类型错误的情况。
- [无效的浮点转换](invalid-float-cast.md) — 检测向浮点类型、从浮点类型转换以及浮点类型之间转换时的越界转换。
- [除以零](division-by-zero.md) — 检测除数为零的除法运算。
- [Nonnull 参数冲突](nonnull-argument-violation.md) — 检测参数错误地接收到空值的情况。
- [Nonnull 返回值冲突](nonnull-return-value-violation.md) — 检测函数错误地返回空值的情况。
- [Nonnull 变量赋值冲突](nonnull-variable-assignment-violation.md) — 检测你错误地将空值赋给变量的情况。
- [空引用创建与空指针解引用](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建和空指针的解引用。
- [无效的对象大小](invalid-object-size.md) — 检测由于类型大小不同而导致的无效指针转换。
- [无效的移位](invalid-shift.md) — 检测无效和溢出的移位操作。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效的可变长度数组](invalid-variable-length-array.md) — 检测负数组边界。
