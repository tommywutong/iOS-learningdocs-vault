---
title: AVPlayerItemMetadataOutputPushDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemmetadataoutputpushdelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemmetadataoutputpushdelegate.json'
content_hash: 'sha256:2e730f081737474f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemMetadataOutputPushDelegate

<sub>Protocol</sub>

Methods you can implement to provide additional metadata.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVPlayerItemMetadataOutputPushDelegate : AVPlayerItemOutputPushDelegate
```

## Overview

This protocol extends the [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md) protocol.

## Relationships

- **Inherits From**: [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Combining timed metadata groups

- [- metadataOutput:didOutputTimedMetadataGroups:fromPlayerItemTrack:](<avplayeritemmetadataoutputpushdelegate/metadataoutput(__didoutputtimedmetadatagroups_from_).md>) — Tells the delegate a new collection of metadata items is available.

## See Also

### Configuring the delegate

- [advanceIntervalForDelegateInvocation](avplayeritemmetadataoutput/advanceintervalfordelegateinvocation.md) — The time interval, in seconds, the player item metadata output object messages its delegate earlier than normal.
- [delegate](avplayeritemmetadataoutput/delegate.md) — The delegate object.
- [delegateQueue](avplayeritemmetadataoutput/delegatequeue.md) — The dispatch queue on which messages are sent to the delegate.
- [- setDelegate:queue:](<avplayeritemmetadataoutput/setdelegate(__queue_).md>) — Sets the delegate and a dispatch queue on which the delegate is called.
