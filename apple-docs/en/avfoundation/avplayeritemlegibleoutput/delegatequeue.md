---
title: delegateQueue
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemlegibleoutput/delegatequeue
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/delegatequeue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput/delegatequeue.json'
content_hash: 'sha256:8f55d28e0433efc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemLegibleOutput](../avplayeritemlegibleoutput.md)

# delegateQueue

<sub>Instance Property</sub>

The dispatch queue on which the delegate is called.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var delegateQueue: dispatch_queue_t? { get }
```

## Discussion

This property does not support key-value observing.

## See Also

### Configuring the delegate

- [delegate](delegate.md) — The delegate of the output class.
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [AVPlayerItemLegibleOutputPushDelegate](../avplayeritemlegibleoutputpushdelegate.md) — Methods you can implement to provide alternative attributed-string output.
- [advanceIntervalForDelegateInvocation](advanceintervalfordelegateinvocation.md) — The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
