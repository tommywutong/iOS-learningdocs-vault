---
title: UIAlertAction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uialertaction
source_url: 'https://developer.apple.com/documentation/uikit/uialertaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uialertaction.json'
content_hash: 'sha256:cdb57f91a9a9e170'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAlertAction

<sub>Class</sub>

An action that can be taken when the user taps a button in an alert.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIAlertAction
```

## Overview

You use this class to configure information about a single action, including the title to display in the button, any styling information, and a handler to execute when the user taps the button. After creating an alert action object, add it to a [UIAlertController](uialertcontroller.md) object before displaying the corresponding alert to the user.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md)

## Topics

### Creating an alert action

- [+ actionWithTitle:style:handler:](<uialertaction/init(title_style_handler_).md>) — Create and return an action with the specified title and behavior.

### Getting the action’s attributes

- [title](uialertaction/title.md) — The title of the action’s button.
- [style](uialertaction/style-swift.property.md) — The style that applies to the action’s button.
- [enabled](uialertaction/isenabled.md) — A Boolean value indicating whether the action is currently enabled.

### Constants

- [Style](uialertaction/style-swift.enum.md) — Styles to apply to action buttons in an alert.

## See Also

### Alerts

- [Getting the user’s attention with alerts and action sheets](getting-the-user-s-attention-with-alerts-and-action-sheets.md) — Present important information to a person or prompt them about an important choice.
- [UIAlertController](uialertcontroller.md) — An object that displays an alert message.
