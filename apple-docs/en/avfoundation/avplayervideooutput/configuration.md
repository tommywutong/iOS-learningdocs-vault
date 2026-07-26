---
title: AVPlayerVideoOutput.Configuration
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayervideooutput/configuration
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayervideooutput/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayervideooutput/configuration.json'
content_hash: 'sha256:6217f960220f7827'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerVideoOutput](../avplayervideooutput.md)

# AVPlayerVideoOutput.Configuration

<sub>Class</sub>

An object that provides configuration information for the related player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Configuration
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Inspecting the configuration

- [sourcePlayerItem](configuration/sourceplayeritem.md) — The player item that’s the source of this configuration.
- [dataChannelDescription](configuration/datachanneldescription.md) — An array of data channels selected for this configuration.
- [activationTime](configuration/activationtime.md) — The host time this configuration became active on its associated player object.
- [preferredTransform](configuration/preferredtransform.md) — The preferred transform of the visual media.

## See Also

### Accessing video data

- [sample(forHostTime:)](<sample(forhosttime_).md>) — Retrieves a video sample along with auxiliary information for display at the specified host time.
- [Sample](sample.md) — A video frame along with auxiliary information for display at the specified presentation time.
- [taggedBuffers(forHostTime:)](<taggedbuffers(forhosttime_).md>) _(deprecated)_
