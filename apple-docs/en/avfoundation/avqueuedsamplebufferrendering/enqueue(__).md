---
title: 'enqueue(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avqueuedsamplebufferrendering/enqueue(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/enqueue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrendering/enqueue%28_%3A%29.json'
content_hash: 'sha256:cf7559b9db1c5576'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuedSampleBufferRendering](../avqueuedsamplebufferrendering.md)

# enqueue(_:)

<sub>Instance Method</sub>

Sends a sample buffer to the queue for rendering.

> [!warning] Deprecated
> Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's enqueue(_:) async or enqueueImmediately(_:) methods instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enqueue(_ sampleBuffer: CMSampleBuffer)
```

## Parameters

- `sampleBuffer` — The sample buffer to be enqueued.

## Discussion

For video data, the sample buffer is processed according to the attachments it contains. If it has a true value for its [kCMSampleAttachmentKey_DoNotDisplay](../../coremedia/kcmsampleattachmentkey_donotdisplay.md) attachment, the frame is decoded but not displayed. If it has a `true` value for its [kCMSampleAttachmentKey_DisplayImmediately](../../coremedia/kcmsampleattachmentkey_displayimmediately.md) attachment, the frame is displayed as soon as possible, regardless of its presentation timestamp. Otherwise, the frame is displayed according to its presentation timestamp, relative to the timebase.

To schedule the removal of previous images at a specific timestamp, enqueue a marker sample buffer that doesn’t contain any samples, with the [kCMSampleBufferAttachmentKey_EmptyMedia](../../coremedia/kcmsamplebufferattachmentkey_emptymedia.md) attachment set to [kCFBooleanTrue](../../corefoundation/kcfbooleantrue.md).

> [!important] Important
> Attachments with the `kCMSampleAttachmentKey_` prefix must be set using [CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)](<../../coremedia/cmsamplebuffergetsampleattachmentsarray(__createifnecessary_).md>) and [CFDictionarySetValue(_:_:_:)](<../../corefoundation/cfdictionarysetvalue(______).md>).  Attachments with the `kCMSampleBufferAttachmentKey_` prefix must be set via [CMSetAttachment(_:key:value:attachmentMode:)](<../../coremedia/cmsetattachment(__key_value_attachmentmode_).md>).

## See Also

### Requesting media

- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates whether the receiver is able to accept more sample buffers. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Tells the target to invoke a client-supplied block in order to gather sample buffers for playback. _(deprecated)_
- [- stopRequestingMediaData](<stoprequestingmediadata().md>) — Cancels any current [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) call. _(deprecated)_
