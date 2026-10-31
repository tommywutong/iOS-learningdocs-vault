---
title: handle
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchsourceprotocol/handle
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/handle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/handle.json'
content_hash: 'sha256:7a67e1de629c920b'
translated: true
---

> 导航： [技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# handle

<sub>实例属性</sub>

返回与指定 dispatch source 关联的底层系统句柄。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var handle: UInt { get }
```

## 另请参阅

### 获取 Dispatch Source 特性

- [data](data.md) — 返回该 dispatch source 的挂起数据。
- [mask](mask.md) — 返回该 dispatch source 所监视事件的掩码。
