---
title: 'depthDataOutput(_:didOutput:timestamp:connection:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedepthdataoutputdelegate/depthdataoutput(_:didoutput:timestamp:connection:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutputdelegate/depthdataoutput(_:didoutput:timestamp:connection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedepthdataoutputdelegate/depthdataoutput%28_%3Adidoutput%3Atimestamp%3Aconnection%3A%29.json'
content_hash: 'sha256:f60cfe36833416af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDepthDataOutputDelegate](../avcapturedepthdataoutputdelegate.md)

# depthDataOutput(_:didOutput:timestamp:connection:)

<sub>Instance Method</sub>

Provides newly captured depth data to the delegate.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func depthDataOutput(_ output: AVCaptureDepthDataOutput, didOutput depthData: AVDepthData, timestamp: CMTime, connection: AVCaptureConnection)
```

## Parameters

- `output` — The depth data output providing data.

- `depthData` — A depth data object containing the captured per-pixel depth data.

- `timestamp` — The time at which the data was captured.

- `connection` — The capture connection through which the data was captured.

## Discussion

The depth data output calls this method whenever it captures and outputs a new depth data object. This method is called on the dispatch queue specified by the output’s [delegateCallbackQueue](../avcapturedepthdataoutput/delegatecallbackqueue.md) property, and can be called frequently. Your implementation must process the depth data quickly in order to prevent dropped depth data.

To maintain optimal performance, the capture pipeline may allocate [AVDepthData](../avdepthdata.md) pixel buffer maps from a finite memory pool. If you hold on to any [AVDepthData](../avdepthdata.md) objects for too long, capture inputs cannot copy new depth data into memory, resulting in dropped depth data. If your application is causing depth data drops by holding on to provided depth data objects for too long, consider copying the pixel buffer map data into a new pixel buffer so that the [AVDepthData](../avdepthdata.md) backing memory can be reused more quickly.

## See Also

### Receiving depth data

- [- depthDataOutput:didDropDepthData:timestamp:connection:reason:](<depthdataoutput(__diddrop_timestamp_connection_reason_).md>) — Informs the delegate that captured depth data was not processed.
- [DataDroppedReason](../avcaptureoutput/datadroppedreason.md) — Constants that define reasons for why the system dropped a frame.
