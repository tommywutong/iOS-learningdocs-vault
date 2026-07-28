---
title: 缓冲区溢出与下溢
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/overflow-and-underflow-of-buffers
source_url: 'https://developer.apple.com/documentation/xcode/overflow-and-underflow-of-buffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/overflow-and-underflow-of-buffers.json'
content_hash: 'sha256:2bed769b1d834799'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程与崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 缓冲区溢出与下溢

<sub>文章</sub>

检测何时超出缓冲区边界访问内存。

## 概述

在 Xcode 7 及更高版本中，你可以使用此检查来检测何时访问了缓冲区边界之外的内存。当访问的内存位于缓冲区末尾之后时，该检查报告溢出；当访问的内存位于缓冲区起始之前时，报告下溢。Xcode 会对堆和栈缓冲区以及全局变量进行消毒。缓冲区溢出和下溢可能导致崩溃或其他不可预测的行为。

### C 语言中的全局、堆和栈溢出

在以下示例中，`global_array`、`heap_buffer` 和 `stack_buffer` 变量的有效索引范围均为 `[0, 9]`，但访问的索引是 `10`，这会导致溢出：

```occ
int global_array[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
void foo() {
    int idx = 10;
    global_array[idx] = 42; // 错误：全局变量越界访问
    char *heap_buffer = malloc(10);
    heap_buffer[idx] = 'x'; // 错误：堆分配变量越界访问
    char stack_buffer[10];
    stack_buffer[idx] = 'x'; // 错误：栈分配变量越界访问
}
```

#### 解决方案

在尝试访问特定索引处的缓冲区之前，添加边界检查。

## 另请参阅

### Address Sanitizer

- [已释放内存的使用](use-of-deallocated-memory.md) — 检测对已释放内存的访问。
- [已释放内存的释放](deallocation-of-deallocated-memory.md) — 检测尝试释放已释放内存的行为。
- [未分配内存的释放](deallocation-of-nonallocated-memory.md) — 检测尝试释放未分配内存的行为。
- [函数返回后栈内存的使用](use-of-stack-memory-after-function-return.md) — 检测在其声明函数返回后访问栈变量内存的行为。
- [超出作用域的栈内存的使用](use-of-out-of-scope-stack-memory.md) — 检测在其声明作用域之外访问变量的行为。
- [C++ 容器的溢出](overflow-of-c-containers.md) — 检测访问 C++ 容器超出其边界的行为。
