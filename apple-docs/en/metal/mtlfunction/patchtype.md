---
title: patchType
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunction/patchtype
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/patchtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/patchtype.json'
content_hash: 'sha256:947b87165e3e2892'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# patchType

<sub>Instance Property</sub>

The tessellation patch type of a post-tessellation vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var patchType: MTLPatchType { get }
```

## Discussion

This value is [MTLPatchTypeNone](../mtlpatchtype/none.md) if the function isn’t a post-tessellation vertex function.

## See Also

### Identifying the tessellation patch

- [patchControlPointCount](patchcontrolpointcount.md) — The number of patch control points in the post-tessellation vertex function.
- [MTLPatchType](../mtlpatchtype.md) — Types of tessellation patches that can be inputs of a post-tessellation vertex function.
