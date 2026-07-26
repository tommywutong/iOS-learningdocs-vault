---
title: 'insertElements(_:atEndOfMenu:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertelements(_:atendofmenu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements(_:atendofmenu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertelements%28_%3Aatendofmenu%3A%29.json'
content_hash: 'sha256:b4543530ae007fd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertElements(_:atEndOfMenu:)

<sub>Instance Method</sub>

Insert elements at the end of an identified parent menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertElements(_ childElements: [UIMenuElement], atEndOfMenu parentIdentifier: UIMenu.Identifier)
```

## Parameters

- `childElements` — The child elements to insert.

- `parentIdentifier` — The identifier of the parent menu to insert elements at the end of.
