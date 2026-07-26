---
title: errorLog()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.3+（27.0 起废弃）, iPadOS 4.3+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avplayeritem/errorlog()
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/errorlog()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/errorlog%28%29.json'
content_hash: 'sha256:250a98c8120ec51b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# errorLog()

<sub>Instance Method</sub>

Returns an object that represents a snapshot of the error log.

> [!warning] Deprecated
> Use fetchErrorLogWithCompletionHandler:

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func errorLog() -> AVPlayerItemErrorLog?
```

## Return Value

An object that represents a snapshot of the error log. The returned value can be `nil`.

## Discussion

If the method returns `nil`, there is no logging information currently available for the player item.

## See Also

### Accessing logging information

- [- accessLog](<accesslog().md>) — Returns an object that represents a snapshot of the network access log. _(deprecated)_
- [AVPlayerItemAccessLog](../avplayeritemaccesslog.md) — An object used to retrieve the access log associated with a player item.
- [AVPlayerItemAccessLogEvent](../avplayeritemaccesslogevent.md) — A single entry in a player item’s access log.
- [AVPlayerItemErrorLog](../avplayeritemerrorlog.md) — The error log associated with a player item.
- [AVPlayerItemErrorLogEvent](../avplayeritemerrorlogevent.md) — A single item in a player item’s error log.
