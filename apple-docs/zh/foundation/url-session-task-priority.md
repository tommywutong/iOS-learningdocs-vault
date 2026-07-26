---
title: URL 会话任务优先级
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/url-session-task-priority
source_url: 'https://developer.apple.com/documentation/foundation/url-session-task-priority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url-session-task-priority.json'
content_hash: 'sha256:21d270eb10a5754e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLSessionTask](urlsessiontask.md)

# URL 会话任务优先级

<sub>API 集合</sub>

用于向主机提供任务优先级提示的常量，与 [priority](urlsessiontask/priority.md) 属性配合使用。

## 主题

### Priority constants

- [NSURLSessionTaskPriorityDefault](urlsessiontask/defaultpriority.md) — 默认的 URL 会话任务优先级，对于任何你未设置优先级的任务都会隐式使用该优先级。
- [NSURLSessionTaskPriorityLow](urlsessiontask/lowpriority.md) — 一个较低的 URL 会话任务优先级，其浮点值高于最小值 `0`，低于默认值。
- [NSURLSessionTaskPriorityHigh](urlsessiontask/highpriority.md) — 一个较高的 URL 会话任务优先级，其浮点值高于默认值，低于最大值 `1.0`。

## 另请参阅

### Controlling the task state

- [- cancel](<urlsessiontask/cancel().md>) — 取消该任务。
- [- resume](<urlsessiontask/resume().md>) — 恢复该任务（如果它处于挂起状态）。
- [- suspend](<urlsessiontask/suspend().md>) — 暂时挂起某个任务。
- [state](urlsessiontask/state-swift.property.md) — 该任务的当前状态——活动、挂起、正在被取消或已完成。
- [State](urlsessiontask/state-swift.enum.md) — 用于确定某个任务当前状态的常量。
- [priority](urlsessiontask/priority.md) — 你希望主机处理该任务的相对优先级，指定为介于 `0.0`（最低优先级）到 `1.0`（最高优先级）之间的浮点值。
