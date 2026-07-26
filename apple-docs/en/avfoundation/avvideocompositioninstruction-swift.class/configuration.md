---
title: AVVideoCompositionInstruction.Configuration
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideocompositioninstruction-swift.class/configuration
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocompositioninstruction-swift.class/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocompositioninstruction-swift.class/configuration.json'
content_hash: 'sha256:dc2cd8361375a7cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md)

# AVVideoCompositionInstruction.Configuration

<sub>Structure</sub>

Configurable properties for initializing a new AVVideoCompositionInstruction instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct Configuration
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a configuration

- [init(backgroundColor:enablePostProcessing:layerInstructions:requiredSourceSampleDataTrackIDs:timeRange:)](<configuration/init(backgroundcolor_enablepostprocessing_layerinstructions_requiredsourcesampledatatrackids_timerange_).md>)

### Inspecting the configuration

- [backgroundColor](configuration/backgroundcolor.md) — The background color of the composition.
- [enablePostProcessing](configuration/enablepostprocessing.md) — A Boolean value that indicates whether the composition enables post-processing.
- [layerInstructions](configuration/layerinstructions.md) — Instructions that specify how to layer and compose video frames from source tracks.
- [requiredSourceSampleDataTrackIDs](configuration/requiredsourcesampledatatrackids.md) — The identifiers of source sample data tracks that the compositor requires to compose frames for the instruction.
- [timeRange](configuration/timerange.md) — The time range to which the instruction applies.

## See Also

### Creating an instruction

- [init(configuration:)](<init(configuration_).md>) — Initialize an AVVideoCompositionInstruction with a configuration.
