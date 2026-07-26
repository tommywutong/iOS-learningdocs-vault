---
title: numberOfSegmentsDownloaded
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 9.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/numberofsegmentsdownloaded
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/numberofsegmentsdownloaded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/numberofsegmentsdownloaded.json'
content_hash: 'sha256:12978b933f7d0a8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# numberOfSegmentsDownloaded

<sub>Instance Property</sub>

A count of the media segments downloaded from the server to this client.

<sub>tvOS</sub>

```swift
var numberOfSegmentsDownloaded: Int { get }
```

## Discussion

The property corresponds to “sc-count”.

The value of this property is negative if unknown.

This property is not compatible with key-value observing.

## See Also

### Getting playback-related log events

- [playbackStartDate](playbackstartdate.md) — The date and time at which playback began for this event.
- [playbackSessionID](playbacksessionid.md) — A GUID that identifies the playback session.
- [playbackStartOffset](playbackstartoffset.md) — The offset, in seconds, in the playlist where the last uninterrupted period of playback began.
- [playbackType](playbacktype.md) — The playback type.
- [startupTime](startuptime.md) — The accumulated duration, in seconds, until the player item is ready to play.
- [durationWatched](durationwatched.md) — The accumulated duration, in seconds, of the media played.
- [numberOfDroppedVideoFrames](numberofdroppedvideoframes.md) — The total number of dropped video frames
- [numberOfStalls](numberofstalls.md) — The total number of playback stalls encountered.
- [segmentsDownloadedDuration](segmentsdownloadedduration.md) — The accumulated duration, in seconds, of the media segments downloaded.
- [downloadOverdue](downloadoverdue.md) — The total number of times that downloading the segments took too long.
