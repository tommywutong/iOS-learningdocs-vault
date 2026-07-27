---
title: 无效的布尔值
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/invalid-boolean
source_url: 'https://developer.apple.com/documentation/xcode/invalid-boolean'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/invalid-boolean.json'
content_hash: 'sha256:15fd818d4cde03fa'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)

# 无效的布尔值

<sub>文章</sub>

检测程序访问布尔变量时，其值既不是 true 也不是 false 的情况。

## 概述

使用此检查可以检测在布尔变量的值既不是 true 也不是 false 时对它的访问。当使用整数或指针而没有进行适当的类型转换时，可能出现这个问题。使用超出范围的布尔值属于未定义行为，可能很难调试。自 Xcode 9 起可用。

### C 语言中的无效布尔变量访问

下面这段代码的本意是在 `result` 非零时调用 `success` 函数。但由于它使用了布尔检查，编译器作为一种优化，可能只生成检查 `predicate` 最低有效位（值为 `0`）的指令，从而导致逻辑错误。

```occ
int result = 2;
bool *predicate = (bool *)&result;
if (*predicate) { // 错误：该变量不是有效的布尔值
    success();
}
```

#### 解决方法

使用整数比较来代替布尔检查。

```occ
int result = 2;
if (result != 0) { // 正确
  success();
}
```

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐的指针](misaligned-pointer.md) — 检测代码访问未对齐的指针或创建未对齐的引用的情况。
- [数组的越界访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [无效的枚举值](invalid-enumeration-value.md) — 检测枚举变量的值无效的情况。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序到达不可达点的情况。
- [动态类型冲突](dynamic-type-violation.md) — 检测对象的动态类型错误的情况。
- [无效的浮点转换](invalid-float-cast.md) — 检测浮点类型之间或与浮点类型互相转换时的越界转换。
- [除以零](division-by-zero.md) — 检测除数为零的除法运算。
- [Nonnull 参数冲突](nonnull-argument-violation.md) — 检测参数错误地接收到空值的情况。
- [Nonnull 返回值冲突](nonnull-return-value-violation.md) — 检测函数错误地返回空值的情况。
- [Nonnull 变量赋值冲突](nonnull-variable-assignment-violation.md) — 检测你错误地将空值赋给变量的情况。
- [创建空引用与解引用空指针](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建和空指针的解引用。
- [无效的对象大小](invalid-object-size.md) — 检测由于类型大小不同而导致的无效指针转换。
- [无效的移位](invalid-shift.md) — 检测无效和溢出的移位操作。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效的可变长度数组](invalid-variable-length-array.md) — 检测负数组边界。
