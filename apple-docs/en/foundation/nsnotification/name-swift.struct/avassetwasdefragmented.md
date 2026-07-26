---
title: AVAssetWasDefragmented
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/avassetwasdefragmented
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avassetwasdefragmented'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/avassetwasdefragmented.json'
content_hash: 'sha256:fb034ee19c1fb1e5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# AVAssetWasDefragmented

<sub>Type Property</sub>

A notification the system posts when a fragmented asset minder observes that the system defragments the asset on disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let AVAssetWasDefragmented: NSNotification.Name
```

## Discussion

The system posts this notification only for changes that occur after an asset’s [canContainFragments](../../../avfoundation/avasset/cancontainfragments.md) property reaches a [AVKeyValueStatus.loaded](../../../avfoundation/avkeyvaluestatus/loaded.md) status.

After the system posts this notification, the value of the asset’s [canContainFragments](../../../avfoundation/avasset/cancontainfragments.md) and [containsFragments](../../../avfoundation/avasset/containsfragments.md) properties is [false](../../../swift/false.md).

## See Also

### AVFoundation

- [AVAssetChapterMetadataGroupsDidChange](avassetchaptermetadatagroupsdidchange.md) — A notification the system posts when an asset’s chapter metadata groups change.
- [AVAssetContainsFragmentsDidChange](avassetcontainsfragmentsdidchange.md) — A notification the system posts when an asset’s fragments change.
- [AVAssetDurationDidChange](avassetdurationdidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset’s duration.
- [AVAssetMediaSelectionGroupsDidChange](avassetmediaselectiongroupsdidchange.md) — A notification the system posts when an asset’s media selection groups change.
- [AVAssetTrackSegmentsDidChange](avassettracksegmentsdidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s segments.
- [AVAssetTrackTimeRangeDidChange](avassettracktimerangedidchange.md) — A notification the system posts when a fragmented asset minder observes a change to a fragmented asset track’s time range.
- [AVAssetTrackTrackAssociationsDidChange](avassettracktrackassociationsdidchange.md) — A notification the system posts when the track associations for an asset track change.
- [subjectAreaDidChangeNotification](../../../avfoundation/avcapturedevice/subjectareadidchangenotification.md) — A notification the system posts when a capture device detects a substantial change to the video subject area.
- [wasConnectedNotification](../../../avfoundation/avcapturedevice/wasconnectednotification.md) — A notification the system posts when a new capture device becomes available.
- [wasDisconnectedNotification](../../../avfoundation/avcapturedevice/wasdisconnectednotification.md) — A notification the system posts when an existing device becomes unavailable.
- [formatDescriptionDidChangeNotification](../../../avfoundation/avcaptureinput/port/formatdescriptiondidchangenotification.md) — A notification the system posts when the capture input port’s format description changes.
- [didStartRunningNotification](../../../avfoundation/avcapturesession/didstartrunningnotification.md) — A notification the system posts when a capture session starts.
- [didStopRunningNotification](../../../avfoundation/avcapturesession/didstoprunningnotification.md) — A notification the system posts when a capture session stops.
- [interruptionEndedNotification](../../../avfoundation/avcapturesession/interruptionendednotification.md) — A notification the system posts when an interruption to a capture session finishes.
- [runtimeErrorNotification](../../../avfoundation/avcapturesession/runtimeerrornotification.md) — A notification the system posts when an error occurs during a capture session.
