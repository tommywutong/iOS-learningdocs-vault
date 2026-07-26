---
title: AVPlayerItemTrack
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemtrack
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemtrack'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemtrack.json'
content_hash: 'sha256:f9efde83860850b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemTrack

<sub>Class</sub>

An object that represents the presentation state of an asset track during playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor class AVPlayerItemTrack
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Observable](../observation/observable.md), [Sendable](../swift/sendable.md)

## Topics

### Setting the enabled state

- [enabled](avplayeritemtrack/isenabled.md) — A Boolean value that indicates whether the player item presents the track’s media during playback.

### Configuring video properties

- [currentVideoFrameRate](avplayeritemtrack/currentvideoframerate.md) — The current frame rate of the video track as it plays.
- [videoFieldMode](avplayeritemtrack/videofieldmode.md) — A mode that specifies the handling of video frames that contain multiple fields.
- [AVPlayerItemTrackVideoFieldModeDeinterlaceFields](avplayeritemtrackvideofieldmodedeinterlacefields.md) — A video field mode that requests deinterlacing of video fields.

### Accessing the asset track

- [assetTrack](avplayeritemtrack/assettrack.md) — An asset track that provides the media for the player item track.

## See Also

### Playback control

- [Observing playback state in SwiftUI](observing-playback-state-in-swiftui.md) — Keep your user interface in sync with state changes from playback objects.
- [Controlling the transport behavior of a player](controlling-the-transport-behavior-of-a-player.md) — Play, pause, and seek through a media presentation.
- [Creating a seamless multiview playback experience](creating-a-seamless-multiview-playback-experience.md) — Build advanced multiview playback experiences with the AVFoundation and AVRouting frameworks.
- [AVPlayer](avplayer.md) — An object that provides the interface to control the player’s transport behavior.
- [AVPlayerItem](avplayeritem.md) — An object that models the timing and presentation state of an asset during playback.
- [AVQueuePlayer](avqueueplayer.md) — An object that plays a sequence of player items.
- [AVPlayerLooper](avplayerlooper.md) — An object that loops media content using a queue player.
