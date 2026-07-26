---
title: UIUserNotificationActionContext.default
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiusernotificationactioncontext/default
source_url: 'https://developer.apple.com/documentation/uikit/uiusernotificationactioncontext/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiusernotificationactioncontext/default.json'
content_hash: 'sha256:2c61b005710e610b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIUserNotificationActionContext](../uiusernotificationactioncontext.md)

# UIUserNotificationActionContext.default

<sub>Case</sub>

The default context for displaying the alert.

> [!warning] Deprecated
> For more information, see [UIUserNotificationCategory](../uiusernotificationcategory.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case `default`
```

## Discussion

In this context, the full UI is displayed for the notification’s alert. You may specify up to four custom actions in this context.

## See Also

### Constants

- [UIUserNotificationActionContextMinimal](minimal.md) — A notification where space is minimal. _(deprecated)_
