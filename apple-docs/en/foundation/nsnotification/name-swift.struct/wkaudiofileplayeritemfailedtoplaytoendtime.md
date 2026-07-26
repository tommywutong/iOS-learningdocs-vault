---
title: WKAudioFilePlayerItemFailedToPlayToEndTime
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 2.0+（6.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/wkaudiofileplayeritemfailedtoplaytoendtime
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/wkaudiofileplayeritemfailedtoplaytoendtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/wkaudiofileplayeritemfailedtoplaytoendtime.json'
content_hash: 'sha256:5298965c5226bbc7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# WKAudioFilePlayerItemFailedToPlayToEndTime

<sub>Type Property</sub>

A notification that the item failed to play to its end.

> [!warning] Deprecated
> Use the [AVFoundation](../../../avfoundation.md) framework’s [AVPlayer](../../../avfoundation/avplayer.md) and [AVQueuePlayer](../../../avfoundation/avqueueplayer.md) classes instead.

<sub>watchOS</sub>

```swift
static let WKAudioFilePlayerItemFailedToPlayToEndTime: NSNotification.Name
```

## Discussion

The notification’s object is the player item. There is no `userInfo` dictionary.

## See Also

### WatchKit

- [WKAccessibilityReduceMotionStatusDidChange](wkaccessibilityreducemotionstatusdidchange.md) — Tells the interface controller that the reduce motion status has changed.
- [WKAudioFilePlayerItemDidPlayToEndTime](wkaudiofileplayeritemdidplaytoendtime.md) — A notification that the item has played successfully to its end. _(deprecated)_
- [WKAudioFilePlayerItemTimeJumped](wkaudiofileplayeritemtimejumped.md) — A notification that the item’s current time has changed discontinuously. _(deprecated)_
