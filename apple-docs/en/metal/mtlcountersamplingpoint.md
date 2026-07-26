---
title: MTLCounterSamplingPoint
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlcountersamplingpoint
source_url: 'https://developer.apple.com/documentation/metal/mtlcountersamplingpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcountersamplingpoint.json'
content_hash: 'sha256:102b2e0187704ced'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCounterSamplingPoint

<sub>Enumeration</sub>

Options for different times when you can sample GPU counters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLCounterSamplingPoint
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Reading sampling boundary types

- [MTLCounterSamplingPointAtBlitBoundary](mtlcountersamplingpoint/atblitboundary.md) — Counter sampling is allowed between blit commands in a blit pass.
- [MTLCounterSamplingPointAtDispatchBoundary](mtlcountersamplingpoint/atdispatchboundary.md) — Counter sampling is allowed between kernel dispatches in a compute pass.
- [MTLCounterSamplingPointAtDrawBoundary](mtlcountersamplingpoint/atdrawboundary.md) — Counter sampling is allowed between draw commands in a render pass.
- [MTLCounterSamplingPointAtStageBoundary](mtlcountersamplingpoint/atstageboundary.md) — Counter sampling is allowed at the start and end of a render pass’s vertex and fragment stages, and at the start and end of compute and blit passes.
- [MTLCounterSamplingPointAtTileDispatchBoundary](mtlcountersamplingpoint/attiledispatchboundary.md) — Counter sampling is allowed between tile dispatches in a render pass.

### Initializers

- [init(rawValue:)](<mtlcountersamplingpoint/init(rawvalue_).md>)

## See Also

### Sampling a GPU device’s counters

- [counterSets](mtldevice/countersets.md) — The counter sets supported by the device object.
- [- supportsCounterSampling:](<mtldevice/supportscountersampling(__).md>) — Returns a Boolean value that indicates whether you can read GPU counters at the specified command boundary.
- [- newCounterSampleBufferWithDescriptor:error:](<mtldevice/makecountersamplebuffer(descriptor_).md>) — Creates a counter sample buffer.
