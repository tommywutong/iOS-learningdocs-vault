---
title: shortcutItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/connectionoptions/shortcutitem
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/shortcutitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/connectionoptions/shortcutitem.json'
content_hash: 'sha256:da10ab814fe7ef5f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ConnectionOptions](../connectionoptions.md)

# shortcutItem

<sub>Instance Property</sub>

The user-selected action to perform.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var shortcutItem: UIApplicationShortcutItem? { get }
```

## Discussion

If the user selected one of your app’s quick actions, this property contains the selected action. You use quick actions to provide access to frequently used features of your app, and the user accesses those actions through interactions with your app’s icon in the Home Screen. If the user didn’t select a quick action, this property is `nil`.

For an example of how to set up quick actions for your app, see [Add Home Screen quick actions](../../add-home-screen-quick-actions.md).
