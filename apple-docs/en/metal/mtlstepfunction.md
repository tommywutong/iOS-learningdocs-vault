---
title: MTLStepFunction
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstepfunction
source_url: 'https://developer.apple.com/documentation/metal/mtlstepfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstepfunction.json'
content_hash: 'sha256:7461cfb39e2f2b12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLStepFunction

<sub>Enumeration</sub>

The frequency and locations at which a function fetches attribute data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLStepFunction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Step options

- [MTLStepFunctionConstant](mtlstepfunction/constant.md) — The function fetches attribute data once.
- [MTLStepFunctionPerInstance](mtlstepfunction/perinstance.md) — The function fetches data based on the instance index.
- [MTLStepFunctionPerPatch](mtlstepfunction/perpatch.md) — The post-tessellation function fetches data based on the patch index of the patch.
- [MTLStepFunctionPerPatchControlPoint](mtlstepfunction/perpatchcontrolpoint.md) — The post-tessellation function fetches data based on the control-point indices associated with the patch.
- [MTLStepFunctionPerVertex](mtlstepfunction/pervertex.md) — The vertex function fetches data for every vertex.
- [MTLStepFunctionThreadPositionInGridX](mtlstepfunction/threadpositioningridx.md) — The compute function fetches data based on the thread’s `x` coordinate.
- [MTLStepFunctionThreadPositionInGridY](mtlstepfunction/threadpositioningridy.md) — The compute function fetches data based on the thread’s `y` coordinate.
- [MTLStepFunctionThreadPositionInGridXIndexed](mtlstepfunction/threadpositioningridxindexed.md) — The compute function fetches data by using the thread’s `x` coordinate to look up a value in the index buffer.
- [MTLStepFunctionThreadPositionInGridYIndexed](mtlstepfunction/threadpositioningridyindexed.md) — The compute function fetches data by using the thread’s `y` coordinate to look up a value in the index buffer.

### Initializers

- [init(rawValue:)](<mtlstepfunction/init(rawvalue_).md>)

## See Also

### Describing fetch behavior

- [stride](mtlbufferlayoutdescriptor/stride.md) — The number of bytes from one buffer entry to the next.
- [stepFunction](mtlbufferlayoutdescriptor/stepfunction.md) — Determines how and when compute functions fetch data.
- [stepRate](mtlbufferlayoutdescriptor/steprate.md) — How frequently the step function should load data.
