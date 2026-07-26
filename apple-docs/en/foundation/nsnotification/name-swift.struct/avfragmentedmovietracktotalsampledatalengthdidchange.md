---
title: AVFragmentedMovieTrackTotalSampleDataLengthDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.10+（10.11 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/avfragmentedmovietracktotalsampledatalengthdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avfragmentedmovietracktotalsampledatalengthdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/avfragmentedmovietracktotalsampledatalengthdidchange.json'
content_hash: 'sha256:b79da7bad21b4c30'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# AVFragmentedMovieTrackTotalSampleDataLengthDidChange

<sub>Type Property</sub>

A notification the system posts when the sample data length of a fragmented movie track changes.

> [!warning] Deprecated
> Use [AVFragmentedMovieTrackTimeRangeDidChange](avfragmentedmovietracktimerangedidchange.md) or [AVFragmentedMovieTrackSegmentsDidChange](avfragmentedmovietracksegmentsdidchange.md) instead.

<sub>macOS</sub>

```swift
static let AVFragmentedMovieTrackTotalSampleDataLengthDidChange: NSNotification.Name
```

## See Also

### AVFoundation

- [AVAssetChapterMetadataGroupsDidChange](avassetchaptermetadatagroupsdidchange.md) — A notification the system posts when an asset’s chapter metadata groups change.
- [AVAssetContainsFragmentsDidChange](avassetcontainsfragmentsdidchange.md) — A notification the system posts when an asset’s fragments change.
- [AVAssetDurationDidChange](avassetdurationdidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset’s duration.
- [AVAssetMediaSelectionGroupsDidChange](avassetmediaselectiongroupsdidchange.md) — A notification the system posts when an asset’s media selection groups change.
- [AVAssetTrackSegmentsDidChange](avassettracksegmentsdidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s segments.
- [AVAssetTrackTimeRangeDidChange](avassettracktimerangedidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s time range.
- [AVAssetTrackTrackAssociationsDidChange](avassettracktrackassociationsdidchange.md) — A notification the system posts when the track associations for an asset track change.
- [AVAssetWasDefragmented](avassetwasdefragmented.md) — A notification the system posts when a fragmented asset minder observes that the system defragments the asset on disk.
- [subjectAreaDidChangeNotification](../../../avfoundation/avcapturedevice/subjectareadidchangenotification.md) — A notification the system posts when a capture device detects a substantial change to the video subject area.
- [wasConnectedNotification](../../../avfoundation/avcapturedevice/wasconnectednotification.md) — A notification the system posts when a new capture device becomes available.
- [wasDisconnectedNotification](../../../avfoundation/avcapturedevice/wasdisconnectednotification.md) — A notification the system posts when an existing device becomes unavailable.
- [formatDescriptionDidChangeNotification](../../../avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification.md) — A notification the system posts when the capture input port’s format description changes.
- [didStartRunningNotification](../../../avfoundation/avcapturesession/didstartrunningnotification.md) — A notification the system posts when a capture session starts.
- [didStopRunningNotification](../../../avfoundation/avcapturesession/didstoprunningnotification.md) — A notification the system posts when a capture session stops.
- [interruptionEndedNotification](../../../avfoundation/avcapturesession/interruptionendednotification.md) — A notification the system posts when an interruption to a capture session finishes.
