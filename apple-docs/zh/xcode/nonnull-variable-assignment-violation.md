---
title: 非空变量赋值违规
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/nonnull-variable-assignment-violation
source_url: 'https://developer.apple.com/documentation/xcode/nonnull-variable-assignment-violation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/nonnull-variable-assignment-violation.json'
content_hash: 'sha256:0b670b06e2faab6a'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [及早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 非空变量赋值违规

<sub>文章</sub>

检测何时你错误地将 null 赋值给变量。

## 概述

使用此检查来检测何时你将 `null` 赋值给带有 `_Nonnull` 注解的变量。适用于 Xcode 9 及更高版本。

> [!note] 注意
> 变量赋值的非空违规检查默认关闭。你可以通过启用 `-fsanitize=nullability-assign` 编译器标志来打开它。

### C 语言中变量赋值的非空注解违规

在以下示例中，对 `assigns_a_value` 的调用破坏了变量 `q` 的 `_Nonnull` 注解：

```occ
void assigns_a_value(int *p) {     
    int *_Nonnull q = p; // 警告：可能赋值为 null
}
assigns_a_value(NULL); // 错误：_Nonnull 变量违规
```

#### 解决方案

修正逻辑错误，或移除 `_Nonnull` 注解。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐指针](misaligned-pointer.md) — 检测代码何时访问未对齐指针或创建未对齐引用。
- [无效布尔值](invalid-boolean.md) — 检测程序何时访问布尔变量且其值非真亦非假。
- [数组越界访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [无效枚举值](invalid-enumeration-value.md) — 检测枚举变量何时包含无效值。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序何时到达不可达点。
- [动态类型违规](dynamic-type-violation.md) — 检测对象何时具有错误的动态类型。
- [无效浮点类型转换](invalid-float-cast.md) — 检测向浮点类型、从浮点类型或浮点类型之间的超出范围的转换。
- [除零](division-by-zero.md) — 检测除数为零的除法。
- [非空参数违规](nonnull-argument-violation.md) — 检测参数何时错误地接收 null 值。
- [非空返回值违规](nonnull-return-value-violation.md) — 检测函数何时错误地返回 null。
- [空引用创建与空指针解引用](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建与空指针的解引用。
- [无效对象大小](invalid-object-size.md) — 检测因类型大小差异导致的无效指针转换。
- [无效移位](invalid-shift.md) — 检测非法和溢出的移位操作。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效变长数组](invalid-variable-length-array.md) — 检测负数的数组边界。
