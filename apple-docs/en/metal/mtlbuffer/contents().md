---
title: contents()
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlbuffer/contents()
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffer/contents()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffer/contents%28%29.json'
content_hash: 'sha256:cec5af993e29c345'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBuffer](../mtlbuffer.md)

# contents()

<sub>Instance Method</sub>

Gets the system address of the buffer’s storage allocation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func contents() -> UnsafeMutableRawPointer
```

## Return Value

A pointer to the shared copy of the buffer data, or `NULL` for buffers allocated with a private resource storage mode ([MTLStorageModePrivate](../mtlstoragemode/private.md)).

## Discussion

Private resources aren’t CPU-accessible.
