---
title: distantFuture
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchtime/distantfuture
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchtime/distantfuture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchtime/distantfuture.json'
content_hash: 'sha256:d2795ac00ba9fa8e'
translated: true
---

> 导航： [技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchTime](../dispatchtime.md)

# distantFuture

<sub>类型属性</sub>

遥远未来的某个时间。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let distantFuture: DispatchTime
```

## 讨论

你可以将此值传给安排工作的方法，让系统无限期等待特定事件发生或条件满足。

## 另请参阅

### 获取常用时间

- [now()](<now().md>) — 返回当前时间。
