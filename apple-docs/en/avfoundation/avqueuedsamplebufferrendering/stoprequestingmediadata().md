---
title: stopRequestingMediaData()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avqueuedsamplebufferrendering/stoprequestingmediadata()
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/stoprequestingmediadata()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrendering/stoprequestingmediadata%28%29.json'
content_hash: 'sha256:0250c5ff51c7c292'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuedSampleBufferRendering](../avqueuedsamplebufferrendering.md)

# stopRequestingMediaData()

<sub>Instance Method</sub>

Cancels any current [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) call.

> [!warning] Deprecated
> Cancel the receiver's Task instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stopRequestingMediaData()
```

## Discussion

Always pair a call to [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) with this method. You can call this method from inside or outside of the requesting method’s block parameter.

## See Also

### Requesting media

- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates whether the receiver is able to accept more sample buffers. _(deprecated)_
- [- enqueueSampleBuffer:](<enqueue(__).md>) — Sends a sample buffer to the queue for rendering. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Tells the target to invoke a client-supplied block in order to gather sample buffers for playback. _(deprecated)_
