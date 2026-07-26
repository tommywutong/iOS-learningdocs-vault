---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemlegibleoutput/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput/delegate.json'
content_hash: 'sha256:6e76f4e9aff79c17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemLegibleOutput](../avplayeritemlegibleoutput.md)

# delegate

<sub>Instance Property</sub>

The delegate of the output class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var delegate: (any AVPlayerItemLegibleOutputPushDelegate)? { get }
```

## Discussion

Because the delegate is held using a zeroing-weak reference, this property has a value of `nil` after a delegate that was previously set has been deallocated.

This property does not support key-value observing.

## See Also

### Configuring the delegate

- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [AVPlayerItemLegibleOutputPushDelegate](../avplayeritemlegibleoutputpushdelegate.md) — Methods you can implement to provide alternative attributed-string output.
- [advanceIntervalForDelegateInvocation](advanceintervalfordelegateinvocation.md) — The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which the delegate is called.
