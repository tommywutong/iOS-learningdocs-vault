---
title: stepRate
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexbufferlayoutdescriptor/steprate
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor/steprate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexbufferlayoutdescriptor/steprate.json'
content_hash: 'sha256:c37ab05ad3723ae2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexBufferLayoutDescriptor](../mtlvertexbufferlayoutdescriptor.md)

# stepRate

<sub>Instance Property</sub>

The interval at which the vertex and its attributes are presented to the vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stepRate: Int { get set }
```

## Discussion

The default value is `1`. The `stepRate` value, in conjunction with the [stepFunction](stepfunction.md) property, determines how often the function fetches new attribute data. The `stepRate` property is generally used when `stepFunction` is [MTLVertexStepFunctionPerInstance](../mtlvertexstepfunction/perinstance.md). If `stepRate` is equal to `1`, new attribute data is fetched for every instance; if `stepRate` is equal to `2`, new attribute data is fetched for every two instances, and so forth.

## See Also

### Organizing the vertex buffer layout

- [stepFunction](stepfunction.md) — The circumstances under which the vertex and its attributes are presented to the vertex function.
- [stride](stride.md) — The number of bytes between the first byte of two consecutive vertices in a buffer.
- [MTLVertexStepFunction](../mtlvertexstepfunction.md) — The frequency with which the vertex function or post-tessellation vertex function fetches attribute data.
