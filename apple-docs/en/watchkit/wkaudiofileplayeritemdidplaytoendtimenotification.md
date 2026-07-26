---
title: WKAudioFilePlayerItemDidPlayToEndTimeNotification
framework: WatchKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [watchOS 2.0+（6.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/watchkit/wkaudiofileplayeritemdidplaytoendtimenotification
source_url: 'https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemdidplaytoendtimenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/watchkit/wkaudiofileplayeritemdidplaytoendtimenotification.json'
content_hash: 'sha256:2096635ecf0501e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WatchKit](../watchkit.md)

# WKAudioFilePlayerItemDidPlayToEndTimeNotification

<sub>Global Variable</sub>

A notification that the item has played successfully to its end.

> [!warning] Deprecated
> Use the [AVFoundation](../avfoundation.md) framework’s [AVPlayer](../avfoundation/avplayer.md) and [AVQueuePlayer](../avfoundation/avqueueplayer.md) classes instead.

<sub>watchOS</sub>

```objc
extern NSString * const WKAudioFilePlayerItemDidPlayToEndTimeNotification;
```

## Discussion

The notification’s object is the player item. There is no `userInfo` dictionary.

## See Also

### Receiving Notifications

- [WKAudioFilePlayerItemTimeJumpedNotification](wkaudiofileplayeritemtimejumpednotification.md) — A notification that the item’s current time has changed discontinuously. _(deprecated)_
- [WKAudioFilePlayerItemFailedToPlayToEndTimeNotification](wkaudiofileplayeritemfailedtoplaytoendtimenotification.md) — A notification that the item failed to play to its end. _(deprecated)_
