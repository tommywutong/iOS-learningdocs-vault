---
title: reapplyCurrentItemStateToPlaybackControlDelegate()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate()
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate%28%29.json'
content_hash: 'sha256:89fadd9a844f82f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinator](../avdelegatingplaybackcoordinator.md)

# reapplyCurrentItemStateToPlaybackControlDelegate()

<sub>Instance Method</sub>

Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func reapplyCurrentItemStateToPlaybackControlDelegate()
```

## See Also

### Coordinating state changes

- [- coordinateRateChangeToRate:options:](<coordinateratechange(to_options_).md>) — Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [- coordinateSeekToTime:options:](<coordinateseek(to_options_).md>) — Coordinates a seek to the specified time for all connected participants.
- [- transitionToItemWithIdentifier:proposingInitialTimingBasedOnTimebase:](<transitiontoitem(withidentifier_proposinginitialtimingbasedon_).md>) — Tells the coordinator to transition to a new item.
- [AVDelegatingPlaybackCoordinatorSeekOptions](../avdelegatingplaybackcoordinatorseekoptions.md) — Constants that define seek options.
- [AVDelegatingPlaybackCoordinatorRateChangeOptions](../avdelegatingplaybackcoordinatorratechangeoptions.md) — Constants that define rate change options.
