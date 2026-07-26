---
title: requiredSourceSampleDataTrackIDs
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class/configuration/requiredsourcesampledatatrackids
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/configuration/requiredsourcesampledatatrackids'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class/configuration/requiredsourcesampledatatrackids.json'
content_hash: 'sha256:8495ce4fe3ba5d38'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVVideoCompositionInstruction](../../avvideocompositioninstruction-swift.class.md) · [Configuration](../configuration.md)

# requiredSourceSampleDataTrackIDs

<sub>Instance Property</sub>

The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiredSourceSampleDataTrackIDs: [CMPersistentTrackID]
```

## See Also

### Inspecting the configuration

- [backgroundColor](backgroundcolor.md) — The background color of the composition.
- [enablePostProcessing](enablepostprocessing.md) — A Boolean value that indicates whether the composition enables post-processing.
- [layerInstructions](layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks.
- [timeRange](timerange.md) — The time range to which the instruction applies.
