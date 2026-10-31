---
title: 'async(execute:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchqueue/async(execute:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqueue/async(execute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqueue/async%28execute%3A%29.json'
content_hash: 'sha256:21eb15125ad98e3d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQueue](../dispatchqueue.md)

# async(execute:)

<sub>实例方法</sub>

安排一个工作项立即执行，并立即返回。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func async(execute workItem: DispatchWorkItem)
```

## 参数

- `workItem` — 包含要执行任务的工作项。有关如何创建此工作项的信息，请参阅 [DispatchWorkItem](../dispatchworkitem.md)。

## 另请参阅

### 异步执行任务

- [asyncAfter(deadline:execute:)](<asyncafter(deadline_execute_).md>) — 安排一个工作项在指定时间执行，并立即返回。
- [asyncAfter(deadline:qos:flags:execute:)](<asyncafter(deadline_qos_flags_execute_).md>) — 使用指定属性安排一个 block 执行，并立即返回。
- [asyncAfter(wallDeadline:execute:)](<asyncafter(walldeadline_execute_).md>) — 安排一个工作项在指定时间之后执行，并立即返回。
- [asyncAfter(wallDeadline:qos:flags:execute:)](<asyncafter(walldeadline_qos_flags_execute_).md>) — 使用指定属性安排一个 block 执行，并立即返回。
