---
title: os_activity_set_breadcrumb
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/os/os_activity_set_breadcrumb
source_url: 'https://developer.apple.com/documentation/os/os_activity_set_breadcrumb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_set_breadcrumb.json'
content_hash: 'sha256:f7ab7150c9561826'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_set_breadcrumb

<sub>宏</sub>

将当前活动标记为面包屑（breadcrumb），以表示一个值得关注的事件。

> [!warning] 已废弃
> 请改用 [os_activity_label_useraction](os_activity_label_useraction.md)。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_activity_set_breadcrumb(name)
```

## 参数

- `name` — 描述该面包屑的标签。

## 讨论

使用面包屑来追踪跨越多个活动的交互。请记住，并非所有活动都是值得关注的事件。

此函数对每个活动只能调用一次；后续调用会被忽略。

## 另请参阅

### 已废弃的宏

- [os_activity_start](os_activity_start.md) _(已废弃)_
- [OS_TRACE_TYPE_DEBUG](os_trace_type_debug.md) — 附加调试器时出现的 trace 消息。 _(已废弃)_
- [OS_TRACE_TYPE_INFO](os_trace_type_info.md) — 附加调试器且请求了额外信息时出现的 trace 消息。 _(已废弃)_
- [OS_TRACE_TYPE_RELEASE](os_trace_type_release.md) — 安装到用户设备上的 App 需要捕获的 trace 消息。 _(已废弃)_
