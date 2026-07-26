---
title: isMuted
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/ismuted
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/ismuted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/ismuted.json'
content_hash: 'sha256:a735d682578bb553'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md)

# isMuted

<sub>Instance Property</sub>

A Boolean value that indicates whether audio for the renderer is in a muted state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isMuted: Bool { get set }
```

## Discussion

This property only affects muting the renderer instance and not the device.

## See Also

### Managing audio output

- [volume](volume.md) — The current audio volume for the audio renderer.
- [audioOutputDeviceUniqueID](audiooutputdeviceuniqueid.md) — The unique identifier of the output device used to play audio.
