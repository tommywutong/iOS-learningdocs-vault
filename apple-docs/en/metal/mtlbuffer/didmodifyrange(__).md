---
title: 'didModifyRange(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 14.0+, macOS 10.11+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlbuffer/didmodifyrange(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffer/didmodifyrange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffer/didmodifyrange%28_%3A%29.json'
content_hash: 'sha256:3f6de0f0b3fd5ce9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBuffer](../mtlbuffer.md)

# didModifyRange(_:)

<sub>Instance Method</sub>

Informs the GPU that the CPU has modified a section of the buffer.

<sub>Mac Catalyst, macOS</sub>

```swift
func didModifyRange(_ range: Range<Int>)
```

## Parameters

- `range` — The range of bytes that have been modified.

## Discussion

If you write information to a buffer created with the [MTLStorageModeManaged](../mtlstoragemode/managed.md) storage mode, you need to call this method to inform the GPU that the information has changed. If you execute GPU commands that read the data without calling this method first, the behavior is undefined.
