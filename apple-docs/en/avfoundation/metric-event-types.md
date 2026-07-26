---
title: Metric event types
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/metric-event-types
source_url: 'https://developer.apple.com/documentation/avfoundation/metric-event-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/metric-event-types.json'
content_hash: 'sha256:7c4c94791cce35df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Media playback](media-playback.md)

# Metric event types

<sub>API Collection</sub>

## Topics

### HTTP Live Streaming

- [AVMetricMediaResourceRequestEvent](avmetricmediaresourcerequestevent.md) — An event that represents a media resource request.
- [AVMetricContentKeyRequestEvent](avmetriccontentkeyrequestevent.md) — An event that represents a live streaming content key resource request.
- [AVMetricHLSMediaSegmentRequestEvent](avmetrichlsmediasegmentrequestevent.md) — An event that represents a live streaming media segment resource request.
- [AVMetricHLSPlaylistRequestEvent](avmetrichlsplaylistrequestevent.md) — An event that represents a live streaming playlist resource request.
- [AVMetricPlayerItemVariantSwitchStartEvent](avmetricplayeritemvariantswitchstartevent.md) — An event that represents when the player attempts a variant switch.
- [AVMetricPlayerItemVariantSwitchEvent](avmetricplayeritemvariantswitchevent.md) — An event that represents when the player completes a variant switch.
- [AVMetricMediaRendition](avmetricmediarendition.md)

### Buffering

- [AVMetricPlayerItemStallEvent](avmetricplayeritemstallevent.md) — An event that represents when playback stalls.
- [AVMetricPlayerItemLikelyToKeepUpEvent](avmetricplayeritemlikelytokeepupevent.md) — An event that represents when playback is likely to continue without stalling.
- [AVMetricPlayerItemInitialLikelyToKeepUpEvent](avmetricplayeriteminitiallikelytokeepupevent.md) — An event that represents the initial state for whether playback is likely to continue without stalling.

### Transport control

- [AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md) — An event that represents the combined metrics for the entire playback session.
- [AVMetricPlayerItemRateChangeEvent](avmetricplayeritemratechangeevent.md) — An event that represents when the playback rate changes.
- [AVMetricPlayerItemSeekDidCompleteEvent](avmetricplayeritemseekdidcompleteevent.md) — An event that represents when the playback seek completes.
- [AVMetricPlayerItemSeekEvent](avmetricplayeritemseekevent.md) — An event that represents when a playback seek occurs.

### Playback mode

- [AVMetricPlaybackMode](avmetricplaybackmode.md) — These constants are the possible playback modes returned by the property “mode” on AVMetricPlaybackModeSwitchEvent
- [AVMetricPlaybackModeSwitchEvent](avmetricplaybackmodeswitchevent.md) — Represents a change in playback state, entering one of AVMetricPlaybackMode _(beta)_

### Summary

- [AVMetricPlayerItemPlaybackSummaryEvent](avmetricplayeritemplaybacksummaryevent.md) — An event that represents the combined metrics for the entire playback session.
- [AVMetricDownloadSummaryEvent](avmetricdownloadsummaryevent.md) — Represents a summary metric event with aggregated metrics for the entire download task.

## See Also

### Metrics

- [AVMetrics](avmetrics.md) — An asynchronous stream of metric information.
- [AVMergedMetrics](avmergedmetrics.md) — An asynchronous stream of metric information from different publishers.
- [AVVideoPerformanceMetrics](avvideoperformancemetrics.md) — An object that provides metrics related to video playback quality.
- [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md) — A type for objects that publish metric events to the event stream.
- [AVMetricEvent](avmetricevent.md) — A base class that represents a metric event.
- [AVMetricErrorEvent](avmetricerrorevent.md) — An object that represents a metric event when an error occurs.
