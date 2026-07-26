---
title: intendedSpatialAudioExperience
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-2wthu
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-2wthu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer/intendedspatialaudioexperience-2wthu.json'
content_hash: 'sha256:36fba92d549cfa9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md)

# intendedSpatialAudioExperience

<sub>Instance Property</sub>

The intended spatial audio experience applied to all AVSampleBufferAudioRenderers within this synchronizer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, copy) CASpatialAudioExperience * intendedSpatialAudioExperience;
```

## Discussion

The default value of CAAutomaticSpatialAudio means the renderers use their AVAudioSession’s intended spatial experience. If the anchoring strategy is impossible (e.g. it uses a destroyed UIScene’s identifier), the renderers follow a “front” anchoring strategy instead.
