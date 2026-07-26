---
title: didResizeSubviewsNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nssplitview/didresizesubviewsnotification
source_url: 'https://developer.apple.com/documentation/appkit/nssplitview/didresizesubviewsnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nssplitview/didresizesubviewsnotification.json'
content_hash: 'sha256:f391946cdc90f162'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSSplitView](../nssplitview.md)

# didResizeSubviewsNotification

<sub>Type Property</sub>

A notification that posts after a change to the size of some or all subviews of a split view.

<sub>macOS</sub>

```swift
class let didResizeSubviewsNotification: NSNotification.Name
```

## Discussion

The notification object consists of the [NSSplitView](../nssplitview.md) that has resized its subviews.

The [userInfo](../../foundation/notification/userinfo.md) dictionary includes the `NSSplitViewDividerIndex` key that contains the index of the divider that the split view or the user moves. If the system sends the notification because the user drags a divider, the dictionary also includes the `NSSplitViewUserResizeKey` key with a value of `1`.

To observe this notification using Swift concurrency, use [DidResizeSubviewsMessage](didresizesubviewsmessage.md).

## See Also

### Managing Notifications

- [NSSplitViewWillResizeSubviewsNotification](willresizesubviewsnotification.md) — A notification that posts before a change to the size of some or all subviews of a split view.
