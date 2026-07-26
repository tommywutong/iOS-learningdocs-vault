---
title: itemTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/itemtime
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/itemtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorseekcommand/itemtime.json'
content_hash: 'sha256:432af8b28a751083'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinatorSeekCommand](../avdelegatingplaybackcoordinatorseekcommand.md)

# itemTime

<sub>Instance Property</sub>

The time to seek to in the item timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var itemTime: CMTime { get }
```

## Discussion

> [!important] Important
> Don’t automatically resume playback after seeking to this time. The coordinator issues a new play command when all participants are ready to resume.

## See Also

### Accessing command details

- [shouldBufferInAnticipationOfPlayback](shouldbufferinanticipationofplayback.md) — A Boolean value that indicates whether the player starts buffering in anticipation of a request to begin playback.
- [anticipatedPlaybackRate](anticipatedplaybackrate.md) — The rate at which the coordinator expects playback to resume.
- [completionDueDate](completionduedate.md) — The deadline by which the coordinator expects the delegate to handle the command.
