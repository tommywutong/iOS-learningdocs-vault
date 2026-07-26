---
title: 'setDepthStencilStates:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/setdepthstencilstates:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/setdepthstencilstates:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/setdepthstencilstates%3Awithrange%3A.json'
content_hash: 'sha256:89591570a867aee6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# setDepthStencilStates:withRange:

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setDepthStencilStates:(id<MTLDepthStencilState> const[]) depthStencilStates withRange:(NSRange) range;
```

## Discussion

Sets an array of depth stencil states at a given buffer index range
