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
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/shouldbufferinanticipationofplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/shouldbufferinanticipationofplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/shouldbufferinanticipationofplayback.json'
content_hash: 'sha256:134f385b33971727'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinatorSeekCommand](../avdelegatingplaybackcoordinatorseekcommand.md)

# shouldBufferInAnticipationOfPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether the player starts buffering in anticipation of a request to begin playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var shouldBufferInAnticipationOfPlayback: Bool { get }
```

## See Also

### Accessing command details

- [anticipatedPlaybackRate](anticipatedplaybackrate.md) — The rate at which the coordinator expects playback to resume.
- [itemTime](itemtime.md) — The time to seek to in the item timeline.
- [completionDueDate](completionduedate.md) — The deadline by which the coordinator expects the delegate to handle the command.
