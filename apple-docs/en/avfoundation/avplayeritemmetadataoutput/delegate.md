---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemmetadataoutput/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutput/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadataoutput/delegate.json'
content_hash: 'sha256:3190b56c01e62a14'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemMetadataOutput](../avplayeritemmetadataoutput.md)

# delegate

<sub>Instance Property</sub>

The delegate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
weak var delegate: (any AVPlayerItemMetadataOutputPushDelegate)? { get }
```

## See Also

### Configuring the delegate

- [advanceIntervalForDelegateInvocation](advanceintervalfordelegateinvocation.md) — The time interval, in seconds, the player item metadata output object messages its delegate earlier than normal.
- [AVPlayerItemMetadataOutputPushDelegate](../avplayeritemmetadataoutputpushdelegate.md) — Methods you can implement to provide additional metadata.
- [delegateQueue](delegatequeue.md) — The dispatch queue on which messages are sent to the delegate.
- [- setDelegate:queue:](<setdelegate(__queue_).md>) — Sets the delegate and a dispatch queue on which the delegate is called.
