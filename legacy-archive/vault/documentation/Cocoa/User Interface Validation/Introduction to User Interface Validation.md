---
title: User Interface Validation
apple_id: 10000040i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-07-10'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UIValidation/UIValidation.html
archived_at: '2026-07-15T07:20:57.310150Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Implementing%20Validation.md)

# Introduction to User Interface Validation

The protocols [NSUserInterfaceValidations](https://developer.apple.com/documentation/appkit/nsuserinterfacevalidations) and [NSValidatedUserInterfaceItem](https://developer.apple.com/documentation/appkit/nsvalidateduserinterfaceitem) provide a standard way to validate user interface items—that is, to set their state as appropriate for the current application context (for example, to disable the Paste menu item if there is no suitable data on the pasteboard).

You should read this document to learn how to implement user interface item validation and how to extend the user interface validation protocol.

For more information about other ways to validate menus and pop-up lists, see _[Application Menu and Pop-up List Programming Topics](../Application%20Menu%20and%20Pop-up%20List%20Programming%20Topics/Introduction%20to%20Application%20Menus%20and%20Pop-up%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazte2i)_.

[Implementing Validation](Implementing%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3denryfvjvomi) describes how to use the `NSUserInterfaceValidations` and _NSValidatedUserInterfaceItem_ protocols to validate user interface items.

[Implementing a Validated Item](Implementing%20a%20Validated%20Item.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42dklkciffekqkjivcq) describes you can implement an item that uses the validation protocol to determine its state, and how to extend the `NSUserInterfaceValidations` protocol to provide custom user interface item validation.

[Next](Implementing%20Validation.md)

