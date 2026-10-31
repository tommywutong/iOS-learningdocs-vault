---
title: 'withUnsafeBytes(body:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchdata/withunsafebytes(body:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/withunsafebytes(body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/withunsafebytes%28body%3A%29.json'
content_hash: 'sha256:258a0f4ae5078ec5'
translated: true
---

> 导航： [技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# withUnsafeBytes(body:)

<sub>实例方法</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result
```

## 另请参阅

### 创建 Dispatch Data 结构

- [init(bytes:)](<init(bytes_)-9lrd.md>) — 根据指定的内存缓冲区创建新的 dispatch data 对象。
- [init(bytesNoCopy:deallocator:)](<init(bytesnocopy_deallocator_)-vfoe.md>) — 使用指定的内存缓冲区和释放器创建新的 dispatch data 对象。
- [Deallocator](deallocator.md) — dispatch data 对象的内存释放器。
- [empty](empty.md) — 表示零长度内存区域的 dispatch data 对象。
