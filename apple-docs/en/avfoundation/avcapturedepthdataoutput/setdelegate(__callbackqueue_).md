---
title: 'setDelegate(_:callbackQueue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedepthdataoutput/setdelegate(_:callbackqueue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput/setdelegate(_:callbackqueue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedepthdataoutput/setdelegate%28_%3Acallbackqueue%3A%29.json'
content_hash: 'sha256:29ff507c4dd62461'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md)

# setDelegate(_:callbackQueue:)

<sub>Instance Method</sub>

Designates a delegate object to receive depth data and a dispatch queue for delivering that data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setDelegate(_ delegate: (any AVCaptureDepthDataOutputDelegate)?, callbackQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — A delegate object to receive depth data.

- `callbackQueue` — The dispatch queue on which to call delegate methods. This parameter must be a serial dispatch queue to guarantee that depth data is delivered in order.

## Discussion

The depth data output vends captured depth data by calling delegate methods  on the specified dispatch queue.

If the callback queue is blocked when new depth data is captured, the [alwaysDiscardsLateDepthData](alwaysdiscardslatedepthdata.md) property determines whether to discard data or hold it for later delivery, allowing you to choose whether to prioritize timeliness or memory usage when your processing is unable to keep up with the rate of incoming depth data.

If you need to minimize the chances of depth data being dropped, provide a dedicated queue and do not share it with other data outputs. The capture output can defer processing of depth data to another queue; however, depth data pixel buffer maps may come from a finite buffer pool, which may be starved if your deferred processing fails to keep up.

## See Also

### Receiving captured depth data

- [delegate](delegate.md) — A delegate object that receives depth data.
- [delegateCallbackQueue](delegatecallbackqueue.md) — A dispatch queue for delivering depth data.
- [AVCaptureDepthDataOutputDelegate](../avcapturedepthdataoutputdelegate.md) — Methods for receiving depth data produced by a depth capture output.
