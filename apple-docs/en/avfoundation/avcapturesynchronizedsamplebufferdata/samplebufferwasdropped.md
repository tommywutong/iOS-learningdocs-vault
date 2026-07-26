---
title: sampleBufferWasDropped
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizedsamplebufferdata/samplebufferwasdropped
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedsamplebufferdata/samplebufferwasdropped'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizedsamplebufferdata/samplebufferwasdropped.json'
content_hash: 'sha256:dd2881524a6f011b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedSampleBufferData](../avcapturesynchronizedsamplebufferdata.md)

# sampleBufferWasDropped

<sub>Instance Property</sub>

A Boolean value indicating whether sample buffers were discarded between capture and processing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var sampleBufferWasDropped: Bool { get }
```

## Discussion

If this value is [true](../../swift/true.md), sample buffers were captured for this synchronization point but could not be delivered. This situation differs from that where no sample buffer capture for the synchronization timestamp occurs. In that case, there is no [AVCaptureSynchronizedSampleBufferData](../avcapturesynchronizedsamplebufferdata.md) object present in the [AVCaptureSynchronizedDataCollection](../avcapturesynchronizeddatacollection.md) object delivered to your delegate method.

## See Also

### Handling dropped data

- [droppedReason](droppedreason.md) — A value indicating why the capture output failed to deliver sample buffers, if applicable.
