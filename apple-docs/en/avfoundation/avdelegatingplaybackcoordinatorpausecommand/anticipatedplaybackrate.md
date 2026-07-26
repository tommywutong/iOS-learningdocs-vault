---
title: anticipatedPlaybackRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand/anticipatedplaybackrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand/anticipatedplaybackrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand/anticipatedplaybackrate.json'
content_hash: 'sha256:63288989439b4abd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinatorPauseCommand](../avdelegatingplaybackcoordinatorpausecommand.md)

# anticipatedPlaybackRate

<sub>Instance Property</sub>

The rate at which the coordinator expects the current item to play.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var anticipatedPlaybackRate: Float { get }
```

## Discussion

Consider this command complete after the player is ready to start playback at the indicated rate.

## See Also

### Accessing command details

- [shouldBufferInAnticipationOfPlayback](shouldbufferinanticipationofplayback.md) — A Boolean value that indicates whether the player starts buffering in preparation for a request to begin playback.
