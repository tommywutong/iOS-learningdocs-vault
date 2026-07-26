---
title: 'coordinateRateChange(to:options:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateratechange(to:options:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateratechange(to:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinator/coordinateratechange%28to%3Aoptions%3A%29.json'
content_hash: 'sha256:d5419de1fc95cfad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinator](../avdelegatingplaybackcoordinator.md)

# coordinateRateChange(to:options:)

<sub>Instance Method</sub>

Coordinates a rate change across all participants, waiting for others to become ready, if necessary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func coordinateRateChange(to rate: Float, options: AVDelegatingPlaybackCoordinatorRateChangeOptions = [])
```

## Parameters

- `rate` — The playback rate for the group to use.

- `options` — Additional configuration of the rate change.

## Discussion

When the rate changes from zero to nonzero, the coordinator may also wait for participant suspensions from the [suspensionReasonsThatTriggerWaiting](../avplaybackcoordinator/suspensionreasonsthattriggerwaiting.md) property.

Don’t call this method if the rate change doesn’t affect the group, or if the group doesn’t have control over local playback temporarily. For example, don’t call the method for a pause that occurs due to an audio session interruption. In those cases, inform the coordinator by beginning a suspension with an appropriate reason.

The suspension stops the coordinator from issuing further commands to its delegate. After beginning a suspension, you can reconfigure your app’s playback object as necessary.

> [!note] Note
> Calling this method while the coordinator is in a suspended state affects only the local playback object. It doesn’t affect group state, even after the suspension ends.

## See Also

### Coordinating state changes

- [- coordinateSeekToTime:options:](<coordinateseek(to_options_).md>) — Coordinates a seek to the specified time for all connected participants.
- [- transitionToItemWithIdentifier:proposingInitialTimingBasedOnTimebase:](<transitiontoitem(withidentifier_proposinginitialtimingbasedon_).md>) — Tells the coordinator to transition to a new item.
- [- reapplyCurrentItemStateToPlaybackControlDelegate](<reapplycurrentitemstatetoplaybackcontroldelegate().md>) — Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [AVDelegatingPlaybackCoordinatorSeekOptions](../avdelegatingplaybackcoordinatorseekoptions.md) — Constants that define seek options.
- [AVDelegatingPlaybackCoordinatorRateChangeOptions](../avdelegatingplaybackcoordinatorratechangeoptions.md) — Constants that define rate change options.
