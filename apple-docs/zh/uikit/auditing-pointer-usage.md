---
title: 审查指针使用情况
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/auditing-pointer-usage
source_url: 'https://developer.apple.com/documentation/uikit/auditing-pointer-usage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/auditing-pointer-usage.json'
content_hash: 'sha256:f8b415c7f05a3200'
translated: true
---

> 导航：[技术](../technologies.md) · [UIKit](../uikit.md) · [App 与环境](app-and-environment.md) · [将 App 从 32 位架构更新到 64 位架构](updating-your-app-from-32-bit-to-64-bit-architecture.md)

# 审查指针使用情况

<sub>文章</sub>

确保代码中的指针对 64 位运行时安全。

## 概述

指针引用内存中的对象和其他数据，在 C 与 Objective-C 中经常用于将对象传给函数，或操控内存内容。从 32 位架构更新到 64 位架构时，代码中的指针大小会翻倍，对整个代码产生影响。任何有关指针大小的假设都可能导致未定义行为、内存损坏（memory corruption）或崩溃。

若要检查代码是否正确使用指针，请查找将指针转换或强制转换为另一种类型的区域。避免将指针转换为整数等其他类型。如果你使用 `NSLog` 或 `printf` 等函数打印指针值，请在格式字符串中使用正确的规定宏，以确保正确显示这些值。

### 有选择地将指针转换为整数

将指针转换为整数类型时，请始终使用一致的指针类型，确保所有变量都足以容纳一个地址。

下面的代码将指针转换为 `int` 类型，以便对地址执行算术运算。在 32 位运行时中，这段代码可以正常工作，因为 `int` 类型与指针的大小相同。但是，在 64 位运行时中，指针比 `int` 类型大，因此赋值会丢失一部分指针数据。若要解决此问题，请移除类型转换。此时，编译器生成的代码会正确推进指针。

```objc
int *c = something passed in as an argument...

int *d = (int *)((int)c + 4); // 错误。

int *d = c + 1;               // 正确。
```

如果必须将指针转换为整数类型，请始终使用 `uintptr_t` 类型以避免截断。请注意，通过整数运算修改指针值，然后将其转换回指针，可能会违反基本的类型别名规则。这可能导致编译器出现意外行为；访问未对齐的指针时，还可能导致处理器故障。

### 使用 sizeof 分配内存

始终使用 `sizeof` 获取要分配的任何结构体或变量的正确大小。切勿使用显式大小调用 `malloc` 来为变量分配空间。

```objc
// 错误。
uint32_t *x = (uint32_t *)malloc(4);

// 正确。
uint32_t *x = (uint32_t *)malloc(sizeof(uint32_t));
```

在代码中搜索后面没有跟随 `sizeof` 的所有 `malloc` 实例。

### 使用获准方法访问 Objective-C 内部结构

如果代码直接访问对象的 `isa` 字段，该代码在 64 位运行时中执行时会失败，因为 `isa` 字段不再存储指针。它会改为包含部分指针数据，并使用剩余位存储其他运行时信息。

若要读取对象的 `isa` 字段，请改用 class 属性，或调用 [object_getClass(_:)](<../objectivec/object_getclass(__).md>) 函数。若要写入对象的 `isa` 字段，请调用 [object_setClass(_:_:)](<../objectivec/object_setclass(____).md>) 函数。

> [!important] 重要
> Simulator App 无法检测此处所述的错误。请务必在实际硬件上测试你的 App。

### 更新格式字符串

当代码必须同时支持 32 位和 64 位运行时时，`printf` 等打印函数可能很难编写，因为数据类型会随运行时而变化。若要解决标准类型和指针大小整数的此类问题，请使用下表列出的各种宏。

| 标准类型 | 格式字符串 |
|---|---|
| `int` | `%d` |
| `long` | `%ld` |
| `long long` | `%lld` |
| `size_t` | `%zu` |
| `ptrdiff_t` | `%td` |
| 任意指针 | `%p` |

| 指针大小的整数类型 | 格式字符串 |
|---|---|
| `int[N]_t`（例如 `int32_t`） | `PRId[N]`（例如 `PRId32`） |
| `uint[N]_t` | `PRIu[N]` |
| `int_least[N]_t` | `PRIdLEAST[N]` |
| `uint_least[N]_t` | `PRIuLEAST[N]` |
| `int_fast[N]_t` | `PRIdFAST[N]` |
| `uint_fast[N]_t` | `PRIuFAST[N]` |
| `intptr_t` | `PRIdPTR` |
| `uintptr_t` | `PRIuPTR` |
| `intmax_t` | `PRIdMAX` |
| `uintmax_t` | `PRIuMAX` |

以下示例代码会打印一个 `intptr_t` 变量（指针大小的整数）和一个指针。

```objc
#include <inttypes.h>
void *foo;
intptr_t k = (intptr_t) foo;
void *ptr = &k;

printf("The value of k is %" PRIdPTR "\n", k);
printf("The value of ptr is %p\n", ptr);
```

## 另请参阅

### 内存与指针访问

- [更新数据结构](updating-data-structures.md) — 检查 App 的数据设计，并更新设计以符合 64 位架构。
- [管理函数和函数指针](managing-functions-and-function-pointers.md) — 确保代码正确处理函数、函数指针和 Objective-C 消息。
