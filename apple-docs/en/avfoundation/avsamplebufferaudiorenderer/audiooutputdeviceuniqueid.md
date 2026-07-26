---
title: audioOutputDeviceUniqueID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.13+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/audiooutputdeviceuniqueid
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/audiooutputdeviceuniqueid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/audiooutputdeviceuniqueid.json'
content_hash: 'sha256:572c91b7fda8c698'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md)

# audioOutputDeviceUniqueID

<sub>Instance Property</sub>

The unique identifier of the output device used to play audio.

<sub>macOS</sub>

```swift
var audioOutputDeviceUniqueID: String? { get set }
```

## Discussion

The default value of this property is `nil`, which indicates the use of the default audio device. Otherwise, set the value to an [NSString](../../foundation/nsstring.md) containing the unique identifier of the Core Audio output device to use for audio output. [kAudioDevicePropertyDeviceUID](../../coreaudio/kaudiodevicepropertydeviceuid.md) is a suitable source of audio output device unique IDs.

Modifying this property while the timebase’s rate isn’t `0.0` may cause the rate to briefly change to `0.0`.

On macOS, you can use the audio device clock as the [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md) and all attached [AVQueuedSampleBufferRendering](../avqueuedsamplebufferrendering.md) timebase clocks. If you modify the `audioOutputDeviceUniqueID`, the clocks of all these timebases may also change.

If you attach multiple renderers with different values for `audioOutputDeviceUniqueID` to the same buffer renderer synchronizer, audio may not stay in sync during playback. To avoid this, ensure that all synchronized sample buffer renderers are using the same audio output device.

## See Also

### Managing audio output

- [volume](volume.md) — The current audio volume for the audio renderer.
- [muted](ismuted.md) — A Boolean value that indicates whether audio for the renderer is in a muted state.
