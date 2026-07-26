---
title: identifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/identifier
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/identifier.json'
content_hash: 'sha256:56c64c0f104439fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# identifier

<sub>Instance Property</sub>

An identifier used to match bar button items across transitions in a navigation bar or toolbar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var identifier: String? { get set }
```

## Discussion

When the set of bar button items in a navigation bar or toolbar changes (for example, when pushing or popping view controllers), UIKit automatically animates the transition between the different sets of items. By default, UIKit uses heuristics based on item position and content to determine which items should be matched for these transitions.

Set this property with the same value on two different bar button items in different navigation item configurations to indicate that they should be treated as the same item during transitions. This allows for more natural animations when the visuals or function of an item changes across contexts.

The default value is `nil`, which means UIKit will use its default heuristics for transitions.
