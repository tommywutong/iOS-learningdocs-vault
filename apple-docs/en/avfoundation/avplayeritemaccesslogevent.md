---
title: AVPlayerItemAccessLogEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslogevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslogevent.json'
content_hash: 'sha256:812a8cd53c773e1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemAccessLogEvent

<sub>Class</sub>

A single entry in a player item’s access log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemAccessLogEvent
```

## Overview

This object provides named properties for accessing the data fields of each log event. Each event is a single entry in an [AVPlayerItem](avplayeritem.md) object’s access log.

These properties aren’t observable. For more information about key-value observing, see [Using Key-Value Observing in Swift](../swift/using-key-value-observing-in-swift.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting server-related log events

- [URI](avplayeritemaccesslogevent/uri.md) — The URI of the playback item.
- [serverAddress](avplayeritemaccesslogevent/serveraddress.md) — The IP address of the server that was the source of the last delivered media segment.
- [numberOfServerAddressChanges](avplayeritemaccesslogevent/numberofserveraddresschanges.md) — A count of changes to the server address over the last uninterrupted period of playback.
- [mediaRequestsWWAN](avplayeritemaccesslogevent/mediarequestswwan.md) — The number of network read requests over a WWAN.
- [transferDuration](avplayeritemaccesslogevent/transferduration.md) — The accumulated duration, in seconds, of active network transfer of bytes.
- [numberOfBytesTransferred](avplayeritemaccesslogevent/numberofbytestransferred.md) — The accumulated number of bytes transferred by the item.
- [numberOfMediaRequests](avplayeritemaccesslogevent/numberofmediarequests.md) — The number of media read requests from the server to this client.

### Getting playback-related log events

- [playbackStartDate](avplayeritemaccesslogevent/playbackstartdate.md) — The date and time at which playback began for this event.
- [playbackSessionID](avplayeritemaccesslogevent/playbacksessionid.md) — A GUID that identifies the playback session.
- [playbackStartOffset](avplayeritemaccesslogevent/playbackstartoffset.md) — The offset, in seconds, in the playlist where the last uninterrupted period of playback began.
- [playbackType](avplayeritemaccesslogevent/playbacktype.md) — The playback type.
- [startupTime](avplayeritemaccesslogevent/startuptime.md) — The accumulated duration, in seconds, until the player item is ready to play.
- [durationWatched](avplayeritemaccesslogevent/durationwatched.md) — The accumulated duration, in seconds, of the media played.
- [numberOfDroppedVideoFrames](avplayeritemaccesslogevent/numberofdroppedvideoframes.md) — The total number of dropped video frames
- [numberOfStalls](avplayeritemaccesslogevent/numberofstalls.md) — The total number of playback stalls encountered.
- [numberOfSegmentsDownloaded](avplayeritemaccesslogevent/numberofsegmentsdownloaded.md) — A count of the media segments downloaded from the server to this client. _(deprecated)_
- [segmentsDownloadedDuration](avplayeritemaccesslogevent/segmentsdownloadedduration.md) — The accumulated duration, in seconds, of the media segments downloaded.
- [downloadOverdue](avplayeritemaccesslogevent/downloadoverdue.md) — The total number of times that downloading the segments took too long.

### Getting bit rate log events

- [observedBitrateStandardDeviation](avplayeritemaccesslogevent/observedbitratestandarddeviation.md) — The standard deviation of the observed segment download bit rates.
- [observedMaxBitrate](avplayeritemaccesslogevent/observedmaxbitrate.md) — The maximum observed segment download bit rate. _(deprecated)_
- [observedMinBitrate](avplayeritemaccesslogevent/observedminbitrate.md) — The minimum observed segment download bit rate. _(deprecated)_
- [switchBitrate](avplayeritemaccesslogevent/switchbitrate.md) — The bandwidth value that causes a switch, up or down, in the item’s quality being played.
- [indicatedBitrate](avplayeritemaccesslogevent/indicatedbitrate.md) — The throughput, in bits per second, required to play the stream, as advertised by the server.
- [observedBitrate](avplayeritemaccesslogevent/observedbitrate.md) — The empirical throughput, in bits per second, across all media downloaded.
- [averageAudioBitrate](avplayeritemaccesslogevent/averageaudiobitrate.md) — The audio track’s average bit rate, in bits per second.
- [averageVideoBitrate](avplayeritemaccesslogevent/averagevideobitrate.md) — The video track’s average bit rate, in bits per second.
- [indicatedAverageBitrate](avplayeritemaccesslogevent/indicatedaveragebitrate.md) — The average throughput, in bits per second, required to play the stream, as advertised by the server.

## See Also

### Accessing logging information

- [- accessLog](<avplayeritem/accesslog().md>) — Returns an object that represents a snapshot of the network access log. _(deprecated)_
- [AVPlayerItemAccessLog](avplayeritemaccesslog.md) — An object used to retrieve the access log associated with a player item.
- [- errorLog](<avplayeritem/errorlog().md>) — Returns an object that represents a snapshot of the error log. _(deprecated)_
- [AVPlayerItemErrorLog](avplayeritemerrorlog.md) — The error log associated with a player item.
- [AVPlayerItemErrorLogEvent](avplayeritemerrorlogevent.md) — A single item in a player item’s error log.
