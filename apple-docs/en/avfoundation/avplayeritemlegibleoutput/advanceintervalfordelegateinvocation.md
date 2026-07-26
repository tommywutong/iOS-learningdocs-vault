---
title: advanceIntervalForDelegateInvocation
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemlegibleoutput/advanceintervalfordelegateinvocation
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/advanceintervalfordelegateinvocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput/advanceintervalfordelegateinvocation.json'
content_hash: 'sha256:ee3396eabbc6861f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemLegibleOutput](../avplayeritemlegibleoutput.md)

# advanceIntervalForDelegateInvocation

<sub>Instance Property</sub>

The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var advanceIntervalForDelegateInvocation: TimeInterval { get set }
```

## Discussion

If possible, an `AVPlayerItemLegibleOutput` instance messages its delegate `advanceIntervalForDelegateInvocation` seconds earlier than it otherwise would.

If the value provided is large, the delegate methods are invoked as soon as possible.

## See Also

### Configuring the delegate

- [delegate](delegate.md) — The delegate of the output class.
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [AVPlayerItemLegibleOutputPushDelegate](../avplayeritemlegibleoutputpushdelegate.md) — Methods you can implement to provide alternative attributed-string output.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which the delegate is called.
