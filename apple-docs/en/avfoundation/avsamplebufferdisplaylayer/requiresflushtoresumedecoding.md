---
title: requiresFlushToResumeDecoding
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/requiresflushtoresumedecoding
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/requiresflushtoresumedecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/requiresflushtoresumedecoding.json'
content_hash: 'sha256:eaa90a7eb7ba3220'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# requiresFlushToResumeDecoding

<sub>Instance Property</sub>

A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames.

> [!warning] Deprecated
> Use sampleBufferRenderer's requiresFlushToResumeDecoding instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var requiresFlushToResumeDecoding: Bool { get }
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [requiresFlushToResumeDecoding](../avsamplebuffervideorenderer/requiresflushtoresumedecoding.md) on the [sampleBufferRenderer](samplebufferrenderer.md) instead.

When an app enters a state where use of video decoder resources isn’t permissible, the value of this property changes to [true](../../swift/true.md) and the display layer’s status changes to a [AVQueuedSampleBufferRenderingStatusFailed](../avqueuedsamplebufferrenderingstatus/failed.md) state.

To resume rendering sample buffers using the display layer after this property’s value is [true](../../swift/true.md), apps must first reset the display layer’s status to [AVQueuedSampleBufferRenderingStatusUnknown](../avqueuedsamplebufferrenderingstatus/unknown.md), which you do by calling the layer’s [- flush](<flush().md>) method.

This property isn’t key-value observable. Instead, observe changes to this property value by observing notifications of type [AVSampleBufferDisplayLayerRequiresFlushToResumeDecodingDidChangeNotification](../avsamplebufferdisplaylayerrequiresflushtoresumedecodingdidchangenotification.md).

## See Also

### Initiating media data requests

- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates the readiness of the layer to accept more sample buffers. _(deprecated)_
- [- stopRequestingMediaData](<stoprequestingmediadata().md>) — Cancels any current media data request.
- [hasSufficientMediaDataForReliablePlaybackStart](hassufficientmediadataforreliableplaybackstart.md) — A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level. _(deprecated)_
