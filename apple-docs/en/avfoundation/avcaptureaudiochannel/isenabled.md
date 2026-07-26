---
title: isEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureaudiochannel/isenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureaudiochannel/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureaudiochannel/isenabled.json'
content_hash: 'sha256:863d49f275f03a81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureAudioChannel](../avcaptureaudiochannel.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the channel is in an enabled state.

<sub>macOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

By default, a connection enables all audio channels that it exposes. You can set this value to [false](../../swift/false.md) to stop the flow of data for a particular channel.

## See Also

### Configuring a channel

- [volume](volume.md) — The current volume (gain) of the channel.
