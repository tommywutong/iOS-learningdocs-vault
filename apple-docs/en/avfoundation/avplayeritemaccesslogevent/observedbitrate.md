---
title: observedBitrate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/observedbitrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/observedbitrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/observedbitrate.json'
content_hash: 'sha256:67087f7154db20c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# observedBitrate

<sub>Instance Property</sub>

The empirical throughput, in bits per second, across all media downloaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var observedBitrate: Double { get }
```

## Discussion

The property corresponds to “c-observed-bitrate”.

The value of this property is negative if unknown.

This property is not compatible with key-value observing.

## See Also

### Getting bit rate log events

- [observedBitrateStandardDeviation](observedbitratestandarddeviation.md) — The standard deviation of the observed segment download bit rates.
- [observedMaxBitrate](observedmaxbitrate.md) — The maximum observed segment download bit rate. _(deprecated)_
- [observedMinBitrate](observedminbitrate.md) — The minimum observed segment download bit rate. _(deprecated)_
- [switchBitrate](switchbitrate.md) — The bandwidth value that causes a switch, up or down, in the item’s quality being played.
- [indicatedBitrate](indicatedbitrate.md) — The throughput, in bits per second, required to play the stream, as advertised by the server.
- [averageAudioBitrate](averageaudiobitrate.md) — The audio track’s average bit rate, in bits per second.
- [averageVideoBitrate](averagevideobitrate.md) — The video track’s average bit rate, in bits per second.
- [indicatedAverageBitrate](indicatedaveragebitrate.md) — The average throughput, in bits per second, required to play the stream, as advertised by the server.
