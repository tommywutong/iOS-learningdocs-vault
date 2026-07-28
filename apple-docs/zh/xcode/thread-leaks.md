---
title: 线程泄漏
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/thread-leaks
source_url: 'https://developer.apple.com/documentation/xcode/thread-leaks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/thread-leaks.json'
content_hash: 'sha256:0a8df807d1ce29e8'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 线程泄漏

<sub>文章</sub>

检测使用线程后未将其关闭的情况。

## 概述

使用此项检查来检测通过 `pthread_create(_:_:_:_:)` 函数创建、但没有相应调用 `pthread_join(_:_:)` 函数的线程。泄漏的线程可能导致性能下降，并可能引发崩溃。此项检查在 Xcode 8 及后续版本中可用。

### C 中的线程泄漏

在以下示例中，代码创建了一个 `thread` 变量，但使用后没有将其关闭：

```occ
void *run(){
    pthread_exit(0);
}
pthread_t thread;
pthread_create(&thread, NULL, run, NULL); // 错误：线程泄漏
sleep(1);
```

#### 解决方案

添加对 `pthread_join(_:_:)` 函数的调用。

```swift
void *run(){
    pthread_exit(0);
}
pthread_t thread;
pthread_create(&thread, NULL, run, NULL);
sleep(1);
pthread_join(thread, NULL); // 正确
```

或者，可以将 `PTHREAD_CREATE_DETACHED` 特性（attribute）传给 `pthread_create(_:_:_:_:)` 来创建分离线程，也可以在线程创建后对其调用 `pthread_detach(_:)`。

## 另请参阅

### Thread Sanitizer

- [数据争用（data race）](data-races.md) — 检测多个线程间对可变状态（mutable state）的未同步访问。
- [Swift 访问争用](swift-access-races.md) — 检测 Swift 中多个线程间对可变状态的未同步访问。
- [集合及其他 API 上的争用](races-on-collections-and-other-apis.md) — 检测一个线程访问可变对象、同时另一线程正在写入该对象的情况。
- [未初始化的互斥锁](uninitialized-mutexes.md) — 检测使用未初始化互斥锁的情况。
