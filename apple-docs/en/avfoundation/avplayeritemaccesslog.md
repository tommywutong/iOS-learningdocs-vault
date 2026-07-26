---
title: AVPlayerItemAccessLog
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemaccesslog
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslog'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemaccesslog.json'
content_hash: 'sha256:62487ceadc4d6e80'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemAccessLog

<sub>Class</sub>

An object used to retrieve the access log associated with a player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemAccessLog
```

## Overview

An `AVPlayerItemAccessLog` object accumulates key metrics about network playback and presents them as a collection of [AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md) instances. Each event instance collates the data that relates to each uninterrupted period of playback.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing log data

- [events](avplayeritemaccesslog/events.md) — A chronologically ordered array of player item access log events.
- [- extendedLogData](<avplayeritemaccesslog/extendedlogdata().md>) — Returns a serialized representation of the access log in the Extended Log File Format.
- [extendedLogDataStringEncoding](avplayeritemaccesslog/extendedlogdatastringencoding.md) — The string encoding of the extended log data.

## See Also

### Accessing logging information

- [- accessLog](<avplayeritem/accesslog().md>) — Returns an object that represents a snapshot of the network access log. _(deprecated)_
- [AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md) — A single entry in a player item’s access log.
- [- errorLog](<avplayeritem/errorlog().md>) — Returns an object that represents a snapshot of the error log. _(deprecated)_
- [AVPlayerItemErrorLog](avplayeritemerrorlog.md) — The error log associated with a player item.
- [AVPlayerItemErrorLogEvent](avplayeritemerrorlogevent.md) — A single item in a player item’s error log.
