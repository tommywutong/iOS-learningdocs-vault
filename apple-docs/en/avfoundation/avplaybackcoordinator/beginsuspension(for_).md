---
title: 'beginSuspension(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplaybackcoordinator/beginsuspension(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinator/beginsuspension(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinator/beginsuspension%28for%3A%29.json'
content_hash: 'sha256:c44a32da180327e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlaybackCoordinator](../avplaybackcoordinator.md)

# beginSuspension(for:)

<sub>Instance Method</sub>

Tells the coordinator to stop sending playback commands temporarily when the playback object disconnects from the group activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func beginSuspension(for suspensionReason: AVCoordinatedPlaybackSuspension.Reason) -> AVCoordinatedPlaybackSuspension
```

## Parameters

- `suspensionReason` — The reason for the suspension. Indicate a system-defined value or a custom suspension reason.

## Return Value

A suspension object.

## Discussion

End a suspension by calling its [- end](<../avcoordinatedplaybacksuspension/end().md>) or [- endProposingNewTime:](<../avcoordinatedplaybacksuspension/end(proposingnewtime_).md>) method.

## See Also

### Suspending state coordination

- [AVCoordinatedPlaybackSuspension](../avcoordinatedplaybacksuspension.md) — An object that represents a temporary suspension of coordinated playback.
- [- expectedItemTimeAtHostTime:](<expecteditemtime(athosttime_).md>) — Returns a time in the current item’s timeline that the coordinator expects to play at the specified host time.
