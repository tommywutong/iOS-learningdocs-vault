---
title: 已释放内存的重复释放
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/deallocation-of-deallocated-memory
source_url: 'https://developer.apple.com/documentation/xcode/deallocation-of-deallocated-memory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/deallocation-of-deallocated-memory.json'
content_hash: 'sha256:d624f9e63e25e381'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 已释放内存的重复释放

<sub>文章</sub>

检测对已释放内存再次调用 `free` 的尝试。

## 概述

使用此检查可检测你对已释放内存调用 `free` 的情况，通常称为*双重释放（double free）* 错误。尝试释放内存超过一次可能导致崩溃或其他不可预测的行为。此功能适用于 Xcode 7 及更高版本。

### C 语言中已释放内存的重复释放

在以下示例中，代码在对 `p_int` 变量调用 `free` 释放其内存后，再次对其调用了 `free`：

```occ
int *pointer = malloc(sizeof(int));
free(pointer);
free(pointer); // 错误：对同一内存地址调用了两次 free 
```

#### 解决方案

确保对分配的内存仅调用一次 `free` 函数。

## 另请参阅

### Address Sanitizer

- [已释放内存的使用](use-of-deallocated-memory.md) — 检测对已释放内存的使用。
- [未分配内存的释放](deallocation-of-nonallocated-memory.md) — 检测对未分配内存调用 `free` 的尝试。
- [函数返回后栈内存的使用](use-of-stack-memory-after-function-return.md) — 检测在声明函数返回后访问栈变量内存的情况。
- [超出作用域栈内存的使用](use-of-out-of-scope-stack-memory.md) — 检测对超出声明作用域变量的访问。
- [缓冲区溢出和下溢](overflow-and-underflow-of-buffers.md) — 检测访问缓冲区边界外内存的情况。
- [C++ 容器溢出](overflow-of-c-containers.md) — 检测访问 C++ 容器边界外内存的情况。
