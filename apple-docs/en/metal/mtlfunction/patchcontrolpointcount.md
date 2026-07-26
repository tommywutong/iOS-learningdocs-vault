---
title: patchControlPointCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlfunction/patchcontrolpointcount
source_url: 'https://developer.apple.com/documentation/metal/mtlfunction/patchcontrolpointcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunction/patchcontrolpointcount.json'
content_hash: 'sha256:ff02d354fc4a4f06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunction](../mtlfunction.md)

# patchControlPointCount

<sub>Instance Property</sub>

The number of patch control points in the post-tessellation vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var patchControlPointCount: Int { get }
```

## Discussion

This value is `-1` if the number of patch control points wasn’t specified or if the function isn’t a post-tessellation vertex function.

## See Also

### Identifying the tessellation patch

- [patchType](patchtype.md) — The tessellation patch type of a post-tessellation vertex function.
- [MTLPatchType](../mtlpatchtype.md) — Types of tessellation patches that can be inputs of a post-tessellation vertex function.
