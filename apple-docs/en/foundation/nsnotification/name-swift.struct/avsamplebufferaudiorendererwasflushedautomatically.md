---
title: AVSampleBufferAudioRendererWasFlushedAutomatically
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/avsamplebufferaudiorendererwasflushedautomatically
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/avsamplebufferaudiorendererwasflushedautomatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/avsamplebufferaudiorendererwasflushedautomatically.json'
content_hash: 'sha256:1db2ef0970ac2d91'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# AVSampleBufferAudioRendererWasFlushedAutomatically

<sub>Type Property</sub>

A notification the system posts when a renderer flushes its enqueued media data without an explicit request to do so.

> [!warning] Deprecated
> Use the result of AVSampleBufferAudioRenderer.Receiver enqueue(_:) and enqueueImmediately(_:) for .successWithSuggestedFlushReason instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let AVSampleBufferAudioRendererWasFlushedAutomatically: NSNotification.Name
```

## Discussion

A renderer may flush enqueued media data when the user routes playback to a new destination, or when you change the playback rate of the attached [AVSampleBufferRenderSynchronizer](../../../avfoundation/avsamplebufferrendersynchronizer.md). No flush occurs for normal pauses and resumes.

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
