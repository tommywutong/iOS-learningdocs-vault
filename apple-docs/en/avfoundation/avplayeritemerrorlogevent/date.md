---
title: date
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemerrorlogevent/date
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemerrorlogevent/date.json'
content_hash: 'sha256:66f8c43aba1307de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemErrorLogEvent](../avplayeritemerrorlogevent.md)

# date

<sub>Instance Property</sub>

The date and time when the error occurred.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var date: Date? { get }
```

## Discussion

The property corresponds to “date”.

The value of this property may be `nil` if the date is unknown.

## See Also

### Getting information about the event

- [URI](uri.md) — The URI of the playback item that had an error.
- [serverAddress](serveraddress.md) — The IP address of the server that was the source of the error.
- [playbackSessionID](playbacksessionid.md) — A GUID that identifies the playback session that had an error.
- [errorStatusCode](errorstatuscode.md) — A unique error code identifier.
- [errorDomain](errordomain.md) — The domain of the error.
- [errorComment](errorcomment.md) — A description of the error encountered.
- [allHTTPResponseHeaderFields](allhttpresponseheaderfields.md) — The HTTP header fields the server returns.
