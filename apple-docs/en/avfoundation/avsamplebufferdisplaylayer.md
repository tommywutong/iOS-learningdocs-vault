---
title: AVSampleBufferDisplayLayer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer.json'
content_hash: 'sha256:ed7238e2f76362e8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferDisplayLayer

<sub>Class</sub>

An object that displays compressed or uncompressed video frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor class AVSampleBufferDisplayLayer
```

## Relationships

- **Inherits From**: [CALayer](../quartzcore/calayer.md)

- **Conforms To**: [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md), [CAMediaTiming](../quartzcore/camediatiming.md), [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing the video renderer

- [sampleBufferRenderer](avsamplebufferdisplaylayer/samplebufferrenderer.md) — An object that enqueues video sample buffers for rendering.

### Configuring the layer

- [readyForDisplay](avsamplebufferdisplaylayer/isreadyfordisplay.md) — A Boolean value that indicates whether the first video frame is ready for display.
- [controlTimebase](avsamplebufferdisplaylayer/controltimebase.md) — A timebase that determines how the layer interprets timestamps.
- [videoGravity](avsamplebufferdisplaylayer/videogravity.md) — A value that indicates how the layer displays video within its bounds.
- [AVLayerVideoGravity](avlayervideogravity.md) — A structure that defines how a layer displays a player’s visual content within the layer’s bounds.

### Protecting content

- [preventsCapture](avsamplebufferdisplaylayer/preventscapture.md) — A Boolean value that indicates whether the layer protects against screen capture.
- [outputObscuredDueToInsufficientExternalProtection](avsamplebufferdisplaylayer/isoutputobscuredduetoinsufficientexternalprotection.md) — A Boolean value that indicates whether the system obscures decoded output due to insufficient external protection on the current device.

### Preventing backgrounding

- [preventsDisplaySleepDuringVideoPlayback](avsamplebufferdisplaylayer/preventsdisplaysleepduringvideoplayback.md) — A Boolean value that indicates whether the layer prevents the system from sleeping during video playback.
- [preventsAutomaticBackgroundingDuringVideoPlayback](avsamplebufferdisplaylayer/preventsautomaticbackgroundingduringvideoplayback.md) — A Boolean value that indicates whether video playback prevents the system from automatically backgrounding an app.

### Handling errors

- [AVSampleBufferDisplayLayerFailedToDecode](../foundation/nsnotification/name-swift.struct/avsamplebufferdisplaylayerfailedtodecode.md) — A notification the system posts when a sample buffer display layer fails to decode.
- [AVSampleBufferDisplayLayerFailedToDecodeNotificationErrorKey](avsamplebufferdisplaylayerfailedtodecodenotificationerrorkey.md) — The key for the corresponding error.

### Deprecated

- [Deprecated symbols](avsamplebufferdisplaylayer-deprecated-symbols.md) — Review unsupported symbols and their replacements.

## See Also

### Presentation

- [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md) — Methods you can implement to enqueue sample buffers for presentation.
- [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md) — An object used to synchronize multiple queued sample buffers to a single timeline.
- [AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md) — An object that enqueues video sample buffers for rendering.
- [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md) — An object used to decompress audio and play compressed or uncompressed audio.
