---
title: 数据争用
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/data-races
source_url: 'https://developer.apple.com/documentation/xcode/data-races'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/data-races.json'
content_hash: 'sha256:9d6096656bda1c10'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 数据争用

<sub>文章</sub>

检测跨多个线程对可变状态（mutable state）未经同步的访问。

## 概述

使用此检查来检测多个线程同时访问同一内存且至少有一个访问是写入的情况。此功能适用于 Xcode 8 及更高版本。

### 包含生产者和消费者函数的数据争用

在以下示例中，`producer()` 函数设置了全局变量 `message`，而 `consumer()` 函数在打印消息前等待一个标志被设置。由于 `producer()` 在一个线程上执行，`consumer()` 在另一个线程上执行，它们的执行可能并发，从而产生数据争用。

```swift
var message: String? = nil
var messageIsAvailable: Bool = false
// 在线程 #1 上执行
func producer() {
    message = "hello!"
    messageIsAvailable = true
}
// 在线程 #2 上执行
func consumer() {
    repeat {
        usleep(1000)
    } while !messageIsAvailable
    print(message)
}
```

#### 解决方案

使用 [Dispatch](../dispatch.md) API 来协调跨多个线程对 `message` 的访问。

## 另请参阅

### Thread Sanitizer

- [Swift 访问争用](swift-access-races.md) — 检测 Swift 中跨多个线程对可变状态未经同步的访问。
- [集合及其他 API 上的争用](races-on-collections-and-other-apis.md) — 检测一个线程访问可变对象而另一个线程正对其进行写入的情况。
- [未初始化的互斥锁](uninitialized-mutexes.md) — 检测你使用了未初始化的互斥锁的情况。
- [线程泄漏](thread-leaks.md) — 检测你在使用后未关闭线程的情况。
