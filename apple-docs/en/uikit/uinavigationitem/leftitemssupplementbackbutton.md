---
title: leftItemsSupplementBackButton
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationitem/leftitemssupplementbackbutton
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationitem/leftitemssupplementbackbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationitem/leftitemssupplementbackbutton.json'
content_hash: 'sha256:45a7d980e7c6fe86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationItem](../uinavigationitem.md)

# leftItemsSupplementBackButton

<sub>Instance Property</sub>

A Boolean value that indicates whether the left items display in addition to the Back button.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var leftItemsSupplementBackButton: Bool { get set }
```

## Discussion

Normally, the presence of custom left bar button items causes the Back button to be removed in favor of the custom items. Setting this property to [true](../../swift/true.md) causes the items in the [leftBarButtonItems](leftbarbuttonitems.md) or [leftBarButtonItem](leftbarbuttonitem.md) property to be displayed to the right of the Back button — that is, they’re displayed in addition to, not instead of, the Back button. When set to [false](../../swift/false.md), the items in those properties are displayed instead of the Back button. The default value of this property is [false](../../swift/false.md).

The value in the [hidesBackButton](hidesbackbutton.md) property still determines whether the Back button is actually displayed.

## See Also

### Getting and setting properties

- [prompt](prompt.md) — A single line of text that displays at the top of the navigation bar.
