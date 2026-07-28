---
title: 未对齐指针
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/misaligned-pointer
source_url: 'https://developer.apple.com/documentation/xcode/misaligned-pointer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/misaligned-pointer.json'
content_hash: 'sha256:df17d92f6692858e'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [及早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 未对齐指针

<sub>文章</sub>

当代码访问未对齐的指针或创建未对齐的引用时进行检测。

## 概述

在 Xcode 9 及更高版本中，你可以使用此检查来检测对未对齐指针的读取或写入，或检测你何时创建了未对齐的引用。如果指针的地址不是其类型对齐方式的倍数，则该指针为未对齐。解引用未对齐的指针属于未定义行为，可能导致崩溃或性能下降。

对齐违规在序列化或反序列化数据的代码中频繁发生。通过使用能够保持数据对齐的序列化格式来避免此问题。

### C 中的未对齐整数指针赋值

在以下示例中，`pointer` 变量必须具有 4 字节对齐，但只具有 1 字节对齐：

```occ
int8_t *buffer = malloc(64);
int32_t *pointer = (int32_t *)(buffer + 1);
*pointer = 42; // 错误：未对齐整数指针赋值
```

#### 解决方案

使用如 `memcpy` 这样的赋值函数，它可以处理未对齐的输入。

```occ
int8_t *buffer = malloc(64);
int32_t value = 42;
memcpy(buffer + 1, &value, sizeof(int32_t)); // 正确
```

> [!note] 注意
> 编译器通常可以安全地优化对 `memcpy` 的调用，即使参数未对齐也是如此。

### C 中的未对齐结构体指针赋值

在以下示例中，`pointer` 变量必须具有 8 字节对齐，但只具有 1 字节对齐：

```swift
struct A {
    int32_t i32;
    int64_t i64;
};
int8_t *buffer = malloc(32);
struct A *pointer = (struct A *)(buffer + 1);
pointer->i32 = 7; // 错误：指针未对齐
```

#### 解决方案

一种解决方案是压缩结构体。在以下示例中，压缩后的 `A` 结构体阻止编译器在成员之间添加填充：

```occ
struct A { ... } __attribute__((packed));
```

> [!important] 重要
> 压缩结构体可能会对性能产生不利影响。

## 另请参阅

### Undefined Behavior Sanitizer

- [无效布尔值](invalid-boolean.md) — 检测程序访问布尔变量且其值不是 true 或 false 的情况。
- [数组越界访问](out-of-bounds-array-access.md) — 检测数组的越界访问。
- [无效枚举值](invalid-enumeration-value.md) — 检测枚举变量具有无效值的情况。
- [到达不可达点](reaching-of-unreachable-point.md) — 检测程序到达不可达点的情况。
- [动态类型违规](dynamic-type-violation.md) — 检测对象具有错误动态类型的情况。
- [无效浮点数转换](invalid-float-cast.md) — 检测浮点类型的越界转换。
- [除零](division-by-zero.md) — 检测除数为零的除法。
- [Nonnull 参数违规](nonnull-argument-violation.md) — 检测参数错误地接收空值的情况。
- [Nonnull 返回值违规](nonnull-return-value-violation.md) — 检测函数错误地返回 null 的情况。
- [Nonnull 变量赋值违规](nonnull-variable-assignment-violation.md) — 检测你错误地为变量赋空值的情况。
- [空引用创建与空指针解引用](null-reference-creation-and-null-pointer-dereference.md) — 检测空引用的创建和空指针的解引用。
- [无效对象大小](invalid-object-size.md) — 检测因类型大小差异导致的无效指针转换。
- [无效移位](invalid-shift.md) — 检测无效和溢出的移位。
- [整数溢出](integer-overflow.md) — 检测算术运算中的溢出。
- [无效变长数组](invalid-variable-length-array.md) — 检测负数数组边界。
