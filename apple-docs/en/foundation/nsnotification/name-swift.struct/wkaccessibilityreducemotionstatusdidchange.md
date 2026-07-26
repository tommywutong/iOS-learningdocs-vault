---
title: WKAccessibilityReduceMotionStatusDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [watchOS 4.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/wkaccessibilityreducemotionstatusdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/wkaccessibilityreducemotionstatusdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/wkaccessibilityreducemotionstatusdidchange.json'
content_hash: 'sha256:22e2b4e095b38cee'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# WKAccessibilityReduceMotionStatusDidChange

<sub>Type Property</sub>

Tells the interface controller that the reduce motion status has changed.

<sub>watchOS</sub>

```swift
static let WKAccessibilityReduceMotionStatusDidChange: NSNotification.Name
```

## Discussion

Use this notification to customize your application’s user interface for when reduced motion is enabled. You can also use the [WKAccessibilityIsReduceMotionEnabled()](<../../../watchkit/wkaccessibilityisreducemotionenabled().md>) function to determine whether reduced motion is enabled.

Observe this notification using the default notification center. This notification doesn’t include a parameter.

## See Also

### WatchKit

- [WKAudioFilePlayerItemDidPlayToEndTime](wkaudiofileplayeritemdidplaytoendtime.md) — A notification that the item has played successfully to its end. _(deprecated)_
- [WKAudioFilePlayerItemFailedToPlayToEndTime](wkaudiofileplayeritemfailedtoplaytoendtime.md) — A notification that the item failed to play to its end. _(deprecated)_
- [WKAudioFilePlayerItemTimeJumped](wkaudiofileplayeritemtimejumped.md) — A notification that the item’s current time has changed discontinuously. _(deprecated)_
