---
title: empty
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchdata/empty
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/empty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/empty.json'
content_hash: 'sha256:e118a3f547c83769'
translated: true
---

> 导航： [技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# empty

<sub>类型属性</sub>

表示零长度内存区域的 dispatch data 对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let empty: DispatchData
```

## 另请参阅

### 创建 Dispatch Data 结构

- [init(bytes:)](<init(bytes_)-9lrd.md>) — 根据指定的内存缓冲区创建新的 dispatch data 对象。
- [init(bytesNoCopy:deallocator:)](<init(bytesnocopy_deallocator_)-vfoe.md>) — 使用指定的内存缓冲区和释放器创建新的 dispatch data 对象。
- [withUnsafeBytes(body:)](<withunsafebytes(body_).md>)
- [Deallocator](deallocator.md) — dispatch data 对象的内存释放器。
