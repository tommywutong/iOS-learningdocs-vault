---
title: UIAccessibilityCustomAction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycustomaction
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycustomaction.json'
content_hash: 'sha256:4212b65d254f0a5c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityCustomAction

<sub>Class</sub>

A custom action to perform on an accessible object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIAccessibilityCustomAction
```

## Overview

Apps that support custom actions can create instances of this class, specifying the user-readable name of the action and the object and selector to use when performing the action. Assistive apps display custom actions in response to specific user cues. For example, VoiceOver lets users access actions quickly using the Actions rotor.

After creating an instance of this class, add it to the [accessibilityCustomActions](../objectivec/nsobject-swift.class/accessibilitycustomactions.md) property of an appropriate accessible object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a custom action

- [- initWithName:actionHandler:](<uiaccessibilitycustomaction/init(name_actionhandler_).md>) — Creates a custom action object with the specified name and action handler.
- [- initWithName:target:selector:](<uiaccessibilitycustomaction/init(name_target_selector_).md>) — Creates a custom action object with the specified name, target, and selector.
- [- initWithName:image:actionHandler:](<uiaccessibilitycustomaction/init(name_image_actionhandler_).md>) — Creates a custom action object with the specified name, image, and action handler.
- [- initWithName:image:target:selector:](<uiaccessibilitycustomaction/init(name_image_target_selector_).md>) — Creates a custom action object with the specified name, image, target, and selector.
- [- initWithAttributedName:actionHandler:](<uiaccessibilitycustomaction/init(attributedname_actionhandler_).md>) — Creates a custom action object with the specified attributed name and action handler.
- [- initWithAttributedName:target:selector:](<uiaccessibilitycustomaction/init(attributedname_target_selector_).md>) — Creates a custom action object with the specified attributed name, target, and selector.
- [- initWithAttributedName:image:actionHandler:](<uiaccessibilitycustomaction/init(attributedname_image_actionhandler_).md>) — Creates a custom action object with the specified attributed name, image, and action handler.
- [- initWithAttributedName:image:target:selector:](<uiaccessibilitycustomaction/init(attributedname_image_target_selector_).md>) — Creates a custom action object with the specified attributed name, image, target, and selector.

### Accessing the action parameters

- [name](uiaccessibilitycustomaction/name.md) — The localized name of the action.
- [attributedName](uiaccessibilitycustomaction/attributedname.md) — The localized name of the action as an attributed string.
- [image](uiaccessibilitycustomaction/image.md) — An image that represents the action in assistive apps.
- [actionHandler](uiaccessibilitycustomaction/actionhandler.md) — A handler to perform for the action.
- [target](uiaccessibilitycustomaction/target.md) — The object that performs the action.
- [selector](uiaccessibilitycustomaction/selector.md) — The method that performs the action.
- [Handler](uiaccessibilitycustomaction/handler.md) — A closure type that defines a handler to perform for an action.

### Type Properties

- [UIAccessibilityCustomActionCategoryEdit](uiaccessibilitycustomaction/editcategory.md) — A constant that an app specifies through the category property on a UIKit accessibility custom action.
- [UIAccessibilityCustomActionCategoryEdit](uiaccessibilitycustomaction/editcategory.md) — A constant that an app specifies through the category property on a UIKit accessibility custom action.

### Instance Properties

- [category](uiaccessibilitycustomaction/category.md)

## See Also

### Actions

- [UIAccessibilityAction](../objectivec/uiaccessibilityaction.md) — A set of methods that accessibility elements can use to support specific actions.
- [Handler](uiaccessibilitycustomaction/handler.md) — A closure type that defines a handler to perform for an action.
- [Delivering an exceptional accessibility experience](../accessibility/delivering_an_exceptional_accessibility_experience.md) — Make improvements to your app’s interaction model to support assistive technologies such as VoiceOver.
