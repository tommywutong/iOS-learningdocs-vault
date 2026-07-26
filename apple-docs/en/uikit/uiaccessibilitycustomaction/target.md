---
title: target
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycustomaction/target
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/target'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomaction/target.json'
content_hash: 'sha256:75390c4ea4edd9da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomAction](../uiaccessibilitycustomaction.md)

# target

<sub>Instance Property</sub>

The object that performs the action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var target: AnyObject? { get set }
```

## See Also

### Accessing the action parameters

- [name](name.md) — The localized name of the action.
- [attributedName](attributedname.md) — The localized name of the action as an attributed string.
- [image](image.md) — An image that represents the action in assistive apps.
- [actionHandler](actionhandler.md) — A handler to perform for the action.
- [selector](selector.md) — The method that performs the action.
- [Handler](handler.md) — A closure type that defines a handler to perform for an action.
