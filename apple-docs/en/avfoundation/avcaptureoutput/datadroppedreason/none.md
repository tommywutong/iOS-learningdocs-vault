---
title: AVCaptureOutput.DataDroppedReason.none
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureoutput/datadroppedreason/none
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureoutput/datadroppedreason/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureoutput/datadroppedreason/none.json'
content_hash: 'sha256:4b35d5938748ca08'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureOutput](../../avcaptureoutput.md) · [DataDroppedReason](../datadroppedreason.md)

# AVCaptureOutput.DataDroppedReason.none

<sub>Case</sub>

The system didn’t drop data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case none
```

## See Also

### Reasons

- [AVCaptureOutputDataDroppedReasonLateData](latedata.md) — The system dropped data because you’ve configured capture output to drop data when delegate queue is in a blocked state, and there’s data to deliver.
- [AVCaptureOutputDataDroppedReasonOutOfBuffers](outofbuffers.md) — The system dropped data because the capture output exhausted its internal pool of memory buffers.
- [AVCaptureOutputDataDroppedReasonDiscontinuity](discontinuity.md) — The system dropped data because the device providing data experienced a discontinuity, and the output lost an unknown number of data objects.
