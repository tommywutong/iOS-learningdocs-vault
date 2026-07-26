---
title: 'init(name:target:selector:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaccessibilitycustomaction/init(name:target:selector:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/init(name:target:selector:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomaction/init%28name%3Atarget%3Aselector%3A%29.json'
content_hash: 'sha256:00650f2b6cd95f70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibilityCustomAction](../uiaccessibilitycustomaction.md)

# init(name:target:selector:)

<sub>Initializer</sub>

Creates a custom action object with the specified name, target, and selector.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(name: String, target: Any?, selector: Selector)
```

## Parameters

- `name` — The localized name of the action. Provide a short and descriptive name for the action.

- `target` — The object that performs the action.

- `selector` — The selector of `target` to call when you want to perform the action. The method signature must take one of the following forms: ```objc - (BOOL)myPerformActionMethod - (BOOL)myPerformActionMethod:(UIAccessibilityCustomAction *)action ```

## Return Value

An initialized custom action object.

## See Also

### Creating a custom action

- [- initWithName:actionHandler:](<init(name_actionhandler_).md>) — Creates a custom action object with the specified name and action handler.
- [- initWithName:image:actionHandler:](<init(name_image_actionhandler_).md>) — Creates a custom action object with the specified name, image, and action handler.
- [- initWithName:image:target:selector:](<init(name_image_target_selector_).md>) — Creates a custom action object with the specified name, image, target, and selector.
- [- initWithAttributedName:actionHandler:](<init(attributedname_actionhandler_).md>) — Creates a custom action object with the specified attributed name and action handler.
- [- initWithAttributedName:target:selector:](<init(attributedname_target_selector_).md>) — Creates a custom action object with the specified attributed name, target, and selector.
- [- initWithAttributedName:image:actionHandler:](<init(attributedname_image_actionhandler_).md>) — Creates a custom action object with the specified attributed name, image, and action handler.
- [- initWithAttributedName:image:target:selector:](<init(attributedname_image_target_selector_).md>) — Creates a custom action object with the specified attributed name, image, target, and selector.
