---
title: intendedSpatialAudioExperience
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-3z7d3
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-3z7d3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-3z7d3.json'
content_hash: 'sha256:7b133dd3fc1e0832'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# intendedSpatialAudioExperience

<sub>Instance Property</sub>

The synchronizer’s intended Spatial Audio experience.

<sub>visionOS</sub>

```swift
var intendedSpatialAudioExperience: any SpatialAudioExperience { get set }
```

## Discussion

The value applies to all [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md) objects within this synchronizer.

If unspecified, the property value defaults to [CAAutomaticSpatialAudio](../../audiotoolbox/caautomaticspatialaudio.md).
