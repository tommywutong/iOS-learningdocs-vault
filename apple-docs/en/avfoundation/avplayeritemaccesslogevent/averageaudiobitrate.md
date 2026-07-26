---
title: averageAudioBitrate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/averageaudiobitrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/averageaudiobitrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/averageaudiobitrate.json'
content_hash: 'sha256:abd402d8af6ae7e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# averageAudioBitrate

<sub>Instance Property</sub>

The audio track’s average bit rate, in bits per second.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var averageAudioBitrate: Double { get }
```

## Discussion

The property corresponds to “c-avg-audio-bitrate”.

This property returns a non-positive value if unknown.

This property is not compatible with key-value observing.

## See Also

### Getting bit rate log events

- [observedBitrateStandardDeviation](observedbitratestandarddeviation.md) — The standard deviation of the observed segment download bit rates.
- [observedMaxBitrate](observedmaxbitrate.md) — The maximum observed segment download bit rate. _(deprecated)_
- [observedMinBitrate](observedminbitrate.md) — The minimum observed segment download bit rate. _(deprecated)_
- [switchBitrate](switchbitrate.md) — The bandwidth value that causes a switch, up or down, in the item’s quality being played.
- [indicatedBitrate](indicatedbitrate.md) — The throughput, in bits per second, required to play the stream, as advertised by the server.
- [observedBitrate](observedbitrate.md) — The empirical throughput, in bits per second, across all media downloaded.
- [averageVideoBitrate](averagevideobitrate.md) — The video track’s average bit rate, in bits per second.
- [indicatedAverageBitrate](indicatedaveragebitrate.md) — The average throughput, in bits per second, required to play the stream, as advertised by the server.
