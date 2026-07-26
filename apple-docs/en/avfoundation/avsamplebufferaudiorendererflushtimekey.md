---
title: AVSampleBufferAudioRendererFlushTimeKey
framework: AVFoundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferaudiorendererflushtimekey
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorendererflushtimekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorendererflushtimekey.json'
content_hash: 'sha256:9b3ff3284d6a1378'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferAudioRendererFlushTimeKey

<sub>Global Variable</sub>

The key that indicates the presentation timestamp of the first queued sample that was flushed.

> [!warning] Deprecated
> Use the result of AVSampleBufferAudioRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .successWithSuggestedFlushReason instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let AVSampleBufferAudioRendererFlushTimeKey: String
```

## Discussion

The value for this key is an [NSValue](../foundation/nsvalue.md) object that wraps a [CMTime](../coremedia/cmtime.md) value.

## See Also

### Removing queued buffers

- [- flushFromSourceTime:completionHandler:](<avsamplebufferaudiorenderer/flush(fromsourcetime_completionhandler_).md>) — Flushes queued sample buffers with presentation time stamps later than or equal to the specified time. _(deprecated)_
