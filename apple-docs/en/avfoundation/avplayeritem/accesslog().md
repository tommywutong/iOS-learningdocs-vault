---
title: accessLog()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.3+（27.0 起废弃）, iPadOS 4.3+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayeritem/accesslog()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/accesslog()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/accesslog%28%29.json'
content_hash: 'sha256:dc64ae0b34660caf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# accessLog()

<sub>Instance Method</sub>

Returns an object that represents a snapshot of the network access log.

> [!warning] Deprecated
> Use fetchAccessLogWithCompletionHandler:

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func accessLog() -> AVPlayerItemAccessLog?
```

## Return Value

An object that represents a snapshot of the network access log. The returned value can be `nil`.

## Discussion

If the method returns `nil`, there is no logging information currently available for the player item.

## See Also

### Accessing logging information

- [AVPlayerItemAccessLog](../avplayeritemaccesslog.md) — An object used to retrieve the access log associated with a player item.
- [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md) — A single entry in a player item’s access log.
- [- errorLog](<errorlog().md>) — Returns an object that represents a snapshot of the error log. _(deprecated)_
- [AVPlayerItemErrorLog](../avplayeritemerrorlog.md) — The error log associated with a player item.
- [AVPlayerItemErrorLogEvent](../avplayeritemerrorlogevent.md) — A single item in a player item’s error log.
