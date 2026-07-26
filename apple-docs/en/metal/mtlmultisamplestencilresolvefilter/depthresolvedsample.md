---
title: MTLMultisampleStencilResolveFilter.depthResolvedSample
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 14.5+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlmultisamplestencilresolvefilter/depthresolvedsample
source_url: 'https://developer.apple.com/documentation/metal/mtlmultisamplestencilresolvefilter/depthresolvedsample'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlmultisamplestencilresolvefilter/depthresolvedsample.json'
content_hash: 'sha256:bb264120eca27f9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLMultisampleStencilResolveFilter](../mtlmultisamplestencilresolvefilter.md)

# MTLMultisampleStencilResolveFilter.depthResolvedSample

<sub>Case</sub>

Chooses the stencil sample corresponding to the depth sample selected by the depth resolve filter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case depthResolvedSample
```

## Discussion

The resolve filter selects the stencil sample corresponding to the sample that the depth resolve filter would have selected.

## See Also

### Stencil resolve filters

- [MTLMultisampleStencilResolveFilterSample0](sample0.md) — Chooses the first stencil sample in the pixel.
