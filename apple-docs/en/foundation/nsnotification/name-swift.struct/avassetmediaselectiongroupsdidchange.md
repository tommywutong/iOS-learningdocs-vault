---
title: AVAssetMediaSelectionGroupsDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/avassetmediaselectiongroupsdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avassetmediaselectiongroupsdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/avassetmediaselectiongroupsdidchange.json'
content_hash: 'sha256:529a6c7b920e9d9b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# AVAssetMediaSelectionGroupsDidChange

<sub>Type Property</sub>

A notification the system posts when an asset’s media selection groups change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let AVAssetMediaSelectionGroupsDidChange: NSNotification.Name
```

## Discussion

The system posts this notification only after the value of an asset’s [availableMediaCharacteristicsWithMediaSelectionOptions](../../../avfoundation/avpartialasyncproperty/availablemediacharacteristicswithmediaselectionoptions.md) property reaches a status of [AVKeyValueStatus.loaded](../../../avfoundation/avkeyvaluestatus/loaded.md).

## See Also

### AVFoundation

- [AVAssetChapterMetadataGroupsDidChange](avassetchaptermetadatagroupsdidchange.md) — A notification the system posts when an asset’s chapter metadata groups change.
- [AVAssetContainsFragmentsDidChange](avassetcontainsfragmentsdidchange.md) — A notification the system posts when an asset’s fragments change.
- [AVAssetDurationDidChange](avassetdurationdidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset’s duration.
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
- [runtimeErrorNotification](../../../avfoundation/avcapturesession/runtimeerrornotification.md) — A notification the system posts when an error occurs during a capture session.
