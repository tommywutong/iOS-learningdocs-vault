---
title: dispatch_semaphore_signal
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_semaphore_signal
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_semaphore_signal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_semaphore_signal.json'
content_hash: 'sha256:83f0c03fa7b650dc'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_semaphore_signal

<sub>函数</sub>

对信号量发信号（递增）。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern intptr_t dispatch_semaphore_signal(dispatch_semaphore_t dsema);
```

## 返回值

如果先前的值小于零，此函数会唤醒当前正在等待的进程。

## 讨论

递增计数信号量。如果先前的值小于零，此函数会唤醒当前在 [dispatch_semaphore_wait](dispatch_semaphore_wait.md) 中等待的线程。
