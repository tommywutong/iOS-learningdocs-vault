---
title: frontFaceStencil
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldepthstencildescriptor/frontfacestencil
source_url: 'https://developer.apple.com/documentation/metal/mtldepthstencildescriptor/frontfacestencil'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldepthstencildescriptor/frontfacestencil.json'
content_hash: 'sha256:cb8d3926ea96078e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDepthStencilDescriptor](../mtldepthstencildescriptor.md)

# frontFaceStencil

<sub>Instance Property</sub>

The stencil descriptor for front-facing primitives.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@NSCopying var frontFaceStencil: MTLStencilDescriptor! { get set }
```

## Discussion

The default value is `nil`, which indicates the stencil test is disabled for the front-facing primitives. For more information, see [MTLStencilDescriptor](../mtlstencildescriptor.md).

## See Also

### Specifying stencil descriptors for primitives

- [backFaceStencil](backfacestencil.md) — The stencil descriptor for back-facing primitives.
