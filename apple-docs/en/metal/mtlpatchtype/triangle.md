---
title: MTLPatchType.triangle
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlpatchtype/triangle
source_url: 'https://developer.apple.com/documentation/metal/mtlpatchtype/triangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlpatchtype/triangle.json'
content_hash: 'sha256:16bcbd1706f43f0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLPatchType](../mtlpatchtype.md)

# MTLPatchType.triangle

<sub>Case</sub>

A triangle patch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case triangle
```

## Discussion

Metal uses this value if the shader is a post-tessellation vertex function with the `[[patch(triangle)]]` attribute.

## See Also

### Patch types

- [MTLPatchTypeNone](none.md) — An option that indicates that this isn’t a post-tessellation vertex function.
- [MTLPatchTypeQuad](quad.md) — A quad patch.
