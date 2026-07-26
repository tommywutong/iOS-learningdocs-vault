---
title: stopRequestingMediaData()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/stoprequestingmediadata()
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/stoprequestingmediadata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/stoprequestingmediadata%28%29.json'
content_hash: 'sha256:cd690b1b7870de85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# stopRequestingMediaData()

<sub>Instance Method</sub>

Cancels any current media data request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func stopRequestingMediaData()
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [- stopRequestingMediaData](<../avqueuedsamplebufferrendering/stoprequestingmediadata().md>) on the [sampleBufferRenderer](samplebufferrenderer.md) instead.

This method cancels any current [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) call. Each invocation of [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) must be balanced by a call to this method.

This method may be called from within the [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) method’s block or from outside the block.

## See Also

### Initiating media data requests

- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates the readiness of the layer to accept more sample buffers. _(deprecated)_
- [requiresFlushToResumeDecoding](requiresflushtoresumedecoding.md) — A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames. _(deprecated)_
- [hasSufficientMediaDataForReliablePlaybackStart](hassufficientmediadataforreliableplaybackstart.md) — A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level. _(deprecated)_
