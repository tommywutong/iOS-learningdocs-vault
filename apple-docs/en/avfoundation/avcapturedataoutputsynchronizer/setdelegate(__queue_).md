---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedataoutputsynchronizer/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedataoutputsynchronizer/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedataoutputsynchronizer/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:c6364ad55ccd4eeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDataOutputSynchronizer](../avcapturedataoutputsynchronizer.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Designates a delegate object to receive synchronized data and a dispatch queue for delivering that data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setDelegate(_ delegate: (any AVCaptureDataOutputSynchronizerDelegate)?, queue delegateCallbackQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — A delegate object to receive synchronized data.

- `delegateCallbackQueue` — The dispatch queue on which to call delegate methods. This parameter must be a serial dispatch queue to guarantee that captured data is delivered in order.

## Discussion

The data output synchronizer gathers data from its data outputs, and when it determines that all data has been received for a given timestamp, it vends collections of synchronized data by calling delegate methods on the specified dispatch queue.

The [AVCaptureDataOutputSynchronizer](../avcapturedataoutputsynchronizer.md) class overrides all the data outputs’ own delegates and callbacks. Data outputs under the control of a data output synchronizer do not fire delegate callbacks. Delegate callbacks are restored to individual data outputs only if you clear the synchronizer’s delegate and callback queue by calling this method and passing `nil` for both parameters.

## See Also

### Receiving synchronized capture data

- [delegate](delegate.md) — A delegate object that receives synchronized capture data.
- [delegateCallbackQueue](delegatecallbackqueue.md) — A dispatch queue for delivering synchronized capture data.
- [AVCaptureDataOutputSynchronizerDelegate](../avcapturedataoutputsynchronizerdelegate.md) — Methods for receiving captured data from multiple capture outputs synchronized to the same timestamp.
