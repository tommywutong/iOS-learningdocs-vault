---
title: os_signpost_id_make_with_pointer
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_signpost_id_make_with_pointer
source_url: 'https://developer.apple.com/documentation/os/os_signpost_id_make_with_pointer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_signpost_id_make_with_pointer.json'
content_hash: 'sha256:1376b048b3307be0'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_signpost_id_make_with_pointer

<sub>函数</sub>

使用指针值生成唯一值，从而创建一个在记录到指定日志的各 signpost 中唯一的 signpost 标识符。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_signpost_id_t os_signpost_id_make_with_pointer(os_log_t log, const void *ptr);
```

## 讨论

如果活动需要跨越进程边界，请不要使用此函数。

## 另请参阅

### 创建 Signpost 标识符

- [os_signpost_id_generate](os_signpost_id_generate.md) — 创建一个在记录到指定日志的各 signpost 中唯一的 signpost 标识符。
