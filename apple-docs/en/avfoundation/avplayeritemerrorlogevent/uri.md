---
title: uri
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemerrorlogevent/uri
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/uri'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemerrorlogevent/uri.json'
content_hash: 'sha256:870a3a5fdbb34300'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemErrorLogEvent](../avplayeritemerrorlogevent.md)

# uri

<sub>Instance Property</sub>

The URI of the playback item that had an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var uri: String? { get }
```

## Discussion

The property corresponds to “uri”.

The value of this property may be `nil` if the URI is unknown.

## See Also

### Getting information about the event

- [date](date.md) — The date and time when the error occurred.
- [serverAddress](serveraddress.md) — The IP address of the server that was the source of the error.
- [playbackSessionID](playbacksessionid.md) — A GUID that identifies the playback session that had an error.
- [errorStatusCode](errorstatuscode.md) — A unique error code identifier.
- [errorDomain](errordomain.md) — The domain of the error.
- [errorComment](errorcomment.md) — A description of the error encountered.
- [allHTTPResponseHeaderFields](allhttpresponseheaderfields.md) — The HTTP header fields the server returns.
