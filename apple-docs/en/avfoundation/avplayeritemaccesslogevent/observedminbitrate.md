---
title: observedMinBitrate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（15.0 起废弃）, iPadOS 7.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, macOS 10.9+（12.0 起废弃）, tvOS 9.0+（15.0 起废弃）, watchOS 1.0+（8.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/observedminbitrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/observedminbitrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/observedminbitrate.json'
content_hash: 'sha256:0bf4fc5df73648c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# observedMinBitrate

<sub>Instance Property</sub>

The minimum observed segment download bit rate.

> [!warning] Deprecated
> Use observedBitrateStandardDeviation to monitor variance in network bitrate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
var observedMinBitrate: Double { get }
```

## Discussion

The value of the property is negative if unknown.

Corresponds to “c-observed-min-bitrate”.

This property is not compatible with key-value observing.

## See Also

### Getting bit rate log events

- [observedBitrateStandardDeviation](observedbitratestandarddeviation.md) — The standard deviation of the observed segment download bit rates.
- [observedMaxBitrate](observedmaxbitrate.md) — The maximum observed segment download bit rate. _(deprecated)_
- [switchBitrate](switchbitrate.md) — The bandwidth value that causes a switch, up or down, in the item’s quality being played.
- [indicatedBitrate](indicatedbitrate.md) — The throughput, in bits per second, required to play the stream, as advertised by the server.
- [observedBitrate](observedbitrate.md) — The empirical throughput, in bits per second, across all media downloaded.
- [averageAudioBitrate](averageaudiobitrate.md) — The audio track’s average bit rate, in bits per second.
- [averageVideoBitrate](averagevideobitrate.md) — The video track’s average bit rate, in bits per second.
- [indicatedAverageBitrate](indicatedaveragebitrate.md) — The average throughput, in bits per second, required to play the stream, as advertised by the server.
