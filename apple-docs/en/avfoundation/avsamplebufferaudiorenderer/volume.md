---
title: volume
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/volume
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/volume'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/volume.json'
content_hash: 'sha256:529e9542927582b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md)

# volume

<sub>Instance Property</sub>

The current audio volume for the audio renderer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var volume: Float { get set }
```

## Discussion

Use this property for frequent vloume changes; for example, a volume knob or fader. A value of `0.0` silences all audio while a value of `1.0` plays all audio at full volume.

## See Also

### Managing audio output

- [muted](ismuted.md) — A Boolean value that indicates whether audio for the renderer is in a muted state.
- [audioOutputDeviceUniqueID](audiooutputdeviceuniqueid.md) — The unique identifier of the output device used to play audio.
