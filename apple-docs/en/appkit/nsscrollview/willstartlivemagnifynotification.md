---
title: willStartLiveMagnifyNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.8+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsscrollview/willstartlivemagnifynotification
source_url: 'https://developer.apple.com/documentation/appkit/nsscrollview/willstartlivemagnifynotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsscrollview/willstartlivemagnifynotification.json'
content_hash: 'sha256:0838ee97b2f2a28a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSScrollView](../nsscrollview.md)

# willStartLiveMagnifyNotification

<sub>Type Property</sub>

Posted at the beginning of a magnify gesture.

<sub>macOS</sub>

```swift
class let willStartLiveMagnifyNotification: NSNotification.Name
```

## Discussion

The notification object is the scroll view performing the magnification.

This notification indicates that the magnification property is being changed due to user action. This may be due to the user performing a pinch gesture or a smart zoom gesture. When animating the magnification value yourself via the object’s animator, this notification is not sent.

To observe this notification using Swift concurrency, use [WillStartLiveMagnifyMessage](willstartlivemagnifymessage.md).

## See Also

### Notifications

- [NSScrollViewDidEndLiveMagnifyNotification](didendlivemagnifynotification.md) — Posted at the end of a magnify gesture.
- [NSScrollViewWillStartLiveScrollNotification](willstartlivescrollnotification.md) — Posted on the main thread at the beginning of user-initiated live scroll tracking (gesture scroll or scroller tracking, for example, thumb dragging).
- [NSScrollViewDidLiveScrollNotification](didlivescrollnotification.md) — Posted on the main thread after changing the clipview bounds origin due to a user-initiated event.
- [NSScrollViewDidEndLiveScrollNotification](didendlivescrollnotification.md) — Posted on the main thread at the end of live scroll tracking.
