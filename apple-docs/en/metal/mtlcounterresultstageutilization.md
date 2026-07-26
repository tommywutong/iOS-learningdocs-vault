---
title: MTLCounterResultStageUtilization
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcounterresultstageutilization
source_url: 'https://developer.apple.com/documentation/metal/mtlcounterresultstageutilization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcounterresultstageutilization.json'
content_hash: 'sha256:6fcb070f6932c17a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterResultStageUtilization

<sub>Structure</sub>

The data structure for storing the data you resolve from a stage-utilization counter set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MTLCounterResultStageUtilization
```

## Overview

For steps that explain how to resolve data from a counter set, such as [MTLCommonCounterSetStageUtilization](mtlcommoncounterset/stageutilization.md), see [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Sendable](../swift/sendable.md)

## Topics

### Stage utilization values

- [totalCycles](mtlcounterresultstageutilization/totalcycles.md) — The total number of cycles the GPU uses to run a pass.
- [vertexCycles](mtlcounterresultstageutilization/vertexcycles.md) — The number of cycles the GPU uses to run vertex shaders during a pass.
- [tessellationCycles](mtlcounterresultstageutilization/tessellationcycles.md) — The number of cycles the GPU uses to run the tessellation stage during a pass.
- [postTessellationVertexCycles](mtlcounterresultstageutilization/posttessellationvertexcycles.md) — The number of cycles the GPU uses to run post-tessellation vertex shaders during a pass.
- [fragmentCycles](mtlcounterresultstageutilization/fragmentcycles.md) — The number of cycles the GPU uses to run fragment shaders during a pass.
- [renderTargetCycles](mtlcounterresultstageutilization/rendertargetcycles.md) — The number of cycles the GPU uses to write data to render targets during a render pass.

### Swift support

- [init()](<mtlcounterresultstageutilization/init().md>) — Creates a default stage-utilization result.
- [init(totalCycles:vertexCycles:tessellationCycles:postTessellationVertexCycles:fragmentCycles:renderTargetCycles:)](<mtlcounterresultstageutilization/init(totalcycles_vertexcycles_tessellationcycles_posttessellationvertexcycles_fragmentcycles_rendertargetcycles_).md>) — Creates a stage-utilization result from utilization values.

## See Also

### Counter sample data output

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md) — Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.
- [MTLCounterResultTimestamp](mtlcounterresulttimestamp.md) — The data structure for storing the data you resolve from a timestamp counter set.
- [MTLCounterResultStatistic](mtlcounterresultstatistic.md) — The data structure for storing the data you resolve from a statistic counter set.
- [MTLCounterErrorValue](mtlcountererrorvalue.md) — A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.
