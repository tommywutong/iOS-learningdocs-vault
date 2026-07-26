---
title: 'offset(for:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/metal/mtltensorbufferattachments/offset(for:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltensorbufferattachments/offset(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensorbufferattachments/offset%28for%3A%29.json'
content_hash: 'sha256:c03a31a4c5f8ed69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensorBufferAttachments](../mtltensorbufferattachments.md)

# offset(for:)

<sub>Instance Method</sub>

Returns the byte offset into the buffer for the given plane.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func offset(for plane: MTLTensorPlaneType) -> Int
```

## Parameters

- `plane` — The plane type to look up.

## Return Value

The byte offset for the given plane.
