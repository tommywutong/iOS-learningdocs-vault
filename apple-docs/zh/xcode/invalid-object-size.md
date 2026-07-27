---
title: 无效的对象大小
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/invalid-object-size
source_url: 'https://developer.apple.com/documentation/xcode/invalid-object-size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/invalid-object-size.json'
content_hash: 'sha256:57981d7cf22486c6'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)

# 无效的对象大小

<sub>文章</sub>

检测由于类型大小不同而导致的无效指针转换。

## 概述

使用此检查来检测源类型大小小于目标类型大小的指针转换。使用此类转换的结果访问越界数据会导致未定义行为。自 Xcode 9 起可用。

### C++ 中从空间不足的类型向下转换

在以下示例中，从 `Base *` 到 `Derived *` 的转换值得怀疑，因为 `Base` 的大小不足以容纳 `Derived` 的实例：

```occ
struct Base {
    int pad1;
};
struct Derived : Base {
    int pad2;
};
Derived *getDerived() {
    return static_cast<Derived *>(new Base); // 错误：无效的向下转换
}
```

优化器可能会移除 `getDerived()->pad2` 之类的表达式，因为 `getDerived()` 返回的指针所指向对象的大小不足以包含 `pad2` 字段。

> [!note] 注意
> 在较低的优化级别下，此 UBSan 检查可能不会触发。

#### 解决方法

解决此问题的一种方式是避免向下转换，例如在需要时直接使用 `Derived` 对象的实例。

## 另请参阅

### Undefined Behavior Sanitizer

- [未对齐的指针](misaligned-pointer.md) — 检测代码访问未对齐的指针或创建未对齐的引用的情况。
- [无效的布尔值](invalid-boolean.md) — 检测程序访问布尔变量时，其值既不是 true 也不是 false 的情况。
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
- [无效的移位](invalid-shift.md) — 检测无效和溢出的移位操作。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效的可变长度数组](invalid-variable-length-array.md) — 检测负数组边界。
