---
title: NSComboButton
framework: AppKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscombobutton
source_url: 'https://developer.apple.com/documentation/appkit/nscombobutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscombobutton.json'
content_hash: 'sha256:8b07495dfd1a721c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AppKit](../appkit.md)

# NSComboButton

<sub>Class</sub>

A button with a pull-down menu and a default action.

<sub>macOS</sub>

```swift
class NSComboButton
```

## Overview

An [NSComboButton](nscombobutton.md) object is a button that displays a title string, image, and an optional control for displaying a menu. Use this control in places where you want to offer a button with a default action and one or more alternative actions. Clicking the title or image executes the default action you provide, and clicking the menu control displays a menu for selecting a different action. If you configure the button to hide the menu control, a long-press gesture displays the menu.

After you create a combo button programmatically or in Interface Builder, choose the button [style](nscombobutton/style-swift.property.md) you want and add a title or image for your content. A combo button has a default action, which you specify at creation time. You can also change that action later using the inherited [target](nscontrol/target.md) and [action](nscontrol/action.md) properties. To specify one or more alternative actions, configure a menu with those actions and assign it to the button’s [menu](nscombobutton/menu.md) property.

This control doesn’t use an [NSCell](nscell.md) object for its underlying implementation. It also doesn’t support the addition of a contextual menu.

## Relationships

- **Inherits From**: [NSControl](nscontrol.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md), [NSAccessibilityProtocol](nsaccessibilityprotocol.md), [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md), [NSAppearanceCustomization](nsappearancecustomization.md), [NSCoding](../foundation/nscoding.md), [NSDraggingDestination](nsdraggingdestination.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md), [NSTouchBarProvider](nstouchbarprovider.md), [NSUserActivityRestoring](nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a Combo Button

- [+ comboButtonWithTitle:image:menu:target:action:](<nscombobutton/init(title_image_menu_target_action_).md>) — Creates a combo button that displays both a title and image.
- [+ comboButtonWithTitle:menu:target:action:](<nscombobutton/init(title_menu_target_action_).md>) — Creates a combo button that displays a title.
- [+ comboButtonWithImage:menu:target:action:](<nscombobutton/init(image_menu_target_action_).md>) — Creates a combo button that displays an image.

### Configuring the Button Appearance

- [style](nscombobutton/style-swift.property.md) — The appearance setting that determines how the button presents its menu .
- [Style](nscombobutton/style-swift.enum.md) — Constants that indicate how a combo button presents its menu.
- [title](nscombobutton/title.md) — The localized string that the button displays.
- [image](nscombobutton/image.md) — The image that the button displays.
- [imageScaling](nscombobutton/imagescaling.md) — The scaling behavior to apply to the button’s image.

### Specifying the Alternative Actions

- [menu](nscombobutton/menu.md) — The menu that contains the button’s alternate actions.

## See Also

### Controls

- [Responding to control-based events using target-action](../uikit/responding-to-control-based-events-using-target-action.md) — Handle user input by connecting buttons, sliders, and other controls to your app’s code using the target-action design pattern.
- [NSButton](nsbutton.md) — A control that defines an area on the screen that a user clicks to trigger an action.
- [NSColorWell](nscolorwell.md) — A control that displays a color value and lets the user change that color value.
- [Combo Box](combo-box.md) — Display a list of values in a pop-up menu that lets the user select a value or type in a custom value.
- [Date Picker](date-picker.md) — Display a calendar date and provide controls for editing the date value.
- [NSImageView](nsimageview.md) — A display of image data in a frame.
- [NSLevelIndicator](nslevelindicator.md) — A visual representation of a level or quantity, using discrete values.
- [Path Control](path-control.md) — A display of a file system path or virtual path information.
- [NSPopUpButton](nspopupbutton.md) — A control for selecting an item from a list.
- [NSProgressIndicator](nsprogressindicator.md) — An interface that provides visual feedback to the user about the status of an ongoing task.
- [NSRuleEditor](nsruleeditor.md) — An interface for configuring a rule-based list of options.
- [NSPredicateEditor](nspredicateeditor.md) — A defined set of rules that allows the editing of predicate objects.
- [Search Field](search-field.md) — Provide a text field that is optimized for text-based search interfaces.
- [NSSegmentedControl](nssegmentedcontrol.md) — Display one or more buttons in a single horizontal group.
- [Slider](slider.md) — Display a range of values from which the user selects a single value.
