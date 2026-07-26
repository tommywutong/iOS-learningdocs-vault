---
title: 'coordinateSeek(to:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateseek(to:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateseek(to:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateseek%28to%3Aoptions%3A%29.json'
content_hash: 'sha256:453afce97b82540e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinator](../avdelegatingplaybackcoordinator.md)

# coordinateSeek(to:options:)

<sub>Instance Method</sub>

Coordinates a seek to the specified time for all connected participants.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func coordinateSeek(to time: CMTime, options: AVDelegatingPlaybackCoordinatorSeekOptions = [])
```

## Parameters

- `time` — A time the group seeks to when the command ends.

- `options` — Additional configuration of the seek.

## Discussion

To end a suspension and also affect the group timing, see [- endProposingNewTime:](<../avcoordinatedplaybacksuspension/end(proposingnewtime_).md>).

> [!note] Note
> Calling this method while the coordinator is in a suspended state affects only the local playback object. It doesn’t affect group state, even after the suspension ends.

## See Also

### Coordinating state changes

- [- coordinateRateChangeToRate:options:](<coordinateratechange(to_options_).md>) — Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [- transitionToItemWithIdentifier:proposingInitialTimingBasedOnTimebase:](<transitiontoitem(withidentifier_proposinginitialtimingbasedon_).md>) — Tells the coordinator to transition to a new item.
- [- reapplyCurrentItemStateToPlaybackControlDelegate](<reapplycurrentitemstatetoplaybackcontroldelegate().md>) — Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [AVDelegatingPlaybackCoordinatorSeekOptions](../avdelegatingplaybackcoordinatorseekoptions.md) — Constants that define seek options.
- [AVDelegatingPlaybackCoordinatorRateChangeOptions](../avdelegatingplaybackcoordinatorratechangeoptions.md) — Constants that define rate change options.
