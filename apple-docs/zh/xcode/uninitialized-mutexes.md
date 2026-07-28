---
title: 未初始化的互斥锁
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/uninitialized-mutexes
source_url: 'https://developer.apple.com/documentation/xcode/uninitialized-mutexes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/uninitialized-mutexes.json'
content_hash: 'sha256:c0d160c990784bd5'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 未初始化的互斥锁

<sub>文章</sub>

检测你何时使用了未初始化的互斥锁。

## 概述

使用此项检查来检测你何时使用未初始化的 `pthread_mutex_t` 变量调用 `pthread_mutex_lock(_:)` 或 `pthread_mutex_unlock(_:)`。尝试使用未初始化的互斥锁（mutex）会导致错误，并绕过已锁定互斥锁上存在的顺序条件。此项检查在 Xcode 8 及更高版本中可用。

### 在 C 中使用未初始化的互斥锁

在以下示例中，`pthread_mutex_lock(_:)` 函数使用未初始化的 `pthread_mutex_t` 变量执行：

```occ
static pthread_mutex_t mutex;
void performWork() {
    pthread_mutex_lock(&mutex); // 错误：互斥锁未初始化
    // ...
    pthread_mutex_unlock(&mutex);
}
```

#### 解决方案

使用 `pthread_once(_:_:)` 函数在使用互斥锁之前对其进行初始化。

```occ
static pthread_once_t once = PTHREAD_ONCE_INIT;
static pthread_mutex_t mutex;
void init() {    
    pthread_mutex_init(&mutex, NULL);
}
void performWork() {
    pthread_once(&once, init); // 正确
    pthread_mutex_lock(&mutex);
    // ...
    pthread_mutex_unlock(&mutex);
}
```

## 另请参阅

### Thread Sanitizer

- [数据争用](data-races.md) — 检测多个线程对可变状态（mutable state）进行的未同步访问。
- [Swift 访问争用](swift-access-races.md) — 检测 Swift 中多个线程对可变状态进行的未同步访问。
- [集合和其他 API 上的争用](races-on-collections-and-other-apis.md) — 检测一个线程访问可变对象、另一个线程同时写入该对象的情况。
- [线程泄漏](thread-leaks.md) — 检测你在使用线程后未将其关闭的情况。
