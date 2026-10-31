---
title: os_function_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_function_t
source_url: 'https://developer.apple.com/documentation/os/os_function_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_function_t.json'
content_hash: 'sha256:0bec1abd34f72e7e'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_function_t

<sub>类型别名</sub>

指向函数的指针。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef void (*)(void *) os_function_t;
```

## 另请参阅

### 内存

- [os_proc_available_memory](os_proc_available_memory.md) — 确定当前 App 的可用内存量。
- [os_block_t](os_block_t.md) — 一个不接受参数且无返回值的 block。
- [os_release](os_release-c.func.md)
- [os_retain](os_retain-c.func.md)
