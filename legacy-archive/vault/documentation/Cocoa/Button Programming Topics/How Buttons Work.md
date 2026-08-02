---
title: Button Programming Topics
apple_id: 10000019i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Button/Concepts/HowButtonsWork.html
archived_at: '2026-07-15T07:11:33.108908Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Button Programming Topics](Introduction%20to%20Buttons.md)


[Next](Types%20of%20Button.md)[Previous](Introduction%20to%20Buttons.md)

# How Buttons Work

Buttons follow the target-action design pattern. A button is a user interface object that sends an action message to a target when clicked. For more information on this design pattern, see [Target-Action](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Target-Action/Target-Action.html#//apple_ref/doc/uid/TP40010810-CH12) in _[Concepts in Objective-C Programming](../../General/Concepts%20in%20Objective-C%20Programming/About%20the%20Basic%20Programming%20Concepts%20for%20Cocoa%20and%20Cocoa%20Touch.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmjq)_.

Most of the button’s work is handled by the `NSButtonCell` class. An `NSButtonCell` instance sends its action message to its target once if its view is clicked and it gets the mouse-down event, but can also send the action message continuously as long as the mouse is held down with the cursor inside the button cell. The button cell can show that it’s being pressed by highlighting in several ways—for example, a bordered button cell can appear pushed into the screen, or the image or title can change to an alternate form while the button cell is pressed.

An `NSButtonCell` object must work with an instance of a subclass of `NSControl`. If you need one button, such as a push button, use an `NSButton` object that contains a single `NSButtonCell` instance. If you need a group of related buttons, such as a group of switches or radio buttons, use an `NSMatrix` object that contains several `NSButtonCell` instances.

`NSButton` and `NSMatrix` both provide a control view. However, while `NSMatrix` requires you to access the `NSButtonCell` objects directly, most of `NSButton`’s methods are “covers” for identically declared methods in `NSButtonCell`. (In other words, the implementation of the `NSButton` method invokes the corresponding `NSButtonCell` method for you, allowing you to be unconcerned with the `NSButtonCell` object’s existence.) The only `NSButtonCell` methods that don’t have covers relate to the font used to display the key equivalent, and to specific methods for highlighting or showing the `NSButton`’s state (these last are usually set together with `NSButton`’s [setButtonType:](https://developer.apple.com/documentation/appkit/nsbutton/1524983-setbuttontype) method).

[Next](Types%20of%20Button.md)[Previous](Introduction%20to%20Buttons.md)

