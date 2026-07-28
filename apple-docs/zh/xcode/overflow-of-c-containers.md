---
title: C++ 容器的溢出
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/overflow-of-c-containers
source_url: 'https://developer.apple.com/documentation/xcode/overflow-of-c-containers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/overflow-of-c-containers.json'
content_hash: 'sha256:7d74c7dad9db5194'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# C++ 容器的溢出

<sub>文章</sub>

检测你在其边界之外访问 C++ 容器的行为。

## 概述

使用此检查来检测你在区域 `[container.begin(), container.end()]` 之外访问 libc++ 容器的行为，即使所访问的内存位于该容器内部使用的堆分配缓冲区中也是如此。此功能在 Xcode 7 及更高版本中可用。

> [!note] 注意
> 此检查默认启用。在早于版本 26 的 Xcode 版本中，它默认禁用。请参阅[禁用容器溢出检查](overflow-of-c-containers.md#Disabling-Container-Overflow-Checks)以禁用它。

### C++ 中的 vector 溢出

在以下示例中，`vector` 变量的有效索引范围为 `[0,2]`，但访问的索引是 `3`，这会导致溢出：

```occ
std::vector<int> vector;
vector.push_back(0);
vector.push_back(1);
vector.push_back(2);
auto *pointer = &vector[0];
return pointer[3]; // 错误：vector 的越界访问
```

#### 解决方案

在尝试访问特定索引处的容器之前添加边界检查。

### 禁用容器溢出检查

> [!note] 注意
> 自 Xcode 26 起，[启用 C++ 容器溢出检查（Enable C++ Container Overflow Checks）](build-settings-reference.md#Enable-C++-Container-Overflow-Checks)构建设置不再有任何效果。

当未使用 Address Sanitizer 编译的代码修改容器时，你可能会遇到误报的“容器溢出”错误。为使容器溢出检查正常工作，你需要使用 Address Sanitizer 编译所有代码。如果你无法做到，请使用以下方法之一关闭容器溢出检查：

- **设置 ASAN_OPTIONS 环境变量** — 将 `ASAN_OPTIONS` 环境变量设置为 `detect_container_overflow=0`，或者如果此环境变量已被设置，则附加 `:detect_container_overflow=0`。你应在运行目标的 Scheme 下，或测试计划的 Configurations 下执行此操作。请注意，对于 UI 测试，你可能需要在 XCUIApplication 的 [launchEnvironment](../xcuiautomation/xcuiapplication/launchenvironment.md) 中设置此项。
- **在你的可执行文件中定义 __asan_default_options 函数** — 当你无法控制程序的环境变量时，使用此方法。通过在可执行文件中定义以下函数来禁用容器溢出检查：

```occ
#ifdef __cplusplus
extern "C" {
#endif
#include <sanitizer/asan_interface.h>

__attribute__((used, visibility("default"))) const char *__asan_default_options() {
    return "detect_container_overflow=0";
}
#ifdef __cplusplus
}
#endif
```

如果你设置了[导出的符号文件（Exported Symbols File）](build-settings-reference.md#Exported-Symbols-File)构建设置，则还需将 `___asan_default_options` 添加到该文件，以确保系统导出该符号。

如果你同时在 `__asan_default_options` 函数和 `ASAN_OPTIONS` 环境变量中设置了 `detect_container_overflow` 选项，系统将使用环境变量中的值。

## 另请参阅

### Address Sanitizer

- [使用已释放的内存](use-of-deallocated-memory.md) — 检测对已释放内存的使用。
- [释放已释放的内存](deallocation-of-deallocated-memory.md) — 检测释放已释放内存的尝试。
- [释放未分配的内存](deallocation-of-nonallocated-memory.md) — 检测释放未分配内存的尝试。
- [函数返回后使用栈内存](use-of-stack-memory-after-function-return.md) — 检测在其声明函数返回后访问栈变量内存的行为。
- [使用超出作用域的栈内存](use-of-out-of-scope-stack-memory.md) — 检测对其声明作用域之外的变量的访问。
- [缓冲区的溢出和下溢](overflow-and-underflow-of-buffers.md) — 检测在缓冲区边界之外访问内存的行为。
