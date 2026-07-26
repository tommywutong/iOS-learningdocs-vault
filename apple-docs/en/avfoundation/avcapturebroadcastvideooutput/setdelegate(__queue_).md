---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avcapturebroadcastvideooutput/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:a1a2ffc264caa850'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the receiver’s delegate and the dispatch queue on which the delegate will be called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setDelegate(_ delegate: (any AVCaptureBroadcastVideoOutputDelegate)?, queue delegateCallbackQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — An object conforming to the [AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md) protocol that will receive broadcast video output notifications.

- `delegateCallbackQueue` — A dispatch queue on which all [AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md) methods will be called.

## See Also

### Related Documentation

- [delegate](delegate.md) — The receiver’s delegate. _(beta)_
- [AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md) — Protocol for receiving broadcast video output events and data. _(beta)_

### Managing the Output

- [delegate](delegate.md) — The receiver’s delegate. _(beta)_
- [delegateCallbackQueue](delegatecallbackqueue.md) — The dispatch queue on which all [AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md) methods will be called. _(beta)_
