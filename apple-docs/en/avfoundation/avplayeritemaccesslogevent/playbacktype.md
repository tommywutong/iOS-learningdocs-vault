---
title: playbackType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent/playbacktype
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/playbacktype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent/playbacktype.json'
content_hash: 'sha256:e6fbc07356d18a64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md)

# playbackType

<sub>Instance Property</sub>

The playback type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var playbackType: String? { get }
```

## Discussion

The playback type can be live, VOD, or from a file. If `nil` is returned the playback type is unknown.

Corresponds to “s-playback-type”.

This property is not compatible with key-value observing.

## See Also

### Getting playback-related log events

- [playbackStartDate](playbackstartdate.md) — The date and time at which playback began for this event.
- [playbackSessionID](playbacksessionid.md) — A GUID that identifies the playback session.
- [playbackStartOffset](playbackstartoffset.md) — The offset, in seconds, in the playlist where the last uninterrupted period of playback began.
- [startupTime](startuptime.md) — The accumulated duration, in seconds, until the player item is ready to play.
- [durationWatched](durationwatched.md) — The accumulated duration, in seconds, of the media played.
- [numberOfDroppedVideoFrames](numberofdroppedvideoframes.md) — The total number of dropped video frames
- [numberOfStalls](numberofstalls.md) — The total number of playback stalls encountered.
- [numberOfSegmentsDownloaded](numberofsegmentsdownloaded.md) — A count of the media segments downloaded from the server to this client. _(deprecated)_
- [segmentsDownloadedDuration](segmentsdownloadedduration.md) — The accumulated duration, in seconds, of the media segments downloaded.
- [downloadOverdue](downloadoverdue.md) — The total number of times that downloading the segments took too long.
