---
title: writeMask
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstencildescriptor/writemask
source_url: 'https://developer.apple.com/documentation/metal/mtlstencildescriptor/writemask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstencildescriptor/writemask.json'
content_hash: 'sha256:6e225f588b6082e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStencilDescriptor](../mtlstencildescriptor.md)

# writeMask

<sub>Instance Property</sub>

A bitmask that determines to which bits that stencil operations can write.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var writeMask: UInt32 { get set }
```

## Discussion

[writeMask](writemask.md) are used for logical AND operations to values that are going to be written into a stencil attachment as the result of a stencil operation.

The least significant bits of the write mask are used. The default value is all ones. A logical AND operation with the default [writeMask](writemask.md) does not change the value.

## See Also

### Configuring stencil bit mask properties

- [readMask](readmask.md) — A bitmask that determines from which bits that stencil comparison tests can read.
