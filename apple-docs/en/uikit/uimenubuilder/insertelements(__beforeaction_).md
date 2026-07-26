---
title: 'insertElements(_:beforeAction:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertelements(_:beforeaction:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements(_:beforeaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertelements%28_%3Abeforeaction%3A%29.json'
content_hash: 'sha256:c0b23481e24145d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertElements(_:beforeAction:)

<sub>Instance Method</sub>

Insert elements before an identified action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertElements(_ insertedElements: [UIMenuElement], beforeAction siblingIdentifier: UIAction.Identifier)
```

## Parameters

- `insertedElements` — The elements to insert.

- `siblingIdentifier` — The identifier of the action to insert elements before.
