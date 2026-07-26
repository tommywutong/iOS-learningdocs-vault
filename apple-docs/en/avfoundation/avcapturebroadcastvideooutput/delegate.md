---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/delegate.json'
content_hash: 'sha256:4d068758626439a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md)

# delegate

<sub>Instance Property</sub>

The receiver’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var delegate: (any AVCaptureBroadcastVideoOutputDelegate)? { get }
```

## Discussion

The value of this property is an object conforming to the [AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md) protocol that will be able to monitor the broadcast output operations.

## See Also

### Related Documentation

- [AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md) — Protocol for receiving broadcast video output events and data. _(beta)_
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the receiver’s delegate and the dispatch queue on which the delegate will be called. _(beta)_

### Managing the Output

- [delegateCallbackQueue](delegatecallbackqueue.md) — The dispatch queue on which all [AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md) methods will be called. _(beta)_
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the receiver’s delegate and the dispatch queue on which the delegate will be called. _(beta)_
