---
title: 采用类型感知内存分配
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/adopting-type-aware-memory-allocation
source_url: 'https://developer.apple.com/documentation/xcode/adopting-type-aware-memory-allocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/adopting-type-aware-memory-allocation.json'
content_hash: 'sha256:786532807b97837b'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [构建系统](build-system.md)

# 采用类型感知内存分配

<sub>文章</sub>

减少在代码中将指针当作数据处理的机会。

## 概述

编译器支持类型感知内存分配（type-aware memory allocation），它会跟踪你为其分配内存的数据类型，并为不同的数据类型返回指向不同区域内存的指针。类型分配器（typed allocator）会为你代码中分配的任何数据结构类型生成描述符，例如 C 的 `struct` 或 C++ 的 `class`。当你分配内存以存储特定数据结构类型时，编译器会计算该类型的描述符，并从专门用于存储具有该描述符的内存区域中返回内存。

由于系统记录了包含该指针的内存区域与指定的类型相关联，因此它可以将包含指针的内存区域的分配与纯数据区域的分配隔离开来。

当你启用类型感知内存分配器（type-aware memory allocator）时，编译器会自动将对 `malloc`、`calloc`、`realloc`、`posix_memalign`、相关函数以及 C++ `new` 运算符的调用重写为使用类型感知的等价调用。

### 为你的目标启用类型感知内存分配器

当你添加增强安全（Enhanced Security）功能时，Xcode 会自动配置你的目标以使用类型感知内存分配器以及其他强化设置。有关更多信息，请参阅[为你的 App 启用增强安全性](enabling-enhanced-security-for-your-app.md)。

要在不添加增强安全功能的情况下启用类型感知内存分配器，请在目标中：

- 将 `CLANG_ENABLE_C_TYPED_ALLOCATOR_SUPPORT` 构建设置的值设为 `YES`
- 将 `CLANG_ENABLE_CPLUSPLUS_TYPED_ALLOCATOR_SUPPORT` 构建设置的值设为 `YES`

考虑添加值为 `YES` 的 [`com.apple.security.hardened-process.hardened-heap`](../bundleresources/entitlements/com.apple.security.hardened-process.hardened-heap.md) entitlement，以应用额外的运行时分配器限制。

### 进行类型感知内存分配

在你使用运行时信息在分配内存前确定类型的任何地方，都需要调用类型感知版本的内存分配函数。例如，如果你的 App 包含某种编程语言的运行时库，该库使用运行时信息来确定指针的类型。要自行调用类型感知版本的内存分配函数，请在函数名前加上 `malloc_type_` 前缀。例如，`malloc` 变为 `malloc_type_malloc`。

与常规分配器函数相比，`malloc_type_` 函数多接受一个参数，即你要分配类型的类型描述符。通过构造一个描述该类型的 `malloc_type_descriptor_v0_t` 并读取其 `type_id` 成员值，来计算给定类型的类型描述符。

如果使用 `union` 类型，请避免设计一个使用同一位置既存指针又存数据的类型，因为类型分配器无法保护该内存。

### 创建类型感知分配器包装函数

如果你的项目包含调用系统内存分配函数的包装函数，请考虑是否可以移除这些包装函数并直接调用内存分配函数，从而受益于编译器自动重写以使用类型分配器。如果无法移除包装函数，请编写包装函数的类型感知变体，并使用 `_MALLOC_TYPED` 宏来注解现有包装函数，使其引用对应的类型感知变体。该宏接受两个参数：

- 类型感知包装函数的名称
- 在原始函数参数列表中，开发者用来传递分配大小的参数的索引（第一个参数位于位置 `1`）

例如：

```c
#if defined(_MALLOC_TYPE_ENABLED) && _MALLOC_TYPE_ENABLED

// 声明包装函数的类型感知变体。
void *my_malloc_typed(size_t size, malloc_type_id_t type_id);

// 声明包装函数，并为其添加指向类型感知变体的注解。
void *my_malloc(size_t size) _MALLOC_TYPED(my_malloc_typed, 1);

#else

// 声明包装函数，不添加任何注解。
void *my_malloc(size_t size);

#endif
```

在包装函数的类型感知变体中，返回使用 `malloc_type_` 库函数变体分配的内存的指针：

```c
void *my_malloc_typed(size_t size, malloc_type_id_t type_id) {
  // 实现包装函数的自定义逻辑。

  return malloc_type_malloc(size, type_id);
}
```

## 另请参阅

### 安全与隐私

- [验证 XCFramework 的来源](verifying-the-origin-of-your-xcframeworks.md) — 发现是谁签署了框架，并在发生变更时采取行动。
- [为你的 App 启用增强安全性](enabling-enhanced-security-for-your-app.md) — 检测越界内存访问、对已释放内存的使用以及其他潜在漏洞。
- [创建增强安全辅助扩展](creating-enhanced-security-helper-extensions.md) — 减少攻击者通过扩展程序攻击你 App 的机会。
- [遵循 Mach IPC 安全限制](conforming-to-mach-ipc-security-restrictions.md) — 避免与 Mach 消息相关的崩溃和潜在不安全情况。
