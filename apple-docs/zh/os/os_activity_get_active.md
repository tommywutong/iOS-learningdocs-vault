---
title: os_activity_get_active
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.12 起废弃）, tvOS 9.0+（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_activity_get_active
source_url: 'https://developer.apple.com/documentation/os/os_activity_get_active'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_get_active.json'
content_hash: 'sha256:43ad463112235cbc'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_get_active

<sub>函数</sub>

返回与当前线程关联的嵌套活动栈。

> [!warning] 已废弃
> 此函数不再受支持，且没有替代方案。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern unsigned int os_activity_get_active(os_activity_id_t *entries, unsigned int *count);
```

## 参数

- `entries` — 大小足以容纳所请求活动数量的缓冲区。

- `count` — 所请求的活动数量。

## 返回值

写入 `entries` 的活动数量。

## 讨论

由于活动可以嵌套，当前线程上可能涉及多个活动。

此函数应仅由诊断工具使用，以便对某种情况进行额外判定。

## 另请参阅

### 已废弃的函数

- [os_log_is_enabled](os_log_is_enabled.md) _(已废弃)_
- [os_log_is_debug_enabled](os_log_is_debug_enabled.md) _(已废弃)_
- [os_activity_end](os_activity_end.md) — 结束当前线程上的指定活动。 _(已废弃)_
- [os_trace_debug_enabled](<os_trace_debug_enabled().md>) — 返回是否已启用 debug 级别的 trace 信息。 _(已废弃)_
- [os_trace_info_enabled](<os_trace_info_enabled().md>) — 返回是否已启用 info 级别的 trace 信息。 _(已废弃)_
- [os_trace_type_enabled](<os_trace_type_enabled(__).md>) — 返回是否已启用指定的 info 级别 trace 信息。 _(已废弃)_
