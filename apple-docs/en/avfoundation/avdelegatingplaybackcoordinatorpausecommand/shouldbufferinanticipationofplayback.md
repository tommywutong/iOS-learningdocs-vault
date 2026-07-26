---
title: shouldBufferInAnticipationOfPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand/shouldbufferinanticipationofplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand/shouldbufferinanticipationofplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorpausecommand/shouldbufferinanticipationofplayback.json'
content_hash: 'sha256:bac406bfa2307372'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinatorPauseCommand](../avdelegatingplaybackcoordinatorpausecommand.md)

# shouldBufferInAnticipationOfPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether the player starts buffering in preparation for a request to begin playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var shouldBufferInAnticipationOfPlayback: Bool { get }
```

## Discussion

A [true](../../swift/true.md) value indicates that a participant player requests starting playback at the [anticipatedPlaybackRate](anticipatedplaybackrate.md) value.

## See Also

### Accessing command details

- [anticipatedPlaybackRate](anticipatedplaybackrate.md) — The rate at which the coordinator expects the current item to play.
