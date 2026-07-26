---
title: MTLCounterResultStatistic
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterresultstatistic
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresultstatistic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresultstatistic.json'
content_hash: 'sha256:83225f3fc960cde7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterResultStatistic

<sub>Structure</sub>

The data structure for storing the data you resolve from a statistic counter set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLCounterResultStatistic
```

## Overview

For steps that explain how to resolve data from a counter set, such as [MTLCommonCounterSetStatistic](mtlcommoncounterset/statistic.md), see [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Statistics values

- [tessellationInputPatches](mtlcounterresultstatistic/tessellationinputpatches.md) — The number of tessellation patches a render pass sends to the tessellation stage.
- [vertexInvocations](mtlcounterresultstatistic/vertexinvocations.md) — The number of times a render pass calls any vertex shader.
- [postTessellationVertexInvocations](mtlcounterresultstatistic/posttessellationvertexinvocations.md) — The number of vertices a render pass sends to a post-tessellation vertex shader.
- [clipperInvocations](mtlcounterresultstatistic/clipperinvocations.md) — The number of primitives a render pass sends to the clip stage.
- [clipperPrimitivesOut](mtlcounterresultstatistic/clipperprimitivesout.md) — The number of primitives the clip stage produces during a render pass.
- [fragmentInvocations](mtlcounterresultstatistic/fragmentinvocations.md) — The number of times a render pass calls fragment shaders.
- [fragmentsPassed](mtlcounterresultstatistic/fragmentspassed.md) — The number of fragments a render pass sends to the visibility and blend stages because they pass the scissor, depth, and stencil tests.
- [computeKernelInvocations](mtlcounterresultstatistic/computekernelinvocations.md) — The number of times a pass calls any compute kernel.

### Swift support

- [init()](<mtlcounterresultstatistic/init().md>) — Creates a default statistics result.
- [init(tessellationInputPatches:vertexInvocations:postTessellationVertexInvocations:clipperInvocations:clipperPrimitivesOut:fragmentInvocations:fragmentsPassed:computeKernelInvocations:)](<mtlcounterresultstatistic/init(tessellationinputpatches_vertexinvocations_posttessellationvertexinvocations_clipperinvocations_clipperprimitivesout_fragmentinvocations_fragmentspassed_co-3af97d296b.md>) — Creates a statistics result from statistic values.

## See Also

### Counter sample data output

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md) — Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.
- [MTLCounterResultTimestamp](mtlcounterresulttimestamp.md) — The data structure for storing the data you resolve from a timestamp counter set.
- [MTLCounterResultStageUtilization](mtlcounterresultstageutilization.md) — The data structure for storing the data you resolve from a stage-utilization counter set.
- [MTLCounterErrorValue](mtlcountererrorvalue.md) — A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.
