---
title: children
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenu/children
source_url: 'https://developer.apple.com/documentation/uikit/uimenu/children'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenu/children.json'
content_hash: 'sha256:fe3e54805c267762'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenu](../uimenu.md)

# children

<sub>Instance Property</sub>

The contents of the menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var children: [UIMenuElement] { get }
```

## Discussion

If the menu doesn’t have any child menu elements, this property contains an empty array.

## See Also

### Accessing child elements

- [- menuByReplacingChildren:](<replacingchildren(__).md>) — Creates a new menu with the same configuration as the current menu, but with a new set of child elements.
