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
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/anticipatedplaybackrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/anticipatedplaybackrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/anticipatedplaybackrate.json'
content_hash: 'sha256:832a77ea116ab389'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinatorSeekCommand](../avdelegatingplaybackcoordinatorseekcommand.md)

# anticipatedPlaybackRate

<sub>Instance Property</sub>

The rate at which the coordinator expects playback to resume.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var anticipatedPlaybackRate: Float { get }
```

## See Also

### Accessing command details

- [shouldBufferInAnticipationOfPlayback](shouldbufferinanticipationofplayback.md) — A Boolean value that indicates whether the player starts buffering in anticipation of a request to begin playback.
- [itemTime](itemtime.md) — The time to seek to in the item timeline.
- [completionDueDate](completionduedate.md) — The deadline by which the coordinator expects the delegate to handle the command.
