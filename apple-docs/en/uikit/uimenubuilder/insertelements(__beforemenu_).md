---
title: 'insertElements(_:beforeMenu:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertelements(_:beforemenu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements(_:beforemenu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertelements%28_%3Abeforemenu%3A%29.json'
content_hash: 'sha256:5ba3135299160964'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertElements(_:beforeMenu:)

<sub>Instance Method</sub>

Insert elements before an identified menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertElements(_ insertedElements: [UIMenuElement], beforeMenu siblingIdentifier: UIMenu.Identifier)
```

## Parameters

- `insertedElements` — The elements to insert.

- `siblingIdentifier` — The identifier of the menu to insert elements before.
