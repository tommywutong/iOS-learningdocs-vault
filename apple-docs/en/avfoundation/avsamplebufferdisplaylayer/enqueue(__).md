---
title: 'enqueue(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avsamplebufferdisplaylayer/enqueue(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/enqueue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/enqueue%28_%3A%29.json'
content_hash: 'sha256:8556a75d0d983b9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# enqueue(_:)

<sub>Instance Method</sub>

Sends a sample buffer for display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func enqueue(_ sampleBuffer: CMSampleBuffer)
```

## Parameters

- `sampleBuffer` — The sample buffer to display.

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [- enqueueSampleBuffer:](<../avqueuedsamplebufferrendering/enqueue(__).md>) on the [sampleBufferRenderer](samplebufferrenderer.md) instead.

If `sampleBuffer` has the [kCMSampleAttachmentKey_DoNotDisplay](../../coremedia/kcmsampleattachmentkey_donotdisplay.md) attachment set to [kCFBooleanTrue](../../corefoundation/kcfbooleantrue.md), the frame will be decoded but not displayed.

If `sampleBuffer` has the [kCMSampleAttachmentKey_DisplayImmediately](../../coremedia/kcmsampleattachmentkey_displayimmediately.md) attachment set to [kCFBooleanTrue](../../corefoundation/kcfbooleantrue.md), the decoded image will be displayed as soon as possible, replacing all previously enqueued images regardless of their timestamps.

Otherwise, the decoded image will be displayed at the `sampleBuffer` output presentation timestamp, as interpreted by the [controlTimebase](controltimebase.md) property (or the `mach_absolute_time` timeline if there is no control timebase).

To schedule the removal of previous images at a specific timestamp, enqueue a marker sample buffer containing no samples, with the [kCMSampleBufferAttachmentKey_EmptyMedia](../../coremedia/kcmsamplebufferattachmentkey_emptymedia.md) attachment set to [kCFBooleanTrue](../../corefoundation/kcfbooleantrue.md).

> [!important] Important
> Attachments with the `kCMSampleAttachmentKey_*` prefix must be set via [CMSampleBufferGetSampleAttachmentsArray(_:createIfNecessary:)](<../../coremedia/cmsamplebuffergetsampleattachmentsarray(__createifnecessary_).md>) and [CFDictionarySetValue(_:_:_:)](<../../corefoundation/cfdictionarysetvalue(______).md>). Attachments with the `kCMSampleBufferAttachmentKey_*` prefix must be set via [CMSetAttachment(_:key:value:attachmentMode:)](<../../coremedia/cmsetattachment(__key_value_attachmentmode_).md>).
