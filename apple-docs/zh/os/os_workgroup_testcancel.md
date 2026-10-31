---
title: os_workgroup_testcancel
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_testcancel
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_testcancel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_testcancel.json'
content_hash: 'sha256:ef1c1d4820d3f484'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_testcancel

<sub>函数</sub>

返回一个布尔值，指示工作组是否已取消。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool os_workgroup_testcancel(os_workgroup_t wg);
```

## 参数

- `wg` — 你要取消的工作组。

## 返回值

如果工作组已取消则为 `true`，如果仍处于活动状态则为 `false`。

## 另请参阅

### 取消

- [os_workgroup_cancel](os_workgroup_cancel.md) — 取消并使指定工作组失效。
