---
title: 管理函数与函数指针
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/managing-functions-and-function-pointers
source_url: 'https://developer.apple.com/documentation/uikit/managing-functions-and-function-pointers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/managing-functions-and-function-pointers.json'
content_hash: 'sha256:489c165a929d9dbf'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Updating your app from 32-bit to 64-bit architecture](updating-your-app-from-32-bit-to-64-bit-architecture.md)

# 管理函数与函数指针

<sub>文章</sub>

确保你的代码正确处理函数、函数指针和 Objective-C 消息。

## 概述

64 位运行时在函数的调用与处理上带来了一些变化。这些变化影响你的代码中如何调用接受可变数量参数的函数以及 Objective-C 消息。通过采用下述调用约定，确保你的代码符合这些变化。

### 始终定义函数原型

在使用更新的项目设置编译时，如果你试图调用一个没有显式原型的函数，编译器会生成错误。你必须提供函数原型，以便编译器能确定函数是否为可变参数函数。

### 确保函数指针使用正确的原型

如果你的代码中传递了函数指针，它的调用约定在代码各处必须采用相同的参数集。永远不要把可变参数函数转换为接受固定数量参数的函数（反之亦然）。

以下代码展示了一个有问题的函数调用示例：

```objc
int MyFunction(int a, int b, ...);

int (*action)(int, int, int) = (int (*)(int, int, int)) MyFunction;
action(1,2,3); // Incorrect.
```

因为这个示例中的函数指针被转换为使用不同的调用约定，调用函数按被调用函数所不期望的顺序放置参数。这种行为可能导致你的 App 崩溃或表现出其他不可预测的行为。

### 使用一致的类型调用可变参数函数

可变参数函数是包含可变参数列表（`varargs`）的函数。可变参数不提供类型信息。此外，可变参数函数的参数不会自动提升为更大型别。在 64 位运行时，如果你向可变参数函数传入不同大小的类型，理解这种行为很重要。

如果你需要区分不同的传入数据类型，请使用格式字符串或类似机制把该信息提供给 `varargs` 函数。如果调用函数没有提供正确信息（或 `varargs` 函数没有正确解读），你将得到不正确的结果。

例如，如果你的 `varargs` 函数需要一个 `long` 整数而你传入一个 32 位值，函数包含你传入数据的 32 位以及下一个参数的 32 位数据。同样，如果你的 `varargs` 函数需要 `int` 类型而你传入 `long` 整数，你只能得到一半的数据。你传入数据的剩余 32 位会出现在紧随其后的参数中。

### 以正确形式转换 Objective-C 消息

如果你的代码调用 [objc_msgSend](../objectivec/objc_msgsend.md) 函数，或 Objective-C 运行时中发送消息的任何其他类似函数，你需要正确转换。尽管消息函数的原型具有可变参数形式，但 Objective-C 运行时所调用的方法函数并不共享相同的原型。

Objective-C 运行时直接调用实现该方法的函数，因此调用约定不匹配。你必须把 [objc_msgSend](../objectivec/objc_msgsend.md) 函数转换为与被调用方法函数相匹配的原型。

以下代码展示了使用底层消息函数分发消息给对象的正确形式：

```objc
- (int) doSomething:(int) x {
   return x + 2;
}

- (void) doSomethingElse {
    int (*action)(id, SEL, int) = (int (*)(id, SEL, int)) objc_msgSend;
    action(self, @selector(doSomething:), 0);
}
```

在这个示例中，`doSomething:` 方法接受单个参数 `x`，并且不是可变参数形式。在 `doSomethingElse` 中，它使用方法函数的原型来转换 [objc_msgSend](../objectivec/objc_msgsend.md) 函数。注意，方法函数总是把 `id` 变量和选择器作为其前两个参数。把 [objc_msgSend](../objectivec/objc_msgsend.md) 函数转换为名为 `action` 的函数指针后，调用通过同一个函数指针分发。

## 另请参阅

### 内存与指针访问

- [Updating data structures](updating-data-structures.md) — 检查你的 App 的数据设计，并更新它以符合 64 位架构。
- [Auditing pointer usage](auditing-pointer-usage.md) — 确保你的代码中的指针对 64 位运行时是安全的。
