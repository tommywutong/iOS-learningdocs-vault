---
title: 函数返回后使用栈内存
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/use-of-stack-memory-after-function-return
source_url: 'https://developer.apple.com/documentation/xcode/use-of-stack-memory-after-function-return'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/use-of-stack-memory-after-function-return.json'
content_hash: 'sha256:20934b9c7b8f9a57'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 函数返回后使用栈内存

<sub>文章</sub>

检测你在声明栈变量的函数返回后访问该变量内存的情况。

## 概述

使用此检查来检测一个函数返回后，对该函数所声明栈变量的访问。尝试以这种方式访问栈内存可能导致崩溃或不可预测的行为。此检查在 Xcode 9 及更高版本中可用。

> [!note] 注意
> 此检查默认处于停用状态。你可以在「Edit Scheme」对话框的 Address Sanitizer 选项下启用它。

### 在 C 中使用函数返回后的栈内存

在以下示例中，`integer_pointer_returning_function` 函数返回一个指向栈变量的指针，随后代码尝试访问所返回指针指向的内存：

```occ
int *integer_pointer_returning_function() {
    int value = 42;
    return &value;
}

int *integer_pointer = integer_returning_function();
*integer_pointer = 43; // 错误：无效访问函数返回后的栈内存
```

#### 解决方案

使用指针参数，让函数能够通过引用返回值。

## 另请参阅

### Address Sanitizer

- [使用已释放的内存](use-of-deallocated-memory.md) — 检测对已释放内存的使用。
- [释放已释放的内存](deallocation-of-deallocated-memory.md) — 检测释放已释放内存的尝试。
- [释放未分配的内存](deallocation-of-nonallocated-memory.md) — 检测释放未分配内存的尝试。
- [使用超出作用域的栈内存](use-of-out-of-scope-stack-memory.md) — 检测对声明作用域之外变量的访问。
- [缓冲区上溢和下溢](overflow-and-underflow-of-buffers.md) — 检测你访问缓冲区边界之外内存的情况。
- [C++ 容器溢出](overflow-of-c-containers.md) — 检测你访问 C++ 容器边界之外元素的情况。
