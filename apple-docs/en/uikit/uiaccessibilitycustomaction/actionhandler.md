---
title: actionHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycustomaction/actionhandler
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/actionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomaction/actionhandler.json'
content_hash: 'sha256:6bbad36819c0e174'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomAction](../uiaccessibilitycustomaction.md)

# actionHandler

<sub>Instance Property</sub>

A handler to perform for the action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var actionHandler: UIAccessibilityCustomAction.Handler? { get set }
```

## Discussion

If you set this property, the system chooses this action handler over the [target](target.md) and [selector](selector.md).

## See Also

### Accessing the action parameters

- [name](name.md) — The localized name of the action.
- [attributedName](attributedname.md) — The localized name of the action as an attributed string.
- [image](image.md) — An image that represents the action in assistive apps.
- [target](target.md) — The object that performs the action.
- [selector](selector.md) — The method that performs the action.
- [Handler](handler.md) — A closure type that defines a handler to perform for an action.
