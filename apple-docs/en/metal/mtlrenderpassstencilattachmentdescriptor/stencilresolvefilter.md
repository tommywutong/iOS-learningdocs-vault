---
title: stencilResolveFilter
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassstencilattachmentdescriptor/stencilresolvefilter
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassstencilattachmentdescriptor/stencilresolvefilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassstencilattachmentdescriptor/stencilresolvefilter.json'
content_hash: 'sha256:c7f7aa41c7d12f15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassStencilAttachmentDescriptor](../mtlrenderpassstencilattachmentdescriptor.md)

# stencilResolveFilter

<sub>Instance Property</sub>

The filter used for stencil multisample resolve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stencilResolveFilter: MTLMultisampleStencilResolveFilter { get set }
```

## Discussion

The default value is [MTLMultisampleStencilResolveFilterSample0](../mtlmultisamplestencilresolvefilter/sample0.md).
