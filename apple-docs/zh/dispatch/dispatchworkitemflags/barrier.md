---
title: barrier
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchworkitemflags/barrier
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitemflags/barrier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitemflags/barrier.json'
content_hash: 'sha256:04cff8aa94c58e0b'
translated: true
---

> 导航：[技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItemFlags](../dispatchworkitemflags.md)

# barrier

<sub>类型属性</sub>

使工作项在提交到并发队列时充当屏障 block。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let barrier: DispatchWorkItemFlags
```

## 讨论

当提交到并发队列时，带有此标志的工作项充当屏障（barrier）。在屏障之前提交的工作项会执行完毕，此时屏障工作项开始执行。屏障工作项完成后，队列恢复调度在屏障之后提交的工作项。

## 另请参阅

### 工作项标志

- [assignCurrentContext](assigncurrentcontext.md) — 将工作项的属性设置为与当前执行上下文的属性匹配。
- [detached](detached.md) — 将工作项的属性与当前执行上下文分离。
- [enforceQoS](enforceqos.md) — 优先采用与 block 关联的服务质量（QoS）类别。
- [inheritQoS](inheritqos.md) — 优先采用与当前执行上下文关联的服务质量类别。
- [noQoS](noqos.md) — 在执行工作项时不分配服务质量类别。
