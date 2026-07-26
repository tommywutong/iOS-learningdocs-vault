---
title: 'buffer(for:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/metal/mtltensorbufferattachments/buffer(for:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltensorbufferattachments/buffer(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorbufferattachments/buffer%28for%3A%29.json'
content_hash: 'sha256:7708f527664e3c8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorBufferAttachments](../mtltensorbufferattachments.md)

# buffer(for:)

<sub>Instance Method</sub>

Returns the buffer backing the given plane, or `nil` if none has been set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func buffer(for plane: MTLTensorPlaneType) -> (any MTLBuffer)?
```

## Parameters

- `plane` — The plane type to look up.

## Return Value

The buffer for the given plane, or `nil`.
