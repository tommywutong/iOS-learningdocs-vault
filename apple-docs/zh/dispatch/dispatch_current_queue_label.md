---
title: DISPATCH_CURRENT_QUEUE_LABEL
framework: Dispatch
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_current_queue_label
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_current_queue_label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_current_queue_label.json'
content_hash: 'sha256:a6ebce0a6ececd22'
translated: true
---

> 导航： [技术](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_CURRENT_QUEUE_LABEL

<sub>宏</sub>

将此常量传给 [dispatch_queue_get_label](dispatch_queue_get_label.md) 函数以检索当前队列的标签。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define DISPATCH_CURRENT_QUEUE_LABEL
```

## 另请参阅

### 管理队列特性

- [dispatch_queue_get_label](dispatch_queue_get_label.md) — 返回你在创建时为该 dispatch queue 分配的标签。
- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — 指定在其上执行与当前对象关联的工作的 dispatch queue。
