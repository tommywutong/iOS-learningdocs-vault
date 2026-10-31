---
title: os_workgroup_cancel
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_workgroup_cancel
source_url: 'https://developer.apple.com/documentation/os/os_workgroup_cancel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_workgroup_cancel.json'
content_hash: 'sha256:0dd95bd55e89fe0a'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_workgroup_cancel

<sub>函数</sub>

取消并使指定工作组失效。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_workgroup_cancel(os_workgroup_t wg);
```

## 参数

- `wg` — 你要取消的工作组。

## 讨论

取消工作组后，不要再在其上调度任何工作。新线程不能加入已取消的工作组，但仍可离开它。对已取消工作组调用的大多数其他工作组 API 会返回相应错误，除此之外不做任何事。

要处理取消，请定期从你的线程代码中调用 [os_workgroup_testcancel](os_workgroup_testcancel.md) 函数，以监视工作组的状态。如果该函数返回 `true`，请停止所有与工作组相关的任务，并调用 `os_workgroup_leave_self` 以将该线程从工作组中移除。取消工作组只影响当前这个工作组本身，不影响其他相关工作组。例如，如果你使用 [os_workgroup_create_with_workgroup](os_workgroup_create_with_workgroup.md) 函数创建了工作组，请分别取消原始工作组及其副本。

## 另请参阅

### 取消

- [os_workgroup_testcancel](os_workgroup_testcancel.md) — 返回一个布尔值，指示工作组是否已取消。
