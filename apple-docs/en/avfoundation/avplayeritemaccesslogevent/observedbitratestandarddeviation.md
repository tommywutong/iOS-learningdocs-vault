---
title: observedBitrateStandardDeviation
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/observedbitratestandarddeviation
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/observedbitratestandarddeviation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/observedbitratestandarddeviation.json'
content_hash: 'sha256:876b42c954e5198a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# observedBitrateStandardDeviation

<sub>Instance Property</sub>

The standard deviation of the observed segment download bit rates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var observedBitrateStandardDeviation: Double { get }
```

## Discussion

The value of the property is negative if unknown.

Corresponds to “c-observed-bitrate-sd”.

This property is not compatible with key-value observing.

## See Also

### Getting bit rate log events

- [observedMaxBitrate](observedmaxbitrate.md) — The maximum observed segment download bit rate. _(deprecated)_
- [observedMinBitrate](observedminbitrate.md) — The minimum observed segment download bit rate. _(deprecated)_
- [switchBitrate](switchbitrate.md) — The bandwidth value that causes a switch, up or down, in the item’s quality being played.
- [indicatedBitrate](indicatedbitrate.md) — The throughput, in bits per second, required to play the stream, as advertised by the server.
- [observedBitrate](observedbitrate.md) — The empirical throughput, in bits per second, across all media downloaded.
- [averageAudioBitrate](averageaudiobitrate.md) — The audio track’s average bit rate, in bits per second.
- [averageVideoBitrate](averagevideobitrate.md) — The video track’s average bit rate, in bits per second.
- [indicatedAverageBitrate](indicatedaveragebitrate.md) — The average throughput, in bits per second, required to play the stream, as advertised by the server.
