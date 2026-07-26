---
title: AVSampleBufferAudioRendererOutputConfigurationDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+（27.0 起废弃）, iPadOS 15.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）, tvOS 15.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 8.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/avsamplebufferaudiorendereroutputconfigurationdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avsamplebufferaudiorendereroutputconfigurationdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/avsamplebufferaudiorendereroutputconfigurationdidchange.json'
content_hash: 'sha256:6ff3cc18f8f14e94'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# AVSampleBufferAudioRendererOutputConfigurationDidChange

<sub>Type Property</sub>

A notification the system posts to indicate that the hardware configuration doesn’t match the enqueued data format.

> [!warning] Deprecated
> Use the result of AVSampleBufferAudioRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .successWithSuggestedFlushReason instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let AVSampleBufferAudioRendererOutputConfigurationDidChange: NSNotification.Name
```

## Discussion

The output configuration of the playback hardware might change during the playback session if other apps play content in different formats. In these cases, the media content format doesn’t match the hardware configuration which would produce suboptimal rendering of the enqueued media data. When the framework detects such mismatch it posts this notification, so an app can flush the renderer and re-enqueue the sample buffers from the current media playhead, which configures the hardware based on the format of newly enqueued sample buffers.

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
