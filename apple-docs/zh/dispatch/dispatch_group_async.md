---
title: dispatch_group_async
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_group_async
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_group_async'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_group_async.json'
content_hash: 'sha256:c67d1df5daed5e34'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_group_async

<sub>函数</sub>

异步安排一个 block 执行，并同时将其与指定的 dispatch group 关联。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_group_async(dispatch_group_t group, dispatch_queue_t queue, dispatch_block_t block);
```

## 参数

- `group` — 要与所提交 block 对象关联的 dispatch group。系统会保留该 group，直到该 block 运行完成。此参数不能为 `NULL`。

- `queue` — 将该 block 对象提交到其上以进行异步调用的 dispatch queue。系统会保留该队列，直到该 block 运行完成。此参数不能为 `NULL`。

- `block` — 要异步执行的 block 对象。此函数会代表调用方执行 `Block_copy` 和 `Block_release`。

## 讨论

将一个 block 提交到某个 dispatch queue，并将该 block 对象与给定的 dispatch group 关联。该 dispatch group 可用于等待它所引用的 block 对象完成。

## 另请参阅

### 向组添加工作

- [dispatch_group_async_f](dispatch_group_async_f.md) — 将一个应用程序定义的函数提交到某个 dispatch queue，并将其与指定的 dispatch group 关联。
