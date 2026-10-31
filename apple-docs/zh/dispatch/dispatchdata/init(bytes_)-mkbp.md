---
title: 'init(bytes:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS, Swift（4.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/dispatch/dispatchdata/init(bytes:)-mkbp'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytes:)-mkbp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/init%28bytes%3A%29-mkbp.json'
content_hash: 'sha256:8b94f560e5bab5d0'
translated: true
---

> 导航： [技术](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# init(bytes:)

<sub>初始化方法</sub>

使用复制的内存内容初始化数据对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytes buffer: UnsafeBufferPointer<UInt8>)
```

## 参数

- `buffer` — 指向内存的指针。将对其进行复制。

## 另请参阅

### 已废弃

- [init(bytesNoCopy:deallocator:)](<init(bytesnocopy_deallocator_)-7h08w.md>) — 初始化数据对象而不复制字节。
- [append(_:count:)](<append(__count_).md>)
- [copyBytes(to:count:)](<copybytes(to_count_)-4ffyj.md>)
- [copyBytes(to:from:)](<copybytes(to_from_)-6ztcb.md>)
