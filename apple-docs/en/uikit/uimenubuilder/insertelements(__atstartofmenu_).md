---
title: 'insertElements(_:atStartOfMenu:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertelements(_:atstartofmenu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements(_:atstartofmenu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertelements%28_%3Aatstartofmenu%3A%29.json'
content_hash: 'sha256:e90c3e209099877a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertElements(_:atStartOfMenu:)

<sub>Instance Method</sub>

Insert elements at the start of an identified parent menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertElements(_ childElements: [UIMenuElement], atStartOfMenu parentIdentifier: UIMenu.Identifier)
```

## Parameters

- `childElements` — The child elements to insert.

- `parentIdentifier` — The identifier of the parent menu to insert elements at the start of.
