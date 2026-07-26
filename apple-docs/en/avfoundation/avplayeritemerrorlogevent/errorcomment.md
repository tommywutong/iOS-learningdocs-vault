---
title: errorComment
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemerrorlogevent/errorcomment
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/errorcomment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemerrorlogevent/errorcomment.json'
content_hash: 'sha256:7a9feb8ef81ed3fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemErrorLogEvent](../avplayeritemerrorlogevent.md)

# errorComment

<sub>Instance Property</sub>

A description of the error encountered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var errorComment: String? { get }
```

## Discussion

The property corresponds to “comment”.

The value of this property may be `nil` if further information is not available.

## See Also

### Getting information about the event

- [date](date.md) — The date and time when the error occurred.
- [URI](uri.md) — The URI of the playback item that had an error.
- [serverAddress](serveraddress.md) — The IP address of the server that was the source of the error.
- [playbackSessionID](playbacksessionid.md) — A GUID that identifies the playback session that had an error.
- [errorStatusCode](errorstatuscode.md) — A unique error code identifier.
- [errorDomain](errordomain.md) — The domain of the error.
- [allHTTPResponseHeaderFields](allhttpresponseheaderfields.md) — The HTTP header fields the server returns.
