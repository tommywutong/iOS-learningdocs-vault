---
title: allHTTPResponseHeaderFields
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, tvOS 17.5+, visionOS 1.2+, watchOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemerrorlogevent/allhttpresponseheaderfields
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/allhttpresponseheaderfields'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemerrorlogevent/allhttpresponseheaderfields.json'
content_hash: 'sha256:4d0cdb9d2f69adec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemErrorLogEvent](../avplayeritemerrorlogevent.md)

# allHTTPResponseHeaderFields

<sub>Instance Property</sub>

The HTTP header fields the server returns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allHTTPResponseHeaderFields: [String : String]? { get }
```

## See Also

### Getting information about the event

- [date](date.md) — The date and time when the error occurred.
- [URI](uri.md) — The URI of the playback item that had an error.
- [serverAddress](serveraddress.md) — The IP address of the server that was the source of the error.
- [playbackSessionID](playbacksessionid.md) — A GUID that identifies the playback session that had an error.
- [errorStatusCode](errorstatuscode.md) — A unique error code identifier.
- [errorDomain](errordomain.md) — The domain of the error.
- [errorComment](errorcomment.md) — A description of the error encountered.
