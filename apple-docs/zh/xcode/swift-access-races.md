---
title: Swift 访问竞态
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/swift-access-races
source_url: 'https://developer.apple.com/documentation/xcode/swift-access-races'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/swift-access-races.json'
content_hash: 'sha256:9b70a8c364c9d4aa'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# Swift 访问竞态

<sub>文章</sub>

检测 Swift 中跨多个线程对可变状态的未同步访问。

## 概述

使用此检查来检测多个线程何时调用结构体上的可变方法，或者何时在不同步的情况下传递对共享变量的引用，因为这可能导致不可预测的行为。此功能在 Xcode 9 及更高版本中可用。

### 使用结构体可变方法时的访问竞态

在以下示例中，`producer()` 函数向全局数组添加消息，`consumer()` 函数从数组中移除消息并打印。由于 `producer()` 在一个线程上执行，而 `consumer()` 在另一个线程上执行，并且两者都调用数组的可变方法，因此 `messages` 上存在访问竞态。

```swift
var messages: [String] = []
// 在线程 #1 上执行
func producer() {
    messages.append("A message");
}
// 在线程 #2 上执行
func consumer() {
    repeat {
        let message = messages.remove(at: 0)
        print("\(message)")
    } while !messages.isEmpty
}
```

#### 解决方案

使用 [Dispatch](../dispatch.md) API 协调多个线程对 `messages` 的访问。

### 使用 inout 参数时的访问竞态

在以下示例中，`writeNumbers()` 函数将数字写入全局字符串。`writeLetters()` 函数将字母写入同一个字符串。由于这两个函数在不同线程上执行，并且都使用 `inout` 通过引用访问 `log`，因此 `log` 上存在访问竞态。

```swift
var log: String = ""
// 在线程 #1 上执行
func writeNumbers() {
    print(1, 2, 3, separator: ",", to: &log)
}
// 在线程 #2 上执行
func writeLetters() {
    print("a", "b", "c", separator:",", to: &log)
}
```

#### 解决方案

使用 [Dispatch](../dispatch.md) API 协调多个线程对 `log` 的访问。

## 另请参阅

### 线程消毒器

- [数据争用](data-races.md) — 检测跨多个线程对可变状态的未同步访问。
- [集合和其他 API 上的竞态](races-on-collections-and-other-apis.md) — 检测一个线程访问可变对象、同时另一个线程正在写入该对象的情况。
- [未初始化的互斥锁](uninitialized-mutexes.md) — 检测使用未初始化互斥锁的情况。
- [线程泄漏](thread-leaks.md) — 检测使用线程后未将其关闭的情况。
