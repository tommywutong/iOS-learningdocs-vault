---
title: MTLPatchType.quad
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpatchtype/quad
source_url: 'https://developer.apple.com/documentation/metal/mtlpatchtype/quad'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpatchtype/quad.json'
content_hash: 'sha256:b194532facc508de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPatchType](../mtlpatchtype.md)

# MTLPatchType.quad

<sub>Case</sub>

A quad patch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case quad
```

## Discussion

Metal uses this value if the shader is a post-tessellation vertex function with the `[[patch(quad)]]` attribute.

## See Also

### Patch types

- [MTLPatchTypeNone](none.md) — An option that indicates that this isn’t a post-tessellation vertex function.
- [MTLPatchTypeTriangle](triangle.md) — A triangle patch.
