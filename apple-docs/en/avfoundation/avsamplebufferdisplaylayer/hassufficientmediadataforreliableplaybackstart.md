---
title: hasSufficientMediaDataForReliablePlaybackStart
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+（18.0 起废弃）, iPadOS 14.5+（18.0 起废弃）, Mac Catalyst 14.5+（18.0 起废弃）, macOS 11.3+（15.0 起废弃）, tvOS 14.5+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart.json'
content_hash: 'sha256:1e5bbd6665c2217e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# hasSufficientMediaDataForReliablePlaybackStart

<sub>Instance Property</sub>

A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level.

> [!warning] Deprecated
> Use sampleBufferRenderer's hasSufficientMediaDataForReliablePlaybackStart instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var hasSufficientMediaDataForReliablePlaybackStart: Bool { get }
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [hasSufficientMediaDataForReliablePlaybackStart](../avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart.md) on the [sampleBufferRenderer](samplebufferrenderer.md) instead.

## See Also

### Initiating media data requests

- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates the readiness of the layer to accept more sample buffers. _(deprecated)_
- [requiresFlushToResumeDecoding](requiresflushtoresumedecoding.md) — A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames. _(deprecated)_
- [- stopRequestingMediaData](<stoprequestingmediadata().md>) — Cancels any current media data request.
