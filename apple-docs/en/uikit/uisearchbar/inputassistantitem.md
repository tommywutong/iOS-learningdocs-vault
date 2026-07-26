---
title: inputAssistantItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/inputassistantitem
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/inputassistantitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/inputassistantitem.json'
content_hash: 'sha256:ee4050579aad7d20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# inputAssistantItem

<sub>Instance Property</sub>

The input assistant to use for configuring the keyboard’s shortcuts bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var inputAssistantItem: UITextInputAssistantItem { get }
```

## Discussion

When search is engaged on iPad, the shortcuts bar above the keyboard contains typing suggestions and may contain other controls for managing text. This property contains the object you use to configure the custom bar button items above the keyboard. The shortcuts bar is not available on iPhone or iPod Touch.

For more information about how to configure shortcut items, see [UITextInputAssistantItem](../uitextinputassistantitem.md).
