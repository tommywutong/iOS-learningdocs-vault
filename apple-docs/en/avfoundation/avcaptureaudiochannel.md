---
title: AVCaptureAudioChannel
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiochannel
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiochannel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiochannel.json'
content_hash: 'sha256:b1aaeba01efe4021'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureAudioChannel

<sub>Class</sub>

An object that monitors average and peak power levels for an audio channel in a capture connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureAudioChannel
```

## Overview

You don’t create instances of this class directly. Instead, an [AVCaptureConnection](avcaptureconnection.md) object that connects an audio input to an audio output provides an array of [AVCaptureAudioChannel](avcaptureaudiochannel.md) objects, one for each channel of audio available. You can poll for audio levels by iterating through these audio channel objects.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring a channel

- [enabled](avcaptureaudiochannel/isenabled.md) — A Boolean value that indicates whether the channel is in an enabled state.
- [volume](avcaptureaudiochannel/volume.md) — The current volume (gain) of the channel.

### Accessing power levels

- [averagePowerLevel](avcaptureaudiochannel/averagepowerlevel.md) — The instantaneous average power level in decibels.
- [peakHoldLevel](avcaptureaudiochannel/peakholdlevel.md) — The peak hold power level in decibels.

## See Also

### Connecting inputs and outputs

- [connections](avcapturesession/connections.md) — The connections between inputs and outputs that a capture session contains.
- [- addConnection:](<avcapturesession/addconnection(__).md>) — Adds a connection to the capture session.
- [- canAddConnection:](<avcapturesession/canaddconnection(__).md>) — Determines whether a you can add a connection to a capture session.
- [- addInputWithNoConnections:](<avcapturesession/addinputwithnoconnections(__).md>) — Adds a capture input to a session without forming any connections.
- [- addOutputWithNoConnections:](<avcapturesession/addoutputwithnoconnections(__).md>) — Adds a capture output to the session without forming any connections.
- [- removeConnection:](<avcapturesession/removeconnection(__).md>) — Removes a capture connection from the session.
