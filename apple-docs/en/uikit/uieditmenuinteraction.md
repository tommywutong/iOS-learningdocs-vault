---
title: UIEditMenuInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieditmenuinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuinteraction.json'
content_hash: 'sha256:8eaab8344d43f751'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIEditMenuInteraction

<sub>Class</sub>

An interaction that provides edit operations using a menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIEditMenuInteraction
```

## Overview

Edit menu interactions provide edit actions — such as cut, copy, and paste — for the content a view displays. The presentation style the interaction uses to display the actions conforms to the input method of the interaction. For touch interactions, the actions display in an editing menu. When responding to a secondary click on devices with pointer-based input, the actions display in a context menu.

Standard UIKit classes, such as [UITextView](uitextview.md) and [UITextField](uitextfield.md), are preconfigured to use edit menu interactions.

To add an edit menu interaction to a generic view:

1. Create an edit menu interaction object, and pass an optional delegate into the default initializer.
2. Call the [- addInteraction:](<uiview/addinteraction(__).md>) method on your view to add the interaction.
3. Create a gesture recognizer to trigger the interaction and add it to the view.

The following example creates an edit menu interaction triggered by a long press.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // Add the edit menu interaction.
    editMenuInteraction = UIEditMenuInteraction(delegate: self)
    interactionView.addInteraction(editMenuInteraction!)

    // Create the gesture recognizer.
    let longPress = UILongPressGestureRecognizer(target: self, action: #selector(didLongPress(_:)))
    longPress.allowedTouchTypes = [UITouch.TouchType.direct.rawValue as NSNumber]
    interactionView.addGestureRecognizer(longPress)
}

@objc func didLongPress(_ recognizer: UIGestureRecognizer) {
    let location = recognizer.location(in: self.view)
    let configuration = UIEditMenuConfiguration(identifier: nil, sourcePoint: location)

    if let interaction = editMenuInteraction {
        // Present the edit menu interaction.
        interaction.presentEditMenu(with: configuration)
    }
}
```

By default, an edit menu interaction generates a menu that includes commands for the standard edit actions your view implements. For more information on these actions, see [UIResponderStandardEditActions](uiresponderstandardeditactions.md). You can use the interaction’s delegate to add additional items to the menu and set the target rectangle to display around using methods in the [UIEditMenuInteractionDelegate](uieditmenuinteractiondelegate.md) protocol. For text views, you can specify the items the menu displays for specific text ranges using methods from the [UITextViewDelegate](uitextviewdelegate.md), [UITextFieldDelegate](uitextfielddelegate.md), or [UITextInput](uitextinput.md) protocols.

> [!note] Related Sessions from WWDC22
> Session 10071: [Adopt desktop-class editing interactions](https://developer.apple.com/wwdc22/10071)

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Creating an edit menu interaction

- [- initWithDelegate:](<uieditmenuinteraction/init(delegate_).md>) — Initializes an edit menu interaction object with the delegate object you specify.

### Managing edit menu interactions

- [delegate](uieditmenuinteraction/delegate.md) — An object that customizes presentation of the menu and actions to display for an edit menu interaction.
- [- presentEditMenuWithConfiguration:](<uieditmenuinteraction/presenteditmenu(with_).md>) — Presents an edit menu using the object you provide for configuration.
- [- reloadVisibleMenu](<uieditmenuinteraction/reloadvisiblemenu().md>) — Updates the actions an edit menu displays.
- [- updateVisibleMenuPositionAnimated:](<uieditmenuinteraction/updatevisiblemenuposition(animated_).md>) — Updates the position of the currently visible menu with an option to animate the action.
- [- dismissMenu](<uieditmenuinteraction/dismissmenu().md>) — Dismiss the edit menu if present.
- [- locationInView:](<uieditmenuinteraction/location(in_).md>) — Returns the location of the user interaction in the specified view’s coordinate system.

## See Also

### Related Documentation

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md) — Optimize your iPad app’s user experience by adopting desktop-class enhancements for multitasking with Stage Manager, document interactions, text editing, search, and more.

### Edit menus

- [UIEditMenuInteractionDelegate](uieditmenuinteractiondelegate.md) — The methods for customizing the menu the interaction displays.
- [UIEditMenuConfiguration](uieditmenuconfiguration.md) — An object containing the configuration details for the menu your app presents in response to an edit menu interaction.
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md) — A set of standard methods that apps can adopt to support editing.
