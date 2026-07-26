---
title: 'expectedItemTime(atHostTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplaybackcoordinator/expecteditemtime(athosttime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/expecteditemtime(athosttime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/expecteditemtime%28athosttime%3A%29.json'
content_hash: 'sha256:0991c3010230bed5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# expectedItemTime(atHostTime:)

<sub>Instance Method</sub>

Returns a time in the current item’s timeline that the coordinator expects to play at the specified host time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func expectedItemTime(atHostTime hostClockTime: CMTime) -> CMTime
```

## Parameters

- `hostClockTime` — The host time to return a player item time for.

## Return Value

A time in the current item’s timeline.

## See Also

### Suspending state coordination

- [- beginSuspensionForReason:](<beginsuspension(for_).md>) — Tells the coordinator to stop sending playback commands temporarily when the playback object disconnects from the group activity.
- [AVCoordinatedPlaybackSuspension](../avcoordinatedplaybacksuspension.md) — An object that represents a temporary suspension of coordinated playback.
