---
title: sampleBuffer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizedsamplebufferdata/samplebuffer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedsamplebufferdata/samplebuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizedsamplebufferdata/samplebuffer.json'
content_hash: 'sha256:ae80603932d3cd13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedSampleBufferData](../avcapturesynchronizedsamplebufferdata.md)

# sampleBuffer

<sub>Instance Property</sub>

The depth data captured at this synchronization point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var sampleBuffer: CMSampleBuffer { get }
```

## Discussion

Note that if the [sampleBufferWasDropped](samplebufferwasdropped.md) property is [true](../../swift/true.md), this [CMSampleBuffer](../../coremedia/cmsamplebuffer.md) object does not contain pixel data (instead, it contains only metadata).

This value is equivalent to that provided by the [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) or [- captureOutput:didDropSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__diddrop_from_).md>) delegate method when using a video data output without a data output synchronizer.
