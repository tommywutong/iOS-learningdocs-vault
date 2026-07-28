---
title: 使用已释放的内存
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/use-of-deallocated-memory
source_url: 'https://developer.apple.com/documentation/xcode/use-of-deallocated-memory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/use-of-deallocated-memory.json'
content_hash: 'sha256:84ed8fe4edb528c3'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 使用已释放的内存

<sub>文章</sub>

检测对已释放内存的使用。

## 概述

使用此检查来检测代码何时访问已释放的内存，这种访问可能导致不可预测的行为。此检查在 Xcode 7 及更高版本中可用。

### 在 Objective-C 中使用已释放的内存

在以下示例中，`unsafePointer` 变量具有 `__unsafe_unretained` 所有权（ownership）。由于没有其他对象持有对它的强引用，自动释放池（autorelease pool）释放了该变量，导致它指向无效内存。

```occ
__unsafe_unretained MyClass *unsafePointer;
@autoreleasepool {    
    MyClass *object = [MyClass new];
    unsafePointer = object;
}
NSLog(@"%d", unsafePointer->instanceVariable); 
// 错误：unsafePointer 已在自动释放池中释放
```

#### 解决方案

使用 `__strong` 或 `__weak` 引用代替 `__unsafe_unretained`。强所有权可确保只有在不存在任何强引用时，你或系统才能释放对象。弱所有权不会影响其所引用对象的生命周期，但可确保在你或系统释放对象时，该变量为 `nil`。

### 在 Objective-C 中使用已释放对象的指针

使用指向非对象类型的指针时也会出现此问题。在以下示例中，释放对象时，指向实例变量（instance variable）的指针会失效：

```occ
int *unsafePointer;
@autoreleasepool {    
    MyClass *object = [MyClass new];
    unsafePointer = &object->instanceVariable;
}
NSLog(@"%d", *unsafePointer);
// 错误：在自动释放池中释放对象时，unsafePointer 会失效
```

#### 解决方案

只要可能，请使用属性存取方法（accessor method），而不要直接访问实例变量和指针。

## 另请参阅

### Address Sanitizer

- [释放已释放的内存](deallocation-of-deallocated-memory.md) — 检测释放已释放内存的尝试。
- [释放未分配的内存](deallocation-of-nonallocated-memory.md) — 检测释放未分配内存的尝试。
- [函数返回后使用栈内存](use-of-stack-memory-after-function-return.md) — 检测你在声明栈变量的函数返回后访问该变量内存的情况。
- [使用超出作用域的栈内存](use-of-out-of-scope-stack-memory.md) — 检测对声明作用域之外变量的访问。
- [缓冲区上溢和下溢](overflow-and-underflow-of-buffers.md) — 检测你访问缓冲区边界之外内存的情况。
- [C++ 容器溢出](overflow-of-c-containers.md) — 检测你访问 C++ 容器边界之外元素的情况。
