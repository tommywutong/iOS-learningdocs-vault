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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchData](../dispatchdata.md)

# init(bytes:)

<sub>Initializer</sub>

Initialize a data object with copied memory content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytes buffer: UnsafeBufferPointer<UInt8>)
```

## Parameters

- `buffer` — A pointer to the memory. It will be copied.

## See Also

### Deprecated

- [init(bytesNoCopy:deallocator:)](<init(bytesnocopy_deallocator_)-7h08w.md>) — Initialize a data object without copying the bytes.
- [append(_:count:)](<append(__count_).md>)
- [copyBytes(to:count:)](<copybytes(to_count_)-4ffyj.md>)
- [copyBytes(to:from:)](<copybytes(to_from_)-6ztcb.md>)
