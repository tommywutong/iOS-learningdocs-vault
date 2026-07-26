---
title: depthResolveFilter
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpassdepthattachmentdescriptor/depthresolvefilter
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpassdepthattachmentdescriptor/depthresolvefilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpassdepthattachmentdescriptor/depthresolvefilter.json'
content_hash: 'sha256:f6e4b5622576a7b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPassDepthAttachmentDescriptor](../mtlrenderpassdepthattachmentdescriptor.md)

# depthResolveFilter

<sub>Instance Property</sub>

The filter used for an MSAA depth resolve operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var depthResolveFilter: MTLMultisampleDepthResolveFilter { get set }
```

## Discussion

The default value is [MTLMultisampleDepthResolveFilterSample0](../mtlmultisampledepthresolvefilter/sample0.md).
