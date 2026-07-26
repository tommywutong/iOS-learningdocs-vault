---
title: 'setDelegate(_:queue:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemlegibleoutput/setdelegate(_:queue:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/setdelegate(_:queue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput/setdelegate%28_%3Aqueue%3A%29.json'
content_hash: 'sha256:b35a310f7779d875'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemLegibleOutput](../avplayeritemlegibleoutput.md)

# setDelegate(_:queue:)

<sub>Instance Method</sub>

Sets the receiver’s delegate and a dispatch queue on which the delegate is called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setDelegate(_ delegate: (any AVPlayerItemLegibleOutputPushDelegate)?, queue delegateQueue: dispatch_queue_t?)
```

## Parameters

- `delegate` — An object conforming to the [AVPlayerItemLegibleOutputPushDelegate](../avplayeritemlegibleoutputpushdelegate.md) protocol.

- `delegateQueue` — A dispatch queue on which all delegate methods will be called.

## Discussion

Because the delegate is held using a zeroing-weak reference, it is safe to deallocate the delegate while the receiver still has a reference to it.

## See Also

### Configuring the delegate

- [delegate](delegate.md) — The delegate of the output class.
- [AVPlayerItemLegibleOutputPushDelegate](../avplayeritemlegibleoutputpushdelegate.md) — Methods you can implement to provide alternative attributed-string output.
- [advanceIntervalForDelegateInvocation](advanceintervalfordelegateinvocation.md) — The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which the delegate is called.
