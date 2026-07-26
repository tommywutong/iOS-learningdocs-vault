---
title: AVCaptureOutput.DataDroppedReason.outOfBuffers
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureoutput/datadroppedreason/outofbuffers
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureoutput/datadroppedreason/outofbuffers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureoutput/datadroppedreason/outofbuffers.json'
content_hash: 'sha256:d94ae6d8a1c44044'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureOutput](../../avcaptureoutput.md) · [DataDroppedReason](../datadroppedreason.md)

# AVCaptureOutput.DataDroppedReason.outOfBuffers

<sub>Case</sub>

The system dropped data because the capture output exhausted its internal pool of memory buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case outOfBuffers
```

## Discussion

This situation typically indicates that your delegate object is holding on to captured data buffers for too long. If you need to perform extended processing of captured data, copy that data into buffers whose lifetimes you manage instead of relying on buffers vended by the capture output.

## See Also

### Reasons

- [AVCaptureOutputDataDroppedReasonNone](none.md) — The system didn’t drop data.
- [AVCaptureOutputDataDroppedReasonLateData](latedata.md) — The system dropped data because you’ve configured capture output to drop data when delegate queue is in a blocked state, and there’s data to deliver.
- [AVCaptureOutputDataDroppedReasonDiscontinuity](discontinuity.md) — The system dropped data because the device providing data experienced a discontinuity, and the output lost an unknown number of data objects.
