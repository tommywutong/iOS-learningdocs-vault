---
title: selector
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycustomaction/selector
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/selector'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomaction/selector.json'
content_hash: 'sha256:7256153ca9c35f86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomAction](../uiaccessibilitycustomaction.md)

# selector

<sub>Instance Property</sub>

The method that performs the action.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selector: Selector { get set }
```

## Discussion

The signature of the selector must take one of the following forms:

```objc
- (BOOL)myPerformActionMethod
- (BOOL)myPerformActionMethod:(UIAccessibilityCustomAction *)action
```

When the user selects a custom action, the assistive technology calls the specified method of the object in the [target](target.md) property. Use your method to perform the indicated action.

## See Also

### Accessing the action parameters

- [name](name.md) — The localized name of the action.
- [attributedName](attributedname.md) — The localized name of the action as an attributed string.
- [image](image.md) — An image that represents the action in assistive apps.
- [actionHandler](actionhandler.md) — A handler to perform for the action.
- [target](target.md) — The object that performs the action.
- [Handler](handler.md) — A closure type that defines a handler to perform for an action.
