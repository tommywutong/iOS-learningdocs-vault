---
title: os_activity_end
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.12 起废弃）, tvOS 9.0+（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_activity_end
source_url: 'https://developer.apple.com/documentation/os/os_activity_end'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_end.json'
content_hash: 'sha256:68cb6ab8fbc09de7'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_end

<sub>函数</sub>

结束当前线程上的指定活动。

> [!warning] 已废弃
> 请改用 [os_activity_create](os_activity_create.md) 和 [os_activity_apply](os_activity_apply.md)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_activity_end(os_activity_t activity);
```

## 参数

- `activity` — 要结束的活动。

## 讨论

调用此函数仅表示发起方已从该活动重新获得控制权。与该活动相关的工作在调用此函数时可能仍在进行中。

## 另请参阅

### 已废弃的函数

- [os_log_is_enabled](os_log_is_enabled.md) _(已废弃)_
- [os_log_is_debug_enabled](os_log_is_debug_enabled.md) _(已废弃)_
- [os_activity_get_active](os_activity_get_active.md) — 返回与当前线程关联的嵌套活动栈。 _(已废弃)_
- [os_trace_debug_enabled](<os_trace_debug_enabled().md>) — 返回是否已启用 debug 级别的 trace 信息。 _(已废弃)_
- [os_trace_info_enabled](<os_trace_info_enabled().md>) — 返回是否已启用 info 级别的 trace 信息。 _(已废弃)_
- [os_trace_type_enabled](<os_trace_type_enabled(__).md>) — 返回是否已启用指定的 info 级别 trace 信息。 _(已废弃)_
