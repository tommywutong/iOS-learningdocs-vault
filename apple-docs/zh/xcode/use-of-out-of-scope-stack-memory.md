---
title: 使用超出作用域的栈内存
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/use-of-out-of-scope-stack-memory
source_url: 'https://developer.apple.com/documentation/xcode/use-of-out-of-scope-stack-memory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/use-of-out-of-scope-stack-memory.json'
content_hash: 'sha256:ace81d6c0957f3bc'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing memory, thread, and crash issues early](diagnosing-memory-thread-and-crash-issues-early.md)

# 使用超出作用域的栈内存

<sub>文章</sub>

检测对声明作用域之外变量的访问。

## 概述

使用此检查来检测你何时在变量的作用域之外访问该变量。尝试访问超出作用域的内存可能导致不可预测的行为。此检查在 Xcode 9 及更高版本中可用。

### 在 C 中使用超出作用域的栈内存

在以下示例中，代码根据条件将 `pointer` 变量赋为 `integer_returning_function` 函数的返回值，随后在其声明作用域之外访问该变量：

```occ
int *pointer = NULL;
if (bool_returning_function()) {
    int value = integer_returning_function();
    pointer = &value;
}
*pointer = 42; // 错误：在声明作用域之外无效访问栈内存
```

#### 解决方案

确保不要在变量的声明作用域之外访问变量，或者使用 `malloc` 函数分配内存。

## 另请参阅

### Address Sanitizer

- [使用已释放的内存](use-of-deallocated-memory.md) — 检测对已释放内存的使用。
- [释放已释放的内存](deallocation-of-deallocated-memory.md) — 检测释放已释放内存的尝试。
- [释放未分配的内存](deallocation-of-nonallocated-memory.md) — 检测释放未分配内存的尝试。
- [函数返回后使用栈内存](use-of-stack-memory-after-function-return.md) — 检测你在声明栈变量的函数返回后访问该变量内存的情况。
- [缓冲区上溢和下溢](overflow-and-underflow-of-buffers.md) — 检测你访问缓冲区边界之外内存的情况。
- [C++ 容器溢出](overflow-of-c-containers.md) — 检测你访问 C++ 容器边界之外元素的情况。
