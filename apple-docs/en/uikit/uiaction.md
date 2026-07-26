---
title: UIAction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaction
source_url: 'https://developer.apple.com/documentation/uikit/uiaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaction.json'
content_hash: 'sha256:cf9ae7e1e262eca9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAction

<sub>Class</sub>

A menu element that performs its action in a closure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIAction
```

## Overview

Create a [UIAction](uiaction.md) object when you want a menu element that performs its action in a closure. The following example adds an action-based menu to the File menu:

```swift
// Create a closure-based action to use as a menu element.
let refreshAction = UIAction(title: "Refresh") { (action) in
    print("Refresh the data.")
}

// Use the .displayInline option to avoid displaying the menu as a submenu,
// and to separate it from the other menu elements using a line separator.
let refreshMenuItem = UIMenu(title: "", options: .displayInline, children: [refreshAction])

// Insert the menu into the File menu before the Close menu.
builder.insertSibling(refreshMenuItem, beforeMenu: .close)
```

## Relationships

- **Inherits From**: [UIMenuElement](uimenuelement.md)

- **Inherited By**: [ActivationAction](uiwindowscene/activationaction.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIMenuLeaf](uimenuleaf.md)

## Topics

### Creating an action

- [init(title:subtitle:image:identifier:discoverabilityTitle:attributes:state:handler:)](<uiaction/init(title_subtitle_image_identifier_discoverabilitytitle_attributes_state_handler_).md>) — Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [init(title:image:identifier:discoverabilityTitle:attributes:state:handler:)](<uiaction/init(title_image_identifier_discoverabilitytitle_attributes_state_handler_).md>) — Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [+ captureTextFromCameraActionForResponder:identifier:](<uiaction/capturetextfromcamera(responder_identifier_).md>) — Creates an action for capturing text using the device’s camera.
- [Identifier](uiaction/identifier-swift.struct.md) — A type that represents an action identifier.
- [UIActionHandler](uiactionhandler.md) — A type that defines the closure for an action handler.

### Getting information about the action

- [title](uiaction/title.md) — The action’s title.
- [image](uiaction/image.md) — The action’s image.
- [identifier](uiaction/identifier-swift.property.md) — The unique identifier for the action.
- [discoverabilityTitle](uiaction/discoverabilitytitle.md) — An elaborated title that explains the purpose of the action.
- [attributes](uiaction/attributes.md) — The attributes indicating the style of the action.
- [state](uiaction/state.md) — The state of the action.
- [sender](uiaction/sender.md) — The object responsible for the action handler.

### Initializers

- [init(title:subtitle:image:selectedImage:identifier:discoverabilityTitle:attributes:state:handler:)](<uiaction/init(title_subtitle_image_selectedimage_identifier_discoverabilitytitle_attributes_state_handler_).md>)
- [init(title:subtitle:image:selectedImage:preferredImageVisibility:identifier:discoverabilityTitle:attributes:state:handler:)](<uiaction/init(title_subtitle_image_selectedimage_preferredimagevisibility_identifier_discoverabilitytitle_attributes_state_handler_).md>)

## See Also

### Menu elements and keyboard shortcuts

- [Adding menus and shortcuts to the menu bar and user interface](adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Adopting menus and UIActions in your user interface](adopting-menus-and-uiactions-in-your-user-interface.md) — Add menus to your user interface, with built-in button support and bar-button items, and create custom menu experiences.
- [UIMenuElement](uimenuelement.md) — An object representing a menu, action, or command.
- [UICommand](uicommand.md) — A menu element that performs its action in a selector.
- [UIKeyCommand](uikeycommand.md) — An object that specifies a key press perform on a hardware keyboard and the resulting action.
- [UIDeferredMenuElement](uideferredmenuelement.md) — A placeholder menu element that the system replaces with the result of the block’s completion handler.
- [Provider](uideferredmenuelement/provider.md)
- [Attributes](uimenuelement/attributes.md) — Attributes that determine the style of the menu element.
- [State](uimenuelement/state.md) — Constants that indicate the state of an action- or command-based menu element.
- [UIMenuLeaf](uimenuleaf.md) — An interface for an object that represents a menu element without child elements.
