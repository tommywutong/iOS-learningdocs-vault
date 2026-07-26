---
title: numberOfStalls
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/numberofstalls
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/numberofstalls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/numberofstalls.json'
content_hash: 'sha256:2dbc1de75a18889b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# numberOfStalls

<sub>Instance Property</sub>

The total number of playback stalls encountered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberOfStalls: Int { get }
```

## Discussion

The property corresponds to “c-stalls”.

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
- [numberOfSegmentsDownloaded](numberofsegmentsdownloaded.md) — A count of the media segments downloaded from the server to this client. _(deprecated)_
- [segmentsDownloadedDuration](segmentsdownloadedduration.md) — The accumulated duration, in seconds, of the media segments downloaded.
- [downloadOverdue](downloadoverdue.md) — The total number of times that downloading the segments took too long.
