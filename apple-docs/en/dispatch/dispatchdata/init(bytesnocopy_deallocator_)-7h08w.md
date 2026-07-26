---
title: 'init(bytesNoCopy:deallocator:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS, Swift（4.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/dispatch/dispatchdata/init(bytesnocopy:deallocator:)-7h08w'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytesnocopy:deallocator:)-7h08w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/init%28bytesnocopy%3Adeallocator%3A%29-7h08w.json'
content_hash: 'sha256:b98ecd3e0d1ab3a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# init(bytesNoCopy:deallocator:)

<sub>Initializer</sub>

Initialize a data object without copying the bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytesNoCopy bytes: UnsafeBufferPointer<UInt8>, deallocator: DispatchData.Deallocator = .free)
```

## Parameters

- `bytes` — A pointer to the bytes.

- `deallocator` — Specifies the mechanism to free the indicated buffer.

## See Also

### Deprecated

- [init(bytes:)](<init(bytes_)-mkbp.md>) — Initialize a data object with copied memory content.
- [append(_:count:)](<append(__count_).md>)
- [copyBytes(to:count:)](<copybytes(to_count_)-4ffyj.md>)
- [copyBytes(to:from:)](<copybytes(to_from_)-6ztcb.md>)
