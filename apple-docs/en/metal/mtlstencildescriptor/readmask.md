---
title: readMask
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstencildescriptor/readmask
source_url: 'https://developer.apple.com/documentation/metal/mtlstencildescriptor/readmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstencildescriptor/readmask.json'
content_hash: 'sha256:d9cf98ca0c0292da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStencilDescriptor](../mtlstencildescriptor.md)

# readMask

<sub>Instance Property</sub>

A bitmask that determines from which bits that stencil comparison tests can read.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var readMask: UInt32 { get set }
```

## Discussion

The [readMask](readmask.md) bits are used for logical AND operations to both the stored stencil value and the reference value.

The least significant bits of the read mask are used. The default value is all ones. A logical AND operation with the default [readMask](readmask.md) does not change the value.

## See Also

### Related Documentation

- [- setStencilReferenceValue:](<../mtlrendercommandencoder/setstencilreferencevalue(__).md>) — Configures the same comparison value for front- and back-facing primitives.

### Configuring stencil bit mask properties

- [writeMask](writemask.md) — A bitmask that determines to which bits that stencil operations can write.
