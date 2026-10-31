---
title: os_activity_get_identifier
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_get_identifier
source_url: 'https://developer.apple.com/documentation/os/os_activity_get_identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_get_identifier.json'
content_hash: 'sha256:7cfff765415a04ab'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_get_identifier

<sub>函数</sub>

检索给定活动对象的标识符。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern os_activity_id_t os_activity_get_identifier(os_activity_t activity, os_activity_id_t *parent_id);
```

## 参数

- `activity` — 要识别的活动。

- `parent_id` — 返回时，若存在，则包含该活动对象父活动的标识符。如果不需要此标识符，请传入 `NULL`。

## 返回值

当前活动标识符。

## 另请参阅

### 获取活动标识符

- [os_activity_id_t](os_activity_id_t.md) — 唯一标识某个活动的数字。
