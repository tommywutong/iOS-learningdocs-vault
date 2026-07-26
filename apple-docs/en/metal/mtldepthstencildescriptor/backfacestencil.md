---
title: backFaceStencil
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldepthstencildescriptor/backfacestencil
source_url: 'https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/backfacestencil'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldepthstencildescriptor/backfacestencil.json'
content_hash: 'sha256:4e91601dedb8bfaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDepthStencilDescriptor](../mtldepthstencildescriptor.md)

# backFaceStencil

<sub>Instance Property</sub>

The stencil descriptor for back-facing primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var backFaceStencil: MTLStencilDescriptor! { get set }
```

## Discussion

The default value is `nil`, which indicates the stencil test is disabled for the back-facing primitives. For more information, see [MTLStencilDescriptor](../mtlstencildescriptor.md).

## See Also

### Specifying stencil descriptors for primitives

- [frontFaceStencil](frontfacestencil.md) — The stencil descriptor for front-facing primitives.
