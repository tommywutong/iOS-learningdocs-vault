---
title: preferredVideoDecoderGPURegistryID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/preferredvideodecodergpuregistryid
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/preferredvideodecodergpuregistryid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/preferredvideodecodergpuregistryid.json'
content_hash: 'sha256:e9eb07a3b99b05b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# preferredVideoDecoderGPURegistryID

<sub>Instance Property</sub>

The registry identifier for the GPU used for video decoding.

<sub>macOS</sub>

```swift
nonisolated var preferredVideoDecoderGPURegistryID: UInt64 { get set }
```

## Discussion

By default, whenever possible, the GPU associated with the display presenting the [CALayer](../../quartzcore/calayer.md) performs the video decoding. Decode transitions to a new GPU, if appropriate, when the [CALayer](../../quartzcore/calayer.md) moves to a new display. This property overrides this default behavior, forcing decode to prefer an affinity to the GPU specified regardless of which GPU displays the associated [CALayer](../../quartzcore/calayer.md). Obtain the GPU registry ID from the GPU [MTLDevice](../../metal/mtldevice.md) using [registryID](../../metal/mtldevice/registryid.md) or from OpenGL or OpenCL.

> [!important] Important
> You must specify an external GPU (or a slotted GPU in Mac Pro) with this property. You can’t switch decoding between the integrated graphics and the built-in discrete graphics.

## See Also

### Configuring audio and video devices

- [audioOutputDeviceUniqueID](audiooutputdeviceuniqueid.md) — Specifies the unique ID of the Core Audio output device used to play audio.
