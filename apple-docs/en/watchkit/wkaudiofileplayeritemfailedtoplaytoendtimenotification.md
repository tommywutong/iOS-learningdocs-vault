---
title: WKAudioFilePlayerItemFailedToPlayToEndTimeNotification
framework: WatchKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [watchOS 2.0+（6.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/watchkit/wkaudiofileplayeritemfailedtoplaytoendtimenotification
source_url: 'https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritemfailedtoplaytoendtimenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/watchkit/wkaudiofileplayeritemfailedtoplaytoendtimenotification.json'
content_hash: 'sha256:e768f9f0d2f67a7f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WatchKit](../watchkit.md)

# WKAudioFilePlayerItemFailedToPlayToEndTimeNotification

<sub>Global Variable</sub>

A notification that the item failed to play to its end.

> [!warning] Deprecated
> Use the [AVFoundation](../avfoundation.md) framework’s [AVPlayer](../avfoundation/avplayer.md) and [AVQueuePlayer](../avfoundation/avqueueplayer.md) classes instead.

<sub>watchOS</sub>

```objc
extern NSString * const WKAudioFilePlayerItemFailedToPlayToEndTimeNotification;
```

## Discussion

The notification’s object is the player item. There is no `userInfo` dictionary.

## See Also

### Receiving Notifications

- [WKAudioFilePlayerItemTimeJumpedNotification](wkaudiofileplayeritemtimejumpednotification.md) — A notification that the item’s current time has changed discontinuously. _(deprecated)_
- [WKAudioFilePlayerItemDidPlayToEndTimeNotification](wkaudiofileplayeritemdidplaytoendtimenotification.md) — A notification that the item has played successfully to its end. _(deprecated)_
