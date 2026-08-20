---
title: Color Programming Topics
apple_id: 10000082i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DrawColor/Tasks/ChoosingColors.html
archived_at: '2026-07-15T07:15:15.569054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Color Programming Topics](Introduction%20to%20Color%20Programming%20Topics%20for%20Cocoa.md)


[Next](Choosing%20the%20Color%20Pickers%20in%20a%20Color%20Panel.md)[Previous](Using%20the%20System%20Control%20Tint.md)

# Choosing Colors With Color Wells and Color Panels

A color well displays and lets the user select a single color value. A user can set a color well’s value by dragging a color to it or by clicking the color well and using the color panel that appears. A color panel contains several color pickers that let the user select a specific color. You can choose which color pickers are displayed and add new ones. See [Choosing the Color Pickers in a Color Panel](Choosing%20the%20Color%20Pickers%20in%20a%20Color%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44telkciffeershivca) and [Adding Custom Color Pickers to a Color Panel](Adding%20Custom%20Color%20Pickers%20to%20a%20Color%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg44tglkciffeershivca).

NSColorWell is an NSControl for selecting and displaying a single color value. An example of an NSColorWell object (or simply color well) is found in NSColorPanel, which uses a color well to display the current color selection. A color well is available from the Palettes panel of Interface Builder.

An application can have one or more active color wells. You can activate multiple color wells by invoking the `activate:` method with `NO` as its argument. When a mouse-down event occurs on a color well’s border, it becomes the only active color well. When a color well becomes active, it brings up the color panel also.

The `mouseDown:` method enables a color well to send its color to another color well or any other subclass of NSView that implements the NSDraggingDestination protocol.

NSColorPanel provides a standard user interface for selecting color in an application. It provides a number of standard color selection modes, and, with the NSColorPickingDefault and NSColorPickingCustom protocols, allows an application to add its own color selection modes. It allows the user to save swatches containing frequently used colors. Once set, these swatches are displayed by NSColorPanel in any application where it is used, giving the user color consistency between applications. NSColorPanel enables users to capture a color anywhere on the screen for use in the active application, or to drag a color from the color panel into an application view.

When you select a color in the panel, NSColorPanel sends a `changeColor:` message to the first responder. It also sends its action message (set by `setAction:`) to its target object (set by `setTarget:`), provided that neither the action nor the target is `nil`. NSColorPanel also sends its action to its target whenever you select a color in the color panel.

An application has only one instance of NSColorPanel, the shared instance. Invoking the `sharedColorPanel` method returns the shared instance of NSColorPanel, instantiating it if necessary.

You can put NSColorPanel in any application created with Interface Builder by adding the “Colors...” item from the Menu palette to the application’s menu.

The NSColorList class provides an API for managing custom color lists. The NSColorPanel methods `attachColorList:` and `detachColorList:` let your application add and remove custom lists from the NSColorPanel object's user interface. For more information, see [About Color Lists](About%20Color%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tolkciffeqssfireq).

NSColorPanel dynamically loads NSColorPicker objects from the following directories:

- `~/Library/ColorPickers/`
- `/Local/Library/ColorPickers/`
- `/System/Library/ColorPickers/`

[Next](Choosing%20the%20Color%20Pickers%20in%20a%20Color%20Panel.md)[Previous](Using%20the%20System%20Control%20Tint.md)

