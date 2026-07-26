---
title: events
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemerrorlog/events
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/events'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemerrorlog/events.json'
content_hash: 'sha256:217c59030d0a4a69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemErrorLog](../avplayeritemerrorlog.md)

# events

<sub>Instance Property</sub>

A chronologically ordered array of player item error log event objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var events: [AVPlayerItemErrorLogEvent] { get }
```

## Discussion

The array contains [AVPlayerItemErrorLogEvent](../avplayeritemerrorlogevent.md) objects that represent the chronological sequence of events contained in the error log.

This property isn’t observable. For more information about key-value observing, see [Using Key-Value Observing in Swift](../../swift/using-key-value-observing-in-swift.md).

## See Also

### Accessing error data

- [- extendedLogData](<extendedlogdata().md>) — Returns a serialized representation of the error log in the Extended Log File Format.
- [extendedLogDataStringEncoding](extendedlogdatastringencoding.md) — The string encoding of the extended log data.
