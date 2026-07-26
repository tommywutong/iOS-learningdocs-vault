---
title: 'init(customView:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarbuttonitem/init(customview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(customview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/init%28customview%3A%29.json'
content_hash: 'sha256:dc4066895db4ef38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# init(customView:)

<sub>Initializer</sub>

Creates an item using the specified custom view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(customView: UIView)
```

## Parameters

- `customView` — A custom view representing the item.

## Return Value

A newly initialized [UIBarButtonItem](../uibarbuttonitem.md).

## Discussion

The bar button item created by this method doesn’t call the action method of its target in response to user interactions. Instead, the bar button item expects the specified custom view to handle any user interactions and provide an appropriate response.
