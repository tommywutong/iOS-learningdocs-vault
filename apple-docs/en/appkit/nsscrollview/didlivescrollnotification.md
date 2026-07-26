---
title: didLiveScrollNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.9+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsscrollview/didlivescrollnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsscrollview/didlivescrollnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsscrollview/didlivescrollnotification.json'
content_hash: 'sha256:299b40d115e0ddac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSScrollView](../nsscrollview.md)

# didLiveScrollNotification

<sub>Type Property</sub>

Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.

<sub>macOS</sub>

```swift
class let didLiveScrollNotification: NSNotification.Name
```

## Discussion

Some user-initiated scrolls (for example, scrolling using legacy mice) are not bracketed by a “willStart/didEnd” notification pair.

The notification object is the scroll view performing the scroll.

To observe this notification using Swift concurrency, use [DidLiveScrollMessage](didlivescrollmessage.md).

## See Also

### Notifications

- [NSScrollViewWillStartLiveMagnifyNotification](willstartlivemagnifynotification.md) — Posted at the beginning of a magnify gesture.
- [NSScrollViewDidEndLiveMagnifyNotification](didendlivemagnifynotification.md) — Posted at the end of a magnify gesture.
- [NSScrollViewWillStartLiveScrollNotification](willstartlivescrollnotification.md) — Posted on the main thread at the beginning of user-initiated live scroll tracking (gesture scroll or scroller tracking, for example, thumb dragging).
- [NSScrollViewDidEndLiveScrollNotification](didendlivescrollnotification.md) — Posted on the main thread at the end of live scroll tracking.
