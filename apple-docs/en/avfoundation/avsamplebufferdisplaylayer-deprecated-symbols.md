---
title: Deprecated symbols
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer-deprecated-symbols
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer-deprecated-symbols'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer-deprecated-symbols.json'
content_hash: 'sha256:d18157ced6d41947'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Sample buffer playback](sample-buffer-playback.md) · [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md)

# Deprecated symbols

<sub>API Collection</sub>

Review unsupported symbols and their replacements.

## Topics

### Initiating media data requests

- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<avsamplebufferdisplaylayer/requestmediadatawhenready(on_using_).md>) — Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [readyForMoreMediaData](avsamplebufferdisplaylayer/isreadyformoremediadata.md) — A Boolean value that indicates the readiness of the layer to accept more sample buffers. _(deprecated)_
- [requiresFlushToResumeDecoding](avsamplebufferdisplaylayer/requiresflushtoresumedecoding.md) — A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames. _(deprecated)_
- [- stopRequestingMediaData](<avsamplebufferdisplaylayer/stoprequestingmediadata().md>) — Cancels any current media data request.
- [hasSufficientMediaDataForReliablePlaybackStart](avsamplebufferdisplaylayer/hassufficientmediadataforreliableplaybackstart.md) — A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level. _(deprecated)_

### Flushing sample buffers

- [- flush](<avsamplebufferdisplaylayer/flush().md>) — Instructs the layer to discard any enqueued sample buffers that are pending.
- [- flushAndRemoveImage](<avsamplebufferdisplaylayer/flushandremoveimage().md>) — Instructs the layer to discard pending enqueued sample buffers and remove any currently displayed image. _(deprecated)_

### Configuring the timebase

- [timebase](avsamplebufferdisplaylayer/timebase.md) — The renderer’s timebase, which determines how the layer interprets time stamps. _(deprecated)_

### Enqueuing the sample buffer

- [- enqueueSampleBuffer:](<avsamplebufferdisplaylayer/enqueue(__).md>) — Sends a sample buffer for display.

### Getting display layer settings

- [status](avsamplebufferdisplaylayer/status.md) — The ability of the display layer to be used for enqueuing sample buffers. _(deprecated)_
- [AVQueuedSampleBufferRenderingStatus](avqueuedsamplebufferrenderingstatus.md) — The statuses for sample buffer rendering. _(deprecated)_

### Handling errors

- [error](avsamplebufferdisplaylayer/error.md) — The error that caused the failure. _(deprecated)_
