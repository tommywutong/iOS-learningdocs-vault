---
title: 'didModifyRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlbuffer/didmodifyrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlbuffer/didmodifyrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlbuffer/didmodifyrange%3A.json'
content_hash: 'sha256:0ccef16f424aeceb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBuffer](../mtlbuffer.md)

# didModifyRange:

<sub>Instance Method</sub>

Informs the GPU that the CPU has modified a section of the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) didModifyRange:(NSRange) range;
```

## Parameters

- `range` — The range of bytes that were modified.

## Discussion

If you write information to a buffer created with the [MTLStorageModeManaged](../mtlstoragemode/managed.md) storage mode, you need to call this method to inform the GPU that the information has changed. If you execute GPU commands that read from the modified sections without calling this method first, the behavior is undefined.
