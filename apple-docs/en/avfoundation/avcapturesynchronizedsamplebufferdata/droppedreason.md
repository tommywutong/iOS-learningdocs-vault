---
title: droppedReason
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesynchronizedsamplebufferdata/droppedreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedsamplebufferdata/droppedreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesynchronizedsamplebufferdata/droppedreason.json'
content_hash: 'sha256:04f913c97ae0ba93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSynchronizedSampleBufferData](../avcapturesynchronizedsamplebufferdata.md)

# droppedReason

<sub>Instance Property</sub>

A value indicating why the capture output failed to deliver sample buffers, if applicable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var droppedReason: AVCaptureOutput.DataDroppedReason { get }
```

## See Also

### Handling dropped data

- [sampleBufferWasDropped](samplebufferwasdropped.md) — A Boolean value indicating whether sample buffers were discarded between capture and processing.
