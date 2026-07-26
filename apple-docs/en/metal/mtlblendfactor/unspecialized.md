---
title: MTLBlendFactor.unspecialized
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblendfactor/unspecialized
source_url: 'https://developer.apple.com/documentation/metal/mtlblendfactor/unspecialized'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblendfactor/unspecialized.json'
content_hash: 'sha256:d21ddccb54213691'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlendFactor](../mtlblendfactor.md)

# MTLBlendFactor.unspecialized

<sub>Case</sub>

Defers assigning the blend factor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case unspecialized
```

## Discussion

Until you specialize this value in the pipeline state, it:

- behaves as `MTLBlendFactorOne` for `sourceRGBBlendFactor` and `sourceAlphaBlendFactor`
- behaves as `MTLBlendFactorZero` for `destinationRGBBlendFactor` and `destinationAlphaBlendFactor`
