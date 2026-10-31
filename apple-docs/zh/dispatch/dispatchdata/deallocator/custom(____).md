---
title: 自定义释放器 custom(_:_:)
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchdata/deallocator/custom(_:_:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/deallocator/custom(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/deallocator/custom%28_%3A_%3A%29.json'
content_hash: 'sha256:3ff0e79666f53fca'
translated: true
---

> 导航： [技术](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchData](../../dispatchdata.md) · [Deallocator](../deallocator.md)

# DispatchData.Deallocator.custom(_:_:)

<sub>Case</sub>

使用自定义释放器。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency case custom(DispatchQueue?, @Sendable () -> Void)
```

## 另请参阅

### 释放器

- [DispatchData.Deallocator.free](free.md) — 使用 `free` 释放内存。
- [DispatchData.Deallocator.unmap](unmap.md) — 使用 `munmap` 释放内存。
