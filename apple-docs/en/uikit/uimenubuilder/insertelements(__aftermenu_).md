---
title: 'insertElements(_:afterMenu:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertelements(_:aftermenu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements(_:aftermenu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertelements%28_%3Aaftermenu%3A%29.json'
content_hash: 'sha256:0fbe4f96ed4af207'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertElements(_:afterMenu:)

<sub>Instance Method</sub>

Insert elements after an identified menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertElements(_ insertedElements: [UIMenuElement], afterMenu siblingIdentifier: UIMenu.Identifier)
```

## Parameters

- `insertedElements` — The elements to insert.

- `siblingIdentifier` — The identifier of the menu to insert elements after.
