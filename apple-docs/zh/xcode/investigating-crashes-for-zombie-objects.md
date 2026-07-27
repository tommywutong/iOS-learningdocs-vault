---
title: 调查僵尸对象导致的崩溃
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/investigating-crashes-for-zombie-objects
source_url: 'https://developer.apple.com/documentation/xcode/investigating-crashes-for-zombie-objects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/investigating-crashes-for-zombie-objects.json'
content_hash: 'sha256:4e7a43d18478ec35'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Xcode](../xcode.md) · [Debugging](debugging.md) · [Diagnosing issues using crash reports and device logs](diagnosing-issues-using-crash-reports-and-device-logs.md) · [Identifying the cause of common crashes](identifying-the-cause-of-common-crashes.md)

# 调查僵尸对象导致的崩溃

<sub>文章</sub>

识别僵尸对象的特征，并调查崩溃的原因。

## 概述

一旦 Objective-C 或 Swift 对象不再有任何强引用指向它，该对象就会被释放。如果继续向该对象发送消息，就好像它仍是有效对象一样，这是一种「释放后使用」（use after free）问题，仍在接收消息的已释放对象被称为 _僵尸对象（zombie object）_。

### 判断崩溃报告中是否有僵尸迹象

Objective-C 运行时无法向已从内存释放的对象发送消息，因此崩溃常常发生在 [objc_msgSend](../objectivec/objc_msgsend.md)、`objc_retain` 或 `objc_release` 函数中。例如，当 Objective-C 运行时无法向已释放的对象发送消息时，崩溃看起来会是这样：

```other
Thread 0 Crashed:
0   libobjc.A.dylib                   0x00000001a186d190 objc_msgSend + 16
1   Foundation                        0x00000001a1f31238 __NSThreadPerformPerform + 232
2   CoreFoundation                    0x00000001a1ac67e0 __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 24
```

再举一个例子，Objective-C 运行时试图释放一个已经释放过的对象：

```other
Thread 2 Crashed:
0   libobjc.A.dylib                 0x00007fff7478bd5c objc_release + 28
1   libobjc.A.dylib                 0x00007fff7478cc8c (anonymous namespace)::AutoreleasePoolPage::pop(void*) + 726
2   com.apple.CoreFoundation        0x00007fff485feee6 _CFAutoreleasePoolPop + 22
```

另一种表明存在僵尸对象的模式，是出现一个 _无法识别的选择器（unrecognized selector）_ 的栈帧，也就是对象没有实现的方法。这类崩溃通常看起来像是某个意料之外类型的对象被要求做一件它显然做不到的事，例如一个数字格式化器类去尝试播放声音。这是因为操作系统重用了曾经保存已释放对象的那块内存，而这块内存现在保存的是另一种类型的对象。通过无法识别的选择器识别出的僵尸对象，其调用栈中会包含 [doesNotRecognizeSelector(_:)](<../objectivec/nsobject-swift.class/doesnotrecognizeselector(__).md>) 方法：

```other
Last Exception Backtrace:
0   CoreFoundation                    0x1bf596a48 __exceptionPreprocess + 220
1   libobjc.A.dylib                   0x1bf2bdfa4 objc_exception_throw + 55
2   CoreFoundation                    0x1bf49a5a8 -[NSObject+ 193960 (NSObject) doesNotRecognizeSelector:] + 139
```

如果你在调试时重现了这样的崩溃，控制台日志会显示更多信息：

```other
Terminating app due to uncaught exception 'NSInvalidArgumentException',
    reason: '-[NSNumberFormatter playSound]: 
    unrecognized selector sent to instance 0x28360dac0'
```

在这个例子中，一条消息被发送给了一个 [NumberFormatter](../foundation/numberformatter.md)，让它执行 `playSound` 选择器，但 [NumberFormatter](../foundation/numberformatter.md) 并没有实现这个名字的方法，于是 App 崩溃了。此前曾有一个对象分配在与当前 [NumberFormatter](../foundation/numberformatter.md) 相同的内存地址上，那个对象实现了 `playSound` 方法，但它已经被释放，如今这个不相关的 [NumberFormatter](../foundation/numberformatter.md) 对象正在使用同一个内存地址。`playSound` 选择器是调试的一条线索。如果你能确定实现了 `playSound` 选择器的类，就可以找出调用它的代码路径，从而确定为什么预期的对象过早被释放了。

### 调查僵尸对象的来源

在因僵尸对象导致崩溃的情况下，回溯记录中可能会有来自 App 的栈帧，但并非总是如此。即使回溯记录中没有任何帧引用你 App 中的代码，你的代码也参与制造了这个僵尸对象，因此要使用 Zombies 工具来调查僵尸对象的来源，具体做法参见 [Finding zombies](https://help.apple.com/instruments/mac/current/#/dev612e6956)。在使用 Zombies 工具时，寻找以下问题的答案，这样你就能获得修改代码、消除僵尸对象所需的信息：

- 已释放对象的类型是什么，向它发送了什么消息？
- 该对象实际是在什么时候被释放的？
- 该对象在释放之后是如何被使用的？

在修改代码时，请留意所涉及对象的预期生命周期。考虑哪些对象使用强引用，哪些对象使用弱引用或无主引用，从而确保对象只有在不再需要时才会被释放，而不会过早释放。有关 Objective-C 中自动引用计数的信息，请参阅 [ARC Overview](https://developer.apple.com/library/archive/releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011226-CH1-SW13)；有关 Swift 中的相关信息，请参阅 [Swift documentation](https://docs.swift.org/swift-book/LanguageGuide/AutomaticReferenceCounting.html)。

## 另请参阅

### 相关文档

- [Analyzing a crash report](analyzing-a-crash-report.md) — 在崩溃报告中识别线索，帮助你诊断问题。

### 内存访问错误

- [Investigating memory access crashes](investigating-memory-access-crashes.md) — 识别因内存访问问题引发的崩溃，并调查崩溃原因。
