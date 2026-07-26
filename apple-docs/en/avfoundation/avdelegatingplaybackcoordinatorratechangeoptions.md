---
title: AVDelegatingPlaybackCoordinatorRateChangeOptions
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdelegatingplaybackcoordinatorratechangeoptions
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinatorratechangeoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinatorratechangeoptions.json'
content_hash: 'sha256:727b2a04eca6fffc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVDelegatingPlaybackCoordinatorRateChangeOptions

<sub>Structure</sub>

Constants that define rate change options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct AVDelegatingPlaybackCoordinatorRateChangeOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Rate change options

- [AVDelegatingPlaybackCoordinatorRateChangeOptionPlayImmediately](avdelegatingplaybackcoordinatorratechangeoptions/playimmediately.md) — Indicates that the coordinator should begin playback as soon as possible, regardless of other participant’s readiness or suspensions.

### Initializers

- [init(rawValue:)](<avdelegatingplaybackcoordinatorratechangeoptions/init(rawvalue_).md>) — Creates a rate change option with a string.

## See Also

### Coordinating state changes

- [- coordinateRateChangeToRate:options:](<avdelegatingplaybackcoordinator/coordinateratechange(to_options_).md>) — Coordinates a rate change across all participants, waiting for others to become ready, if necessary.
- [- coordinateSeekToTime:options:](<avdelegatingplaybackcoordinator/coordinateseek(to_options_).md>) — Coordinates a seek to the specified time for all connected participants.
- [- transitionToItemWithIdentifier:proposingInitialTimingBasedOnTimebase:](<avdelegatingplaybackcoordinator/transitiontoitem(withidentifier_proposinginitialtimingbasedon_).md>) — Tells the coordinator to transition to a new item.
- [- reapplyCurrentItemStateToPlaybackControlDelegate](<avdelegatingplaybackcoordinator/reapplycurrentitemstatetoplaybackcontroldelegate().md>) — Tells the coordinator to reissue current play state commands to synchronize the current item to the state of other participants.
- [AVDelegatingPlaybackCoordinatorSeekOptions](avdelegatingplaybackcoordinatorseekoptions.md) — Constants that define seek options.
