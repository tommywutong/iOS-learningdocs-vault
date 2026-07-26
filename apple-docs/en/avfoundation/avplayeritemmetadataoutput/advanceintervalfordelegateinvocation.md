---
title: advanceIntervalForDelegateInvocation
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemmetadataoutput/advanceintervalfordelegateinvocation
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/advanceintervalfordelegateinvocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadataoutput/advanceintervalfordelegateinvocation.json'
content_hash: 'sha256:411e5162d410efc2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemMetadataOutput](../avplayeritemmetadataoutput.md)

# advanceIntervalForDelegateInvocation

<sub>Instance Property</sub>

The time interval, in seconds, the player item metadata output object messages its delegate earlier than normal.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var advanceIntervalForDelegateInvocation: TimeInterval { get set }
```

## Discussion

If  possible, an `AVPlayerItemMetadataOutput` will message its delegate `advanceIntervalForDelegateInvocation` seconds earlier than otherwise. If the value you provide is large, effectively requesting provision of samples earlier than the `AVPlayerItemMetadataOutput` is prepared to act on them, the delegate will be invoked as soon as possible.

## See Also

### Configuring the delegate

- [delegate](delegate.md) — The delegate object.
- [AVPlayerItemMetadataOutputPushDelegate](../avplayeritemmetadataoutputpushdelegate.md) — Methods you can implement to provide additional metadata.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which messages are sent to the delegate.
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate and a dispatch queue on which the delegate is called.
