---
title: 'setActions(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uimutableusernotificationcategory/setactions(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/setactions(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableusernotificationcategory/setactions%28_%3Afor%3A%29.json'
content_hash: 'sha256:a3d54eb675a48767'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableUserNotificationCategory](../uimutableusernotificationcategory.md)

# setActions(_:for:)

<sub>Instance Method</sub>

Sets the actions to display for different alert styles.

> [!warning] Deprecated
> For more information, see [UIMutableUserNotificationCategory](../uimutableusernotificationcategory.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setActions(_ actions: [UIUserNotificationAction]?, for context: UIUserNotificationActionContext)
```

## Parameters

- `actions` — An array of [UIUserNotificationAction](../uiusernotificationaction.md) objects representing the actions to display for the given context. When displaying the notification to the user, the system displays the action buttons using the same order as the items in this array. If you specify `nil` or an empty array, this method removes the actions for the specified context.

- `context` — The context in which the alert is displayed. For a list of possible values, see [UIUserNotificationActionContext](../uiusernotificationactioncontext.md).

## Discussion

Use this method to set or change the actions associated with a specific context.

## See Also

### Modifying the action settings

- [identifier](identifier.md) — The name of the action group. _(deprecated)_
