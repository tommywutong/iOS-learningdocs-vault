---
title: AVPlayerItemOutputPullDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemoutputpulldelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemoutputpulldelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemoutputpulldelegate.json'
content_hash: 'sha256:8988ce99aee0126d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemOutputPullDelegate

<sub>Protocol</sub>

Methods you can implement to respond to pixel buffer changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVPlayerItemOutputPullDelegate : NSObjectProtocol, Sendable
```

## Overview

The methods in this protocol are called by [AVPlayerItemVideoOutput](avplayeritemvideooutput.md) objects.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Responding to pixel buffer changes

- [- outputMediaDataWillChange:](<avplayeritemoutputpulldelegate/outputmediadatawillchange(__).md>) — Tells the delegate that new samples are about to arrive.
- [- outputSequenceWasFlushed:](<avplayeritemoutputpulldelegate/outputsequencewasflushed(__).md>) — Tells the delegate that a new sample sequence is commencing.

## See Also

### Configuring the delegate

- [- setDelegate:queue:](<avplayeritemvideooutput/setdelegate(__queue_).md>) — Sets the delegate and dispatch queue for the receiver.
- [delegate](avplayeritemvideooutput/delegate.md) — The delegate for the video output object.
- [delegateQueue](avplayeritemvideooutput/delegatequeue.md) — The dispatch queue on which to call delegate methods.
