---
title: 'transitionToItem(withIdentifier:proposingInitialTimingBasedOn:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdelegatingplaybackcoordinator/transitiontoitem(withidentifier:proposinginitialtimingbasedon:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/transitiontoitem(withidentifier:proposinginitialtimingbasedon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinator/transitiontoitem%28withidentifier%3Aproposinginitialtimingbasedon%3A%29.json'
content_hash: 'sha256:2c84eba3c7952df0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinator](../avdelegatingplaybackcoordinator.md)

# transitionToItem(withIdentifier:proposingInitialTimingBasedOn:)

<sub>Instance Method</sub>

Tells the coordinator to transition to a new item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func transitionToItem(withIdentifier itemIdentifier: String?, proposingInitialTimingBasedOn snapshotTimebase: CMTimebase?)
```

## Parameters

- `itemIdentifier` — The identifier for the new current item, which is `nil` if there isn’t anything to play.

- `snapshotTimebase` — A time base that communicates the initial playback state of the new item. If you specify `nil`, the coordinator assumes that the player pauses at [zero](../../coremedia/cmtime/zero.md). You can retrieve an appropriate time base to pass for this value from AVFoundation playback objects like [AVSampleBufferRenderSynchronizer](../avsamplebufferrendersynchronizer.md). You can also create one manually using the [CMTimebaseCreateWithSourceClock(allocator:sourceClock:timebaseOut:)](<../../coremedia/cmtimebasecreatewithsourceclock(allocator_sourceclock_timebaseout_).md>) function.

## See Also

### Coordinating state changes

- [- coordinateRateChangeToRate:options:](<coordinateratechange(to_options_).md>) — Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [- coordinateSeekToTime:options:](<coordinateseek(to_options_).md>) — Coordinates a seek to the specified time for all connected participants.
- [- reapplyCurrentItemStateToPlaybackControlDelegate](<reapplycurrentitemstatetoplaybackcontroldelegate().md>) — Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [AVDelegatingPlaybackCoordinatorSeekOptions](../avdelegatingplaybackcoordinatorseekoptions.md) — Constants that define seek options.
- [AVDelegatingPlaybackCoordinatorRateChangeOptions](../avdelegatingplaybackcoordinatorratechangeoptions.md) — Constants that define rate change options.
