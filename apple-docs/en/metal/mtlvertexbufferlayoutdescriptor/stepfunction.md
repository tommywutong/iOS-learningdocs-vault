---
title: stepFunction
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexbufferlayoutdescriptor/stepfunction
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor/stepfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexbufferlayoutdescriptor/stepfunction.json'
content_hash: 'sha256:827cebb689f485a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLVertexBufferLayoutDescriptor](../mtlvertexbufferlayoutdescriptor.md)

# stepFunction

<sub>Instance Property</sub>

The circumstances under which the vertex and its attributes are presented to the vertex function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var stepFunction: MTLVertexStepFunction { get set }
```

## Discussion

The default value is [MTLVertexStepFunctionPerVertex](../mtlvertexstepfunction/pervertex.md).

If `stepFunction` is [MTLVertexStepFunctionPerVertex](../mtlvertexstepfunction/pervertex.md), the function fetches new attribute data based on the `[[ vertex_id ]]` attribute qualifier. The function fetches new attribute data each time a new vertex is processed. In this case, `stepRate` needs to be set to `1`, which is its default value.

If `stepFunction` is [MTLVertexStepFunctionPerInstance](../mtlvertexstepfunction/perinstance.md), the function fetches new attribute data based on the `[[ instance_id ]]` attribute qualifier.  In this case, `stepRate` needs to be greater than `0` and its value determines how often the function fetches new attribute data.

If `stepFunction` is [MTLVertexStepFunctionConstant](../mtlvertexstepfunction/constant.md), the function fetches attribute data just once, and that attribute data is used for every vertex. In this case,`stepRate` needs to be set to `0`.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Organizing the vertex buffer layout

- [stepRate](steprate.md) — The interval at which the vertex and its attributes are presented to the vertex function.
- [stride](stride.md) — The number of bytes between the first byte of two consecutive vertices in a buffer.
- [MTLVertexStepFunction](../mtlvertexstepfunction.md) — The frequency with which the vertex function or post-tessellation vertex function fetches attribute data.
