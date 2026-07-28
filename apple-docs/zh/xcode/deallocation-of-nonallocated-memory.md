---
title: 未分配内存的释放
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/deallocation-of-nonallocated-memory
source_url: 'https://developer.apple.com/documentation/xcode/deallocation-of-nonallocated-memory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/deallocation-of-nonallocated-memory.json'
content_hash: 'sha256:963c7365eb4ed316'
translated: true
---

> 导航： [技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [提前诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 未分配内存的释放

<sub>文章</sub>

检测尝试释放未分配内存（nonallocated memory）的行为。

## 概述

使用此检查可检测何时对未使用 `malloc` 分配的内存调用 `free`。尝试释放未分配内存可能导致崩溃。适用于 Xcode 7 及更高版本。

### C 语言中栈变量的释放

在以下示例中，`value` 变量在栈（stack）上分配，并在函数退出时释放，因此对其调用 `free` 是不正确的：

```occ
int value = 42;
free(&value); // 错误：对栈上分配的变量调用了 free
```

#### 解决方案

不要对在栈上分配的变量调用 `free` 函数。

## 另请参阅

### Address Sanitizer

- [已释放内存的使用](use-of-deallocated-memory.md) — 检测已释放内存的使用。
- [已释放内存的释放](deallocation-of-deallocated-memory.md) — 检测尝试释放已释放内存的行为。
- [函数返回后栈内存的使用](use-of-stack-memory-after-function-return.md) — 检测在其声明函数返回后访问栈变量内存的行为。
- [超出作用域栈内存的使用](use-of-out-of-scope-stack-memory.md) — 检测在声明作用域外访问变量的行为。
- [缓冲区溢出和下溢](overflow-and-underflow-of-buffers.md) — 检测在缓冲区边界外访问内存的行为。
- [C++ 容器溢出](overflow-of-c-containers.md) — 检测在 C++ 容器边界外访问容器的行为。
