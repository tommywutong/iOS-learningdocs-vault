---
title: 'depthDataOutput(_:didDrop:timestamp:connection:reason:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedepthdataoutputdelegate/depthdataoutput(_:diddrop:timestamp:connection:reason:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutputdelegate/depthdataoutput(_:diddrop:timestamp:connection:reason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedepthdataoutputdelegate/depthdataoutput%28_%3Adiddrop%3Atimestamp%3Aconnection%3Areason%3A%29.json'
content_hash: 'sha256:409a5942431242ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDepthDataOutputDelegate](../avcapturedepthdataoutputdelegate.md)

# depthDataOutput(_:didDrop:timestamp:connection:reason:)

<sub>Instance Method</sub>

Informs the delegate that captured depth data was not processed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func depthDataOutput(_ output: AVCaptureDepthDataOutput, didDrop depthData: AVDepthData, timestamp: CMTime, connection: AVCaptureConnection, reason: AVCaptureOutput.DataDroppedReason)
```

## Parameters

- `output` — The depth data output providing data.

- `depthData` — A depth data object containing information about the  dropped data, such as its data type. Because this depth data was not captured or processed, its [depthDataMap](../avdepthdata/depthdatamap.md) property is empty.

- `timestamp` — The time at which the data was captured.

- `connection` — The capture connection through which the data was captured.

- `reason` — The reason depth data was dropped.

## Discussion

The capture output calls this method once for each incident of dropped depth data. The object in the `depthData` parameter is an empty shell, and doesn’t contain a depth data backing pixel buffer.

The capture output calls this method on the dispatch queue specified by its [delegateCallbackQueue](../avcapturedepthdataoutput/delegatecallbackqueue.md) property. Because this method executes on the same dispatch queue that outputs depth data, your implementation must be efficient to prevent further capture performance problems such as additional drops.

## See Also

### Receiving depth data

- [- depthDataOutput:didOutputDepthData:timestamp:connection:](<depthdataoutput(__didoutput_timestamp_connection_).md>) — Provides newly captured depth data to the delegate.
- [DataDroppedReason](../avcaptureoutput/datadroppedreason.md) — Constants that define reasons for why the system dropped a frame.
