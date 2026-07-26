---
title: delegateCallbackQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avcapturebroadcastvideooutput/delegatecallbackqueue
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/delegatecallbackqueue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturebroadcastvideooutput/delegatecallbackqueue.json'
content_hash: 'sha256:6c368515bf1cdc84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureBroadcastVideoOutput](../avcapturebroadcastvideooutput.md)

# delegateCallbackQueue

<sub>Instance Property</sub>

The dispatch queue on which all [AVCaptureBroadcastVideoOutputDelegate](../avcapturebroadcastvideooutputdelegate.md) methods will be called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var delegateCallbackQueue: dispatch_queue_t? { get }
```

## Discussion

The value of this property is a dispatch queue on which all delegate method calls will be serialized. If you have not called the [- setDelegate:queue:](<setdelegate(__queue_).md>) method, the value of this property will be `nil`.

## See Also

### Related Documentation

- [delegate](delegate.md) — The receiver’s delegate. _(beta)_
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the receiver’s delegate and the dispatch queue on which the delegate will be called. _(beta)_

### Managing the Output

- [delegate](delegate.md) — The receiver’s delegate. _(beta)_
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the receiver’s delegate and the dispatch queue on which the delegate will be called. _(beta)_
