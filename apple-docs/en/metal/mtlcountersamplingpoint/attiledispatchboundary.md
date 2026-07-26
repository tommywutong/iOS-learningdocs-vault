---
title: MTLCounterSamplingPoint.atTileDispatchBoundary
framework: Metal
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplingpoint/attiledispatchboundary
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplingpoint/attiledispatchboundary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplingpoint/attiledispatchboundary.json'
content_hash: 'sha256:459ed7fc292909ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLCounterSamplingPoint](../mtlcountersamplingpoint.md)

# MTLCounterSamplingPoint.atTileDispatchBoundary

<sub>Case</sub>

Counter sampling is allowed between tile dispatches in a render pass.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case atTileDispatchBoundary
```

## Discussion

When a Metal device instance supports this sampling boundary, you can call the [- sampleCountersInBuffer:atSampleIndex:withBarrier:](<../mtlrendercommandencoder/samplecounters(samplebuffer_sampleindex_barrier_).md>) method on an [MTLRenderCommandEncoder](../mtlrendercommandencoder.md) to sample the counters between individual tile shader dispatches commands.

## See Also

### Reading sampling boundary types

- [MTLCounterSamplingPointAtBlitBoundary](atblitboundary.md) — Counter sampling is allowed between blit commands in a blit pass.
- [MTLCounterSamplingPointAtDispatchBoundary](atdispatchboundary.md) — Counter sampling is allowed between kernel dispatches in a compute pass.
- [MTLCounterSamplingPointAtDrawBoundary](atdrawboundary.md) — Counter sampling is allowed between draw commands in a render pass.
- [MTLCounterSamplingPointAtStageBoundary](atstageboundary.md) — Counter sampling is allowed at the start and end of a render pass’s vertex and fragment stages, and at the start and end of compute and blit passes.
