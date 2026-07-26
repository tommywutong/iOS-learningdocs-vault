---
title: AVPlayerItemErrorLog
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemerrorlog
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemerrorlog.json'
content_hash: 'sha256:4a0d174a227fbc26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemErrorLog

<sub>Class</sub>

The error log associated with a player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemErrorLog
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing error data

- [events](avplayeritemerrorlog/events.md) — A chronologically ordered array of player item error log event objects.
- [- extendedLogData](<avplayeritemerrorlog/extendedlogdata().md>) — Returns a serialized representation of the error log in the Extended Log File Format.
- [extendedLogDataStringEncoding](avplayeritemerrorlog/extendedlogdatastringencoding.md) — The string encoding of the extended log data.

## See Also

### Accessing logging information

- [- accessLog](<avplayeritem/accesslog().md>) — Returns an object that represents a snapshot of the network access log. _(deprecated)_
- [AVPlayerItemAccessLog](avplayeritemaccesslog.md) — An object used to retrieve the access log associated with a player item.
- [AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md) — A single entry in a player item’s access log.
- [- errorLog](<avplayeritem/errorlog().md>) — Returns an object that represents a snapshot of the error log. _(deprecated)_
- [AVPlayerItemErrorLogEvent](avplayeritemerrorlogevent.md) — A single item in a player item’s error log.
