---
title: AVPlayerItemLegibleOutputPushDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemlegibleoutputpushdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate.json'
content_hash: 'sha256:b430d56e318d8c4c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemLegibleOutputPushDelegate

<sub>Protocol</sub>

Methods you can implement to provide alternative attributed-string output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVPlayerItemLegibleOutputPushDelegate : AVPlayerItemOutputPushDelegate
```

## Overview

This protocol extends the [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md) protocol.

## Relationships

- **Inherits From**: [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Providing alternative attributed-string output

- [- legibleOutput:didOutputAttributedStrings:nativeSampleBuffers:forItemTime:](<avplayeritemlegibleoutputpushdelegate/legibleoutput(__didoutputattributedstrings_nativesamplebuffers_foritemtime_).md>) — Asks the delegate to process the delivery of new textual samples.

## See Also

### Configuring the delegate

- [delegate](avplayeritemlegibleoutput/delegate.md) — The delegate of the output class.
- [- setDelegate:queue:](<avplayeritemlegibleoutput/setdelegate(__queue_).md>) — Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [advanceIntervalForDelegateInvocation](avplayeritemlegibleoutput/advanceintervalfordelegateinvocation.md) — The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
- [delegateQueue](avplayeritemlegibleoutput/delegatequeue.md) — The dispatch queue on which the delegate is called.
