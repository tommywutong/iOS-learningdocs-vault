---
title: serverAddress
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemerrorlogevent/serveraddress
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/serveraddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemerrorlogevent/serveraddress.json'
content_hash: 'sha256:4c6c2af9aa216181'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemErrorLogEvent](../avplayeritemerrorlogevent.md)

# serverAddress

<sub>Instance Property</sub>

The IP address of the server that was the source of the error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var serverAddress: String? { get }
```

## Discussion

The property corresponds to “s-ip”.

The value of this property can be either an IPv4 or IPv6 address, and may be `nil` if the address is unknown.

## See Also

### Getting information about the event

- [date](date.md) — The date and time when the error occurred.
- [URI](uri.md) — The URI of the playback item that had an error.
- [playbackSessionID](playbacksessionid.md) — A GUID that identifies the playback session that had an error.
- [errorStatusCode](errorstatuscode.md) — A unique error code identifier.
- [errorDomain](errordomain.md) — The domain of the error.
- [errorComment](errorcomment.md) — A description of the error encountered.
- [allHTTPResponseHeaderFields](allhttpresponseheaderfields.md) — The HTTP header fields the server returns.
