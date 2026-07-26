---
title: MTLVertexStepFunction
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlvertexstepfunction
source_url: 'https://developer.apple.com/documentation/metal/mtlvertexstepfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlvertexstepfunction.json'
content_hash: 'sha256:b810fb7df7575b77'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLVertexStepFunction

<sub>Enumeration</sub>

The frequency with which the vertex function or post-tessellation vertex function fetches attribute data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLVertexStepFunction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Step functions

- [MTLVertexStepFunctionConstant](mtlvertexstepfunction/constant.md) — The vertex function fetches attribute data once and uses that data for every vertex.
- [MTLVertexStepFunctionPerVertex](mtlvertexstepfunction/pervertex.md) — The vertex function fetches and uses new attribute data for every vertex.
- [MTLVertexStepFunctionPerInstance](mtlvertexstepfunction/perinstance.md) — The vertex function regularly fetches new attribute data for a number of instances that is determined by `stepRate`.
- [MTLVertexStepFunctionPerPatch](mtlvertexstepfunction/perpatch.md) — The post-tessellation vertex function fetches data based on the patch index of the patch.
- [MTLVertexStepFunctionPerPatchControlPoint](mtlvertexstepfunction/perpatchcontrolpoint.md) — The post-tessellation vertex function fetches data based on the control-point indices associated with the patch.

### Initializers

- [init(rawValue:)](<mtlvertexstepfunction/init(rawvalue_).md>)

## See Also

### Organizing the vertex buffer layout

- [stepFunction](mtlvertexbufferlayoutdescriptor/stepfunction.md) — The circumstances under which the vertex and its attributes are presented to the vertex function.
- [stepRate](mtlvertexbufferlayoutdescriptor/steprate.md) — The interval at which the vertex and its attributes are presented to the vertex function.
- [stride](mtlvertexbufferlayoutdescriptor/stride.md) — The number of bytes between the first byte of two consecutive vertices in a buffer.
