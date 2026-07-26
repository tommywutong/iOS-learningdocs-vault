---
title: startupTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/startuptime
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/startuptime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/startuptime.json'
content_hash: 'sha256:1bc914551adbec6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# startupTime

<sub>Instance Property</sub>

The accumulated duration, in seconds, until the player item is ready to play.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startupTime: TimeInterval { get }
```

## Discussion

The value of the property is negative if unknown.

Corresponds to “c-startup-time”.

This property is not compatible with key-value observing.

## See Also

### Getting playback-related log events

- [playbackStartDate](playbackstartdate.md) — The date and time at which playback began for this event.
- [playbackSessionID](playbacksessionid.md) — A GUID that identifies the playback session.
- [playbackStartOffset](playbackstartoffset.md) — The offset, in seconds, in the playlist where the last uninterrupted period of playback began.
- [playbackType](playbacktype.md) — The playback type.
- [durationWatched](durationwatched.md) — The accumulated duration, in seconds, of the media played.
- [numberOfDroppedVideoFrames](numberofdroppedvideoframes.md) — The total number of dropped video frames
- [numberOfStalls](numberofstalls.md) — The total number of playback stalls encountered.
- [numberOfSegmentsDownloaded](numberofsegmentsdownloaded.md) — A count of the media segments downloaded from the server to this client. _(deprecated)_
- [segmentsDownloadedDuration](segmentsdownloadedduration.md) — The accumulated duration, in seconds, of the media segments downloaded.
- [downloadOverdue](downloadoverdue.md) — The total number of times that downloading the segments took too long.
