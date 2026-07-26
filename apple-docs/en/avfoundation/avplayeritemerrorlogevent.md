---
title: AVPlayerItemErrorLogEvent
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemerrorlogevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemerrorlogevent.json'
content_hash: 'sha256:8821387fb722552f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemErrorLogEvent

<sub>Class</sub>

A single item in a player item’s error log.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemErrorLogEvent
```

## Overview

This object provides properties for accessing the data fields of each log event. Each event is a single entry in an [AVPlayerItem](avplayeritem.md) object’s error log.

These properties aren’t observable. For more information about key-value observing, see [Using Key-Value Observing in Swift](../swift/using-key-value-observing-in-swift.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting information about the event

- [date](avplayeritemerrorlogevent/date.md) — The date and time when the error occurred.
- [URI](avplayeritemerrorlogevent/uri.md) — The URI of the playback item that had an error.
- [serverAddress](avplayeritemerrorlogevent/serveraddress.md) — The IP address of the server that was the source of the error.
- [playbackSessionID](avplayeritemerrorlogevent/playbacksessionid.md) — A GUID that identifies the playback session that had an error.
- [errorStatusCode](avplayeritemerrorlogevent/errorstatuscode.md) — A unique error code identifier.
- [errorDomain](avplayeritemerrorlogevent/errordomain.md) — The domain of the error.
- [errorComment](avplayeritemerrorlogevent/errorcomment.md) — A description of the error encountered.
- [allHTTPResponseHeaderFields](avplayeritemerrorlogevent/allhttpresponseheaderfields.md) — The HTTP header fields the server returns.

## See Also

### Accessing logging information

- [- accessLog](<avplayeritem/accesslog().md>) — Returns an object that represents a snapshot of the network access log. _(deprecated)_
- [AVPlayerItemAccessLog](avplayeritemaccesslog.md) — An object used to retrieve the access log associated with a player item.
- [AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md) — A single entry in a player item’s access log.
- [- errorLog](<avplayeritem/errorlog().md>) — Returns an object that represents a snapshot of the error log. _(deprecated)_
- [AVPlayerItemErrorLog](avplayeritemerrorlog.md) — The error log associated with a player item.
